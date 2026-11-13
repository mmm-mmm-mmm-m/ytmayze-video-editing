#!/usr/bin/env python3
"""Read-only inventory of EffectCraft v1 animation presets.

Prints JSON to stdout. Never imports effects, runs expressions or modifies files.
Time units are not inferred: provide --ticks-per-second for seconds, and --fps
for frame coordinates. A last key time is an extent, not a clip duration.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys


def positive_fraction(value):
    try:
        number = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError('Use a positive number or rational timebase/frame rate.') from error
    if number <= 0:
        raise ValueError('Timebase and frame rate must be positive.')
    return number


def inspect(path, ticks_per_second=None, fps=None):
    if path.suffix.lower() != '.ecpreset' or path.name.startswith('._'):
        raise ValueError('Inspect a native .ecpreset, not a project or sidecar.')
    raw = path.read_bytes()

    def invalid_constant(value):
        raise ValueError('Nonfinite JSON number: ' + value)

    data = json.loads(raw, parse_constant=invalid_constant)
    if not isinstance(data, dict) or type(data.get('effectcraftAnimationPreset')) is not int or data['effectcraftAnimationPreset'] != 1:
        raise ValueError('Unsupported animation-preset marker; inspect its format separately.')
    effects, properties = data.get('effects', []), data.get('properties', [])
    if not isinstance(effects, list) or not isinstance(properties, list):
        raise ValueError('Effects and properties must be arrays.')
    channels, expressions, times = [], [], []

    def walk(node, prefix):
        if not isinstance(node, dict):
            raise ValueError('Property/effect nodes must be objects.')
        match = str(node.get('match', node.get('name', '(unnamed)')))
        current = prefix + [match]
        if node.get('expression'):
            expressions.append('/'.join(current))
        keys = node.get('keys', [])
        if not isinstance(keys, list):
            raise ValueError('Keyframes must be an array.')
        if keys:
            key_times = []
            for key in keys:
                if not isinstance(key, dict) or type(key.get('time')) is not int:
                    raise ValueError('This inspector supports integer native key times only.')
                key_times.append(key['time'])
            times.extend(key_times)
            channels.append({'path': '/'.join(current), 'key_count': len(keys),
                             'first_key_tick': min(key_times), 'last_key_tick': max(key_times)})
        children = node.get('children', [])
        if not isinstance(children, list):
            raise ValueError('Property children must be an array.')
        for child in children:
            walk(child, current)

    for group_name, group in [('effects', effects), ('properties', properties)]:
        for node in group:
            walk(node, [group_name])
    bounds = [min(times), max(times)] if times else None
    result = {'file': str(path), 'name': data.get('name'),
              'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
              'format_marker': 1,
              'effect_order': [e.get('match', e.get('name')) for e in effects],
              'animated_channels': channels, 'expressions_present': expressions,
              'key_time_bounds_ticks': bounds,
              'ticks_per_second': str(ticks_per_second) if ticks_per_second else None,
              'fps': str(fps) if fps else None,
              'validation_scope': 'Partial structural inventory, not full schema validation; no native import, render or creative acceptance.'}
    if bounds and ticks_per_second:
        seconds = [Fraction(t, 1) / ticks_per_second for t in bounds]
        result['key_time_bounds_seconds_exact'] = [str(t) for t in seconds]
        if fps:
            result['key_time_bounds_frames_exact'] = [str(t * fps) for t in seconds]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', type=Path)
    parser.add_argument('--ticks-per-second')
    parser.add_argument('--fps')
    args = parser.parse_args()
    try:
        ticks = positive_fraction(args.ticks_per_second) if args.ticks_per_second else None
        fps = positive_fraction(args.fps) if args.fps else None
        if fps and not ticks:
            raise ValueError('--fps requires an explicit --ticks-per-second.')
        paths = sorted(p for p in args.path.glob('*.ecpreset') if not p.name.startswith('._')) if args.path.is_dir() else [args.path]
        if not paths:
            raise ValueError('No native presets found.')
        reports = [inspect(p, ticks, fps) for p in paths]
    except (OSError, ValueError, TypeError, KeyError) as error:
        print(str(error), file=sys.stderr)
        return 2
    print(json.dumps({'presets': reports}, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

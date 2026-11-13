# EffectCraft edit integrity

Read this when changing an EffectCraft project, not for a prose-only review.

## Current state is the source

Resolve the user-designated current version and whether newer user edits exist in the open app. Do not replace them with a stale disk snapshot. If an unsaved state cannot be captured safely, resolve that before creating a revision from disk. Do not open/close another project in a way that discards unsaved work.

Create a named editable revision, leaving source media and the original project intact. Preserve dimensions, frame rate, color/audio settings and selected composition unless the task changes them. Discover the installed editor interface/CLI and current schema instead of assuming a historical binary path or project structure.

## Verify the allowed change

Before a programmatic change, capture the source project hash and relevant properties: composition/duration, layer identities, in/out points, source references/offsets, speed/time maps, transforms, effect keys, audio levels and links. Use a deep copy. Define the permitted property changes narrowly enough for this pass. Reparse the output and compare outside those properties; a typography task should not alter effect keys or timing, and a click-level task should not alter note audio or drag gestures.

Preserve the distinction between source time, composition time, layer-local keyframe time and asset pre-roll. Use the project's timebase and actual fps. Do not mix decimal seconds and HH:MM:SS:FF. State whether frame ranges include or exclude their end, and verify their durations. Quantize deliberately, not by repeatedly rounding intermediate values.

For an authorized ripple, identify everything that travels with the content: camera, screen, source audio, editorial sounds, captions, pumps, overlays, adjustment layers and their keys/parents. Long shared layers crossing the edit need specific handling, not a blind bulk shift. Re-map downstream events after the move. For a one-frame gap repair under locked timing, use suitable adjacent media/handles without moving the rest of the timeline; do not conceal a gap by an arbitrary timing change.

Keep effects near the layers/sections they affect, ordinary edit layers accessible, and composites grouped where useful. Do not lock layers or discard muted/hidden media merely as tidying. A hidden caption or older source may still be intentionally retained. Cleanup needs its own authorized scope and a way to recover.

## Review proportional to the change

Confirm required media are reachable before diagnosing a black render as a creative gap; Saint Alien once lost hundreds of media references when the external drive disconnected. Do not rewrite paths to invented substitutes or relink an unrelated file. Keep unaffected work possible and identify the unavailable source.

Render a short native preview when authorized and useful, covering the changed range plus its seams. Check for missing pictures/audio, exposed edges, timing drift and clipped cue tails. A structural diff or full decode supports an integrity claim, not subjective acceptance. For audio-sensitive edits, compare protected material and listen to the full local context; report listening as pending when it did not happen.

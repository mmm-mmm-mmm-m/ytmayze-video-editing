---
name: "ytmayze-reactive-vfx"
description: "Design or repair beat- and action-reactive VFX for music-production tutorials inspired by @ytmayze’s editing style, including pumps, sustained bass motion, slides, glow and distortion. Use when reaction timing or the movement’s relationship to sound matters."
---

# @ytmayze Reactive VFX

Make the screen express the sound’s character. Correct timing and readable action come before intensity. The recurring failure is random or twitching pumps on claps, speech or empty space, sometimes after transferring a known-good treatment across cuts.

## Map events in the current edit

Inspect the audible kick/bass/slide and visible action that should cause each reaction. Separate kick/bass events from clap/snare hits, sustained tails, speech and existing editorial SFX. A mixed waveform peak is not sufficient evidence of a kick. Use isolated audio/events when available and confirm in context; label uncertain anchors.

Map each source event through the current clip’s trim, placement and speed. For a simple forward constant-rate clip:

`output_time = clip_start + (source_event - source_in) / playback_rate`

Include events only inside that clip’s actual source interval. Use piecewise mapping for skips and retimed clips; use the actual time map for ramps, reverse or freeze sections. Do not extrapolate one beat grid across a removed bar. Quantize at the composition’s real frame rate when the editor requires frames, keeping exact/rational timing until that conversion.

Align the effect’s perceived impact/peak, not merely the layer’s in-point. If an asset’s impact is three frames after its start, begin it three frames before the event. Keep anticipation/decay inside the intended region and inspect cut boundaries for clipping or spillover.

## Choose the movement

- Punchy kick/short bass: a decisive, controlled expansion or tilt with clean recovery may fit.
- Long growling 808: let motion follow its body and release; a smoother expansion, sustained pressure or slower recovery often fits better than repeated rapid punches.
- Slide: visualize the direction and duration with an appropriate move/warp, rather than treating its tail as another kick.
- Distortion/bitcrush: a graded change in crunch, saturation or texture can express the knob’s audible change.

These are starting options, not mandatory presets or verified sonic facts about a new clip. Confirm them against the current audio. Reuse a current approved example’s shape when appropriate, then remap its timing and adapt it to the new bass. Inspect and replace/disable conflicting old reactions instead of stacking two pump systems. Match camera and screen energy deliberately; avoid accidental competing motion.

Keep the notes, playhead or relevant action visible so the viewer can understand why the picture reacts. Use overscan/margins for tilt and expansion; check for exposed edges, UI leaks, motion reversal, oscillation and a delayed visual peak. Speech and quiet recovery can remain still.

## Verify and reuse

Preserve approved cuts/audio and work in an editable copy. Audit the whole affected playback, especially the first hit, skipped bars, sustained notes, last hit and the return to speech. Watch and listen together where possible. After moving/rippling a section, recheck the event map and all related effects.

Separate reusable motion shape from this timeline’s event anchors; do not freeze old timestamps, one BPM or a layer ID into a general gesture. For native packaging, library lookup and transfer checks, use `ytmayze-effect-presets` when available. Event choice, musical adaptation and readable reactive motion stay here. Read [reactive examples](references/examples.md) for prior corrections.

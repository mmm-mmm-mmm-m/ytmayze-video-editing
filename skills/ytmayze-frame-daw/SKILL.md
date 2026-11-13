---
name: "ytmayze-frame-daw"
description: "Crop and animate DAW footage for music-production tutorials inspired by @ytmayze’s editing style, including mouse/playhead tracking, webcam placement, and vertical reframing. Use when the demonstrated action or musical playback needs clearer framing."
---

# @ytmayze DAW Framing

Frame what the viewer needs to see now: the note being entered, control being changed, or musical playback being heard. The established look is focused piano-roll/playlist footage with little unused DAW chrome. Tightness serves legibility; an extreme zoom that loses the action fails the style.

## Find the visual subject

Inspect the complete action, including its last click or drag release. Mark target positions at changes of direction, high/low notes, selection edges and the end of the gesture. During playback, follow the playhead and enough surrounding notes to explain the sound. Do not follow the pointer automatically when it is idle or crossing irrelevant UI.

Keep piano keys when they orient the notes. Hide velocity lanes, toolbars, browser panels and margins when unused; reveal them when velocity, browsing, scale selection or another control is the actual demonstration. A plugin/sampler can be shown as a clean, intentional insert instead of a full desktop view. Necessary UI outranks a rigid “no UI” rule.

## Compose and move

Choose a crop or small set of framing anchors that holds the relevant targets with margin. Reposition the webcam when it obscures notes or controls; start from the user’s existing preset, headroom and gaze. Moving the camera is preferable to hiding the musical action. Do not mirror the performer by default.

Animate toward the next useful area smoothly, with a stable hold when nothing warrants movement. Prefer a few purposeful moves over chasing every pointer tremor. Keep intentional motion distinct from a beat-reactive pump. If a crop cannot hold both context and a moving target, widen or pan; do not keep increasing zoom.

For adjacent clips that continue one action, match the outgoing and incoming framing state. Check interpolation between keys, not just endpoints: equal-looking keys can still drift, overshoot or briefly reveal the frame edge. Track until the action actually ends; an audible final note click with its target offscreen is a failure.

## Vertical layout

Use the current Shorts camera preset if available, with camera above a useful DAW area. Reframe the actual piano roll to fill its region and leave performer headroom. Give the notes enough width to read. Avoid blurred fill as the automatic solution when better scaling/reframing of the source solves the space. Composite constructions such as the laptop keyboard may be grouped; ordinary camera and screen layers should remain directly adjustable.

Keep reusable portrait and landscape layouts distinct, named by format/placement and saved in discoverable locations. Preserve the previous useful version when revising geometry. Use `ytmayze-effect-presets`, if available, when packaging or adapting a layout rather than carrying old coordinates into a new composition.

## Check the result

Preserve cuts, source timing and audio unless the current task authorizes changes. Apply project edits in an editable copy. Verify the target stays visible and unoccluded throughout every move, at the last gesture and across clip boundaries. Review the beginning/middle/end and the motion between them; sample more densely where a target approaches an edge. Watch playback for bobbing, snaps and direction reversals. Report when framing is inferred from a specification rather than observed in footage.

For style precedents and tricky exceptions, read [framing examples](references/examples.md). Exact crop coordinates and old layer numbers are project details, not presets for a new recording.

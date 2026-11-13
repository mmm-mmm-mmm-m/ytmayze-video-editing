# Usage

## What this is for

ytmayze video editing is an experimental set of skills for agent-assisted refinement of music-production tutorials. The source tutorials were rough-cut by a person first, then improved through many directed iterations with an agent. Reliable raw-footage cutting and complete tutorials from one prompt remain untested.

The workflow is most useful when you can give specific direction and review short passages. The agent does not start with your creative taste. Tell it what matters, what to protect, and what is not working. Leave room for musical phrases to resolve and for jokes to breathe; an edit can feel rushed even when the visuals are busy.

## Before a pass

1. Make a rough cut and save a working copy of the project.
2. Give the agent the project and the media it needs, or explain the tools it can access.
3. Choose one short passage and state exact in and out timecodes.
4. Describe the desired result in observable terms. List protected material, such as cuts, audio, source offsets, gestures, webcam placement, or wording.
5. Attach style references, drawings, images, audio, or meme clips when they help. Say whether the agent may find missing material and define the allowed sources and limits.
6. Ask for a short reviewable result. Listen and watch it yourself, then give concrete notes for the next iteration.

## Example prompt

> Use `$ytmayze-video-editing` on my rough-cut music tutorial. Edit **01:12–01:28** only. Make the piano-roll note entry easier to follow and keep the full mouse gesture visible. Preserve all cut points, music timing, source offsets, and webcam placement. Follow the attached framing sketch. You may use only the attached assets; do not search for or download media. Make a named editable copy, then show me this passage before applying the same treatment elsewhere. Tell me which project and media you inspected and what you could not verify.

For Claude Code, invoke `/ytmayze-video-editing` in place of `$ytmayze-video-editing`. The skill may route a focused task to a companion skill, such as `ytmayze-frame-daw` for framing or `ytmayze-design-sound` for action-matched foley.

## Directing the iteration

Review the returned passage in context. Useful feedback names a moment and an adjustment: “At 01:19, keep the cursor visible until the last note lands,” or “Let the chord ring for another beat before the joke.” You can ask the agent to explain a choice, revise only that passage, or prepare another named copy. Do not assume that a plan, screenshot, or structural check confirms native playback, sync, mix, or creative quality.

Sound effects, DAW framing, musical pacing, and contextual entertainment are focus areas, not promised results. A reasonable request may still need several rounds—or may not fit the available footage and tools.

## Tool access and optional HyperFrames

The agent needs access to an editor, supported project interface, or other media tools to change a project. With no editor access, it can still review supplied material or provide a cue sheet and edit specification. Verify changes in the target editor and listen to the result.

HyperFrames is optional. HyperFrames inserts require that runtime and its guidance to be installed separately; this repository does not bundle a renderer. Other editor-specific capabilities also depend on the tools actually available to the agent.

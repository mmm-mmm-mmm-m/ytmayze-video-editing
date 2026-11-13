# Reactive timing examples

A long bass tail calls for a movement shaped around its body and release; rapid identical pulses can misrepresent it. A large mixed-waveform peak may be a clap or speech, so verify the sound before assigning a kick reaction.

Worked timing example, using source and output frames at the same constant frame rate: source range [600,720) starts at output 0. A bass hit at source 612 lands at output 12. The next clip starts at source 780/output 120, so source hit 792 lands at output 132. Source hit 732 was removed. If the effect peaks three frames after its start, start the two effect instances at output 9 and 129. Use the current edit’s time map for retiming, reverse or ramps.

Reuse the motion shape, then replace the event map and check the playhead remains visible.

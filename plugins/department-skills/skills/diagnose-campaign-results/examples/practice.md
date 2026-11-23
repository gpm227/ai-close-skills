# Trace a campaign before recommending a test

**Request.** “Which variant deserves another run? Report as of June 10 at 12:00 UTC. Measure post-delivery events within seven full days. Count one recipient per variant. A booked meeting is an identified booking linked to this campaign.”

**Delivery export, UTC.** All dates are June 2026; all timestamps 09:00. A failed final delivery is a bounce.

| Person | Variant | Sent | Final delivery |
| --- | --- | --- | --- |
| p1 | A | 1 | delivered June 1 |
| p2 | A | 1 | delivered June 1 |
| p3 | A | 1 | bounce June 1 |
| p4 | B | 1 | delivered June 1 |
| p5 | B | 1 | delivered June 1 |
| p6 | B | 8 | delivered June 8 |

**Event export.** Jun 2: p1 human-positive r1, p1 human-positive r1 (duplicate), p2 automated out-of-office r2, p4 human-negative r3. Jun 3: p1 booked m1 from reply, p5 booked m2 directly via campaign link. Jun 9: p6 human-positive r4. All event timestamps 09:00. No held-meeting data supplied.

## Worked result

| Mature cohort | Delivered / attempted | Human responders / delivered | Positive / delivered | Booked people / delivered | Held |
| --- | --- | --- | --- | --- | --- |
| A | 2/3 (66.7%) | 1/2 (50%) | 1/2 (50%) | 1/2 (50%) | unknown |
| B | 2/2 (100%) | 1/2 (50%) | 0/2 (0%) | 1/2 (50%) | unknown |

The A bounce is from an attempt old enough to assess. Omit p6 from the mature comparison and show its 1/1 delivered, one provisional positive separately. A single recipient generated r1 twice. Include p5's direct meeting in booked people and exclude it from conversion *from a reply*. No variant is a defensible winner from two delivered people per arm. Investigate the failed delivery independently.

**Next test.** Keep the list criteria, sender, schedule, subject and body fixed; randomize eligible recipients to the original CTA or a revised CTA. Judge booked recipients / delivered recipients after seven days, with bounce and unsubscribe counts monitored. If enrollment closes June 20 at 09:00 UTC, read June 27 at 09:00 UTC or later. Agree the minimum sample and decision threshold before enrollment. Until then the result is exploratory.

## Different case

“Same export, but each variant has only the count of outbound messages. Several people got three messages and the calendar has no campaign IDs.” Show message-level delivery with the available data. Recipient reply rates and attributable meetings are unknown. Ask for a deduplicated recipient export and meeting attribution; do not label unknown meetings zero.

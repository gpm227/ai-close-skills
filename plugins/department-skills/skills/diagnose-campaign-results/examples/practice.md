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

## Where the campaign lost people

| Mature cohort | Delivered / attempted | Human responders / delivered | Positive / delivered | Booked people / delivered | Held |
| --- | --- | --- | --- | --- | --- |
| A | 2/3 (66.7%) | 1/2 (50%) | 1/2 (50%) | 1/2 (50%) | unknown |
| B | 2/2 (100%) | 1/2 (50%) | 0/2 (0%) | 1/2 (50%) | unknown |

The A bounce is from an attempt old enough to assess. Omit p6 from the mature comparison and show its 1/1 delivered, one provisional positive separately. A single recipient generated r1 twice. Include p5's direct meeting in booked people and exclude it from conversion *from a reply*. No variant is a defensible winner from two delivered people per arm. Investigate the failed delivery independently.

**Next test.** Keep the list criteria, sender, schedule, subject and body fixed; randomize eligible recipients to the original CTA or a revised CTA. Judge booked recipients / delivered recipients after seven days, with bounce and unsubscribe counts monitored. If enrollment closes June 20 at 09:00 UTC, read June 27 at 09:00 UTC or later. Agree the minimum sample and decision threshold before enrollment. Until then the result is exploratory.

## Different case

“Our dashboard shows 110 messages sent for A and 60 for B this week. Several people got three touches. The calendar has no campaign IDs. Which one should we scale?”

| This week's evidence | A | B |
| --- | ---: | ---: |
| Attempted messages | 110 | 60 |
| Confirmed delivered messages | Unknown | Unknown |
| Unique delivered people, responders and attributable bookings | Unknown | Unknown |

Hold the scaling decision. The 50-message difference measures send volume. Ask campaign operations for message ID, recipient ID, variant, sent time and final delivery status. Check that each attempted message has one final outcome, then calculate delivered messages divided by attempted messages for each variant. To judge meetings, also obtain campaign-linked booking IDs and timestamps.

## Read a campaign by signal

This separate fictional pilot observes all activity through the end of the agreed follow-up window. Each account has one assignment. Bookings and qualifications are linked to that assignment. The team qualifies a held meeting when the buyer confirms a recurring process, the owner and a specific result to improve.

| Account / primary signal at assignment | Delivered recipients | Positive responders | CRM booking and disposition |
| --- | --- | --- | --- |
| A1 / branch opening | P1, P2 | P1, P2 | M1 held with both people; all three criteria recorded |
| A2 / branch opening | P3 | none | M2 booked directly; buyer did not attend |
| A3 / branch opening | none; P4 bounced | none | none |
| A4 / relocation | P5 | P5 | M3 held; owner has not recorded qualification |
| A5 / missing tag | P6 | none | none |

**Request.** Which signals have generated qualified calls? Show account reach, contacts per positive responder, and the meeting evidence behind the answer.

**Check.** For branch openings, two of three assigned accounts were reached. Three people received the draft and two responded positively, or 1.5 delivered contacts per positive responder. Two meetings were booked, one was held and one was qualified: one qualified account out of three assigned. M1 counts once. For relocation, one of one accounts was reached. One delivered contact replied, and M3 remains pending after the meeting. For the missing tag, one of one accounts was reached, and no positive response makes contacts per positive responder undefined. Preserve the unknown category. The groups observed here cannot establish that mentioning a branch opening caused a qualified call.

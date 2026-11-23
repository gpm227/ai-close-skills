---
name: improve-skill
description: "Investigates a mistake a skill made, finds the cause, and prepares a tested fix for the team lead to approve. Use when a skill got something wrong, an automatic check failed, or someone reports \"it did X again.\""
---

# Improve a skill

Plain AI fixes the one example in front of it. The fix is so specific it never fires again, or so broad it breaks three things that used to work.

## You'll need

- **The run.** Run ID, skill version, the input, and the output.
- **What it should have done,** with the source that proves it.
- **The check result and any comments,** kept separate. No comment doesn't mean it passed.

If something is missing, ask the person who reported it for the one missing item.

## Steps

1. Rerun the original input on the released version. Confirm the mistake happens.
2. Find the cause: bad input, an unclear standard, a gap in the instructions, or a wrong check.
3. If the standard itself is unclear, ask the lead to decide. Don't decide for them.
4. Make the smallest change that fixes the general case, not just this example.
5. Add this case as a regression test.
6. Keep one unseen test case aside. Don't use it while writing the fix.

## What you get back

A change request: old behavior, new behavior, the exact rule changed, regression results, risks, and the proposed version number. The lead decides whether it ships.

After approval, a second person runs the unseen case in a fresh session. Record the version and result.

## The trap

Period Report compared May 1 to 18 with all of April. The narrow fix is "when the cutoff is the 18th, use 18 days." The real fix is "compare the same number of elapsed days in both months, capped at the shorter month's end." Test it on the 31st.

## Check it

- The original failing case now passes.
- Every earlier regression still passes.
- The unseen case was not used during the fix.

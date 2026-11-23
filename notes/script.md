# Speaker script — CSR leadership, spillovers, and first-mover advantage

Target 30–45 min. Written at roughly 140 words per minute. Timing per slide is
indicative; the `[PAUSE]` marks are where to stop and let the room catch up.

Conventions: **bold** = stress it. *Italic* = the slide shows it, don't read it
out. `[…]` = stage direction, not spoken.

---

## Slide 1 — Title · 40 s

Good afternoon. I'm going to present Michael Kopel's 2021 paper, "CSR
leadership, spillovers, and first-mover advantage," from *Decisions in
Economics and Finance*.

The paper asks a question that sounds like a management-seminar question but
turns out to have a clean theoretical answer: **does moving first on corporate
social responsibility pay?**

I'll give you the model, the three results, and then one thing I computed myself
that I think is the most interesting part — and which the paper doesn't state.
Then I want to open it up, because there are at least three places where I think
the model can be pushed.

---

## Slide 2 — The question · 60 s

Here's the setup in one sentence. A firm invests in socially responsible
activities *before* its competitor does. Does it earn more as a result?

Kopel calls that firm the **CSR leader**. And he's very precise about what a
first-mover advantage means. It means exactly this: the leader's equilibrium
profit exceeds the follower's.

[PAUSE]

Notice what that is *not*. It is not "the leader invests more in CSR." Those are
two different comparisons, and one of the things I want you to take away is that
they don't coincide. There's a whole region of the parameter space where the
leader invests more and still earns less.

---

## Slide 3 — Why the question is open · 70 s

Before the paper, the literature had two camps, and they were both arguing from
cases rather than from a model.

The optimistic camp — Tetrault Sirsly and Lamertz — say a CSR leader *can* keep
its advantage, but only under a condition: the initiative has to be central to
the firm's mission, visible to stakeholders, and generate firm-specific benefits
beyond those of a public good.

The skeptical camp — Reinhardt, and Vogel in *The Market for Virtue* — say that
condition is almost never met. CSR is hard to keep specific to one firm's
strategy, so whatever advantage you get, you lose.

And here's the gap Kopel is filling: the strategy literature on first- versus
second-mover advantage is enormous, and almost none of it is about CSR.

---

## Slide 4 — What practitioners were told · 45 s

This is the quote I find most useful for framing. From *The Economist* in 2008,
quoted in the paper:

*[read the quote]*

"One large consultancy advises its big clients to be number two or three on
corporate responsibility rather than number one."

[PAUSE]

That's not a value judgement. That's an empirical claim about an equilibrium —
and that's precisely the kind of claim a formal model can test.

---

## Slide 5 — What the paper actually does · 75 s

So Kopel builds a duopoly model and asks when the leader wins.

Now, one thing to flag early, because it caught me out when I first read it. The
framing on page 490 sets Tetrault Sirsly and Lamertz *against* the skeptics. If
you only read the introduction, you'd expect the paper to pick a side.

But the conclusion doesn't do that. On page 502 Kopel writes that his study
"provides support for the claims in conceptual papers like Tetrault Sirsly and
Lamertz, Burke and Logsdon, and Reinhardt" — he groups all three **together**.

So the paper **formalises** Tetrault Sirsly and Lamertz's condition rather than
refuting it. They said an advantage is possible if the benefit is firm-specific.
Kopel agrees. What he adds is a magnitude — and the magnitude is the surprise.

---

## Slide 6 — Two parameters · 50 s

Everything in this paper lives in a two-dimensional space.

**Gamma** is competition intensity — how substitutable the two products are.
Zero means they're independent; higher gamma means closer substitutes and
tougher competition.

**Theta** is the spillover. How much of the leader's CSR benefit leaks across to
the rival. Zero means the leader keeps all of it; one means the rival gets the
full benefit for free.

Every result is a statement about some region of the gamma–theta plane. If you
hold onto nothing else, hold onto those two letters.

---

## Slide 7 — What CSR is, formally · 55 s

Formally, firm *i* buys a CSR level *s-i* at a cost of *s-i* squared. What it
buys is an increase in consumers' willingness to pay — a shift in the demand
intercept.

So CSR here is **vertical** differentiation. It's quality-like: everybody
prefers more of it, other things equal. Gamma, by contrast, is **horizontal**
differentiation — taste-based distance between the products.

[PAUSE]

I want to flag this now because it bounds everything that follows. A conclusion
about an appropriable *demand shift* does not automatically apply to CSR
modelled as a cost, or as an emissions cap, or as a delegation parameter. I'll
come back to that near the end.

---

## Slide 8 — Appropriability · 70 s

So what is theta, economically? It's the inverse of **appropriability**.

Kopel borrows the definition from Burke and Logsdon: specificity is "the firm's
ability to capture or internalize the benefits of a CSR programme, rather than
simply creating collective goods which can be shared by others in the industry,
community or society at large."

And he gives two examples that I think are better than the formal definition.
Patagonia sustained its differentiation and defended a premium segment. StarKist
announced dolphin-safe tuna procurement, and — the paper's words — competitors
"imitated this policy almost immediately."

[PAUSE]

My reading of those examples is that appropriability doesn't come from the CSR
act at all. It comes from an asset the rival doesn't have — a brand position, a
location, a process. The CSR action is copyable. The asset isn't.

---

## Slide 9 — The asymmetry is assumed · 65 s

Now, an assumption I want to put on the table early, because I think it's the
most questionable thing in the paper.

The general demand system has two spillover parameters, one for each firm. Kopel
sets the leader's to **zero** and the follower's to theta. So the follower
free-rides on the leader, and the leader gets nothing back.

His justification is on page 494: it's plausible that theta-one is at most
theta-two, "because the CSR follower can free ride on the CSR efforts of the
leader."

[PAUSE]

That's reasonable as far as it goes. But notice: the paper's question is *who
benefits from whom*. Assuming the leader benefits by exactly zero is not a
neutral modelling choice with respect to that question. Hold that thought — it's
the first thing I want to discuss at the end.

---

## Slide 10 — Demand and profits · 60 s

Here's the machinery. Differentiated Bertrand duopoly, constant unit cost *c*,
reservation price *a*.

The leader's inverse demand has its own CSR term. The follower's has its own CSR
term **plus theta times the leader's**. That's the whole spillover, right there
in the second equation.

Profits are revenue minus cost minus the CSR investment, which is quadratic.

[PAUSE — point at the second equation]

One detail that matters later: theta *adds* to the follower's demand. It does
not *subtract* from the leader's. The leader's demand shift is *s-one* whatever
theta is. I'll come back to that on slide 20, because it changes how you're
allowed to phrase the result.

A word on how this gets solved, since it's three stages and you might reasonably
want to know where the closed forms come from. You invert this system to get
direct demands, which is where the one-over-one-minus-gamma-squared terms come
in. You solve the two price first-order conditions simultaneously — that gives
prices as functions of both CSR levels. You substitute those into the follower's
profit and solve its first-order condition, which gives the reaction function on
the next slide. Then you substitute *that* into the leader's profit and solve
the leader's first-order condition. Everything comes out in closed form.

I've put the full equilibrium expressions on a backup slide if anyone wants to
see them.

---

## Slide 11 — Three stages · 55 s

The game has three stages. The leader picks its CSR level, and that level is
**observed**. Then the follower picks its own. Then both set prices
simultaneously. Solved backwards, as usual.

The commitment only has value because stage one is observed and locked in before
stage two. Take away the sequencing and the whole mechanism disappears.

[PAUSE]

And here's the second assumption to flag: **who leads is exogenous**. Kopel says
it explicitly — "in my paper the leader–follower structure is exogenously
given." Nobody in this model chooses to move first. That's going to look
uncomfortable once we see the results.

---

## Slide 12 — The hinge · 75 s

This is the hinge of the whole model, so let me slow down.

Take the follower's reaction function and differentiate it. The follower's CSR
falls when the leader's rises **if and only if** theta is below gamma over
two-minus-gamma-squared.

Below that threshold, CSR levels are strategic **substitutes**. The leader
invests more, the follower pulls back and free-rides. That's the story everyone
expects.

Above it, they become strategic **complements**. The leader's own incentive has
collapsed so far that the follower actually *raises* its CSR — in Kopel's words,
"to counterbalance this effect."

[PAUSE]

Look at the threshold itself for a second: gamma over two-minus-gamma-squared.
It's increasing in gamma. So the tougher the competition, the *more* spillover
the model can absorb before the strategic relationship flips. On my arithmetic
it's about 0.05 at gamma of 0.1 and about 0.59 at gamma of 0.8 — those are my
numbers, not the paper's. That's a wide range, and it's going to matter.

Remember this threshold. I'm going to come back to it at slide 22, because it is
the threshold that **does not** explain the main result — even though it looks
like it should.

---

## Slide 13 — Lemma 1 · 50 s

Let's start with the clean case. Set theta to zero. CSR is perfectly proprietary
— nothing leaks.

Lemma 1: with no spillovers, the leader invests more than the follower, **and**
the leader earns more. A genuine first-mover advantage.

So in the limiting case, the optimists are right. If you can fully protect your
CSR investment, leading pays.

---

## Slide 14 — The paper doesn't prove it · 60 s

But I want to be straight with you about the status of that result.

The paper's proof reads, in full: "The proof of the lemma follows from a simple
comparison is therefore omitted." That sentence has a typo in the original, and
that's the whole proof. Lemma 2 is omitted on the same grounds.

[PAUSE]

So I re-derived the model myself. I took equation one, inverted demand, solved
the price stage, solved the follower's stage, substituted, solved the leader's
stage — symbolically, in sympy — and checked Lemma 1 on a grid of thirty-nine
points across the admissible range of gamma. It holds everywhere I looked.

That's strong evidence. **It is not a proof.** I want to be clear about which of
the things I'm telling you today are proved, which are verified numerically, and
which are my own reading.

---

## Slide 15 — Three effects · 70 s

Why does competition affect CSR at all? Kopel decomposes it into three effects,
and this decomposition is the most useful thing in the paper for intuition.

The **markup effect** is negative. Tougher competition pushes prices toward
marginal cost, so each extra unit of demand you buy with CSR is worth less. That
hits both firms.

The **demand effect** is positive. When products are closer substitutes, a given
CSR investment shifts more demand. Also both firms — and Kopel states this for
the no-spillover case specifically.

The **strategic effect** is positive, and it hits the **leader only**. By
committing to high CSR, the leader induces the follower to cut its own.

[PAUSE]

Only the leader gets the third one. That asymmetry *is* the model.

And it's worth being precise about why the strategic effect is positive, because
it's a two-negatives story. More follower CSR hurts the leader — that derivative
is negative. And more leader CSR makes the follower retreat — that derivative is
also negative, as long as we're below the threshold from the last slide. The
product of two negatives is positive, which is what Kopel's footnote fourteen
states. I should say the paper gives only the sign of the product; splitting it
into the two factors is my reading, not his.

The consequence is that the leader **over-invests**. It buys more CSR than the
direct return alone would justify, because the investment is doing a second job:
it's suppressing the rival.

---

## Slide 16 — The U-shape · 75 s

Put those together and you get this picture.

*[the figure]* I plotted this myself from the verified equilibrium expressions
rather than copying the paper's figure — partly so I could annotate it, partly
so I could be sure the curve is the one I checked.

One thing to note before the shape: at gamma of zero the two curves coincide, at
one-third. So "the leader always invests more" holds for gamma strictly positive.

The solid line is the leader. At low competition the markup effect dominates, so
its CSR falls. Past gamma of about 0.532 the demand effect takes over and it
rises again — a U-shape. The dashed line is the follower, which has no strategic
effect, so it just declines all the way.

And notice the gap widens. Kopel's phrase is that the leader's advantage "can
not only be sustained, but made even larger" as products become more homogeneous.

One number worth having: the leader's turning point is at gamma of about 0.532.
I recomputed it and got 0.5319633, against the paper's 0.531963 — so that one
checks out to the precision it's printed at.

[PAUSE — point at the right edge]

Keep an eye on where that dashed line ends up. It reaches zero right at the
upper edge of the range the paper analyses. We'll come back to that on slide 25.

---

## Slide 17 — Let the rival benefit · 50 s

Now switch on spillovers. Raise theta above zero.

The two firms' incentives move in **opposite directions**. The derivative of the
leader's marginal return with respect to theta is negative. The follower's is
positive.

[PAUSE]

So — and this is my framing, not Kopel's — theta isn't a leak. A leak would just
waste something. This is a **transfer**: it takes incentive from the leader and
hands it to the follower. And it does that continuously, starting from theta
equals zero. There's no threshold you have to cross for it to begin.

---

## Slide 18 — Lemma 2 · 45 s

Lemma 2 is the paper's central result. A CSR leader achieves a first-mover
advantage **only if** the outcomes of its CSR efforts are highly specific to it —
that is, only if theta is, in Kopel's words, "quite small."

Otherwise the follower gets a **second-mover advantage**. It earns more than the
firm that went first and paid for it.

So the obvious question is: how small is "quite small"?

---

## Slide 19 — "In fact very low" · 35 s

Kopel flags this himself as the surprise of the paper. On page 491: "What is
surprising, however, is that the level of CSR spillovers for which a first-mover
advantage can be sustained is **in fact very low**."

[PAUSE]

And then he never puts a number on it. Nowhere in the paper is there a figure
for how low "very low" is. So I computed it.

---

## Slide 20 — How low · 85 s

At a moderate level of competition — gamma of 0.3 — the spillover rate has to
stay below **0.15 percent** for the leader to out-earn the follower.

[PAUSE — let that sit]

Zero point one five percent. The table gives the frontier across the range. At
gamma of 0.1 it's five in a hundred thousand. At gamma of 0.8 — near the top of
the range the model admits — it's still under ten percent.

This is my own calculation from the verified equilibrium profit expressions —
it's not a table in the paper.

One phrasing note, because I got this wrong at first and had to correct it.
It's tempting to turn this into a retention percentage — "the leader must keep
such-and-such a share of its benefit." That's **wrong**, for the reason I
flagged on slide 10: theta adds a benefit to the rival, it doesn't subtract one
from the leader. The defensible statement is a bound on the spillover *rate*.

Now, what does a spillover rate of 0.15 percent mean in practice? I'd argue it
means essentially nothing leaks. Not "the patent holds for a few years." Not "we
have a head start." Essentially nothing. And when you line that up against
Kopel's own examples — StarKist's procurement policy copied almost immediately —
the natural conclusion is that the condition is met rarely enough that the
default expectation should be no advantage.

That's also why the comparison to the Economist quote is interesting. The
consultancy advising clients to be number two or three was giving advice that
this model says is right for almost the whole parameter space.

---

## Slide 21 — The roles swap · 60 s

Push theta further and something stranger happens.

Lemma 3 gives two numerical thresholds — 0.202 and 0.229 — and they govern
*different firms*. Below the first, the follower's CSR declines in competition
while the leader's is U-shaped. Above the second, it's the other way round.

One caveat if anyone presses on this. Kopel's footnote fifteen defines those
thresholds by the sign of the derivative *at the endpoint*, at gamma-max. That
criterion can't see an interior hump, and when I swept it the follower's curve
is already non-monotone from about theta equals 0.190. So "monotone throughout"
below 0.202 is a bit stronger than the method supports.

Between them is a narrow band where **both** are U-shaped. And the figure Kopel
chooses to print, at theta equals 0.21, sits exactly inside that band.

*[the figure]* Here it is, plotted from the verified expressions. Both U-shaped
— and look which curve is on top. The **follower** is now the bigger investor.
The roles have completely swapped relative to the previous figure.

---

## Slide 22 — Three thresholds · 90 s

Here's the part I find most interesting, and it came out of a consistency check
rather than a content pass.

We've now met three different events. The first-mover advantage dying. The
leader ceasing to out-invest. And deterrence switching from strategic
substitutes to complements.

It's natural to assume these are roughly the same event. They are not. This is
all three plotted together — note the log scale.

[PAUSE]

At gamma of 0.3: the first-mover advantage dies at theta of 0.0015. The leader
stops out-investing at 0.0169. And deterrence doesn't switch until 0.157 — about
**one hundred and five times later**.

The ordering is strict at every gamma: the profit frontier is below the
investment frontier, which is below the deterrence switch.

Let me walk the three curves. The top one, dash-dotted, is the deterrence switch
— gamma over two-minus-gamma-squared, the threshold from slide 12. The middle
dashed one is where the leader stops out-investing the follower. The bottom solid
red one is where the first-mover advantage dies, and the shaded area underneath
it is the only region where the leader actually earns more.

Look at how thin that shaded region is, and remember the vertical axis is
logarithmic. On a linear axis it would be invisible for most of the range.

---

## Slide 23 — The mechanism isn't what it looks like · 90 s

So here's what that buys us.

The natural story — the one I would have told you, and the one I had written
down before I checked — is that spillovers wreck the leader's ability to deter
the follower, and that's why the advantage dies.

**The numbers rule that out.**

At the moment the first-mover advantage disappears, CSR levels are still
strategic substitutes. The follower still retreats when the leader invests. The
leader still invests more than the follower. Nothing about the deterrence
mechanism has broken.

[PAUSE]

So the right statement is this, and note the scope — I mean over the range where
the advantage is actually being lost, theta between about 0.0015 and 0.0169 at
gamma of 0.3: **the leader keeps deterring the follower, keeps out-investing it,
and still loses on profit.**

And that makes sense once you go back to the transfer-of-incentive framing from
slide 17 — which, to be clear, is my reading rather than a sentence of Kopel's.
The follower *receives* a demand shift it did not pay for. It does not take one
away from the leader; the leader's own shift is unchanged. That bites immediately, from theta equals zero. It doesn't need
the strategic relationship to invert — it's already decisive long before.

I think that's a sharper and more uncomfortable finding than "spillovers wreck
CSR leadership." It says the leader can be winning the strategic game and losing
the only game that counts.

And I want to be honest about where this came from, because it says something
about method. I didn't find it by reading the paper more carefully. I found it
by putting two numbers side by side that the paper never puts side by side —
the profit frontier, which I had computed, and the substitutes threshold, which
is stated in the text several pages earlier. Both were already in my notes. The
error was in the sentence connecting them, and it survived two rounds of
checking the notes against the paper, because the paper doesn't contain the
contradiction. It only appears when you check the notes against themselves.

---

## Slide 24 — What that does and doesn't establish · 60 s

Two caveats, because I don't want to oversell my own arithmetic.

What it **does** establish: the deterrence story cannot be the explanation.
Deterrence is intact when the advantage dies. That's a clean exclusion.

What it **does not** establish: that the transfer-of-incentive story is the only
remaining candidate. Ruling out one mechanism is not proving another. I'd want
the full comparative statics to make that claim properly.

And one more: the gap narrows sharply with competition. It's 940-fold at gamma
of 0.1, but only **six-fold** at 0.8. So "two orders of magnitude" is true up to
about gamma of 0.3 and I shouldn't state it generally.

---

## Slide 25 — Where the model stops · 80 s

Now something about the boundary of the model that I think is under-stated in
the paper.

The analysis requires gamma below 0.810736. Kopel justifies this in one line —
it keeps "the equilibrium of the game in the interior" and satisfies the
second-order conditions. It reads like housekeeping, and he doesn't say which
condition is actually binding.

I went looking. It isn't the second-order conditions — those fail at 0.83 and
0.93. It's the **follower's interiority at theta equals zero**: the follower's
CSR and its output reach zero *together* at exactly that point.

[PAUSE]

So gamma-max isn't a technical nuisance. It marks the point where the duopoly
would **collapse into a monopoly**. Which means the claim that the leader's
advantage grows as products become homogeneous is being evaluated right up
against the edge where the follower is squeezed out of the market altogether.

And here's the nice part. Go back to our replot on slide sixteen: the dashed
line reaches zero at the right-hand edge. Kopel's own Figure 1 — which I haven't
reproduced here — shows the same thing, and its vertical axis is labelled 0.66
at the top, which is the leader's CSR level at gamma-max on my recomputation.
The figure and the algebra agree; it's the prose that under-describes what's
happening.

Why does it matter? Because it bounds the headline. "The advantage grows with
competition" sounds like a general claim about competitive industries. What it
actually describes is a region whose upper end is the point where you no longer
have a duopoly. I'd want to know whether the comparative static is economically
meaningful there, or whether we're reading off the behaviour of a model at the
edge of its own validity.

---

## Slide 26 — Four other models · 75 s

Briefly, for context, I read four other duopoly CSR papers. I should say clearly
that these were read and summarised only — no verification, no independent
review — so treat what follows as indicative.

Two things came out of the comparison that I couldn't have seen from Kopel alone.

First, **rival exclusion recurs**. Chen and co-authors, and Bárcena-Ruiz and
Sagasta, both reach a corner where one firm's output goes to zero. What's
interesting is the *status* each paper gives it: Kopel treats it as a technical
bound, Chen treats it as a result, and Bárcena-Ruiz treats it as a deliberate
strategy — a shareholder choosing the CSR level that drives the rival's profit
to zero.

Second, and more important: **"CSR" is five different formal objects** across
these five papers. A demand intercept, an objective weight, an emissions cap, a
shareholder's weight on consumer surplus, a delegation parameter.

[PAUSE]

Which means a result in one category doesn't transfer to another. Kopel's
conclusion is about *appropriable demand shifts*. It does not imply that an
emissions cap fails to pay — that mechanism doesn't depend on keeping a benefit
away from the rival at all.

Hirose and Matsumura make that concrete. They treat an emissions cap as a
commitment device to soften competition — the same engine as Kopel's, but
applied mutually rather than sequentially, so the appropriability problem
doesn't arise in the same way. I should stress I have not verified that paper.

And one more that I found genuinely uncomfortable. Xing and Lee find that in a
competitive delegation setting, owners adopt **zero** environmental CSR unless
they can cooperate on it. Put that beside Kopel and you get two papers saying
unilateral CSR doesn't pay the firm that does it, for two different reasons —
in Kopel the follower free-rides, in Xing and Lee nobody moves at all without
coordination. Neither of them is the "CSR as competitive advantage" story.

---

## Slide 27 — What we didn't verify · 55 s

Before I open up, here's what I have *not* checked, so you can discount
accordingly.

Lemmas 1 and 2 aren't proved — not in the paper, not by me. Grid checks only.

The third-party quotations — Burke and Logsdon, *The Economist*, Tetrault Sirsly
and Lamertz — I verified only as Kopel reproduces them. I didn't obtain the
originals.

And the four context papers have no verification at all.

One thing I can strengthen rather than weaken: all the figures use *a* minus *c*
equal to one, and I initially flagged that as a limitation. It isn't. The
quantity *(a − c)* is a bare multiplicative factor, so the CSR levels are
homogeneous of degree one and profits of degree two. Every ordering and every
derivative sign is independent of it. The normalisation is without loss of
generality.

---

## Slide 28 — Discussion 1 · 50 s

So — three things I'd like to argue about.

First: is setting the leader's spillover to zero doing too much work?

The paper's question is who benefits from whom, and the model answers part of
that by assumption. And Kopel's own text undercuts it: on page 494 he says that *if* the follower
copies and improves the leader's green attributes, it can raise demand without
bearing the full development cost. A follower who improves on the leader's CSR
would create a reverse spillover the model excludes by construction.

The good news is this is testable with the model as it stands. Re-solve with a
small positive theta-one and see whether the frontier moves materially.

---

## Slide 29 — Discussion 2 · 60 s

Second: **would anyone choose to be the leader?**

The paper's conclusion is that leading usually loses. But the timing is
exogenous. If you endogenised it, both firms would want to wait — you'd get a
war of attrition, not a Stackelberg game. The model can't represent the
situation its own conclusion implies. Kopel does list endogenous timing as an
extension on page 502.

Third: **is a result about an unmeasurable parameter actionable?** The
first-mover advantage needs theta below 0.0015, and Kopel concedes the answer
"depends on factors which are quite hard to measure accurately." If theta is
unobservable and the admissible region is that narrow, is the practical content
just a prior — assume you won't get an advantage? Or is there an observable
proxy: speed of imitation, patent protection, brand concentration?

---

## Slide 30 — Discussion 3 and close · 60 s

And the last one, which came from the cross-paper reading: **is rival exclusion
a prediction or an artefact?**

Three independent models all contain a corner where a firm's output goes to
zero — though two of those three I read without verifying. All three use linear
demand, no fixed costs, and no entry. Is that what
CSR competition does — or what the functional form does at its edge?

[PAUSE]

Let me close with the one line I'd want you to leave with.

Over the range where the advantage is lost, the leader is still deterring. It is
still out-investing. And it still loses.

Which means the question for a CSR strategy isn't "can we move first?" It's
"can we hold on to it?" — and in this model, almost nothing lets you.

Thank you. I'd like to start with the first of those three.

---

## Backup slides — only if asked

- **B1** Full equilibrium expressions, equations (5) to (7).
- **B2** The Figure 2 discrepancy: page 500 describes the dashed-curve regions
  the wrong way round. The figure's own labels, Lemma 2, and my computation all
  agree against the sentence. I follow the figure.
- **B3** Convergent CSR — leaders actively pressure rivals to imitate, out of
  fear of reputation spillovers, which destroys their own advantage.
- **B4** Footnote 15's threshold is an *endpoint* criterion, evaluated at
  gamma-max, so it can't see an interior hump. The follower's curve is already
  non-monotone from about theta equals 0.190.
- **B5** Spillovers lower the leader's CSR sharply at high competition: from
  0.504 at theta zero to 0.208 at theta 0.21, when gamma is 0.8.
- **B6** Could the U-shape reconcile the conflicting literature? If the true
  relation is U-shaped *and* role-dependent, a linear specification recovers
  whichever sign the sample spans. That's my inference, not Kopel's.
- **B7** Symbol clashes across the five papers — theta is a spillover rate in
  Kopel but a CSR level in Bárcena-Ruiz.

**Do not raise**: the Hirose & Matsumura / Kopel numerical coincidence logged as
`open-questions` Q9. It has not been derived and a coincidence is not a finding.

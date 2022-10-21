---
title: "Machine Learning, Physics and underdetermination"
date: 2022-10-20
permalink: /posts/2022/10/machine-learning-physics-underdetermination/
tags:
  - machine-learning
  - physics
  - english
---

In this blog-post, I would like to lay out some thoughts relating
Machine Learning to Physics, by showing how they both face some form of
"underdetermination" that challenges their ability to make predictions,
unless relevant non-empirical constraints relieve this
under-determination. This suggests ways in which an analogy between ML
and Science may be fruitful.

# Machine Learning, generalization and scientific underdetermination

Much of Machine Learning is about making predictions by inferring
regularities based on past observations (data). Given some observations
$(x_i,y_i)$, one would like to find a function $f$ such that
$y_i = f(x_i)$. Once this function has been successfully determined, one
can predict $y$ for new values of $x$. This turns out to be a roughly
adequate, although very simplistic picture of what scientists, too, are
doing. From observations, scientists try to find some regularities in
the data (usually in the form of "laws"). They then hope that these laws
will allow them to correctly predict the outcome of future experiments.

Now, statisticians that attempt to find a function $f$ that fits their
data face a problem very similar to one that is faced by scientists,
which is not so surprising if we admit that they are pursuing similar
goals. The problem is that for a finite set of observations
$(x_1,y_1),...(x_n,y_n)$, there exists an infinity of functions $f$ such
that $f(x_i) = y_i$ (it is very straightforward to see that, by finding
one suitable function $f$, and then by changing any of its value for
$x \notin \{x_1, ..., x_n\}$). These functions may provide different
predictions for future observations, most of which will be plain wrong,
which is problematic for the statistician who's hoping to, e.g., make
money off his predictions. This problem in Machine Learning is called
*overfitting*. This means that the function $f$ fits the data too well,
but in a way that does not capture the true regularities at play, such
that it will fail to make reliable predictions for future data. This
problem, in a way, is very similar to the problem of *scientific
underdetermination*, which states that evidence does not univoquely
determines theory. Based on the same evidence, we could hold different
beliefs[^1]. This is a problem for scientists, because it suggests that
they can never really know whether their inferences reflect a proper
understanding of the processes at play. The problem of scientific
underdetermination has been used by sociologists of science to push a
social-constructivist narrative, arguing that scientists' beliefs are
shaped by interests or ideology and the like. This issue, if
unaddressed, threatens the very possibility of making successful
predictions[^2].

# Managing underdetermination with theoretical constraints

Fortunately, both statisticians and scientists have developed successful
strategies to overcome this issue.

How do they do that? Let us start with the statisticians. Since they are
many ways to pick a function $f$ that works for past observations, one
might want to try to make a clever pick. What is a clever pick ? It is
one that have a good chance of "generalizing well" as statisticians
would put it. Generalizing well means that the function $f$ is good at
making predictions (i.e. that given unseen values of $(x,y)$, $f(x)$
correctly yields $y$ in most cases). To assess that, statisticans first
elaborate a strategy to determine $f$. Then, they apply this strategy
using a fraction of their data points $(x_i,y_i)$ (let's say, 80% of the
data available to them). This process (which is called *training* or
*learning*) yields a function $f$. Statisticians can then assess the
ability of this function $f$ to correctly predict $y$ from $x$ by
applying it to the remainder of the data. They measure this ability by
using a performance score, which depends on the goal they are trying to
achieve. If the score is good, then the function $f$ is said to
generalize well. This is usually taken as evidence that the *strategy*
for picking $f$ was good. Therefore, statisticians are able to probe the
efficiency of their strategies for making inferences.

How do statisticians elaborate strategies ? In order to make the best
out of their data, they resort to *theoretical* arguments. For instance,
let's say one chooses the following strategy for choosing $f$ : Given
the training data $(x_i,y_i)$, one decides to choose $f$ such that
$f(x)$ is equal to $y_i=f(x_i)$ where $x_i$ is the point closest to x.
It turns out that, under rather general assumptions, this is a terrible
strategy that generalizes very poorly when the $x$ have many dimensions,
which is often the case in Machine Learning (for instance, $x$ can
represent a large image). By using theoretical arguments (which of
course embed additional assumptions), one can tell that this strategy
will be bad. And this can be tested, by following the method described
above.

Statisticians learn what sorts of procedures have a good chance of
providing good predictive functions. They can learn those through
calculations (i.e. by deriving bounds on how good the function is
expected to perform), but this is usually not a tractable solution.
Usually they know by experience what kind of procedure works, because
they or others have shown in the past that they indeed work. In
particular, they are some general features that are desired because they
are known to improve the ability of procedures to generalize. One of
them is *simplicity*. A model that is simple (e.g. that has few
parameters) is estimated to have a reduced risk of overfitting. It is
very easy to get a very good fit for a set of points with a high-order
polynomial, but chances are that its predictive power will be lower than
that of a low-order polynomial fit. What choosing a strategy for
determining $f$ will essentially do is *constraining* the space of
functions $f$ that the learning procedure will yield, but in a clever
way that will prevent overfitting.

A general method for addressing overfitting is *regularization.* It
consists in penalizing values of the parameters of a model that would
seem very unlikely (e.g. values that would be absurdly large). Again,
such a strategy requires additional assumptions about the values of the
parameters that are not only based on the data. Lasso regression is an
example of regularization, which consists in a hard-constraint on the
parameter-space (for instance, that the L1 norm of the parameters should
be less than a certain value). Regularization is also readily achieved
in a Bayesian framework by setting priors for each parameter or even for
the level of complexity of a model.

Scientists, too, have devised solutions to scientific
under-determination. Them, too, do so by resorting to different kind of
arguments to constrain the space of candidate theories for explaining
the data and making predictions. And it must be working somehow, because
it is not unusual that they make successful predictions. There is no
recipe for that, but there are some general features that scientists
find appealing in a theory, such as *simplicity*. Maybe it is rational
to appreciate simplicity, provided a simple explanation of the data has
a better chance of making successful predictions. I do not aim to argue
that specifically, but generally we can see that i) scientists work
under constraints (they don't just randomly build theories, and instead
they follow some patterns prescribed by their discipline and research
tradition) and ii) those constraints must be somewhat reasonable,
because they manage to make successful predictions despite scientific
underdetermination. Those constraints that scientists use may have shaky
grounds and lack strong justifications -- just like those used by
computer scientists sometimes. McAllister, for instance, argue that
scientists sometimes appraise theories based on "aesthetic" criteria on
the grounds that they have been successful in the past. Of course, such
criteria may also fail in the future and later be seen as unreliable.

# Which theoretical constraints should we trust?

This parallel, I think, can be pursued further. Ivanova[^3] argue that
these aesthetic criteria may have a cognitive value. To illustrate her
case, she cites the pursuit of unified laws in physics. The function of
such criteria is then to define what is a satisfying explanation. The
move towards "Explainable Artificial Intelligence" (which is concerned
with the ability to *understand* why algorithms make certain
predictions), again, provides some common ground with this issue of what
constitutes a proper scientific explanation. These seem to be two
independent problems: on one hand, making predictions that generalize
well and have a high chance of being confirmed in future experiments; on
the other hand, designing models (or theories) that provide a sense of
satisfying explanation to humans (whatever this may imply). According to
our understanding that those two goals are independent, it could very
well be that they may even clash (Hossenfelder 2018).

Is the cognitive function (the achievement of a sense of satisfying
explanation) unrelated to the issue of handling the underdetermination
of the theory by data in order to maintain the ability to make
predictions? In the case of ML, "understanding" the predictions of the
model will generally increase our trust in the model. Is this a rational
attitude? It is the case, anyway, that something similar takes place in
physics. We trust more those theories that have satisfying structure --
even though it is not clear whether what we find satisfying does not
have a purely cognitive component uncorrelated to truth value. As the
physicist Giudice (2017) puts it, "Adding one or two particles only for
the reason of generating dark matter is not something that nature would
do, if she indeed has a grand scheme in mind. It is much more plausible
that the dark matter is only the tip of the iceberg of a sector that
serves a structural purpose". According to such a statement, a proper
theoretical account of dark matter (one that will provide reliable
predictions) should simultaneously solve a number of conceptual puzzles,
rather than being a purely ad-hoc process designed to make the model fit
those data-points that are directly related to dark-matter. It does
seems reasonable to expect that any model of dark-matter that also
resolves several conceptual puzzles has a higher chance of being more
robust to further experiment, provided these "puzzles" have some
epistemic grounds.

In general, "conceptual problems"[^4], although non-empirical, do
suggest that the theory has a flaw that threatens its ability to make
successful predictions in some domain; for instance, the Higgs-mass
"naturalness problem", which is criticized as ill-founded and purely
aesthetic by some physicists, seems to threaten the predictions of the
Standard Model of Particle Physics (SM) below a certain length-scale. It
is interesting how "naturalness" problems in physics, or more generally
"fine-tuning problems" are similar to the issue addressed by
regularization in ML. In physics, fine-tuning problems arise when
parameters of a theory must take values that seem highly improbable in
order to fit the data. This is one way to state the Higgs-mass
naturalness problem, but there are other examples, such as the
cosmological constant problem. Recall that regularization in ML assumes
too that certain values for the parameters of a model seem highly
unlikely and therefore should be penalized. In both cases, that the
parameters take "unlikely" values is seen as a threat to generalization,
and when it happens the model is expected to break down at some point.
Such kind of reasoning has been the basis for Bayesian approaches to
naturalness, which assign prior distributions to the parameters of
the model, such that certain values would be deemed very unlikely and therefore suspicious.
This allows to quantify and compare the extent of fine-tuning
of various models. The underlying hypothesis is that models that are
less fine tuned have more chance of being correct.

The problem in physics is that there is often no agreement about whether
we should expect certain parameters to lie within a certain range. It is
unclear that our expectations that certain values for certain parameters
are improbable is purely cognitive, aesthetic, or that it really has
epistemic grounds. The choice of the appropriate theoretical constraints
is at the core of the debates within HEP. With time, particle physicists
have become more interested in Effective Field Theories (EFT). Roughly
speaking, EFTs are theories that are known to be at best approximately
valid above a certain length-scale. "SMEFTs" (Standard Model Effective
Field Theories) are EFTs built upon the Standard Model of Particle
Physics. They form a largely unconstrained range of theories that allows
to explore the many ways in which the SM could fail to generalize to
further experiments at slightly smaller length-scales. Therefore SMEFTs
too allows physicists to explore potential deviations from their best
theory (i.e. failures of the theory to generalize) when they are not so
sure where too look at for such failures (in part because the
theoretical constraints and criteria they typically use to reduce the
space of alternative theories do not seem so reliable, thus making
agnostic exploration strategies more appealing). As the physicists
struggle in their search for reliable non-empirical constraints for
managing underdetermination, they try to be less reliant on theoretical
constraints in their searches for new phenomena. This, however, comes at
a cost -- and it is also useful to draw a parallel between physics and
Machine Learning in that case, as I will discuss in a future blog post.

[^1]: <https://plato.stanford.edu/entries/scientific-underdetermination/>

[^2]: Dawid (2013), *String Theory and the Scientific Method*, p. 48

[^3]: Ivanova, M., "Beauty, truth and understanding", *The Aesthetics of
    Science*, 2020

[^4]: cf. Laudan's *Progress and Its problems*

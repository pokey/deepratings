I'm trying to learn a bit about whisky by getting a couple really nice, but
reasonably priced bottles.  There's a great website with good prices, tons of
selection, and lots of ratings for each whisky.  Unfortunately, their rating
aggregation is garbage.  Looks easy to scrape, so I was planning to gather all
the ratings and aggregate them myself.

The goal is to figure out how to balance rating quantity vs rating value.  Ie
if there's one 5 star rating, it shouldn't be considered better than a thousand
ratings where the average rating is 9.9.

Continuing our current philosophy that deep learning is the best answer to
every problem even when it's not, I figured this would be a perfect application
of deep learning.

During training, we feed the first k ratings for a whisky into a network and
then output a distribution over the possible values of the k+1st rating. The
loss is the negative log probability assigned to the actual value of the k+1st
rating (I think this is called multi-valued cross-entropy loss).  We do this
for every whisky and every value of k.

Frankly I really only care how likely I am to give the whisky 5 stars, so the
idea is to feed in all the ratings for a whisky, then view myself as the next
reviewer, and compute the probability that I'll give it 5 stars.  Then rank all
whiskies under £50 by this probability.  Either way, the output distribution
seems like a useful object.  You could take an expectation over it, or compute
probability of rating above 3, etc.

Here are reasons I like this problem:

- It's obviously useful for lots of applications (amazon, yelp, etc)
- It's simply stated, and seems like it should be simply solved
- It requires the ability to handle arbitrary sequence lengths, but I don't
  think a traditional RNN / LSTM makes sense.  The order of the ratings strikes
  me as irrelevant, so I'd like to leverage this symmetry somehow.  Maybe
  simply putting each rating through a feedforward network and then summing all
  these outputs.  The weights would be shared across the whole sequence.  Seems
  like a good baseline anyways.
- I'm a lush

Beyond the baselines of summing and LSTM, I was thinking of some kind of
convnet applied to fixed size subsets of the ratings and then summing the
outputs of these convnets.  Although maybe this isn't quite right, because
convnet is sensitive to order.  Also, the way we'd be handling variable sized
input is still by having a sum, so I wonder what other ways there are to deal
with this.  We basically need a commutative operation that goes from a
variable-sized input to a fixed-size output.  Another thought is to keep sum,
but do it as a tree, by basically summing neighbors, then summing this output
with output of their neighbors, etc.  Ie it would be a network whose depth
varies by sequence length k as O(log k).  This might add more discriminative
power by making the network deeper. 

Here's a relevant [baseline technique](http://math.stackexchange.com/a/942965).

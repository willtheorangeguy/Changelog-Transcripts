[0.00 --> 4.30]  One of the things that people do not think about is, you know, you're carrying around
[4.30 --> 6.34]  your mobile device all the time.
[6.34 --> 10.82]  And 90% of us are walking around with location services on.
[11.18 --> 15.44]  And then we have all these crazy conversations that we're having in our political sphere
[15.44 --> 19.64]  right now about, you know, what the government's going to do or what they're not going to do
[19.64 --> 20.68]  or who's doing this.
[20.72 --> 24.96]  And I'm like, you're allowing them to track you every moment of the day.
[24.96 --> 30.08]  And some people actually sleep with their phone on their nightstand while it's on.
[30.26 --> 31.88]  I'm like, this is insane.
[32.02 --> 34.06]  Your actions are so incongruent.
[34.42 --> 36.08]  And that data is hugely valuable.
[36.22 --> 37.86]  You can do a great deal with it.
[37.92 --> 42.18]  And we do a lot with it in my day job, in my consulting work and all sorts of things.
[42.48 --> 47.70]  And then at the end of the book, I take them through what two years from now will look like
[47.70 --> 51.14]  with just location services as the foundation.
[54.96 --> 67.14]  Welcome to Practical AI, a weekly podcast making artificial intelligence practical,
[67.46 --> 69.22]  productive, and accessible to everyone.
[69.60 --> 71.28]  Subscribe now if you haven't already.
[71.52 --> 74.38]  Head to practicalai.fm for all the ways.
[74.74 --> 79.72]  Special thanks to our partners at Fastly for delivering our shows super fast to wherever
[79.72 --> 80.36]  you listen.
[80.70 --> 82.52]  Check them out at fastly.com.
[82.52 --> 87.84]  And to our friends at fly.io, we deploy our app servers close to our users.
[88.06 --> 88.88]  And you can too.
[89.24 --> 91.14]  Learn more at fly.io.
[97.40 --> 100.50]  Welcome to another episode of Practical AI.
[100.82 --> 102.44]  This is Daniel Whitenack.
[102.54 --> 105.66]  I'm a data scientist with SIL International.
[106.00 --> 111.08]  And I'm joined as always by my co-host, Chris Benson, who is a tech strategist at Lockheed
[111.08 --> 111.36]  Martin.
[111.36 --> 112.36]  How are you doing, Chris?
[112.90 --> 114.30]  I'm doing very well.
[114.36 --> 116.84]  And Daniel, I'm just so happy to actually be online.
[117.06 --> 120.66]  As you know, I was struggling to actually show up today here.
[121.08 --> 124.38]  So internet issues, you know, they still happen.
[124.92 --> 125.04]  Yeah.
[125.16 --> 125.36]  Yeah.
[125.50 --> 126.56]  When in doubt, reboot.
[126.68 --> 126.92]  Right.
[127.08 --> 128.00]  So here we are.
[128.00 --> 129.82]  You know, data transfer.
[129.82 --> 132.20]  That's often an issue.
[132.20 --> 140.10]  And very, you know, actually fitting for today's conversation because today is all about data,
[140.28 --> 140.54]  Chris.
[140.54 --> 143.48]  We're privileged to be joined by John K.
[143.48 --> 147.90]  Thompson, who is the author of a new book called Data for All.
[147.90 --> 151.56]  And he's also written a number of other books.
[151.92 --> 158.28]  Analytics Teams, Harnessing Analytics and Artificial Intelligence for Business Improvement and Analytics,
[158.28 --> 159.82]  How to Win with Intelligence.
[159.82 --> 162.56]  So, John, it's great to have you with us.
[162.62 --> 164.52]  We can't wait to learn all about the data.
[165.34 --> 166.92]  So glad to be here, Daniel.
[167.14 --> 170.90]  And with you and Chris, looking forward to the conversation.
[171.04 --> 171.80]  Thanks for inviting me.
[171.80 --> 172.98]  Yeah, yeah.
[173.08 --> 178.76]  It was super interesting as I was reading about the motivations for the book and what you're
[178.76 --> 180.40]  covering in the book.
[180.46 --> 187.88]  You talk about how the book provides, you know, this vision of how new laws, regulations, services
[187.88 --> 194.78]  around data work in the kind of time that we live in, but also how we can benefit from
[194.78 --> 198.08]  data in new and lucrative ways, which sounds great.
[198.08 --> 201.76]  I'm all about benefiting from data in new and lucrative ways.
[202.20 --> 206.62]  Could you talk a little bit about like why kind of the motivations and why you thought
[206.62 --> 212.02]  this was kind of the time to bring in some of these discussions around types of data,
[212.18 --> 215.88]  how it's stored, who controls it, what the regulations are, et cetera, et cetera?
[216.42 --> 216.62]  Yeah.
[216.76 --> 218.24]  And thanks for the opportunity.
[218.54 --> 222.54]  I, you know, I, as you said, this is my third book.
[222.56 --> 227.52]  I've written mostly about analytics up to this point, how to build a team, how to invest in
[227.52 --> 231.54]  a team, who to hire, who not to hire, how to structure it and all that kind of stuff.
[231.80 --> 238.88]  But I started my career 37 years ago and I was a programmer and an analyst and everything
[238.88 --> 241.74]  I did just seemed to revolve around data.
[241.88 --> 244.64]  It was just all data, data, data, data all the time.
[245.10 --> 249.16]  So, you know, it just struck me as that, you know, data was the thing.
[249.50 --> 254.50]  And I switched my career to be part of, you know, the business intelligence and data warehousing
[254.50 --> 254.96]  fields.
[254.96 --> 259.82]  And, you know, I did that for decades and I've been thinking about it for a long time.
[259.82 --> 266.42]  And when we were raising our two kids that are 25 and 23 now, you know, we were always
[266.42 --> 269.36]  talking to them about, Hey, you know, how's that game going?
[269.44 --> 269.94]  What are you doing?
[269.98 --> 270.88]  They're like, Oh, it's free.
[270.98 --> 271.52]  We love it.
[271.54 --> 273.18]  And it's like, no, it's not free.
[273.18 --> 277.60]  You're giving them your information about who you are and your age and your behavior
[277.60 --> 282.82]  and your, you know, what your elasticity is and what your tolerance is for trading this
[282.82 --> 284.78]  and trading that and what the price is.
[284.96 --> 290.48]  And, you know, so we've always had this conversation over our dinner table about, you know, there's
[290.48 --> 291.24]  no free thing.
[291.58 --> 295.64]  You know, if you think it's free, then you are the product, you know, your behavior and
[295.64 --> 296.94]  you are what they're selling.
[297.58 --> 302.10]  So I've been thinking about it for a long time and I've been part of the data industry
[302.10 --> 303.94]  for almost four decades, as I said.
[304.60 --> 308.46]  And a lot of it, you know, Daniel, I know you're here in the, in the Midwest.
[308.74 --> 309.34]  I'm in Chicago.
[309.52 --> 310.42]  You're in Indianapolis.
[310.62 --> 312.92]  Chris, I think you're somewhere in the United States.
[313.10 --> 314.00]  I'm down in Atlanta.
[314.18 --> 314.66]  That's right.
[314.72 --> 314.92]  Okay.
[314.92 --> 315.74]  You're down in Atlanta.
[316.10 --> 319.50]  Well, the whole Midwest is where the whole data world started.
[319.98 --> 321.56]  So, you know, Arthur C.
[321.62 --> 326.78]  Nielsen is the guy that, you know, two miles up the road is the guy that created this
[326.78 --> 332.84]  entire ecosystem that we live in, the legal, the norms, the way people think about data.
[333.20 --> 335.32]  And I thought, nobody really knows this.
[335.44 --> 338.88]  Nobody really understands it except for maybe a handful of people.
[339.36 --> 340.34]  So I wrote the book.
[340.34 --> 346.80]  So people would be able to understand over the last hundred years why data is thought
[346.80 --> 355.50]  of as it is and why it's regulated as it is and why we have this really misguided idea
[355.50 --> 357.26]  that our data is not our own.
[357.56 --> 362.40]  That, you know, these other, these companies that manage it and move it around and resell
[362.40 --> 363.92]  it and use it own it.
[363.96 --> 364.92]  But they don't.
[365.30 --> 366.10]  We own it.
[366.10 --> 368.92]  But now we're starting to get a legal framework.
[368.92 --> 373.30]  It's led by the EU to where we can actually own our data.
[373.58 --> 374.72]  We can manage it.
[374.76 --> 375.70]  We can delete it.
[375.76 --> 377.12]  We can do things with it.
[377.22 --> 381.26]  So, you know, the book was, you know, it was just decades and decades of me thinking,
[381.48 --> 386.60]  gosh, this whole thing, this whole area is just opaque and confusing and people don't
[386.60 --> 387.32]  understand it.
[387.32 --> 391.56]  And there's got to be some book out there that says this is really the way it should be.
[391.72 --> 393.88]  And this is why it has been like this.
[393.94 --> 395.08]  That's the first part of the book.
[395.08 --> 399.98]  The second part of the book is what's happening today and what does happen with your data,
[400.08 --> 403.90]  because a lot of people don't understand what happens with their data when they're on Facebook
[403.90 --> 407.30]  or LinkedIn or Google or wherever it happens to be.
[407.90 --> 412.06]  And then the third part of the book is is all the laws and the frameworks and everything
[412.06 --> 417.12]  that's coming out of the EU that's now spilling over into the United States and the rest of
[417.12 --> 417.54]  the world.
[417.70 --> 421.98]  So you can look at it and say, OK, I really do want to manage my data.
[422.36 --> 424.24]  I do want to monetize my data.
[424.24 --> 430.20]  And there's an example in the book where I talk about that if you are an average user
[430.20 --> 435.86]  and you're on three platforms and you had the chance to monetize your data, it's probably
[435.86 --> 440.20]  two grand to you every year for doing nothing more than what you do today.
[440.72 --> 442.86]  And I talk to experts and they're all like, two grand.
[442.94 --> 443.42]  Who cares?
[443.56 --> 445.12]  No one no one wants any money.
[445.28 --> 449.64]  You know, they just want to have free email and continue on the way they are.
[449.64 --> 454.72]  And I'm like, hey, I would like to have two grand a year for doing whatever I do.
[454.84 --> 457.02]  I'd be happy to get a check for two grand.
[457.60 --> 460.80]  Every time I talk to someone, they're like, I would love to have ten dollars.
[461.10 --> 465.88]  You know, it's I don't understand why the experts are like, oh, nothing should ever change.
[465.98 --> 467.04]  You know, people don't care.
[467.34 --> 468.08]  People do care.
[468.08 --> 468.64]  Yeah.
[468.82 --> 474.44]  So you do talk about some of the history around this topic in in the book.
[474.44 --> 480.50]  What do you think are some of the main points to stress about that history to like help people
[480.50 --> 485.56]  understand why we got to this point where, yeah, there's a lot of experts saying like
[485.56 --> 488.38]  people don't don't care about their data.
[488.38 --> 493.26]  But there's also people waking up to the fact that their their data is being abused.
[493.26 --> 498.62]  There's also this general sense like I get, you know, very frequently from my non-technical
[498.62 --> 499.08]  friends.
[499.30 --> 504.76]  The thing that comes up in conversation is like, well, I'm sure, you know, Google, whoever's
[504.76 --> 505.44]  listening to me.
[505.44 --> 505.62]  Right.
[505.62 --> 509.18]  Because I said this and then later on I see this this ad or whatever.
[509.28 --> 513.74]  But there's a very there's a mystery around like what is actually collected?
[513.84 --> 514.80]  Is that actually true?
[514.82 --> 515.52]  Is it not true?
[515.88 --> 520.42]  So like what are the things kind of in the history of how this has evolved that you think
[520.42 --> 523.58]  are important to stress to to give context, I guess?
[524.12 --> 524.22]  Sure.
[524.30 --> 524.70]  Absolutely.
[524.84 --> 525.70]  And I have that.
[525.78 --> 528.06]  I just had that conversation two days ago with my sister.
[528.38 --> 533.30]  She was like, well, I was talking to your niece, her daughter, you know, about X, Y,
[533.40 --> 533.52]  Z.
[533.60 --> 537.12]  And then all of a sudden I start seeing it in my Facebook feed, in my Google feed.
[537.12 --> 540.80]  And I started asking her, I said, well, did you search on anything?
[540.98 --> 543.34]  Did you type anything into Facebook or Google?
[543.48 --> 547.52]  And she goes, no, I just had the conversation with with her on the phone.
[547.52 --> 551.30]  So I know they're listening to my phone and I'm like, they're not listening to your phone.
[551.58 --> 552.82]  This is not the NSA.
[553.38 --> 554.74]  This is not the DNI.
[555.00 --> 556.14]  We had more conversations.
[556.34 --> 560.00]  She goes, well, I did go search for this and I did go search for that.
[560.04 --> 561.30]  And I'm like, well, there you go.
[561.66 --> 566.66]  You actually put it into the engine and your search, you know, your history got, you know,
[566.70 --> 570.90]  modified by the algorithm or whatever, you know, whatever they're using there.
[571.00 --> 572.30]  But anyway, I digress.
[572.72 --> 573.60]  So everybody's talked.
[573.68 --> 575.00]  A lot of people are talking about this.
[575.00 --> 580.20]  And, you know, the thing that I think is very important for people to realize and, you know,
[580.26 --> 584.46]  Arthur Nielsen, you know, great guy, created Nielsen, really smart fellow.
[585.10 --> 588.98]  But precedence in the United States legal system is a huge deal.
[589.54 --> 595.14]  And when Arthur struck the deal with these grocery stores that they would basically transfer
[595.14 --> 599.34]  all their usage data to him for free, set a precedence.
[599.48 --> 604.10]  And it went on and on and on for 100 years and no one really thought about it.
[604.10 --> 610.24]  And they kept accreting more and more data, media data and sales data and, you know, radio
[610.24 --> 611.86]  data, television data.
[612.04 --> 613.84]  And it went on and on and on.
[613.90 --> 617.10]  And now some people say, well, you know, Nielsen does pay for the raw material.
[617.40 --> 618.34]  Yes, they do.
[618.50 --> 620.14]  I absolutely understand that.
[620.18 --> 621.10]  I used to work at Nielsen.
[621.20 --> 621.90]  I know what they do.
[622.52 --> 624.54]  So, yes, they do pay people for the data.
[624.56 --> 628.16]  But it's a pittance compared to what they get paid for the data.
[628.16 --> 634.04]  So, all that's to say that this precedent that was set 100 years ago still continues
[634.04 --> 634.58]  today.
[635.38 --> 638.76]  So, people are saying, well, you know, my data really isn't worth anything.
[639.02 --> 641.22]  But the world has changed.
[641.76 --> 643.24]  You know, we have the ubiquitous internet.
[643.48 --> 644.36]  We have broadband.
[644.64 --> 646.00]  We are always on.
[646.10 --> 647.28]  We have mobile phones.
[647.52 --> 649.32]  We're, you know, always contributing.
[649.66 --> 653.22]  Some people call it digital exhaust, which I don't really like that term.
[653.22 --> 656.70]  But we are always contributing our usage data.
[656.94 --> 658.88]  Think of, do either of you have electric cars?
[659.14 --> 659.88]  I do not.
[660.08 --> 660.26]  No.
[660.62 --> 661.08]  Not yet.
[661.12 --> 662.48]  But my brother-in-law does.
[662.58 --> 662.74]  Yeah.
[663.26 --> 664.52]  I have a Mustang Mach-E.
[664.78 --> 666.10]  It's not a car.
[666.36 --> 667.40]  It's a rolling computer.
[667.80 --> 671.50]  And it's generating data 24 hours a day, even if I'm not in it.
[672.00 --> 676.86]  So, you know, we have to realize that we are generating the data.
[677.42 --> 679.10]  We own the data.
[679.10 --> 683.44]  This idea, this precedence of giving away for free must change.
[684.00 --> 688.18]  And that's one of the things that in the book that I talk about a lot is that we have
[688.18 --> 697.24]  a colored or a skewed view of data ownership that we give away the province or the province
[697.24 --> 699.72]  of our data to all these companies.
[699.72 --> 701.18]  And they use it for free.
[701.40 --> 707.84]  And in the book, I talk about, you know, Facebook doesn't pay for the raw materials that it uses
[707.84 --> 708.82]  to run its business.
[709.10 --> 710.32]  And it makes no sense.
[710.88 --> 714.52]  I mean, Daniel and Chris, if you went to a builder and said, hey, I'd like you to build
[714.52 --> 715.24]  me a house.
[715.64 --> 720.70]  And the builder came back and said, well, you know, we're going to get the lumber for free.
[721.34 --> 721.74]  No.
[722.22 --> 725.38]  Nobody gets a major raw material for free.
[726.08 --> 731.20]  And, you know, my point is that, number one, we have to understand that we own the data.
[731.66 --> 734.08]  And number two, they should pay for it.
[734.20 --> 735.40]  So let me ask you a question.
[735.40 --> 739.80]  You've already kind of created the context around it, I think, over the last couple of
[739.80 --> 740.08]  minutes.
[740.44 --> 744.94]  But something you said a couple of times earlier, you talked about the EU leading the way.
[745.36 --> 751.32]  And certainly there is a certain well-known EU law that I suspect we're talking about
[751.32 --> 751.58]  there.
[751.58 --> 758.94]  But aside from the law itself, I'm curious, why is the EU leading the way in your view?
[759.06 --> 765.82]  What is it about the EU that has created that law and has done this, whereas we have struggled
[765.82 --> 769.18]  to do that in the United States and elsewhere in the world?
[769.18 --> 774.56]  And where we have done something, it has been in smaller geographic areas like specific states.
[774.74 --> 775.14]  That's right.
[775.40 --> 776.90]  You're referring to GDPR.
[777.00 --> 777.24]  Indeed.
[777.32 --> 780.28]  That was put into law six years ago.
[780.82 --> 783.36]  And GDPR has been a huge success.
[783.68 --> 788.18]  It has really been a great movement for the people of Europe.
[788.80 --> 791.12]  And we all know Britain is no longer in Europe.
[791.34 --> 792.06]  They're on their own.
[792.18 --> 793.66]  They're outside the EU at this point.
[793.66 --> 799.50]  So GDPR has been a boon for the citizens of Europe.
[799.80 --> 800.66]  They can go in.
[800.74 --> 801.74]  They can access their data.
[801.84 --> 802.96]  They can delete their data.
[803.08 --> 804.46]  They can take it off platforms.
[804.66 --> 806.14]  They can do all sorts of things with it.
[806.56 --> 813.40]  And based on the success of GDPR, the EU has now passed the Data Act, the Data Governance
[813.40 --> 815.26]  Act, and the Digital Markets Act.
[815.52 --> 817.70]  And all of those acts have been passed.
[818.08 --> 821.10]  And they are now going into effect.
[821.10 --> 828.16]  And those laws now put together data pools, data unions, data exchanges, all the structures
[828.16 --> 834.50]  that I talk about in the book that if you and I or any of us want to go to Google, Facebook,
[834.94 --> 840.28]  Amazon, United Airlines, American Airlines, and say, I want all my data.
[840.62 --> 841.48]  They have to give it to you.
[841.72 --> 842.40]  That's number one.
[842.66 --> 848.80]  But number two, as it goes on, these data exchanges and data pools are going to be the intermediaries
[848.80 --> 854.04]  that we work with that we go in and say, you know, you know, you can we can withdraw your
[854.04 --> 854.28]  data.
[854.38 --> 859.30]  Let's say that you're you're really worried about climate change, you know, and any company
[859.30 --> 863.36]  that you feel contributes to climate change in a negative way.
[863.40 --> 865.68]  You can say you can't have my data at all.
[865.70 --> 871.64]  You can just say United Airlines or Exxon or Mobil or Rosnaft or, you know, whoever you
[871.64 --> 872.32]  want to block.
[872.38 --> 872.76]  You can.
[872.76 --> 874.96]  But my point is, why block them?
[875.40 --> 880.06]  My point is, you know, if you're going to say, you know, the music royalty system is
[880.06 --> 884.42]  the system that makes the most sense to me when you're thinking about data monetization.
[884.94 --> 888.20]  You know, you may take all my browsing data and I'll let you use it.
[888.64 --> 892.44]  Every time you touch it, you got to pay me a penny or a half a penny or a tenth of a
[892.44 --> 893.36]  penny or whatever it is.
[893.68 --> 897.08]  For these companies, you say every time you touch my data, you have to pay me a million
[897.08 --> 897.60]  dollars.
[897.60 --> 902.54]  That sends a pretty strong signal that you really don't like what they do, you know,
[902.60 --> 906.22]  and if they pick you up on it and say they want to use your data, either intentionally
[906.22 --> 910.24]  or by mistake, and they use it four times, they got to pay you four million dollars.
[910.42 --> 911.90]  So, you know, stay in the game.
[911.90 --> 931.22]  Well, John, I'm really fascinated by this sort of topic and area talking about like data
[931.22 --> 938.60]  exchanges and like the I guess the infrastructure or the mechanisms by which some of these newer
[938.60 --> 941.68]  ways of dealing with your data could come about.
[941.78 --> 943.78]  It actually it actually reminded me.
[944.14 --> 950.22]  So my my brother in law works for a company that is sort of an intermediary between farmers
[950.22 --> 951.44]  and grocery stores.
[951.44 --> 954.32]  So like there's the raw material, right?
[954.34 --> 956.40]  There's the vegetable carrots or whatever.
[956.40 --> 962.88]  And he mediates this exchange between like the actual farmers and and grocery stores.
[962.88 --> 966.92]  I'm wondering, you know, in the data world, like let's say there's there's Google, there's
[966.92 --> 969.32]  Facebook, there's whoever wants to use my data.
[969.78 --> 972.72]  And there's me who who owns the data.
[972.90 --> 977.72]  At least that's sort of the shifting mindset that we want to think about from your mind,
[977.72 --> 982.00]  like how might this sort of data exchange or the other mechanisms that you talked about,
[982.00 --> 983.34]  where do those sit?
[983.50 --> 988.52]  Who sort of regulates those or how might how might those come about?
[988.62 --> 994.50]  Is there a current example that you could give or or maybe a way forward that you think
[994.50 --> 995.38]  is probable?
[995.38 --> 996.72]  They do exist.
[996.94 --> 1000.60]  They exist predominantly in the UK and the EU.
[1000.90 --> 1006.54]  There's one that's very prominent called Pool Data IO, and they're working really hard to
[1006.54 --> 1008.36]  have their data exchange be out there.
[1008.40 --> 1011.50]  And there's all sorts of other data exchanges going on right now.
[1011.80 --> 1016.40]  Across the United States, we usually see these kind of structures and they do exist and have
[1016.40 --> 1019.28]  existed for many years in the area of health.
[1019.28 --> 1024.98]  And they're usually related to cancer or heart disease, but they're more prominent in the
[1024.98 --> 1026.40]  area of rare diseases.
[1027.12 --> 1033.88]  You know, people that have have got hereditary angioedema or primary immunodeficiency disease
[1033.88 --> 1035.86]  or hemophilia or something like that.
[1035.86 --> 1041.96]  And these exchanges really allow these people to contribute, you know, all their diagnostic
[1041.96 --> 1044.94]  data, their clinical data and maybe even their genetic data.
[1045.34 --> 1048.48]  So, you know, they do exist and they do operate.
[1048.64 --> 1049.56]  They're in the United States.
[1049.64 --> 1050.60]  They're around the world.
[1050.88 --> 1054.94]  Commercially, they're mostly in the UK and the EU right now.
[1054.94 --> 1059.56]  And physically, the way it's going to work is that when these laws come out in California
[1059.56 --> 1062.32]  and five other states have these laws on the books right now.
[1062.94 --> 1068.42]  So you can go in and say, you have to give me all my data and you have to delete it.
[1068.78 --> 1073.90]  You know, if you live in Britain or Denmark or somewhere in Europe, you can do that.
[1074.34 --> 1078.70]  What's going to happen in the future is these data exchanges will sit in the middle.
[1078.70 --> 1084.68]  So, you know, Amazon and all the other companies are not going to contribute their data to some
[1084.68 --> 1087.08]  monolithic central storage unit.
[1087.20 --> 1088.26]  That's not going to happen.
[1088.42 --> 1093.96]  Don't, you know, Colossus or, you know, whatever, you know, Megalith, that won't be the case.
[1094.48 --> 1097.88]  What's going to happen is they will still own their data.
[1098.30 --> 1099.94]  They will still have their data.
[1100.06 --> 1101.10]  We will own our data.
[1101.24 --> 1107.00]  And through the exchanges, you will go in and say, for my browsing data, for my shopping
[1107.00 --> 1111.86]  data, for my health data, whatever, you know, you have in there, your airline travel data,
[1112.30 --> 1115.50]  you will put a monetization amount on it.
[1115.66 --> 1119.10]  And you will say that these companies can or cannot use it.
[1119.60 --> 1123.54]  So when those companies go to use the data, they will have to pass to the exchange.
[1123.98 --> 1126.82]  They will have to check the yes or no, the opt in, opt out.
[1127.00 --> 1130.34]  They will have to understand the monetary value associated with it.
[1130.34 --> 1134.90]  And when they go back and use it, they will have to have an accounting system where they rack
[1134.90 --> 1138.58]  up the amount of money that they owe you, me, and everyone for using that data.
[1139.04 --> 1141.28]  So I have kind of a dumb question I want to ask.
[1141.42 --> 1142.14]  No dumb question.
[1142.38 --> 1143.98]  Because we've, I knew you were going to say that.
[1144.96 --> 1147.02]  We've leapt forward a little bit.
[1147.34 --> 1152.90]  But what exactly constitutes a data exchange as we're using the term around, is it always
[1152.90 --> 1153.66]  a third party?
[1154.16 --> 1159.30]  Could a social media giant like Facebook or Google or whoever, could they have their own
[1159.30 --> 1159.72]  exchange?
[1160.04 --> 1161.04]  What's the difference in those?
[1161.16 --> 1163.50]  What does it mean to have a data exchange?
[1163.50 --> 1168.54]  A data exchange is a legal entity created by EU law at this point.
[1168.94 --> 1171.82]  And it will happen, will be created in the United States as well.
[1172.42 --> 1177.12]  And a data exchange is a third party that does just what we talked about.
[1177.26 --> 1179.30]  They allow you to come in through an interface.
[1179.54 --> 1180.76]  They allow you to set prices.
[1181.00 --> 1184.20]  They allow you to set usage policies and those kind of things.
[1184.54 --> 1187.22]  They cannot monetize data.
[1187.66 --> 1191.28]  They cannot accrue, store, and sell data.
[1191.28 --> 1197.68]  They're an exchange where they allow you to set your policies, set your prices, you know,
[1198.08 --> 1199.66]  stop people from using your data.
[1200.08 --> 1205.10]  What they can do is they can reach into systems and they can analyze usage patterns and they
[1205.10 --> 1211.30]  can suggest to you how to best monetize your data or how best to achieve your objectives.
[1211.30 --> 1218.12]  Maybe your objectives are to give all the money that you get from your data monetization usage
[1218.12 --> 1224.98]  efforts to a charity, you know, that comes along and says, OK, every time I get, you know,
[1225.04 --> 1231.44]  $100 in my data usage account or my data monetization account, I want to donate it to the American Cancer
[1231.44 --> 1238.76]  Society or I want to donate it to Ukrainian Relief or I want it, you know, spent over all these
[1238.76 --> 1239.24]  areas.
[1239.24 --> 1246.14]  Or you can actually say, you know, when these charitable organizations use my data, I want
[1246.14 --> 1246.58]  to pay them.
[1247.02 --> 1252.08]  So there there is a little bit of a marketplace that it establishes and maybe not in a precise
[1252.08 --> 1257.42]  approach across the board, but maybe as a is a very rough analogy, sort of like a stock exchange
[1257.42 --> 1262.22]  where you don't necessarily know how to price what you're looking at.
[1262.30 --> 1266.02]  But the market that exists in that exchange prices it for you.
[1266.12 --> 1268.04]  But in this case, it's data directly.
[1268.58 --> 1268.80]  Exactly.
[1269.10 --> 1270.64]  And you can set your own objectives.
[1270.80 --> 1275.32]  You want to say, I want to maximize the amount of money that I accrue because I'm going to take
[1275.32 --> 1276.64]  that money myself and spend it.
[1276.72 --> 1277.42]  And it is money.
[1277.62 --> 1278.52]  It's not credits.
[1278.76 --> 1280.06]  It's not units.
[1280.06 --> 1280.74]  It's money.
[1280.86 --> 1281.54]  It's dollars.
[1281.54 --> 1282.12]  It's euros.
[1282.42 --> 1284.94]  It's, you know, drachma, yen, whatever it is.
[1285.24 --> 1289.46]  So, you know, you are actually piling up money in your account that you can spend.
[1290.08 --> 1296.18]  Now, your other objectives may be, I want to reduce the usage of my data by people who
[1296.18 --> 1297.04]  are climate offenders.
[1297.54 --> 1305.70]  Or maybe I want to help, you know, these charitable organizations, you know, understand my activity
[1305.70 --> 1306.08]  better.
[1306.50 --> 1310.92]  Or maybe you find a group of people that are like-minded or have the same affinities as you
[1310.92 --> 1312.40]  do and you group together.
[1312.60 --> 1316.72]  And all your data can only be used in aggregate as a pool.
[1317.00 --> 1318.96]  There's a million different ways you can take this.
[1318.96 --> 1324.14]  One of the other things I love about the topics that you cover in your book is actually digging
[1324.14 --> 1327.62]  into how data works today.
[1327.62 --> 1331.08]  And what that actually looks like.
[1331.08 --> 1336.12]  So we're talking about this sort of monetization or exchange a little bit.
[1336.12 --> 1342.14]  But if we shift and think about, like, from your perspective, whether it's daily interactions
[1342.14 --> 1347.12]  with people in your own social circles or it's your actual business colleagues who are working
[1347.12 --> 1349.86]  on data problems specifically.
[1350.54 --> 1357.40]  What do you think are some of the main types of data that people aren't considering or the
[1357.40 --> 1360.82]  main characteristics of that data maybe they aren't considering?
[1360.82 --> 1367.24]  I know you talk a little bit about fresh or stale or repetitive, infrequent, episodic,
[1367.36 --> 1369.68]  these sorts of things.
[1369.86 --> 1374.76]  So from your perspective, what are some of those types of data or characteristics that maybe
[1374.76 --> 1377.92]  people aren't thinking about as much as they should?
[1378.30 --> 1382.96]  I think, you know, one of the, I know that one of the things that people do not think about
[1382.96 --> 1387.04]  is, you know, you're carrying around your mobile device all the time.
[1387.04 --> 1393.24]  And 90% of us, or maybe 80%, I'm making these numbers up, are walking around with location
[1393.24 --> 1394.80]  services on, you know?
[1394.80 --> 1399.76]  And then we have all these crazy conversations that we're having in our political sphere right
[1399.76 --> 1403.90]  now about, you know, what the government's going to do or what they're not going to do
[1403.90 --> 1404.94]  or who's doing this.
[1404.96 --> 1409.10]  And I'm like, you're allowing them to track you every moment of the day.
[1409.22 --> 1414.30]  And some people actually sleep with their phone on their nightstand while it's on.
[1414.46 --> 1416.10]  I'm like, this is insane.
[1416.10 --> 1419.16]  Your actions are so incongruent, you know?
[1419.26 --> 1423.32]  And I take people through, you know, in the beginning of the book, I take them through
[1423.32 --> 1427.34]  a very light scenario of what happens with just location services.
[1427.80 --> 1429.48]  And that data is hugely valuable.
[1429.62 --> 1431.26]  You can do a great deal with it.
[1431.32 --> 1435.80]  And we do a lot with it in my day job, in my consulting work and all sorts of things.
[1436.26 --> 1441.22]  And then at the end of the book, I take them through what two years from now will look
[1441.22 --> 1445.08]  like with just location services as the foundation.
[1445.08 --> 1449.46]  So, you know, all these people saying that, you know, they're, hey, they're, they're upset
[1449.46 --> 1451.20]  about this or they're upset about that.
[1451.30 --> 1455.64]  I'm like, well, just turn your phone off and you'd be a lot better off there.
[1455.98 --> 1459.32]  And then the other thing that we talk about a lot in the book, and I've talked about in
[1459.32 --> 1464.52]  my other books, and I am a big proponent of is if you're an analytical professional,
[1464.52 --> 1469.80]  you know, this whole idea of just stacking up one source of data, you know, in neural networks,
[1469.80 --> 1473.88]  they always show, you know, trying to discern between chihuahuas and muffins.
[1474.14 --> 1474.60]  Okay, fine.
[1474.68 --> 1478.86]  I don't know what real application is going to be helpful in understanding the difference
[1478.86 --> 1480.78]  between the two pictures, but I get it.
[1481.14 --> 1485.68]  So you take a billion images of chihuahuas and a billion images of muffins and you analyze them,
[1486.02 --> 1490.82]  you know, but really what happens, what we're trying to get to and what we are getting to
[1490.82 --> 1497.00]  in analytics is we're trying to get models to reason as realistically as we possibly can.
[1497.00 --> 1502.60]  I try to stay away from, you know, the whole AGI concept of, you know, artificial general
[1502.60 --> 1509.22]  intelligence, but we are trying to use many, many, many sources of data and integrate them
[1509.22 --> 1509.64]  together.
[1509.88 --> 1515.16]  And that's one thing that people don't really understand is that we as analytics professionals
[1515.16 --> 1520.98]  are starting to take three, four, five, six, seven, eight, nine, 10, 12 sources of data and
[1520.98 --> 1526.98]  bring them together and generate features that realistically show us what people are going to
[1526.98 --> 1527.22]  do.
[1527.62 --> 1533.10]  And we can do a really good job of predicting what most people will do with six, seven,
[1533.18 --> 1534.34]  eight different sources of data.
[1534.70 --> 1540.60]  And that is something that is really going to come into the fore over the next three, four,
[1540.68 --> 1541.14]  five years.
[1541.34 --> 1547.44]  So the concept of data, you know, location data, voice data, browsing data, commerce data,
[1547.96 --> 1553.74]  you know, driving data, all of that is the true picture, is a real picture of who you
[1553.74 --> 1554.86]  are and what you do.
[1555.26 --> 1561.24]  And we know that when people describe who they are, they always describe that they eat
[1561.24 --> 1563.68]  25% less calories than they do.
[1563.82 --> 1566.30]  They always say that they sleep less than they do.
[1566.72 --> 1568.96]  They always say they talk less than they do.
[1569.34 --> 1571.66]  Well, we can see what they actually do.
[1572.10 --> 1573.88]  And we know how people act.
[1573.94 --> 1578.24]  I was just going to ask you, you have my full attention because you completely freaked me out
[1578.24 --> 1578.72]  a minute ago.
[1579.10 --> 1584.86]  So I'm hijacking a short segment of the show here to go back and ask you a question because
[1584.86 --> 1586.20]  I am guilty.
[1586.54 --> 1591.24]  You mentioned some people even sleep with their cell phone on, on the nightstand.
[1591.48 --> 1592.34]  No, Chris.
[1592.76 --> 1593.00]  No.
[1593.00 --> 1593.54]  I do.
[1593.90 --> 1600.62]  I'm confessing to the audience that I have actually done that not once, not twice, but pretty
[1600.62 --> 1601.38]  much every night.
[1601.38 --> 1606.56]  So doing that, and in my mind, I'm thinking, you know, I got an elderly mother, I only have
[1606.56 --> 1607.04]  a cell phone.
[1607.10 --> 1609.66]  I don't have anything but that, need to be available and stuff.
[1610.18 --> 1614.72]  But as you talk about that, like that's a real life scenario from my standpoint.
[1615.08 --> 1617.74]  And you just, you know, you hit it with a hammer just now.
[1617.96 --> 1623.80]  Like if I'm going to be available overnight, you know, in case my mom has an emergency or
[1623.80 --> 1626.08]  something, what is it like?
[1626.14 --> 1627.40]  Can you talk a little bit about that?
[1627.42 --> 1628.72]  Because that's incredibly tangible.
[1628.72 --> 1634.76]  Can you talk a little bit, what have I just sacrificed in terms of my, you know, privacy
[1634.76 --> 1636.96]  or the data I'm giving up to do that?
[1637.02 --> 1639.86]  Because I'm truly like weighing this at this point.
[1639.92 --> 1644.34]  My mom's going to be horrified to hear that I'm weighing whether her safety is worth it.
[1644.44 --> 1647.02]  But please, just for a moment, dive back into that.
[1647.36 --> 1647.46]  Yeah.
[1647.56 --> 1651.22]  I mean, you know, we all have these, you know, we're all talking about that.
[1651.46 --> 1653.42]  And I turn my location services off.
[1653.90 --> 1657.92]  My net position, my default position is location services off.
[1657.92 --> 1660.80]  And at night, I turn my phone off.
[1661.22 --> 1664.62]  And I can do that when I'm at home because I have a landline.
[1665.18 --> 1667.74]  You got the old fashioned one right there beside it, the other one.
[1667.98 --> 1672.16]  So, you know, my family knows if they need to call me, call the home line.
[1672.24 --> 1672.82]  I'll pick it up.
[1673.06 --> 1676.10]  You know, don't call my mobile phone because after six o'clock, it's off.
[1676.10 --> 1676.80]  Okay.
[1677.04 --> 1677.32]  Yeah.
[1677.44 --> 1685.30]  I think maybe it speaks to the issue at hand that the one of us on this discussion that's
[1685.30 --> 1690.90]  been an analytics professional for their entire career takes that position.
[1690.90 --> 1694.80]  And maybe we're on a little bit different side.
[1694.98 --> 1697.02]  That's probably worth noting.
[1697.32 --> 1700.30]  I'm just saying guests don't freak me out completely most of the time.
[1700.40 --> 1702.42]  But, you know, I'm kind of freaking right here.
[1702.44 --> 1702.74]  Okay.
[1703.26 --> 1704.68]  I'm thinking, what have I done?
[1704.96 --> 1709.14]  I tell you what I, you know, I used to, well, pre-COVID, you know, we'd go to cocktail parties
[1709.14 --> 1711.14]  and ask, people would ask me what I would do.
[1711.18 --> 1714.54]  And I would give them, you know, kind of the same description that we've been talking about.
[1714.98 --> 1717.28]  And they would get freaked out and not talk to me anymore.
[1717.88 --> 1720.26]  So when people ask me now, I just say.
[1720.38 --> 1721.40]  You have a show to complete though.
[1721.50 --> 1722.86]  You know, you have no choice.
[1722.90 --> 1723.50]  I have no choice.
[1723.54 --> 1724.26]  We're going to do this.
[1724.36 --> 1726.84]  Now I say I take data and turn it into money.
[1727.06 --> 1727.72]  That's what I do.
[1727.72 --> 1733.04]  Yeah, I guess that's a really interesting point because you could see Chris's phone on,
[1733.04 --> 1738.68]  on his nightstand as a moneymaker, I guess, and based on our previous discussion, right?
[1738.82 --> 1746.16]  If, but that's only possible if he had the opportunity to monetize that data, right?
[1746.16 --> 1752.06]  So I think like in terms, I know you talk about like different jurisdictions and in the book and
[1752.06 --> 1755.64]  such, maybe for those, you've talked a little bit about Europe.
[1755.96 --> 1761.92]  What is the landscape look like around the rest of the world in terms of how quickly we're moving
[1761.92 --> 1768.48]  towards this position where we're able to kind of in a more lucrative way, manage our data?
[1768.92 --> 1769.06]  Yeah.
[1769.28 --> 1772.26]  The EU will be there within 18 months.
[1772.26 --> 1776.86]  Australia will probably be there in about the same timeframe, maybe 24 months.
[1777.66 --> 1782.02]  Spotty across the United States, California has already got their privacy law and they
[1782.02 --> 1786.64]  are actually following very closely the three laws that I just talked about in the EU.
[1787.12 --> 1790.82]  Then we've got five other US states that have those laws.
[1791.34 --> 1795.76]  And beyond that, you can take a look at where the liberal Western democracies are.
[1796.20 --> 1799.00]  And most of those will come up in the next three to five years.
[1799.00 --> 1805.24]  You know, you can look at the other countries and autocracies and the, you know, the autocrats
[1805.24 --> 1807.20]  and dictators and things like that.
[1807.30 --> 1812.14]  And that will probably be never if they continue with that standard of government, because they
[1812.14 --> 1816.84]  just don't like, you know, the transparency and the, well, they do like it if they control
[1816.84 --> 1819.56]  all the data, they like it that way.
[1819.70 --> 1824.62]  But as far as their citizens being able to monetize their data, that's not going to happen
[1824.62 --> 1825.30]  anytime soon.
[1825.30 --> 1855.28]  Thank you.
[1855.30 --> 1868.66]  John, a couple of the sections of the book that you dive into are trust and privacy.
[1869.22 --> 1874.28]  These are two terms that are, I don't know, Chris, I don't know what percentage of the
[1874.28 --> 1876.02]  conversations we have on this podcast.
[1876.40 --> 1882.52]  Someone uses one of those two terms, but I would say it's, it's very much, you know,
[1882.52 --> 1884.52]  terms that come up very often.
[1884.52 --> 1893.16]  I'm wondering, John, as you've really dug into the state of how data flows these days,
[1893.32 --> 1901.00]  how the regulations are changing around data, maybe as like analytics professionals or as
[1901.00 --> 1908.90]  AI developers or as AI researchers or, you know, for professionals in the field like ourselves,
[1908.90 --> 1915.12]  what do you think are the kind of practical considerations that we should be thinking
[1915.12 --> 1921.70]  about in terms of trust and privacy as we're building out, like, I'm going to make the,
[1922.26 --> 1924.72]  this AI enabled app to do X.
[1925.04 --> 1930.52]  What should be those things on my mind related to trust and privacy from your perspective?
[1931.12 --> 1932.00]  Yeah, it's a great question.
[1932.00 --> 1936.46]  You know, and I've been in this field long enough to know that, you know, when we started
[1936.46 --> 1941.40]  out, you know, those many decades ago, you know, we just always did it because we were
[1941.40 --> 1946.22]  just trying to sell more, you know, bars of soap or cans of soup or pizzas or whatever
[1946.22 --> 1946.70]  it was.
[1947.06 --> 1948.50]  It wasn't anything nefarious.
[1948.68 --> 1950.32]  It wasn't anything, you know, in it.
[1950.62 --> 1954.66]  And we did have people ask us to do things that crossed the line, you know, that broke ethics
[1954.66 --> 1955.94]  and we just wouldn't do it.
[1956.30 --> 1960.78]  So it was a pretty small community and we just did what was ethical and, you know, what was the
[1960.78 --> 1961.42]  right thing to do.
[1961.76 --> 1967.52]  Now we've gone to where data and analytics are, you know, the horse is out of the barn.
[1968.16 --> 1972.94]  You know, we actually need, and I've never been a proponent of this until the last couple
[1972.94 --> 1973.34]  of years.
[1973.60 --> 1975.70]  You know, we need government to step in.
[1976.14 --> 1981.08]  You know, we have organizations like Facebook and people like Mark Zuckerberg and, you know,
[1981.10 --> 1983.18]  that have no rules, that have no red lines.
[1983.18 --> 1985.64]  You know, they just go all over the place.
[1986.12 --> 1989.18]  Mark Zuckerberg's answer to any problem with Facebook is more Facebook.
[1989.58 --> 1990.20]  Yeah, exactly.
[1990.20 --> 1990.64]  Yeah.
[1990.64 --> 1993.88]  I'm actually stealing that from Kai Risdahl, just so that you know.
[1994.06 --> 1994.68]  I've heard it.
[1994.76 --> 1995.38]  I've seen it.
[1995.52 --> 1996.62]  I know what he's saying.
[1996.76 --> 1997.38]  You know, absolutely.
[1997.98 --> 2004.58]  So, you know, the reason I delve so deeply and dedicated an entire chapter to trust and
[2004.58 --> 2011.42]  an entire chapter to privacy is they are concepts that we talk about a lot, but we generally
[2011.42 --> 2014.26]  are not taught what they really mean.
[2014.26 --> 2018.90]  I think we understand what the words, you know, the connotative meaning, the denotative
[2018.90 --> 2020.24]  meaning of trust and privacy.
[2020.78 --> 2024.82]  But when you start to really delve into those concepts and how they relate to human behavior,
[2024.82 --> 2029.12]  we could all use, you know, a little bit more education than we're getting.
[2029.12 --> 2032.34]  And that's why I spend so much time in the book on those.
[2032.50 --> 2038.04]  So we as analytics professionals have to be ready and should welcome government regulation
[2038.04 --> 2038.80]  in these areas.
[2038.90 --> 2039.50]  It's required.
[2039.60 --> 2040.10]  It's needed.
[2040.44 --> 2044.42]  You know, it's we're getting to a point where the folks in data and analytics or some of the
[2044.42 --> 2049.22]  folks in data and analytics are really getting into trouble and causing trouble for us as
[2049.22 --> 2049.78]  a society.
[2049.78 --> 2051.46]  And we can't stand that.
[2051.54 --> 2052.98]  That's not that cannot happen.
[2053.40 --> 2059.32]  In privacy, I talk a lot about, you know, the need for privacy and secrecy, which, you
[2059.32 --> 2061.12]  know, is really an interesting concept.
[2061.12 --> 2063.28]  And we could spend hours talking about it.
[2063.30 --> 2067.02]  But, you know, if nothing else, that might be something while you read the book is to
[2067.02 --> 2071.02]  understand the difference between the need for privacy and the need for secrecy.
[2071.56 --> 2075.22]  It's interesting when we talk about government, because, you know, you have the left and the
[2075.22 --> 2078.58]  right and the different in the, you know, the conversation kind of goes back and
[2078.58 --> 2079.90]  forth depending on circumstances.
[2080.70 --> 2086.38]  But maybe I think maybe people can arrive at, yes, we need government regardless of
[2086.38 --> 2090.56]  which side you're coming from, because they've been so slow to come at all.
[2090.66 --> 2095.40]  And I think one of the challenges that we've all observed there is, you know, every time
[2095.40 --> 2102.06]  we see one of these, you know, figures in technology such as Zuckerberg, you know, or any of the
[2102.06 --> 2106.90]  big companies that we're always talking about, and they testify before Congress or something
[2106.90 --> 2113.42]  like that, you see how far behind, you know, government, you know, officials, very congressmen,
[2113.54 --> 2115.62]  senators and stuff are at that point.
[2115.82 --> 2119.84]  That's the big news thing is, you know, one of these figures testifies and everyone's like,
[2119.88 --> 2121.96]  oh, my God, did you hear the questions that were being asked?
[2122.18 --> 2127.88]  Is that part of the problem potentially that there's such a knowledge difference in this
[2127.88 --> 2133.68]  topic that maybe in some cases government doesn't really know what to do to do it regardless
[2133.68 --> 2135.30]  of which side of the aisle they're on?
[2135.74 --> 2139.98]  Could that be part of the struggle or do you would you identify it somewhere else?
[2139.98 --> 2143.18]  No, I think you put your finger on a very salient problem.
[2143.56 --> 2147.88]  You know, we've got a bunch of octogenarians, you know, running the government right now,
[2148.00 --> 2150.58]  and most of them don't even understand how to use a computer.
[2151.12 --> 2152.22]  So that is a real problem.
[2152.38 --> 2157.16]  But, you know, there are people out there like me and others who are experts in this field
[2157.16 --> 2162.98]  who would love to serve on a blue ribbon panel to, you know, formulate the laws and the rules
[2162.98 --> 2164.32]  and the regulations that we need.
[2164.84 --> 2167.26]  I'm sure there's lots of Americans that would love to help.
[2167.60 --> 2170.30]  And then the EU has done a lot of the hard work.
[2170.74 --> 2174.96]  You know, I know we're as Americans, we're loathe to think that anything outside the United
[2174.96 --> 2177.02]  States is better than anything we would ever do.
[2177.16 --> 2181.80]  But the problem, but the fact of the matter is they've done a good job over the last eight
[2181.80 --> 2183.82]  years in formulating GDPR.
[2184.04 --> 2185.28]  They've implemented it.
[2185.28 --> 2186.24]  It has worked.
[2186.62 --> 2190.78]  It has changed the way that we look at data, the way that we do analytics, the way that
[2190.78 --> 2192.28]  people can access their data.
[2192.82 --> 2196.96]  The three other acts, the Data Act, the Data Governance Acts, the Digital Marketing Acts,
[2197.36 --> 2199.62]  those are very nice pieces of legislation.
[2199.82 --> 2202.48]  And I don't think I've ever had those words come out of my mouth before.
[2203.00 --> 2204.70]  You know, I've sat down, I've read them.
[2204.90 --> 2205.92]  They're easy to read.
[2206.10 --> 2206.88]  They're clear.
[2207.02 --> 2207.64]  They're concise.
[2208.36 --> 2211.42]  You know, anybody with a high school education can understand them.
[2211.72 --> 2213.54]  It's the way that it needs to go.
[2213.54 --> 2220.48]  I'm wondering, part of me is thinking about this conversation as someone who is producing
[2220.48 --> 2221.10]  data.
[2221.48 --> 2227.90]  But then another part of me is thinking about this conversation like someone in a business
[2227.90 --> 2230.28]  or organization that is using data.
[2230.58 --> 2230.78]  Right.
[2230.78 --> 2235.62]  So, like, there's one side of it that, like, I own my data.
[2235.80 --> 2239.80]  I would love to, you know, benefit on that and maybe make money on that.
[2240.04 --> 2242.06]  I certainly see that.
[2242.18 --> 2247.96]  And then I'm thinking, oh, well, if I'm thinking that and I'm a person in a company that wants
[2247.96 --> 2254.64]  to actually build a model or an analytics system or something using that data, that changes
[2254.64 --> 2261.80]  how that, you know, how that business entity then thinks about its strategy of building
[2261.80 --> 2262.80]  that product.
[2262.80 --> 2263.20]  Right.
[2263.20 --> 2267.18]  So from your perspective, maybe shifting to that other perspective.
[2267.18 --> 2272.90]  So if I'm sitting in the company and I see, okay, well, these things are changing.
[2273.04 --> 2277.36]  People are going to be able to exchange their data for money.
[2277.82 --> 2280.76]  There's going to be this exchange.
[2281.60 --> 2287.58]  How, from your perspective, should we start shifting our thinking as analytics professionals
[2287.58 --> 2293.62]  or AI professionals to, like, how we would approach maybe architecting our systems or
[2293.62 --> 2297.78]  how we would approach, like, starting out a project and how we're thinking about data
[2297.78 --> 2299.34]  on that project, that sort of thing?
[2299.70 --> 2300.86]  Yeah, that's a great question, Daniel.
[2301.14 --> 2306.38]  If you are doing analytics the way that I've been doing it for decades now, you don't have
[2306.38 --> 2307.00]  to change anything.
[2307.62 --> 2312.10]  You know, I've worked for, I've been part of consulting firms and software firms and services
[2312.10 --> 2312.54]  firms.
[2312.70 --> 2315.26]  And now I'm part of a biopharmaceutical firm.
[2315.26 --> 2319.00]  You know, there's lots of data inside those companies that you don't have to pay for.
[2319.30 --> 2320.16]  You know, you're part of the company.
[2320.28 --> 2320.98]  You get that for free.
[2321.40 --> 2326.06]  Other data that you are going to use and that you use today and that we use today that you're
[2326.06 --> 2330.72]  going to have to augment and want to augment to get to that 10, 12, 13 sources of data
[2330.72 --> 2333.36]  I was talking about earlier, you're going to have to pay for all that data anyway.
[2334.06 --> 2337.52]  So, you know, you're going to pay somebody for that value-added data.
[2337.80 --> 2339.92]  And in the future, you're going to pay somebody.
[2340.02 --> 2341.18]  It's just going to be a different somebody.
[2341.30 --> 2341.76]  That's all.
[2341.76 --> 2346.24]  You know, so now you really don't have to think about it in any different way.
[2346.66 --> 2351.20]  You may have to budget, you know, a little bit more money for it, but it doesn't dramatically
[2351.20 --> 2352.60]  change the way you do things.
[2353.04 --> 2355.42]  I have a follow-up to that real quick, if you don't mind.
[2355.78 --> 2361.84]  Would it be right to think, you know, we think of, you know, stores of value in terms of money,
[2361.84 --> 2363.24]  and we've been talking about money.
[2363.74 --> 2367.96]  In recent years, we've looked at cryptocurrencies and we're starting to think of those as stores
[2367.96 --> 2370.70]  of value and forms the currency themselves.
[2371.18 --> 2373.88]  Should we be thinking of data in a direct way?
[2373.96 --> 2379.34]  Because we've kind of talked like one step removed so far, but is data money in the way
[2379.34 --> 2380.72]  that we should be thinking going forward?
[2381.12 --> 2381.42]  It is.
[2381.66 --> 2382.32]  Data is money.
[2382.54 --> 2383.42]  There's no doubt about it.
[2383.58 --> 2384.42]  Data is cash.
[2384.90 --> 2389.12]  You know, you're either going to pay for using it or you're going to use it to generate value
[2389.12 --> 2390.50]  on the back end.
[2390.70 --> 2392.92]  You know, it's just, it is that way.
[2392.92 --> 2396.44]  You know, Daniel touched on it lightly earlier in the conversation.
[2397.02 --> 2399.70]  Most people think of Google as a search engine and they are.
[2399.88 --> 2400.66]  There's no doubt about it.
[2400.72 --> 2406.16]  It's the most popular search engine by far in the world, but they're a huge data shop.
[2406.34 --> 2412.22]  They're a huge advertising organization, you know, and, you know, we buy in my day job,
[2412.34 --> 2414.40]  we buy data from Google all the time.
[2414.66 --> 2420.34]  You know, we go through the B2B interface of Google and we buy their geolocation data.
[2420.34 --> 2424.90]  We buy travel data, we buy advertising, we buy all sorts of things from Google.
[2425.10 --> 2428.38]  So, you know, it's, it's just the way it is.
[2428.46 --> 2429.60]  You know, data is money.
[2430.18 --> 2435.66]  I wonder, it's triggering so many things in my mind, like the sort of market around data.
[2435.86 --> 2442.54]  It seems like it could get very, very complicated and sort of multi-tiered in the sense that like
[2442.54 --> 2446.56]  there's people generating data, but there's people that could buy data, right?
[2446.56 --> 2451.32]  And if data is money and that money escalates in value, right?
[2451.38 --> 2457.04]  All of a sudden you've got a sort of market for, for this thing that, you know, increases
[2457.04 --> 2458.60]  in value over time.
[2458.60 --> 2463.22]  And there's like an investing element to it as well, which is, which is quite interesting.
[2463.22 --> 2471.28]  One, one other feature of this that I see you touch on, on the book is like derived or synthetic
[2471.28 --> 2477.24]  data, which, which I think is quite interesting because Chris and I have talked about this a
[2477.24 --> 2483.02]  number of times on the podcast in relation to privacy and the fact that if you are able
[2483.02 --> 2489.68]  to augment your data sets, especially as a professional with derived or synthetic data,
[2489.68 --> 2496.04]  you can actually do things maybe beyond what you would be able to do with the amount of
[2496.04 --> 2502.60]  data that, that you have, that's maybe cleaned and detoxed and has no privacy issues.
[2502.60 --> 2507.30]  So I don't know, could you, could you touch on that a little bit and maybe how you see
[2507.30 --> 2514.26]  the, the methods and usage of generated data and synthetic data kind of progressing as we
[2514.26 --> 2514.78]  move forward?
[2515.14 --> 2515.78]  Yeah, absolutely.
[2515.78 --> 2520.26]  And it's a great topic to talk about and I love to get into it with, with the analytics
[2520.26 --> 2525.56]  professionals all the time is that, you know, we've, we've gone past the era of aggregations
[2525.56 --> 2527.96]  and averages and integrating data.
[2528.18 --> 2529.16]  We still integrate data.
[2529.30 --> 2534.00]  Of course, it's a powerful tool for us, but you know, if you really want to get somewhere
[2534.00 --> 2538.90]  today and have competitive advantage, you are probably going to have to derive data from
[2538.90 --> 2544.26]  multiple data sets to come up with indicators and, and, you know, functions and things that don't
[2544.26 --> 2545.38]  exist other places.
[2545.86 --> 2551.38]  You will have to create something that is proprietary and unique to the way that you see the world
[2551.38 --> 2553.20]  and you, you, you're approaching the world.
[2553.32 --> 2554.40]  That's derived data.
[2554.48 --> 2557.96]  You take, you know, travel data, location data, and you bring it together and you have
[2557.96 --> 2559.36]  a whole new set of data there.
[2560.02 --> 2562.38]  Synthetic data usually comes up at least to now.
[2562.38 --> 2566.70]  And today it comes up where you have industries where people are really not watching them
[2566.70 --> 2572.22]  very closely and you don't have access to proprietary data because the small number of people in
[2572.22 --> 2574.02]  those industries won't give it to you.
[2574.30 --> 2576.48]  They're smart enough to hold onto it then for themselves.
[2577.14 --> 2581.68]  So then you have to synthesize and create the data to measure that industry from the outside
[2581.68 --> 2582.52]  and you can do it.
[2582.60 --> 2583.42]  We're doing it today.
[2583.72 --> 2588.12]  We just did a project where, where we did that and it's worked out very, very well for
[2588.12 --> 2588.36]  us.
[2588.52 --> 2593.22]  So you can derive data from, from existing sources, bringing them together and coming
[2593.22 --> 2598.66]  up with a whole new data set, or you can actually synthesize the data and create it from different
[2598.66 --> 2601.38]  indirect measures that you can see from the outside.
[2601.38 --> 2606.82]  I have one small follow-up to that, that is intriguing me a little bit to start with.
[2606.94 --> 2610.82]  You've definitely changed the way I'm thinking about it in terms of the monetization of data.
[2611.28 --> 2615.84]  We have these exchanges, which are giving us the ability to place a market value on it.
[2615.84 --> 2618.72]  And so I'm, I'm definitely moving into that mindset.
[2619.04 --> 2624.02]  And so if I look at the analogy for a moment back to cryptocurrencies, when we talk about
[2624.02 --> 2629.22]  synthetic, there is a mathematical limitation in terms of the compute required to generate
[2629.22 --> 2630.14]  new value there.
[2630.42 --> 2636.16]  If you're going to look at synthetic data and place value on it, you know, in a, in a monetary
[2636.16 --> 2639.94]  sense, uh, in an exchange, how do we regulate that?
[2640.00 --> 2645.00]  It seems like there could potentially be the ability that if you're really going into a new
[2645.00 --> 2649.10]  business, maybe this is several years in the future, exchanges are widespread and we're
[2649.10 --> 2654.40]  seeing an industry built around the monetization of data specifically at that point, you know,
[2654.42 --> 2658.06]  here in the U S and people are synthesizing data to do that.
[2658.32 --> 2662.40]  How is that not printing money potentially, or is that just one of those gotchas we got
[2662.40 --> 2663.48]  to figure out going forward?
[2663.74 --> 2666.46]  We're going to have to figure that out as we go, you know, go forward.
[2666.70 --> 2668.00]  That's something that we'll see.
[2668.14 --> 2670.84]  And there'll be all sorts of people stretching and pushing the boundaries.
[2670.84 --> 2673.68]  And we'll have to look at those edge cases as they come to be.
[2674.18 --> 2677.64]  One thing that I'll throw on the table that, that might be interesting for you and your
[2677.64 --> 2683.04]  listeners is what industry in the United States has generated the most millionaires over the
[2683.04 --> 2683.60]  last decade?
[2683.96 --> 2684.90]  Over the last decade.
[2685.52 --> 2686.02]  I don't know.
[2686.12 --> 2686.72]  Social media.
[2687.18 --> 2687.66]  I don't know.
[2687.80 --> 2691.00]  I would guess something like along those lines, but I don't know either.
[2691.40 --> 2692.10]  Market research.
[2692.96 --> 2693.88]  Market research.
[2694.32 --> 2698.94]  There's more market research organizations in the United States that are run by entrepreneurs
[2698.94 --> 2701.48]  that have become millionaires than any other business.
[2702.40 --> 2702.46]  Interesting.
[2703.10 --> 2703.38]  Yeah.
[2703.94 --> 2704.64]  And it's all data.
[2705.12 --> 2707.06]  There's nothing to those businesses other than data.
[2707.06 --> 2711.32]  And that sort of brings me to, to a last question, John.
[2711.70 --> 2718.08]  We've talked a lot about different elements of this and certain ones that are maybe like
[2718.08 --> 2722.54]  Chris was saying, he was disturbed by certain things and other things that are maybe cool.
[2722.54 --> 2725.72]  Cause I'm going to be me making an extra two grand each year.
[2725.72 --> 2732.56]  So, you know, that's positive as you look at, you know, where things are headed, what,
[2732.68 --> 2740.38]  what in a sort of positive way excites you about kind of the future of maybe the, the
[2740.38 --> 2747.28]  professions associated with, with data, whether that be analytics or AI or how those professions
[2747.28 --> 2752.16]  are shifting under this, this changing climate, what, what kind of excites you about that?
[2752.16 --> 2756.56]  And you're looking forward to, yeah, this is, you know, the, some people, you know, look
[2756.56 --> 2759.56]  at the book and they come away from it and go, oh my gosh, this is terrible.
[2759.84 --> 2763.02]  Everything's, you know, it's, it's, it's all been a sham and I don't understand, you
[2763.02 --> 2766.50]  know, the overlords have been manipulating me and all this kind of stuff.
[2766.50 --> 2768.36]  And it's like, no, that's not the takeaway from the book.
[2768.60 --> 2771.12]  The takeaway is that, you know, we're all waking up.
[2771.42 --> 2772.62]  We're all in a new era.
[2772.94 --> 2778.30]  We need to throw off the regulations and the structures that we were using from a hundred years
[2778.30 --> 2780.88]  ago today and look at where we are today.
[2781.52 --> 2785.70]  And, you know, there's the EU is putting in the, in the structures and the frameworks that
[2785.70 --> 2786.72]  we need to leverage.
[2786.86 --> 2792.88]  And we all just need to look at how we want to monetize our data and how we can have that
[2792.88 --> 2797.48]  be part of our life that is beneficial and positive each as individuals.
[2797.76 --> 2802.10]  Now, as far as the data and analytics profession goes, I'm bullish.
[2802.10 --> 2807.66]  You know, there's, you know, if we took every high school student and college student and
[2807.66 --> 2812.78]  graduate student in America and turn them into data scientists, we might have a 10th of
[2812.78 --> 2813.34]  what we need.
[2813.68 --> 2817.32]  So, you know, there's lots and lots and lots of jobs, you know, all these people that are
[2817.32 --> 2820.78]  wringing their hands and saying, oh, you know, the future is nigh.
[2820.90 --> 2824.80]  And, you know, our children won't have the same level of lifestyle we had.
[2824.98 --> 2825.62]  That's bunk.
[2825.98 --> 2829.88]  There's lots of opportunity out there around the data and analytics fields.
[2829.88 --> 2832.38]  And that alone would employ everybody.
[2832.78 --> 2834.18]  Not everybody's going to want to do that.
[2834.30 --> 2838.52]  We need, you know, we need people to make chairs and dig ditches and run factories and
[2838.52 --> 2839.38]  those kinds of things too.
[2839.88 --> 2845.40]  But, you know, data and analytics is a very, very bright spot for all of us, you know, and
[2845.40 --> 2850.38]  that's, I had both of my kids go through, you know, two big 10 schools, Michigan and Illinois,
[2850.38 --> 2853.90]  and they're both engineers and they both work with data every day.
[2854.08 --> 2857.94]  So, you know, I'm living my own truth right there.
[2857.94 --> 2860.86]  And it's way better than digging ditches, I got to say.
[2861.16 --> 2861.86]  I dug ditches.
[2861.96 --> 2866.52]  I dug graves when I was a kid and it's no fun being a grave digger.
[2866.62 --> 2868.26]  I can attest to that.
[2868.84 --> 2869.48]  Yeah, yeah.
[2869.74 --> 2870.96]  Or painting fences.
[2871.20 --> 2872.58]  That was my first one.
[2873.14 --> 2875.66]  John, it's been a real pleasure.
[2876.26 --> 2880.72]  Your book is available now on early access and on Manning.
[2881.10 --> 2885.52]  We do have a permanent discount code with Manning, 40%.
[2885.52 --> 2887.70]  That's pretty amazing.
[2888.38 --> 2888.86]  40%.
[2888.86 --> 2893.38]  So listeners, the code is PODPracticalAI19.
[2893.94 --> 2896.26]  And we'll put that in our show notes as well.
[2896.44 --> 2898.44]  So please take a look at that.
[2898.52 --> 2902.06]  We'll put the link to the book in there along with John's other books.
[2902.24 --> 2903.74]  It's been a real pleasure, John.
[2903.74 --> 2906.84]  We're excited to see the book take off.
[2906.96 --> 2911.32]  And also, whatever you write next, we'll be excited to have you back on the show.
[2911.96 --> 2912.74]  I'd love to.
[2912.98 --> 2914.38]  I enjoyed the conversation.
[2914.74 --> 2916.16]  I'm sorry to have freaked you out, Chris.
[2916.82 --> 2917.80]  I'll get over it.
[2918.04 --> 2920.16]  But yeah, when the new book comes out, we'll do it again.
[2920.16 --> 2929.72]  All right.
[2929.88 --> 2931.44]  That is our show for this week.
[2931.68 --> 2934.06]  If you dig it, don't forget to subscribe.
[2934.64 --> 2937.26]  Head to PracticalAI.fm for all the ways.
[2937.76 --> 2943.20]  And if Practical AI has benefited your life, pay it forward by sharing the show with a friend or colleague.
[2943.54 --> 2946.50]  Word of mouth is the number one way people find shows like ours.
[2946.50 --> 2952.52]  Thanks again to Fastly for fronting our static assets, to Fly.io for backing our dynamic requests,
[2953.08 --> 2955.76]  to BreakmasterCylinder for the beats, and to you for listening.
[2956.02 --> 2956.66]  We appreciate you.
[2956.92 --> 2957.86]  That's all for now.
[2958.08 --> 2959.58]  We'll talk to you again on the next one.

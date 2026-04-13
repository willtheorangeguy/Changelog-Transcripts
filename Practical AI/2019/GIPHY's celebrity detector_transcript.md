[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[15.72 --> 20.34]  This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 --> 25.10]  And we're excited to share they now offer dedicated virtual droplets.
[25.10 --> 29.04]  And unlike standard droplets, which use shared virtual CPU threads,
[29.04 --> 32.88]  their two performance plans, general purpose and CPU optimized,
[33.40 --> 36.08]  they have dedicated virtual CPU threads.
[36.42 --> 40.86]  This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 --> 45.20]  So if you have build boxes, CI, CD, video encoding, machine learning, ad serving,
[45.50 --> 49.98]  game servers, databases, batch processing, data mining, application servers,
[50.18 --> 54.92]  or active front end web servers that need to be full duty CPU all day every day,
[55.14 --> 57.92]  then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 --> 61.26]  Pricing is very competitive starting at 40 bucks a month.
[61.66 --> 66.38]  Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 --> 69.02]  Again, do.co slash Changelog.
[69.02 --> 86.38]  Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 --> 88.56]  productive, and accessible to everyone.
[88.94 --> 93.44]  This is where conversations around AI, machine learning, and data science happen.
[93.92 --> 98.20]  Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 --> 99.38]  Follow us on Twitter.
[99.48 --> 100.96]  We're at Practical AI FM.
[101.46 --> 102.28]  And now onto the show.
[106.82 --> 111.64]  This is Daniel Whitenack, one of the co-hosts of Practical AI.
[111.94 --> 114.52]  I'm a data scientist with SIL International.
[114.96 --> 123.18]  I'm joined today by my co-host, Chris, who is a chief AI strategist with Lockheed Martin RMS APA Innovations.
[123.32 --> 123.96]  How are you doing, Chris?
[124.06 --> 124.50]  Doing great.
[124.56 --> 125.48]  How's it going today, Daniel?
[125.48 --> 126.44]  It's going great.
[126.44 --> 128.00]  We were just talking before the show.
[128.10 --> 130.26]  I'm dealing with a few allergy issues.
[130.40 --> 132.82]  I think you are too, but it's that time of year, I guess.
[133.08 --> 133.46]  It is.
[133.56 --> 137.68]  So a couple of coughs here and there's a normal part of a podcast as far as I'm concerned.
[137.98 --> 138.14]  Yep.
[138.26 --> 140.98]  Well, are you up to date on your pop culture, Chris?
[141.12 --> 141.86]  I'm trying.
[142.12 --> 145.84]  I'm looking forward to learning a whole lot more on this episode.
[145.84 --> 154.26]  So my wife and I have been listening or watching Jeopardy now that it's on Netflix during our dinners recently.
[154.26 --> 158.70]  And I fail often at the pop culture categories.
[158.70 --> 175.76]  So I'm really glad that we have Nick Hasty from Giphy with us today, who is an expert in such areas, but also an expert in AI to talk about some of the work they're doing in AI at Giphy and where that crosses with pop culture and other things.
[175.94 --> 176.54]  So welcome, Nick.
[176.74 --> 176.94]  Hi.
[177.12 --> 177.78]  Thanks for having me.
[177.82 --> 178.50]  It's great to be here.
[178.66 --> 178.86]  Yes.
[179.48 --> 183.48]  Extensive pop culture knowledge is a prerequisite here at Giphy.
[183.48 --> 185.36]  Yeah, I assume so.
[185.82 --> 189.90]  So hopefully I can do a little bit better at Jeopardy after the show.
[190.38 --> 190.50]  Yeah.
[190.62 --> 194.28]  So Nick is the director of research and development at Giphy.
[194.56 --> 203.54]  Nick, do you want to just give us a little bit of background about yourself, how you got into tech, how you got into AI and how you ended up at Giphy?
[203.78 --> 204.30]  Yeah, for sure.
[204.32 --> 204.94]  I'd be happy to.
[205.56 --> 207.82]  I've got kind of a varied background, to be honest.
[208.44 --> 211.34]  So I'm currently director of R&D here at Giphy.
[211.34 --> 213.56]  We're in New York, New York, and I live in Brooklyn.
[213.84 --> 215.58]  So I grew up in Georgia, actually.
[216.52 --> 218.06]  Ah, that's where I'm at.
[218.22 --> 218.38]  Okay.
[218.48 --> 219.64]  Good for you.
[219.88 --> 220.46]  Georgia rocks.
[220.90 --> 221.48]  Canton, Georgia.
[221.62 --> 223.56]  It's like about an hour and a half north of Atlanta.
[223.74 --> 224.64]  I'm in Kennesaw.
[224.82 --> 225.22]  I know.
[225.38 --> 225.82]  No kidding.
[226.12 --> 227.52]  And I grew up in Cobb County.
[227.70 --> 232.40]  So for those who don't know the Atlanta metro area, I'm sorry, but we're practically neighbors growing up.
[232.58 --> 233.22]  Yeah, totally.
[233.40 --> 236.02]  I feel a little left out here, but I'll let you guys continue.
[236.10 --> 236.60]  I'm so sorry.
[236.80 --> 237.88]  Yeah, that's really funny.
[238.02 --> 238.72]  Small world.
[239.32 --> 240.04]  Atlanta's doing good.
[240.04 --> 243.66]  So then, yeah, I went to University of Georgia as an undergrad, and I was actually an English major.
[244.02 --> 250.58]  And always dabbled in computing in terms of, like, custom Doom mods and, like, music technology stuff.
[250.66 --> 256.76]  I was big into music, and I actually didn't really get into, you know, web stuff and more computer science until grad school.
[256.76 --> 262.36]  When I went to an interactive telecommunications program called ITP at NYU.
[262.36 --> 267.02]  It's kind of an art technology school in the Tisch School of the Arts.
[267.02 --> 273.38]  And they kind of take a bunch of random people who are good at a lot of different stuff and throw technology at them.
[273.68 --> 280.90]  Anything from algorithms and, you know, visualizations, data, data, data, stuff to, like, actual light, electrical engineering.
[281.24 --> 282.72]  Just kind of see where you end up.
[282.72 --> 287.66]  So I was, like, historically very into, like, creative tech stuff and even, like, art proper.
[288.00 --> 293.20]  So after ITP, I started working for the new museum here in New York.
[293.42 --> 296.38]  They have a new media art branch called Rhizome.
[296.78 --> 299.22]  And it's been around since the mid-'90s.
[299.30 --> 306.04]  It started off as a listserv, and it's now a website and museum and an archive and stuff where they house digital art.
[306.04 --> 308.32]  It's like an internet art organization.
[308.70 --> 314.32]  I was a director of technology there for a number of years, and I got a lot of my web chops there.
[314.78 --> 324.76]  And being at Rhizome, we were very invested in the GIF early on because it was, I mean, the GIF is, like, a purely internet media, I guess you could say.
[324.84 --> 326.12]  It's, like, something that was really born.
[326.52 --> 329.80]  I mean, it predates the internet, but, I mean, it really came to its own.
[330.04 --> 334.24]  Yeah, once upon a time, there were only GIFs and JPEGs on the internet, you know, for images.
[334.24 --> 336.08]  Yeah, like old.
[336.22 --> 342.80]  Well, it's also, it's like a primary communication technique now, almost, native to the internet.
[342.98 --> 346.00]  It's a really wild kind of trajectory that the GIF has had.
[346.30 --> 347.60]  It's been really interesting to see.
[347.82 --> 352.22]  So, yeah, when I was at Rhizome, we would do, like, art shows where, like, the artists would only work in the GIF format.
[352.98 --> 355.26]  This is, like, the early, not early 2000s.
[355.26 --> 360.06]  This is, like, well, they did stuff in the art shows like that since the 90s and the 2000s.
[360.06 --> 363.84]  And I started in the late 2000s there and I've worked hard on their digital archives.
[363.98 --> 368.30]  So, it was a lot of archive digital assets, including animated GIFs and those kinds of things.
[368.50 --> 370.54]  And after that, I started working.
[370.86 --> 374.82]  I was kind of, like, teaching myself Node and I was building a GIF maker tool.
[374.82 --> 382.34]  And through school, I was introduced to, through a schoolmate, I was introduced to Alex Chung, GIF's founder.
[382.70 --> 390.48]  He was at Betaworks and he had just been pulled in as, like, they were doing, like, a seed program for a number of different startup people.
[391.06 --> 392.78]  Alex is kind of like a serial entrepreneur.
[392.78 --> 399.60]  He's been in the game for many, many, many years and just has tremendous technical knowledge and just, like, business expertise.
[399.60 --> 405.46]  And he was looking for an engineer to build a team and we met and talked and just really hit it off.
[405.64 --> 410.26]  And so, they started working at GIFI the next day and this was GIFI's first week.
[410.38 --> 413.34]  So, I was technically GIFI's first employee for a while.
[413.48 --> 414.26]  There were two founders.
[414.82 --> 416.28]  A guy named Jace Cook was the other founder.
[416.58 --> 417.28]  And then Alex.
[417.46 --> 421.18]  And then I was working, building the website and Alex was building the API.
[421.58 --> 425.26]  And we were just kind of cranking for a while and the team continued to grow.
[425.26 --> 428.92]  So, yeah, I mean, we definitely, GIFI kind of took off like a rocket.
[429.26 --> 430.08]  It was very interesting.
[430.20 --> 433.10]  I think it was a really cool way that it worked out.
[433.16 --> 434.38]  It was, like, the time and the place.
[434.56 --> 436.78]  Like you were just saying, Daniel, the GIF.
[437.00 --> 439.32]  It was coming into its own, I think, with bandwidth increases.
[439.92 --> 442.80]  And, you know, it wasn't taking, like, 10 minutes for a GIF to load.
[442.92 --> 444.64]  You know, in Tumblr, dumping GIFs everywhere.
[444.74 --> 445.50]  There was a whole way.
[445.86 --> 453.18]  I think on Tumblr, people really started kind of communicating with GIFs and using GIFs as reactions and using GIFs as a communications medium.
[453.18 --> 457.88]  You got, like, pop culture and all these kind of different things you can load into a GIF.
[458.38 --> 464.24]  And, you know, so it's like if a celebrity is saying hello, you know, you got all these kind of different layers of meaning that you can unpack.
[464.40 --> 468.58]  And it became kind of a, you know, really interesting way for which people to interact with each other online.
[468.58 --> 470.00]  And we kind of realized that.
[470.38 --> 476.98]  And our goal was to just, you know, since GIFs are so old and since they kind of work everywhere.
[476.98 --> 484.24]  I mean, at this time, it was 2013, so, like, there was still, like, contention around which video codec to use on the web.
[484.46 --> 489.14]  And, you know, somebody supported, you know, Firefox supported this, but Safari supported that.
[489.24 --> 491.42]  But, like, no matter what, the GIF was supported everywhere.
[491.96 --> 496.32]  It was definitely an old format and, you know, overweight and kind of slow.
[496.48 --> 503.46]  But it's kind of universal ability to just load and play in anything, including, like, iMessage way, way back in the day.
[503.46 --> 511.88]  So, I guess at this point, with you guys being going for quite a few years at this point, what does GIFI Research do now, now that you've kind of grown into a full organization?
[512.08 --> 514.90]  What are the typical types of things that your researchers are engaged in?
[515.06 --> 522.52]  Yeah, so fast forward now, I've kind of moved out of engineering and I'm more, I guess I'd say more, I'm like a product director person.
[522.94 --> 524.48]  So, I run the R&D team.
[525.10 --> 527.96]  We are within the search division.
[528.68 --> 529.84]  So, our earlier...
[529.84 --> 532.60]  How big is GIFI in general, just to get a sense?
[532.60 --> 533.56]  Yeah, that's a good question.
[533.66 --> 534.52]  There's about 100 people.
[534.70 --> 537.18]  There's roughly 75 in New York.
[537.64 --> 540.78]  In LA, we have our own content creation studio.
[540.98 --> 542.38]  So, there's, like, artists and animators out there.
[542.44 --> 543.52]  There's about 25 of those.
[543.92 --> 547.72]  Engineering-wise, we're probably 30 to 40 at this point.
[548.10 --> 548.28]  Yeah.
[548.38 --> 549.56]  That's a good-sized organization.
[549.74 --> 552.10]  You're definitely past the early startup phase.
[552.30 --> 552.96]  Oh, yeah, totally.
[553.06 --> 555.16]  It's been a wild ride to see that happen.
[555.44 --> 556.40]  There's a lot of people here now.
[556.58 --> 561.22]  And it's awesome to have a lot of super talented people here taking care of the things that, you know, just like,
[561.22 --> 563.26]  that you could never deal with in the past.
[563.52 --> 567.60]  And just now we're just so much more mature and so much more able to handle everything that comes at us.
[567.90 --> 571.64]  So, you know, like I was saying, my background is more like, I like making things.
[571.84 --> 577.82]  And so, I have been able to move into the more of the R&D, like, special projects, the kind of research things,
[577.92 --> 580.44]  find fun stuff, you know, create prototypes for things.
[580.44 --> 583.24]  And then other teams maybe, you know, find value in it and pick it up.
[583.24 --> 591.16]  But, I mean, to be honest, our team, we're a good-sized company, but we're not so big that we can just sit in the back and, like, mix chemicals and, like, play with our thumbs.
[591.26 --> 592.18]  Like, we've got to ship stuff.
[592.54 --> 594.94]  So, maybe one day.
[595.28 --> 595.80]  Maybe one day.
[596.14 --> 603.08]  But, yeah, so my team, alongside the celebrity detector stuff, I mean, we've done, we were kind of the first team to really use deep learning tools.
[603.46 --> 607.40]  Like, Word2Vec, we use this open source model.
[607.40 --> 612.26]  We use that deep learning model, like, all over the place for recommendations and a couple of other things.
[612.38 --> 618.26]  So, like, on the GIFI website, if you go to the GIF detail page, which is, like, a single GIF, all the related GIFs down below,
[618.40 --> 629.06]  like, our team kind of overhauled that and used Word2Vec to take user data to approximate relatedness in terms of how visitors visited the GIFI website in a session.
[629.46 --> 631.30]  We did a similar thing with our tag space.
[631.30 --> 637.26]  So, like, we do, like, related tags and recommended searches using deep learning, Word2Vec specifically.
[637.88 --> 646.84]  We are doing other kind of things now where we're building trending tools using, you know, various types of models, not all deep learning.
[647.00 --> 652.72]  Some just, you know, machine learning or some of them just kind of old school statistical algorithms.
[653.28 --> 655.14]  Doing, like, language prediction stuff.
[655.14 --> 662.58]  We're doing head-to-head comparisons against, like, search results so that we can kind of get a better sense of how our search is performing.
[663.06 --> 668.42]  We had a spell of time in which we were doing a lot of image annotation.
[668.98 --> 671.20]  Obviously, Giphy has a whole lot of GIFs.
[671.38 --> 675.96]  And, you know, we relied on our content team to annotate those for a long time.
[676.44 --> 686.02]  You know, we have, like, a team of people who are ultra-mega pop culture wizards who can, you know, prattle off anybody in a GIF and then all the slubs and everything.
[686.02 --> 690.72]  And, you know, humans can only go so far when you reach the tens of millions in terms of your catalog.
[691.48 --> 692.62]  You know, it strikes me as funny.
[692.72 --> 696.30]  You're the company that can have, like, a pop culture wizard department.
[696.82 --> 697.38]  Oh, yeah, totally.
[697.50 --> 698.10]  I mean, we've got it.
[698.16 --> 699.64]  I mean, it's – we could call it that.
[699.72 --> 707.54]  Our content development team is definitely, you know, people, like – people whose jobs are to watch TV shows and cut GIFs out of them or live GIFs.
[707.70 --> 708.30]  That's not their only thing.
[708.30 --> 709.48]  They do a lot of stuff.
[709.48 --> 710.60]  But, like, we'll watch the live event.
[710.76 --> 723.18]  Like, they'll watch the Oscars and they will cut GIFs of the Oscars in real time and catch all those awesome moments of people with sassy looks or, you know, celebratory speeches and those kinds of things.
[723.32 --> 724.68]  And we'll cut those in real time.
[724.72 --> 732.16]  And we work with partners, movie studios, these kinds of, you know, various other people in the entertainment industry to live GIF events and things like that.
[732.24 --> 733.60]  So, yeah, it's very funny.
[733.60 --> 738.50]  So, how many – I mean, you mentioned a lot of different things that you've done and are doing.
[738.50 --> 745.00]  Like, how many people are on this R&D team working with you to come up with these projects?
[745.28 --> 745.38]  Yeah.
[745.50 --> 746.86]  So, right now, there's five of us.
[747.10 --> 748.14]  We've grown a little bit.
[748.44 --> 752.66]  So, we work with a team in the Ukraine called Rails Reactor.
[753.20 --> 758.72]  And so, I have a guy – Dmitry Wojtek, Ihor Krush are working with us right now.
[758.82 --> 760.46]  We've had a couple of other employees from them.
[760.46 --> 768.82]  But they are really amazing machine learning engineers and kind of the specialists in terms of, like, the algorithms and building out the systems and stuff like that.
[769.16 --> 770.00]  So, we work with them.
[770.52 --> 776.24]  And then GIFI's CTO, Anthony, has – Anthony Johnson works on our team a lot, too.
[776.38 --> 779.40]  He has a pretty extensive background in machine learning and deep learning.
[779.66 --> 782.24]  And so, right now, we're tag-teaming the team.
[782.36 --> 783.08]  It's been really awesome.
[783.08 --> 784.72]  We're, like, really cranking out some stuff.
[785.04 --> 794.54]  So, is it almost like having – between the two organizations working together, kind of almost having a sub-team of deep learning folks inside your R&D organization then?
[794.68 --> 795.08]  Exactly.
[795.26 --> 795.80]  Yeah, totally.
[796.12 --> 802.26]  It's like – you know, like I said, I've kind of moved into more product and vision and strategy and communication.
[802.26 --> 812.40]  I mean, I still will open up a Jupyter Notebook and kind of, like, work on the data a little bit and kind of figure out, like, you know, things around training data and sources and making decisions.
[812.62 --> 816.60]  But in terms of, like, the actual implementation, I don't do that as much anymore.
[816.92 --> 818.16]  Just – just – it's cool.
[818.50 --> 826.48]  So, with it being, like – I mean, obviously, the things that you're building are filtering pretty quickly into the product.
[826.48 --> 829.74]  And you're moving quick and you have a smaller team.
[830.18 --> 832.72]  Do you feel like that – I mean, you are R&D.
[832.92 --> 833.06]  Yeah.
[833.18 --> 839.20]  But R&D in some organizations, like, things take forever to get from R&D to product.
[839.42 --> 845.46]  Do you feel like that has – that's influenced how you approach AI development in one way or another?
[845.76 --> 846.02]  Yeah.
[846.22 --> 854.32]  I think, you know, R&D initially was, like, me trying to end up in a really, really removed kind of fun playland.
[854.32 --> 858.36]  And I'm kind of hoping for that and thinking if I put the name first, then the reality will follow.
[859.20 --> 859.90]  But the truth –
[859.90 --> 860.32]  You can hope.
[860.32 --> 860.60]  Yeah.
[860.88 --> 869.00]  And not that I don't enjoy shipping in, but, you know, with the velocity of Giphy, it would be – I was kind of hoping to, like, slow down and kind of, like, play a little bit.
[869.58 --> 874.28]  But truth be told, I mean, the work we did was, like, had a lot of value.
[874.28 --> 878.00]  It was very obvious that it needed to be integrated into the company itself.
[878.54 --> 881.20]  So, we ship, and it's a goal of ours.
[881.20 --> 884.58]  And I think a lot of companies say, oh, we're going to spin up an R&D team.
[885.08 --> 887.60]  And then, you know, the team disappears and nothing ever shows up.
[887.62 --> 889.22]  And they're like, whoa, what are we throwing money into?
[889.50 --> 891.16]  You know, that can be kind of a gotcha.
[891.36 --> 898.88]  So, we work hard to make sure that, you know, we're doing cool stuff and we're reading papers and, like, we're, like, looking at the latest stuff.
[898.88 --> 907.92]  But we're also then taking what's out there and applying it directly to Giphy so that there is a real value that can be proven and integrated.
[908.36 --> 914.28]  You know, I think my team's probably taken over four or five of the Giphy API endpoints.
[914.64 --> 922.02]  We don't do, like, the actual search algorithm, but we have provided a lot of metadata for the search that gets fed into the search engine.
[922.02 --> 928.88]  But, I mean, like, the Slack integration, we took that over a while ago and we redid it over last summer.
[929.26 --> 934.80]  That's one of Giphy's probably most well-known integrations is, you know, forward slash Giphy and then whatever.
[934.98 --> 937.04]  And then you get kind of a random GIF.
[937.30 --> 938.64]  Historically, it was very random.
[938.86 --> 943.16]  And we really liked the juxtaposition of the weirdness, you know, just kind of, like, the funniness.
[943.38 --> 943.90]  Like, I don't know.
[944.10 --> 945.16]  I mean, I think it...
[945.16 --> 947.18]  Yeah, I remember those days very well.
[947.64 --> 947.86]  Yeah.
[948.16 --> 949.66]  Our philosophy is work is boring.
[950.16 --> 951.44]  You probably don't want to be there.
[951.44 --> 957.52]  So maybe if you can just throw a little weirdness into the mix, you know, it can make things a little funner.
[958.04 --> 973.82]  But, yeah, but since we have taken over that and, you know, applied some learning techniques to that to make it a little smarter and make it a little more on point and measured engagement, you know, it's been like 20 to 30% increases overall in terms of how people have used the integration itself.
[973.82 --> 982.62]  So, like Slack and that endpoint, which is our translate endpoint, our related GIFs endpoint, related tag searches endpoint.
[983.10 --> 983.18]  Yeah.
[983.26 --> 986.92]  So point being, like, the things that we've done, we've been able to prove value in that.
[987.00 --> 990.52]  And then those things have been able to be incorporated by the company as a whole.
[990.52 --> 999.02]  So the AI stuff that you're doing, do you typically have, like, a target value add, like, product-wise when you're going into that?
[999.16 --> 1000.16]  Or is it...
[1000.16 --> 1003.16]  Do some things just start as, like, oh, I wonder if we could do that with GIF?
[1003.58 --> 1004.36]  That's a good question.
[1004.44 --> 1005.14]  A little bit of both.
[1005.14 --> 1022.00]  You know, like, being with the company for so long and not having the media constraints of having to ship very specific things, I kind of wanted to explore the periphery of GIFs products and offerings that have kind of been more lackluster or kind of unexplored or whatever.
[1022.18 --> 1030.00]  Like, you know, our tag space, which is something that, like, no one had really been maintained and it was very flat and it was just kind of no one knew what to do with it.
[1030.00 --> 1031.98]  And then, you know, here comes WordDevick.
[1032.06 --> 1036.76]  Let's see what happens when we throw over the tags in WordDevick and play around like, oh, wow, this is really cool.
[1036.82 --> 1041.04]  We can see interesting relationships between our tags that we never knew existed.
[1041.70 --> 1047.02]  Hey, these are actually better than our current implementation, you know, of how we do related tags.
[1047.14 --> 1049.08]  Let's keep iterating on this product.
[1049.34 --> 1051.00]  And then it becomes like an actual...
[1051.72 --> 1053.92]  replaces the old method in which we were to do that.
[1054.34 --> 1055.64]  So it's kind of...
[1055.64 --> 1056.44]  That's been the approach.
[1056.44 --> 1064.16]  I mean, for the Celeb Detector itself, though, that was something that we've always had a need for tools that can annotate images.
[1064.58 --> 1069.40]  Like I was saying earlier, due to like, you know, just general human constraints around our content team.
[1069.62 --> 1072.50]  As obvious, you know, entertainment, celebrities, that's our bread and butter.
[1072.90 --> 1080.40]  So if we have a tool that can annotate these GIFs as they come in through uploads and crawls and that kind of stuff and help us surface those things, that's a value add.
[1081.00 --> 1084.94]  But that being said, it was always something we wanted to open source.
[1084.94 --> 1093.54]  And it was always something we wanted to do to kind of demonstrate where Giphy is and what we're doing and kind of the different intersections we exist at.
[1093.74 --> 1105.24]  Because, I mean, people, I think, given Giphy's kind of distributed nature, like, oh, I know you from Slack or, oh, I see you in Facebook Messenger or Instagram Messenger or, oh, I use stickers on Instagram or whatever.
[1105.38 --> 1107.62]  People don't always know, like, what it is.
[1107.62 --> 1109.18]  It's kind of this amorphous thing.
[1109.18 --> 1117.22]  So this was kind of a flag in a way to say, hey, you know, this is kind of we're doing these things, using these technologies, the things we're thinking about.
[1117.84 --> 1119.94]  And this is the data that we have to deal with.
[1120.02 --> 1126.78]  So, like, the list of the celebrities that we trained in, those are taken from our top 50,000 celebs that people search for.
[1127.12 --> 1129.98]  So these are the celebrities that people actually care about.
[1129.98 --> 1133.28]  Like, there are celeb detection systems out there.
[1133.42 --> 1137.32]  I mean, you know, I think Microsoft has one that you can pay for.
[1137.52 --> 1139.24]  There's a couple of third-party hosts.
[1140.00 --> 1154.80]  But those services, while they may have a large number of classes in which they can provide, they didn't always hit the ones that we needed because we tended to just be more on the cutting edge in terms of, like, what's going on in popular culture and celebrity culture.
[1154.80 --> 1161.34]  Sure. So, you know, the thesis was we can really demonstrate that we can do the tech, we can build something interesting and fun.
[1161.76 --> 1167.42]  We have a very unique set of data that is not necessarily handled by other people.
[1167.56 --> 1178.28]  So we can kind of, you know, put all our different ingredients into this, like, stew and then give it to people as a way to, if you're new to deep learning or if you're new to these kinds of things, we can open this up for people.
[1178.28 --> 1180.54]  And GIFs are fun and easy.
[1180.76 --> 1182.42]  I mean, it's a nice entry point.
[1182.42 --> 1192.72]  Like, if people are slightly intimidated by machine learning or deep learning or any of these technologies, you know, GIFs and celebrities is kind of like a nice spoonful of sugar to help people kind of dive in.
[1193.00 --> 1205.26]  I mean, I've always personally found that when I'm working with fun content or working on a fun project, I tend to learn the technology better that way as opposed to just reading a book or, you know, hammering stuff out in the class.
[1205.26 --> 1209.04]  I'm like, I want to build something and I want to incorporate this fun thing and this fun thing.
[1209.26 --> 1214.84]  And, you know, if I end up needing like some deep learning algorithm or whatever to make it happen, that's cool.
[1215.18 --> 1216.44]  Yeah, that was kind of the thought behind that.
[1216.44 --> 1225.66]  This episode is brought to you by Discover.Bot.
[1225.86 --> 1229.84]  Learn everything there is to know about bots at Discover.Bot slash Practical AI.
[1230.38 --> 1238.26]  Discover.Bot was built by Amazon Registry Services as an online community for bot creators and makers of all skill levels to learn from one another, to share stories.
[1238.26 --> 1248.48]  And they regularly publish guides and resources to answer questions like how to set up payments to your bot, how to stop shopping cart abandonment, what KPIs are worth measuring, how to write an engaging chat bot dialogue.
[1248.92 --> 1250.86]  You can even register .bot domains there.
[1250.86 --> 1255.82]  Learn more and explore this huge library of bot resources at discover.bot slash practical AI.
[1256.22 --> 1258.74]  Again, discover.bot slash practical AI.
[1268.26 --> 1286.78]  So, Nick, to take you back, we kind of leapt right into the full company, but I actually want to ask you a question about you described when you had come into the company and, you know, you were having that conversation and the next day you were doing it.
[1286.78 --> 1292.10]  But even possibly before that, as you know it, how did the project itself come about?
[1292.10 --> 1298.42]  What was its genesis and also why were celebrities the thing that you moved to or was there anything before that?
[1298.64 --> 1301.34]  The project, you mean the celebrity editor or Giphy itself?
[1301.78 --> 1303.06]  Maybe describe both of them.
[1303.16 --> 1306.24]  Maybe kind of discriminate between the two and where they each were.
[1306.36 --> 1307.00]  Yeah, totally.
[1307.26 --> 1319.10]  So for Giphy itself, so Alex Chung, who is the founder, he built, he's just a perennial creator, like dude who just, you know, just makes stuff all the time and has worked in the internet industry for a long time.
[1319.10 --> 1329.26]  And he kind of, he caught on the Giphy thing and he built a Giphy search engine that was just a website that he kind of built on his own and he launched it and it would immediately, he got some traction.
[1329.96 --> 1336.84]  I think it was like a press article and crashed and burned and because of it's just the influx of traffic.
[1337.30 --> 1346.00]  And so Betaworks, which is a New York City incubator slash, you know, venture capital firm, they knew Alex and they were introduced to him.
[1346.00 --> 1349.14]  And Alex was like, I got this thing building and, you know, they're a cool company.
[1349.24 --> 1352.72]  They are very aware of culture and art and technology.
[1353.32 --> 1355.92]  And we're like kind of got what Alex is up to.
[1356.36 --> 1356.96]  And they're like, let's.
[1357.18 --> 1361.78]  Our episode with Hugging Face, Clem mentioned them as well.
[1361.90 --> 1362.42]  Okay, right on.
[1362.48 --> 1362.92]  Yeah, totally.
[1363.26 --> 1365.18]  So they understood what Alex was trying to do.
[1365.60 --> 1371.84]  And so they were like, they had a hackers in residence program and they brought Alex on and his, to build Giphy.
[1371.84 --> 1377.28]  And then, you know, Alex, within the first week of Alex working there, I was introduced.
[1377.52 --> 1381.46]  I was doing contract work and I had been working on a Giphy stuff.
[1381.60 --> 1389.46]  I had been working on Giphy stuff already at my previous job at Ryzone and I was building a Giphy creator because at the time in 2013, there was no good way to really make Gips on the web.
[1389.78 --> 1393.32]  And I met Alex through mutual friend and we just like really hit it off.
[1393.44 --> 1397.92]  And I had already kind of been, you know, it was very evident that we would probably do good together.
[1397.92 --> 1399.82]  And so I just started working the next day.
[1400.04 --> 1401.02]  So that was 2013.
[1401.66 --> 1405.82]  Flash forward six years, I'm doing the R&D stuff.
[1406.30 --> 1410.20]  And, you know, the impetus is like, you know, Giphy is we do a lot of different things.
[1410.26 --> 1414.78]  People know us in different ways, but let's really flex and demonstrate how the cool tech we're doing.
[1415.24 --> 1422.50]  I think people may have an idea of like the volume and the gifts and we serve and like kind of the scale of which we do.
[1422.60 --> 1424.74]  I mean, we serve a couple billion gifts every day.
[1424.74 --> 1437.64]  But I don't know if anyone, people know kind of like about the more interesting kind of projects that happen in-house and how working at Giphy is working at like working with interesting technology at the nexus of culture and entertainment.
[1438.16 --> 1441.42]  So the Slub Detector, you know, kind of embodied this.
[1441.72 --> 1446.86]  We could do this project, say, hey, you know, Giphy, we do deep learning.
[1447.08 --> 1447.70]  We're working hard.
[1448.20 --> 1450.78]  We've had this experiment kind of happening in the background.
[1451.26 --> 1453.72]  We use this tool in-house to annotate our gifts.
[1453.72 --> 1459.06]  But, you know, the real goal is to like put it out there for people, hopefully get some press.
[1459.18 --> 1463.50]  Hopefully people are interested in it and also be excited about the community itself.
[1463.66 --> 1467.90]  I mean, like any startup, you know, like we use tons and tons of open source projects.
[1468.12 --> 1474.30]  And Giphy would not exist categorically if it wasn't for, you know, awesome open source projects.
[1474.68 --> 1483.16]  So our success, we want to give some of it back and be able to demonstrate some of the things we've picked up and learned along the way and give something that, you know, people could play with.
[1483.16 --> 1484.42]  So, yeah, that was where it came.
[1484.70 --> 1485.08]  Cool. Yeah.
[1485.18 --> 1487.88]  So, I mean, that describes a lot of the motivation.
[1488.08 --> 1488.54]  I'm curious.
[1488.96 --> 1492.06]  You've talked about how the Celeb project came about.
[1492.32 --> 1499.20]  I'm wondering, like, you talked about previously using like Word2Vec and other things for related gifts and all of that.
[1499.30 --> 1499.46]  Yep.
[1499.46 --> 1513.38]  So, in particular on the Celeb Detector project, as you moved into that space, what were the kind of different things that you needed to learn tech-wise to be able to accomplish that that you weren't doing before in your AI work?
[1513.38 --> 1514.98]  Yeah, that's a good question.
[1514.98 --> 1518.64]  I mean, we hadn't done a lot of ConfNet stuff.
[1519.26 --> 1527.18]  A lot of the image recognition object detection stuff we had used a lot of third parties for, you know, like API.
[1527.66 --> 1534.80]  Like, you're not going to build – if you need a generalized model for object detection and images, like, you're not necessarily going to train your own for that.
[1534.80 --> 1538.10]  So, we didn't necessarily need that in-house.
[1538.68 --> 1545.14]  But for the celebrity detection one, yeah, it was – this was, like, our first real extensive deep learning project.
[1545.66 --> 1548.22]  So, there was a lot of experimentation in the background.
[1548.48 --> 1554.54]  I mean, first, you know, it was, like, just getting the data together against our searches.
[1554.76 --> 1558.02]  Like, we had a lot of images around some of these celebrities.
[1558.60 --> 1559.68]  Some of them we didn't.
[1559.90 --> 1563.28]  So, we had to, like, scour the web a little bit to build the image data set.
[1563.28 --> 1569.40]  And then making sure we had, you know – and this is probably, like, any real machine learning or deep learning project.
[1569.64 --> 1572.04]  But, you know, making sure the labels were good.
[1572.24 --> 1580.84]  Like I had mentioned earlier, you know, Giphy's tag system has been going for a while and was kind of big and difficult to carry or difficult to manage in some ways.
[1580.94 --> 1583.76]  And so, we used Figure 8.
[1584.26 --> 1585.42]  It used to be Cropflower.
[1585.58 --> 1589.42]  We used them to help us make sure that the labels that we had for the celebrities was really good.
[1589.42 --> 1594.90]  And then I think since it is face detection, we did use previous existing models.
[1595.46 --> 1601.92]  So, just finding the right one that we wanted to kind of do the – to build ours of ended up being the ResNet 50.
[1602.62 --> 1605.18]  I think that was – all that, you know, was pretty standardized.
[1605.38 --> 1615.00]  I think a lot of it kind of got a little more hairy when it became things like clustering and finding out how to, like, group our faces together.
[1615.00 --> 1622.52]  So, when our team used the center loss approach for face recognition, that was like a real – in the blog post, I linked to the paper.
[1622.86 --> 1628.20]  When we used that approach, that kind of really – the results really dramatically increased.
[1628.62 --> 1630.22]  That was, like, a big gateway.
[1630.22 --> 1636.68]  So, when you're saying – I know in the blog post, which we'll link in the show notes, by the way, so make sure and check that out.
[1637.36 --> 1647.94]  But you mentioned kind of the, like, face vectors, face detection, and then this clustering bit, which you just mentioned around, like, using center loss.
[1648.28 --> 1659.62]  So, like, could you describe a little bit, for those that aren't familiar, like, what do you mean when you say, like, these faces are kind of, like, encoded or vectorized, and then we're doing, like, clustering with center loss?
[1659.62 --> 1661.76]  What does that process really mean?
[1661.88 --> 1663.54]  What are you doing when you're doing that?
[1663.86 --> 1664.10]  Yeah.
[1664.46 --> 1673.04]  So, and again, I'm more of the product person at this point, so I'm going to try to, like, give my high level – I wasn't into weeds as much on that stuff.
[1673.06 --> 1673.34]  Yeah, no worries.
[1673.46 --> 1673.84]  No worries.
[1674.24 --> 1679.98]  But, yeah, when you have a face coming in to the network, you make an embedding of it so that it becomes, like, a series of numbers or whatever.
[1680.20 --> 1681.60]  Yeah, so it's, like, face to numbers.
[1681.84 --> 1682.28]  Yeah, exactly.
[1682.28 --> 1682.40]  Exactly.
[1682.76 --> 1691.02]  And so then for all the faces that have a numerical representation, and what you want to do is be able to find similar faces and be able to match them.
[1691.44 --> 1703.58]  So if a new face comes in, when you translate that face into a group of numbers, you want to be able to check it against the previously existing groups of numbers that kind of live within the model to come up with a prediction.
[1703.58 --> 1712.82]  So for us, you know, there are pre-existing models, like I was saying, like the ResNet that can take an image and make it into a vector.
[1713.32 --> 1724.34]  And so that wasn't so hard, but finding the right way to take the vectors and cluster them and group them in such a way that when a new face vector came in, we can make an accurate prediction.
[1724.70 --> 1726.60]  That was definitely the biggest challenge for us.
[1726.60 --> 1730.26]  So you mentioned that you had selected, you know, ResNet 50.
[1730.60 --> 1734.78]  What kind of tools were using, was the team using to be able to do it?
[1734.86 --> 1739.04]  Was this TensorFlow or PyTorch or, you know, MXNet?
[1739.36 --> 1740.22]  Do you have any sense?
[1740.50 --> 1742.18]  Yeah, we, yeah, totally.
[1742.48 --> 1744.16]  So we went with PyTorch.
[1744.72 --> 1747.54]  We played with TensorFlow a little bit, but PyTorch was great.
[1747.64 --> 1748.88]  I mean, we've kind of fell in love with it.
[1749.02 --> 1751.70]  I guess it's very Pythonic to say.
[1751.70 --> 1757.22]  TensorFlow and Python has its own kind of idioms and its own kind of ways in which it wants to be used.
[1757.40 --> 1762.02]  But PyTorch felt it was kind of easier to, it's just more malleable, we would say.
[1762.10 --> 1764.12]  And it was, it allowed us to iterate faster.
[1764.64 --> 1766.42]  It allowed us to kind of experiment quicker.
[1766.90 --> 1768.16]  So yeah, we really fell in love with that.
[1768.20 --> 1769.64]  And that's kind of become our go-to.
[1769.84 --> 1772.20]  And the code that we released is all in PyTorch.
[1772.38 --> 1772.52]  Cool.
[1772.64 --> 1772.82]  Yeah.
[1772.92 --> 1778.70]  So I'm kind of wondering, as I'm thinking, like, you're building this face detector bit, which vectorizes the faces.
[1778.70 --> 1780.88]  You've got this clustering bit.
[1781.64 --> 1787.68]  And I'm just imagining, like, pop culture in general, like, there's so much of, it's so dynamic, right?
[1787.76 --> 1792.66]  Like, there's going to be new celebrities that are super popular in a super short period of time.
[1792.66 --> 1804.70]  So have you thought about it, like, how that influences how you kind of manage and deploy the model in the sense of, like, as new celebrities come onto the scene, how you're updating it over time,
[1804.70 --> 1811.76]  how, like, you're swapping out models in terms of, like, serializing them out of PyTorch and then swapping them out in a service or something?
[1811.86 --> 1815.34]  Like, how do you think about that sort of updating stuff over time?
[1815.54 --> 1816.14]  Yeah, for sure.
[1817.08 --> 1822.02]  I mean, we'll probably continue adding to the model based on, you know, the search queries that come in.
[1822.16 --> 1826.66]  Because it's like, we want to be able to identify the celebrities that, like, our users are searching for.
[1826.66 --> 1831.70]  And that, by its nature, tends to be the more of the newer, the cutting edge stuff.
[1831.88 --> 1836.44]  So we'll continue to, I'm not sure when the next time we will, because we've got other projects going on.
[1836.46 --> 1841.78]  But at some point in the future, we'll probably do another big sweep across our searches and see who we're missing.
[1842.20 --> 1844.02]  Can I ask a follow-up to that before you move on?
[1844.14 --> 1844.62]  Yeah, yeah.
[1844.62 --> 1845.36]  I'm just curious.
[1845.36 --> 1855.86]  So when you're tying, you know, the business side, so a new celebrity comes on the scene and you guys are going through some sort of process about, you know, hey, we got to add this in.
[1855.98 --> 1858.14]  And you have this deep learning model out there.
[1858.32 --> 1867.72]  How are you connecting the business side and the technical side together in a meaningful way to where you're able to get on top of it quickly and make it work and get it deployed out?
[1867.96 --> 1871.16]  What's the connection between the business side and the deep learning team?
[1871.16 --> 1876.86]  I would say in terms of like, you mean in terms of like making this value proposition to the business?
[1877.14 --> 1877.92]  Yeah, like process.
[1878.06 --> 1887.12]  Like how does it go from somebody who has nothing to do with deep learning is maybe watching the celebrity scene saying, oh, there's somebody else that we need to start paying attention to.
[1887.26 --> 1892.82]  How does that get into a task level action from the deep learning team?
[1892.92 --> 1894.44]  You know, how does that move across there?
[1894.68 --> 1894.94]  Totally.
[1894.94 --> 1902.38]  I mean, I usually I'm in pretty good contact with like our content development team and they're kind of in charge of all the latest pop culture stuff.
[1902.52 --> 1912.38]  And I work closely with them through this to get the for them to go through the list of celebs to approve the different ones and make sure there's nothing bad or weird in there.
[1912.38 --> 1920.00]  And they can certainly, you know, as things bubble up, they can hit us up and be like, hey, you know, this person's really growing.
[1920.26 --> 1921.44]  Can we add them at some point?
[1921.88 --> 1926.58]  And we'll probably wait, obviously, because training is it takes, you know, a little time, obviously.
[1926.58 --> 1928.88]  And we have to make sure we got the right data set.
[1928.98 --> 1936.06]  So as we hit a certain kind of set of new celebs, we'll probably just do one big training and then re-release the model after that.
[1936.40 --> 1938.36]  Hasn't been a huge ask so far.
[1938.36 --> 1949.74]  I mean, in terms of business value, I think this isn't something where we're like, hey, Giphy's got an API that we offer to everyone that's part of the Giphy API so you can get celebrity predictions.
[1950.16 --> 1954.58]  You know, it's not like this isn't the proposition was never deep learning as a service.
[1954.82 --> 1963.66]  It was always like, let's do this thing in-house, set it up in-house and then also give it out to other people to kind of show how we do things in-house.
[1963.66 --> 1971.72]  That's why we included like some ops oriented code like Docker and those kinds of things to show how we're our philosophy now for deploying those kinds of things.
[1971.98 --> 1973.42]  Yeah, that's much appreciated, by the way.
[1973.52 --> 1973.72]  Yeah.
[1973.88 --> 1981.86]  We've actually been working with for some of the latest stuff that we're doing, looking into Kubeflow and specifically Selden.
[1982.44 --> 1987.28]  I don't know if you guys are familiar with that because we use Kubernetes here at Giphy for all our architecture and deployments and stuff.
[1987.28 --> 2002.42]  And Kubeflow seems pretty magical and awesome, especially Selden because it'll give you gRPC and REST APIs kind of out of the box and handles all the model management, all those kinds of things that historically have been, you know, they feel a little ad hoc.
[2002.58 --> 2010.62]  I think everyone kind of just does what they can like, oh, put it on S3 and then download it or put it directly into, you know, the image or something.
[2010.62 --> 2012.36]  That's kind of where we're moving towards.
[2012.46 --> 2017.44]  It seems like a sustainable and kind of a very efficient way to handle machine learning, deep learning deployments.
[2017.84 --> 2020.66]  Yeah, that community is moving forward really quickly.
[2020.90 --> 2024.50]  I know Chris and I are both big fans of things that are going on there.
[2024.84 --> 2034.86]  And in our last episode, so the one that will air prior to this one, we talked about some AI infrastructure and Selden was mentioned there and Kubeflow too.
[2034.86 --> 2038.36]  And just a lot of the great things that are going on in the Kubernetes community.
[2038.88 --> 2045.64]  So I definitely encourage people to check that stuff out and check out that episode if you want more details there as well.
[2046.02 --> 2052.30]  Specifically, so you kind of moved to talking a little bit about how you really wanted people to try this out.
[2052.64 --> 2062.94]  You realized that there wasn't a great open source tool for this and you wanted to release it and kind of put your foot down somewhere in terms of your open source contributions.
[2062.94 --> 2069.84]  I'm wondering, like being the probably the greatest experts on using AI for GIFs.
[2069.94 --> 2077.24]  I was wondering, you know, for those that are interested in this subject, and maybe they'll look at the GitHub repo, which we'll link in the show notes.
[2077.60 --> 2086.66]  What are kind of the unique challenges of using GIF data in AI models as opposed to like videos or images, like single images?
[2086.66 --> 2091.22]  Does it carry over like the same techniques, like you mentioned, convolutional neural networks?
[2091.52 --> 2094.84]  Some of that I imagine carries through frame by frame or something like that.
[2095.48 --> 2100.44]  How different is working with GIFs and AI models than working with videos and images?
[2100.86 --> 2101.06]  Yeah.
[2102.28 --> 2105.56]  It's like you said, you know, we do it frame by frame for the most part.
[2105.88 --> 2108.80]  You know, we use a com net and just kind of iterate through the frames.
[2108.80 --> 2112.80]  The challenges, though, are just like, and I mean, video is kind of the same way.
[2112.98 --> 2117.92]  And truth be told, we do transcode like all our GIFs into different video formats.
[2118.36 --> 2120.76]  And so we don't always work exclusively with GIFs.
[2121.00 --> 2125.52]  Sometimes it is easier just to, you know, if you're doing some stuff to just work with a video file or whatever.
[2125.90 --> 2129.86]  But, you know, the challenges are, well, number one, the format's heavy.
[2130.30 --> 2131.56]  You know, it's kind of a hefty format.
[2131.56 --> 2137.36]  So the compression algorithm is, is it Limpel Ziv Welch or whatever?
[2137.62 --> 2139.14]  It's older, right?
[2139.62 --> 2142.76]  And it's like kind of dictionary based from what I remember.
[2143.30 --> 2146.16]  So it compresses, but it's still a big format.
[2146.58 --> 2151.52]  You know, it still suffers from like, well, it hasn't been able to take advantage of like all the things that happen in video.
[2151.84 --> 2156.24]  So it's really just like a bunch of images that are squashed together into this file.
[2156.24 --> 2158.86]  And the player just kind of goes through each of the frames.
[2158.86 --> 2165.28]  And there's metadata at the beginning and end of the file that kind of say, here's the speed and here's the colors and those kinds of things.
[2165.66 --> 2167.46]  GIFs are also limited in the color palette.
[2167.88 --> 2177.22]  So if you have a high quality video or high quality image and then you transfer it over to GIF, you know, each frame is only limited to like 256 colors, I believe.
[2177.22 --> 2190.90]  So you're going to lose some coloration there, which could very well affect how your machine learning system, you know, how your deep learning system like interprets the image properties of it and determines the values.
[2191.26 --> 2199.26]  So ideally, you know, you would, if you can, it's good to work with this high quality, as high quality of images as you can in order to say your model can be the most accurate.
[2199.26 --> 2201.74]  So those are the kind of the main thing.
[2201.86 --> 2206.74]  And it's just slowness to like, you know, if you're moving with big files and it takes longer to train and it takes longer.
[2207.10 --> 2209.38]  If you're moving stuff over the wire, that takes slower.
[2209.74 --> 2212.66]  So those are kind of the biggest challenges I would say that we had to deal with.
[2212.94 --> 2214.34]  And maybe this happens with video too.
[2214.34 --> 2225.52]  But if you have, so, you know, if a GIF has 90 frames or 120 frames, it may become the situation where like evaluating every frame is not their best option just because of the overhead involved or the time involved.
[2225.62 --> 2232.58]  So you got to like do some sampling across frames and then figuring out which frames to sample and then, you know, how you want to aggregate it and how you want to.
[2232.58 --> 2242.80]  If the end result is a single prediction of a celebrity, getting to that single prediction by looking at a single GIF, which could count 100 frames, maybe multiple faces, those kinds of things.
[2243.14 --> 2249.26]  Since there are so many frames there and more than one frame, one more than one, the frames are different.
[2249.66 --> 2251.98]  So more than one face could appear in a frame or not.
[2252.56 --> 2260.24]  So you do have to play a lot with, like I was saying earlier, with the clustering and how you want to group things in order to end up with that single prediction.
[2260.24 --> 2262.86]  So there was a lot of time spent in that component.
[2263.22 --> 2265.02]  So I wanted to ask a quick question.
[2265.10 --> 2269.54]  I noticed in the blog post, you talked about testing the model for different types of bias.
[2269.78 --> 2271.86]  And that kind of piqued my curiosity.
[2271.96 --> 2274.38]  I was wondering if you could give us a little bit of detail on that.
[2274.50 --> 2275.12]  Yeah, for sure.
[2275.32 --> 2276.52]  We want to do another bias.
[2276.74 --> 2278.98]  I mean, we want to do another blog post around that specifically.
[2278.98 --> 2292.18]  But I mean, it's been a it's been in the news, obviously, that, you know, there are biases built in to or like certain models that have been released, you know, tend to have different biases around race or gender or these kinds of things.
[2292.18 --> 2294.74]  And we were kind of curious to see about that.
[2294.74 --> 2308.70]  We took all the classes and I think our methodology was to we wanted to see the representation of cultures, you know, just in terms of our data set to make sure that it wasn't something that was leaning any one specific way.
[2308.78 --> 2315.80]  Like we wanted to make sure that we had a big, accurate, like a wide swath of people who were kind of being identified.
[2316.26 --> 2316.36]  Sure.
[2316.64 --> 2318.16]  That's a big challenge for a lot of folks.
[2318.28 --> 2318.72]  For sure.
[2318.72 --> 2321.94]  And then making sure that, you know, those identifications are proper.
[2322.22 --> 2329.16]  So, yeah, we we looked at the different names and we checked out their I think we used Wikipedia, you know, to get their ethnicities.
[2329.40 --> 2333.48]  And then we kind of did a breakdown and kind of see which ways we'd skewed.
[2333.62 --> 2336.22]  And there wasn't any kind of like major red flags.
[2336.32 --> 2339.30]  You know, we had I mean, Giphy itself, you know, we're a younger company.
[2339.44 --> 2341.50]  Most people who work here, you know, are millennials.
[2341.50 --> 2343.66]  So, like, we're very sensitive to these kinds of things.
[2343.66 --> 2350.70]  And our user base, you know, tends to be kind of proper representation of, you know, genders and diversity, those kinds of things.
[2350.86 --> 2354.98]  So, yeah, we found the classes that we had was like, you know, a good representation.
[2354.98 --> 2361.42]  And there wasn't any kind of like overweight in terms of any single ethnicity or like gender or whatever.
[2361.84 --> 2370.58]  So we put up the this is probably one of my favorite things about the whole project is that we there's a link in the blog post to the vector space of all the faces that we have.
[2370.58 --> 2371.74]  Yeah, that was super cool.
[2371.90 --> 2372.68]  I checked that out.
[2372.68 --> 2384.34]  Yeah. And you can really see it's interesting to see how a computer or when you take an image and you crunch it down into numbers and then you group those numbers together and then you reequate those numbers with faces.
[2384.34 --> 2391.66]  It's cool to see how the computer actually groups faces together based on their properties, you know, skin tone and hair color and all these kinds of things.
[2391.66 --> 2399.98]  So it was really funny to see celebrities to look alike or who had shared similar characteristics in their face that you had never, never seen.
[2399.98 --> 2405.72]  In fact, I mean, to be honest, like our maybe our very favorite thing about this whole thing was within the company itself.
[2406.00 --> 2410.06]  Everyone would upload their own face and then they would get their celebrity prediction.
[2410.40 --> 2422.52]  And there was like a huge email thread that the company shared out where everyone was like, oh, look, you know, my match is Brad Pitt or oh, you know, I'm Jennifer Lawrence or Idris Elba or whatever, you know, everyone's got their ego stroked a little bit.
[2422.52 --> 2434.26]  Yeah, that's awesome. I for one, I was just thinking while you're doing or while you're talking about open sourcing things and having that online, it's something I need to I need to try out and share the results with my wife.
[2434.32 --> 2436.76]  I'm sure she would be interested to see that.
[2436.90 --> 2442.00]  But yeah, I really appreciate you taking time to go through the project with us.
[2442.18 --> 2443.58]  Just great work on everything.
[2443.58 --> 2452.50]  I really appreciate your your practical perspective on things and also appreciate you, you know, diving into some of the finer points of things like bias and other things.
[2452.58 --> 2455.24]  We'll look forward to that, that follow up blog post.
[2455.44 --> 2458.46]  But yeah, I think all of this will be linked in the show notes.
[2458.66 --> 2464.60]  So Nick mentioned the 3D face embedding explorer, the GitHub repo, the blog post.
[2464.74 --> 2466.34]  We'll link all of that in the show notes.
[2466.34 --> 2467.06]  So check it out.
[2467.14 --> 2469.40]  But thank you so much for joining us, Nick.
[2469.40 --> 2474.72]  This has been really fun and I've definitely learned a few things about GIF along the way.
[2475.08 --> 2476.90]  And I learned a few things about pop culture.
[2477.14 --> 2478.82]  Hey, my job here is done then.
[2479.92 --> 2482.90]  What, right as we finish out, do you have a favorite GIF?
[2484.22 --> 2485.08]  I do.
[2485.46 --> 2491.38]  And so within the Reddit release, when I released, when we put it on Reddit, someone asked for the favorite GIF and I put it there.
[2491.38 --> 2492.60]  It's Vince McMahon.
[2492.72 --> 2494.58]  Do you know Vince McMahon from World Wrestling?
[2494.88 --> 2498.04]  He is like this crazy showman with insane faces.
[2498.04 --> 2504.14]  And there's a meme situation where he has this progressively more audacious reaction to images.
[2504.46 --> 2510.20]  So there's this one where there's this bodybuilder dude and then Vince McMahon looks at him and keeps getting more and more excited until he falls out of a chair.
[2510.44 --> 2512.20]  And it's just, it just encapsulates, I don't know.
[2512.30 --> 2513.16]  It's just really, really funny.
[2513.26 --> 2516.20]  And that whole Vince McMahon meme format for me, I don't know.
[2516.48 --> 2520.30]  Maybe this is the Georgia in me talking about wrestling.
[2520.56 --> 2522.56]  But yeah, that's maybe my all-time favorite.
[2522.72 --> 2523.00]  Awesome.
[2523.00 --> 2529.70]  Yeah, I think wrestling is uniquely suitable there to that GIF format, you know, with the expressions and the exaggeration in it.
[2529.88 --> 2530.80]  It's incredible drama.
[2531.16 --> 2541.16]  Yeah, we've got some great wrestling, just totally ridiculous wrestling gifts that I could just watch over and over and just kind of ponder what the hell, what's all happening within this thing.
[2541.36 --> 2541.58]  Yeah.
[2541.84 --> 2542.24]  Awesome.
[2542.50 --> 2545.48]  Well, we'll make sure and add that link to the show notes as well.
[2545.48 --> 2547.60]  But thank you so much, Nick.
[2547.64 --> 2548.40]  It's been great.
[2548.50 --> 2549.22]  Thanks for joining us.
[2549.44 --> 2549.72]  Of course.
[2549.78 --> 2550.14]  My pleasure.
[2552.52 --> 2552.98]  All right.
[2553.02 --> 2555.64]  Thank you for tuning into this episode of Practical AI.
[2555.90 --> 2557.36]  If you enjoyed the show, do us a favor.
[2557.48 --> 2558.86]  Go on iTunes, give us a rating.
[2559.14 --> 2561.00]  Go in your podcast app and favorite it.
[2561.08 --> 2563.84]  If you are on Twitter or social network, share a link with a friend.
[2563.92 --> 2566.26]  Whatever you got to do, share the show with a friend if you enjoyed it.
[2566.54 --> 2569.22]  And bandwidth for ChangeLog is provided by Fastly.
[2569.34 --> 2570.78]  Learn more at Fastly.com.
[2570.78 --> 2574.18]  And we catch our errors before our users do here at ChangeLog because of Rollbar.
[2574.18 --> 2576.78]  Check them out at Rollbar.com slash ChangeLog.
[2577.08 --> 2579.60]  And we're hosted on Linode Cloud servers.
[2579.96 --> 2581.58]  Head to Linode.com slash ChangeLog.
[2581.66 --> 2582.12]  Check them out.
[2582.18 --> 2583.02]  Support this show.
[2583.36 --> 2586.60]  This episode is hosted by Daniel Whitenack and Chris Benson.
[2587.04 --> 2589.12]  The music is by Breakmaster Cylinder.
[2589.50 --> 2592.94]  And you can find more shows just like this at ChangeLog.com.
[2593.16 --> 2595.08]  When you go there, pop in your email address.
[2595.38 --> 2601.40]  Get our weekly email keeping you up to date with the news and podcasts for developers in your inbox every single week.
[2601.80 --> 2602.58]  Thanks for tuning in.
[2602.58 --> 2603.50]  We'll see you next week.
[2604.18 --> 2623.02]  All right.
[2623.02 --> 2626.20]  Because you've stuck in here to the end of the show, got a surprise for you.
[2626.58 --> 2629.14]  Here's another preview of our upcoming show called Brain Science.
[2629.14 --> 2631.52]  This podcast is for the curious.
[2631.86 --> 2639.10]  We explore the inner workings of the human brain to understand behavior change, habit formation, mental health, and the complexities of the human condition.
[2639.46 --> 2645.30]  It's hosted by myself, Adam Stachowiak, and my good friend, Muriel Reese, a doctor in clinical psychology.
[2645.86 --> 2651.56]  It's about brain science applied, not just how the brain works, but how we apply what we know about the brain to better our lives.
[2651.92 --> 2652.52]  Here we go.
[2652.52 --> 2659.00]  That applied brain science really stood out to me because I don't want it to just be data.
[2659.36 --> 2661.04]  I want you to go, how can this fit?
[2661.16 --> 2662.04]  What can I take away?
[2662.34 --> 2663.72]  Now, how am I going to change?
[2664.08 --> 2674.44]  And that that sort of is where you come in more and even some of the questions like, so like I want to ask you, what are some of the most challenging things working in the tech world when it comes to relationships?
[2674.44 --> 2677.00]  Probably the most important one is isolation.
[2677.46 --> 2684.36]  More and more of the world and companies are being, for good reasons, they're being okay with what they call distributed teams.
[2684.80 --> 2684.90]  Yeah.
[2685.02 --> 2689.20]  And that means that you and I, we work for the same company, but you work from your home office.
[2689.32 --> 2690.30]  I work from my home office.
[2690.30 --> 2704.72]  Because I might go into the office a couple times a week if I live local, but even if I live in San Francisco, I'm still probably a remote worker, even though I can hop in an Uber or hop on, you know, the train or whatever and go into the office and be there in a half hour.
[2704.76 --> 2705.74]  But why waste the time?
[2706.24 --> 2711.38]  You know, and this is where I would revisit what I want to talk about with resonance.
[2711.38 --> 2719.08]  And that whenever we're learning, no matter what thing, it's really helpful when we get feedback that's both immediate and specific.
[2719.98 --> 2726.94]  And so when you're by yourself and you don't have any interaction with other people, how can you get any feedback?
[2727.48 --> 2737.50]  I mean, you're losing most of the nonverbal communication and you also don't have all of the voice inflections or facial expression.
[2737.50 --> 2743.10]  Have you ever tried to, you know, be sad, feel sad and smile at the same time?
[2743.86 --> 2744.24]  Try it.
[2745.46 --> 2746.86]  It's pretty hard.
[2747.26 --> 2747.76]  Right.
[2747.84 --> 2754.96]  Because facial expression is exactly what's involved when it comes to empathy, which is relationships.
[2755.52 --> 2766.16]  I was reading a research article recently and it talked about, you know, how couples who are together a really long time end up sort of looking like each other.
[2766.16 --> 2766.20]  Yeah.
[2766.74 --> 2767.36]  Never heard that.
[2767.36 --> 2767.76]  Yeah.
[2768.66 --> 2777.24]  And so what they've looked at is when we actually empathize with other people, facial expression is really key within that.
[2777.80 --> 2789.48]  And so when you empathize with the partner you're with over and over and over again, your face begins to make the same creases and facial expression as it relates to where somebody else is emotionally.
[2789.88 --> 2790.44]  Wow.
[2790.72 --> 2791.10]  Right.
[2791.72 --> 2792.28]  Say it in.
[2792.34 --> 2793.22]  So that's creepy.
[2793.22 --> 2802.08]  Well, again, this is sort of the hotbed when it comes to neuroscience these days is mirror neurons.
[2802.72 --> 2806.26]  And these mirror neurons are what are involved with empathy.
[2806.56 --> 2811.48]  And so mirroring, meaning I get another person's emotional world.
[2811.48 --> 2816.38]  And so one of the research studies looked at Botox.
[2817.00 --> 2824.64]  And what they found is that Botox, because it actually assists in paralyzing facial muscles.
[2824.78 --> 2825.06]  Right.
[2825.18 --> 2828.26]  But then you can't contort your face so you don't get wrinkles.
[2828.68 --> 2831.48]  But actually levels of empathy go down.
[2831.96 --> 2832.66]  Uh-uh.
[2833.42 --> 2833.94]  Right.
[2833.94 --> 2836.88]  Because your physical appearance can't reflect your inner appearance.
[2837.36 --> 2837.76]  Yeah.
[2838.18 --> 2838.86]  You got it.
[2839.24 --> 2845.54]  And so when you're working in these remote locations, it might facilitate better work or more focus.
[2845.54 --> 2851.48]  And it allows people to be distributed and to capitalize on the talents across the country.
[2851.48 --> 2851.78]  Right.
[2852.24 --> 2852.68]  Yeah.
[2852.92 --> 2853.24]  Wow.
[2853.36 --> 2855.82]  So that's like a treasure trove, in my opinion.
[2855.82 --> 2855.90]  Yeah.
[2856.32 --> 2861.48]  Talking about in a scientific way, you know, not just like, hey, this is my opinion.
[2861.84 --> 2862.06]  Yeah.
[2862.06 --> 2863.68]  About all the cons of that.
[2864.06 --> 2868.62]  Because I think what we can do is still have remote work, but do it in more healthy ways.
[2868.94 --> 2873.66]  Because I'm fully, I mean, I've been self-employed remote worker since 2006.
[2874.14 --> 2875.44]  Now I'm a unique animal.
[2875.84 --> 2876.98]  I know that.
[2877.08 --> 2878.12]  My wife knows that.
[2878.34 --> 2878.78]  Right.
[2878.80 --> 2879.64]  And I'm fine with it.
[2879.94 --> 2881.96]  I'm a good human being, but I've got some flaws.
[2881.96 --> 2884.96]  And I'm willing to accept and share those to some degree.
[2884.96 --> 2893.30]  And I think the problem is we just, we just lack more, maybe a more purposeful or intentional feedback loop.
[2893.42 --> 2893.80]  Yeah.
[2893.96 --> 2900.06]  Which I think is super important to being able to operate in this world in just good ways.
[2900.16 --> 2904.84]  I don't know, healthy ways is probably the best way to use in this show context is healthy ways.
[2906.80 --> 2908.74]  That's a preview of Brain Science.
[2908.74 --> 2908.88]  Brain Science.
[2908.88 --> 2916.40]  If you love where we're going with this, send us an email to get on the list to be notified the very moment this show gets released.
[2916.74 --> 2919.86]  Email us at editors at changelog.com.
[2919.98 --> 2925.40]  In the subject line, put in all caps, Brain Science with a couple bangs if you're really excited.
[2925.88 --> 2930.18]  You can also subscribe to our master feed to get all of our shows in one single feed.
[2930.18 --> 2936.10]  Head to changelog.com slash master or search in your podcast app for Change Log Master.
[2936.22 --> 2936.82]  You'll find it.
[2937.14 --> 2941.26]  Subscribe, get all of our shows and even those that only hit the master feed.
[2941.40 --> 2943.42]  Again, changelog.com slash master.
[2943.42 --> 2958.84]  Make sure you don't like drag one lagi more time.
[2960.10 --> 2962.70] oru.com
[2962.70 --> 2963.18] ancies
[2963.18 --> 2967.96]  If the maker of child ceеловanya has probably answered, then more punishable.

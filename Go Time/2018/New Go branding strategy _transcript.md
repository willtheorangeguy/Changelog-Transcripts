[0.46 --> 1.52]  And we're live, too.
[1.90 --> 2.96]  You want a little music?
[4.28 --> 4.70]  Yeah.
[4.84 --> 5.58]  You want some music?
[5.88 --> 6.30]  Gosh.
[7.32 --> 8.78]  Let's get some music going here.
[8.92 --> 10.20]  This is our 8-bit, Steve.
[10.30 --> 11.22]  What do you think about the 8-bit?
[13.30 --> 13.74]  Hmm.
[14.14 --> 14.58]  Yes.
[16.12 --> 16.56]  Yes.
[17.20 --> 18.18]  Get it, BMC.
[21.12 --> 21.48]  Woo!
[22.76 --> 23.68]  You like that?
[23.68 --> 30.14]  Adam's just having too much fun with this.
[30.66 --> 31.72]  I got problems, okay?
[31.84 --> 32.54]  I got problems.
[32.70 --> 34.04]  Please do this show without me.
[34.86 --> 37.64]  Bandwidth for Changelog is provided by Fastly.
[37.94 --> 40.08]  Learn more at Fastly.com.
[40.38 --> 43.28]  We move fast and fix things here at Changelog because of Rollbar.
[43.28 --> 45.32]  Check them out at Rollbar.com.
[45.62 --> 47.34]  And we're hosted on Linode servers.
[47.70 --> 49.46]  Head to linode.com slash Changelog.
[50.38 --> 52.28]  This episode is brought to you by Datadog.
[52.28 --> 58.88]  Datadog helps you collect and visualize all kinds of metrics so you know exactly what's going on with your Go app.
[59.02 --> 68.76]  With over 200 integrations, including AWS, PostgreSQL, Kubernetes, and Go, you have access to all the information you need in one place.
[68.92 --> 78.50]  Datadog provides you with real-time visibility from built-in and customizable dashboards, algorithmic alerts, end-to-end request tracing, and real-time collaboration.
[78.92 --> 82.22]  Start a free trial, and Datadog will send you a T-shirt.
[82.28 --> 85.04]  Head to datadog.com slash GoTime.
[85.04 --> 114.28]  This is GoTime, a panel of Go experts and special guests every single week discussing the Go programming language, the community, and everything in between.
[114.28 --> 118.46]  We record live every Thursday at noon Pacific, 3 p.m. Eastern.
[118.94 --> 120.28]  Tune in at GoTime.fm.
[127.08 --> 130.32]  Welcome back, everybody, to another episode of GoTime.
[130.54 --> 132.28]  Today's episode is number 79.
[133.18 --> 138.06]  And on the show today, we have myself, Eric St. Martin, and Carlicia Pinto.
[138.80 --> 139.42]  Hi there.
[139.42 --> 145.40]  And joining us today from behind the curtains is also Adam Stikowiak.
[146.08 --> 147.16]  It is me.
[147.30 --> 148.12]  I have arrived.
[149.58 --> 155.14]  And our special guest for today is the product lead on the Go team, Steve Francia.
[155.34 --> 155.90]  Welcome, Steve.
[156.78 --> 157.64]  Thanks for having me.
[158.38 --> 163.52]  Now, we've had you on the show before, so I don't know whether we need like a whole intro,
[163.70 --> 168.42]  but do you want to give just kind of a little bit of background about yourself and kind of the role you play on the Go team?
[168.42 --> 171.02]  Maybe what's changed since the last time I talked to you?
[171.10 --> 171.70]  Anything change?
[173.42 --> 176.56]  I've gained weight since the last time you talked to me.
[177.48 --> 179.92]  Aside from your weight, maybe along your role.
[180.10 --> 181.20]  Has anything changed in your role?
[181.60 --> 181.96]  No.
[183.34 --> 187.34]  Yeah, so I've been at Google about 18 months now, a little more.
[187.78 --> 189.24]  Actually, closer to two years.
[189.24 --> 194.72]  I've been the product lead at Google on the Go project the entire time.
[197.12 --> 203.20]  I think I've settled into that role a little bit more over time, but it's been the same role.
[205.54 --> 209.98]  There's not a lot of new with me as far as roles and stuff.
[210.34 --> 211.64]  So, yeah.
[212.18 --> 213.26]  How excited are you?
[213.26 --> 215.68]  It's an exciting time.
[216.02 --> 217.02]  It really is.
[218.80 --> 226.02]  I'll say that I've had some good experiences in my career.
[226.72 --> 236.12]  I've been a part of MongoDB since at the very beginning and took it to when it was the third most popular database.
[236.12 --> 239.82]  I was an early part of Docker.
[240.48 --> 247.46]  So I've had some opportunities to be a part of something when it took off and it transformed.
[248.58 --> 260.64]  And Go is going through what I might even call a second surgence or second surge in that it's really hit its stride.
[261.24 --> 263.30]  And you can feel there's something tangible about it.
[263.30 --> 267.26]  This doesn't happen very often with languages or projects in general.
[268.46 --> 270.90]  And it's just a really exciting thing to be a part of.
[271.88 --> 273.54]  Well, I was actually – sorry.
[273.62 --> 274.08]  Go ahead, Carlicia.
[274.52 --> 278.48]  No, I was going to say – elaborate on that a little more, please.
[278.52 --> 285.40]  What makes you feel this tangible thing that goes going through this second surge?
[285.40 --> 291.60]  So all projects kind of go through ebbs and flows.
[293.00 --> 296.54]  And that's just the nature of life.
[298.28 --> 306.38]  And when I joined the Go project, we weren't tracking as close as we are now growth numbers.
[306.38 --> 313.04]  But it was lower than what we're seeing now by a significant amount.
[314.50 --> 322.72]  And so I'll say in 2017, the Go adoption grew 76%.
[322.72 --> 332.82]  And that means over 700,000 people, developers, adopted Go in 2017.
[333.20 --> 335.56]  Are you tracking that by number of downloads?
[336.50 --> 336.86]  No.
[337.66 --> 338.54]  How are you tracking that?
[339.56 --> 344.40]  We use two different metrics to arrive at that.
[344.40 --> 349.44]  They're both external surveys done of the broad developer community.
[350.10 --> 355.78]  And both of them pay Go as around 7% of developers using it.
[357.62 --> 359.24]  And so that's how we arrive at it.
[359.28 --> 362.00]  So it's the O'Reilly survey and the Stack Overflow survey.
[362.96 --> 364.08]  And we use those.
[364.24 --> 368.42]  And we found those are the most accurate way of telling broad developers.
[368.42 --> 373.42]  And between the two, we figure that's a pretty good check.
[374.30 --> 375.84]  They do appeal to different audiences.
[376.00 --> 377.90]  They don't always get the exact same numbers.
[378.08 --> 380.88]  But they're always pretty close to each other.
[381.50 --> 386.82]  I was at a conference recently, actually, just this past weekend at Zite.
[388.40 --> 389.42]  Small internet company.
[389.56 --> 390.88]  I guess I shouldn't say small.
[391.04 --> 394.06]  It's sort of maybe an up-and-coming cloud service.
[394.54 --> 397.28]  So it's still in a smaller phase compared to other clouds, compared to like.
[397.28 --> 402.88]  And one of the talks had Go in it.
[403.02 --> 410.34]  And it was more like a web front-end, more like a front-ender space, like a front-end developer space than I would imagine even seeing Go.
[410.40 --> 411.94]  And there's Go in there.
[412.48 --> 418.86]  And if you do a little scroll back in the GoTime.fm channel there, you'll see a slide that says,
[419.08 --> 420.44]  Why not write everything in Go?
[422.12 --> 422.92]  I was floored.
[422.92 --> 423.52]  Yeah.
[424.52 --> 431.20]  There's – on top of just the raw numbers, we're seeing the number of conferences expanding.
[432.22 --> 435.66]  We're seeing more participation.
[436.12 --> 438.16]  We're seeing a greater diversity of talks.
[438.16 --> 445.10]  We're seeing talks from more diverse people as well, not just – in all sorts of types of diversity.
[447.26 --> 449.06]  We're seeing an increase of meetups.
[450.62 --> 456.14]  Not a day goes by, really, where you don't see some interesting project that was written in Go happening.
[456.58 --> 460.12]  There's just a lot of excitement happening around the whole ecosystem.
[460.12 --> 462.02]  More conferences?
[463.54 --> 463.82]  Yeah.
[463.86 --> 468.34]  This year we've added five new conferences as far as – if I remember right.
[469.28 --> 474.88]  So I think we're up to 15 or 16 Go – dedicated Go conferences in 2018.
[475.78 --> 476.02]  Wow.
[476.06 --> 478.00]  That's just wild how fast it's grown.
[479.10 --> 479.34]  Yeah.
[479.74 --> 479.98]  Yeah.
[480.04 --> 480.38]  Crazy.
[480.64 --> 481.68]  Crazy to think of.
[481.68 --> 487.44]  I'm excited for Go Europe, which is in Iceland.
[487.66 --> 490.10]  It's coming up in, I think, three or four weeks now.
[492.24 --> 495.48]  But there's – I know this week is Go Singapore.
[497.38 --> 499.44]  There's just a lot of conferences happening.
[499.72 --> 502.08]  It's so much that it's hard to keep up with them all.
[502.52 --> 502.78]  Yeah.
[503.74 --> 505.34]  So let's talk about this branding.
[505.96 --> 509.80]  What prompted Google to do – to take on this project?
[509.80 --> 511.98]  What was the reason behind it?
[513.72 --> 518.38]  So I'll say it was mostly me.
[520.00 --> 522.60]  And so if you want to blame someone, you can blame me.
[523.08 --> 530.22]  But it wasn't anyone from Google corporate that was saying, oh, we need to do Brand Go.
[530.44 --> 533.80]  It came mostly out of, I think, two things.
[533.80 --> 545.72]  So when I joined the team, one of the first things that happened, just a little experience, was we sponsored the .go conference.
[546.56 --> 550.22]  And Andrew had moved to a new project.
[550.40 --> 551.22]  He moved to Upspin.
[552.08 --> 555.80]  And so that left me in charge of sponsorships.
[555.80 --> 561.98]  And so we're sponsoring .go and they asked us for a blurb to go along with our sponsorship.
[563.20 --> 565.98]  And so I started asking everybody, well, what's our blurb?
[566.08 --> 567.46]  How do we talk about Go?
[568.30 --> 570.98]  And nobody had one.
[572.32 --> 574.70]  And we really didn't know.
[574.82 --> 577.68]  And I asked people and I wrote something and I got lots of feedback.
[577.68 --> 579.56]  But I got lots of feedback.
[579.92 --> 581.58]  A lot of it was not consistent.
[583.14 --> 588.16]  And that came with the idea that we really needed a more consistent way of talking about Go.
[589.60 --> 598.60]  And so the idea behind the brand book, the brand guidelines that were published, actually came out of, in spite of it being quite visual,
[598.60 --> 606.02]  the genesis of it came from that we needed a better way to talk about ourselves and what the project was.
[606.12 --> 611.80]  And we needed it clear and we needed to have it very digestible.
[613.10 --> 617.00]  And so that's how the branding actually started completely as text.
[617.74 --> 620.32]  And the visual element was added later to it.
[620.32 --> 631.22]  But if you look at the brand book that we've now published and there's a blog post on blog.golang.org on it,
[631.42 --> 635.30]  you'll see the first part is the brand.
[636.02 --> 638.90]  And that makes up the entire first half of the book.
[639.16 --> 640.08]  And it's all words.
[641.44 --> 643.18]  And they're pretty-looking words, right?
[643.22 --> 645.98]  There's decorations around them, but they're just words.
[645.98 --> 649.82]  And we spent the majority of the time focused on this.
[650.32 --> 651.40]  And trying to figure it out.
[652.38 --> 656.84]  We also had some – so that was my personal experience.
[657.20 --> 659.96]  I've done a number of surveys of the Go community.
[660.78 --> 666.06]  And two interesting things came out of those as it relates to this.
[666.06 --> 680.10]  We found that there was a reoccurring theme of people that had – when they had tried Go,
[680.10 --> 681.66]  they fell in love with it.
[682.16 --> 687.12]  But they didn't know how to communicate its value to their teammates or to their managers.
[688.70 --> 698.38]  And historically, the best way we've actually talked about Go is we've had kind of an unofficial slogan of try it and you'll like it.
[698.68 --> 699.62]  Or try it and you'll love it.
[700.24 --> 702.58]  And that's reinforced by our website.
[702.58 --> 706.38]  When you go to the Go laying website, what's the first thing you see?
[708.34 --> 708.82]  Anyone?
[709.88 --> 710.34]  Try it.
[710.80 --> 712.02]  You see try Go.
[712.26 --> 712.80]  Try Go.
[713.00 --> 713.48]  Try Go.
[713.62 --> 714.78]  It's right at the top.
[715.42 --> 719.64]  And then you see a happy Go for a download Go, which is also a way to try Go.
[720.80 --> 721.08]  Right?
[721.52 --> 723.72]  That's kind of the way we reinforce it.
[723.88 --> 724.72]  And that's good.
[724.72 --> 732.82]  And for the early adopter audience that we've served for a number of years, the idea that you could just try it is very valuable.
[733.48 --> 741.42]  As we go to more mainstream programmers, people that might not come with a CS background,
[741.42 --> 748.22]  the idea of trying a static compiled language is a bit intimidating.
[750.00 --> 753.28]  And a lot of them are looking just to find out more about it.
[753.40 --> 759.68]  And so when we heard this very consistent feedback that people, when they used Go, they loved it,
[759.72 --> 762.28]  but they didn't know how to explain its value.
[762.28 --> 773.56]  We also heard feedback from people that are tech leads or decision makers, directors of engineering, CTOs, et cetera,
[774.12 --> 776.96]  that they didn't know what Go's value was.
[777.16 --> 783.70]  You know, in our number of surveys and interviews, we found, you know, they'd heard concurrency and they've heard performance,
[784.06 --> 788.54]  but they weren't really sure what Go's value was.
[788.54 --> 799.42]  And it's a tough thing because with Go, it's not a single feature that really produces a value.
[799.98 --> 803.16]  Rather, it's the amalgamation of all the features, right?
[803.16 --> 809.60]  When you add them all up, it produces an experience that's really unlike any other in computer science.
[810.26 --> 814.78]  And it's that experience and how it scales over time that really produces the value.
[815.38 --> 816.80]  And that's a very hard thing to convey.
[816.80 --> 819.52]  And we tried to capture it the best we could with this brand.
[820.72 --> 822.00]  That is a good point.
[822.18 --> 823.98]  An experience is hard to communicate.
[825.26 --> 831.68]  People might have shared experiences, but also specific, distinct experiences.
[832.94 --> 841.00]  But I think having a guideline that helps them communicate different aspects of their experiences could be very helpful.
[841.00 --> 844.28]  So that was our intent.
[844.28 --> 858.72]  And, you know, to go into a little bit more, if you'd like, of our process going through this, because I think it's pretty insightful, is we worked with a branding agency.
[858.72 --> 863.88]  We recognized this was not a core strength of our engineering team, was branding.
[863.88 --> 873.48]  And the first thing that he did, or the person we worked with, his name is Adam, and his agency is within.
[874.18 --> 878.50]  The first thing that he did was he just did a series of interviews.
[878.50 --> 887.54]  And he interviewed all the early project members, as well as a bunch of members of the Go team.
[888.58 --> 891.70]  And to just get their feedback on what they thought Go was.
[891.70 --> 894.86]  And how they talked about Go.
[895.52 --> 901.02]  And then, and these were, you know, about 30 to 45 minute interviews.
[902.36 --> 910.08]  And then he took all of that together and came up, tried to distill it down to really its core essence.
[910.08 --> 916.96]  And then he worked with myself a lot.
[917.50 --> 921.64]  Chris Broadfoot worked a lot on this, as well as Russ Cox.
[922.40 --> 926.02]  And, and a bunch of other people.
[926.26 --> 928.06]  But I think those were the primary three.
[929.54 --> 934.48]  And, and we just kept trying to distill it down further and further and further.
[934.48 --> 946.98]  So it was a very, it was a very, it took a surprising, it's amazing how much time it takes to come up with a small number of words.
[947.96 --> 952.28]  I believe it's Mark Twain who famously said, I'm sorry I wrote you a long letter.
[952.36 --> 954.06]  I didn't have time to write you a short one.
[954.20 --> 955.08]  I'm paraphrasing.
[955.20 --> 956.24]  That's not the exact quote.
[956.24 --> 964.36]  But it really took a long time to distill it right down to the essence of what we believe Go is.
[965.48 --> 971.42]  And I particularly love the section, the tone of voice section of the book, of the brand book.
[972.12 --> 975.68]  Because it tries to really narrow it down, right?
[975.78 --> 982.50]  Because it's one thing for you to say one word that tries to encapsulate what the language or what the community is all about.
[982.50 --> 989.72]  So here we have a few words about what gophers are and corresponding words about what gophers are not.
[989.96 --> 991.56]  For example, what gophers are.
[991.56 --> 995.24]  I'm just, I want to go through the lists for people who are looking at this.
[995.90 --> 996.82]  Gophers are concise.
[997.12 --> 998.44]  Gophers are not verbose.
[998.74 --> 1000.32]  We're genuine, not dubious.
[1000.52 --> 1001.74]  Friendly, not exclusive.
[1002.08 --> 1003.36]  Direct, not ambiguous.
[1004.26 --> 1005.52]  Thoughtful, not reactive.
[1005.88 --> 1007.78]  Humble, not haughty.
[1007.90 --> 1008.28]  Haughty?
[1008.36 --> 1009.22]  Is that how you say that word?
[1009.88 --> 1010.32]  That's right.
[1010.32 --> 1018.46]  So I really like that the effort was made to describe what gophers are not.
[1020.02 --> 1021.16]  It's really helpful.
[1021.80 --> 1030.80]  And it's really helpful to, when you are thinking of how to behave in a community, right?
[1030.80 --> 1031.68]  What is acceptable?
[1032.24 --> 1033.80]  Or how to write code?
[1033.92 --> 1035.42]  What is good idioms?
[1035.42 --> 1038.58]  You start thinking about these things and it helps.
[1039.94 --> 1042.16]  And we thought especially, thank you.
[1042.42 --> 1057.42]  I think especially with the growth that we're going through, we can't expect our culture to spread through all this growth unless we codify it.
[1057.42 --> 1069.38]  And we try and lead with the – and so that's a bunch of this around like, well, we need a single place as a reference to the entire global community.
[1070.06 --> 1086.62]  Whether you're from Australia or you're from Singapore, you're from China or you're from Brazil or you're from Seattle or anywhere where you could have a single document that really reinforced what it meant to be part of Go.
[1087.42 --> 1090.58]  And that was our goal of what we tried to do here.
[1091.22 --> 1095.84]  I think branding is probably the – an extremely tough exercise.
[1095.84 --> 1117.92]  And the fact that you all started with words and interviews is a testament to the faithfulness to describe exactly what Go is but then also what the – a programmer using Go may or may not be like because a lot of branding is not really at all the visual part of it.
[1117.92 --> 1125.74]  While, you know, maybe some of the backlash or some of the surprise from the community is based on the visual pieces of it.
[1126.26 --> 1134.36]  It's the understanding who you are and why you do what you do to explain who you are is really the core components of a brand.
[1134.84 --> 1141.16]  You know, like you can't show off who you are or visualize who you are unless you know who you are.
[1142.66 --> 1143.46]  Well said.
[1143.46 --> 1147.02]  I guess maybe what's – what are your hopes here?
[1147.10 --> 1153.02]  I mean I know that this may have been not a surprise to you obviously because you're involved behind the scenes.
[1153.12 --> 1160.10]  But I think for many it was like, OK, Go is like nine years old, eight and some years old.
[1160.32 --> 1164.98]  And here comes this, you know, either brand or rebrand.
[1164.98 --> 1171.54]  And I'm not really sure if this is an actual – a rebrand because I'm not sure there ever was a true brand in place to this degree.
[1172.78 --> 1176.52]  You know, what are your hopes for the community to respond?
[1177.00 --> 1181.66]  Like when you released this, Steve, you wrote the article, the post on the Go blog.
[1181.78 --> 1183.42]  What was your anticipation?
[1183.72 --> 1184.48]  Were you surprised?
[1184.76 --> 1185.94]  What were you most surprised about?
[1186.02 --> 1188.36]  What were your hopes for releasing this to the world?
[1188.36 --> 1194.08]  So I think – I'll answer the first question.
[1194.20 --> 1195.50]  Is it a brand or a rebrand?
[1195.96 --> 1200.78]  And it's – I'll say there's not a lot new here.
[1203.10 --> 1214.84]  In a sense, our real goal here was – as I said, I kind of started from that first experience I had maybe two weeks into joining the Go team of having to write a blurb of who we are.
[1214.84 --> 1219.14]  And, you know, I talked to Robert Griesmeyer and he gave me some feedback.
[1219.32 --> 1222.26]  And I talked to Andrew and he gave me completely different feedback.
[1222.50 --> 1224.36]  And I talked to Ian and it was different again.
[1225.04 --> 1239.54]  We really wanted to come up with what would be our story, our concise story that represents not only the Go team at Google but the entire Go community, that we can have one way of talking about it.
[1239.54 --> 1243.56]  And that really was the primary goal.
[1245.54 --> 1256.58]  And, you know, the other part was when everything is done kind of ad hoc, you don't have a lot of opportunities to make decisions.
[1257.98 --> 1262.14]  And I would describe the historic Go brand as mostly ad hoc.
[1262.26 --> 1266.38]  When we were asked a question that we needed a blurb for this, we wrote a blurb for that.
[1266.38 --> 1270.32]  And when we needed a website that looked like this, we did that.
[1270.88 --> 1287.54]  And, you know, Rene has been fantastic in providing lots of wonderful gopher designs as well as a logo, which a lot of people – I learned after that blog post launched, a lot of people didn't know it was – we had a logo before.
[1287.54 --> 1296.02]  But a lot of – everything was kind of disconnected in how it was designed.
[1296.70 --> 1302.00]  And we often design something for an immediate need without looking at the holistic picture.
[1302.00 --> 1308.84]  And with this, we really took the opportunity to say, look at all these pieces we've done over the last 10 years.
[1310.40 --> 1321.58]  And how can we put them together and make some real decisions about which are the ones that we want to be our voice or our mission or our look?
[1321.58 --> 1325.06]  Now, there's some new looks here.
[1326.16 --> 1332.02]  Definitely the logo went through an evolution from Rene's hand-drawn into a vectored image.
[1334.58 --> 1338.78]  But – and Rene's used a lot of different colors over the years.
[1338.88 --> 1344.14]  And we definitely used that as inspiration as we came up with our color palette here.
[1344.14 --> 1355.92]  But, yeah, there's – a lot of these ideas have been floating around, but most of it was to provide just a single point where people could use it as an anchor.
[1356.12 --> 1360.64]  And hopefully answer that question when people ask, how do I communicate Go's value?
[1361.26 --> 1365.62]  They can look at this and say, you know, well, this is what Go is.
[1366.12 --> 1367.76]  You know, we've written a real clear description.
[1368.02 --> 1370.48]  Go is – and I'll read it for those who don't have it.
[1370.48 --> 1378.24]  Go is an open-source programming language that enables the production of simple, efficient, and reliable software at scale.
[1379.70 --> 1381.06]  That's really what Go is.
[1381.20 --> 1388.46]  We think that's the best articulation we've ever heard or we were able to come up with of really what Go is.
[1389.28 --> 1398.84]  And as you continue through it, our goal is – our hope is that people use this as a reference and that it can help unite the community.
[1398.84 --> 1404.52]  Yeah, I got really caught up on the logo and the visual aspects of the branding.
[1405.08 --> 1407.18]  And I totally missed the point.
[1407.40 --> 1408.98]  I mean, the point is completely different.
[1409.44 --> 1417.84]  And I'm really glad you're here to tell us since people – to me, people like me who might have missed the point too.
[1418.74 --> 1421.34]  And, in fact, I don't remember that we had a logo.
[1421.46 --> 1423.26]  And that was a question that I was going to ask.
[1423.54 --> 1425.58]  So you just said it, that we did have a logo.
[1425.66 --> 1426.98]  I don't remember what it was.
[1426.98 --> 1438.58]  So that's – you are not alone in that, as we learned very clearly from some of the feedback we got.
[1439.30 --> 1444.52]  People misunderstood that Go had a logo and the logo was the gopher.
[1445.16 --> 1445.56]  Yes.
[1445.56 --> 1453.20]  And so when we said we have a new logo, I think this is really – it was obviously a misunderstanding.
[1454.32 --> 1456.82]  But it came out of people's love for the gopher.
[1456.82 --> 1468.32]  The people have fallen in love with this very human side of a very technical project that we all love.
[1468.32 --> 1471.78]  I think there's no one on – no one that doesn't love the gopher.
[1472.42 --> 1478.94]  And the reaction that we got was, I think, mostly stemming from that, that people love the gopher.
[1479.60 --> 1486.56]  And the thought of it not being around, I don't know, kind of gave people a shock.
[1486.56 --> 1500.04]  That said, if you – on our blog, you can actually see the original logo, not in the most recent post, but in a post a number of years ago that we wrote on the gopher.
[1500.04 --> 1508.08]  And I'm actually looking it up right now as we're talking.
[1512.66 --> 1514.30]  So I can get the – okay.
[1514.44 --> 1518.22]  So it's blog.golang.org slash gopher.
[1519.58 --> 1527.62]  And this goes through the history of the gopher and as well as Renee's history with Plan 9 and other things.
[1527.62 --> 1530.68]  And it also talks about our initial logo.
[1531.98 --> 1533.72]  And it has a picture of it there.
[1534.70 --> 1536.08]  There with the black background?
[1536.86 --> 1537.54]  That's right.
[1537.62 --> 1538.64]  The one with the black background.
[1538.66 --> 1539.26]  Oh, okay.
[1540.50 --> 1551.80]  And if you watch some of the old videos, you'll actually see Brad and Rob and others wearing T-shirts with this logo on it.
[1552.34 --> 1553.06]  That is true.
[1553.16 --> 1553.90]  I remember that.
[1554.52 --> 1555.66]  I remember those T-shirts.
[1555.66 --> 1563.90]  So this logo is the – was the official go logo, although it wasn't used very heavily.
[1566.12 --> 1569.34]  We used it in some of those T-shirts and it appears here.
[1569.70 --> 1571.28]  But it's not on the blog.
[1571.44 --> 1572.98]  It's not in a number of other places.
[1573.70 --> 1578.66]  We've ended up using the gopher far more when we created swag.
[1580.44 --> 1582.80]  So that's the old logo.
[1582.80 --> 1585.80]  The new logo actually started from a very similar place.
[1586.36 --> 1588.40]  And you can see it ended in a very similar place.
[1588.62 --> 1589.62]  It's very similar.
[1590.54 --> 1592.96]  And this logo, Renee drew.
[1592.96 --> 1599.92]  I might not be accurate on this, but a number of years ago.
[1599.98 --> 1601.70]  I wanted to say 2008 or 2009.
[1602.80 --> 1604.14]  A very long time ago.
[1604.14 --> 1619.38]  This episode is brought to you by Rollbar.
[1619.62 --> 1621.46]  Move fast and fix things.
[1621.82 --> 1624.02]  Resolve errors and minutes and deploy with confidence.
[1624.42 --> 1626.68]  Head to rollbar.com slash changelog.
[1626.76 --> 1627.56]  Request a demo.
[1627.70 --> 1628.58]  Get started today.
[1628.58 --> 1634.24]  It's loved by developers, trusted by enterprises, and most of all, we use it here at Changelog.
[1634.60 --> 1637.26]  Move fast and fix things with Rollbar.
[1637.54 --> 1640.54]  Once again, rollbar.com slash changelog.
[1640.54 --> 1658.72]  What's interesting, too, is this blog post.
[1658.72 --> 1664.14]  I was actually going to ask this question in hopes of stirring up the origin story of the gopher.
[1664.98 --> 1668.28]  And I was not aware of this blog post, but this shares that.
[1668.56 --> 1677.34]  It has a history of Renee making it for a radio station called WFMU for a fundraiser they had.
[1677.34 --> 1684.46]  And had a second appearance as it Bell Labs with Bob, I'm not sure how you say his name, his avatar.
[1685.20 --> 1687.80]  And then again for playing nine as a mascot.
[1688.04 --> 1694.78]  And then I guess when the open source happened for Go, Renee suggested it to adopt the mascot.
[1694.94 --> 1695.98]  And the gopher was born then.
[1696.12 --> 1697.30]  So right around 2009.
[1697.30 --> 1703.80]  That's an interesting process to, you know, and you said in a way ad hoc.
[1703.92 --> 1715.78]  So this gopher is kind of like has made its way through several different forms and several different reasons for even being to now be, you know, the beloved mascot of gophers.
[1717.38 --> 1717.94]  Yeah.
[1718.20 --> 1718.46]  Yeah.
[1718.46 --> 1723.14]  It's amazing what an impact it's had on the project.
[1724.42 --> 1731.30]  And we owe Renee a huge amount of gratitude for her contribution to it.
[1731.42 --> 1741.32]  I think she really provided for us, you know, kind of our identity.
[1742.10 --> 1748.22]  You know, we don't call ourselves, you know, in Python they call themselves Pythonistas.
[1749.42 --> 1751.70]  And everyone has different monikers.
[1752.12 --> 1754.38]  We don't call ourselves the goers or anything like that.
[1754.44 --> 1755.08]  We're gophers.
[1755.22 --> 1757.38]  And that comes from Renee's mascot.
[1759.16 --> 1764.96]  And, you know, even GopherCon and everything that's come since all really stems from Renee's mascot.
[1764.96 --> 1769.20]  So I think she did an amazing job providing an identity for us.
[1769.20 --> 1781.04]  And our goal with the visual branding here was to really take Renee's work and to build on it and to try and consolidate it down.
[1782.10 --> 1789.04]  You know, and Renee did a lot of work with gophers and colors and the logo.
[1789.04 --> 1792.56]  She didn't do a lot of work with the website and other things.
[1793.06 --> 1797.58]  And so our objective here was to really create a holistic presence for go.
[1797.86 --> 1802.68]  And, you know, you see the brand book and it has some of the things.
[1802.68 --> 1813.02]  As I mentioned in our blog posts, we're also working on revamping our website to follow this new brand.
[1813.56 --> 1817.00]  And we're pretty close to having the blog ready to launch.
[1817.72 --> 1819.26]  It should be a few more weeks.
[1821.06 --> 1823.38]  But – and that's where we're starting.
[1823.64 --> 1824.78]  We're starting with the blog.
[1824.78 --> 1828.86]  We'd like to get the community involved as early as possible.
[1829.56 --> 1836.56]  And we hope to be able to take the work that we did on the blog and apply it to the website and keep going.
[1836.78 --> 1844.92]  And as a part of this, we're also extending our blog to support multiple languages, which is something we've never had before.
[1844.92 --> 1854.80]  And on Follow-On, we're using the same technology back end for the website, which will also enable us to have multiple languages.
[1855.82 --> 1856.72]  And I say the website.
[1856.92 --> 1858.72]  There's lots of components to our website.
[1859.48 --> 1866.34]  And we're going to focus more on the static content first rather than things like play, where it's more interactive.
[1866.34 --> 1875.18]  But we're going to stage it out and hopefully have a consistent brand and feel across all of the different Go websites.
[1877.12 --> 1885.38]  Was Renee involved at all in this process with Adam and team to interview and kind of self-examine the process?
[1886.46 --> 1887.18]  Renee was.
[1887.36 --> 1889.98]  She was very involved.
[1889.98 --> 1894.90]  In fact, a lot of people were involved at the beginning for the interview.
[1895.56 --> 1902.74]  And then we spent a lot of time after their interviews just working through everything and trying to consolidate things down.
[1903.18 --> 1904.56]  And that was a much smaller group.
[1905.54 --> 1909.32]  And then we'd go back to the larger group just for feedback every once in a while.
[1909.98 --> 1915.30]  Renee spent less time on the verbal part of the brand.
[1915.30 --> 1920.86]  But she spent a considerable part on the visual part of the brand.
[1921.60 --> 1923.30]  And she did so over time.
[1923.86 --> 1926.10]  So she was very involved with it.
[1926.54 --> 1928.60]  She helped pick the color palette.
[1928.76 --> 1933.10]  She helped name the colors, particularly the gopher blue one.
[1934.14 --> 1938.28]  She worked with us on every part of the visual aspect.
[1939.48 --> 1940.78]  That sounds fantastic.
[1941.06 --> 1941.84]  I mean, I don't know.
[1942.26 --> 1944.90]  Whoever was involved, you guys did a really good job.
[1944.90 --> 1946.50]  I personally really like it.
[1946.58 --> 1948.94]  So I'm just going to put my bias out front.
[1950.28 --> 1951.70]  I love it.
[1951.80 --> 1953.78]  I think it came out really, really well.
[1954.00 --> 1955.36]  It was a good job.
[1956.60 --> 1957.26]  Thank you.
[1957.78 --> 1961.36]  Not that this is that important to dive into.
[1962.02 --> 1968.40]  But I think it's kind of interesting, the stark exact opposite response.
[1969.08 --> 1971.44]  And I know Hacker News isn't the best place to have comments.
[1971.44 --> 1974.24]  It's not the best place to meet the most loving programmers.
[1975.02 --> 1979.08]  However, you know, there's such a backlash from so many people.
[1979.08 --> 1983.58]  I wonder why people feel so like they should respond that way.
[1983.90 --> 1984.98]  I didn't see that.
[1985.32 --> 1986.32]  I mean, I didn't look either.
[1986.58 --> 1987.80]  None of it seems very positive.
[1988.24 --> 1991.80]  Steve, I'm sure you had to dig into some of this or at least be like, come on.
[1991.84 --> 1992.40]  Really, guys?
[1992.40 --> 1996.26]  You got to, you know, someone says they're incredibly sad.
[1996.34 --> 1997.28]  The logo is awful.
[1998.06 --> 2000.84]  You know, looks like somebody else's logo.
[2001.26 --> 2002.62]  There's a lot of just, you know.
[2004.36 --> 2012.10]  You know, the immediate gut response, it seems, from some people, potentially even a larger community here on Hacker News.
[2012.10 --> 2014.20]  But again, we understand what Hacker News is.
[2014.28 --> 2017.38]  Comments can tend to be like not very positive.
[2018.18 --> 2027.00]  They seem to be very right on point with Hacker News' way is being somewhat negative about, you know, this process and just bashing rather than uplifting.
[2027.26 --> 2028.22]  It drives me crazy.
[2028.22 --> 2038.64]  So what I saw – so first I want to say I think a lot of this just comes from the fact of how passionate people are.
[2038.94 --> 2039.14]  Yeah.
[2039.62 --> 2043.20]  I think people love the Gopher.
[2044.84 --> 2048.46]  I think, you know, there's a lot of people that really love Go.
[2048.98 --> 2053.66]  And the thought of something changing has always been hard for people.
[2053.66 --> 2059.02]  And the brand is really the essence of something.
[2059.56 --> 2062.60]  There's a visual element as well as all the text.
[2062.70 --> 2064.72]  It really defines what the essence of something is.
[2065.22 --> 2070.90]  And people were worried that their beloved language and mascot, et cetera, were changing.
[2071.64 --> 2081.98]  And I think what we saw was a reaction to, you know, if people didn't love Go, if they weren't so passionate around it, we wouldn't have seen that.
[2081.98 --> 2082.10]  Yeah.
[2082.88 --> 2086.34]  So I think it's a testament to how passionate people are around it.
[2086.86 --> 2100.28]  I think it's also what we noticed was there was – in spite of what I – I think the language on the blog post, I looked at it after this feedback and spent quite a bit of time on it.
[2100.28 --> 2111.62]  But it's right in the very beginning that says, built upon the great foundation that Rene French established and rest easy, our beloved Gopher mascot remains the center of our brand.
[2111.84 --> 2112.08]  Yeah.
[2112.08 --> 2115.48]  As you scroll down, the Gopher is very present.
[2116.68 --> 2125.12]  It's featured in the video that shows our Go logo design process and all the different – not all, but many of the iterations we went through with the logo.
[2125.86 --> 2134.18]  It's also very prominent in the slide presentation as well as it's prominent in the brand book, all of which are featured.
[2134.18 --> 2145.48]  So I think we communicated the Gopher was very part of our brand well because the Gopher was a consistent part but not the new part.
[2145.94 --> 2150.00]  We didn't heavily feature the Gopher here but made sure that it was included.
[2150.56 --> 2153.88]  But we focused more on things that were new and different.
[2153.88 --> 2162.00]  In spite of that, I think what we saw was some people reacting to some people's reactions.
[2162.88 --> 2171.80]  And so some people misunderstood that the new logo was replacing our mascot, the Gopher.
[2172.30 --> 2177.22]  And they started tweeting about that or posting comments about it.
[2177.22 --> 2185.72]  And then people reacted to that post rather than finding out for themselves that that's not accurate.
[2186.56 --> 2196.60]  And so it kind of escalates when people have a misunderstanding and then people look at that without going to the source.
[2196.82 --> 2198.24]  It always escalates things.
[2198.24 --> 2210.26]  And that's just a bit of a statement of where we live today and the kind of world of – I remember life before the internet and how hard it was to find information.
[2210.42 --> 2212.64]  You had to drive places or walk to libraries.
[2213.34 --> 2214.54]  You had to use these –
[2214.54 --> 2215.90]  Pay phones.
[2216.04 --> 2216.26]  Right.
[2216.44 --> 2218.50]  I remember we had these card catalogs.
[2218.58 --> 2225.74]  You had to look up these giant dressers with all these papers in them that told you where to find things.
[2225.84 --> 2227.30]  It was very hard to find information.
[2227.30 --> 2228.44]  Now it's very easy.
[2228.92 --> 2232.20]  It seems people are resistant to doing so.
[2233.08 --> 2236.28]  That's funny too because it seemed like the Gopher wasn't really going anywhere.
[2236.48 --> 2249.80]  It also didn't seem like unless you read some words visually, it didn't seem like the Gopher, unless you looked hard, at least just real quickly at this blog post, the Gopher was kind of missing quickly from a quick visual glance.
[2250.08 --> 2250.36]  I agree.
[2250.50 --> 2255.94]  You have to either press play or just scroll down a little bit or click on any of the things.
[2255.94 --> 2256.94]  Yeah.
[2256.94 --> 2257.78]  Yeah, I agree.
[2258.12 --> 2261.12]  It's – especially when other people are saying it.
[2261.26 --> 2261.54]  Yeah.
[2261.54 --> 2267.44]  And so I think what we saw was people reacting to reactions and –
[2267.44 --> 2268.06]  Misinformation.
[2269.36 --> 2278.76]  But it's sort of easy to see how people could have been misled because like Adam was saying, the Gopher is not on the post itself.
[2278.96 --> 2281.20]  Of course, if you go into the document, the Gopher is there.
[2282.30 --> 2283.54]  And maybe people didn't go that far.
[2283.54 --> 2287.42]  If you play the video, which I know not everybody wants to play videos.
[2288.04 --> 2292.18]  Or if you scroll to the bottom, right, the last image has multiple Gophers on it.
[2292.32 --> 2299.36]  But again, we didn't anticipate that people would have – I mean shame on me.
[2299.80 --> 2301.28]  I should have anticipated more.
[2301.28 --> 2301.64]  No, no, no.
[2301.66 --> 2302.78]  That's not worth saying at all either.
[2302.98 --> 2304.26]  Because one of the points –
[2304.26 --> 2304.88]  I'm going to say that.
[2305.10 --> 2305.80]  I'm going to say that.
[2305.80 --> 2306.66]  I didn't say that.
[2306.66 --> 2307.66]  Same one you, Steve.
[2307.66 --> 2312.70]  And I'm going to say if I could have done it again, I would have put the Gopher more prevalent at the top.
[2313.04 --> 2313.22]  Yeah.
[2313.88 --> 2317.94]  And I didn't anticipate that people would have made the misunderstanding.
[2318.70 --> 2319.44]  Can you not edit the post?
[2319.44 --> 2320.18]  And that's on me.
[2320.84 --> 2322.16]  Can you not edit the post?
[2322.76 --> 2323.28]  I could.
[2323.28 --> 2326.10]  But we thought about it.
[2326.24 --> 2329.10]  And the reality is the post is pretty clear.
[2330.30 --> 2331.48]  The words are clear.
[2331.62 --> 2333.00]  The mascot is staying there.
[2333.18 --> 2336.12]  We're not intimidating anything about the mascot going.
[2336.12 --> 2337.36]  If you click through the things.
[2337.94 --> 2348.86]  And by the time – again, as most people are reacting to reactions, by the time the post went live, that was the time that people needed to hear that the Gopher was there in the beginning.
[2349.06 --> 2351.90]  So the window was really before it was posted.
[2353.24 --> 2354.78]  And we missed the window.
[2355.36 --> 2362.98]  But I think if you give it time – first, here's the thing about change.
[2362.98 --> 2366.58]  People are always nervous at the beginning about change.
[2367.36 --> 2368.90]  And give them time.
[2369.66 --> 2372.06]  And I don't expect everyone's going to love it.
[2372.12 --> 2373.30]  It's a subjective thing.
[2373.42 --> 2375.66]  Not everybody loves every painting.
[2375.86 --> 2377.38]  Not everybody loves every color.
[2378.02 --> 2380.66]  Not every – you know, nothing appeals universally.
[2380.66 --> 2383.92]  But I think with a lot of people, give it time.
[2384.02 --> 2386.36]  It's going to set a lot of their fears.
[2386.76 --> 2388.08]  It's going to calm a lot of their fears.
[2388.72 --> 2389.16]  And –
[2389.16 --> 2397.48]  One really strong reaction that I saw people having was that the playfulness of Go was there.
[2397.62 --> 2400.30]  And now it's not because this logo is not as playful.
[2400.58 --> 2403.94]  Then, of course, it goes back to people equating the logo with the Gopher.
[2404.12 --> 2405.28]  And the Gopher is not going away.
[2405.28 --> 2406.32]  We've covered that.
[2406.92 --> 2416.68]  But that brings up a point, too, which is when you codify something, it means now that is the right way of doing things.
[2416.72 --> 2419.02]  And if there's a right way, there's a wrong way, right?
[2419.44 --> 2423.30]  So how do we handle this?
[2423.44 --> 2427.62]  How are we – because Google, okay, you sponsor things.
[2427.68 --> 2428.56]  You need to have your blurb.
[2428.56 --> 2429.56]  You need to have your logo.
[2429.98 --> 2431.00]  But how about us?
[2431.02 --> 2432.32]  How can we use this?
[2433.10 --> 2435.50]  How will we be using this in the wrong way?
[2435.72 --> 2437.36]  Or what if we don't use any of this?
[2437.40 --> 2438.30]  Would it be wrong?
[2438.56 --> 2444.76]  Are we going to get a call from Google's lawyers and say, hey, you know, using the proper material?
[2445.50 --> 2447.48]  How does it apply to everybody else?
[2448.64 --> 2451.10]  So I'm going to answer this in two ways.
[2451.36 --> 2454.48]  One, there's a few things here that are copyrighted.
[2455.44 --> 2457.20]  The logo being one of them.
[2458.38 --> 2461.26]  And the logo does have guidelines for its usage.
[2461.26 --> 2469.62]  So I want to be clear that the logo needs to be used appropriately according to those guidelines.
[2471.24 --> 2473.56]  So I want to be clear with that up front.
[2474.58 --> 2478.72]  Beyond that, you are welcome to use this or not use this.
[2480.54 --> 2483.10]  This is meant as a guide for the community.
[2483.10 --> 2491.16]  It is not a – no one came down from the mountain with stone tablets.
[2492.38 --> 2494.54]  We think it's going to be a valuable asset.
[2495.26 --> 2499.06]  We hope it's something that the community embraces and uses.
[2499.06 --> 2506.96]  We fully expect everyone to continue to do their own thing as they have.
[2507.56 --> 2509.50]  You know, we just finished up Gotham Go.
[2509.50 --> 2512.62]  And it continued to have its own brand.
[2513.44 --> 2519.88]  And I know GopherCon this year is using a theme of race cars.
[2519.88 --> 2523.90]  And we fully expect them to continue their brand.
[2524.68 --> 2525.64]  And I think that's –
[2525.64 --> 2528.86]  I was going to ask, what was going to be the theme for this year?
[2529.72 --> 2530.16]  Thank you.
[2530.20 --> 2531.42]  It's all over the website already.
[2531.54 --> 2532.56]  Have you not been on the website?
[2533.26 --> 2533.76]  I have.
[2533.90 --> 2534.30]  I didn't know.
[2534.38 --> 2534.66]  Sorry.
[2536.02 --> 2537.74]  GopherCon.com, y'all.
[2538.30 --> 2538.98]  Sorry, Steve.
[2539.04 --> 2540.30]  That was such a detour.
[2540.30 --> 2541.98]  Anyway, yeah.
[2542.06 --> 2545.96]  So I think people are welcome to use their own brands.
[2547.32 --> 2551.26]  You know, we think this is something that can help inspire the community.
[2551.82 --> 2556.18]  We hope the community is – follows the values.
[2557.34 --> 2560.12]  And we want – we would like that to happen.
[2560.60 --> 2560.74]  Right?
[2560.74 --> 2562.22]  We want people that are thoughtful.
[2562.40 --> 2563.82]  We want people that are friendly.
[2563.82 --> 2572.82]  But, you know, people – each group is welcome to adopt what they want to from this.
[2573.74 --> 2581.26]  There is no consequence for not – as long as people follow the code of conduct.
[2581.44 --> 2581.60]  Right?
[2581.68 --> 2584.22]  I want to make sure that's independent of this.
[2584.68 --> 2586.32]  And that does have consequences.
[2587.10 --> 2590.96]  So what does it mean when you say that the Go logo is copyrighted?
[2591.02 --> 2592.28]  That sounds pretty serious.
[2593.82 --> 2594.98]  What does it mean?
[2595.02 --> 2597.26]  Do we have to credit Google when we use it?
[2597.42 --> 2599.92]  Does it mean we cannot change – adulterate it?
[2600.08 --> 2601.44]  Or, like, what is it?
[2602.18 --> 2606.78]  So our logo is more flexible that's used than most logos.
[2607.60 --> 2611.76]  But there's guidelines within the brand book on what acceptable use is.
[2612.96 --> 2619.90]  And we talked a lot about what to license it under and spend some time with our open source legal team.
[2619.90 --> 2623.02]  And their advice was copyright.
[2623.66 --> 2626.64]  The logo is the appropriate thing to do.
[2626.86 --> 2634.62]  And it lets people use it under fair use rights and under the guidelines that you've set forth.
[2634.82 --> 2636.72]  But they can't make modifications.
[2636.98 --> 2637.74]  They can't sell it.
[2637.80 --> 2640.74]  They can't do different things to it because it's copyrighted.
[2641.16 --> 2644.10]  But can I flop it anywhere without crediting anybody?
[2644.44 --> 2646.04]  Or do I have to worry about giving credits?
[2646.04 --> 2648.30]  Yeah, there's no credit needed.
[2649.48 --> 2657.72]  A lot of the copyright is just to say that it's their mark and that no one else can use the mark in a trademarked or copyrighted scenario.
[2658.38 --> 2664.92]  And as a copyright holder, you have to protect your copyright because otherwise you don't have a copyright.
[2664.92 --> 2665.06]  That's right.
[2666.06 --> 2666.88]  That's right.
[2666.98 --> 2674.94]  And I'll just say I encourage people to ignore what I've said but read the document.
[2676.62 --> 2684.00]  There's two pages on what is acceptable use with lots of diagrams and pictures of what to do and what not to do.
[2684.86 --> 2689.18]  So we hope the Go community uses this.
[2689.18 --> 2694.12]  We hope it becomes – I don't think it's going to replace the Gopher in any sense.
[2694.76 --> 2696.82]  But I do think it's a nice accent.
[2697.22 --> 2700.20]  It definitely reinforces our brand.
[2700.80 --> 2705.50]  A lot of people have – the Gopher is wonderful and it's fun.
[2705.62 --> 2706.14]  It's playful.
[2707.00 --> 2710.00]  It's not immediately recognizable as the word go is.
[2711.16 --> 2717.06]  If you're not familiar with the Gopher and go but you see the word go, you're going to associate that.
[2717.06 --> 2724.62]  I think of it like maybe on product websites like when you go to a service and they support certain languages.
[2725.16 --> 2727.92]  What do they put in place of Go now?
[2728.02 --> 2730.32]  They probably use the Gopher.
[2731.54 --> 2737.32]  They might or a lot just come up with their own logo or their own thing.
[2737.50 --> 2737.72]  Right.
[2738.24 --> 2740.56]  And what ends up happening is there's never a match.
[2741.64 --> 2742.04]  Exactly.
[2742.26 --> 2743.36]  There's no consistency.
[2743.94 --> 2744.16]  Yeah.
[2744.16 --> 2744.68]  Yeah.
[2745.12 --> 2750.94]  And so that's what we're trying to provide here is that consistency so that when you see this mark, you know it's the language.
[2751.88 --> 2753.40]  And yeah, please read the document.
[2753.54 --> 2755.54]  It talks about all the different ways to use it.
[2756.74 --> 2760.92]  And I will say I was at Gotham Go.
[2761.10 --> 2765.10]  I was the emcee for the – I don't know, third or fourth year in a row.
[2765.10 --> 2773.22]  And I was thrilled that a number of the speakers used the logo on their decks.
[2775.38 --> 2778.28]  And, you know, it was nice.
[2778.32 --> 2779.80]  It was nice to see that consistency.
[2781.02 --> 2782.88]  Not everybody used it and that was fine.
[2783.48 --> 2789.88]  I didn't expect anybody to except Cassandra who used the actual deck that we distribute.
[2789.88 --> 2792.82]  But she was also part of the process of creating it.
[2793.26 --> 2810.46]  And so just to clarify for people, on the blog post that is on the Golang website, there is a link to download a slide, master slides that you can use that's already branded with the colors and the logo.
[2810.46 --> 2810.94]  That's right.
[2810.94 --> 2812.12]  So that's right.
[2812.26 --> 2812.68]  That's right.
[2812.78 --> 2816.32]  And there's also a link there to the brand book that we've been talking about.
[2816.52 --> 2819.84]  Those links are right next to each other under the download section.
[2820.70 --> 2828.72]  And talking about the website there, going back a little bit, is the website going to be decoupled from the language repo?
[2832.48 --> 2833.04]  Yes.
[2833.04 --> 2833.28]  Yes.
[2834.48 --> 2841.38]  The plan is to decouple the website from the language repo.
[2841.76 --> 2847.22]  And partly because there was value in coupling it.
[2847.34 --> 2854.18]  But as we need to scale into different languages and different things, we can't see another way but to decouple them.
[2855.54 --> 2859.92]  That said, there will remain documentation as part of the distribution.
[2859.92 --> 2864.42]  But the website itself will be decoupled.
[2864.52 --> 2865.96]  At least that's the current strategy.
[2866.92 --> 2873.10]  Yeah, I hope so because the website would only be updated once there was a release.
[2874.60 --> 2877.12]  Yeah, right now it's every six months.
[2877.74 --> 2878.08]  Yeah.
[2879.08 --> 2879.68]  Yeah.
[2879.68 --> 2889.82]  Our goal is to – part of the new design is also to provide a little more contextual information towards what's happening now.
[2891.20 --> 2894.92]  And try and keep our community members, our users more informed.
[2895.54 --> 2899.74]  And every six months is just not frequent enough.
[2899.74 --> 2900.74]  Yeah.
[2900.74 --> 2901.30]  Yeah.
[2901.44 --> 2905.02]  If you have a typo you want to fix, get away in six months.
[2906.28 --> 2911.76]  Or some new information, like a new link you want to add, get away in six months.
[2912.24 --> 2915.14]  Yeah, I'm pretty sure we can fix typos within six months.
[2915.14 --> 2925.32]  But our goal is to – it would be great on our homepage if we had things like upcoming conferences and keep our global community more informed.
[2925.98 --> 2929.94]  And that's not possible every six months.
[2930.24 --> 2932.34]  We don't have dates and links.
[2932.86 --> 2937.64]  The conferences are just too dynamic for that.
[2938.48 --> 2940.40]  What are you doing to move faster on those fronts?
[2940.84 --> 2943.36]  I know she just mentioned, is it being decoupled?
[2943.36 --> 2955.08]  A lot of – one of the things that helps a language succeed other than obviously being a good language is its supportive community, which Go does very well.
[2955.48 --> 2962.46]  But it does seem like there's some slowness around these kinds of things that could be sped up.
[2962.56 --> 2969.86]  Not so much that it's bad, just like how are you kind of optimizing for those things to make those things a bit more faster?
[2971.40 --> 2973.26]  It's a good question.
[2973.36 --> 2978.34]  I mean obviously Cassandra came on the team recently, so you got community things happening.
[2978.44 --> 2979.32]  So there's some change happening.
[2979.38 --> 2980.56]  I'm just curious how that's playing out.
[2981.48 --> 2984.42]  Yeah, I would actually defer to Cassandra on that.
[2985.02 --> 2990.90]  She's doing an amazing job of really devising strategies and trying to help this community scale.
[2990.90 --> 3005.02]  I'll say one of the smartest things we've done is actually step out of the way as Google and let the community do what it does.
[3005.22 --> 3006.72]  That's been very productive.
[3007.56 --> 3009.16]  It's been very beneficial.
[3009.16 --> 3012.06]  We've also realized there's a balance there.
[3012.98 --> 3020.26]  And there's – especially as we grow, there's a lot of value in adding support.
[3020.26 --> 3028.50]  And so one of the things we've recently done is – which I don't know that we've talked about publicly because it's not public.
[3028.50 --> 3039.68]  But we've set up a communication channel for the different conference organizers so that they're able to talk to each other and start comparing things and try and get more consistency.
[3041.02 --> 3043.26]  Google doesn't have any stake in that.
[3043.80 --> 3047.62]  We don't have any – it's not like they have to follow the guidelines or anything.
[3047.62 --> 3048.32]  We're setting forth.
[3048.38 --> 3049.10]  We're not doing any of that.
[3049.16 --> 3051.66]  We're just providing a communication channel.
[3052.26 --> 3065.18]  But trying to do things like that more often I think is a way to let the community do the brilliant job that it's already doing but also support them so they can support each other better and do it better at scale.
[3066.50 --> 3070.00]  But the real answer is probably one that Cassandra could give you better.
[3070.00 --> 3078.40]  So I get that a concise, clean brand is easier to communicate.
[3080.10 --> 3083.02]  And so I get that part.
[3083.02 --> 3097.32]  I'm wondering if there is a hope that Go will be seen as mature as it is, that we will also have an impact on adoption,
[3097.32 --> 3101.16]  not from the perspective of people understanding what Go does.
[3101.28 --> 3104.56]  I mean that's of course a big part if you're going to adopt a language.
[3105.16 --> 3115.82]  But also because it will seem more serious and mature and also that Google is investing in the language to the point of even wanting to do this.
[3115.82 --> 3123.80]  Is there anything like that in the general thinking for the reason to come up with this branding?
[3123.80 --> 3127.36]  It's a great question.
[3131.52 --> 3134.80]  I'm going to answer it by pointing us to another part.
[3134.86 --> 3139.30]  In fact, it's the final part that we haven't really talked about yet of the brand guide.
[3139.92 --> 3142.14]  There's a section in it called our audience.
[3143.78 --> 3146.92]  And we've never done this before.
[3146.92 --> 3158.04]  Go has had kind of an implicit audience from the beginning of generally systems programmers with CS backgrounds.
[3158.88 --> 3166.24]  And even though we've never articulated that, if you read through our material that's been developed in our documentation,
[3166.64 --> 3168.30]  it's kind of the implicit audience.
[3168.88 --> 3172.38]  We don't explain programming concepts anywhere.
[3172.38 --> 3176.60]  We expect that you know them throughout our documentation.
[3176.94 --> 3181.64]  And we often make comparisons to different languages like C in the documentation.
[3183.26 --> 3190.68]  And as part of this, we set forth that we really – for where we are and the growth that we're experiencing and our goals,
[3190.86 --> 3197.62]  we believe that Go could be the next mainstream language with broad adoption across the industry.
[3197.62 --> 3203.78]  And to get there, we recognized that there was three different audiences we needed to focus on.
[3205.16 --> 3208.82]  And we've articulated them in the brand book.
[3209.12 --> 3211.66]  The first one is potential and new programmers.
[3211.66 --> 3219.72]  And these potential Go programmers and new programmers, meaning people new to programming.
[3220.58 --> 3228.28]  This is an audience that we haven't ever targeted in the way that we want to target now.
[3228.36 --> 3235.80]  So this is an explicit declaration that we believe our audience is now people new to Go and new to programming.
[3236.44 --> 3240.30]  And that has broad impact across all that we do.
[3240.30 --> 3248.04]  And we talk about the key messages that we want to target for that audience.
[3249.78 --> 3256.14]  And I'll leave it to the listeners to read what they are in the brand book.
[3256.70 --> 3264.16]  Our second is decision makers, technical decision makers, which we use CIOs, CTOs, and tech leads.
[3264.16 --> 3273.02]  These are the people that are the people often responsible for choosing architecture or approving architecture.
[3273.38 --> 3278.56]  And we want to make sure that they have the support they need.
[3278.56 --> 3295.22]  As someone who's been in that role many times, I'm familiar with the – largely your goal is – always running through the back of your mind is what are the risks in doing something.
[3295.22 --> 3299.00]  As you know, in technical decisions, there's always tradeoffs.
[3299.84 --> 3305.56]  And trying to understand what the risks are of a given tradeoff or a given technology is important.
[3305.56 --> 3313.32]  And so we have specific messages that we'd like to land for that.
[3313.74 --> 3315.50]  And this is part of the rebrand.
[3316.84 --> 3321.80]  And the third audience is existing Go users.
[3322.66 --> 3329.18]  We definitely want to embrace these new audiences but also embrace our existing audience.
[3329.18 --> 3332.70]  And that's the audience that's served us well for 10 years.
[3333.20 --> 3337.04]  And we have key messages targeted towards that audience as well.
[3338.36 --> 3343.88]  And so I think as you read through this, you'll see this isn't answered your question.
[3344.80 --> 3355.26]  Part of it is conveying maturity, not just in visual but in our language and everything else.
[3355.26 --> 3366.00]  We really want to communicate the reality that Go is ready for production use, that you're not taking a risk to use it.
[3367.60 --> 3378.02]  And one of the challenges and opportunities of joining Google is you get to learn a lot of information that you didn't know when I was a member of the community.
[3378.02 --> 3389.58]  And now I've got an opportunity to work with many, many companies who have embraced Go, some of which have been vocal about it and some of which have not.
[3389.58 --> 3398.78]  And it's amazing to see the ones who haven't and how broad Go adoption is, much broader than I ever knew as a community member.
[3399.48 --> 3414.60]  And how these companies have embraced Go and how many, often thousands of programmers are using Go within these major companies that for their own reasons haven't been vocal about talking about that yet.
[3414.60 --> 3425.26]  And we're trying to surface that a bit more and let people know that Go is ready and Go is mature and Go is a safe decision to make.
[3426.56 --> 3428.66]  So I hope that answers the question.
[3428.86 --> 3436.48]  I think that is part of it is really we're trying to target different audiences with different messages than we have in the past.
[3436.48 --> 3449.34]  And a big part of that is letting decision makers know the value of Go and how it's not a risky decision to make.
[3450.00 --> 3451.46]  It does answer the question.
[3451.60 --> 3453.56]  It makes very good sense.
[3454.22 --> 3460.04]  It also made me curious to ask, how is the adoption of Go inside Google now?
[3461.24 --> 3463.28]  Has that grown in the past year?
[3463.28 --> 3468.92]  I know we don't talk about things like this.
[3469.26 --> 3476.28]  Google doesn't reveal – so I'll say broadly, Google does not share internal language usage.
[3477.90 --> 3487.26]  And I'll just point out what is public already, which is this week we announced G-Visor,
[3487.26 --> 3498.76]  which is a new container, a new container runtime that works with Kubernetes and Docker.
[3499.76 --> 3506.10]  And it is a sandbox container runtime.
[3506.68 --> 3509.24]  It was announced a couple days ago.
[3509.24 --> 3513.96]  I believe it might have been announced at KubeCon, which is also happening this week.
[3513.96 --> 3521.30]  But I think it's been a part of Google for years.
[3521.64 --> 3523.18]  We've just released it.
[3523.68 --> 3527.06]  It is, I think, an industry transformative.
[3527.74 --> 3532.32]  It has the power to transform our industry, particularly in cloud.
[3532.78 --> 3536.72]  It brings a brand new approach to running containers in a secure and isolated way.
[3536.72 --> 3540.72]  And this entire application is written in Go.
[3542.08 --> 3552.90]  And I think you'll see a lot of core Google projects that are being open sourced or written in Go.
[3554.30 --> 3557.96]  And that's probably the best answer I have for that question.
[3558.74 --> 3559.58]  Thank you.
[3559.58 --> 3563.98]  I know what you can say is limited, but we always try to ask anyway.
[3564.52 --> 3566.50]  Someday somebody will slip, I promise.
[3566.72 --> 3567.70]  I promise the listeners.
[3569.72 --> 3571.20]  Yeah, as long as it's not me.
[3574.52 --> 3576.86]  Yeah, I encourage people to check out G-Visor.
[3577.06 --> 3581.26]  You can see it at github.com slash google slash gvisor.
[3581.26 --> 3583.98]  And you can download it.
[3584.08 --> 3584.80]  It's open source.
[3585.22 --> 3587.26]  And it's...
[3588.26 --> 3589.26]  I should...
[3589.26 --> 3594.26]  For all those people who are in our...
[3596.72 --> 3598.56]  I haven't looked at it yet.
[3598.84 --> 3601.76]  What is the equivalent of it out there that I would know?
[3603.10 --> 3604.08]  There isn't.
[3604.08 --> 3604.46]  Kubernetes?
[3605.04 --> 3605.86]  I don't know.
[3606.00 --> 3606.68]  What would it be?
[3606.68 --> 3615.32]  So, it's a brand new approach to securing containers.
[3616.34 --> 3618.60]  And there's the post here that goes through it.
[3618.88 --> 3622.68]  But in short, historically, we've used...
[3623.36 --> 3628.38]  In spite of how light containers are and how much power and benefit they bring,
[3628.96 --> 3631.42]  they don't provide good isolation.
[3633.02 --> 3635.50]  And it's not one of their strengths.
[3635.50 --> 3636.60]  It's not part of the design.
[3636.68 --> 3644.40]  And so, historically, there's been two approaches you've used to provide that kind of isolation to them.
[3644.90 --> 3649.24]  One is to use virtual machines to emulate hardware.
[3650.64 --> 3654.84]  And that approach is expensive but effective.
[3655.68 --> 3658.86]  And then there's a second approach, which is a rule-based execution,
[3659.66 --> 3663.70]  which is using things like SC Linux and AppArmor.
[3663.70 --> 3671.66]  And GVisor creates a third approach that takes some of the advantages of each.
[3672.42 --> 3674.86]  It takes a more simple approach.
[3674.92 --> 3679.98]  So, it's a lot lighter than the virtualized approach.
[3679.98 --> 3684.38]  And it's simpler than the AppArmor approach.
[3686.70 --> 3692.70]  So, again, it's a runtime for containers in a secure way.
[3693.10 --> 3694.42]  It works with Kubernetes.
[3694.66 --> 3695.50]  It works with Docker.
[3696.28 --> 3696.74]  Cool.
[3698.12 --> 3699.38]  I see now what you're saying.
[3699.38 --> 3706.20]  Yeah, I encourage people to read the post, read me around it.
[3706.38 --> 3713.06]  It's transformative in the way that it's going to make containers.
[3714.06 --> 3719.36]  In my mind, this really – and I've been part of the container space for a very long time.
[3719.36 --> 3728.86]  So, this really is the project that tackles the biggest gap in what containers can do.
[3729.78 --> 3736.22]  So, with GVisor, I think containers are in a place where they really are the future.
[3737.58 --> 3739.76]  And it doesn't – there's no more gaps.
[3739.92 --> 3741.36]  GVisor closes the last gap.
[3741.36 --> 3744.34]  Yeah, I'm actually really excited about it.
[3744.44 --> 3746.84]  And I'm kind of sad I haven't got to play with it yet.
[3747.28 --> 3751.88]  Just getting back from Chicago and getting caught up and about to leave for Seattle.
[3752.50 --> 3753.46]  So, I'm like, no.
[3755.48 --> 3757.52]  Airplanes are good places to do work.
[3757.66 --> 3760.38]  You just got to download stuff because Wi-Fi is not that good.
[3760.74 --> 3761.40]  This is true.
[3762.64 --> 3764.98]  But, yeah, it's fun.
[3765.22 --> 3768.38]  It's fun to play with and to look at.
[3768.38 --> 3772.40]  And, you know, written and go.
[3773.56 --> 3775.84]  So, I know we were running short on time.
[3776.86 --> 3779.28]  Do we have time for projects and news?
[3779.36 --> 3779.98]  Probably not.
[3780.06 --> 3781.80]  We might have to skip to free software Friday.
[3781.98 --> 3784.66]  We've got about two minutes on the clock.
[3785.56 --> 3786.86]  Two minutes on the clock.
[3787.02 --> 3787.24]  All right.
[3787.28 --> 3788.42]  How fast can we do this?
[3788.42 --> 3792.16]  So, GVisor was in the projects and news thing.
[3793.38 --> 3794.52]  And Steve mentioned it.
[3794.52 --> 3798.84]  Go 1.10.2 and Go 1.9.5 is out.
[3800.10 --> 3807.76]  There will be a link in the show notes to this really cool intro to the compiler that is actually in the Go GitHub repo.
[3808.54 --> 3810.72]  I found a cool project called RAT.
[3810.72 --> 3813.66]  We'll link to that in the show notes.
[3814.36 --> 3825.52]  And that's a cool way of, like, running multiple commands and windowing them side by side and then, like, annotating them based on kind of patterns that show up in there.
[3825.78 --> 3826.98]  So, that's super cool.
[3827.64 --> 3828.82]  I think that's everything.
[3829.06 --> 3830.18]  Did I get it in two minutes?
[3831.46 --> 3832.12]  Let's see.
[3832.44 --> 3832.72]  You have...
[3833.72 --> 3835.76]  I'd say so.
[3835.96 --> 3837.80]  You have 35 seconds left.
[3837.80 --> 3841.64]  That should be a segment once in a while.
[3841.90 --> 3843.82]  Just, like, as fast as you can.
[3844.00 --> 3846.62]  60 seconds or 120 seconds.
[3846.74 --> 3847.94]  As many things as you can mention.
[3849.12 --> 3850.12]  Go in two minutes.
[3850.48 --> 3850.96]  I like it.
[3850.98 --> 3851.24]  All right.
[3852.66 --> 3854.14]  So, Free Software Friday.
[3854.28 --> 3857.42]  Did anybody have anyone or anything they want to give a shout out to?
[3858.52 --> 3858.92]  No.
[3860.06 --> 3861.12]  I got a good one.
[3861.12 --> 3866.08]  So, Julia Evans, if you're not following her on Twitter, you should.
[3866.60 --> 3876.28]  But she always puts out these amazing little graphic cards explaining complex things in very, very easy to digest ways.
[3876.28 --> 3886.12]  And speaking of her, she's releasing, like, a zine with, I think there's, like, 20 or something of them in there called Byte Size Linux.
[3886.68 --> 3892.32]  And we will link in the show notes, too, where you can pick that up if you want to give her some love.
[3893.18 --> 3893.50]  Excellent.
[3893.50 --> 3900.50]  I'll give a shout out to, so we had, as I mentioned, called them Go just last week.
[3900.74 --> 3909.32]  And I saw a brilliant talk from Ron Evans about GoCV and the different work.
[3909.40 --> 3914.26]  So, Ron Evans, I know he was on the blog post or on the podcast recently.
[3914.70 --> 3916.20]  I think maybe even last episode.
[3916.20 --> 3924.18]  But we know him from GoBot and all the work he does with Go and Embedded.
[3925.00 --> 3930.60]  And as part of that, he started working on GoVision stuff.
[3930.80 --> 3937.84]  So, it's detecting different, you know, faces and it can do different blurs.
[3938.00 --> 3940.70]  And he gave a really interesting talk.
[3940.78 --> 3941.76]  And I'll give one more.
[3941.76 --> 3950.20]  There was another talk by a man named Anthony Starks about Go SVG.
[3950.82 --> 3952.60]  And I was blown away by this talk.
[3952.76 --> 3957.74]  The amount of work that he's done with SVG and Go was phenomenal.
[3958.04 --> 3965.28]  And the maturity of the libraries that he's built is just – I was blown away by it.
[3966.20 --> 3969.06]  And so, big shout out to both of them.
[3969.06 --> 3974.86]  I learned about these projects and I just want to pass them along because I'm excited to play with both of them.
[3975.32 --> 3975.80]  Yeah.
[3975.88 --> 3979.54]  And Ron is an absolute trip to hang out with.
[3980.12 --> 3984.18]  So, if you're ever at a conference he's at, like, walk up and talk to him.
[3984.22 --> 3984.68]  It's amazing.
[3985.08 --> 3988.70]  And GopherCon, we always do, like, a GoBot room that he hangs out in.
[3989.48 --> 3992.64]  I met Ron a couple years back.
[3992.68 --> 3996.12]  I want to say potentially our first year there.
[3996.12 --> 3996.52]  I don't know.
[3996.56 --> 3996.98]  I can't remember.
[3997.14 --> 4000.90]  But I just remember thinking, like, this guy is fascinating.
[4002.06 --> 4004.00]  Anyways, that's Ron.
[4005.00 --> 4005.84]  Always a pleasure.
[4007.12 --> 4020.68]  So, I'm going to put a link to Anthony's GitHub account in the Hangout, in the whatever it's called, the Slack channel.
[4020.68 --> 4025.02]  He also built this amazing tool to generate slide decks.
[4026.52 --> 4031.98]  And he presented with it, and this was by far the prettiest one there.
[4032.36 --> 4035.40]  So, frankly, for me, I can't stand XML.
[4035.66 --> 4037.48]  I try and avoid it as much as possible.
[4037.96 --> 4044.62]  But that's why I'm glad people like Anthony exist, is that they make nice libraries so I don't have to write XML.
[4044.62 --> 4046.66]  All right.
[4046.84 --> 4049.58]  So, I think we are about out of time.
[4050.16 --> 4051.24]  We're probably over.
[4052.18 --> 4056.42]  But Adam, the producer, is on the show, so he can't really give us a hard time about that.
[4056.42 --> 4056.88]  Mm-mm.
[4058.84 --> 4071.72]  Well, I want to say I'm thrilled you all had me on the show because it gave me a chance to tell the story around the branding that it was clear that needed to be told.
[4071.72 --> 4080.96]  And the blog post didn't come close to telling the story of how we created it and why we created it and all of the depth in that brand book.
[4081.10 --> 4085.22]  And I just, you know, I hope that people take the opportunity to really read it.
[4086.48 --> 4089.26]  We spent, I can't tell you how many, countless hours.
[4089.94 --> 4101.28]  To think the Go team invested a considerable amount of time in writing that document because we consider it of the highest value to the project.
[4101.72 --> 4107.84]  And to be able to tell that story, I'm very grateful to be able to be on the show today.
[4108.48 --> 4110.86]  I'll say you got an open invite.
[4111.02 --> 4129.82]  When you have, you know, things like this, this important to the Go community at large, I would welcome even collaboration to give you all an opportunity to come on a show like this that hopefully communicates to the largest Go community we can in a larger form, podcast form.
[4129.82 --> 4132.82]  So, you know, we'd welcome having you back on again in the future.
[4133.82 --> 4134.90]  Well, I appreciate it.
[4134.96 --> 4136.26]  I'm always a pleasure to be here.
[4136.52 --> 4137.36]  So, yeah.
[4137.60 --> 4139.92]  Keep this in mind because we could time things.
[4139.98 --> 4143.10]  For example, it was pure luck that today was opening.
[4143.38 --> 4146.58]  I think it was really good that you came on the show to talk about this.
[4146.94 --> 4149.96]  And we weren't sure that we were going to have enough things to talk about.
[4150.08 --> 4151.18]  It turned out that we did.
[4151.18 --> 4154.34]  And I thought it was very insightful.
[4155.68 --> 4156.66]  I appreciate it.
[4156.72 --> 4157.78]  You're right.
[4158.60 --> 4162.58]  It was a, what do they call it?
[4164.16 --> 4165.66]  It was fortunistic.
[4166.20 --> 4167.98]  It was, there's a better word for that.
[4168.42 --> 4168.62]  Fortunistic.
[4169.76 --> 4171.28]  When things just work out right.
[4171.54 --> 4172.80]  And this was one of them.
[4173.42 --> 4173.78]  Serendipitous.
[4174.34 --> 4176.26]  Oh, that's the word that I was looking for.
[4176.28 --> 4176.70]  There you go.
[4176.78 --> 4177.70]  I got your back, Steve.
[4177.70 --> 4178.06]  Don't worry.
[4178.06 --> 4180.44]  I was like, I knew I couldn't get it.
[4180.56 --> 4184.62]  It was serendipitous that this happened.
[4184.84 --> 4185.40]  And you're right.
[4185.46 --> 4187.36]  We need to be more proactive about it.
[4187.36 --> 4187.62]  Yeah.
[4187.98 --> 4196.16]  We're glad to work together however we can to make sure that the GoCommit at large has the right information to be excited.
[4196.74 --> 4199.14]  To be concise.
[4199.94 --> 4201.92]  But to be, you know, purposeful in their work.
[4203.12 --> 4204.96]  That's what our goal is.
[4204.96 --> 4205.80]  We're friendly.
[4206.36 --> 4206.80]  Genuine.
[4206.80 --> 4206.88]  Genuine.
[4207.34 --> 4208.52]  That's what we're going for.
[4208.82 --> 4209.24]  Concise.
[4209.66 --> 4210.10]  Yes.
[4210.30 --> 4213.06]  But not so much in a 45 minute podcast.
[4213.30 --> 4213.40]  Maybe.
[4214.70 --> 4215.10]  But.
[4216.40 --> 4217.92]  Definitely direct and thoughtful.
[4219.24 --> 4219.96]  We're trying.
[4221.22 --> 4221.46]  Yeah.
[4221.52 --> 4222.80]  It looks like you guys are trying.
[4224.52 --> 4225.00]  All right.
[4225.10 --> 4228.00]  So I think we are definitely over now.
[4228.18 --> 4229.90]  So I suppose we should wrap things up.
[4229.90 --> 4230.58]  Yeah.
[4230.58 --> 4231.14]  Yeah.
[4231.14 --> 4232.78]  Thanks so much for coming on, Steve.
[4232.84 --> 4239.38]  I'm really glad we got to talk about that and kind of talk about the real reason that the branding was done.
[4239.38 --> 4247.20]  And it wasn't so much about the logo that was more a byproduct of the core thing that you all were going for.
[4247.20 --> 4250.34]  And hopefully this clears up a lot.
[4251.96 --> 4253.66]  So thanks, Steve, for coming on the show.
[4253.92 --> 4255.64]  Thanks, Adam, for jumping in with us.
[4256.06 --> 4258.62]  It's always fun to have you walk out from behind the curtain.
[4259.62 --> 4259.90]  I try.
[4259.90 --> 4264.48]  And as always, thank you to all of you, the listeners.
[4265.44 --> 4267.90]  Definitely follow us on Twitter at GoTimeFM.
[4269.46 --> 4276.48]  If you hit us up at github.com slash GoTimeFM slash ping to give suggestions for guests or topics.
[4277.48 --> 4279.00]  And with that, goodbye, everybody.
[4279.10 --> 4279.66]  We'll see you next week.
[4284.24 --> 4284.74]  All right.
[4284.76 --> 4286.72]  That's it for this week's episode of GoTime.
[4286.88 --> 4287.74]  I hope you enjoyed it.
[4287.74 --> 4293.60]  Do us a favor, go on Overcast, go on Apple Podcasts, go on wherever you're listening to this podcast.
[4293.96 --> 4297.62]  Favorite it, share it, like it, tweet it, whatever you got to do.
[4297.94 --> 4301.14]  Help us promote this show to your friends and fellow gophers.
[4301.90 --> 4305.34]  Bandwidth for GoTime and ChangeLog is provided by Fastly.
[4305.62 --> 4307.12]  Head to Fastly.com to learn more.
[4307.38 --> 4310.74]  And we move fast here at ChangeLog and fix things because of Rollbar.
[4311.08 --> 4312.74]  Check them out at Rollbar.com.
[4313.04 --> 4314.90]  And we're hosted on Linode servers.
[4314.90 --> 4316.94]  Head to Linode.com slash ChangeLog.
[4316.94 --> 4317.48]  Check them out.
[4317.56 --> 4318.46]  Support this show.
[4318.98 --> 4320.94]  Our music is produced by Breakmaster Cylinder.
[4321.34 --> 4328.04]  And you can find more shows just like this at ChangeLog.com or on Apple Podcasts or on Overcast or wherever you subscribe to podcasts.
[4328.54 --> 4330.70]  Thank you for tuning in and we'll see you next week.

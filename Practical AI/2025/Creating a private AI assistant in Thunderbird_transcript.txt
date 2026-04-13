[0.00 --> 8.74]  Welcome to the Practical AI Podcast, where we break down the real-world applications
[8.74 --> 13.64]  of artificial intelligence and how it's shaping the way we live, work, and create.
[13.88 --> 19.14]  Our goal is to help make AI technology practical, productive, and accessible to everyone.
[19.48 --> 23.54]  Whether you're a developer, business leader, or just curious about the tech behind the
[23.54 --> 25.12]  buzz, you're in the right place.
[25.12 --> 29.84]  Be sure to connect with us on LinkedIn, X, or Blue Sky to stay up to date with episode
[29.84 --> 33.02]  drops, behind-the-scenes content, and AI insights.
[33.36 --> 35.88]  You can learn more at practicalai.fm.
[36.00 --> 37.50]  Now, on to the show.
[49.14 --> 52.08]  Welcome to the Practical AI Podcast.
[52.08 --> 54.02]  This is Daniel Whitenack.
[54.46 --> 60.18]  I am CEO at Prediction Guard, and I'm joined, as always, by my co-host, Chris Benson, who
[60.18 --> 63.30]  is a Principal AI Research Engineer at Lockheed Martin.
[63.78 --> 64.46]  How are you doing, Chris?
[64.98 --> 66.36]  I am doing just fine.
[67.08 --> 71.70]  It's been a good day, good fall, and lots of cool things happening to talk about.
[72.10 --> 72.84]  Yeah, yeah.
[72.84 --> 79.30]  I'm excited for today's discussion, although I have to say I feel a bit outnumbered by the
[79.30 --> 85.42]  Chris's, but there's some cool Chris's on the show today, including yourself, Chris Benson.
[85.72 --> 92.64]  But we've also got with us Chris Aquino, who is a software engineer at Thunderbird.
[92.76 --> 93.02]  Welcome.
[93.34 --> 98.54]  We won't call you Chris B. Actually, your last name starts with an A, so maybe you're Chris
[98.54 --> 102.86]  A, and Chris Benson is Chris B, and that just works out because his name starts with B.
[104.00 --> 104.74]  That's perfect.
[104.96 --> 105.16]  Yeah.
[105.16 --> 105.60]  Hello.
[106.86 --> 107.06]  Hello.
[107.28 --> 108.70]  Thank you for having me.
[108.84 --> 113.82]  I know that we had some rescheduling issues early on, but we're here now.
[114.12 --> 116.16]  We're here now, and glad we are.
[116.28 --> 123.64]  Yeah, because we've had a few guests from Mozilla or projects that Mozilla has been involved with
[123.64 --> 129.10]  for some time, or a couple times in the past, and it's always great discussions, and of course
[129.10 --> 134.02]  love the perspective that Mozilla brings, but also projects like Thunderbird.
[134.02 --> 139.24]  Could you give us maybe just starting out a little bit about your personal background
[139.24 --> 143.92]  and kind of how that eventually led you into work on Thunderbird?
[144.34 --> 144.64]  Yeah.
[144.98 --> 152.22]  So my personal background, I've been a web developer since, oh my goodness, two decades.
[152.30 --> 159.58]  Let's go with two decades ago is when I started, and I worked for various companies that did
[159.58 --> 160.16]  different things.
[160.38 --> 166.04]  I've been, in addition to a web developer, I've done teaching and authoring.
[166.38 --> 172.42]  Most recently, well, prior to Thunderbird, I was at SurveyMonkey for a little while, and
[172.42 --> 178.02]  then the great layoffs of 2022 and 2023 hit.
[178.52 --> 180.90]  I was one of the newer engineers, so I got cut.
[181.40 --> 185.16]  And as I was applying for jobs, I was like, you know, I've always wanted to work for Mozilla.
[185.16 --> 188.90]  Let's just see what their job board looked like.
[189.30 --> 195.26]  And that's when I submitted an application and got word back from somebody who was clearly
[195.26 --> 196.06]  not a recruiter.
[196.52 --> 201.50]  The director of product emailed me, you know, just emailed me and said, hey, I'd love to
[201.50 --> 202.46]  talk with you.
[203.12 --> 210.12]  And yeah, that was, I initially got hired on to build just weird stuff that was outside
[210.12 --> 212.46]  of the realm of the Thunderbird desktop.
[213.38 --> 216.28]  He, his name is Ryan, Ryan Sipes.
[216.44 --> 218.44]  He had, he's always got something cooking.
[218.70 --> 224.56]  He had some interesting ideas for a set of products that he wanted to explore.
[224.90 --> 230.16]  And so he's like, yeah, could you, would you be interested in joining us and working on
[230.16 --> 232.00]  some of this, some of this weird stuff?
[232.04 --> 233.98]  And so I said, I said, yes.
[233.98 --> 239.16]  Is a quick follow-up on that is you're talking a little, just for the guests that may not
[239.16 --> 243.36]  be familiar with Mozilla and the kind of the context of Thunderbird within Mozilla.
[243.52 --> 246.96]  Could you talk a little bit about that for a moment, just to kind of set the stage?
[247.34 --> 248.64]  Yes, I will do my best.
[248.76 --> 252.62]  It is a little convoluted as Wikipedia can tell you.
[252.80 --> 254.16]  So Thunderbird, all right.
[254.20 --> 255.38]  You can think of Thunderbird.
[255.94 --> 259.62]  Well, first of all, for those who don't know, for the kids out there who are like, what
[259.62 --> 260.08]  is email?
[260.08 --> 263.06]  Now, Thunderbird is a desktop email client.
[263.56 --> 268.42]  And for a certain generation, those three words strung together means nothing, but it
[268.42 --> 276.56]  is a 20 plus year old open source project, which originated at the company now known as
[276.56 --> 276.88]  Mozilla.
[277.80 --> 283.34]  If you're familiar with the Firefox browser that is made by our sister company, the Mozilla
[283.34 --> 289.54]  Corporation and Thunderbird and the Mozilla Corporation all fall within, I guess you could say the
[289.54 --> 294.04]  guidance of the Mozilla Foundation, which is a nonprofit.
[295.26 --> 302.58]  And as of, ooh, I guess it was five, five-ish years ago, maybe a little bit longer than that,
[303.96 --> 306.80]  Mozilla was, nobody was maintaining Thunderbird.
[306.80 --> 313.52]  So this application that was not Firefox had, you know, they didn't want to deal with the
[313.52 --> 320.12]  maintenance that was, you know, engineers, engineers need to maintain this almost 20 year old C++
[320.12 --> 321.00]  code base.
[321.74 --> 326.90]  And that was for, you know, management reasons are like, okay, we could just hand this to
[326.90 --> 329.08]  the community or we could just shut it down.
[329.08 --> 335.22]  And the director of product here at, who's now the director of product, Ryan said, wait
[335.22 --> 338.22]  a minute, listen, give me a shot.
[338.30 --> 339.64]  Let me try something out.
[339.72 --> 343.90]  Let me see if I can turn this into something more than it is now.
[344.54 --> 350.74]  And they did whatever legal things and paperwork was necessary to spin it off into its own entity.
[351.22 --> 353.64]  We are known as Thunderbird or the Thunderbird Project.
[353.64 --> 360.18]  But if you look us up on the internet, we're officially MZLA, which sometimes I feel like
[360.18 --> 364.72]  it's one of those acronyms that doesn't really mean anything, but that's what it says on my
[364.72 --> 365.00]  resume.
[365.22 --> 368.24]  So that's Thunderbird in a nutshell.
[368.92 --> 376.28]  Now, yeah, you mentioned this kind of history, this sort of desktop email application history.
[376.28 --> 382.84]  Just for context, I'm sure there's many people listening that do remember those sorts of days,
[383.12 --> 388.82]  but others that might have just always used Gmail in a browser or something like that.
[388.96 --> 395.54]  But there's a whole generation of us that use something, whether it's Outlook, you know,
[395.60 --> 397.66]  a lot of people have used.
[397.66 --> 406.36]  I remember installing Ubuntu for the first time earlier in my career and using Thunderbird
[406.36 --> 408.80]  in that context on my computer.
[409.26 --> 414.84]  Now, you mentioned there's kind of maybe a different, a more vision for this now.
[415.04 --> 422.42]  Any context you could provide there in terms of, you know, the way people use email now versus
[422.42 --> 427.28]  those days when Thunderbird was being used as that desktop application.
[427.94 --> 433.42]  What is kind of the, I guess, the focus and transition, if you will, or at least some of
[433.42 --> 434.68]  the things that are being thought about?
[435.02 --> 435.22]  Yeah.
[435.98 --> 441.30]  I'll start with sort of the ethos, like why is Thunderbird still around?
[441.84 --> 444.36]  There are still people who use email.
[445.12 --> 446.90]  It works perfectly well.
[446.90 --> 455.42]  But unlike using, say, a webmail-based provider, these folks are not interested in having ads
[455.42 --> 457.12]  sort of injected for them.
[457.50 --> 461.00]  And maybe they want to be able to opt in to AI.
[461.28 --> 464.02]  They don't want an AI just like ever present and reading their emails.
[464.56 --> 469.80]  So with Thunderbird, it's free and open source, no ads ever, forever.
[470.64 --> 472.76]  And, you know, your email is your own.
[472.82 --> 474.42]  It gets downloaded to your computer.
[474.42 --> 478.14]  So if you lost internet access, you can still read your email.
[478.34 --> 484.42]  If you lost power and your laptop is open to Thunderbird, you've still got it, right?
[484.48 --> 486.34]  All those emails that you downloaded, they're right there.
[486.92 --> 493.36]  So I think that the way that email is being used, it's different.
[493.46 --> 494.16]  It's different now.
[494.30 --> 499.02]  One of the great things about Thunderbird back in the early days, and it's still true today,
[499.12 --> 502.60]  is it's very easy to manage multiple email accounts.
[502.60 --> 509.54]  That was, you know, I remember a time when like, oh, you have more than one email address?
[509.96 --> 510.40]  Amazing.
[511.24 --> 512.46]  You must be really important.
[512.56 --> 518.34]  And now you can just sign up for email addresses, dozens of them if you want, and, you know,
[518.70 --> 520.58]  have them each dedicated to a different purpose.
[520.94 --> 522.52]  You can still do that with Thunderbird.
[522.52 --> 530.00]  However, one of the things that people are encountering now, as we all are, is a certain
[530.00 --> 532.26]  amount of information overload, right?
[532.36 --> 539.40]  You're subscribed to so many newsletters and mailing lists, and you, you know, you're working
[539.40 --> 542.26]  on some, collaborating on some side project.
[542.36 --> 545.28]  And then you've got your main work email.
[545.28 --> 548.54]  How do you, how do you read?
[548.66 --> 549.66]  How do you read all that email?
[549.76 --> 551.10]  How do you deal with all of it?
[551.52 --> 556.20]  So those are the sorts of things that we're thinking about now is how do we empower the
[556.20 --> 562.04]  user to better deal with just this huge influx of information that they're getting every
[562.04 --> 563.42]  day, every hour?
[564.14 --> 569.72]  So first off, thank you for validating my multiple email use.
[569.72 --> 577.36]  Every once in a while, my wife gives me a hard time because, you know, I generate a new email
[577.36 --> 583.28]  like every once in a while when I get frustrated with my email feed or have a specific purpose.
[583.28 --> 589.06]  And it seems like no one knows, no one ever knows which email to email me at, which maybe
[589.06 --> 591.04]  is a strategy in and of itself.
[591.04 --> 592.42]  I'm not sure.
[592.88 --> 594.92]  So thanks for validating that.
[594.92 --> 605.82]  But yeah, I know that there's a good amount of kind of AI intersection with email, whether
[605.82 --> 608.92]  that be from like the web email side.
[609.22 --> 618.08]  So in Gmail or other things with Gemini or email clients that maybe are specifically geared
[618.08 --> 622.36]  towards AI features like a superhuman or these sorts of things.
[622.36 --> 628.48]  Not asking you to comment on every single one of those, but maybe in general, like how
[628.48 --> 634.70]  from your perspective, have you viewed this gradual integration with AI and what sort of,
[634.70 --> 641.38]  I guess, categories could people have in their mind of the kinds of ways that AI is being
[641.38 --> 647.88]  applied within email and some of those trade-offs that maybe you're making when you're using
[647.88 --> 653.54]  those features that, of course, I know we'll talk about privacy in some of what we talk
[653.54 --> 654.54]  about with Thunderbird.
[654.76 --> 661.36]  But maybe just from a perspective, we'd be curious on how you categorize AI in email could
[661.36 --> 662.46]  mean a lot of things.
[662.68 --> 665.64]  Could you help people understand maybe some of that landscape?
[666.28 --> 666.62]  Sure.
[666.96 --> 667.16]  Yeah.
[667.32 --> 673.72]  I think that the two main ways that I see, I mean, in my own Gmail account, because I will
[673.72 --> 679.80]  use a device that doesn't have Thunderbird on it because I am a, I'm a longtime distro
[679.80 --> 684.54]  hopper and maybe I'm using a distro that doesn't have Thunderbird prepackaged and I'm
[684.54 --> 685.70]  just, I'm just trying things out.
[686.10 --> 692.50]  I have found that the automatic summarization is a thing that, you know, Gmail's like, hey,
[692.62 --> 694.46]  Gemini can do this for you.
[694.46 --> 702.00]  Or all of the autocomplete that it tries to helpfully offer me, I feel like it's a little
[702.00 --> 705.40]  creepy sometimes, especially depending on what the email is.
[705.50 --> 712.26]  Like if I'm talking to my doctor over email and it's like, clearly this LLM has read this
[712.26 --> 713.70]  very private information.
[713.70 --> 716.22]  I'm like, oh, how do I turn this off?
[716.48 --> 721.72]  But I do understand that for a lot of people, those two features, they are time savers.
[721.72 --> 729.70]  You have this way of compressing more human time into your day by offloading it to an LLM.
[729.94 --> 730.78]  So that's great.
[730.86 --> 734.92]  It's a, it's a time saver and it's great that people have access to that.
[735.22 --> 741.34]  Some things that you lose out on that you're, you're gaining time, but what you're trading
[741.34 --> 743.72]  are things like tone, right?
[743.82 --> 751.02]  You, you, the tone is for some summarization models, you will, it will kind of strip out all
[751.02 --> 757.72]  the tone or if it's bulk summarizing multiple emails that, you know, email from your mom
[757.72 --> 759.40]  doesn't really sound like your mom.
[759.48 --> 762.58]  It is literally just like your mother's coming to town this weekend.
[763.32 --> 770.32]  So there, there's maybe dehumanization of email is kind of the, the wrong term or maybe a little
[770.32 --> 775.50]  extreme, but that gets essentially normalized to the tone of the LLM.
[775.50 --> 781.40]  Um, and yeah, to your point, the, the privacy aspect, that's, that's kind of the, the big
[781.40 --> 783.12]  one, uh, for us here at Thunderbird.
[783.24 --> 790.24]  We're very privacy respecting, privacy preserving because that a lot of our users choose to use
[790.24 --> 794.94]  Thunderbird, uh, because of that they want to manage and own their own email.
[794.94 --> 803.26]  Um, they don't want, they don't want their personal emails harvested for marketing purposes
[803.26 --> 804.56]  or for training data.
[804.56 --> 825.08]  Well, friends, when you're building and shipping AI products at scale, there's one constant
[825.08 --> 826.02]  complexity.
[826.40 --> 826.84]  Yes.
[826.90 --> 830.26]  Your wrangling models, data pipelines, deployment infrastructure.
[830.26 --> 833.84]  And then someone says, let's turn this into a business.
[834.30 --> 835.56]  Cue the chaos.
[836.06 --> 837.38]  That's where Shopify steps in.
[837.48 --> 842.70]  Whether you're spinning up a storefront for your AI powered app or launching a brand around
[842.70 --> 843.50]  the tools you built.
[843.90 --> 849.78]  Shopify is the commerce platform trusted by millions of businesses and 10% of all U S e-commerce
[849.78 --> 856.78]  from names like Mattel, Jim shark to founders, just like you with literally hundreds of ready
[856.78 --> 861.50]  to use templates, powerful built in marketing tools and AI that writes product descriptions
[861.50 --> 862.08]  for you.
[862.48 --> 865.02]  Headlines, even polishes your product photography.
[865.58 --> 867.18]  Shopify doesn't just get you selling.
[867.34 --> 869.04]  It makes you look good doing it.
[869.16 --> 870.18]  And we love it.
[870.18 --> 871.56]  We use it here at change log.
[871.70 --> 872.48]  Check us out.
[872.60 --> 873.00]  Merch.
[873.28 --> 873.66]  Change all.
[873.80 --> 874.12]  Dot.
[874.32 --> 880.54]  That's our storefront and it handles the heavy lifting to payments, inventory, returns,
[880.92 --> 882.52]  shipping, even global logistics.
[882.52 --> 887.08]  It's like having an ops team built into your stack to help you sell.
[887.44 --> 890.24]  So if you're ready to sell, you are ready for Shopify.
[890.86 --> 897.56]  Sign up now for your $1 per month trial and start selling today at shopify.com slash practical
[897.56 --> 898.10]  AI.
[898.64 --> 903.20]  Again, that is shopify.com slash practical AI.
[903.20 --> 915.00]  Well, Chris, we were starting to get into a little bit of, I guess, the intersection of
[915.00 --> 919.94]  the ethos of Thunderbird with these sorts of AI features.
[920.78 --> 925.58]  Now, could you, could you help us understand, I guess, like we talked about autocomplete, we
[925.58 --> 927.64]  talked about summarization, for example.
[927.64 --> 936.06]  There are various mechanisms by which these features can be implemented in an email client
[936.06 --> 943.12]  or an application or web application, whatever that is, in terms of the actual AI model,
[943.32 --> 947.60]  where it sits, how the data flows, what the model is trained on, maybe.
[947.96 --> 950.20]  Could you help us understand that piece?
[950.20 --> 958.30]  What are the buffet of options available to us in terms of how we might, like the integration
[958.30 --> 960.08]  point and the flow of data?
[960.48 --> 960.74]  Sure.
[960.98 --> 967.38]  Yeah, we have discussed at length different ways that we could approach this.
[967.64 --> 977.36]  So let me begin by saying that this experimental work in bringing an AI assistant to Thunderbird,
[977.54 --> 979.02]  this is not baked into Thunderbird.
[979.02 --> 981.70]  We're not going to turn it on for users.
[981.90 --> 985.30]  It's not going to be automatic or anything like that.
[985.74 --> 992.62]  Instead, what we've done is we have built it as, I'm going to call it sort of like a companion
[992.62 --> 993.36]  for right now.
[993.74 --> 994.78]  We'll put a pin in that.
[994.96 --> 1000.00]  We'll return to that because there's a lot of decisions we had to make because of that
[1000.00 --> 1000.44]  approach.
[1000.44 --> 1009.36]  Now, our options that were available to us, we could just do like add model inference to
[1009.36 --> 1010.48]  Thunderbird itself.
[1010.76 --> 1015.60]  This is, in my opinion, like, yeah, but now this is us turning it on for all users.
[1015.60 --> 1019.52]  It's like, just add the model in there and allow us to do inference locally.
[1019.52 --> 1021.68]  It's private, right?
[1021.74 --> 1022.92]  And that's great.
[1023.40 --> 1030.02]  However, we're not so invested in this idea that we want to put that on the desktop team's
[1030.02 --> 1030.46]  roadmap.
[1030.84 --> 1036.70]  When I say the desktop team, just a little plug for the mobile team at Thunderbird.
[1036.84 --> 1039.34]  There, you can grab it for Android now.
[1039.60 --> 1040.20]  Works really well.
[1040.20 --> 1042.42]  iOS is coming soon.
[1043.24 --> 1048.48]  But as far as the desktop client goes, they already had their roadmap and we just kind
[1048.48 --> 1051.58]  of want to run our AI experiment parallel to that.
[1052.68 --> 1052.94]  Okay.
[1053.12 --> 1055.62]  So that's one option.
[1056.00 --> 1064.62]  A second option is like, well, could we run inference in a separate application also locally?
[1065.24 --> 1066.06]  Yes, we can.
[1066.06 --> 1071.02]  And we've kind of poked around with that, but we don't necessarily, if we want to roll
[1071.02 --> 1076.32]  this out, we don't necessarily want to require users to download a second application.
[1076.84 --> 1076.98]  Okay.
[1077.04 --> 1078.72]  So, well, how do we split the difference here?
[1078.90 --> 1079.12]  All right.
[1079.14 --> 1084.28]  So what if we, what if we called out to an API, like one of the cloud providers for,
[1084.28 --> 1090.28]  you know, any of the models that would be good at helping you out with email, the typical
[1090.28 --> 1092.98]  tasks of summarization or reply generation.
[1092.98 --> 1098.54]  So we decided that could be a thing because it doesn't require installing anything, you
[1098.54 --> 1103.64]  know, heavyweight and additional, but that brings up a separate problem of like, where,
[1103.80 --> 1106.18]  where are you sending the email data to?
[1106.80 --> 1110.88]  And I'm happy I will be talking more at length about that.
[1111.58 --> 1111.70]  Yeah.
[1111.88 --> 1112.08]  Yeah.
[1112.08 --> 1120.14]  I think in all my discussions in my day job work, that's often what it comes down to is
[1120.14 --> 1122.68]  we would love your AI features.
[1123.38 --> 1124.56]  Where is the data going?
[1124.96 --> 1128.16]  So I definitely, I definitely understand that.
[1128.16 --> 1136.98]  And I assume that, you know, there's definitely this tension of doing things locally and putting
[1136.98 --> 1143.18]  that on, like you said, the desktop roadmap, but also there, you know, would potentially
[1143.18 --> 1151.38]  be kind of either limitations in terms of the kind of model you could use, or even just
[1151.38 --> 1159.16]  if you could use a model that worked well, but it might just like destroy all of the battery of
[1159.16 --> 1162.12]  the device on which it's running or, or that sort of thing.
[1162.18 --> 1165.30]  Were those, were those things also part of that conversation?
[1165.30 --> 1171.92]  They definitely were, especially regarding the, you know, the, the second application that,
[1171.96 --> 1175.18]  you know, just ran a model inference process in the background.
[1175.18 --> 1180.54]  I don't know about you, but I, my laptop, my work laptop, not super fancy.
[1181.14 --> 1188.28]  It generates, you know, a few tokens per second, which is, it's just not fast enough for this.
[1188.54 --> 1191.94]  I mean, literally for me to work on the thing that I'm working on.
[1192.14 --> 1199.52]  So that was a big concern that, and, you know, a lot of our users are on Linux and they're
[1199.52 --> 1205.16]  running Linux because maybe they're, they're continuing to use their perfectly good hardware.
[1205.18 --> 1210.86]  hardware from 10 years ago, which most certainly cannot do any sort of local model, anything,
[1210.86 --> 1213.06]  but yeah, laptop users.
[1213.26 --> 1215.02]  I love my battery life.
[1215.32 --> 1220.82]  I don't want to completely destroy it by trying to summarize to a batch of today's emails.
[1221.30 --> 1221.42]  Yeah.
[1221.58 --> 1221.84]  Yeah.
[1221.84 --> 1222.56]  That makes sense.
[1223.14 --> 1230.50]  So you mentioned this idea of using a model that is behind a remote API.
[1231.16 --> 1233.26]  There's obviously a selection.
[1233.26 --> 1234.70]  We're kind of narrowing in.
[1234.70 --> 1238.72]  There's a sort of selection of ways that, that that could happen.
[1238.72 --> 1248.38]  And there's like various approaches around maintaining privacy there from just using an API
[1248.38 --> 1254.68]  that explicitly doesn't store certain data, at least according to their terms, or doesn't
[1254.68 --> 1258.56]  train on your data, uh, at least according to their terms.
[1258.56 --> 1265.86]  There's also kind of, uh, you know, I know people are exploring kind of, uh, homomorphic
[1265.86 --> 1269.48]  encryption and all of these things to like, keep, keep data private.
[1269.48 --> 1271.64]  And then there's sort of end to end encryption.
[1271.64 --> 1277.46]  And there's, there's all sorts of ways that you could think about privacy in that context.
[1277.46 --> 1284.10]  What, what were the main, I guess, the main pillars of what were important for you all
[1284.10 --> 1284.76]  to consider?
[1284.76 --> 1288.54]  Was that where data is stored at rest?
[1288.54 --> 1295.36]  Is it the openness of the, the models or whether you were hosting those or a third party was
[1295.36 --> 1296.20]  hosting those?
[1296.20 --> 1297.14]  Was it, yeah.
[1297.14 --> 1302.86]  What, what were kind of the main, the main topics that came up once you kind of, you
[1302.86 --> 1306.46]  know, dipped into that, uh, remote inference side of things?
[1307.12 --> 1307.94]  That is a great question.
[1307.94 --> 1311.10]  And I have, I'm going to try to condense the story down.
[1311.20 --> 1312.04]  Okay, great.
[1312.46 --> 1317.76]  It'll be kind of like, you know, the Hobbit and then the three parts of, um, the rest of
[1317.76 --> 1318.18]  the story.
[1318.34 --> 1318.74]  Sure.
[1318.74 --> 1319.22]  Wow.
[1319.64 --> 1325.82]  You should just totally like revoke my nerd card now for not coming up like off the top
[1325.82 --> 1326.42]  of my head.
[1326.42 --> 1326.94]  Fellowship of the ring.
[1327.08 --> 1327.82]  That's the one.
[1328.08 --> 1328.32]  Exactly.
[1328.76 --> 1330.50]  I just lost half of your listeners.
[1330.82 --> 1332.62]  The two towers, return of the king.
[1332.90 --> 1333.10]  Yeah.
[1333.98 --> 1334.70]  You got it.
[1334.76 --> 1341.54]  I, I, I, at least, uh, I, I might not know about the cool encryption stuff that you're about
[1341.54 --> 1345.64]  to talk about or whatever that is, but at least, at least I have that one.
[1346.24 --> 1346.72]  Nice.
[1346.72 --> 1348.80]  Well, our powers combined.
[1349.08 --> 1350.10]  The powers combined.
[1350.22 --> 1351.08]  It takes a community.
[1351.46 --> 1351.58]  Yes.
[1352.16 --> 1352.46]  Yes.
[1353.22 --> 1361.12]  Um, so to, let me, let me start this little story off with, uh, the very earliest experiment
[1361.12 --> 1365.62]  with this was as a Thunderbird add-on.
[1366.10 --> 1366.36]  Okay.
[1366.40 --> 1366.84]  What is it?
[1366.88 --> 1368.34]  What is a Thunderbird add-on?
[1368.40 --> 1372.66]  A Thunderbird add-on, um, you're familiar with, and your listeners are probably familiar
[1372.66 --> 1373.78]  with browser extensions.
[1374.56 --> 1375.08]  Okay.
[1375.08 --> 1383.64]  So fun fact, Thunderbird under the hood uses the gecko rendering, the gecko engine from
[1383.64 --> 1384.14]  Firefox.
[1384.64 --> 1393.22]  So we, we have access to APIs that can make, make it possible so that, uh, something almost
[1393.22 --> 1397.48]  exactly like a browser extension can reside within Thunderbird.
[1397.82 --> 1403.56]  And if you're not familiar with extent, like browser extension development, um, it's basically
[1403.56 --> 1405.68]  like HTML, CSS, and JavaScript.
[1405.68 --> 1414.60]  So we started by writing something that was, it was the most 1990s looking webpage that was
[1414.60 --> 1419.54]  just sort of like jammed into an add-on and just displayed in a new tab in Thunderbird.
[1419.54 --> 1426.82]  And it was, I mean, you know, it looked like an engineer built it and that's totally fine.
[1427.10 --> 1430.96]  But, uh, yeah, that's when we started with calling, like we started off with open eight
[1430.96 --> 1437.80]  AI's API and just handing off a number of emails to like, I think it was chat GPT four.
[1437.80 --> 1444.20]  And that did a, that did an okay job, but what that was like, okay, it does work.
[1444.58 --> 1445.74]  How do we build this out?
[1445.80 --> 1451.68]  And then we started, we started trying to get better results with some prompts tuning and
[1451.68 --> 1451.98]  whatnot.
[1452.36 --> 1459.64]  And then for, as we started, you know, uh, trying to use it with more people within Thunderbird,
[1459.74 --> 1463.44]  we found out like these people, their emails are sensitive.
[1463.44 --> 1466.76]  Like we don't, what do we, we need to do something about this.
[1466.80 --> 1471.66]  So we started shopping around for some sort of, you know, cloud-based provider that could
[1471.66 --> 1475.38]  give us a guarantee of, yes, we do not store your data.
[1476.06 --> 1477.76]  Um, no, we're not using it for training.
[1478.42 --> 1482.80]  And we talked to, we were in contact with a couple of different companies.
[1482.96 --> 1487.56]  Um, some of whom just sort of sent us to like a, like one of the pages on their website,
[1487.56 --> 1491.30]  which told us nothing useful, couldn't give us a good guarantee.
[1491.30 --> 1497.74]  So, um, that's when we started talking to the folks at Flower Labs.
[1497.74 --> 1503.20]  And I know that you have had several guests from Flower, uh, on the show.
[1503.42 --> 1506.94]  I just want to say that they are so terrific to work with.
[1507.20 --> 1512.40]  They took care of, I mean, really, they took care of like all of our needs.
[1512.58 --> 1518.22]  Um, they moved things around on their own development roadmap, uh, and gave us early access to things
[1518.22 --> 1525.12]  like end-to-end encryption, um, and access to their, um, their newest product, uh, Flower
[1525.12 --> 1528.38]  Intelligence, uh, which it is.
[1528.52 --> 1533.20]  So for the listeners who hadn't listened, hadn't heard of Flower or listened to previous episodes,
[1533.20 --> 1539.06]  they're known for their, um, their federated learning SDK, right?
[1539.06 --> 1546.08]  They built software that sort of does learning on individual nodes and then shares the learnings
[1546.08 --> 1547.70]  with a centralized server.
[1548.22 --> 1549.46]  Um, all very cool stuff.
[1550.10 --> 1551.04]  We didn't need that though.
[1551.52 --> 1559.80]  We, we needed private, uh, API or rather API access to a private LLM.
[1559.80 --> 1567.90]  Um, what we got in addition to that is we got a nice SDK in TypeScript and we also got, so
[1567.90 --> 1571.16]  we got the end-to-end encryption and, oh, right.
[1571.26 --> 1577.00]  They found a model for us and then they, they did some post training on email summarization.
[1577.30 --> 1580.98]  They built an eval system so they could like fine tune.
[1581.24 --> 1586.08]  They help produce prompts, you know, through the eval system.
[1586.28 --> 1588.34]  I mean, they've just, they've been incredible.
[1588.34 --> 1594.54]  I'm just curious as you, as you talk about this and especially having had, uh, uh, multiple
[1594.54 --> 1598.72]  folks from Flower on the show in the past, you're talking a little bit about kind of how
[1598.72 --> 1603.40]  you got into the collaboration, but like, how did you, how did Flower come into the picture
[1603.40 --> 1604.58]  to begin with for you guys?
[1604.72 --> 1610.52]  You know, how was that connection made and, and, and how, as you were looking at that connection
[1610.52 --> 1616.66]  potential, how did you know that that was a good fit for this new strategy that you've
[1616.66 --> 1617.34]  been laying out?
[1617.34 --> 1621.58]  I have the most boring yet magical answer to that question.
[1621.68 --> 1625.68]  It just kind of fell into our laps because, um, Mozilla, all right.
[1625.76 --> 1632.12]  Remember I was talking about the, the nonprofit Mozilla foundation, uh, under which Thunderbird
[1632.12 --> 1634.60]  sits, they're an investor in Flower.
[1634.60 --> 1644.04]  And so, uh, Mark Sermon connected Ryan, my boss's boss's boss, uh, with Daniel from Flower.
[1644.16 --> 1646.64]  And I just ended up on a zoom with him one day.
[1646.84 --> 1649.76]  Ryan introduced us and said, all right, take it away.
[1649.76 --> 1651.96]  Um, and that's when the collaboration began.
[1651.96 --> 1658.38]  Um, I, and so that's the thing, I guess having a human face to go with the company made me
[1658.38 --> 1663.06]  feel good about those guarantees of like, no, we're, we're literally not in the business
[1663.06 --> 1664.04]  of harvesting data.
[1664.04 --> 1668.42]  Like we, we're going to set up this infrastructure and we literally can't help you debug your
[1668.42 --> 1669.94]  prompt because it's encrypted now.
[1669.94 --> 1677.24]  Um, so that was, um, the fact that they, they've been so, they were so helpful at every step,
[1677.24 --> 1682.32]  except when I sent some bad data, like the fact that they were like, we really want to help you,
[1682.32 --> 1687.42]  but we built it in a way that we can't, we can't see it, the data.
[1687.72 --> 1690.18]  So that was, it was a fortuitous connection.
[1690.58 --> 1692.96]  Thanks to the reach of, of the Mozilla foundation.
[1693.68 --> 1699.66]  Well, Chris, uh, you started kind of, uh, unveiling some of what made this,
[1699.66 --> 1704.86]  this particular, uh, route of experimentation useful for you all.
[1704.86 --> 1710.02]  Could you help us understand maybe just at a, at a slightly, uh, deeper level?
[1710.02 --> 1721.20]  Like I could, let's say, spin up a model in VLM in a VM on GCP or wherever I host things
[1721.20 --> 1723.88]  and then connect to that over an API.
[1723.88 --> 1731.58]  What, what kind of makes the, the hosting of the private model within the flower system?
[1731.58 --> 1737.84]  Cause it's, it's like you say, it's not federated, but there is still kind of more there as, as
[1737.84 --> 1741.50]  you mentioned, of course, there's the post training that you talked about, but as far
[1741.50 --> 1744.14]  as the inference side, could you help us understand that a little bit more?
[1744.92 --> 1745.24]  Yes.
[1745.24 --> 1750.60]  So as I mentioned, they, they take, they've taken care of all of that, which is, that is
[1750.60 --> 1751.60]  the big benefit.
[1751.72 --> 1756.96]  They've really been a great technical partner, um, while we conducted these, these experiments.
[1757.44 --> 1763.18]  Um, and from the privacy aspect, you know, our, my coworkers no longer have to prune their
[1763.18 --> 1769.90]  inbox and remove anything sensitive before trying out, um, uh, what we, at this point we
[1769.90 --> 1771.66]  have dubbed Thunderbird assist.
[1771.66 --> 1775.16]  It is your personal executive assistant within Thunderbird.
[1775.34 --> 1776.44]  That was, that was the idea.
[1776.64 --> 1782.16]  Anyway, um, thanks to the, the guarantees made by flower, you know, we were then able to try
[1782.16 --> 1788.74]  out, I mean, we didn't land on that, uh, that the current model immediately.
[1789.00 --> 1795.76]  We tried different births, different Barts, Roberta, all the various summarization models.
[1795.76 --> 1800.50]  And then one day the summaries got way better.
[1800.82 --> 1803.74]  And I said, what did you do?
[1804.24 --> 1805.58]  What is this magic?
[1806.02 --> 1812.88]  They switched to, um, one of the llamas from Meta that was trained for conversation.
[1813.74 --> 1816.94]  And it just, it worked better for email content.
[1817.30 --> 1822.36]  So at that point we stopped thinking about the prompt because they had squared that away.
[1822.36 --> 1827.60]  And prior to that, they found a model that could do the task very well.
[1828.06 --> 1833.44]  So then that got to the part where we're like, okay, so it's really great at summarization
[1833.44 --> 1834.72]  and reply generation.
[1835.20 --> 1840.24]  Um, the third feature that we worked on, you know, this is the biggest thing we aimed for,
[1840.28 --> 1845.70]  because when you think about like, oh, Hey, you're doing email summarization and reply generation.
[1845.70 --> 1846.14]  That's great.
[1846.14 --> 1847.32]  That's great.
[1847.50 --> 1852.18]  That's basically the hello world of, uh, you know, LLMs summarizes text.
[1852.66 --> 1859.72]  So we started working on something that was, um, or we had been working on this feature that was,
[1859.72 --> 1861.52]  it did not work well.
[1861.54 --> 1867.30]  It was, we refer to it as the daily brief and it was intended to be an executive summary of
[1867.30 --> 1868.32]  your recent emails.
[1868.32 --> 1871.90]  This is when I learned the definition of overprompting.
[1872.68 --> 1880.62]  What I would do is I would take however many emails arrived in the last 24 to 48 hours,
[1881.68 --> 1888.76]  ship it off to the model and then ask it to do, oh, can you find the most important messages,
[1889.42 --> 1897.70]  extract all of the highlights and any action items and return those back to me,
[1897.70 --> 1903.24]  grouped in this particular way with, you know, links back to the original emails.
[1903.52 --> 1908.02]  I mean, the garbage that I got back sometimes was epic.
[1908.44 --> 1912.62]  So I then learned that, okay, what I need to do is I need to split this up into multiple,
[1912.70 --> 1914.92]  multiple requests, right?
[1915.00 --> 1918.84]  Let's like, let's send a batch and only ask for importance.
[1919.60 --> 1923.24]  Some of your listeners are like, okay, that's highly subjective.
[1923.24 --> 1925.42]  And I will return to that momentarily.
[1925.86 --> 1932.82]  But when we provided the emails, we also provided the unique message IDs from Thunderbird.
[1932.92 --> 1938.74]  So that way I could then, you know, use that as an index, grab the original emails again,
[1938.74 --> 1944.20]  and send off a second request, which was like, okay, so for these, I want you to find the action
[1944.20 --> 1946.54]  items and then take the same batch.
[1946.88 --> 1950.66]  Now ask for highlights and, you know, crucial information.
[1951.52 --> 1954.68]  The formatting task never worked well.
[1955.46 --> 1959.52]  So I will, I have lots of feelings about that.
[1959.60 --> 1960.90]  So we'll put a pin in that.
[1960.98 --> 1966.78]  The formatting never turned out because that was what I wanted as an application developer,
[1967.48 --> 1969.40]  the LLM was not capable of, right?
[1969.40 --> 1972.34]  It was, it's a statistical model.
[1972.62 --> 1977.42]  And I guess it's thinking that maybe they want the header bolded sometimes, and maybe
[1977.42 --> 1978.06]  they don't.
[1978.12 --> 1980.36]  I'm like, LLM, do what I want.
[1980.88 --> 1982.22]  And it's like, who knows?
[1982.26 --> 1982.88]  I'll roll the dice.
[1983.00 --> 1984.40]  Maybe I'll give it to you the way that you want.
[1985.02 --> 1993.52]  And so that was, that was an important lesson was like, okay, so in this currently, you,
[1993.52 --> 2000.84]  you really need to be very careful, specific and constrained in what you ask the model for.
[2001.90 --> 2008.14]  And then the problem turned into, okay, so how long does it take to make these subsequent
[2008.14 --> 2008.92]  requests?
[2009.48 --> 2011.36]  What can we parallelize?
[2011.88 --> 2017.84]  How do we do that effectively without, you know, burning up all of Flowers compute in their
[2017.84 --> 2018.38]  infrastructure?
[2018.38 --> 2026.34]  So we started looking for, you know, ways to optimize that and we switched to a local
[2026.34 --> 2027.60]  Bayesian classifier.
[2027.78 --> 2030.98]  So we'll take the first of several tasks and we'll just do that locally.
[2031.20 --> 2039.42]  So instead of asking an LLM to very subjectively decide what sounds important or what is, what
[2039.42 --> 2046.92]  the cosine similarity algorithm tells them is important, we'll do that locally.
[2046.92 --> 2052.78]  We'll let the user use the Thunderbird feature of tagging emails as, you know, like priority
[2052.78 --> 2054.20]  one, priority two, whatever.
[2054.78 --> 2061.44]  So for our experimentation, we had each user tag a handful of messages as, you know, highest
[2061.44 --> 2063.94]  importance and tag a handful as least important.
[2064.60 --> 2069.56]  And then the local Bayesian classifier that was, we just included as a JavaScript library
[2069.56 --> 2075.04]  in the Thunderbird add-on works very quickly, even for lots and lots and lots of messages.
[2075.04 --> 2079.50]  And so, okay, task number one, taken off the plate of the LLM.
[2079.96 --> 2084.22]  And so now we just have it do the, you know, the rest of the tasks.
[2084.84 --> 2088.44]  And likewise, the formatting task, we just handled that ourselves.
[2088.86 --> 2090.44]  A quick note about formatting.
[2090.82 --> 2098.44]  For a time when we were using one of the other third party cloud providers, we found that
[2098.44 --> 2104.26]  you could provide them a JSON schema that the model would conform to when giving you the
[2104.26 --> 2104.86]  response.
[2105.60 --> 2111.02]  That was a magical time for me as an application developer, because it's like, oh yeah, give
[2111.02 --> 2111.64]  me the JSON.
[2111.92 --> 2116.08]  I will just put it through my framework and it's just going to render the things beautifully.
[2116.24 --> 2120.68]  Like, look at my CSS applied so perfectly to this.
[2120.80 --> 2121.76]  This is amazing.
[2121.76 --> 2128.74]  When we, as we were model hopping and provider hopping, you know, that kind of went away and
[2128.74 --> 2135.02]  we haven't returned back to it because at some point we realized that, okay, so learning our
[2135.02 --> 2140.74]  lesson from before about splitting up tasks, I, we realized that we need to take a different
[2140.74 --> 2142.82]  approach for the daily brief.
[2142.82 --> 2150.36]  And this is when I, I got it in my head that like, okay, so the future of this feature is
[2150.36 --> 2156.68]  not to just keep on sequentially prompting the same language model for like, hey, now do
[2156.68 --> 2156.98]  this.
[2157.10 --> 2157.68]  Now do this.
[2157.68 --> 2163.44]  Instead, I think of like, you know, you go into a professional chef's kitchen and you
[2163.44 --> 2169.34]  don't see like this one giant tool that can slice dice and microwave and air fry on top
[2169.34 --> 2169.70]  of that.
[2169.82 --> 2173.92]  You see lots of little dedicated tools that are like in expert hands.
[2173.92 --> 2177.56]  It, it does, it does that one thing and it's going to do it the best.
[2177.80 --> 2183.36]  So one of the things that we've got that I have written down in my mad science notebook
[2183.36 --> 2191.42]  is to explore like, well, what if we could dedicate some small models to specific tasks
[2191.42 --> 2195.00]  and then coordinate them in some sort of much more deterministic way.
[2195.20 --> 2201.34]  So the, the daily brief currently, all that to say the daily brief currently has been kind
[2201.34 --> 2207.96]  of sidelined and, you know, we're like, okay, so shipping assist means more or less summarization
[2207.96 --> 2209.56]  and reply generation.
[2209.56 --> 2214.96]  Um, and daily brief, we still need to work on that because again, the, the approach needs
[2214.96 --> 2218.52]  to be more, more granular and more, uh, more deterministic.
[2219.00 --> 2221.66]  I'm kind of curious as you've taken us through that process.
[2221.66 --> 2227.34]  One of the things on my mind is how different kind of, you know, I don't, for lack of a better
[2227.34 --> 2234.22]  word audiences within your customer base, um, different profiles, uh, you know, how these
[2234.22 --> 2238.84]  different approaches that you've taken as you guys have devised the strategy forward on
[2238.84 --> 2242.10]  Thunderbird, where are you seeing more uptake?
[2242.20 --> 2246.24]  Where are you seeing, you know, people like, you know, we, I think in early in the conversation,
[2246.24 --> 2251.02]  we talked about, um, younger generation who may not have grown up with email like we did.
[2251.02 --> 2255.88]  And then on the, on the far side of that, you have kind of the corporate world and stuff
[2255.88 --> 2256.52]  like that.
[2256.52 --> 2263.28]  And with a, with a, you know, a certain segment of your, of your user base, uh, in different
[2263.28 --> 2269.08]  aspects, I'm just curious, um, how that may have, uh, how people are receiving this in
[2269.08 --> 2272.36]  those different capacities, given the fact that you have different interests and stuff.
[2273.00 --> 2273.16]  Yeah.
[2273.36 --> 2273.58]  Yeah.
[2273.76 --> 2278.96]  Well, the, the short answer is that our users are fairly homogenous at this point.
[2279.08 --> 2281.94]  Our users of Thunderbird assist are very homogenous.
[2282.18 --> 2283.82]  They are all Thunderbird employees.
[2285.64 --> 2288.38]  Because it is, yeah, it does.
[2288.46 --> 2288.74]  It does.
[2288.74 --> 2292.22]  And even though this work is, it is open source, it's on GitHub right now.
[2292.58 --> 2299.30]  Um, uh, we haven't released it, um, you know, for general use because again, flower, flower,
[2299.30 --> 2306.50]  um, had been tuning the, the models and making changes to their infrastructure.
[2306.50 --> 2313.78]  Um, so they weren't ready to receive like, uh, a lot of users from all over the world.
[2314.18 --> 2317.56]  So within Thunderbird there, there are even different needs.
[2317.56 --> 2322.44]  Some people use the, uh, individual email summary feature.
[2322.64 --> 2322.94]  Okay.
[2323.00 --> 2323.76]  So let me back up.
[2323.82 --> 2328.10]  There are, there are three features that are available in Thunderbird assist.
[2328.62 --> 2331.90]  Uh, the first of which individual email summarization.
[2331.90 --> 2336.92]  And if you aim it at, at like a quoted thread, you could call it a thread summarizer.
[2337.24 --> 2339.52]  Um, there's email reply generation.
[2339.84 --> 2342.10]  And then the third one is the daily brief.
[2342.10 --> 2347.64]  Now for the different, the, the different kinds of users fall into two camps.
[2347.96 --> 2355.08]  There are the, I would like, you know, the, this long thread from the Thunderbird mailing
[2355.08 --> 2355.48]  list.
[2355.48 --> 2358.46]  I need that summarized because wow, that is too long.
[2358.96 --> 2367.80]  Uh, the other kind of user is the one who gets way too many emails and it needs an executive
[2367.80 --> 2368.40]  assistant.
[2369.36 --> 2374.62]  And that was where, as I just mentioned, it's like, okay, so that, that feature is just not
[2374.62 --> 2376.98]  going to work very well given the approach that we've taken.
[2376.98 --> 2386.56]  Um, based on what some of the users have requested in response to using, um, Thunderbird assist,
[2386.60 --> 2392.56]  that's given us some ideas of like, well, what we should be focusing on is we need things
[2392.56 --> 2399.98]  like semantic search, um, or because it is a Thunderbird add-on and has access to more
[2399.98 --> 2400.64]  than email.
[2400.64 --> 2404.42]  Like it has access to your calendar account.
[2404.42 --> 2411.32]  That's in Thunderbird, Thunderbird also does task management and it even pulls in RSS feeds,
[2411.96 --> 2415.80]  which RSS it's coming back so strong.
[2415.90 --> 2416.56]  I love RSS.
[2416.92 --> 2424.10]  I think that this idea of like, okay, so if we could correlate between these different
[2424.10 --> 2430.58]  pools of information that could be extremely useful to, uh, some users, which brings us back
[2430.58 --> 2435.28]  to the whole, like, okay, well, you need, you need small dedicated models for, for each
[2435.28 --> 2437.64]  kind of data because they're going to be formatted very differently.
[2438.44 --> 2445.44]  Well, Chris, I, I have sort of two, uh, well, uh, an observation and then maybe a clarification.
[2446.06 --> 2455.02]  So number one, I, I love how you described this, this progression from kind of the one tool
[2455.02 --> 2461.02]  to accomplish every task, which is often how people do think about using these models down
[2461.02 --> 2466.46]  to splitting this out into maybe it could be different models.
[2466.46 --> 2471.00]  It could just be different applications of the same model, but that are segmented or these
[2471.00 --> 2471.56]  sorts of things.
[2471.56 --> 2475.02]  This is so often what I recommend to people.
[2475.02 --> 2479.92]  It's kind of like when you have a junior developer and they come to you and they're like, I wrote
[2479.92 --> 2480.66]  all the functionality.
[2480.66 --> 2482.82]  It's all in this one function, right?
[2483.00 --> 2484.22]  Thousands of lines of code.
[2484.44 --> 2487.24]  And, and you're like, okay, we, we need to split this up, right?
[2487.32 --> 2493.38]  It's sort of in this AI world, there's that need for that splitting, splitting up.
[2493.46 --> 2497.50]  And of course it makes things more testable and all of that as well.
[2497.62 --> 2499.20]  But so thanks for highlighting that.
[2499.26 --> 2501.82]  I think that's a really, really practical and good point.
[2502.22 --> 2507.48]  Um, I think, uh, the, the clarification just want to make sure that people picked up on,
[2507.48 --> 2511.80]  you, you kind of referenced some of this work with flower and we talked about that remote
[2511.80 --> 2512.30]  inference.
[2512.30 --> 2518.76]  If I'm understanding, right, because you're running a local application, the data that
[2518.76 --> 2523.60]  flows to that remote inference is encrypted on the device.
[2523.60 --> 2525.54]  So it's encrypted in transit.
[2525.54 --> 2531.38]  And then if I'm understanding flowers implementation, you can correct me if I'm wrong, that would only
[2531.38 --> 2538.38]  be decrypted sort of in a confidential enclave in the inference infrastructure.
[2538.70 --> 2538.80]  Right.
[2538.88 --> 2543.06]  So that's when you say like, even flower, even if this is running in their infrastructure,
[2543.06 --> 2545.38]  they would not be able to tell you what a prompt is.
[2545.52 --> 2548.84]  Did I pick up on that somewhat in the right vein?
[2549.54 --> 2549.94]  Absolutely.
[2550.22 --> 2551.86]  That is, uh, that is totally correct.
[2552.02 --> 2559.62]  It is, uh, for any web developers or, or, you know, anybody who has had to write software
[2559.62 --> 2564.64]  that interacts with an API, you're probably communicating over something called HTTPS,
[2564.98 --> 2569.10]  which is sort of like, okay, that is, that is the baseline amount of encryption that we
[2569.10 --> 2569.38]  want.
[2569.44 --> 2575.46]  It's going to encrypt the traffic between your browser, the client, and then the server.
[2575.86 --> 2577.46]  Um, they take it a step further.
[2577.70 --> 2582.94]  There is, um, there's a, I would call it a three-part process for making sure that your,
[2583.02 --> 2584.68]  your data is protected.
[2584.86 --> 2588.42]  So first off, let's say you're logged in, right?
[2588.42 --> 2595.00]  You, you log into your, your Thunderbird account, which we created specifically for
[2595.00 --> 2598.50]  assist and some other services, which I will talk about a bit later.
[2598.92 --> 2605.14]  Then you are issued an API authentication token from flower itself, right?
[2605.18 --> 2606.04]  You're logged in.
[2606.18 --> 2608.12]  You're now going to talk to flower flowers.
[2608.30 --> 2610.48]  Like, yep, you, you logged in through Thunderbird.
[2610.68 --> 2610.88]  Cool.
[2611.58 --> 2613.58]  Here's your, uh, authentication token.
[2613.58 --> 2620.98]  And use this now to exchange public keys with yet another server.
[2620.98 --> 2627.22]  And that server does nothing besides run the, um, you know, run the language model.
[2627.22 --> 2635.14]  And at that point, as you, um, as you observed that any traffic between your client, between
[2635.14 --> 2642.54]  Thunderbird assist specifically, and then the machine running the model, like it's all encrypted
[2642.54 --> 2643.02]  in between.
[2643.18 --> 2650.08]  So you, you have, um, yeah, you're, you're double protected, I guess, HTTPS plus the, um,
[2650.08 --> 2653.98]  the public key encryption between you and the, the model server.
[2653.98 --> 2655.00]  That's great.
[2655.00 --> 2655.36]  Yeah.
[2655.60 --> 2662.10]  And I think this is a great way to maybe expand people's, um, thought process around
[2662.10 --> 2667.98]  what's possible with privacy and LLMs and how that can be split up between like where
[2667.98 --> 2671.76]  the LLM is running, whether that's local or not, or, or both.
[2671.98 --> 2675.56]  So yeah, appreciate, appreciate you going into a few of those details.
[2675.56 --> 2676.68]  I think it's really helpful.
[2676.68 --> 2683.56]  Um, as we, as we do get closer to the, to the end here, um, uh, I would love to maybe
[2683.56 --> 2690.18]  just, uh, kind of ask you to close us out by, by thinking about, you know, the future
[2690.18 --> 2694.50]  now that you've run these experiments, you've kind of gone through this process.
[2694.50 --> 2701.02]  I love how we kind of, uh, went through the, this kind of story of how this developed now,
[2701.02 --> 2706.38]  now that you've gone through that process, as you look towards the future, um, what,
[2706.46 --> 2712.44]  what excites you about where things are at now and where they're headed, um, in, in
[2712.44 --> 2717.36]  this project, or maybe in terms of like the wider ecosystem that you're now a part of using
[2717.36 --> 2723.08]  this tooling around, um, kind of remote confidential inference and that sort of thing.
[2723.08 --> 2728.94]  Yeah, there, there are a lot of exciting directions that we could take this work.
[2729.10 --> 2735.28]  Again, this was sort of an initial experiment, but we are, um, planning on shipping this with
[2735.28 --> 2740.26]  what we're calling Thunderbird Pro, which is a, a suite of services.
[2740.26 --> 2746.48]  Like my, my other web developer teammates, they're working on other things like, um, a scheduling
[2746.48 --> 2749.16]  application, a web-based scheduling application.
[2749.16 --> 2757.26]  There's, um, an end-to-end encrypted file sending application and there's Thundermail.
[2757.48 --> 2763.84]  I'm just going to say that again, Thundermail, um, which is our very own email service.
[2763.84 --> 2764.38]  Okay.
[2764.48 --> 2771.28]  So the, one of the things that, um, could be very interesting and perhaps even take advantage
[2771.28 --> 2772.74]  of federated learning.
[2772.74 --> 2773.52]  Thanks flower.
[2773.52 --> 2780.48]  Is if you could treat the server, the email server, or, you know, another machine that
[2780.48 --> 2785.84]  is co-located with the server, um, as another client, right.
[2785.84 --> 2787.90]  That has access to your encrypted email.
[2787.90 --> 2793.42]  That's on Thundermail that, you know, while you're, while you're asleep or while you were
[2793.42 --> 2798.74]  disconnected from the, from the internet, it could be creating embeddings or doing some
[2798.74 --> 2805.66]  other inference, um, based on your email data and then transmitting the, um, the learnings
[2805.66 --> 2807.12]  to your local machine.
[2807.12 --> 2813.38]  So that, uh, imagine if you could do semantic search without having to generate the embeddings
[2813.38 --> 2818.78]  on your laptop and you can do it in an offline way, because as far as you're concerned, the
[2818.78 --> 2823.64]  embeddings are effectively pre-generated and downloaded along with the messages themselves.
[2823.64 --> 2828.48]  The trick there of course is doing it in a, in a way that will satisfy, you know, the
[2828.48 --> 2831.60]  most staunch privacy advocates are like, wait a minute.
[2831.60 --> 2836.90]  If you have a server that's in your infrastructure and has access to my email, then it's really
[2836.90 --> 2837.82]  not end to end.
[2837.82 --> 2838.70]  It's not encrypted.
[2838.70 --> 2843.72]  Um, so we need to figure out a good solution to that before we can explore that.
[2843.72 --> 2850.58]  But some, some other things that I alluded to earlier involve expanding, that's such an
[2850.58 --> 2854.32]  overloaded word, expanding the context that the model has access to.
[2854.52 --> 2857.64]  And I don't mean like, you know, context window.
[2857.74 --> 2864.82]  I mean like, okay, so, um, giving it access to your calendar, to, uh, your to-dos, your RSS
[2864.82 --> 2865.32]  feed.
[2865.68 --> 2872.86]  Um, what if we added a notes application to Thunderbird and then effectively turning, making it possible
[2872.86 --> 2879.58]  so that Thunderbird could be used as an LLM assisted personal knowledge management and
[2879.58 --> 2885.34]  communication tool that whatever future that looks like, that's, that's more exciting to
[2885.34 --> 2886.26]  me personally.
[2886.26 --> 2893.80]  Um, one of those people who like, I have notes from the last handful of like a last couple
[2893.80 --> 2899.00]  of decades, um, that I still keep around and I would love some, an LLM to help me sift
[2899.00 --> 2899.50]  through that.
[2899.50 --> 2906.12]  It would be even more interesting that as I'm making a note, it could suggest related
[2906.12 --> 2911.40]  documents and ideas that I've had in the past, or just, I mean, for a lot of users, just helping
[2911.40 --> 2912.52]  them stay organized.
[2912.52 --> 2918.84]  Because again, there's, there's so much for one tiny human brain to keep track of, and
[2918.84 --> 2920.14]  there's just so much information.
[2920.14 --> 2929.88]  So I think that for me as not as, you know, uh, an ML researcher or an AI expert, I'm just
[2929.88 --> 2931.10]  an application developer.
[2931.36 --> 2932.70]  I want to work on that.
[2932.76 --> 2938.04]  I want to build that and make it possible for people to, um, have more control over their
[2938.04 --> 2943.84]  information, help them retain their privacy, but, you know, make those creative connections
[2943.84 --> 2946.02]  that only they as a human can do.
[2946.58 --> 2956.02]  But an LLM local or, you know, uh, confidential remote compute assisted reminding you of like,
[2956.06 --> 2957.02]  Oh, you wrote this.
[2957.02 --> 2960.52]  Here are some things that you've written about that are related to that.
[2960.58 --> 2963.24]  Or here's some conversations you had in email or in chat.
[2963.24 --> 2971.28]  Um, and then for you, the user as a, just a regular squishy brain human, you're like, Oh,
[2971.68 --> 2976.90]  I just had this weird random flash of insight based on this constellation of information that
[2976.90 --> 2979.82]  I generated over years.
[2980.04 --> 2983.12]  I think I liked that future of AI.
[2983.26 --> 2991.02]  And also as an application developer, I think that I really want LLMs to be more deterministic.
[2991.02 --> 2997.14]  Like, it's so weird to call an API with the same data and get very different results.
[2997.90 --> 3004.58]  And I, we can get into this or not, but I definitely feel like chat is the wrong interface
[3004.58 --> 3006.02]  for a lot of tasks.
[3006.28 --> 3006.50]  Yes.
[3006.68 --> 3007.26]  Thank you.
[3007.68 --> 3008.24]  Okay, cool.
[3009.52 --> 3011.42]  Just want to make sure I'm in good company.
[3011.78 --> 3018.14]  So I've got, I don't know, again, in my little mad science notebook, I've got ideas around like,
[3018.14 --> 3022.76]  okay, how do you, uh, how do you swap in deterministic functions?
[3023.26 --> 3025.38]  Um, how do you coordinate the efforts?
[3025.52 --> 3031.82]  And I think something beyond, I mean, maybe I'm describing a more strict version of MCP,
[3031.94 --> 3039.72]  but the fact that your input and your output currently is plain language is it's a double
[3039.72 --> 3046.34]  edged sword because the only way to determine if you've got a bad result is for you as a human
[3046.34 --> 3047.74]  to evaluate it.
[3048.12 --> 3052.90]  Unless you spin up another language model to verify the first result.
[3053.52 --> 3057.34]  But as a programmer, that feels a lot to me like, oh, I just wrote a function.
[3057.74 --> 3062.62]  And the only way to know that if my function call was correct is to write another function
[3062.62 --> 3063.28]  to check it.
[3063.86 --> 3066.06]  And it just feels like, it just feels wrong.
[3066.06 --> 3074.76]  So I, I really, um, yeah, I, I want, um, I want discreet inputs and outputs.
[3075.06 --> 3080.74]  I want language models that are small and dedicated to specific tasks.
[3080.74 --> 3087.40]  And then I, I want, um, reusable, shareable ways of wiring them together.
[3087.40 --> 3093.56]  I want to create essentially like workflows of information processing within, within Thunderbird.
[3093.56 --> 3095.40]  So that's, that's me.
[3095.48 --> 3099.54]  I'm, I'm the, uh, personal knowledge management cheerleader at, uh, at Thunderbird.
[3099.62 --> 3100.32]  That's my new title.
[3101.04 --> 3102.04]  That's awesome.
[3102.20 --> 3108.22]  Well, I, the, the, that future is a, uh, is one that I could get on board with for sure.
[3108.32 --> 3113.54]  After, after struggling with a lot of the things that you mentioned as well, and, and also hoping
[3113.54 --> 3115.28]  for, for many of those things.
[3115.28 --> 3120.42]  So yeah, thank you so much for sharing this journey and this experimentation that you've been
[3120.42 --> 3123.58]  on with Thunderbird and please keep up the good work.
[3123.72 --> 3129.56]  Give our thanks to the, to the team for inspiring us with, uh, with a lot of amazing work and thanks
[3129.56 --> 3132.10]  for sharing your, your insights here with us.
[3132.18 --> 3133.56]  Uh, appreciate you taking time.
[3134.32 --> 3134.46]  Yeah.
[3134.52 --> 3136.86]  Thank you so much for having me.
[3137.06 --> 3139.76]  I'm really, really glad that we could make this happen.
[3140.20 --> 3140.60]  Us too.
[3140.84 --> 3141.50]  We'll see you soon.
[3141.88 --> 3142.32]  All right.
[3142.32 --> 3142.96]  Thanks.
[3150.42 --> 3150.90]  All right.
[3151.08 --> 3152.48]  That's our show for this week.
[3152.86 --> 3157.84]  If you haven't checked out our website, head to practical AI.fm and be sure to connect with
[3157.84 --> 3159.82]  us on LinkedIn X or blue sky.
[3159.98 --> 3164.36]  You'll see us posting insights related to the latest AI developments, and we would love
[3164.36 --> 3165.76]  for you to join the conversation.
[3166.02 --> 3170.02]  Thanks to our partner prediction guard for providing operational support for the show.
[3170.34 --> 3172.34]  Check them out at prediction guard.com.
[3172.68 --> 3176.38]  Also thanks to break master cylinder for the beats and to you for listening.
[3176.62 --> 3179.56]  That's all for now, but you'll hear from us again next week.
[3180.42 --> 3181.42]  Bye.

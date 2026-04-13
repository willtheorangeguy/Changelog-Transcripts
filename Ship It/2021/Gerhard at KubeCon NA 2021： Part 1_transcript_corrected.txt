[0.16 → 5.90] I'm your host, Gerhard Lazy, and you're listening to Shi bit, a podcast about getting your best
[5.90 → 8.48] ideas into the world and seeing what happens.
[8.84 → 13.82] We talk about code, ops, infrastructure, and the people that make it happen.
[14.42 → 18.56] Yes, we focus on the people, because they drive everything else.
[19.10 → 23.74] This is my first set of interviews from Rubicon Cloud Native Con North America 2021.
[24.50 → 27.36] Thank you, Katie Minders, for our changelog invite.
[27.36 → 32.82] I spoke with William Morgan, and he shares with us some of the finer Linked details,
[33.36 → 39.30] such as the underlying security theme, why native Kubernetes objects instead of more CRDs,
[39.66 → 41.26] and meeting team members in person.
[41.82 → 49.04] Frederik Transit speaks about ARCA, a new continuous system profiling tool that uses EPF to help
[49.04 → 51.94] you understand what is happening on your hosts.
[51.94 → 58.16] Andrew Reinhardt gives us a great Talos OS and Lifespan perspective and shares some follow-up
[58.16 → 59.70] videos on these topics.
[60.18 → 64.92] The last conversation was with David Flanagan, you know him as Raw Code, about new beginnings.
[65.44 → 71.02] It's only been less than two months since we've had him in episode 18, and he kept really busy.
[71.48 → 77.08] Caleb, his three weeks old baby boy, was the youngest attendee at this conference, and some
[77.08 → 79.64] talks made him sleepy, so good job everyone.
[80.00 → 83.68] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[84.04 → 85.94] Thank you for the great bandwidth, Vastly.
[86.12 → 91.68] You can learn more at Fastly.com, ship new features with confidence by getting your feature
[91.68 → 98.10] flags powered by LaunchDarkly.com, and thank you Linde for keeping our Kubernetes fast and
[98.10 → 98.46] simple.
[98.46 → 104.72] You too can run our infrastructure as we do via lino.com forward slash changelog.
[110.92 → 111.80] What's up shippers?
[111.94 → 115.36] This episode is brought to you by our friends at Fly.
[115.72 → 119.74] Fly lets you deploy your apps and databases close to your users in minutes.
[120.00 → 127.50] You can run your Ruby, Go, Node, Dino, Python, or Elixir app and databases all over the world.
[127.50 → 128.58] No ops required.
[129.02 → 131.48] Fly's vision is that all apps should run close to their users.
[131.94 → 136.12] They have generous free tiers for most services, so you can easily prove to yourself and your
[136.12 → 139.72] team that the Fly platform has everything you need to run your app globally.
[140.14 → 144.78] Learn more at fly.io slash changelog, and check out the speed run and their excellent docs.
[145.20 → 148.52] Again, fly.io slash changelog, or check the show notes for links.
[151.72 → 155.62] We are going to ship in three, two, one.
[157.50 → 174.36] One of my favourite talks from Rubicon in May, the European one, was overview and state of
[174.36 → 174.68] Linked.
[174.68 → 177.04] And you, Will, did a fabulous job.
[177.36 → 182.38] But I have to say, between you and Mate, I'm not sure who was the better one, because it
[182.38 → 183.62] was a great, great talk.
[184.02 → 185.36] No, seriously, how is Mate doing?
[185.66 → 186.46] He's doing great.
[186.74 → 189.04] He's doing really fantastic.
[189.56 → 193.26] You know, he's kind of a rising star in the CNCF.
[193.34 → 198.90] He was a community bridge participant, you know, as a student just, I think, a year ago,
[198.90 → 203.30] and then has already risen to the levels of Linked maintainer.
[203.50 → 204.76] So yeah, he's really fantastic.
[205.24 → 206.08] I really love that story.
[206.16 → 209.52] Like him shipping code, going from nothing to shipping code for Linked.
[209.74 → 210.84] That was amazing to see.
[211.06 → 214.82] And the enthusiasm and the fresh perspective, all that's been great.
[215.22 → 220.24] So in May, we heard many good things, many great things about Linked 2.10.
[220.50 → 222.40] I know that Linked 2.11 is out.
[222.54 → 223.98] So what is new in the new version?
[223.98 → 225.72] Yeah, yeah, great question.
[225.84 → 229.64] So 2.11 is actually, 2.10 was a big step, but 2.11 is even bigger.
[230.10 → 234.98] This is the first time when we have introduced policy into Linked, which means that you can
[234.98 → 240.56] now control which services are allowed to connect and to communicate with each other.
[240.84 → 245.82] So prior to 2.11, you know, whenever you've told Linked, hey, I'm service A, and I want
[245.82 → 249.36] to talk to service B, Linked has done its best to make that happen, right?
[249.40 → 251.78] It'll do retries if there's a transient failure.
[252.10 → 253.10] It'll do load balancing.
[253.10 → 254.12] It'll do all this stuff.
[254.72 → 258.36] And now with 2.11, for the first time, you can say, no, A is not allowed to talk to B
[258.36 → 260.36] unless these conditions are met.
[260.80 → 265.32] So that's a big, you know, for anyone who's in the security world, this is the idea of
[265.32 → 268.68] micro segmentation, you know, and this sort of thing becomes very important.
[268.96 → 269.74] How do you declare that?
[269.84 → 270.70] Do you have a UI?
[270.88 → 271.72] Do you have a configuration?
[271.96 → 272.58] How does that work?
[272.84 → 278.82] Yeah, so we, a lot of our design principles in Linked are to allow you to do powerful things
[278.82 → 280.88] with as little configuration as possible.
[280.88 → 285.88] And the way we do that typically is by sticking as close as we can to Kubernetes primitives.
[285.88 → 289.98] So, you know, rather than inventing some new version of the service, well, we just use
[289.98 → 294.68] regular Kubernetes services rather than inventing abstraction layer on top of these other things.
[294.80 → 297.46] Well, we just give you, give you those Kubernetes objects directly.
[297.46 → 304.68] So we've tried to avoid introducing CRDs, you know, and I think prior to 2.11, we had two CRDs, I think,
[304.78 → 308.78] in total from, you know, two years of development or three or five years of development,
[308.90 → 309.72] however you want to count it.
[310.08 → 312.44] But with 2.11, we introduced two new CRDs.
[312.68 → 317.82] So the way that it works is you express policy by using a set of annotations that you can set
[317.82 → 321.74] at the cluster level, at the namespace level, at the workload level.
[321.74 → 328.18] Or in addition to that, you can add these CRDs that basically specify the types of traffic
[328.18 → 329.44] that are allowed to happen.
[329.84 → 335.42] And that combination together is really elegant because it means you can express a wide variety
[335.42 → 340.24] of things from like either a very open cluster that only has like certain exceptions, like
[340.24 → 344.66] this sensitive service, you can only talk to it under these conditions, all the way to
[344.66 → 346.38] everything's locked down.
[346.38 → 350.92] And the only traffic that can happen is traffic that I've explicitly allowed to happen and
[350.92 → 352.06] everything kind of in between.
[352.58 → 352.68] Yeah.
[352.84 → 353.08] Okay.
[353.70 → 357.30] So that makes perfect sense, especially from the Kubernetes primitive side.
[357.38 → 358.82] I really like how you're thinking about that.
[359.08 → 362.90] But one thing which I really loved about Linked was the visual elements, right?
[362.94 → 366.46] The dashboards, the graphs, all that stuff.
[366.54 → 367.46] That was amazing.
[367.90 → 372.02] So I'm wondering from that perspective, do you also allow some customization via the UI,
[372.02 → 376.74] which then gets translated to those native Kubernetes primitives?
[377.08 → 377.32] Yeah.
[377.38 → 381.64] So one thing we've never done and probably never will is allowed you to create those objects
[381.64 → 382.22] through the UI.
[382.36 → 387.20] So we've always wanted the UI to be a read-only tool that allows you to understand the state
[387.20 → 387.78] of the system.
[388.02 → 392.56] But once you get into like, you know, you're dragging a slider, or you're like, you know,
[392.90 → 396.40] pressing buttons to implement YAML, it just, it gets very hairy very quickly.
[396.52 → 399.78] And then the security concerns and permissions and all that stuff.
[399.78 → 402.70] So we've kept the UI totally read-only.
[403.14 → 403.96] That sounds great to me.
[404.08 → 405.54] That is a very wise decision.
[405.68 → 409.70] And I'm sure we'll come back to this later another time, not today, but that sounds great.
[410.24 → 413.14] So which is your Linked top of your mind item?
[413.24 → 416.82] And this can be something that you will be working on or something that's, you know,
[416.82 → 421.16] it's like a hard problem that you've been working for some time or something that you're
[421.16 → 425.74] excited about Linked, which is outside this release or outside the features,
[426.04 → 427.10] which is your top of your mind?
[427.10 → 427.66] Yeah.
[427.80 → 430.94] So for me, it's kind of a, I think it's a theme more than anything else.
[431.18 → 435.08] And it's a theme that we didn't really expect when we were first starting to develop Linked,
[435.18 → 440.68] but it's one around security around, especially, you know, security of the traffic in your
[440.68 → 441.04] cluster.
[441.44 → 446.70] So we came into Linked, you know, in the early days of the project, very reliability focused.
[447.02 → 451.26] You know, our background was at Twitter and Twitter was constantly down, at least at the
[451.26 → 451.68] time.
[451.68 → 455.52] And so, you know, kind of our vision for what we were doing was what we're going to
[455.52 → 455.68] do.
[455.96 → 459.88] We're going to have load balancing and retries and blue-green deploys and like all these,
[459.96 → 461.70] you know, reliability techniques.
[461.96 → 466.62] And what we learned early on was that a lot of the use, I mean, some people love that stuff,
[466.82 → 469.36] but a lot of the use of Linked was from mutual TLS.
[470.04 → 470.44] Why?
[470.58 → 473.50] Because people wanted to encrypt the traffic in transit.
[473.66 → 473.94] Why?
[474.14 → 477.88] Because either, you know, they have these regulatory concerns, right?
[477.88 → 481.86] Oh, well, we work with financial data and like, you know, the government basically says we
[481.86 → 485.22] have to do this or, you know, they just have security concerns.
[485.30 → 486.10] We're running in the cloud.
[486.22 → 488.60] We don't have any control over the network, you know, best practices.
[488.86 → 490.60] We should maintain confidentiality.
[490.90 → 493.26] So that was like our foray into the world of security.
[493.26 → 497.98] And that theme has continued to develop, you know, through the policy features, you know,
[498.02 → 501.86] in micro segmentation and onto other features, more types of policies.
[501.86 → 509.02] You know, there's a lot more we can do in this area of how do you secure the traffic in your
[509.02 → 509.28] cluster?
[509.38 → 513.38] And it's a blossoming area because everyone, I think, is becoming a little more comfortable
[513.38 → 514.04] with Kubernetes.
[514.20 → 518.82] So the operational concerns are, you know, I wouldn't say they're taken care of, but like
[518.82 → 519.38] they're understood.
[519.82 → 523.40] And now they're in the world of, well, crap, now how do I, you know, I can run it, but how
[523.40 → 524.48] do I secure it?
[524.52 → 530.00] How do I make sure that, you know, if one node gets hacked, that like everything doesn't
[530.00 → 535.16] fall apart or, you know, more likely if someone deploys a mistake, you know, it can't accidentally
[535.16 → 541.24] delete our user or expose, you know, production, you know, expose sensitive information to the
[541.24 → 541.72] outside world.
[542.10 → 546.42] So that theme has been just developing for us over the past couple of releases.
[546.42 → 551.04] And it's gratifying, not just because things like that are cool, but because people are
[551.04 → 554.18] using it, and they're getting a lot of value out of it, which, you know, it's kind of like
[554.18 → 555.70] the end goal of Linked.
[555.82 → 559.86] If no one's using it, then it's a little, I don't know, to me, that's a little unsatisfying.
[560.00 → 560.08] Yeah.
[560.48 → 565.30] I know that that is very big, complicated, meaty problem to tackle, which you're not
[565.30 → 568.32] going to solve in a patch release, maybe not even in the major release.
[568.38 → 570.64] It'll take many, many cycles to get it right.
[571.18 → 574.50] And it's changing as well with all the new rules and regulations.
[575.02 → 579.24] I know that this is something which you are passionate about because I've seen your blog
[579.24 → 579.58] post.
[579.68 → 582.20] I've only skimmed it, the one about MTLS and Kubernetes.
[582.54 → 583.94] I intend to go back and read it properly.
[584.02 → 584.66] That's a good one.
[584.86 → 585.90] So thank you for that.
[585.96 → 586.92] There is a lot there.
[586.92 → 595.80] My top of mind is, can Linked 2.11 still do Linked install pipe subject apply-f?
[595.96 → 597.04] Because that was amazing.
[597.26 → 599.76] Like you can install Linked in your Kubernetes with Linked.
[599.90 → 601.76] That just blew my mind when I first saw it.
[601.82 → 603.52] And I'm wondering, does it still work?
[603.76 → 603.94] Yep.
[604.16 → 604.40] Yep.
[604.54 → 605.42] So that still works.
[605.62 → 606.36] We've maintained that.
[606.72 → 611.62] That's not typically the production deployment, you know, because people are moving into repeatable
[611.62 → 615.56] deployments and the Helm charts and code is config and so on.
[615.70 → 616.32] Config is code.
[616.94 → 618.18] But yes, that still works.
[618.66 → 622.16] And I think that's still really important because a lot of people, believe it or not,
[622.28 → 625.98] you know, Linked has been around for six years at this point or something.
[626.14 → 628.62] You know, it was the first service mesh project ever.
[628.62 → 634.48] But people are still coming into it fresh-faced, like never heard of a service mesh before.
[634.58 → 635.64] I'm trying to understand this thing.
[635.72 → 637.64] I've just learned Kubernetes, you know.
[637.68 → 642.88] So there is a big audience to Linked every day when you're not ready to like helmet up.
[642.96 → 645.32] Like you're just trying to play around with this thing and understand it.
[645.52 → 646.50] So yeah, that still works.
[646.86 → 649.20] How would you recommend someone that installs Linked in production?
[649.38 → 654.10] So this is a very nice getting started, which I find very valuable, especially when I'm trying
[654.10 → 657.22] things I love when tools are really easy to use.
[657.52 → 661.50] And this is, in my perspective, one of the ways in which Linked is super easy to get
[661.50 → 662.12] started with.
[662.32 → 665.02] But how would you recommend that someone installs Linked in production?
[665.20 → 670.74] Yeah, so what we've seen basically is people using Helm or Terraform or like tools that
[670.74 → 673.90] allow you to do it in a programmatic and repeatable way.
[674.18 → 676.22] And I think that's probably the best practice for production.
[676.70 → 681.34] You want to be able to, especially if you're in the world of spinning out multiple clusters
[681.34 → 686.76] or starting to treat your clusters as cattle and not as pets, you want this deploys to
[686.76 → 687.46] be repeatable.
[687.68 → 691.50] And you want to know exactly how things were set up when you come back to it three years
[691.50 → 692.68] later, you know.
[692.72 → 697.70] So you don't want it to be in someone's terminal window that they like, they closed their laptop
[697.70 → 699.34] three years ago, and then they left the company.
[699.50 → 701.22] And now you're like, hmm, I wonder how this was involved.
[701.50 → 702.66] So that's the best practice.
[702.92 → 703.08] Okay.
[703.40 → 708.20] One of the things which I've seen on there quite liked, especially when it comes to some projects
[708.20 → 712.44] which can be a bit more involved to set up, is there's an operator which is just meant
[712.44 → 717.48] to install things, and then you apply a thing and the operator knows how to install itself.
[717.80 → 723.10] Because then the thinking goes, the operator can also automate upgrades, which I think is
[723.10 → 723.96] an interesting proposition.
[724.32 → 724.38] Yeah.
[724.52 → 729.04] So does Linked have something like that or is Linked thinking about something like that?
[729.12 → 732.96] It's certainly something we've discussed in the past and I don't think there's a reason
[732.96 → 734.08] why we wouldn't do it.
[734.08 → 737.90] You know, the easing upgrades especially is something I'd love to do.
[738.20 → 742.68] The upgrade to 2.11 is actually pretty easy, but going from 2.9 to 2.10 was painful.
[742.90 → 745.26] Some of the configs changed and stuff like that.
[745.62 → 749.46] I don't know that that would have been 100% automatable, but it would have been something
[749.46 → 751.04] we could assist at least.
[751.36 → 754.84] And there are other operations too, you know, that I think an operator would be helpful
[754.84 → 755.06] with.
[755.36 → 756.34] So yeah, we're open to it.
[756.80 → 757.94] PR is welcome.
[758.36 → 758.56] Nice.
[758.72 → 759.30] Very smooth.
[759.48 → 760.08] Very smooth.
[760.08 → 760.40] Okay.
[760.88 → 766.20] So the upgrade from 2.10 to 2.11, does it just apply the Helm upgrade?
[766.60 → 767.38] Is that all it takes?
[767.60 → 768.72] That really should be it.
[768.94 → 769.76] We didn't change.
[769.82 → 774.54] There's one or two breaking changes around the mechanics of some of the multi-cluster stuff.
[774.96 → 778.42] But yeah, the majority of 2.11 is really additive.
[779.06 → 784.06] And, you know, which again is a theme that we, you know, that we try and stick to with Linked.
[784.06 → 789.34] So all the policy stuff, you know, which was a new feature, that's all built on top
[789.34 → 791.48] of all the MTLS stuff, right?
[791.56 → 795.66] And all that MTLS stuff is built on top of the Kubernetes primitives of service accounts
[795.66 → 798.52] and mutating, you know, webhooks and whatever else.
[798.62 → 799.88] It just kind of compounds.
[800.16 → 804.16] And you get these very nice situations where, well, the moment you install Linked, I mean,
[804.20 → 805.68] it's awesome that you can install it really quickly.
[805.80 → 810.04] But what's even more awesome to me is that when you install it and you mesh your pods, you
[810.04 → 813.24] actually have MTLS working out of the box there without doing any config.
[813.24 → 817.38] Like, if you read that long, long MTLS guide that, you know, that you talked about, you
[817.38 → 821.02] know, the vast majority of its stuff, you know, like it's complicated stuff.
[821.10 → 824.14] And then at the end, I'm like, but you don't have to do any of that because you can just
[824.14 → 825.30] install Linked, and it does all this stuff.
[825.60 → 830.08] And that means that all the policy stuff can then be built on top of the identities that
[830.08 → 831.04] MTLS provides.
[831.08 → 835.56] So the cryptographically secured identities and, you know, it's all done in this zero trust
[835.56 → 839.06] fashion where the enforcement point is at the pod granularity.
[839.14 → 841.18] It's not at the firewall or the edge of the cluster.
[841.48 → 843.10] So all this nice stuff happens.
[843.24 → 843.48] Okay.
[843.84 → 848.54] Do you have any dependency on something like cert manager or maybe a specific Kubernetes
[848.54 → 849.08] version?
[849.48 → 850.22] What does that look like?
[850.38 → 855.30] So for Kubernetes versions, we basically try and, you know, support the most recent three
[855.30 → 856.64] Kubernetes versions.
[857.10 → 862.74] And, you know, often we'll have support for earlier ones, but it's not really the policy
[862.74 → 864.34] is like, okay, most recent three.
[864.72 → 869.10] Now, if you really have to, you know, do something with an older release, maybe we can make that
[869.10 → 869.28] work.
[869.50 → 874.32] In terms of dependencies on cert manager, there's not an explicit dependency, but one thing
[874.32 → 880.56] you do have to figure out when you're running Linked is the certificate rotation, not of
[880.56 → 884.10] the pods themselves, but of the cluster level issuer certificate.
[884.10 → 889.08] We have some docs that have that automated with cert manager, or you can just remember to
[889.08 → 889.36] do it.
[889.52 → 893.64] But by default, you know, if you run that Linked install command, that generates a certificate
[893.64 → 894.70] that's only valid for a year.
[894.88 → 898.42] So you have a year then to figure out, okay, here's how I'm going to rotate it.
[898.74 → 898.86] Right.
[898.86 → 899.58] That's a good one.
[899.64 → 899.74] Yeah.
[899.74 → 901.32] That actually catches quite a few people.
[901.54 → 902.42] They don't think about that.
[902.86 → 902.96] Yeah.
[902.96 → 905.98] But maybe if you upgrade, does it get rotated part of the upgrade?
[906.06 → 907.08] Because that would solve the problem.
[907.50 → 907.94] No, it doesn't.
[908.06 → 910.88] No, it doesn't because I don't believe it does.
[911.28 → 911.94] Actually, I'm not sure.
[912.28 → 912.42] Yeah.
[912.54 → 912.74] Okay.
[913.30 → 917.02] But in addition to the issuer certificate, there's also the trust certificate or the trust route,
[917.02 → 919.48] which definitely doesn't get rotated as part of an upgrade.
[919.62 → 919.78] Yeah.
[920.10 → 921.62] And that also has a one-year expiration.
[921.74 → 924.92] So, you know, it is easy to install, and it's easy to make things work.
[924.92 → 929.76] But like with any sophisticated piece of technology, as you push it into production,
[929.96 → 932.10] there's stuff that you need to be aware of.
[932.28 → 937.52] We actually wrote a run book, a production run book for Linked on buoyant.io.
[937.68 → 942.44] So if you want our advice as, you know, the company that has installed Linked and helped
[942.44 → 946.38] people operate Linked in a lot of different places, and in fact, we operate it ourselves.
[947.10 → 950.36] If you want our best advice for how to install it, you can read through the run book, and we talk
[950.36 → 953.40] about certificate rotation and some other things you want to be aware of.
[953.58 → 954.08] That's a good one.
[954.08 → 954.32] Okay.
[954.34 → 955.08] I didn't know about that.
[955.14 → 955.44] Thank you.
[955.54 → 957.22] That's a great, great tip.
[957.48 → 961.14] You got to make sure like you don't have clock skew between the nodes because, you know,
[961.18 → 962.60] all these TLS certificates.
[963.08 → 963.54] Oh, yes.
[963.56 → 964.80] You don't have time components.
[964.80 → 967.48] And if you've got big clock skew, then like things are not going to be able to connect
[967.48 → 967.98] even though they should.
[968.22 → 968.72] There are details.
[968.82 → 970.16] It turns out computers are complicated.
[970.62 → 972.74] As much as we try and simplify them, there are details.
[973.02 → 977.16] So I'm wondering, what are you looking forward to the most when it comes to Rubicon,
[977.28 → 978.78] this Rubicon, which is?
[979.04 → 980.40] Oh, for me, that's easy.
[980.48 → 982.14] And it's actually not really project.
[982.14 → 984.06] Well, it's kind of semi-project related.
[984.48 → 987.84] It's just being there in person with other human beings.
[988.44 → 989.90] Like for me, that's so gratifying.
[990.50 → 994.66] You know, I think open source can be a little isolating because a lot of your interactions
[994.66 → 999.92] with people are, they come into the, you know, in our case, the Slack channel, and they're
[999.92 → 1000.88] like, hey, I have this problem.
[1001.22 → 1002.80] And then you like to help them fix it.
[1003.02 → 1003.60] And they're like, thanks.
[1003.60 → 1004.18] And then they leave.
[1004.56 → 1006.88] And then the next person comes and presents you with another problem.
[1006.98 → 1009.84] And like, you develop this kind of transactional relationship.
[1010.00 → 1014.32] And what you don't see in that, which you do see in person, what you don't see on Slack
[1014.32 → 1017.80] is, oh, people then go off, and they like deploy Linked, and they're really successful.
[1018.14 → 1021.64] And their company is, you know, thankful and like everything's working well.
[1021.86 → 1024.14] They don't come back to the Slack to say, well, sometimes they do.
[1024.14 → 1025.58] But usually they're like, okay, cool.
[1025.66 → 1026.94] Now I can do the rest of my job.
[1027.54 → 1030.52] But in person, you know, when you talk to these people, you realize there actually are
[1030.52 → 1032.40] a ton of people who are running Linked.
[1032.88 → 1034.88] They're, you know, it's solving big problems for them.
[1034.96 → 1037.56] And now they have an opportunity to come up and tell you about that.
[1037.92 → 1040.44] So that aspect has always been really amazing for me.
[1040.54 → 1045.70] And the virtual conferences, you know, as much as I like the convenience of not having
[1045.70 → 1048.42] to hop on an airplane, they don't quite have that same thing.
[1048.54 → 1050.62] So that's the long answer to a short question.
[1051.00 → 1052.90] I'm looking forward to the human interaction.
[1052.90 → 1053.76] Oh, yes.
[1053.96 → 1054.52] Don't we all.
[1054.82 → 1055.32] Don't we all.
[1055.72 → 1055.88] Yeah.
[1056.10 → 1057.74] I wish there wasn't a screen today.
[1059.00 → 1059.60] About Linked.
[1059.72 → 1059.82] Yeah.
[1060.12 → 1060.52] Human.
[1060.68 → 1062.70] Another human that's not part of my family.
[1062.84 → 1063.48] Isn't that nice?
[1064.24 → 1065.76] They're sick of hearing about it, right?
[1065.98 → 1066.20] Yeah.
[1067.12 → 1067.44] Right.
[1067.60 → 1067.94] Okay.
[1068.08 → 1075.76] So if someone's listening to this, and you are using Linked, and especially if it works
[1075.76 → 1080.46] and you don't think you need to get back to William and the Bryan team and the Linked
[1080.46 → 1082.10] community, that's actually wrong.
[1082.10 → 1084.72] Like, go and show a sign of gratitude.
[1084.88 → 1085.54] Say, hey, thank you.
[1085.56 → 1086.12] This is great.
[1086.28 → 1087.06] Share your use case.
[1087.24 → 1088.60] Share what you like about it.
[1088.90 → 1092.76] Even if everything is perfect, sharing that is worth it.
[1092.92 → 1094.28] People will appreciate it.
[1094.34 → 1095.24] And you've heard it from William.
[1095.44 → 1097.48] So do as William says.
[1097.74 → 1098.66] That's what I say.
[1098.92 → 1099.10] Yeah.
[1099.30 → 1100.48] At a minimum, swing by.
[1100.64 → 1102.32] If you're at Rubicon, swing by and see.
[1102.32 → 1102.50] Yeah.
[1102.88 → 1103.46] That as well.
[1103.54 → 1104.00] That as well.
[1104.08 → 1104.18] Yeah.
[1104.22 → 1105.70] I wish I could swing by, but I can't.
[1105.78 → 1106.14] Next one.
[1106.20 → 1106.48] Next one.
[1106.48 → 1109.40] If you come to Europe, because that's what the next one will be.
[1109.98 → 1115.60] So anyway, for the people that can't attend Rubicon, like myself, and they will be catching
[1115.60 → 1116.52] up on videos.
[1116.88 → 1118.38] Any advice that you have for those people?
[1118.60 → 1122.58] How can they make the most out of it, even though they can't be there in person?
[1122.58 → 1125.14] And some of them are just catching up on the videos.
[1125.14 → 1125.90] What can they do?
[1126.12 → 1126.38] Yeah.
[1126.60 → 1128.84] So, you know, I don't know if I have great advice.
[1128.96 → 1131.90] My relationship with virtual conferences is not a great one.
[1132.28 → 1134.96] It's just a different experience.
[1135.04 → 1135.32] I don't know.
[1135.44 → 1140.26] I think like many of us, I sit in front of a screen all day and, you know, it's really
[1140.26 → 1143.36] hard to want to keep doing that in any other form.
[1143.44 → 1147.86] But I will say we have a buoyant virtual booth, and we've tried to make that as fun and as
[1147.86 → 1148.86] interesting as possible.
[1149.00 → 1152.70] I'll be hanging out there, you know, even though I'm in person at the event, I'll also be spending
[1152.70 → 1153.82] time on the virtual booth.
[1153.82 → 1157.42] We've got the run book and like a bunch of other Linked stuff.
[1157.52 → 1161.44] We've got an opportunity for you to get, I think we're raffling off Linked swag.
[1161.62 → 1165.22] So if you visit us, you know, you've got a chance, and we'll actually ship you a hat and
[1165.22 → 1166.62] some shirts and stuff.
[1167.14 → 1170.62] So I don't know about the rest of the conference, but I think the Linked booth at least will
[1170.62 → 1171.06] be interesting.
[1171.30 → 1171.46] Okay.
[1171.78 → 1173.40] Did you have time to check the talk schedule?
[1173.58 → 1174.36] Anything interesting?
[1174.74 → 1176.14] Any talks that you're looking forward to?
[1176.30 → 1179.28] Well, now I'm going to seem like a bad person because I only look at the Linked talks.
[1179.98 → 1180.56] That's okay.
[1180.74 → 1181.28] That's fine.
[1181.36 → 1182.14] That's perfectly fine.
[1182.54 → 1182.90] Yeah.
[1182.90 → 1183.96] We have one.
[1183.98 → 1185.08] My kids are also the best.
[1185.20 → 1185.74] You know what I mean?
[1186.50 → 1190.64] So there are two talks at Rubicon that I am particularly excited about.
[1190.96 → 1195.08] Actually, one of them is going to be at Service Mesh Con, which is a day zero event, which I
[1195.08 → 1197.76] have mixed feelings about as a conference.
[1197.76 → 1202.74] But there is a really cool talk there from the folks at Elko, which is the largest retailer
[1202.74 → 1207.48] in the Nordics about how, you know, and it's like a multi-billion dollar business that everyone,
[1207.94 → 1212.12] you know, in that region knows about, about how they use Linked and Kubernetes to like
[1212.12 → 1214.04] deplatform their entire company.
[1214.26 → 1215.14] So that one's really cool.
[1215.26 → 1219.96] That's Frederick, who is also a Linked ambassador and is like heavily involved in the project.
[1219.96 → 1222.96] So it's really awesome to see him be able to talk about what he did with it.
[1222.96 → 1226.58] And then the other one that I'm really excited about is from, I guess, the other part of
[1226.58 → 1231.68] the world, which is the folks from Indian Australia have this amazing story where they
[1231.68 → 1235.90] basically 10x their throughput using Linked of like their entire system.
[1235.98 → 1239.16] They have a huge deployment through a combination of load balancing and some other
[1239.16 → 1239.36] stuff.
[1239.42 → 1241.16] So we're going to talk about that at Rubicon proper.
[1241.24 → 1241.90] I think that's on Friday.
[1241.90 → 1245.24] So those two things I'm really excited about because I've been talking to these people
[1245.24 → 1247.14] for a long, both of them for a long time.
[1247.72 → 1250.24] And yeah, I'm just really excited to get their story out there.
[1250.40 → 1251.82] They're both really exciting stories.
[1252.20 → 1252.24] Okay.
[1252.44 → 1254.28] I will make sure to check them out as well.
[1254.68 → 1257.82] I'll put them in the show notes for people to check them out if they'll be available,
[1257.82 → 1258.48] but that's great.
[1258.58 → 1259.50] Thank you for sharing that.
[1259.92 → 1264.80] When it comes to the people that you're most looking forward to meeting, anyone in particular
[1264.80 → 1265.78] that you want to shout out?
[1266.00 → 1266.66] Oh boy.
[1267.66 → 1271.34] I actually am meeting a ton of people there, but is there anyone I want to shout out?
[1271.34 → 1272.20] No, I don't think so.
[1273.38 → 1273.88] That's good.
[1273.98 → 1274.44] It's too many.
[1274.78 → 1278.18] Let's pretend it's so many, like no particular name comes to your mind.
[1278.24 → 1278.66] That's okay.
[1278.86 → 1279.54] That works too.
[1279.72 → 1283.30] You know, one thing that's weird is I'm going to be meeting people who have worked on Linked
[1283.30 → 1285.22] for a long time who I've never actually met in person.
[1285.58 → 1286.24] That part's exciting.
[1286.24 → 1290.30] I'm going to be meeting people who work at Boyne who I've never actually met in person.
[1290.98 → 1293.52] You know, even though I'm the CEO, like I've never actually met them in person.
[1293.60 → 1294.94] So we're going to meet for the first time at Rubicon.
[1295.30 → 1297.74] I mean, that's just a sign of the crazy times we live in.
[1298.18 → 1301.22] Well, I hope everybody shows up and everybody will be just as excited
[1301.22 → 1303.66] as you to meet them and happy afterwards.
[1303.90 → 1304.94] Like they'll want to do it again.
[1305.14 → 1306.76] Everyone will be smiling behind their masks.
[1307.74 → 1308.06] Exactly.
[1308.26 → 1308.44] Yeah.
[1308.46 → 1309.20] You can't see it.
[1309.40 → 1311.62] So yeah, if they're frowning, well, actually if they're frowning, you can see.
[1311.70 → 1315.52] But anyway, anyway, anything interesting happening in the next six months
[1315.52 → 1317.34] for Linked that you want to share?
[1317.60 → 1318.36] Anything coming up?
[1318.54 → 1319.12] Whoa, boy.
[1319.24 → 1322.24] Gosh, I feel like we just had all the interesting things happen at once.
[1322.24 → 1328.14] We had graduation happen just like a few months ago, 2.11, you know, and now we're planning
[1328.14 → 1330.30] 2.12 and 2.13.
[1330.56 → 1334.68] So, you know, do we have anything specific beyond like some really cool releases coming
[1334.68 → 1334.90] up?
[1335.04 → 1335.68] I don't know.
[1335.80 → 1339.74] A lot of what I've been focusing on recently has actually been on Boyne Cloud, which is
[1339.74 → 1342.32] our SaaS kind of complement to Linked.
[1342.42 → 1346.64] And there's a free tier so you can check it out, and you can, you know, use it without having
[1346.64 → 1349.60] to actually swipe a credit card, you know, at least at small scales.
[1349.60 → 1353.00] And there, a lot of the exciting stuff we've been working on is how do we take all the
[1353.00 → 1357.14] cool stuff that's in Linked and actually extend that out, you know, so that, you know,
[1357.20 → 1360.38] yes, you're getting metrics, but like, can we just host those metrics for you?
[1360.66 → 1363.84] Yes, you're getting data about which services are talking to which ones.
[1363.90 → 1366.10] Can we draw that in a nice topology map for you?
[1366.36 → 1367.30] Yes, you're getting MTLS.
[1367.60 → 1370.34] Can we break down that traffic into like these different categories?
[1370.70 → 1374.14] So there's a lot of cool stuff happening on the Boyne Cloud side.
[1374.26 → 1378.68] But yeah, I think for Linked, you know, a couple more releases, we're going to keep going
[1378.68 → 1379.92] down the path of policy.
[1380.14 → 1384.44] The other big thing we want to focus on is mesh expansion, which means running the data
[1384.44 → 1389.36] plane, you know, the proxies themselves, which are these ultralight Rust proxies, running
[1389.36 → 1390.26] them outside of Kubernetes.
[1390.82 → 1395.70] Control plane is still going to be in Kubernetes, but that way you can extend your mesh out to
[1395.70 → 1397.60] VMs or to non-Kubernetes environments.
[1397.76 → 1400.72] Apparently people run code outside of Kubernetes, or so I hear.
[1401.42 → 1403.50] So there's a world outside of Kubernetes.
[1403.88 → 1405.66] Sometimes for me, it's hard to believe as well.
[1405.86 → 1406.06] It's scary.
[1406.06 → 1408.60] William, this has been everything I imagined it would be.
[1409.08 → 1410.38] Thank you very much for making the time.
[1410.52 → 1411.16] It's been my pleasure.
[1411.36 → 1411.66] Thank you.
[1411.74 → 1413.80] It's been an absolute pleasure to be here.
[1413.90 → 1414.66] Thank you for having me.
[1414.66 → 1435.20] This episode is brought to you by our friends at Launch Darkly, feature management for the
[1435.20 → 1436.04] modern enterprise.
[1436.40 → 1438.60] Power testing in production at any scale.
[1438.84 → 1439.62] Here's how it works.
[1439.62 → 1444.54] Launch Darkly enables development teams and operation teams to deploy code at any time,
[1444.80 → 1447.08] even if a feature isn't ready to be released to users.
[1447.44 → 1451.66] Wrapping code with feature flags gives you the safety to test new features and infrastructure
[1451.66 → 1455.34] in your production environments without impacting the wrong end users.
[1455.78 → 1459.30] When you're ready to release more widely, update the flag status and the changes are made
[1459.30 → 1462.12] instantaneously by the real-time streaming architecture.
[1462.54 → 1466.80] Eliminate risk, deliver value, get started for free today at LaunchDarkly.com.
[1466.80 → 1468.82] Again, LaunchDarkly.com.
[1483.98 → 1488.70] So, the first and the last time that we spoke, it was two Rubicons ago.
[1488.90 → 1489.76] That's why I measure it.
[1489.90 → 1492.50] And I say Rubicons, I mean Rubicon North America.
[1492.98 → 1494.70] That was Change Lock episode 375.
[1494.70 → 1498.84] We had a discussion with the Prometheus core maintainers, and you were one of them.
[1499.26 → 1501.48] And that was 2019, as I mentioned.
[1501.70 → 1504.04] So, what is new with you, Frederick, since then?
[1504.18 → 1507.00] So, yeah, actually since 2019, a lot has happened.
[1507.62 → 1511.50] So, I guess I can go chronologically from that point onwards.
[1512.16 → 1518.38] So, in 2019, I actually, I did give a keynote at Rubicon in Barcelona.
[1518.38 → 1521.44] So, that was the other Rubicon that was happening that year.
[1521.90 → 1530.08] About the future of observability that was together with Tom, who I believe you spoke to at the same Rubicon as well.
[1530.44 → 1537.16] So, we were talking about a couple of predictions that we felt like were going to happen to the observability space.
[1537.16 → 1547.46] And one of my predictions was that I felt like continuous profiling was going to establish itself as an area within observability.
[1547.84 → 1556.46] And for that keynote, I had put together a proof of concept that I very creatively called CONTROL, you know, continuous profiling.
[1556.46 → 1564.24] And got some traction, but I never really had enough time to work on it beyond the proof of concept.
[1564.54 → 1569.98] And, yeah, I guess just at some point, you know, the pandemic probably had some part in it.
[1570.22 → 1575.92] Like half a year into the pandemic, I felt like there still wasn't enough being done in that space, I felt.
[1576.26 → 1579.90] And so, I thought to myself, it's kind of now or never.
[1580.32 → 1584.00] And I, end of last year, decided to make it my full-time job.
[1584.06 → 1585.52] And I founded Polar Signals.
[1585.52 → 1592.44] You know, we, I guess kind of because of the history of when I worked at CoreOS, and we got acquired by Red Hat,
[1592.64 → 1596.44] I had quite a lot of interest from investors pretty much immediately.
[1597.02 → 1605.14] But at the same time, I didn't feel like we had explored the space enough to, you know, take on VC money immediately.
[1605.72 → 1609.32] And, you know, raise money that we wouldn't know what to do with.
[1609.56 → 1612.54] I guess that's just me personally, the kind of person I am.
[1612.54 → 1616.08] And I wanted to understand what I would do with money if we raised it.
[1616.42 → 1617.10] And so...
[1617.10 → 1619.10] I would like to stop you there because this is really important.
[1619.52 → 1620.92] And I don't think listeners know this.
[1621.22 → 1624.92] Having looked at what you're about, it's not enough to observe.
[1625.22 → 1626.28] You have to understand.
[1626.70 → 1629.24] So, I think this understanding runs very deep for you.
[1629.24 → 1633.44] And I can see the connection to, you have to understand.
[1633.58 → 1636.16] You have to know, really know what you're doing.
[1636.56 → 1640.54] And I would like to connect these two dots because they're important, and they'll keep coming back.
[1640.78 → 1641.54] But please carry on.
[1641.54 → 1641.86] Yeah.
[1642.00 → 1643.56] Thank you for making that point.
[1643.66 → 1645.04] I think I know where you're going.
[1645.38 → 1647.04] So, we started the company.
[1647.58 → 1659.42] And a perfect friend from Coro West Times, Thor Hansen, he, many years ago at a Gopher Con, he told me, you know, if you ever start a company, I want to be the first person to work with you.
[1659.42 → 1660.60] And he kept his word.
[1661.22 → 1663.98] In November 2020, he joined Polar Signals.
[1664.42 → 1666.60] And since then, a couple more people have joined.
[1667.28 → 1675.14] And in February of this year, we launched a private invite-only beta of our product for continuous profiling.
[1675.60 → 1678.78] And I guess we should talk a little bit about what continuous profiling is.
[1679.22 → 1683.84] So, essentially, profiling itself has been around ever since programming has, right?
[1683.84 → 1689.08] When we did our research, we found it had gone back at least to the 60s and 70s.
[1689.08 → 1696.50] Because everybody, as soon as they started programming, needed to understand what was happening with the code that they had been writing, right?
[1696.92 → 1699.14] What was using the CPU time?
[1699.26 → 1705.44] And even, especially in the 60s and 70s, it was so much more precious to have CPU time, right?
[1705.72 → 1708.44] And so, profiling has been around for a while.
[1708.78 → 1710.44] There had been kind of two problems with it.
[1710.44 → 1716.28] One was, for the longest time, profiling was incredibly expensive to do in production.
[1716.28 → 1725.16] You would only do it to specific processes at a certain, like, on-demand because you didn't want to create too much additional overhead.
[1725.60 → 1731.58] There was one thing that kind of led to us being able to do this in production and always on.
[1732.00 → 1735.68] And one of those things is what we call sampling profiling.
[1735.68 → 1748.90] So, instead of kind of tracing exactly, absolutely everything a process does, we only, you know, 100 times per second look at what the program does at that particular moment in time and capture the stack trace of what it does.
[1749.12 → 1752.74] Because, essentially, the stack trace represents what the program is doing, right?
[1752.74 → 1764.02] And so, for a start already, for some hyperscalers, this was already enough to build continuous profiling tools for them to consume internally because they could do it always on in production now.
[1764.34 → 1771.42] Now, as it goes with so much cloud-native technology and developments, that wasn't necessarily accessible to everyone.
[1771.42 → 1778.44] And one of the really amazing things that also have happened somewhat recently has been EPF.
[1778.82 → 1790.00] And EPF allows us to capture this data at an even lower overhead because we can already capture it in the form that we are going to consume it afterwards.
[1790.42 → 1798.70] We don't need to use some pre-baked format that may have a ton of information that we don't need, a ton of detail we don't need.
[1798.70 → 1805.96] We can produce exactly the data that we want and make that exportable to user space and then ingest it into our storage.
[1806.28 → 1810.56] So, that was definitely also a huge part of what created a movement.
[1811.16 → 1813.78] But kind of, this doesn't really have to do with overhead.
[1814.38 → 1821.80] There's also another aspect, which is just kind of Kubernetes unifying the observability space in a way.
[1821.80 → 1825.82] And I think we might have talked about this in our last session, actually.
[1826.36 → 1832.08] The way that Prometheus also and Kubernetes have kind of standardized a lot of terms in our industry.
[1832.36 → 1835.24] It just makes us all speak the same language.
[1835.86 → 1843.78] And so, this is super powerful because all of a sudden, when I say pod, and you say pod, we immediately know what we're talking about, right?
[1843.78 → 1850.62] And so, this is much more cultural than it is technologically, but it means that our knowledge is transferable.
[1851.04 → 1852.46] And so, this is incredibly powerful.
[1852.70 → 1855.40] And then the last piece is putting all of this together.
[1855.94 → 1862.50] EPF with Kubernetes now allows us to automatically discover all the containers that are running in our infrastructure
[1862.50 → 1868.88] and be able to look at all the CPU time that is being consumed in our infrastructure at once.
[1868.88 → 1880.66] And the reason why this is so powerful is that all of a sudden, we can now say this stack trace in this binary is what's causing 20% of our CPU time.
[1881.14 → 1887.76] If we optimize this stack trace away, we're now saving 20% of CPU time in our infrastructure.
[1888.26 → 1889.54] That's huge, right?
[1889.60 → 1895.16] Think of the banks, automotive companies, any company that has a large cloud bill, right?
[1895.48 → 1898.62] They can save millions of dollars with these kinds of measurements.
[1898.62 → 1902.10] It's just the reality is they can do these measurements today.
[1902.44 → 1905.86] And it doesn't really matter what language you're using, right?
[1905.90 → 1907.94] Because everything runs as a pod.
[1908.20 → 1911.18] It doesn't matter whether it's Java, whether it's Go, whether it's Erlang.
[1911.30 → 1912.14] It really doesn't matter.
[1912.56 → 1920.04] The point being is you run this agent on your Kubernetes worker node where all these pods are being scheduled.
[1920.46 → 1924.96] And you can see out of the pods which are being scheduled, out of the containers which are running within those pods,
[1925.30 → 1927.42] which are the ones that consume the most CPU.
[1927.42 → 1929.48] And I imagine this goes beyond CPU.
[1929.96 → 1939.14] It goes to memory, disk operations, network operations, I operations, all that nice, important stuff that the kernel knows about.
[1939.30 → 1942.76] And it presents you via EPF in a way that makes sense to you.
[1942.84 → 1945.94] And it doesn't matter what language is making that call.
[1946.10 → 1948.50] Whether you have a serverless framework, it really doesn't matter.
[1948.60 → 1949.44] It's really powerful.
[1949.74 → 1951.18] I like the way you're thinking about this.
[1951.18 → 1958.14] So I was going to ask you, parka.dev is the thing that you're opening up to the world at this Rubicon.
[1958.50 → 1962.54] And I was going to ask you, why do you need parka?
[1962.74 → 1964.90] But I think the answer is to cost optimize.
[1965.62 → 1967.02] But maybe there's something more to it.
[1967.24 → 1970.30] First, I think, and we said this in our announcement as well.
[1970.30 → 1979.52] I think just the people that we are and the company that we're building, I think we needed to have an open source piece to be ourselves.
[1979.52 → 1986.56] So even if there wasn't anything else, that would probably already would have been enough of an argument for us.
[1986.94 → 1997.72] But I think more importantly, continuous profiling is, even though there are now several vendors, several projects out there, in the only one year that Polar Signals has existed, right?
[1997.80 → 2002.34] Like there are several companies that have sprung up, several vendors that have created products.
[2002.66 → 2007.02] But it's still a really young space and is still not very well understood.
[2007.02 → 2017.26] And so in a way, the open source project is also about democratizing this for the community and educating the community about continuous profiling.
[2017.56 → 2024.50] So that when we talk about continuous profiling, hopefully in a year or two, everyone understands it like when I say distributed tracing.
[2024.90 → 2031.12] So if I understand correctly, it's your need to understand what the system does.
[2031.12 → 2037.12] And the itch that you're scratching is you wanting to understand what is happening on those nodes.
[2037.52 → 2038.40] So that's why I did it.
[2038.68 → 2039.30] As simple as that.
[2040.18 → 2040.80] I love that.
[2041.20 → 2041.74] I love that.
[2041.88 → 2045.72] The backstory actually goes a little bit further than where I started.
[2045.72 → 2057.14] But the reason why I even went into putting together that proof of concept with Conprof was because I read a paper by Google where they described these methodologies, right?
[2057.14 → 2064.02] How they used this kind of methods to cut down on infrastructure costs every quarter by multiple percentage points, right?
[2064.46 → 2067.64] And I was just amazed by that for several reasons.
[2068.00 → 2072.38] One, I just wanted to have this tool while I was working on Prometheus, right?
[2072.38 → 2075.62] And the other one was I had worked on Prometheus.
[2076.02 → 2082.20] At least I thought to myself, I think I know a thing or two about working with data over time, right?
[2082.26 → 2089.64] And so I think that's kind of what ultimately created the circumstances of me wanting to create a tool like this.
[2089.98 → 2092.82] So I got the tool up and running in seconds.
[2092.96 → 2093.08] Right.
[2093.22 → 2095.78] Like that just shows how easy it is to get started.
[2095.86 → 2096.76] This was just local.
[2097.16 → 2101.90] I didn't want to venture in our production Kubernetes cluster because I have something else in mind for that.
[2101.90 → 2104.94] But in a few seconds, I could access the UI.
[2105.28 → 2106.52] I could see the CPU time.
[2107.12 → 2113.36] And the UI, what surprised me, is it's better than the first Prometheus UI that I remember.
[2113.72 → 2117.24] And I think the secret to this is your coffee machine.
[2117.46 → 2118.12] Let me explain.
[2118.32 → 2118.54] Okay.
[2118.60 → 2119.18] Let me explain.
[2119.84 → 2121.46] So this is what's going on in my mind.
[2122.10 → 2130.34] When I first heard of ARCA a few weeks back, I checked it out, and it was looking good, but it wasn't as polished as it is today.
[2130.34 → 2136.26] Just in a matter of a few weeks, I was astounded by how fast you're iterating on it.
[2136.64 → 2139.06] And I think that it's your new coffee machine.
[2140.06 → 2141.28] Is that it?
[2141.82 → 2142.68] What's the secret?
[2143.04 → 2144.76] I would say it has a part in it.
[2145.10 → 2145.42] Okay.
[2145.42 → 2151.00] I think the UI is actually an evolution of several attempts at it.
[2151.22 → 2171.78] The very first one was actually within our closed source beta product where, you know, when we launched it in early February this year, we used this to work really closely with a couple of early users to understand what is it that they, beyond the UI even, what is it that they want from an experience from a tool like this?
[2171.78 → 2172.06] Right.
[2172.44 → 2178.36] But then also, of course, like also with ourselves using the software, like how do we want to use it?
[2178.46 → 2186.40] And so I think there's so much Gooding that was going on from basically day one, because this is a tool that we built for ourselves.
[2186.64 → 2188.66] We wanted to put that work into it.
[2188.82 → 2188.92] Right.
[2189.18 → 2190.22] What do you use the tool for?
[2190.28 → 2190.98] This is fascinating.
[2191.20 → 2191.94] I love this story.
[2191.94 → 2193.54] I mean, there's a theme here.
[2193.80 → 2208.92] Every great product dogwoods itself and the developers and the product and the entire team that works on it uses it on a daily basis, understands the shortcomings and fixes them maybe before even uses C, those problems.
[2209.06 → 2210.02] I think there's a theme here.
[2210.34 → 2212.74] But how do you use Parka for Parka?
[2213.00 → 2215.66] This question and the answer fascinates me.
[2215.66 → 2215.96] Yeah.
[2216.08 → 2225.96] So actually, this is a cool topic that I think we even want to run blog post series about, because I think there are just so many aspects to this that I would love to talk about.
[2226.06 → 2227.14] Can we have a short answer?
[2227.48 → 2231.82] Because this is a short piece, but it's obvious that we need a much longer one.
[2231.82 → 2232.32] Yeah.
[2232.50 → 2239.62] So basically, like boiled down, Parka itself is a really performance sensitive software, right?
[2239.66 → 2247.82] It has a specifically designed storage and query engine so that we can actually do all of these amazing things with continuous profiling.
[2248.04 → 2250.56] So we use Parka to optimize Parka.
[2250.56 → 2253.10] And so this is kind of a vicious cycle, right?
[2253.14 → 2262.64] Because we keep creating this more and more performance software to create more and more performance software to do even more powerful things to optimize it even further.
[2262.96 → 2266.06] And so it's kind of, it's really addicting almost.
[2266.38 → 2266.86] I love that.
[2266.98 → 2267.42] I love that.
[2267.48 → 2268.38] We do the same thing.
[2268.46 → 2269.44] I'm a big fan of that.
[2269.54 → 2270.04] That's it.
[2270.22 → 2270.78] That loop.
[2271.02 → 2272.34] It's one of my favourite loops.
[2272.72 → 2273.14] Amazing.
[2273.14 → 2282.90] So just to switch gears a little bit and think about the Rubicon, and what's going to happen this week, what are you looking forward to the most at this Rubicon?
[2283.26 → 2284.40] Is there something that you're looking forward to?
[2284.64 → 2290.36] I think, of course, this probably reflects my own interests quite a lot and what we do with Parka as well.
[2290.76 → 2298.36] But I'm really excited about how the EPF space is evolving into more of a production ready state, if that makes sense.
[2298.36 → 2307.56] I feel like it's very similar to the first hype wave of service mesh that we had where everybody was talking about it, but no one was using it.
[2307.92 → 2317.86] And then one or two Rubicons after that, suddenly there were all these great stories about how people were actually running it and using it in really useful ways, right?
[2317.86 → 2329.76] And so I feel like we're kind of at a turning point with EPF as well, where so many people have gotten their hands on it that we're suddenly seeing all these really incredible applications for it.
[2330.04 → 2334.24] And so I'm really looking forward to a bunch of the EPF talks that are coming out.
[2334.60 → 2335.64] Any specific talks?
[2335.98 → 2345.20] There's one by Derek Parker who works on the Delve debugger, which is kind of the de facto debugger in the Go community.
[2345.20 → 2347.84] I think he's doing some fascinating things.
[2348.32 → 2351.70] There are even some integrations into the debugger with EPF.
[2351.86 → 2353.22] I find that fascinating.
[2353.80 → 2361.82] But the really cool thing about EPF is almost its unpredictability of what you can do with it.
[2362.42 → 2369.34] Because it allows us to do such wild things anywhere in the kernel attached to any kind of event,
[2369.34 → 2377.04] people have come up with super innovative things that we were able to do in the past with kernel modules.
[2377.20 → 2382.08] But let's be honest, nobody really enjoyed the user experience of that.
[2382.42 → 2387.78] And now all of these things are being productionized, and I'm just really excited about all the possibilities.
[2388.28 → 2389.44] That sounds interesting.
[2389.70 → 2393.36] So anything EPF related, that's where your interest is.
[2393.94 → 2395.94] And you, Derek Parker, did you say?
[2396.08 → 2396.28] Yeah.
[2396.28 → 2396.64] Okay.
[2396.80 → 2398.12] I've heard Derek Parker.
[2398.48 → 2399.30] Derek Parker.
[2399.54 → 2399.68] Okay.
[2400.26 → 2400.92] That's a good one.
[2401.96 → 2403.16] Park everywhere, right?
[2403.28 → 2403.98] That is completely unintentional.
[2404.10 → 2405.22] Yeah, that's what happens.
[2405.88 → 2408.98] And I'm imagining that you're not going to attend the conference in person, right?
[2409.18 → 2409.50] Yeah.
[2409.70 → 2418.30] Unfortunately, you know, as much as I would have wanted to, unfortunately, travel restrictions are still in place for Europe to travel to the US.
[2418.30 → 2418.60] Yeah.
[2418.60 → 2421.50] But, you know, there's always another Rubicon.
[2421.78 → 2423.04] Yeah, it was the same for me.
[2423.14 → 2423.52] You're right.
[2423.64 → 2425.10] I really wanted to be there in person.
[2425.70 → 2437.04] So what advice do you have for those that couldn't attend and will be attending virtually and some will be catching up on the videos because they won't be able to attend virtually because of the time difference?
[2437.04 → 2443.18] Yeah, I mean, look, it's like half of the world that's not able to attend this Rubicon, so you're not alone.
[2443.52 → 2452.06] I know there are several folks that are doing just, you know, local meetups or local virtual meetups or just, you know, going for lunch or something.
[2452.52 → 2453.46] Find your local group.
[2453.46 → 2455.46] Or if not, just watch the recordings.
[2456.30 → 2461.64] The platforms have become so much better since the first time we've done these virtual conferences.
[2462.00 → 2465.60] Just try to be a part of it as much as you can, given the circumstances.
[2465.98 → 2471.96] And, you know, we've got Rubicon EU coming up next year, and it's at the end of the winter, right?
[2472.04 → 2477.12] So no matter what happens, that's kind of the time when COVID cases went down anyway.
[2477.34 → 2480.62] I feel like the next Rubicon in EU is going to be great.
[2480.62 → 2483.90] A lot of us are going to be able to attend that one, if not this one.
[2484.10 → 2484.92] Those are some great tips.
[2485.26 → 2489.22] Is there anything interesting happening in the next six months for Parka that you want to share?
[2489.42 → 2498.78] I think in a way, a lot of what we're, we shared it really early intentionally to understand what the community also wants from a project like this.
[2499.00 → 2510.32] Like we intentionally did not immediately release multiple types of visualizations, or we didn't immediately go all in on a query language or stuff like that.
[2510.32 → 2521.22] We do think these things are on the horizon, but it's just so much, you're going to create something so much better when you work with a community and talk to a lot of people.
[2521.22 → 2531.64] It's just like creating any product, you know, but we just feel like we owe it to the open source community because really the open source community has made us who we are today.
[2531.64 → 2537.44] And so if we can give back a little bit of that, then we've achieved our goal, you know.
[2537.70 → 2537.82] Wow.
[2537.94 → 2538.56] That's amazing.
[2538.90 → 2541.06] I wish everybody thought like that.
[2541.36 → 2544.48] And I think most people think like that in the CNCF space.
[2544.64 → 2547.04] And it just goes to show, that's it.
[2547.18 → 2552.06] This right here is the reason why the CNCF is as successful because people think like you do.
[2552.26 → 2553.34] It's amazing to see that.
[2553.34 → 2561.56] The one thing which I would like to do as we are wrapping this up is I want to congratulate you on the hiring page, which I think is a baseline for others to follow.
[2561.80 → 2562.54] It's simple.
[2562.74 → 2563.52] It's to the point.
[2563.66 → 2564.34] It's inviting.
[2564.92 → 2567.20] It makes me want to find out more.
[2567.38 → 2568.46] And that is saying a lot.
[2568.46 → 2573.80] So I would like to congratulate you once again, like well done for striking such a great balance.
[2574.22 → 2578.96] And I'm sure that it's so simple because a lot of thinking went into it and a lot of refinement.
[2579.52 → 2582.70] And again, I'm seeing a trend here, which I really like.
[2583.04 → 2583.88] That's been great to see.
[2584.14 → 2584.42] Thank you.
[2584.56 → 2584.88] Thank you.
[2584.88 → 2614.86] Thank you.
[2614.88 → 2644.86] Thank you.
[2644.88 → 2674.86] Thank you.
[2674.88 → 2679.78] And in that cozy talk, Andrew and Stephen did an amazing job.
[2680.00 → 2686.26] My concluding thought was that it made me reconsider the operating system that I want for changelog.com.
[2686.26 → 2695.34] And I do have to say that while I didn't get there, I'm really glad that we have this opportunity to talk with your amazing microphone, Andrew.
[2695.34 → 2699.40] Yeah, I have since upgraded Rubicon EU.
[2699.40 → 2702.50] I used to, I think that was with my blue baby bottle.
[2702.62 → 2704.72] This one's the Sennheiser MKH 416.
[2704.72 → 2707.84] And it's just a this one is made for like a voiceover.
[2707.84 → 2709.52] So yeah, I'm loving it.
[2709.74 → 2711.56] It's an amazing sound, I have to say.
[2711.62 → 2712.88] And there's also something natural there.
[2712.88 → 2713.52] So I really like it.
[2713.52 → 2713.66] So I really liked it.
[2713.66 → 2717.70] Like, you know, listening to that talk and seeing the visuals that Stephen produced were amazing.
[2718.36 → 2720.38] So that was, yeah, that was a great one.
[2721.08 → 2725.86] So since Rubicon EU, which is about five months now, what is new in the world of Cozy?
[2726.02 → 2736.24] So Cozy proper, as far as, you know, what it is in the GitHub org and, you know, outside of Talos, not much has looked like it has changed.
[2736.48 → 2743.94] But in Talos itself, we've been implementing a lot of the ideas and kind of using that as a proving grounds, if you will, for the idea.
[2744.08 → 2746.68] And it's actually working out phenomenally well.
[2746.68 → 2752.76] We have since rewritten our entire networking stack of Talos on top of the concepts of Cozy.
[2753.58 → 2755.70] And it's really, really cool.
[2755.92 → 2757.94] I mean, where do I even start?
[2758.28 → 2762.28] When you submit your configuration to Talos, the controllers just pick it up.
[2762.68 → 2764.24] They know when to set up bonding.
[2764.46 → 2769.20] They know when to, you know, the order in which you should set up the interfaces to get bonding going.
[2770.20 → 2775.72] Validation on whether the particular combination of options for an interface, say.
[2775.72 → 2777.42] It just won't work.
[2777.66 → 2779.38] You know, tons of validation around things.
[2779.56 → 2784.00] We've since launched a product called Loops Band, which we could probably get into more later.
[2784.14 → 2787.32] But it's basically a way to do automated wire guard.
[2787.90 → 2791.80] And in Talos, all you really do is just you set up two little configurations.
[2792.22 → 2794.60] You set them enabled, true, or something to that effect.
[2795.16 → 2800.16] And all of a sudden, all these nodes know how to reconfigure themselves reactively.
[2800.16 → 2803.86] And this is all really because of the ideas around Cozy.
[2804.22 → 2811.16] Otherwise, we're going to be stuck with SSH and going in and manually executing, you know, classic Unix utilities.
[2811.52 → 2816.12] And it just, sure, it would work, but it would not feel clean.
[2816.46 → 2817.82] It would feel very hacky.
[2817.94 → 2820.30] So I'm pretty proud of what the team has been doing.
[2820.30 → 2824.10] So first, when I looked at Talos, it looked fascinating.
[2824.56 → 2827.22] The getting started part, I struggled a little bit.
[2827.60 → 2831.60] And I know the Super came along and that made some things easier.
[2832.12 → 2836.54] Cozy was fascinating because the concepts, they were not like specific to an implementation,
[2836.74 → 2839.30] but they were like a standard that you were trying to build.
[2839.42 → 2840.82] And I really like that.
[2841.08 → 2846.62] I do have to say, since trying Super, the first time I think was 0.1 when I struggled.
[2846.62 → 2847.76] I haven't tried it since.
[2847.84 → 2848.76] I know it's 0.3.
[2849.28 → 2853.42] So even though I would love to start with this, how would I start?
[2853.54 → 2855.22] Like, where would I go with Talos?
[2855.26 → 2857.30] Which is like the first thing that I would do.
[2857.58 → 2858.54] What would you recommend?
[2858.94 → 2859.14] Yeah.
[2859.24 → 2865.98] So we have the ability to basically spin up Kubernetes clusters right there on your laptop,
[2866.18 → 2867.44] built into our CLI.
[2867.80 → 2869.98] I'd say that that's the easiest way.
[2870.04 → 2874.48] If you want to get a feel for what it's like to interact with an operating system that's API driven
[2874.48 → 2879.38] and has a CLI and doesn't have SSH and all these things, that is the easiest way.
[2879.44 → 2880.64] You just do a simple command.
[2880.74 → 2882.14] Talos CTL cluster create.
[2882.42 → 2888.32] The good news is that this kind of translates really well into, say, running it on bare metal.
[2888.42 → 2893.92] You could literally grab that configuration file, maybe modify the networking section a little bit,
[2894.30 → 2896.10] turn on a machine with an ISO file,
[2896.10 → 2902.78] and submit the configuration file that you had running from your mock environment,
[2903.14 → 2905.92] by the way, which runs in Docker or SMU.
[2906.26 → 2909.10] Those are probably the two easiest ways.
[2909.40 → 2912.30] One has a benefit of being more developer friendly.
[2912.44 → 2918.26] Let's say that you're developing an application, and you want something to represent your testing
[2918.26 → 2919.68] or production environments closely.
[2919.94 → 2924.46] That's when Talos CTL cluster create is really nice because you could just spin up a Kubernetes cluster.
[2924.46 → 2931.10] You got one a minute or two later, and it matches at least API-wise everything that you're going to run in production.
[2931.82 → 2936.48] And then, you know, getting that to work in actual bare metal, that's another story.
[2936.62 → 2941.42] Typically, that just involves networking, and that's where 90% of all the problems happen.
[2942.16 → 2947.78] So at that point, it's really just crafting the networking section, as we just talked about.
[2948.06 → 2949.50] Cozy's going to roll those out for you.
[2949.66 → 2951.22] Well, Talos using Cozy.
[2951.22 → 2955.30] The easiest way to get started on bare metal, I would say, is using the ISO or the ISO.
[2956.02 → 2957.74] Some people call it different things.
[2958.36 → 2960.40] After that, you know, pixie booting.
[2960.56 → 2964.44] Pixie booting is a whole other level, and that's where we have our Pedro product,
[2964.66 → 2969.26] which aims to streamline that whole process and really own it for you.
[2969.26 → 2972.70] But that's the natural progression that I would go towards.
[2972.94 → 2977.66] Of course, you have the cloud in there somewhere, and right after you, you know, that's where they diverge,
[2977.72 → 2980.86] right when you're talking about using the ISO or not.
[2981.00 → 2982.34] In the cloud, it's a little bit different.
[2982.48 → 2988.06] You have to have some image that's been uploaded, and all of our documentation goes through how to upload the image.
[2988.06 → 2992.80] In our releases, we have the assets already prepared for you.
[2993.18 → 3000.60] You follow the documentation to upload the image into your particular cloud, and all you do really is turn it on with the correct user data.
[3000.60 → 3009.62] So what I'm getting at really at the end of the day is it just really boils down to how do I get Talos just simply installed or like running somewhere, right?
[3009.66 → 3012.74] Whether that's a VM or containers or bare metal.
[3013.26 → 3015.94] And then it's just knowing the configuration file.
[3016.16 → 3019.34] In the same way that with Kubernetes, I know that I have Kubernetes.
[3019.54 → 3021.16] Do I really care where it's running?
[3021.32 → 3027.72] I know that I can describe my application and how it should run using declarative YAML.
[3027.72 → 3031.46] We're bringing that same experience into the operating system.
[3031.66 → 3039.60] So getting started, you know, it's really just grasping the idea that you just need to turn Talos on, however that may be and wherever that may be,
[3039.68 → 3044.38] and get comfortable with the configuration file and being able to submit and update the system.
[3044.66 → 3050.30] I can see where I've been going wrong because I usually start in the cloud and I usually start with pixie booting.
[3050.56 → 3053.16] And I think that is possibly the hardest way.
[3053.16 → 3059.20] So if you start there without knowing the lay of the land, you went like in extreme mode.
[3059.54 → 3061.36] So good luck trying to figure all those things out.
[3061.42 → 3066.72] And I think this was actually even before Cozy, like six months ago, nine months ago, somewhere around there.
[3067.06 → 3069.22] And I know that you've made strides since then.
[3069.34 → 3070.26] And things are clearer.
[3070.38 → 3071.70] Things are better, as you would expect.
[3071.70 → 3075.14] So I think that I know what I'm going to do next.
[3075.44 → 3078.98] And for someone that doesn't even run Docker locally, I just like everything in the cloud.
[3079.02 → 3082.92] Because if it's on my machine, well, how do I know that it will run in the cloud?
[3083.00 → 3089.18] But I know that Talos makes it slightly different, even though most things it runs locally, but it will not work the same in the cloud.
[3089.24 → 3090.92] And that's always like a friction.
[3090.92 → 3094.58] I want to touch on that because I actually think that that's really important to point out.
[3094.70 → 3100.52] And that's actually a huge motivating factor around Talos was because I was managing Kubernetes clusters.
[3101.08 → 3105.58] And, you know, the first place that I was doing this, we were debating, should we do this with bare metal?
[3105.80 → 3106.78] Can we run CoreOS?
[3107.48 → 3112.40] Well, typically we run CentOS, but we're also running, you know, this up in AWS.
[3112.78 → 3114.92] And I wanted this consistency story.
[3114.92 → 3122.90] And then we also had our developers that were saying, hey, I want to be able to actually spin this up on my local laptop and not depend on anything that you guys have set up.
[3123.36 → 3129.38] Even though we went to great lengths to give them testing environments, they still ended up just creating their own.
[3129.72 → 3134.96] And so Talos is really beautiful in that sense because it's literally the same image.
[3135.06 → 3139.94] The same image that runs right there on your laptop can be rolled out to anywhere.
[3140.16 → 3143.48] Raspberry Pis, the cloud, bare metal, anywhere that you can imagine.
[3143.48 → 3146.88] And the experience is going to be consistent, more or less.
[3147.02 → 3154.66] Obviously, when you're running in containers, you have the element of the kernel being the host operating systems kernel and networking and stuff like that.
[3154.72 → 3156.02] But that's minor, right?
[3156.08 → 3158.58] Those are things that you can kind of craft after the fact.
[3158.88 → 3161.94] I feel that you've shared a secret with us, at least with me.
[3162.04 → 3163.72] And now I know what I mean to do next.
[3163.76 → 3164.98] So thank you very much for that.
[3165.58 → 3166.20] Of course.
[3166.52 → 3172.36] The next thing which I'm thinking about is why would someone want to pick Talos over, let's say, Debian or Ubuntu?
[3172.36 → 3173.58] What would you say to them?
[3174.04 → 3174.20] Yeah.
[3174.32 → 3176.98] So this is a question that we usually get.
[3177.32 → 3187.20] One of the main reasons that you really would consider Talos over, you know, like you said, something like Debian is because these things simply come with way too much at the end of the day.
[3187.30 → 3189.32] They come with package managers.
[3189.32 → 3195.74] They come with an extra set of packages that you simply don't need if all you're concerned with is running Kubernetes.
[3196.10 → 3203.94] In some cases, you even have to do upgrades of the nodes for things completely unrelated for the purposes of running Kubernetes.
[3204.32 → 3208.50] And this is just unnecessary, to put it simply, right?
[3208.50 → 3212.42] So the first point is the minimalism that you're going to get with Talos.
[3212.56 → 3214.68] It's only about 50 megabytes.
[3215.32 → 3221.74] At the end of the day, you're going to get something tiny comparative to everything else out there.
[3221.78 → 3223.14] You're going to get no package manager.
[3223.72 → 3226.12] We don't even have SSH or Bash, right?
[3226.12 → 3238.20] And the reason why we did things like that is, or why we removed those was because if you've ever operated Kubernetes to, at any scale, right, you found yourself constantly duplicating work.
[3238.30 → 3239.66] You had to manage users.
[3239.90 → 3242.30] You had to manage hardening.
[3242.46 → 3243.76] You had to manage automation.
[3244.40 → 3248.98] But at two different layers, you had Kubernetes itself that you have to worry about and then at the operating system itself.
[3248.98 → 3255.70] And so the whole goal with Talos is to just remove that node element entirely so that you can focus on just the cluster.
[3255.94 → 3263.74] We like to tell people that we want them to look at the cluster as one giant machine and the nodes simply as more compute to that.
[3263.88 → 3266.26] So it's just more CPU and RAM to a bigger machine.
[3266.96 → 3274.74] We can't really look at it like that if we have to concern ourselves with who's logging on there, what have they changed, permissions, automating it.
[3274.84 → 3277.50] Just this overhead simply should go away.
[3277.50 → 3281.70] And that's first and foremost one of the reasons why you should consider Talos.
[3282.22 → 3285.16] And secondly, we have a really strong security emphasis.
[3285.42 → 3290.54] We recently just went through a whole exercise of actually securing our supply chain.
[3290.62 → 3292.48] So now everything's completely reproducible.
[3292.68 → 3298.44] You can get all the checksums and make sure that you're actually running the intended version of Talos.
[3298.86 → 3300.26] The file system is read-only.
[3300.66 → 3303.32] As I mentioned, Talos is only 50 megabytes.
[3303.44 → 3307.18] What I didn't mention is that it's delivered as a Squash FS, which is only read-only.
[3307.50 → 3309.30] And there is no other way to run it.
[3309.42 → 3311.32] It is also completely ephemeral.
[3311.88 → 3314.86] Now, Kubernetes, of course, needs places to write things.
[3314.86 → 3316.94] And there's only one place in Talos that's writeable.
[3317.12 → 3321.76] It's slash var, at least writeable in the sense that it's going to be persisted across reboots.
[3322.08 → 3324.58] Of course, we have slash temp and things like that.
[3325.14 → 3328.22] But that is completely ephemeral and only Talos uses those places.
[3328.76 → 3331.30] And so you're going to get a much more hardened experience.
[3331.42 → 3332.56] You're going to get people that can't.
[3332.56 → 3338.06] You're going to completely eliminate the possibility of people going on there and making a node a snowflake.
[3338.06 → 3341.40] It's really just Kubernetes that can change.
[3341.84 → 3346.88] And so that's a huge benefit when you're talking about running anything more than 10 nodes.
[3346.88 → 3352.70] I know that everybody's thinking about security chain attacks and security of everything.
[3353.16 → 3355.24] Software, developers, signing.
[3355.50 → 3363.24] Like, can you just sign everything from your commit to the release, to the artifact, to what it runs, when it runs,
[3363.30 → 3366.64] so that you can trace it all the way back to the origin of the code being written.
[3366.76 → 3367.96] That's really, really important.
[3367.96 → 3374.94] I really like this minimalist story, not just from a security perspective, that you only run what you absolutely need,
[3375.14 → 3376.72] and you run it with the least privileges.
[3376.72 → 3378.64] That is very, very powerful.
[3378.94 → 3383.94] And I think it somehow has been forgotten in the age of containers and Docker, you know,
[3384.00 → 3386.24] because it was like the wild, wild west for a long, long time.
[3386.68 → 3392.68] And I'm really glad these concerns are now coming back, because I know how important they were 10, 15 years ago.
[3392.94 → 3394.30] So I can see the cycle.
[3394.42 → 3395.56] We're back where we started.
[3395.56 → 3402.16] So from that perspective, I know that these minimalist systems, one of the things that they replace,
[3402.30 → 3407.12] and I'm wondering whether Talos does the same thing, they replace Glib for something like Musil.
[3407.38 → 3412.50] And what that tends to happen is Glib is a lot more hardened, battle-hardened, battle-tested.
[3412.78 → 3416.96] So the performance on Glib of anything tends to be better.
[3417.54 → 3424.04] So what I've seen is like weird crashes, weird degradations, weird like IO performance when you don't run Glib.
[3424.04 → 3425.68] So what does Talos use?
[3425.96 → 3428.86] We actually use Musil, and we haven't seen that at all.
[3428.98 → 3434.56] And I think that may largely be due to the fact that the only reason that we run Musil, let's see,
[3434.62 → 3437.00] we only have a handful of things really on the root FS.
[3437.22 → 3445.78] We have container D, and we have XFS frogs, and maybe some LVM tooling, and then Talos itself.
[3445.78 → 3451.96] And so the actual C libraries that are running in Talos are practically negligible.
[3452.12 → 3453.02] It's practically zero.
[3453.32 → 3454.92] We don't even have system D.
[3455.18 → 3461.24] In fact, our unit system is a new unit system that we're building for the purposes of these style of operating systems,
[3461.42 → 3462.68] API-driven operating systems.
[3463.00 → 3464.24] And so that is written in Go.
[3464.52 → 3466.22] Practically everything that we do is in Go.
[3466.22 → 3473.32] And so I think maybe that can be contributed to the fact that, you know, we are running Musil, but we haven't run into any issues.
[3473.94 → 3479.98] And then Kubernetes itself, since it's delivered in containers, those containers have Glib.
[3480.28 → 3485.64] So the role that Musil really plays in our ecosystem is very, very small.
[3485.86 → 3485.96] Yeah.
[3486.32 → 3487.24] I always had it different.
[3487.24 → 3492.06] So usually the host would run Glib, and the container would run Musil.
[3492.44 → 3497.52] And then that combination from that direction always seems to have seemed to have created problems.
[3497.94 → 3499.68] This was about two years ago.
[3499.80 → 3506.56] I remember when we're looking at RabbitMQ, the image, in the context of running it, you know, at performance, at scale,
[3506.86 → 3507.82] what's the most you can get.
[3507.88 → 3509.94] And then you have the Erlang VM, so it's slightly different.
[3510.14 → 3516.10] But I do remember the Alpine-based images had all sorts of weird issues that the Ubuntu ones never had.
[3516.10 → 3517.62] Now again, this is the container image.
[3517.86 → 3518.68] This is not the host.
[3519.02 → 3522.64] So I'm really curious to try it out for myself and see what is different.
[3522.72 → 3523.08] Who knows?
[3523.26 → 3524.38] Performance could even be better.
[3524.58 → 3526.04] Which kernel version are you using, by the way?
[3526.20 → 3527.76] We are on the latest LTS.
[3527.98 → 3530.30] I think it's 5.10.62.
[3530.74 → 3531.14] Nice.
[3531.44 → 3531.76] Okay.
[3531.98 → 3532.24] Okay.
[3532.32 → 3535.30] We used to run, like, latest Linux kernel.
[3535.70 → 3538.62] And, you know, we still kind of go back and forth on what we should do.
[3538.62 → 3545.48] And I think we're now leaning more towards LTS because the changes that Linux sometimes introduces just causes us
[3545.48 → 3548.72] more headaches, especially when you're on the bleeding edge versions of it.
[3548.94 → 3552.80] But the latest LTS so far has been really, really great for us.
[3552.92 → 3558.98] We've been playing with the idea of maybe having LTS-style releases of Talos,
[3559.06 → 3561.62] which are pinned to LTS versions of the Linux kernel,
[3561.62 → 3566.58] and then having more edge versions, which are running the latest stable, not LTS.
[3566.58 → 3572.32] But today, you know, we're still playing with the overall strategy that we want to take long-term.
[3572.52 → 3575.70] And we just kind of settled on LTS for now because that's kind of a safe play.
[3576.24 → 3582.20] So speaking about LTS and strategy and roadmaps, anything interesting coming in the next six months?
[3582.48 → 3585.52] So between this Rubicon and the next one for Talos and Cozy?
[3585.52 → 3590.94] Yeah, I'd say the biggest one is this week we're announcing Lifespan, which is, I mean,
[3590.98 → 3594.54] I'm just super excited about this idea and I haven't even explained it yet.
[3594.94 → 3595.20] Okay.
[3595.20 → 3595.90] Yes, please.
[3596.56 → 3597.88] That sounds very interesting.
[3598.02 → 3598.20] Please.
[3598.36 → 3598.70] Yes.
[3598.88 → 3603.10] The idea is that since Talos can run practically anywhere,
[3603.42 → 3611.14] we're finding people want to bridge, say, bare metal clusters with instances running in the cloud.
[3611.14 → 3614.60] And so far, there hasn't been any good solutions for this.
[3614.94 → 3617.70] With Talos, we're kind of uniquely positioned since it's API-driven.
[3617.88 → 3618.90] We own the whole stack.
[3619.26 → 3621.12] We know we got Cozy managing the network.
[3621.12 → 3627.08] And so what we did is we went ahead, and we actually wrote a tooling to basically automate
[3627.08 → 3633.22] the key distribution and the peer discovery of WireGuard VPN.
[3633.22 → 3640.66] So I can spin up a cluster right here in my closet that's running on Raspberry Pis and extend
[3640.66 → 3644.94] that out to AWS really, really simply, really, really easily.
[3645.18 → 3651.86] And the latency is somewhere like, I think the latency that WireGuard adds is somewhere around
[3651.86 → 3652.52] a millisecond.
[3652.52 → 3655.12] And so it's, you know, it's negligible.
[3655.12 → 3661.74] But you get this consistent experience network-wise regardless of where you're running that particular
[3661.74 → 3662.12] node.
[3662.68 → 3665.22] Even the pod traffic can be routed over it.
[3665.42 → 3669.92] Kubernetes can actually be configured to purely talk over the WireGuard network.
[3669.92 → 3676.72] And so the idea with this long-term, the vision is that we're going to have users, customers
[3676.72 → 3681.60] that running in the data centre, bare metal, which is a large part of our user base.
[3681.78 → 3687.58] All of a sudden, they have an influx in traffic, and they need to expand the cluster, but they
[3687.58 → 3688.44] don't have the resources.
[3688.96 → 3689.50] Okay, fine.
[3689.58 → 3692.32] Let's just expand out to AWS momentarily.
[3692.48 → 3696.46] And when things calm down, we'll scale it back down to our core infrastructure or even
[3696.46 → 3698.80] another data centre, spill it over to another data centre.
[3698.80 → 3702.34] Now, a completely different use case, but very similar is maybe the Edge.
[3702.42 → 3708.10] I have some Raspberry Pis that I want to actually join up to a cluster at the core, which is
[3708.10 → 3710.26] hosted in AWS.
[3711.12 → 3717.56] But maybe these Raspberry Pis are running in shipping trucks, and they have, you know, intermittent
[3717.56 → 3719.00] network connectivity.
[3719.24 → 3722.86] That's kind of troublesome when you're talking about running the Kubernetes control plane.
[3722.96 → 3725.38] But a worker, you know, it can kind of go in and out.
[3725.38 → 3730.92] And, you know, I think the story there could be better on the Kubernetes side, but at least
[3730.92 → 3735.34] using WireGuard, as soon as they get any kind of networking, whether it's, you know, some
[3735.34 → 3741.60] Wi-Fi when they pull up to a store or mobile data, they can join the cluster with WireGuard
[3741.60 → 3745.04] and everything just seems as if they're right there on the same network.
[3745.38 → 3746.14] That's fascinating.
[3746.14 → 3748.62] So let me see if I understood this correctly.
[3748.96 → 3755.54] You're saying that you can scale out your Kubernetes clusters on demand, wherever, whether it's your
[3755.54 → 3760.32] closet or whether it's not the data centre or the cloud, you can maintain the same privacy
[3760.32 → 3761.10] of the network.
[3761.62 → 3762.34] Everything is encrypted.
[3762.64 → 3766.72] The data on those workers, you would think it's ephemeral data so that you don't store any
[3766.72 → 3768.88] state there so that you can scale back in.
[3769.24 → 3772.10] And Lifespan makes this seamless.
[3772.52 → 3773.30] Is that what you're saying?
[3773.30 → 3774.68] That's exactly what I'm saying.
[3775.12 → 3778.82] Of course, there's, you know, little caveats, like the way WireGuard roughly works is you
[3778.82 → 3781.30] need at least one direction of communication.
[3781.66 → 3786.74] So in the case of, say, my private cluster running right here in my closet, it needs to
[3786.74 → 3789.24] be able to at least reach the workers.
[3789.38 → 3791.32] The workers don't necessarily need to reach it.
[3791.44 → 3794.06] It can establish the channel that way.
[3794.62 → 3799.32] And so there are some, you know, limitations within the system you can find in the documentation
[3799.32 → 3801.80] stuff over my head when it comes to networking.
[3801.80 → 3804.80] Something around cones and gnats and stuff.
[3804.98 → 3807.02] Is it IPv4 or IPv6?
[3807.30 → 3808.44] What network does it lay down?
[3808.52 → 3809.20] Or dual stack?
[3809.36 → 3809.56] Either.
[3809.86 → 3810.12] Wow.
[3810.34 → 3810.66] Okay.
[3810.80 → 3811.74] I want to try it out.
[3812.02 → 3813.62] I want to try out how it actually works.
[3813.78 → 3814.44] It's pretty neat.
[3814.70 → 3818.88] In fact, one of our engineers, he just created a video of him just spinning up Talos right
[3818.88 → 3823.96] there in IMU, right there on his laptop and then joined an AWS Graviton instance to it.
[3824.38 → 3825.50] So it's pretty neat.
[3825.74 → 3826.82] I'm super excited about it.
[3826.92 → 3830.40] I will put that link in the show notes because that sounds like something which I would want to
[3830.40 → 3830.82] try out.
[3830.92 → 3831.66] That sounds amazing.
[3831.82 → 3832.06] Okay.
[3832.26 → 3832.50] Okay.
[3833.04 → 3836.64] So shifting focus a little bit towards Rubicon and what's happening this week.
[3836.76 → 3838.40] First, will you be attending in person?
[3838.66 → 3839.00] I will.
[3839.24 → 3839.86] I can't wait.
[3839.98 → 3840.22] You will.
[3840.32 → 3840.56] Okay.
[3840.78 → 3841.18] Amazing.
[3841.40 → 3842.84] What are you most looking forward to?
[3843.08 → 3843.62] Meeting people?
[3843.72 → 3844.18] Let me guess.
[3845.04 → 3846.58] I just want to see another human.
[3847.08 → 3848.74] That's exactly what it comes down to.
[3848.88 → 3849.16] Okay.
[3849.16 → 3851.06] No, actually, that is true.
[3851.16 → 3855.80] But more specifically, the thing that I'm really looking forward to is meeting everybody
[3855.80 → 3857.10] that works at Seder Labs.
[3857.28 → 3860.06] We've been fully remote for two years now.
[3860.14 → 3863.32] I think I've only met a couple of people that are currently at the company.
[3863.70 → 3867.32] And I just can't wait for us all to get together and just have dinner, you know, go to the
[3867.32 → 3868.20] bar, whatever.
[3868.34 → 3872.98] Just have a good time and actually not have to worry about seeing each other over pixelated
[3872.98 → 3874.76] streams and audio issues.
[3874.76 → 3879.60] So just seeing another human is going to be really nice and especially meeting everybody
[3879.60 → 3880.56] that's a part of the company.
[3880.82 → 3880.94] Wow.
[3881.32 → 3883.62] So this is two out of three people.
[3883.92 → 3888.84] Actually, both people that go to Rubicon in person, you and William Morgan, you're both
[3888.84 → 3890.14] looking forward to the same thing.
[3890.72 → 3894.48] William Morgan from Linked from Boolean, he was saying the same thing, like meeting the
[3894.48 → 3898.26] rest of his company, meeting the community and meeting another human being.
[3898.34 → 3899.56] Like he's really looking forward to that.
[3899.68 → 3900.46] So, okay.
[3900.46 → 3902.84] I think everybody, everybody's on the same page.
[3902.84 → 3908.08] And I have to say that those that couldn't make it in person, myself including, we wish
[3908.08 → 3908.78] we could be there.
[3908.98 → 3912.48] But by the time EU comes along, I'm sure things will be easier.
[3912.72 → 3917.28] And then next year for the next Rubicon, North America, I hope to be there in person and meet
[3917.28 → 3921.68] all the great people that, you know, Rubicon is so big, like you can never meet everybody
[3921.68 → 3922.46] that you want to.
[3922.82 → 3925.60] But at least there will be fewer people this year.
[3925.64 → 3928.58] So it will be a bit better for meeting in person.
[3928.82 → 3928.92] Yeah.
[3929.22 → 3932.66] And, you know, speaking of EU, we will be there as well, too.
[3932.66 → 3934.96] So, you know, we can see each other than.
[3935.20 → 3935.46] Amazing.
[3935.62 → 3935.82] Okay.
[3936.02 → 3936.28] Yes.
[3936.62 → 3936.82] Take.
[3937.52 → 3942.54] So what advice do you have for the people that can't attend the conference in person?
[3942.70 → 3943.88] Anything that you recommend to them?
[3944.18 → 3948.24] You know, nothing I think that you're not going to get from the CNCF as far as their
[3948.24 → 3949.04] recommendations go.
[3949.16 → 3950.24] Attend the virtual booths.
[3950.68 → 3953.24] I would say join the CNCF Slack.
[3953.44 → 3958.68] That was really fun when I did Rubicon EU, just talking to people and just all kinds of
[3958.68 → 3959.46] random channels.
[3959.70 → 3960.72] That was a blast.
[3960.72 → 3965.84] It did a decent job of giving me that, you know, camaraderie that I wanted, that you're
[3965.84 → 3967.18] looking for when you go to Rubicon.
[3967.30 → 3970.24] So I'd say that that's the you should sign up for that immediately.
[3970.52 → 3970.80] Okay.
[3971.14 → 3973.50] And what about the people that want to do catch up videos?
[3973.50 → 3977.38] Because for example, it may be too late in the night for them, and they can't, you know,
[3977.64 → 3978.90] be up all hours.
[3979.14 → 3980.48] Anything you would tell them?
[3980.92 → 3984.20] Set aside enough time because there are a lot of really cool things.
[3984.20 → 3988.78] And just try to prioritize and, you know, because you're not going to get through all of them.
[3989.16 → 3993.26] Figure out the ones that probably are most applicable to you, things you're most excited
[3993.26 → 3996.08] about and, you know, just have fun watching them.
[3996.28 → 3998.26] Speaking about that, which talks are you excited about?
[3998.46 → 3999.34] Anything in particular?
[3999.68 → 4005.56] I've noticed my taste has changed ever since I've become into a role where I'm playing more
[4005.56 → 4007.46] of a management role and business role.
[4007.46 → 4011.22] I do get hands-on technically, but less and less so over time.
[4011.50 → 4017.06] So I'm finding myself gravitating more towards things like, you know, building community.
[4017.30 → 4021.86] There's a particular talk on how to make contributors, maintainers, building your brand,
[4022.24 → 4022.96] stuff like that.
[4023.22 → 4024.46] Technical stuff.
[4024.80 → 4030.26] There is one on supply chain that I want to go look at, but I am reserving a lot of time
[4030.26 → 4032.84] for just talking to people as well.
[4033.02 → 4036.48] So I'll maybe grab a few, but you know, they're going to be less technical.
[4036.48 → 4036.92] Okay.
[4037.28 → 4038.54] Well, Andrew, this has been a pleasure.
[4038.70 → 4040.36] I'm really glad that we had this opportunity.
[4041.02 → 4045.62] Rubicon EU just flew by, and I didn't have time, but now I'm so glad that we had this
[4045.62 → 4046.48] time together.
[4046.80 → 4051.08] I'm really looking forward to trying Talos OS, to trying Hero and seeing Cube span.
[4051.20 → 4052.28] How well does it work in practice?
[4052.60 → 4055.22] Thank you very much for sharing all these amazing things with us.
[4055.46 → 4055.62] Yeah.
[4055.64 → 4056.38] Thank you for having me.
[4056.44 → 4057.54] It was a blast.
[4066.48 → 4076.48] This episode is brought to you by our friends at Ray gun.
[4076.74 → 4079.06] Have you ever wondered how users are really experiencing your software?
[4079.36 → 4083.38] When you unlock real user insights, you'll be able to identify and resolve front-end
[4083.38 → 4087.66] performance issues and ensure your application is consistently delivering superior experiences.
[4088.04 → 4092.12] Ray gun will deliver a daily performance summary to keep your finger on the pulse of your website
[4092.12 → 4097.70] with an overview of your slowest pages, Core Web Vitals, user sessions, and user satisfaction.
[4098.20 → 4101.10] This gets sent straight to your inbox or Slack channel of your choice.
[4101.46 → 4106.08] Join thousands of performance-focused, customer-centric software teams who use Ray gun every single
[4106.08 → 4108.56] day to deliver flawless experiences to their customers.
[4108.56 → 4127.42] So, Rubicon is my favourite time to catch up with the cloud-native community, with the people,
[4127.64 → 4129.52] with the events, new features, new products.
[4129.64 → 4131.44] It's such an eventful time, Rubicon.
[4131.52 → 4131.92] I love it.
[4132.26 → 4133.14] But also new beginnings.
[4133.64 → 4136.04] So, we only spoke, was it like a month ago?
[4136.44 → 4137.38] It wasn't that long.
[4137.38 → 4138.62] Episode 18.
[4138.90 → 4140.04] Yes, it was.
[4140.20 → 4142.00] Around four or five weeks ago, I think it was.
[4142.30 → 4144.82] And you have been really busy in this one month, right?
[4145.36 → 4146.70] So, tell us about it.
[4146.72 → 4148.00] What happened in the last month?
[4148.16 → 4152.80] Well, we brought a new person into this world, which has been rather time-consuming.
[4153.44 → 4158.24] So, I can't remember if we spoke about this during the last one, but my wife was pregnant.
[4158.76 → 4161.80] And now we have a beautiful baby boy who's entered this world.
[4161.94 → 4163.00] His name is Caleb.
[4163.40 → 4165.60] He is two weeks and five days old.
[4165.60 → 4170.34] And because that wasn't enough change in a short period of time for me, I also decided,
[4170.52 → 4170.88] you know what?
[4171.06 → 4171.40] Screw it.
[4171.44 → 4172.70] Let's change jobs as well.
[4172.88 → 4176.08] So, the last time we spoke, I was working Equinix Metal.
[4176.38 → 4179.06] And I am now a developer advocate for Plum.
[4179.06 → 4183.98] So, I think that this is going to be my favourite announcement from this Rubicon, which is the
[4183.98 → 4188.04] newest and youngest member of the cloud native community, Caleb.
[4188.40 → 4190.84] He's, what, two weeks, three weeks?
[4191.02 → 4191.74] Two weeks, five days.
[4191.84 → 4192.00] Yeah.
[4192.14 → 4196.10] Well, I don't think there's a younger member of the cloud native community.
[4196.24 → 4196.96] So, two weeks?
[4197.44 → 4198.78] That's just, and five days, he said.
[4199.02 → 4199.80] That's just crazy.
[4200.30 → 4200.88] So, okay.
[4200.88 → 4204.86] Well, he will be watching some of the Rubicon festivities and talks remotely with me.
[4204.98 → 4208.22] Obviously, in the UK, we are travel banned until November 1st.
[4208.24 → 4212.86] So, I will be participating as much as I can through my laptop and through the video material.
[4213.52 → 4216.62] And I'm sure Caleb will be throwing up on me for a good few of those sessions.
[4217.30 → 4219.50] Or falling asleep, I would like to think, right?
[4219.54 → 4221.20] Like, during those boring sessions.
[4221.66 → 4222.24] No, not boring.
[4222.36 → 4223.30] Boring to him, obviously.
[4223.68 → 4225.44] He'll be like, Kubernetes what?
[4225.44 → 4227.40] He'll just, like, fall asleep.
[4227.70 → 4229.58] Like, spiffy this and spiffy that.
[4229.68 → 4231.54] Yeah, that sounds like a nice nursery rhyme.
[4231.64 → 4234.66] So, anyway, I just thought about this.
[4234.96 → 4243.04] This is maybe the best strategy to shift your body clock, the West Coast time zone, without actually travelling, right?
[4243.24 → 4247.38] Because a new baby will keep you awake through the night.
[4247.56 → 4250.20] So, you can watch all the talks and you'll be awake.
[4250.40 → 4253.14] So, I haven't thought about this, but this is genius, David.
[4253.50 → 4253.82] Yeah.
[4253.82 → 4258.14] And not exactly clocking in, you know, my regular seven or eight hours sleep at all.
[4258.40 → 4263.90] So, you know, why not spend some of those times awake catching up with some great cloud-native material and stuff like that?
[4264.00 → 4264.54] Yeah, it'll be good.
[4264.66 → 4266.02] And, of course, you know, it's Rubicon.
[4266.20 → 4268.80] So, it's been remote for the last four editions.
[4268.96 → 4271.10] I think that this is the fourth remote one since the pandemic.
[4271.38 → 4277.12] So, you know, the hallway track on Slack and Discords and Twitter, always Twitter, is always very active.
[4277.28 → 4279.94] So, there's always something to keep your company during those late nights.
[4279.94 → 4282.58] So, which is your process of joining remote Rubicons?
[4282.70 → 4283.40] Tell me about it.
[4283.82 → 4287.48] And then I can share you my process and see how it compares to yours.
[4287.86 → 4288.48] How do you do it?
[4288.70 → 4292.08] Well, I wish I could say I was really, you know, methodological about it.
[4292.14 → 4294.32] And I knew exactly what talks I was going to watch each day.
[4294.44 → 4295.34] But I don't.
[4295.42 → 4299.88] I really just kind of show up and log into the platform and see what's happening then and there.
[4299.88 → 4302.94] I definitely watch a lot of it after Rubicon.
[4303.12 → 4304.70] So, I can do the 2x on YouTube.
[4304.92 → 4309.58] I am very guilty of 2xing a lot of these sessions and slowing down as required.
[4309.78 → 4312.44] But I do try to catch a few things live as much as possible.
[4312.72 → 4318.18] And it's really just, especially with having a young one right now, my method is going to be slightly different from previous Rubicons.
[4318.18 → 4319.68] So, I'm really just taking it day by day.
[4319.90 → 4321.32] We're on a DCTL event right now.
[4321.78 → 4322.52] I'm logging on.
[4322.64 → 4324.26] I'm going, okay, I've got 40 minutes.
[4324.34 → 4325.28] What can I catch right now?
[4325.42 → 4327.12] And just trying to do as much as I can at the moment.
[4327.26 → 4329.86] But it's not as well planned as I would expect.
[4329.96 → 4332.62] I'm sure you've got it down to the letter, right?
[4332.72 → 4335.22] You must know exactly every session you're going to check out.
[4335.22 → 4336.76] Yeah, something like that.
[4336.84 → 4337.44] Something like that.
[4337.52 → 4339.66] So, actually, I try to drop in all of them.
[4340.00 → 4342.48] I'm making use of three monitors plus an iPad.
[4342.80 → 4345.34] I have a picture from the last Rubicon that I attended.
[4346.04 → 4348.32] And then I just watch three sessions and I mute.
[4348.68 → 4352.98] And I just pick one, listen for a few minutes, then switch to another one, switch to another one.
[4353.16 → 4355.30] And that's how I just consume three at the same time.
[4355.60 → 4360.44] And then when something is, you know, I mean, it's interesting, but maybe there's something more interesting.
[4360.60 → 4361.64] I just switch to another one.
[4361.84 → 4363.00] But I can consume three.
[4363.26 → 4364.12] That's my max.
[4364.12 → 4365.98] I think four will be a bit challenging.
[4366.32 → 4371.60] When it comes to the sessions, like I don't pick them like ahead of time because the titles and descriptions can be misleading.
[4372.06 → 4374.44] I try to drop in on them as you would do.
[4374.68 → 4376.08] And then I just pick and choose.
[4376.14 → 4379.56] But I try to drop on all three of them, which is impossible if you're in person.
[4380.02 → 4384.00] So I think this is the best way to do it virtually when it comes to consuming the talks.
[4384.22 → 4388.48] But what about interacting with the Rubicon, the rest of the attendees?
[4388.62 → 4390.62] How do you do that or do you even do that?
[4390.92 → 4392.78] Yeah, I do try and remain active.
[4392.78 → 4394.48] I'll go back to the schedule first.
[4394.64 → 4395.84] Actually, just a little bit on that.
[4396.16 → 4400.62] So you're not the first person I've heard who has multiple talks running at the same time.
[4400.70 → 4402.02] There's a community member, Noel Georgie.
[4402.10 → 4402.34] Okay.
[4402.46 → 4404.86] Who does four or five talks at the same time as well, flicking between them.
[4405.14 → 4405.96] I don't know how you do it.
[4406.00 → 4407.42] I'm a complete single tasked.
[4407.60 → 4410.64] I just don't have the focus or attention plan to do multiples.
[4411.14 → 4412.52] So mad respect there.
[4412.52 → 4415.78] But I'm always following the operations track mostly, this Rubicon.
[4415.94 → 4419.96] As I was the chair of that track, I helped select all the talks that you're going to see.
[4420.06 → 4420.62] Oh, wow.
[4420.72 → 4421.64] I didn't know that.
[4421.90 → 4422.18] Yeah.
[4422.22 → 4423.58] I don't think I've actually told anyone.
[4423.80 → 4425.80] I didn't even really talk about it on Twitter either.
[4426.18 → 4426.76] But I did share that.
[4426.76 → 4427.50] That's amazing.
[4427.94 → 4428.28] Wow.
[4428.38 → 4429.58] I helped pick all the talks.
[4429.76 → 4432.82] If you don't like them, it's sadly my fault and one other person.
[4433.04 → 4434.74] But it should be a pretty good Rubicon.
[4434.74 → 4435.18] Right.
[4435.76 → 4436.16] Okay.
[4436.70 → 4438.80] Well, then that means that you know all the talks.
[4439.02 → 4440.08] Well, not all the talk.
[4440.26 → 4445.64] Like, you have a good idea of the talks, of what are coming, the themes, the speakers.
[4446.24 → 4446.84] That's amazing.
[4447.08 → 4449.28] Anything that you would recommend in particular?
[4449.44 → 4452.90] Something that resonated with you from that track?
[4453.02 → 4453.26] Yeah.
[4453.32 → 4455.68] I think my bias definitely helped towards some of the selection.
[4455.90 → 4459.10] You know, I've got an affinity for Git Ops and infrastructure as code.
[4459.10 → 4463.32] So there are a lot of perfect sessions that feature using Argo for deployment.
[4463.32 → 4464.86] You know, we talked about that last time.
[4465.06 → 4466.48] I think we're both fans of the project.
[4466.62 → 4470.70] And we're just seeing more and more sessions submitted on Argo every single year.
[4470.82 → 4472.48] And it's just because of the demand.
[4472.64 → 4475.94] People want to be able to do this automated, Git Ops-style-based deployment.
[4476.08 → 4477.28] So you'll see a lot of sessions there.
[4477.50 → 4482.02] A lot of sessions on infrastructure as code, but Terraform and Cross plane really popular this year.
[4482.08 → 4486.70] We've seen a lot, a lot of submissions talking about Cross plane, which is great to see.
[4487.20 → 4491.68] And of course, there are a few Plum sessions in there from some of my teammates, my new teammate Plum as well.
[4491.68 → 4492.10] I see.
[4492.10 → 4492.72] I see.
[4492.86 → 4493.10] Okay.
[4493.32 → 4493.62] Okay.
[4494.18 → 4497.72] So when it comes to Git Ops, Flux or Argo?
[4497.86 → 4498.46] What do you think?
[4498.70 → 4500.40] Oh, I'm so on the fence.
[4500.56 → 4501.76] I actually use both.
[4502.00 → 4504.06] I really love the simplicity of Flux.
[4504.18 → 4505.80] It just seems to work.
[4506.08 → 4509.96] But I love the Argo UI, and I wish I could merge them together somehow.
[4510.48 → 4513.36] Well, previously we said, I mentioned that Flux are working on a UI.
[4513.52 → 4514.44] It's still super early.
[4514.58 → 4516.42] I don't recommend people use it yet.
[4516.50 → 4517.38] There are many, many bugs.
[4517.38 → 4523.18] But I do tend to use Flux, but I'm getting more familiar and comfortable using Argo.
[4523.18 → 4534.20] I think the challenge I've found with Argo is the custom resources are slightly more complicated, especially when you have to adopt the app of apps models, which is an app to deploy an app which has sub-apps.
[4534.20 → 4537.38] And I haven't really got my head around that completely.
[4537.38 → 4541.62] I'm not as fluent with it as I am with Flux, but I definitely think both tools are really great.
[4541.78 → 4543.42] I don't think you can go wrong with using either.
[4543.56 → 4547.36] I think it comes down to just whatever one you've used first, whatever one you're comfortable with.
[4547.56 → 4547.66] Yeah.
[4547.74 → 4548.50] Yeah, both great projects.
[4548.72 → 4548.88] Yeah.
[4548.88 → 4552.10] So it's a matter of trying them, I suppose, and see what works for you.
[4552.28 → 4553.40] That's one of my favourites.
[4553.60 → 4556.08] Well, we got this announcement, was it two years ago?
[4556.14 → 4561.52] Maybe you'll remember, but the team was into it, I think, were the original creators of Argo.
[4562.16 → 4569.28] And Flux came out of WeWork's, and they had this big joint announcement where they said they were going to consolidate both the tools to give us one Git Ops tool to rule them all.
[4569.34 → 4570.92] And it was going to be called the Git Ops toolkit.
[4571.28 → 4572.16] It never really happened.
[4572.16 → 4577.36] And now we're back to this divergence era where we have multiple tools kind of trying to fulfill the same thing.
[4577.36 → 4578.76] Yeah, 2019.
[4579.00 → 4581.68] I was actually there at that Rubicon, and I was so excited.
[4581.96 → 4583.38] That was also the North America one.
[4583.86 → 4586.46] And I would like to dig more into that to see why that happened.
[4586.82 → 4589.60] I didn't get the chance to speak to the Flux team.
[4589.82 → 4590.68] They're, like, on my list.
[4590.82 → 4591.50] They really are.
[4591.60 → 4593.16] But it's, like, you know, too many things happening.
[4593.46 → 4594.62] But the day will come.
[4594.66 → 4595.78] There's a Git Ops days, I think.
[4595.84 → 4599.08] There's, like, a summit coming or, like, next week, I believe.
[4599.32 → 4599.58] Maybe.
[4599.78 → 4600.64] I can't remember exactly.
[4600.88 → 4601.72] Yeah, something like that.
[4601.76 → 4602.94] Like, it's happening as well.
[4603.20 → 4605.16] And that will be an interesting one to watch.
[4605.16 → 4612.82] But I would really like to understand what happened there with Flux and Argo and what are the strengths and the weaknesses of one versus the other.
[4612.90 → 4614.40] The UI, that's, like, a good one.
[4614.72 → 4618.70] I do have to say, even though I have tried Argo, I haven't tried Flux.
[4619.18 → 4625.10] So this GitHub Summit, which is coming, I'm hoping I'll be able to try it out in that context.
[4625.20 → 4625.96] I'm looking forward to that.
[4626.08 → 4626.20] Okay.
[4626.20 → 4633.04] I think Flux shines a bit better when it comes to being a bit more agnostic on the tools that you want to use to actually generate the YAML.
[4633.30 → 4636.24] Like, you know, not all of our Git Ops repositories are straight YAML manifests.
[4636.58 → 4641.52] And we're using tools that customize or the Carvel dev tools, or we're using Capital.
[4641.92 → 4643.14] Like, there's so much choice there.
[4643.30 → 4646.60] You know, decision fatigue is real, especially in the cloud-native landscape.
[4646.94 → 4651.98] So Flux makes it a lot easier to say, I want to use a tool to generate the manifest before we do the apply stage.
[4652.14 → 4655.28] With Argo, I think it's a little bit more convoluted.
[4655.28 → 4658.18] There has to be a concept of, like, a provider, if I remember correctly.
[4658.58 → 4659.62] And they're not all supported.
[4659.86 → 4661.50] But that could have changed since the last time I looked.
[4661.74 → 4662.02] Cool.
[4662.50 → 4662.80] Okay.
[4663.14 → 4664.40] I definitely have to follow up on that.
[4664.44 → 4665.14] So thank you for that.
[4665.26 → 4665.52] Thank you.
[4665.56 → 4666.36] I really appreciate it.
[4666.66 → 4669.98] In the context of Rubicon coming back, so there's the operations track.
[4670.28 → 4671.92] Any other track that you're excited about?
[4672.10 → 4672.54] All of them.
[4672.64 → 4680.38] I think I'm in a really unfortunate position, which you probably are as well, is that, you know, we need to really stay on top of a lot of this, you know, as well as our day jobs.
[4680.86 → 4684.96] We have our extracurricular activities where we need to be knowledgeable in a lot of these domains.
[4684.96 → 4690.58] So I really am watching all the tracks as much as possible and 2x in all the talks on YouTube.
[4690.80 → 4696.18] But anything to do with continuous integration and delivery is something that I'm really keen on following talks with.
[4696.50 → 4697.52] Infrastructure of code.
[4697.86 → 4700.22] Infrastructure as code, of course.
[4700.22 → 4702.26] Definitely loving tools that are doing this.
[4702.50 → 4717.38] And one of the reasons I joined Plum is just because it directly is everything I love doing with platforms, which is taking the primitive tools that we have, like Flux and Argo and Kubernetes and cloud providers, and being able to give developers a platform to deploy their applications.
[4717.38 → 4720.82] And my interest, Plum's interest are just the same there.
[4721.06 → 4724.08] So infrastructure of code, continuous integration, continuous delivery.
[4724.72 → 4727.34] Those are the main things I want to see from Rubicon this year.
[4727.70 → 4734.34] So I would like to dig into that a little bit more because that's like the other big thing that changed in the last month for you, the new job with Plum.
[4734.54 → 4737.96] I think Kat Cosgrove, is she there as well at Plum, I believe?
[4737.96 → 4741.50] Yes, Matty Stratton, Kat Cosgrove, and Laura Santa maria.
[4741.86 → 4742.68] They're my teammates.
[4742.86 → 4744.90] They're the developer advocacy team at Plum.
[4745.58 → 4749.16] And I'm joining in with some great people there, definitely.
[4749.46 → 4750.64] Yeah, a big shout-out to them.
[4751.00 → 4752.62] That was the first thing which I wanted to do.
[4752.94 → 4758.10] And the second thing is asked you, as I asked you before, why Plum specifically?
[4758.40 → 4758.98] Why Plum?
[4759.14 → 4760.10] Could you see this one coming?
[4760.18 → 4761.34] Tell me, let's be honest.
[4761.38 → 4762.28] Did you see this one coming?
[4762.38 → 4763.30] Of course, of course.
[4763.40 → 4763.68] Okay.
[4763.68 → 4768.94] I always look back at my career, and I've always worked for relatively small shops.
[4769.18 → 4772.90] You know, every time I write a line of code, I've always been responsible for the deployment of production.
[4773.14 → 4776.50] I've never had that throw over the wall scenario because of silence.
[4776.96 → 4781.54] So, you know, infrastructure as code and continuous integration and deployment, these are just things I've always had to do.
[4781.66 → 4783.58] I've never been able to dodge that bullet, unfortunately.
[4783.94 → 4788.48] So, you know, I think I cut my teeth like the rest of us using Terraform and HCL.
[4788.90 → 4791.22] And I think Terraform is a fantastic tool.
[4791.58 → 4793.18] No one's ever going to say otherwise, right?
[4793.18 → 4801.62] But there has some really rough edges when it comes to programmatically defining some elements of it, like nodes in a cluster or doing loops or conditionals.
[4801.72 → 4805.60] These things get a little bit tricky because of the constraints of the HCL language.
[4805.92 → 4809.58] Now, I know with Terraform 0.10, they started to bring in some of these primitives.
[4809.80 → 4815.72] But, you know, these primitives already exist in high-level programming languages, which is where Plum shines.
[4815.88 → 4820.62] It comes in and says, well, you can just define your resource graph using the language that you're familiar with.
[4820.80 → 4821.88] I'm a big fan of Go.
[4821.88 → 4823.08] I'm a big fan of TypeScript.
[4823.24 → 4824.66] They're both options available to me.
[4824.98 → 4827.52] But Plum also supports any of the .NET languages.
[4827.72 → 4828.54] It supports Python.
[4829.02 → 4830.28] And I'm sure there are other things coming.
[4830.40 → 4835.14] And there's some really cool announcements that I managed to sneakily find out just yesterday coming at Rubicon.
[4835.14 → 4841.34] So there's just all those languages that already have loops, conditionals, the ability to provide a single function.
[4841.40 → 4842.64] This is my favourite thing in Plum, right?
[4842.70 → 4844.64] Sorry, I'm going a little bit scour bred here.
[4844.74 → 4847.70] But being able to see, I want a Kubernetes cluster on GCP.
[4847.90 → 4849.96] And I want different node pools that look like this.
[4850.02 → 4851.04] And I want a load balancer.
[4851.24 → 4854.56] And I want some applications deployed to that cluster as part of the bootstrap process.
[4854.74 → 4856.96] Now, I could do that as an HCL Terraform module.
[4856.96 → 4864.72] But as a TypeScript Plum application, I can actually make that a function call, publish it to NPM, and then anyone can pull that in.
[4864.84 → 4874.64] You can literally do NPM install raw code, my super Kubernetes cluster package, call that function as many times as you want, get all these clusters with everything encapsulated in that way.
[4874.92 → 4876.20] And I just think that is a superpower.
[4876.20 → 4884.30] And I think, you know, once you see that, and you start to use that approach, looking at more abstractions like HCL or YAML, you're just like, why?
[4884.56 → 4892.40] Why am I constraining myself to the opinions and the subjective nature of other people that think that's the best way to do it when my experience may be slightly different?
[4892.74 → 4895.36] And programming languages are the best way to encapsulate that knowledge.
[4895.78 → 4898.90] So this is fascinating from multiple perspectives.
[4898.90 → 4906.90] I see a couple of products, tools, however you want to call them, enter this space in recent months.
[4907.12 → 4912.08] One which is top of my mind, which is, by the way, an episode that's going to ship, I think, this week.
[4912.38 → 4915.68] I mean, by the time we're listening, it'll be like a few weeks back, Dagger.
[4916.10 → 4919.40] And I really like how they're making use of Q and Build Kit.
[4919.94 → 4925.02] So Q as a language to define these things sounds fascinating.
[4925.02 → 4929.74] So I'm wondering how does Q compare to HCL and Plum?
[4930.02 → 4945.58] Plum in the case of Plum being like the actual programming language versus something like Cross plane, which is supposed to be your control cluster, which then you define your compositions and your, there's something else we call them, I forget, compositions.
[4945.82 → 4946.68] And it's not an abstraction.
[4947.06 → 4947.90] Do you remember what it is?
[4948.08 → 4949.52] There's a composition in Cross plane.
[4949.52 → 4950.70] Yeah, the XRDs.
[4950.94 → 4955.80] So you can actually have a single resource that then creates multiple subresources below it.
[4955.90 → 4958.86] So yes, I think they do call them compositions or XRDs.
[4959.28 → 4959.54] Yeah.
[4960.08 → 4961.02] And there's like another name.
[4961.08 → 4964.16] So there's just like two things, like the compositions are like the things that you combine them in.
[4964.32 → 4966.76] But they have these providers, they interact with all the IAS's.
[4967.14 → 4968.38] You can declare your YAML.
[4968.50 → 4976.08] So you declare your GK cluster right in Google and just like makes it happen and all the other things that you want within that IAS.
[4976.08 → 4978.10] And it works across IAS's.
[4978.24 → 4981.84] So I'm wondering, how does Plum compare to Cross plane?
[4982.18 → 4983.02] Let's start with that.
[4983.46 → 4989.66] And how does Plum compare with Dagger, which is using Q rather than a programming language?
[4990.08 → 4993.52] And Q, I mean, it is kind of programming language, but it's more like a data language.
[4993.60 → 4994.42] That's the way I see it.
[4994.44 → 4997.82] And I know that you know a bit more about Q with Brian Kettle son.
[4998.20 → 5000.08] You have blocks, Q blocks.
[5000.32 → 5003.34] Yeah, Brian Kettle son and I are the creators and maintainers of Q blocks.
[5003.34 → 5005.88] So we're both huge fans of Q.
[5006.00 → 5014.72] We think it's just a great language for defining schema, applying constraints, and even doing some basic comprehensions and, you know, mathematics within.
[5014.90 → 5020.96] So it's not touring complete programming language, but they are starting to add more query APIs and other things to bring it in line with some of that.
[5021.34 → 5022.34] So I really like Dagger.
[5022.58 → 5027.20] I have done an episode with Solomon on Lockwood Live where we dug into Dagger, and we did some deployments.
[5027.26 → 5028.34] And I think it's a perfect tool.
[5028.46 → 5030.26] I love seeing Q used in this way.
[5030.26 → 5041.26] It's very similar to Terraform in the regards of that you have to have something that understands the abstract form, the HCL, the YAML, or even the Q, which is just compiling down to YAML at the end of the day anyway.
[5041.76 → 5045.72] So you're still constrained in that you can't do a lot of conditional logic.
[5046.14 → 5049.04] Loop logic does exist in Q and you can do some things like that.
[5049.04 → 5054.12] But then modifying things within the loop gets a little bit difficult because you've only got access to the Array account and things like that.
[5054.30 → 5056.48] So, you know, it depends on your use case.
[5056.58 → 5061.80] But I think Dagger is great in that they're moving beyond into, like, where Boundary is as well.
[5061.90 → 5066.06] I'm not sure if you're familiar with HashiCorp's Boundary, but it's like that second step.
[5066.18 → 5071.94] It's like, okay, we provide the platform or the infrastructure, but what about the applications that then belong and live on that application?
[5071.94 → 5076.76] And that's where Boundary comes in, fulfilling the continuous delivery component of your application.
[5077.14 → 5082.42] And Dagger can move right into that and provides, like, a single interface to all of it, which I think is really, really cool.
[5082.80 → 5084.96] But the constraints are still there, very similar to HCL.
[5085.42 → 5086.90] Cross plane things get fascinating.
[5087.30 → 5090.04] Cross plane still has defined, you're still constrained by YAML.
[5090.18 → 5093.12] Like, you can only say so much that's not programming.
[5093.30 → 5098.12] So you're not going to be able to provide a function that does a thing, but you can provide a composite resource that does a thing.
[5098.12 → 5102.04] What I really love about Cross plane is that continuous reconciliation.
[5102.38 → 5105.16] This is something that Plum doesn't do yet.
[5105.38 → 5106.84] That's one of the first things I want to change.
[5106.94 → 5109.74] Like, I'm going to be into Plum, and I'm going to be like, we need to get into this space.
[5109.88 → 5114.00] We have to control the actual reconciliation and not just the client-side reconciliation.
[5114.32 → 5116.16] So I think Cross plane is killing it there.
[5116.28 → 5119.54] I don't think any other product is as good as Cross plane in that regard.
[5119.68 → 5125.24] The fact that I can have that controller running in my Kubernetes cluster, if I delete an S3 bucket, it's going to be recreated.
[5125.52 → 5127.84] Now, of course, there are things that can happen there that are bad.
[5127.84 → 5132.06] It could be data in that S3 bucket, and you may have to build workflows onto it to restore from a backup.
[5132.28 → 5134.02] These are not things that really happened yet.
[5134.56 → 5136.92] Cross plane is going to slide around to that, and I know they are because they're a great team.
[5137.18 → 5137.92] Cross plane is great.
[5138.42 → 5140.78] Got a reconciliation look, Kubernetes event model.
[5141.04 → 5142.84] Going to be a lot familiar to people.
[5143.30 → 5144.82] They're going to be really happy with that approach.
[5145.18 → 5150.46] I want to see Plum do more of that, control the execution of Plum and not just have it client-side.
[5150.76 → 5151.74] And Dagger is great.
[5151.92 → 5153.66] Solomon and the team are fantastic.
[5153.66 → 5157.78] But you're still, it's not a programming language, but you can still do some really cool things with Q.
[5157.78 → 5167.44] I think where Dagger is really going to excel is that something that's difficult to do with Terraform and even difficult to do with Cross plane is that you have to have the provider first.
[5167.94 → 5173.76] Dagger has made it really easy to provide really superficial providers by just taking the Q and saying, this is what I need to do with this code.
[5173.98 → 5175.54] It's a very small amount of goal.
[5175.84 → 5176.84] There's not a lot of boilerplate.
[5177.04 → 5179.50] And I think we'll see a lot of adoption because of that.
[5179.50 → 5185.64] But hopefully Plum is in a well-positioned place to try and help on both of those fronts as well.
[5185.88 → 5197.64] The other tool that I've seen take a similar approach is CDK from Amazon, where you get to declare your infrastructure using a higher level language.
[5198.00 → 5203.48] TypeScript, I know that's something which is pushed at Amazon, which makes sense with CDK.
[5203.68 → 5204.74] I've used it briefly.
[5205.20 → 5205.90] It was okay.
[5206.10 → 5208.54] Way better than using the YAML alternative.
[5208.54 → 5213.34] That was like the most horrible YAML I've seen in my life, where you get to do like ink, which is the function.
[5213.48 → 5216.06] You get two arguments, which are defined like in an array.
[5216.24 → 5220.90] And then you get an operation, which, you know, you capture the result, and then you reuse that result as a variable.
[5221.02 → 5221.66] That was horrible.
[5221.76 → 5222.74] And all defined in YAML.
[5222.94 → 5223.90] That was crazy.
[5224.22 → 5225.56] That was the craziest YAML I've seen.
[5226.14 → 5228.78] So CDK was better in that respect.
[5228.84 → 5230.36] So I can see some similarities there.
[5230.54 → 5232.84] It's interesting that you run it client-side.
[5233.14 → 5237.64] And when you say client-side, I imagine the CI could run it as well if it has all the secrets.
[5237.64 → 5240.92] But still, it's not built into the product.
[5241.58 → 5242.40] So that's interesting.
[5242.66 → 5243.74] Maybe there is a Plum cloud.
[5243.92 → 5244.28] I don't know.
[5244.32 → 5244.64] I haven't.
[5244.72 → 5247.32] I don't know enough about Plum is what I'm getting at.
[5247.58 → 5249.78] And also what I'm getting at is I would like to find out more.
[5249.90 → 5251.60] So you know what the follow-up is, right?
[5251.94 → 5252.22] Yeah.
[5252.64 → 5254.32] CDK is a really cool tool.
[5254.40 → 5255.58] And it's very similar to Plum.
[5255.58 → 5257.06] It doesn't have the provider support.
[5257.18 → 5259.64] It doesn't support the Terraform providers out of the box.
[5259.78 → 5262.26] Kind of like what Plum tries to do with their generators.
[5262.46 → 5263.22] The CDK is awesome.
[5263.34 → 5267.90] And I think what really excels here is that Plum and CDK shine when you're using TypeScript.
[5268.12 → 5272.98] I think it's such a great language for infrastructure as code because it's strictly typed.
[5272.98 → 5278.26] You can have interfaces that you can define for the different properties that you need to get out to expose output variables.
[5278.38 → 5279.70] You're just using the export keyword.
[5279.98 → 5282.56] Like all of these things just TypeScript is just great.
[5282.66 → 5287.98] I think if you haven't tried to do any infrastructure as code using TypeScript with CDK or Plum, you should just go try it.
[5288.08 → 5288.66] It's so cool.
[5289.08 → 5295.58] And the way that the node ecosystem in TypeScript allows you to pass functions around or, you know, the first class, they can be exported.
[5295.88 → 5296.76] They can be renamed.
[5296.86 → 5297.44] They can be bound.
[5297.52 → 5298.36] They can be higher order.
[5298.44 → 5299.70] You can pass function within the functions.
[5299.70 → 5301.52] The flexibility there is phenomenal.
[5301.70 → 5305.60] So I encourage everyone to try TypeScript first before going to any of the other languages.
[5306.20 → 5307.10] But not you.
[5307.54 → 5308.36] You're Go, right?
[5308.64 → 5310.66] I do most of my Plum in TypeScript.
[5311.02 → 5312.36] I have started doing it in Go.
[5312.60 → 5314.12] And I just, it's not as nice.
[5314.28 → 5318.16] Error checking all the time is still very present in Plum Go.
[5318.66 → 5320.28] So I do stick to TypeScript, actually.
[5320.64 → 5327.26] I actually, when I was working at Equinix Metal, I handled all the Tinker bell CCD infrastructure using Plum with Go.
[5327.74 → 5328.94] And it was super painful.
[5328.94 → 5331.54] So I actually opened an issue going, please let me do this in TypeScript.
[5332.44 → 5332.80] Okay.
[5333.22 → 5334.14] And how did that go?
[5334.24 → 5335.68] Is it still open, the issue?
[5336.08 → 5338.98] We closed the issue and left it in Go just because the work was done.
[5339.28 → 5345.02] But TypeScript, because of first class functions support, higher order functions, being able to pass them around, being able to publish it to NPM.
[5345.54 → 5347.18] There's just so many convenience factors there.
[5347.26 → 5348.28] That ecosystem is great.
[5348.48 → 5349.22] Dependencies in Go.
[5349.80 → 5351.06] I mean, does anyone love them?
[5351.58 → 5352.06] Probably not.
[5352.20 → 5353.18] Yeah, I know.
[5353.28 → 5354.32] That's like a very weird.
[5354.44 → 5355.44] Things are better now.
[5355.44 → 5360.16] I mean, I still have nightmares from like six, seven years ago, like early Go when it was just released.
[5360.22 → 5361.34] It was amazing as a language.
[5361.84 → 5363.68] But oh my goodness me, the whole dependencies.
[5364.42 → 5371.76] It's just like, and it was like, I keep forgetting there was like all these tools which were being invented, which were like half working and mostly not working.
[5371.76 → 5375.40] I even forget like the names of those tools, and they were like so annoying.
[5375.72 → 5376.68] They were trying to be helpful.
[5376.84 → 5378.06] They were trying to address the pain.
[5378.40 → 5381.24] But I think they were causing even more pain in the process.
[5381.44 → 5382.34] So I remember that.
[5382.64 → 5383.64] That's actually a good point.
[5383.88 → 5387.86] Yeah, we used to vendor everything and commit them to our own Git repositories, which was terrible.
[5388.08 → 5395.42] And then we had that semi-official dip, which just magically disappeared because Good came out with like, well, 110, 111.
[5395.50 → 5396.32] 111, I think it was.
[5396.32 → 5397.32] And it's been better.
[5397.56 → 5403.14] I've got to say, but since more projects are now running Good, my life is easier, but still definitely challenging.
[5403.44 → 5403.60] Okay.
[5404.16 → 5410.68] So as we are getting close to wrapping this up, I have one more thought, which I want to share with you.
[5411.20 → 5412.64] And it's more like a question, really.
[5413.08 → 5414.32] What happens with raw code?
[5414.70 → 5415.54] Oh, that's not stopping.
[5415.78 → 5419.88] You know, I've been taking a nice break, bedtime with my family for the last couple of weeks.
[5420.30 → 5422.78] But raw code live will be back in Anger in November.
[5422.78 → 5426.56] And then we've just more, you know, the cloud native ecosystem is not standing still.
[5426.80 → 5428.44] There are so many, many projects out there.
[5428.64 → 5435.48] I think what we will see changing in raw code is, you know, I'll probably move away from just high level introductions to all these tools.
[5435.84 → 5438.42] You know, it's great having the founder there and just showing people how to get started.
[5438.56 → 5441.28] But I really want to get into use case specific stuff.
[5441.44 → 5445.56] So I've been talking to more people in the community and going, what are you actually doing with this tool?
[5445.66 → 5447.20] And what problem is it solving for you?
[5447.20 → 5454.72] So that we can show people not just the getting started guys from all these projects, but here's a real use case that this organization has.
[5454.84 → 5458.02] And here's what they're doing with this tool to give people a bit more inspiration.
[5458.30 → 5459.96] Hopefully remove some of that cognitive.
[5460.26 → 5461.34] Well, did I call it earlier?
[5461.84 → 5462.94] Fatigue, decision fatigue.
[5463.16 → 5464.52] Like we want to try and remove some of this.
[5464.64 → 5467.26] Like if you're staring there, and you're like, what Git Ops tool do I use?
[5467.36 → 5468.88] Or which CNI do I use?
[5469.10 → 5470.94] Like, okay, what is your use case?
[5471.08 → 5471.50] Who does it?
[5471.54 → 5472.76] Is it similar to this organization?
[5472.88 → 5475.86] So this one, and here's the one they use and how they're getting on and what they're doing.
[5475.86 → 5479.32] But yeah, you'll see more use case driven stuff in the next few months.
[5479.62 → 5481.98] That's really exciting because I'm thinking exactly the same way.
[5482.36 → 5491.90] I mean, it's great to have all these conversations, like to get people interested and to get people kind of steered into what resonates with them so that they know what's out there.
[5491.94 → 5493.72] And there's so much out there, as you mentioned.
[5493.94 → 5501.46] But once you do that, you kind of start, I don't know, you feel which way you'd want to go, which way gets you most excited.
[5501.86 → 5505.68] And then the next natural step is to explore that space, right?
[5505.68 → 5508.40] You don't want to stay shallow all the time.
[5508.74 → 5510.84] I mean, breadth is very important.
[5511.22 → 5520.14] But there comes a point you want to go a bit deeper than like the first hour or the first like two hours, which is just very early beginning of any tool, really.
[5520.80 → 5524.06] So yeah, I think there's like everything we do is difficult, right?
[5524.14 → 5525.30] Software development is not easy.
[5525.52 → 5526.60] Doesn't matter how long you've been doing it.
[5526.66 → 5528.26] In fact, it probably gets harder the longer you've been doing it.
[5528.26 → 5534.38] But I think having that breadth of knowledge of what the tools are, when to use them and roughly what they do is really important for everyone.
[5534.64 → 5538.52] But at some point, you do need to go down and actually use it in anger.
[5538.64 → 5540.70] You have to be able to solve real problems with the tool.
[5541.16 → 5547.44] You know, unless you want to be a consultant, and you can jump from company to company and just say, oh, use this tool, use that and then move on and never actually help them implement it.
[5547.44 → 5551.94] But at some point, you do need to use these tools in a real use case driven fashion.
[5552.18 → 5554.86] But yeah, I want to try and tackle that and make that easier for everyone.
[5555.28 → 5559.04] Well, I'm really looking forward to the new and better Raw Code Live.
[5559.30 → 5561.36] And I'm looking forward to what you do next.
[5561.36 → 5568.98] But I encourage you taking these couple of weeks, months, however long it's going to be to make sure everything is nice and smooth.
[5569.20 → 5570.86] The transition in the new job is smooth.
[5570.96 → 5572.14] Onboarding is very important.
[5572.14 → 5574.90] And very often it's skipped, right?
[5574.94 → 5577.46] Like you just get thrown straight in the middle of it.
[5577.92 → 5579.26] And that can be okay.
[5579.64 → 5581.02] And like, it's not always bad.
[5581.28 → 5588.00] But sometimes it's better to just like go slower, go smoother, take the lay of the land and enjoy it.
[5588.08 → 5591.18] Because we keep moving too fast through things, don't we?
[5591.34 → 5594.78] I feel it's like an acceleration of the next thing, the next thing.
[5594.94 → 5599.02] And it's not enough time on enjoying or appreciating the present.
[5599.22 → 5600.62] I couldn't agree more.
[5600.62 → 5604.82] I'd definitely take another couple of weeks just to spend time with the family.
[5605.16 → 5608.48] And then I'll come back in November, hopefully do some more cool stuff.
[5608.60 → 5611.94] You know, I've got big plans for Clustered, big plans for Raw Code Live.
[5612.48 → 5621.22] And with Plum being my new role, I think it's the first time in a long time that my particular interests in technology are directly aligned with the work that I'll be doing.
[5621.54 → 5622.86] So yeah, lots of great stuff.
[5623.08 → 5624.26] I'm really looking forward to that, David.
[5624.42 → 5625.62] Thank you very much for joining us.
[5625.68 → 5626.18] This was great.
[5626.28 → 5626.60] Thank you.
[5626.72 → 5627.34] Thank you for having me.
[5627.40 → 5627.72] It was a pleasure.
[5630.62 → 5633.72] Thank you for tuning in to another episode of Ship It.
[5634.08 → 5635.78] I enjoyed making it for you.
[5636.22 → 5639.14] This is just one of the podcasts for developers that we ship.
[5639.60 → 5642.62] Go to changelog.com forward slash master for the rest.
[5643.10 → 5648.78] You can join me and the rest of our community at changelog.com forward slash community.
[5649.36 → 5651.12] There are no imposters in our stack.
[5651.46 → 5652.62] Everyone is welcome.
[5652.62 → 5657.02] Huge thanks to our partners Vastly, Launch Darkly and Linde.
[5657.30 → 5660.66] Thank you, Brake master Cylinder for all our awesome beats.
[5661.20 → 5662.38] That's it for this week.
[5662.72 → 5663.42] See you next week.
[5663.42 → 5676.78] The music is out.
[5676.82 → 5680.98] And we are asking.
[5682.90 → 5686.56] The music is out.
[5686.56 → 5693.52] Game on.

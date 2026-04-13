[0.10 → 6.66] I'm your host, Gerhard Lazy, and you're listening to Ship It, a podcast about code, ops, infrastructure,
[6.88 → 8.52] and the people that make it happen.
[8.90 → 15.20] Yes, we focus on people and what they do when their best ideas meet the real world.
[15.74 → 16.02] Why?
[16.34 → 20.46] Because that's the only long-term game that is worth playing.
[20.86 → 26.34] This is my second and last set of interviews from Rubicon, Cloud Native Con North America
[26.34 → 27.00] 2021.
[27.00 → 31.08] In this series, I speak with Liz Rice, and it's true.
[31.70 → 33.32] EPF gives you superpowers.
[33.80 → 38.24] We covered William with Hubble, what's it like to work with Duffy Cooley, and William
[38.24 → 39.96] reaching incubating status.
[40.44 → 45.52] Speaking of which, Cross plane was another project that reached the same status, and Gerhard
[45.52 → 47.14] Watts shared the story behind it.
[47.50 → 51.86] We are also joined by Dan Magnum, who tells us what it was like to be at this Rubicon in
[51.86 → 54.54] person, as well as his new COO role.
[54.54 → 57.34] And by that, I mean Click Ops officer.
[57.82 → 63.20] David An sari from VMware speaks about his first Rubicon experience both as an attendee and
[63.20 → 63.78] as a speaker.
[64.34 → 68.76] The RabbitMQ deep dive talk that he gave will be a nice surprise if you watch it.
[69.22 → 70.24] Link in the show notes.
[70.94 → 75.88] To wrap it all up, Dan Lawrence brings his unique perspective on supply chain security.
[75.88 → 81.20] We speak about the new company that he co-founded, Chain Guard, as well as how to secure container
[81.20 → 86.08] images, and one of the Easter eggs that Scott Nichols put in chainguard.dev.
[86.34 → 88.42] That is a great one to end this Rubicon on.
[88.78 → 92.70] Big thanks to our partners Vastly, Launch Darkly, and Linde.
[92.70 → 94.88] Thank you for the great bandwidth Vastly.
[95.10 → 97.22] You can learn more at Fastly.com.
[97.70 → 102.60] Ship new features with confidence by getting your feature flags, powered by LaunchDarkly.com.
[103.02 → 106.82] And thank you, Linde, for keeping our Kubernetes fast and simple.
[107.40 → 113.66] You too can run our infrastructure as we do via Linode.com forward slash changelog.
[113.66 → 120.74] What's up, shippers?
[120.86 → 124.22] This episode is brought to you by our friends at Fly.
[124.64 → 128.66] Fly lets you deploy your apps and databases close to your users in minutes.
[128.66 → 136.46] You can run your Ruby, Go, Node, Dino, Python, or Elixir app and databases all over the world.
[136.74 → 137.50] No ops required.
[137.88 → 140.42] Fly's vision is that all apps should run close to their users.
[140.88 → 142.66] They have generous free tier for most services,
[142.66 → 145.48] so you can easily prove to yourself and your team
[145.48 → 148.66] that the Fly platform has everything you need to run your app globally.
[149.08 → 151.54] Learn more at fly.io slash changelog
[151.54 → 153.72] and check out the speed run and their excellent docs.
[154.14 → 157.44] Again, fly.io slash changelog or check the show notes for links.
[160.66 → 164.58] We are going to shift in 3, 2, 1.
[172.66 → 181.02] So I've attended the last Rubicon virtually.
[181.16 → 182.18] This was Rubicon EU.
[182.82 → 187.48] And I got the impression that the biggest trend then was EPF.
[188.14 → 189.60] Everybody was talking about it.
[189.60 → 194.46] And some were calling it the JavaScript for the kernel, kernel 2.0.
[194.54 → 194.74] Yeah.
[194.86 → 195.90] All sorts of references.
[195.90 → 198.64] How do you think about EPF, Liz?
[198.64 → 202.24] So I've also heard that idea of it being,
[202.62 → 209.06] it's expressed as EPF is to the kernel what JavaScript is to an HTML page,
[209.52 → 211.30] in that it makes it programmable.
[211.64 → 214.76] Kind of interesting analogy, but it kind of makes my brain hurt.
[214.92 → 217.80] So I find it easier to just think about the kernel.
[217.80 → 225.26] So what EPF allows us to do is to run custom programs that we load into the kernel
[225.26 → 227.28] and we associate them with events.
[228.08 → 231.06] And because there are so many different types of events
[231.06 → 233.32] that we can attach our programs to,
[233.52 → 237.60] and because they're in the kernel, there's only one kernel per host.
[237.94 → 244.00] So these programs have access to pretty much everything that's happening on the entire machine.
[244.00 → 249.76] And that makes them incredibly powerful and incredibly useful for observing what's going on,
[250.08 → 252.70] security, and of course, networking as well.
[253.18 → 253.28] Yeah.
[253.42 → 255.44] So yeah, very excited about EPF.
[255.70 → 257.42] That was exactly my impression as well.
[257.74 → 262.30] I really like this idea where you have all those containers running on this host,
[262.36 → 263.44] and then you have many hosts.
[263.68 → 265.34] But still, when it comes to the host,
[265.54 → 268.20] why is this particular set of containers struggling?
[268.62 → 269.50] What is going on there?
[270.02 → 272.00] Networking is such a big issue even today.
[272.00 → 275.72] I think things are getting better, but I remember like three, four years ago,
[275.80 → 278.80] it was like the wild, wild west in the world of Kubernetes IP tables.
[279.06 → 280.64] Oh my goodness me, don't get me started.
[281.24 → 284.56] So I think EPF is making things a little bit more visible,
[284.82 → 287.02] a little bit more understandable, and that helps.
[287.36 → 291.36] And we can skip past those IP tables by just, we'll just ignore that.
[291.46 → 292.92] We'll just use EPF instead.
[293.36 → 297.20] And that does lead to some genuinely measurable performance improvements,
[297.20 → 298.58] which is really nice.
[298.58 → 302.58] So when it comes to the end users, what is EPF helping them with?
[302.80 → 304.14] Understanding things, networking?
[304.54 → 305.92] Is there something more to it?
[306.04 → 307.08] I mean, that's at the surface.
[307.34 → 309.56] If we peel back the first layer, what do we have underneath?
[309.82 → 313.46] So I think one thing to be clear about is that although a lot of us as engineers
[313.46 → 316.30] are getting very excited about EPF programs,
[316.38 → 319.94] and I love to talk about, hey, let's write an EPF program.
[319.94 → 326.54] In reality, most people are not going to need to write EPF programs themselves,
[327.18 → 331.24] much like most of us aren't involved in kernel programming,
[331.50 → 333.30] but we use the kernel all the time.
[333.64 → 338.86] And I think we're increasingly going to see tools that build on EPF primitives,
[339.04 → 342.80] if you like, and offer us really useful abstractions.
[343.14 → 347.04] There are lots of different projects in the CNCF that are starting to do that,
[347.04 → 349.68] and I'm sure we're going to see some more coming forward.
[350.12 → 355.58] There's a history of observability in particular using EPF.
[355.88 → 359.24] Brendan Gregg's been doing amazing work for several years
[359.24 → 364.16] with all these different command line tools that you can use to measure,
[364.38 → 368.74] get metrics on pretty much everything that's happening across your system.
[368.96 → 374.04] But until recently, that's all been very command line driven, quite low level.
[374.04 → 380.66] You know, how many TCP packets are being dropped is a very useful question to be able to answer,
[380.82 → 384.16] but sometimes you want a higher level abstraction.
[384.50 → 390.36] And I think that's where we're seeing a lot of the innovation in this bringing EPF power
[390.36 → 397.26] and capabilities into tools that are at the kind of levels that answer questions for end users.
[397.52 → 397.82] Okay.
[397.82 → 401.80] So I know that one tool that you're very familiar with is Cilium.
[402.04 → 405.06] And I'm wondering where does Cilium and EPF meet?
[405.28 → 408.88] Because end users, I think they would know more about Cilium features
[408.88 → 412.16] and what that helps them do, see and understand,
[412.60 → 416.28] and less about EPF, specifically the technology that Cilium makes use of.
[416.60 → 416.82] Yeah.
[417.04 → 420.66] So Cilium has always made use of EPF.
[420.66 → 428.42] It was originally created as a networking project that uses EPF to create that network plumbing
[428.42 → 431.66] between different endpoints in your system.
[432.04 → 437.16] And I think probably a lot of users just know it as a Kubernetes CNI,
[437.34 → 439.02] but it's actually a lot more than that.
[439.14 → 443.86] It's also offering sort of CNI with lots of bells and whistles.
[443.86 → 449.74] So things like observability, being able to look at network flows, network policy.
[450.06 → 453.72] So giving you security enforcement at the network level.
[454.26 → 460.50] And increasingly, some of our roadmap features take it to the next level with things like
[460.50 → 467.68] Bio-based service mesh, which I think service mesh is a really great example of something
[467.68 → 473.46] whereby running code in the kernel, we don't have to instrument each individual application.
[473.46 → 478.54] And that's a big benefit, going to make things much simpler for people to deploy.
[479.52 → 485.46] So does Cilium, I know that it exposes all these metrics and all this like visibility into
[485.46 → 489.16] what is happening under the hood, especially from a networking perspective and from a
[489.16 → 490.18] communication perspective.
[490.72 → 494.98] But Cilium, what are the components in the Cilium product project?
[495.08 → 498.38] I'm not sure how you want to call it, because obviously there's like the CNI and there's
[498.38 → 499.32] other things.
[499.42 → 501.46] What are the big components that make Cilium?
[501.46 → 502.02] Yeah.
[502.24 → 508.12] So when you run Cilium, you install a Cilium agent on every node.
[508.72 → 513.10] And if all you want is networking capabilities, then that gets you going.
[513.40 → 517.62] You probably want to start being able to see those network flows.
[517.90 → 523.78] And to do that, you'd install a component called Hubble, which collects this network information
[523.78 → 527.38] and the Kubernetes identities associated with it.
[527.38 → 533.82] So if you look at Hubble flows, you can see traffic flowing between different Kubernetes
[533.82 → 535.02] pods.
[535.32 → 541.88] And then there's also a Hubble UI, which pulls that flow information, brings it into a much
[541.88 → 543.60] more sort of human-readable form.
[544.04 → 549.04] So for example, showing you a service map and showing you how traffic is flowing between
[549.04 → 552.04] these different Kubernetes services.
[552.04 → 557.08] And perhaps where maybe there are issues, you can see the packets that are being dropped
[557.08 → 558.48] within that UI.
[558.70 → 562.00] So that's very useful in terms of debugging a network issue.
[562.40 → 566.12] What about when it comes to alerting, monitoring, that side of things?
[566.24 → 569.12] When there is a problem, you're being informed that, hey, there is a problem.
[569.40 → 570.48] Is there such a component?
[570.70 → 573.42] Or would you integrate Cilium with something else for that capability?
[573.72 → 574.76] What does that story look like?
[574.76 → 577.34] Yeah, you'd integrate that with something else.
[577.46 → 582.88] I think a lot of people will push the flow data into some kind of sim, for example.
[583.40 → 585.78] But I'm thinking about, for example, packet loss.
[586.12 → 591.02] There's a lot of our congestion or lots of retries, whatever the case may be.
[591.10 → 597.54] Is there a way to monitor or to consume the Cilium metrics, I'm assuming, and then have alerts?
[597.84 → 603.68] So you can absolutely get the metrics into Prometheus or into showing Grafana.
[603.68 → 606.94] Yeah, there are some beautiful screenshots.
[607.24 → 611.10] And I think I can't quite remember where I saw them recently, but just this whole series
[611.10 → 616.00] of amazing Grafana graphs that you can use to diagnose your network.
[616.20 → 616.46] Okay.
[616.82 → 620.14] I'm not sure whether you can tell by now that I'm really interested in trying Cilium out
[620.14 → 621.80] for real in a production environment.
[621.92 → 622.46] I really am.
[622.48 → 624.28] And I'm trying to figure out what the components are.
[624.74 → 627.88] So my next question would be, where would you recommend that I start?
[628.16 → 629.36] Do I take the Helm chart?
[629.48 → 630.48] Is there an operator?
[631.02 → 632.46] What does the getting started look like?
[632.46 → 635.02] So there are a few different options.
[635.42 → 636.48] There is a Helm chart.
[636.80 → 642.46] There's a command line tool, the Cilium CLI, which makes it as simple as installing the
[642.46 → 646.90] CLI and then Cilium install and Cilium Hubble install.
[646.90 → 647.68] I like that.
[648.40 → 653.24] Does really make that getting started experience nice.
[653.74 → 660.10] Also, if you want a helping hand, we're just about to start a series of weekly install
[660.10 → 660.60] fests.
[660.60 → 665.64] So the idea is to have a session with someone who's experienced in Cilium.
[665.86 → 669.78] They're kind of guiding you through the process, and it'll be interactive so that if people
[669.78 → 673.06] have issues and questions, they can get help along the way.
[673.48 → 674.72] So that's kicking off.
[674.80 → 680.54] I think our first one is either this week or next week, but there's a new kind of feature
[680.54 → 685.94] on the Cilium.io website to book your place on one of those install fests.
[686.30 → 687.28] I love the sound of that.
[687.42 → 687.58] Wow.
[687.62 → 690.12] That's like the I wasn't expecting for that answer, but that's amazing.
[690.22 → 691.74] That's exactly what I'm looking for.
[691.82 → 693.76] So thank you, Liz, for thinking ahead of time.
[694.68 → 695.12] Thank you.
[695.18 → 695.24] Sure.
[695.32 → 696.20] This is perfect.
[696.38 → 696.64] Okay.
[696.64 → 698.14] I really love where this is going.
[698.64 → 703.34] So I'm thinking of watching you code live, which is at the top of my list for this Rubicon.
[703.46 → 707.56] It's like one of the must-do for me at this Rubicon to watch you code live.
[707.88 → 709.44] Can you tell us a little bit more about that?
[709.74 → 710.94] Where the idea came from?
[711.24 → 712.46] How do you intend to do that?
[712.58 → 713.66] What are you intending to cover?
[713.98 → 714.20] Yeah.
[714.28 → 718.04] So I've done a few talks about EPF programming.
[718.42 → 722.60] There's lots of different frameworks and libraries that you can use, and you can write your
[722.60 → 727.34] user space code in different languages like Python and Go, Rust now as well.
[727.84 → 731.54] My Rust isn't quite up to doing live coding in that myself.
[732.24 → 733.88] What do you use for live coding?
[733.96 → 740.78] I typically use either, Go is my kind of go-to language, but for ease of demonstrating a lot
[740.78 → 746.78] of EPF capabilities, I'll quite often use the BCC framework, which supports Python.
[747.20 → 751.28] That's also very, I think, very easy to read in a live coding environment.
[751.28 → 753.52] And occasionally I've done some that you see.
[754.18 → 760.30] So because the kernel programs, the EPF programs that you're actually running in the kernel
[760.30 → 764.06] are typically written in C, can now be written in Rust.
[764.18 → 765.78] So I'm going to have to up my Rust game.
[766.38 → 773.12] But because the kernel part is often written in C, a lot of EPF programmers are also comfortable
[773.12 → 777.34] in that language and therefore writing the user space part in C as well.
[777.74 → 777.96] Okay.
[777.96 → 780.12] And what do you like to cover in those sessions?
[780.42 → 783.78] Like, which is your, I don't know, step number one, step number two?
[783.84 → 785.16] What do you tend to cover in those?
[785.44 → 788.86] I haven't watched one, but again, top of my list, as I mentioned.
[789.02 → 789.26] Yeah.
[789.50 → 792.76] So the kind of step one is usually Hello World.
[793.00 → 795.80] I think that's step one in any programming scenario.
[795.80 → 802.58] And running a little program in the kernel that will just trace out Hello World in response
[802.58 → 806.76] to perhaps a system call or perhaps a network event.
[806.94 → 808.84] And that's very easy to set up.
[809.10 → 815.40] Then maybe we go down the direction of like, how do we get information in and out of the
[815.40 → 815.68] kernel?
[815.68 → 821.70] So there's a concept in EPF called Maps, where they're shared data structures so that
[821.70 → 827.70] we can pass information between BPF programs or into user space between the kernel and user
[827.70 → 828.10] space.
[828.26 → 830.18] Or maybe we go in a networking direction.
[830.42 → 834.32] I did a virtual office hours yesterday where I did some code.
[834.42 → 839.94] Live coding maybe is, I made my life easier in yesterday's virtual office hours by having
[839.94 → 843.30] some pre-prepared code and sort of commenting and uncommenting things out.
[843.30 → 845.64] But it's all running live.
[846.00 → 850.52] So I think that's the best way to approach it, if you think about it, because live coding,
[850.68 → 854.04] it's about like going through it and explaining to users, this is what this does, less about
[854.04 → 854.54] like typing.
[854.74 → 857.20] I think that's like the least interesting part.
[857.32 → 859.92] And it's how you think about things and how you start structuring things.
[859.92 → 861.46] I think that is really, really helpful.
[862.06 → 863.28] So, but yes, I will.
[863.58 → 865.28] Today, do you have a live coding session?
[865.42 → 869.06] Yeah, I've got one 6.30 UK time today.
[869.40 → 869.66] Okay.
[869.72 → 872.72] And another one tomorrow that I think is a little bit earlier.
[872.72 → 873.08] Okay.
[873.20 → 873.78] Check my calendar.
[873.78 → 874.00] Okay.
[874.44 → 874.74] Great.
[875.06 → 875.66] Thank you for that.
[876.08 → 876.36] Okay.
[876.66 → 882.32] So I know that this Rubicon, one of the things that you do is you have a talk, cloud native
[882.32 → 883.88] superpowers with EPF.
[884.04 → 885.16] I know that it's really late for you.
[885.24 → 886.98] 12.30 you said I was looking.
[887.24 → 889.28] So I intend to join and keep you awake.
[889.30 → 890.20] Oh, thank you.
[890.48 → 891.18] How are you with heckling?
[891.28 → 891.92] Do you like heckling?
[892.06 → 892.90] I love heckling.
[893.12 → 894.34] I love questions.
[894.68 → 895.24] Okay, great.
[895.40 → 895.70] Okay.
[895.78 → 896.42] Okay, great.
[896.50 → 897.58] So that's what I intend to do.
[897.64 → 898.10] That sounds good.
[898.20 → 898.38] Okay.
[898.58 → 898.98] Fantastic.
[898.98 → 901.82] I know that Duffy Cooley recently joined you.
[902.00 → 903.34] What's it been like working with him?
[903.42 → 904.98] And by the way, hi, Duffy, if you're listening.
[905.76 → 906.74] Yeah, Duffy is great.
[906.84 → 909.56] We're so pleased that he's joined us at surveillance.
[909.80 → 912.08] He's in LA at the moment.
[912.08 → 916.10] And so he and Dan, our CEO, are our kind of onsite presence.
[916.66 → 919.64] And then most of the team are kind of involved more remotely.
[920.06 → 922.44] But yeah, we're super excited to have Duffy.
[922.60 → 927.34] And he's such a great, he's got so much experience in networking as well.
[927.52 → 931.58] I've always sort of known him more on a sort of security and obviously Kubernetes background.
[931.94 → 935.64] Turns out he has loads of network experience as well.
[935.74 → 937.30] So he's fabulous to have on board.
[937.30 → 937.66] Okay.
[938.08 → 942.72] Do you get to pair with him or just bounce ideas of what does working with him look like?
[942.82 → 945.18] I know that you have shows, live shows with him.
[945.48 → 946.30] I know about that.
[946.42 → 947.76] What happens outside of that?
[948.06 → 949.60] Yeah, so we are eight hours different.
[949.76 → 953.18] So that makes it a little bit more difficult to collaborate than ideal.
[953.40 → 958.20] But yeah, we're definitely figuring out some of the ways that we want to tell stories.
[958.50 → 962.16] Some of the, you know, doing Echo, which is our live stream.
[962.26 → 963.58] That's a lot of fun to do together.
[963.58 → 967.52] And yeah, it's a delight to have him in the company.
[967.96 → 968.48] That sounds great.
[969.04 → 972.58] Speaking about Rubicon, I know that you'll be remote, virtual.
[972.86 → 974.84] I've seen even like your Twitter tagline change.
[974.92 → 976.58] I'm thinking everything the same, but it's a great idea.
[976.68 → 977.88] I'll be at Rubicon, but virtually.
[978.06 → 980.56] So I'll be there, but you won't see me unless it's online.
[980.96 → 982.94] What are you looking forward to the most at this Rubicon?
[983.26 → 985.20] Well, I'll be completely honest.
[985.32 → 991.22] I'm very much looking forward to the project updates announcements about new projects joining
[991.22 → 992.10] the CNCF.
[992.20 → 994.34] That's only in about an hour away from now.
[994.56 → 1001.20] So keep your eye out for a project that we know and love becoming a CNCF project.
[1001.78 → 1002.90] I'm looking forward to that.
[1003.02 → 1003.20] Okay.
[1003.48 → 1006.52] By the way, this goes live, I think about in about two weeks.
[1006.88 → 1010.10] So if there are announcements that you want to make, you can, because it's going to be
[1010.10 → 1010.70] post-Rubicon.
[1010.90 → 1013.04] So if there's anything like that, it's fine.
[1013.16 → 1013.98] In that case.
[1014.44 → 1014.72] Go on.
[1015.08 → 1015.52] I'll trust you.
[1015.52 → 1016.44] It's only an hour away anyway.
[1016.44 → 1023.06] It's not really even a secret, but we officially announced today that Cilium is becoming a CNCF
[1023.06 → 1024.72] incubation level project.
[1024.96 → 1028.36] So I'm excited about that as a Cilium person.
[1028.36 → 1034.86] And I'm excited about that as a TOC person, because it means we've got networking, you know,
[1034.86 → 1037.00] finally on the landscape.
[1037.00 → 1041.46] We've got a couple of sandbox projects, but we didn't have anything that was really, you
[1041.46 → 1047.42] know, production hardened, filling that kind with CNI box on the landscape.
[1047.74 → 1054.26] So I feel like that's a really nice box that we're ticking from a CNCF perspective and obviously
[1054.26 → 1057.78] hugely exciting from a Cilium community perspective.
[1058.20 → 1058.98] That sounds amazing.
[1059.16 → 1059.34] Wow.
[1059.48 → 1059.72] Okay.
[1060.00 → 1060.32] Right.
[1060.74 → 1064.62] I mean, you just added like another big reason why I want to do certain things, but yeah.
[1064.62 → 1064.86] Okay.
[1064.94 → 1065.20] Okay.
[1065.40 → 1066.56] Let me not get ahead of myself.
[1066.68 → 1067.34] I always do that.
[1067.40 → 1068.02] I get too excited.
[1068.20 → 1069.06] I mean, this sounds great.
[1069.06 → 1070.50] I'm really looking forward to that, by the way.
[1070.50 → 1075.26] So for the people that can attend Rubicon in person, like you and me, what would you
[1075.26 → 1075.64] recommend?
[1076.24 → 1080.28] How would you recommend they feel part of it without actually being there in person?
[1080.58 → 1087.28] For me, I find that the interaction, even if it's chat, is what makes me feel connected
[1087.28 → 1088.08] to people.
[1088.90 → 1094.28] So, and also if you're attending a talk and there are speakers, speakers love getting
[1094.28 → 1094.74] questions.
[1094.74 → 1096.80] It kind of shows that you're paying attention.
[1096.80 → 1101.78] So don't be shy, type those questions in, or if you are able to be there in person,
[1102.00 → 1102.94] ask the questions.
[1103.36 → 1108.88] And I also think, although it can sometimes be a little bit kind of difficult to take the
[1108.88 → 1114.10] leap into, you know, turning your camera on in some kind of hallway track event.
[1114.10 → 1119.16] But if you do get, you know, if you're tempted to even slightly tempted, it can be so rewarding
[1119.16 → 1121.70] to get into a, you know, a video chat.
[1121.70 → 1124.48] You know, sometimes there'll be virtual office hours.
[1124.70 → 1129.24] I think they'll probably, I think for us in our time zone, most of the sort of social
[1129.24 → 1133.32] hallway track events are likely to be in the middle of the night.
[1133.48 → 1135.88] So maybe I'll be doing less of that this time.
[1136.14 → 1138.50] But, and get into Slack.
[1138.70 → 1141.20] There'll be loads of people watching.
[1141.50 → 1145.56] I'm, every time I go on Twitter and I see a photo of someone, you know, and I'm thinking,
[1145.82 → 1148.08] they're in LA, and I'm kind of jealous.
[1148.48 → 1151.98] But I also know there are lots of us who aren't able to be there.
[1152.02 → 1153.10] So we're all in the same boat.
[1153.36 → 1156.92] And I'm sure we all chat to each other, whatever time zone we're in.
[1157.30 → 1157.56] That's right.
[1157.68 → 1158.80] Slack does help.
[1158.88 → 1161.64] I have to say at Tube and EU, I know it was in our time zone.
[1161.72 → 1164.52] So that made some things easier, but it was still virtual.
[1164.52 → 1165.68] So we had to adapt to that.
[1165.68 → 1170.42] So having Slack helped the happy hours, the impromptu ad hoc sessions where like a bunch
[1170.42 → 1174.22] of us would get together, whether it was four or five of us and would like talk.
[1174.22 → 1176.82] That would really help to meet people that you would normally meet.
[1177.14 → 1182.06] And it was like, I never had like a bad conversation, even though people that I've met for the first
[1182.06 → 1182.38] time.
[1182.46 → 1183.76] So that was, that was a good experience.
[1184.14 → 1187.34] I think the virtual office hours, that is a great idea.
[1187.70 → 1192.00] Conversations like these help and like more of this happening live would help for sure.
[1192.82 → 1195.16] But I think we're all trying to figure this out, right?
[1195.18 → 1197.12] And we don't expect it to be permanent.
[1197.36 → 1202.24] I mean, it's now, I think this was like an unfortunate situation because from November,
[1202.24 → 1205.78] I know that UK and much of Europe can go to the US.
[1206.02 → 1207.70] So it was just bad timing, I suppose.
[1207.70 → 1207.94] Yeah.
[1208.18 → 1212.98] Although I hope that we do keep some of this virtual element going, because I think there
[1212.98 → 1217.92] are a lot of people who, you know, for financial reasons or, you know, commitment reasons, or,
[1218.10 → 1223.56] you know, there are many reasons beyond COVID why people can't necessarily make it to an event.
[1223.56 → 1230.48] So I think if we can maintain some of the virtual elements, I do think that that brings more
[1230.48 → 1235.08] people in and, you know, won't ever be quite the same as being there in person, but it is
[1235.08 → 1236.78] still an opportunity to connect.
[1237.30 → 1242.50] And as you're going to say, the platform that they're using this time around seems quite
[1242.50 → 1248.52] good for certainly when I did the virtual office hours yesterday, it works, and you can
[1248.52 → 1251.04] have conversations with people.
[1251.04 → 1252.88] So, you know, we're getting there.
[1253.54 → 1254.70] That is a very interesting perspective.
[1254.80 → 1257.12] And I do have to say, it makes a lot of sense, right?
[1257.58 → 1262.04] Especially for, as you mentioned, people for which travelling is difficult, right?
[1262.08 → 1267.58] It is a considerable financial investment for many attendees, and it just opens up, right?
[1267.60 → 1273.06] We have so many more people joining this wonderful community that I don't think they would have
[1273.06 → 1273.96] the opportunity otherwise.
[1274.30 → 1277.02] So in a way, it is a blessing in disguise.
[1277.12 → 1280.30] And I think I did talk about this at some point, but I forgot about that.
[1280.30 → 1280.82] And you're right.
[1280.94 → 1282.12] So thank you for reminding me.
[1282.56 → 1287.54] So as we are preparing to wrap up, I'm wondering if there's anything interesting happening for
[1287.54 → 1292.04] EPF or Cilium in the next six months that you would like to share?
[1292.04 → 1296.22] Well, I guess we've started off with those weekly install fests.
[1296.38 → 1298.42] So that's our kind of initial thing.
[1298.50 → 1305.28] I mean, I think from a feature roadmap perspective, there are some pretty interesting things coming
[1305.28 → 1308.96] down the pipeline and in particular, I think Kern or Service Mesh.
[1309.30 → 1313.92] In general, I think the whole Service Mesh space is pretty confusing right now.
[1313.98 → 1319.38] And I think we are seeing some evolution in the different products that are out there.
[1319.54 → 1322.14] And Cilium is definitely going to be a big part of that story.
[1322.14 → 1322.62] Okay.
[1323.26 → 1327.90] Well, I didn't need any more reasons, but I got them to watch this even more closely,
[1328.06 → 1333.30] try it out for myself and try running it in production just to see what's it like with
[1333.30 → 1337.94] some significant amounts of traffic to see how it holds up, to see what it shows us.
[1338.08 → 1339.34] I'm really excited about that.
[1339.62 → 1345.58] And if you do have any questions or issues, the Cilium Slack community is super helpful.
[1345.94 → 1348.40] So jump in there and let us know how you get on.
[1348.56 → 1349.10] We want to hear.
[1349.10 → 1350.32] That's another great tip.
[1350.44 → 1350.92] Thank you, Liz.
[1350.98 → 1352.20] Thank you very much for making the time.
[1352.32 → 1353.28] It's been an absolute pleasure.
[1353.62 → 1353.94] Thank you.
[1354.10 → 1354.94] Thank you for having me.
[1370.62 → 1374.40] This episode is brought to you by our friends at Incident.io.
[1374.80 → 1379.06] Every software team on the planet has to manage incidents and a very large percentage of those
[1379.06 → 1381.00] teams are using Slack to communicate.
[1381.18 → 1382.16] That includes us.
[1382.48 → 1387.42] With Incident.io, you can create, manage, and resolve incidents directly inside Slack.
[1387.70 → 1388.62] Here's how it works.
[1388.88 → 1390.96] Head to Incident.io and sign up for free.
[1391.18 → 1392.60] Then add it to your Slack.
[1392.76 → 1396.62] From there, you have a brand-new incidents channel where all incidents get announced.
[1397.00 → 1399.56] Use the slash incident command to create and manage incidents.
[1399.98 → 1404.36] This command lets you share updates, assign roles, set important links, and more,
[1404.68 → 1406.54] all without ever leaving the Incident channel.
[1406.94 → 1411.94] Each Incident gets their own Slack channel plus a high-res dashboard at Incident.io
[1411.94 → 1414.42] with the entire timeline from report to resolution.
[1414.96 → 1418.16] Get everyone on the same page from the moment they join the Incident and help stakeholders
[1418.16 → 1419.02] stay in the loop.
[1419.38 → 1423.52] Add Incident, IO to your Slack today and prove to yourself and your team that they have everything
[1423.52 → 1425.12] you need to streamline your incident management.
[1425.60 → 1428.02] Learn more and sign up for free at Incident.io.
[1428.32 → 1429.38] No credit card required.
[1429.38 → 1431.38] Again, Incident.io.
[1444.50 → 1451.24] So, out of everyone that I spoke to so far, Dan, you're the first one that you're at Rubicon
[1451.24 → 1451.92] in person.
[1452.30 → 1455.18] So, tell us what's it like for everyone that couldn't make it.
[1455.30 → 1456.04] Yeah, absolutely.
[1456.04 → 1460.70] Well, first, it is incredibly nice to be able to see folks that I haven't been
[1460.70 → 1464.76] able to see in a number of years and also some folks I've never met in person before.
[1464.96 → 1469.94] So, regardless of the whole situation with COVID and all, I definitely feel very privileged
[1469.94 → 1472.06] to be here and don't take that lightly.
[1472.38 → 1478.00] In terms of, you know, comparing to previous Rubicons, I've actually been mostly to virtual
[1478.00 → 1481.70] Rubicons just because, you know, we've been in this pandemic stage for so long.
[1481.70 → 1486.86] I did have the opportunity to go to Rubicon in San Diego in person, which obviously you
[1486.86 → 1489.80] remember because we recorded a great podcast episode there.
[1490.08 → 1491.76] And it definitely feels different from that.
[1491.90 → 1496.98] The CNCF has done an incredible job of making this a very safe environment with their health
[1496.98 → 1497.94] and safety protocols.
[1498.18 → 1502.88] So, that's been very impressive in terms of spacing, in terms of making sure everyone's
[1502.88 → 1508.08] comfort levels with being close to people or being in proximity of others is adhered to.
[1508.22 → 1509.60] That's been very impressive.
[1509.60 → 1514.30] There's absolutely less attendance than there has been at past Rubicons.
[1514.66 → 1518.84] And one of the things that I've noticed is there's a lot more just community members
[1518.84 → 1522.84] here rather than end users, I'd say, which has pros and cons, right?
[1522.86 → 1526.24] It's always really nice to talk to end users because they're the folks that really motivate
[1526.24 → 1530.18] product roadmaps and CNCF project roadmaps and that sort of thing.
[1530.24 → 1532.22] And it's really valuable to hear from them.
[1532.36 → 1535.68] But it's also really nice to be able to collaborate with other projects.
[1535.68 → 1540.18] So, I've been spending a lot of time just talking to other maintainers, talking to other companies,
[1540.60 → 1544.12] seeing what they're up to, talking about different integrations that could be possible.
[1544.54 → 1549.98] So, it's a different feel, but its unique atmosphere, I think, is really advantageous in some respects.
[1550.54 → 1551.50] That sounds great.
[1551.60 → 1553.62] So, how did you make it work, Jared?
[1554.04 → 1555.78] Because I know that you're remote, right?
[1555.78 → 1557.94] But you have the virtual office hours.
[1558.14 → 1559.34] How did you make those works?
[1559.44 → 1560.16] Did they help?
[1560.68 → 1561.84] How did that feel for you?
[1562.08 → 1563.38] Yeah, it's actually kind of interesting.
[1563.50 → 1566.24] I was just thinking about it and reflecting a little bit while Dan was answering.
[1566.56 → 1568.60] And so, you know, actually, so I live in San Diego.
[1568.88 → 1574.02] And so, I'm actually fairly close to, in proximity to where Rubicons is being held in Los Angeles.
[1574.52 → 1578.14] But then my schedule ended up getting booked up with so many virtual commitments
[1578.14 → 1583.70] that it didn't make it super possible to go up there and then do everything, you know, all at the same time.
[1583.70 → 1589.20] And so, yeah, so it's, I mean, the CNCF does a good job with organizing this and making all the virtual events possible
[1589.20 → 1594.18] to kind of be inclusive and make sure that as a hybrid event, people are getting opportunities to participate
[1594.18 → 1597.74] if they're either in person, but also back at home, wherever that may be.
[1598.06 → 1602.92] So, the virtual office hours that we ran yesterday was quite successful with, you know, a lot of people joining in,
[1603.26 → 1604.86] a lot of questions being asked also.
[1605.06 → 1611.34] And so, you know, the ability to connect with people virtually and not feel left out from the in-person event running on
[1611.34 → 1615.92] is, I think, actually working quite well and everyone's still feeling, as far as I can tell,
[1616.04 → 1619.28] pretty connected and getting lots of chances to participate, which is perfect.
[1619.58 → 1623.94] Were there any questions that really stood out to you, something like really memorable that made you think
[1623.94 → 1626.52] or something fascinating that you weren't expecting?
[1626.90 → 1628.80] There were a lot of good questions yesterday.
[1629.16 → 1634.04] One of the things that's kind of, I've realized too, is that while I'm presenting and questions are flooding in,
[1634.14 → 1639.16] it's really, perfect to have multiple people there to be able to support and answer questions
[1639.16 → 1642.22] and do that asynchronously in addition to the ones we answer on camera,
[1642.28 → 1645.74] because there's just too many questions to answer on camera and also get through all the material.
[1646.22 → 1649.12] So, you know, I was trying to focus on delivering the material,
[1649.22 → 1651.30] why everyone else was attacking all the questions.
[1651.72 → 1655.64] So, Dan, do you remember any specific ones that, you know, you were jumping on while I was presenting?
[1656.08 → 1656.62] Yeah, absolutely.
[1656.82 → 1659.16] Like you said, there were a lot of really great questions.
[1659.32 → 1664.70] The ones that really stuck out to me, and this is something that's kind of been a point of interest for folks
[1664.70 → 1668.52] throughout all of Cross Plan's lifecycle, and that's handling of sensitive data.
[1668.52 → 1672.78] So with Cross Plan, we have two major kind of sources of sensitive data,
[1672.92 → 1676.60] one of them being credentials to talk to cloud providers or external APIs,
[1677.18 → 1681.66] and the other being credentials to communicate with the infrastructure that you're provisioning
[1681.66 → 1683.36] using those external APIs.
[1684.02 → 1689.48] And so some of the progress we've made around being able to supply external API credentials
[1689.48 → 1694.46] via secret stores like Vault and injecting those into the file system of our providers
[1694.46 → 1699.60] and that sort of thing, as well as some of the proposals around how we publish connection details
[1699.60 → 1701.06] to that infrastructure that comes up.
[1701.22 → 1706.42] It's always really exciting when you go from one conference to, you know, the next iteration of it,
[1706.60 → 1710.90] and you have some solutions for the folks that had questions about that the previous time,
[1710.90 → 1715.10] or you at least have something where you have a design for what it's going to look like.
[1715.10 → 1719.56] So this kind of topic areas around security and credentials and that sort of thing
[1719.56 → 1722.60] was something that really stuck out to me in the questions that we got.
[1722.60 → 1726.18] There was also a question that really stuck out in my mind now that just popped back in,
[1726.24 → 1731.72] is that somebody asked, yeah, I could just go into the GCP console in the UI and create infrastructure.
[1731.86 → 1733.08] Why do I need Cross Plan at all?
[1733.42 → 1737.36] And so the thing that really stuck in my mind is that, hey, one, we definitely, hey,
[1737.40 → 1742.34] we could probably improve our educational content and, you know, our messaging and really make it more
[1742.34 → 1744.38] clear to people what the value is.
[1744.44 → 1746.02] So that's an improvement we can make on our side.
[1746.06 → 1747.02] There's no question about it.
[1747.22 → 1751.70] But that's a big point of the project is that a lot of times you most certainly don't want to be giving
[1751.70 → 1755.92] direct access to the cloud provider consoles, to your developers and have them, you know,
[1755.96 → 1758.68] being able to willy-nilly create resources on their own.
[1758.74 → 1762.74] You want to be able to have a separation of concerns and, you know, kind of gate the access
[1762.74 → 1764.06] that they get to resources there.
[1764.22 → 1767.46] So that is a big value, you know, selling point of the project.
[1767.58 → 1770.54] And so that's, that kind of, it's just stuck to me that, hey, maybe we need to be messaging
[1770.54 → 1771.40] that a little bit better.
[1771.84 → 1772.66] Here's an idea for you.
[1772.66 → 1778.76] Next time someone asks you this, I think you should introduce Dan as the COO, Chief
[1778.76 → 1779.74] Click Ops Officer.
[1780.26 → 1782.66] Say, we created a role.
[1783.52 → 1784.90] That was like such a good thing.
[1785.06 → 1789.14] So Click Ops is real, and we have just the right antidote for it.
[1789.18 → 1790.28] And he's called Dan Magnum.
[1791.10 → 1792.54] So yeah, that's a good one.
[1793.00 → 1793.28] Okay.
[1793.38 → 1793.64] Okay.
[1793.80 → 1796.46] This is actually something which I've been thinking about as well.
[1796.62 → 1799.84] I started using Cross plane to manage all my GKE clusters.
[1800.14 → 1800.92] It worked great.
[1800.92 → 1805.58] I never want to go back and not even to the CLI, which is really weird because the G-Class
[1805.58 → 1809.18] CLI is great, but Cross plane is better from that perspective.
[1809.30 → 1810.24] So I really enjoy that.
[1810.48 → 1813.44] And in that world, I was wondering, how can we handle secrets better?
[1813.60 → 1817.38] Because, you know, secrets in Kubernetes by default, Base64 encoded.
[1817.58 → 1819.38] Well, sorry, that's not really secret.
[1819.82 → 1820.68] Anyone can get it.
[1820.94 → 1821.60] That's a great one.
[1821.68 → 1823.40] I will definitely want to follow up on that.
[1823.70 → 1828.20] But I have another thing on my mind because San Diego was mentioned a couple of times and
[1828.20 → 1831.26] I had an amazing run around the San Diego Marina.
[1831.86 → 1836.14] So I'm wondering, Dan, was the run in LA better than this is your San Diego one?
[1836.52 → 1837.54] What can you tell us about it?
[1837.76 → 1839.60] So you're catching me at a good time.
[1839.84 → 1844.60] Right before this podcast, I got back from the SIG run event we had this morning where
[1844.60 → 1847.44] there was about 15 of us or so that ran through LA.
[1847.44 → 1852.80] And I can say absolutely that running in LA is not as good as running in San Diego.
[1853.20 → 1855.00] There are a lot of stoplights.
[1855.22 → 1860.38] I had one run out to Dodger Stadium earlier this week and that was pretty nice.
[1860.62 → 1866.88] But overall, I would not recommend coming to Los Angeles as a destination spot for getting
[1866.88 → 1867.64] your runs in.
[1867.98 → 1868.14] Right.
[1868.36 → 1872.74] So next Rubicon, I'm thinking a place where we can all enjoy running a lot more, right?
[1872.74 → 1877.14] Because that's the most important criteria for choosing a Rubicon location.
[1877.44 → 1877.92] Right.
[1877.96 → 1878.66] That's a good one.
[1878.90 → 1879.66] Do you run, Jared?
[1879.76 → 1881.20] I never asked, and I don't know.
[1881.36 → 1881.70] Do you run?
[1881.94 → 1887.76] I am more of a person who likes to do their exercise like in a combination with a goal,
[1887.96 → 1889.04] like a direct activity.
[1889.24 → 1892.38] So surfing and ice hockey are my big exercise things.
[1892.52 → 1893.94] I just had an ice hockey game last night.
[1894.06 → 1897.26] And so I'm having a little bit of trouble waking up this morning and feeling a little sore,
[1897.34 → 1899.58] a little banged up from some of the violence out there.
[1899.58 → 1902.74] And so Dan's saying he's getting back from his run this morning when I
[1902.74 → 1905.24] is not the same morning that I've had so far.
[1905.90 → 1906.22] I see.
[1906.94 → 1907.34] Right.
[1908.36 → 1909.12] That's interesting.
[1909.28 → 1909.68] Surfing.
[1909.76 → 1910.58] I never tried it.
[1910.68 → 1912.52] I think I would like out of the two activities.
[1912.70 → 1914.12] That sounds a very interesting one.
[1914.32 → 1915.26] That would be up for trying.
[1915.36 → 1917.58] So let's see where Rubicon happens next in the US.
[1917.86 → 1918.64] Is it Detroit?
[1918.74 → 1919.80] I've heard Detroit being mentioned.
[1919.92 → 1920.38] Is that real?
[1920.62 → 1920.78] Yep.
[1920.82 → 1925.06] They announced yesterday Rubicon EU, I believe is in Valencia and Rubicon
[1925.06 → 1929.28] North America is going to be in Detroit, which is I'm pumped about it coming to the
[1929.28 → 1929.56] Midwest.
[1929.56 → 1934.32] I think that's kind of exciting because we sometimes miss out on some events in the Midwest.
[1934.32 → 1935.68] I see.
[1935.88 → 1936.18] I see.
[1936.26 → 1936.46] Okay.
[1936.64 → 1937.40] No surfing there.
[1937.46 → 1939.70] I'm imagining in Detroit to be in the Midwest.
[1940.04 → 1940.34] I don't think so.
[1940.44 → 1942.08] I haven't heard of it as the surfing destination.
[1942.78 → 1943.90] Concrete surfing, maybe.
[1944.52 → 1944.72] Yeah.
[1944.74 → 1945.30] Or Valencia.
[1945.30 → 1946.00] That's a good one.
[1946.12 → 1946.34] Okay.
[1946.68 → 1946.88] Yeah.
[1946.88 → 1949.12] That's more for like yachting, I suppose, or something like that.
[1949.22 → 1949.42] Okay.
[1949.84 → 1951.54] So let's talk about the big news.
[1951.98 → 1954.36] Cross plane was announced for incubation status.
[1954.62 → 1956.60] It was a few weeks ago before Rubicon.
[1956.92 → 1958.14] That is huge.
[1958.18 → 1959.68] And I'm wondering what changed for you?
[1959.74 → 1964.60] What changed for Cross plane day to day as a project with it entering the incubation phase?
[1964.86 → 1965.70] Jared, what do you think?
[1965.96 → 1966.32] Yes.
[1966.32 → 1971.58] The incubation thing is definitely something that I put a lot of effort into with the due
[1971.58 → 1978.12] diligence and making sure that the proposal is really covering all aspects of the project.
[1978.30 → 1982.84] And so I got a good finger on the pulse in terms of the project's growth and the maturity
[1982.84 → 1983.84] and all that sort of stuff.
[1984.26 → 1987.60] So one thing that's kind of interesting is that it is a bit of a long process.
[1987.60 → 1995.26] So the vetting and diligence is pretty thorough, which is a good thing because that's how projects
[1995.26 → 1998.66] that make it to this level are given a stamp of maturity.
[1999.26 → 2003.58] And the ecosystem as a whole can have confidence in them that they're mature and that they're
[2003.58 → 2006.54] reliable, and they check a certain set of criteria.
[2007.02 → 2008.10] So the process was a long thing.
[2008.18 → 2013.40] So it was a bit of a rolling experience there were the project was still maturing and while
[2013.40 → 2015.36] we're almost at incubation, but not quite.
[2015.36 → 2021.34] And so with the announcement itself, though, we absolutely saw a new influx of adopters
[2021.34 → 2023.26] and users coming in to check out the project.
[2023.54 → 2029.16] You're looking at some of the metrics and stats, the graphs for GitHub stars or Slack members,
[2029.28 → 2033.82] et cetera, went vertical for about a week or two, which was really cool to see that, hey,
[2033.86 → 2037.40] we've made some inroads, and we built a community, but there's more people out there to reach.
[2037.74 → 2042.62] And the CNCF is helping us do that with declaring the project more mature and making a lot of
[2042.62 → 2043.24] noise about it.
[2043.24 → 2047.26] So, you know, day to day how the project is run is not changing because the governance
[2047.26 → 2050.70] is there and, you know, the project release processes and all this sort of things is
[2050.70 → 2052.10] pretty healthy and really well done.
[2052.28 → 2053.30] So that doesn't change.
[2053.38 → 2056.48] But, you know, the influx of people coming and more people to try it out and the community
[2056.48 → 2061.44] continues to grow because now they feel it's mature enough to do that is really encouraging
[2061.44 → 2061.86] to see.
[2062.30 → 2062.44] Right.
[2062.52 → 2063.32] What about you, Dan?
[2063.34 → 2068.12] What makes you most excited about cross-plane reaching incubation status?
[2068.12 → 2068.56] Absolutely.
[2069.70 → 2074.02] Well, Jared touched on a bunch of great things there and Jared absolutely led this effort
[2074.02 → 2077.44] and a ton of a ton of effort and work went into it.
[2077.80 → 2081.96] So we're very appreciative to all of that he put in and just let us sit back and
[2081.96 → 2082.78] work on the project.
[2082.78 → 2083.06] Right.
[2083.06 → 2086.92] But, you know, kind of building on some of the things that he already mentioned, one of
[2086.92 → 2092.56] the things that I really love about cross-plane being an incubating project is a lot of folks
[2092.56 → 2096.70] that I talk to now who are new folks that I'm meeting at least have some sort of kind
[2096.70 → 2102.36] of baseline knowledge of what our mission is, which allows us to kind of get to more advanced
[2102.36 → 2103.60] conversations faster.
[2103.80 → 2108.98] So I absolutely love talking to folks who don't know anything about cross-plane and want to hear
[2108.98 → 2112.62] about, you know, the big picture vision and that sort of thing, but we can really kind
[2112.62 → 2116.94] of get down to brass tacks and talk about more tangible things when folks come in and
[2116.94 → 2120.40] already have a little bit of an idea of what we're trying to do.
[2120.50 → 2124.68] And that gives us ideas as maintainers, you know, about what do folks need to take this
[2124.68 → 2126.42] to the next level and that sort of thing.
[2126.52 → 2130.52] So I think just that visibility has been a huge boon for us already.
[2130.86 → 2135.20] It's crazy that I remember 2019, right, when we started talking about cross-plane, this
[2135.20 → 2139.38] new thing, people like some heard of it, but it was still very new.
[2139.80 → 2143.54] It took, I'm not sure what stage you were at then, but now you're incubating.
[2143.68 → 2144.94] There was a sandbox stage.
[2145.14 → 2147.52] Were you in sandbox back then, two years ago, 2019?
[2147.90 → 2151.02] We weren't even part of the CNCF at that point in our first conversation.
[2151.30 → 2151.58] Okay.
[2151.92 → 2153.54] When did you join the CNCF, by the way?
[2153.76 → 2154.64] June 2020.
[2155.14 → 2155.46] Okay.
[2155.80 → 2159.94] So it took about a year and a bit to go from sandbox to incubation.
[2160.20 → 2160.74] Yeah, exactly.
[2160.90 → 2164.84] We started the process to apply for incubation probably March of this year.
[2164.84 → 2168.06] So it's about nine months or so that we started, you know, getting serious and putting the
[2168.06 → 2169.04] proposal out there.
[2169.10 → 2171.10] And then the process itself took about six months.
[2171.50 → 2171.62] Yeah.
[2171.70 → 2176.22] I think that in my mind explains a lot about the level of busyness that I've seen in the
[2176.22 → 2177.60] level of activity, right?
[2177.60 → 2182.54] Because even before then, I can imagine this must be a really thorough process, as you mentioned,
[2182.64 → 2183.28] for good reason.
[2183.76 → 2186.90] And it's great to see this journey that you're on.
[2187.34 → 2191.06] I mean, 2019, as you mentioned, not even part of the CNCF, but you were there.
[2191.16 → 2192.76] I was like, oh yes, that was there.
[2192.76 → 2194.38] And I wanted to use it since then.
[2194.72 → 2196.56] I'm finally using cross-plane.
[2196.68 → 2197.82] And I love what I see there.
[2197.88 → 2198.90] I have so many questions.
[2199.26 → 2202.48] And I'm sure that many more people will have many more questions.
[2202.96 → 2208.48] Which is the best way of, first, finding out about cross-plane, starting to use it.
[2208.76 → 2213.50] And then once you get a bit more intermediate in the cross-plane usage, what do you do the
[2213.50 → 2213.80] next?
[2213.96 → 2216.42] What does that trajectory look like in your mind, Dan?
[2216.64 → 2216.84] Yeah.
[2216.84 → 2220.86] So, you know, a lot of folks start off with just coming to our getting started guide and
[2220.86 → 2222.68] getting introduced to what that looks like.
[2222.76 → 2227.30] And one of the decisions we've made in our getting started guide is to incorporate some
[2227.30 → 2230.46] of our kind of actual more advanced concepts early on.
[2230.56 → 2234.68] And when I'm talking about advanced concepts, that's mostly our composition engine and our
[2234.68 → 2235.10] packaging.
[2235.10 → 2241.00] And despite introducing these earlier, because they are tools that are used to build abstractions,
[2241.34 → 2245.04] folks actually get a nicer interface to using cross-plane right off the bat.
[2245.40 → 2249.26] They're able to use these advanced concepts without actually understanding all the little
[2249.26 → 2249.80] bits of it.
[2249.80 → 2252.18] So usually folks will go through that process.
[2252.64 → 2257.08] And in our getting started guide, we have an abstraction of a database and show how that
[2257.08 → 2263.04] can create an RDS instance on AWS or a Cloud SQL instance on GCP, all from the same spec from
[2263.04 → 2265.94] the actual resource that you're creating in your Kubernetes cluster.
[2266.66 → 2270.22] And so generally what folks will do is they'll go through that process, and they'll start to
[2270.22 → 2271.60] kind of see the bigger picture.
[2272.00 → 2277.62] And then honestly, a lot of the way that folks continue to dive into the project is number
[2277.62 → 2281.44] one, looking at some of the content that we put out there on YouTube and that sort of
[2281.44 → 2281.70] thing.
[2281.92 → 2286.14] Victor joined Upbound and the Cross plane community and has been putting out some great content
[2286.14 → 2286.92] around that.
[2287.28 → 2292.26] And then also just our Slack workspace has exploded over the past six months or so.
[2292.26 → 2296.88] And there are countless folks in there just asking questions, learning more about it.
[2297.16 → 2302.58] One of the really rewarding things to see as a maintainer is community members helping other
[2302.58 → 2303.40] community members.
[2303.86 → 2307.20] Because, you know, earlier on, it was mostly community members coming along.
[2307.20 → 2310.12] And asking maintainers questions and then answering those.
[2310.20 → 2311.42] And that didn't scale super well.
[2311.90 → 2316.94] Now that we have end users helping each other use Cross plane and talking about what features
[2316.94 → 2320.76] they'd like to see, what things work for their organizations, how that would affect others.
[2321.16 → 2325.18] That's really where we see folks really get into the weeds of Cross plane and start to understand
[2325.18 → 2328.36] how they can extend it for their specific use cases.
[2328.66 → 2330.34] Yeah, building that community is super important.
[2330.46 → 2335.06] I know that is such a huge and important part of what you do every day, right?
[2335.06 → 2339.54] I mean, I see you everywhere, Twitter, YouTube, Slack, so much activity.
[2339.76 → 2341.22] And now that will only pick up.
[2341.66 → 2342.04] And you're right.
[2342.10 → 2346.60] There's a point where people have to start helping one another out because it can't be
[2346.60 → 2348.12] on you, the project maintainers.
[2348.38 → 2352.48] So I think that is one important thing for people listening to this to try and help others.
[2352.48 → 2356.76] If you're into Cross plane and you know something, you know, help your friend that you may not
[2356.76 → 2359.20] know yet, but get to know him or her.
[2359.20 → 2362.30] And yeah, see how you can help one another out.
[2362.60 → 2367.88] One thing which I would like to say is that the GCP provider, there was a very recent version,
[2368.02 → 2369.66] I think 0.18 or 0.19.
[2369.76 → 2370.70] I can't remember exactly.
[2371.12 → 2373.12] That upgrade was very interesting.
[2373.64 → 2377.94] And I think that those things will become when you deprecated the GKE cluster for the cluster.
[2378.48 → 2381.58] So there was like an export to be made and then reimport to be made.
[2381.74 → 2383.34] There was a fairly involved process.
[2383.34 → 2387.46] So I'm wondering that going forward, is that something that you're thinking about, Jared,
[2387.60 → 2390.02] in terms of how to make it smoother for users?
[2390.28 → 2396.00] Because if people will keep spending a lot of time on figuring that out or even performing it,
[2396.02 → 2398.98] to be honest, what I've done, I just didn't bother with the upgrade.
[2399.10 → 2402.62] I deleted all the clusters, remove, reinstall because it was too involved.
[2402.72 → 2407.34] I tried it, but like step number five or six, I said, it's just too much work.
[2407.34 → 2414.16] So I'm wondering how you're thinking about the continued usage and the upgrades going forward
[2414.16 → 2416.96] so that users, their lives are easier.
[2417.28 → 2418.84] Yeah, that's a really, perfect question.
[2419.50 → 2421.50] There are a couple of thoughts come to mind on that.
[2421.62 → 2424.52] First is that there was a lot of thought put into that.
[2424.86 → 2429.52] It wasn't an easy decision of, oh, hey, let's just make this change here and roll it out.
[2429.78 → 2431.68] Dan drove that effort to begin with.
[2431.94 → 2434.50] And so he made a proposal about it, explained it very thoroughly,
[2434.50 → 2441.78] and gave the entire community a sense of what the situation is with GCP having kind of
[2441.78 → 2445.34] beta API that some people may want to depend on and then a stable API,
[2445.54 → 2447.08] which other people may want to depend on.
[2447.20 → 2450.62] So kind of supporting two different APIs from the cloud provider itself
[2450.62 → 2455.32] with different varying levels of guarantees around breaking changes and things like that.
[2455.70 → 2458.72] So Dan did a perfect job laying all that out, putting it out to the community,
[2458.72 → 2464.02] and then spending a couple of months actually with getting feedback and kind of understanding it, right?
[2464.50 → 2465.36] So that was a good thing there.
[2465.42 → 2468.76] And then Hassan did a perfect job of writing up a migration guide.
[2469.08 → 2470.80] So something I learned from the Rook project,
[2471.10 → 2473.58] the storage orchestration for Kubernetes that I'm also involved with,
[2473.64 → 2476.54] is that migrations are one thing.
[2476.74 → 2481.08] But if you don't provide any path at all for people, then that could be a failure.
[2481.64 → 2485.10] And so there are some manual steps with that upgrade or the migration.
[2485.10 → 2489.26] And, you know, having the guide to do that, to give people the opportunity,
[2489.26 → 2495.16] it was something I was definitely proud that we paid attention to that and had some empathy for the community to go ahead and invest in that.
[2495.62 → 2498.52] And then the last comment I'll make there is that, you know,
[2498.54 → 2502.88] there are different levels of maturity and guarantees within the Cross plane ecosystem itself also.
[2503.32 → 2505.76] So Cross plane as a core project, you know,
[2505.76 → 2509.64] the functionality and machinery and tooling to build your own custom platforms, etc.
[2509.64 → 2512.86] That is at, you know, a 1.0 or 1.5 almost now.
[2513.20 → 2514.62] That's stable, the API there.
[2514.94 → 2519.66] You know, there are some guarantees around breaking changes and, you know, backwards compatibility and things like that.
[2519.80 → 2525.68] So we don't anticipate and haven't done any, you know, difficult migrations in core Cross plane in quite a while.
[2525.94 → 2530.40] And we're going to stick to that, you know, unless we do like a 2.0 and then that'll be very explicit as well.
[2530.50 → 2534.08] But for the providers, they are not at that same level of stability yet.
[2534.08 → 2539.68] So they're still in a, you know, alpha, beta sort of phase where there are going to be some of those breaking changes, perhaps,
[2539.84 → 2542.94] as things are being figured out and matured along the way.
[2543.22 → 2545.28] But you won't, you shouldn't see that in core Cross plane.
[2545.60 → 2550.50] It's very nice that you've laid out all that background because I remember looking at the issue that Dan opened.
[2550.82 → 2552.72] It was perfect, like really well-thought-out.
[2552.84 → 2554.70] There wasn't a lot of engagement on the issue.
[2554.86 → 2556.54] Maybe that happened on Slack or elsewhere.
[2557.16 → 2562.84] But I really like that I could follow the trail all the way to the source and see, well, this has been happening for a while.
[2562.84 → 2565.28] Well, thought has been put into this.
[2565.44 → 2565.74] You're right.
[2565.82 → 2566.76] That guide was perfect.
[2566.86 → 2567.74] Like I followed it.
[2568.02 → 2568.78] It worked.
[2569.14 → 2570.78] But I was thinking, do I really want to do this?
[2570.82 → 2572.40] It's like there's like too much stuff here.
[2572.44 → 2574.84] And I have to like, I was like step number three or four.
[2575.24 → 2578.36] And I still have like to continue like four others or something like that.
[2578.76 → 2580.78] So I was like halfway through and I thought, you know what?
[2580.96 → 2582.44] It would be easier to do that.
[2582.78 → 2589.06] What I want to say is that having gone to the end, having gone like to the latest version of the GCP provider,
[2589.54 → 2592.06] everything that I thought it would have, it had.
[2592.06 → 2597.96] So the new cluster resource behaved a lot better than the GKE cluster one.
[2598.04 → 2599.30] So it was worth getting there.
[2599.40 → 2605.66] And once I had that, I found the extra properties, especially around auto-scaling, very, very useful.
[2605.90 → 2606.98] So I love seeing that.
[2607.14 → 2608.98] It was a great end state to get to.
[2608.98 → 2615.36] So as we are about to wrap this up, anything coming in the next six months that you'd like to share with us?
[2615.36 → 2620.72] So I'll talk a little bit about some of the future things that we have planned for Cross plane.
[2620.92 → 2626.16] And some of this, you know, Cross plane, as we all know here, is a CNCF project, right?
[2626.22 → 2631.12] So when I talk about what I want to see in Cross plane, that doesn't necessarily mean it's going to happen.
[2631.44 → 2636.50] It's my personal desire for what happens and my contribution to the roadmap as a maintainer.
[2636.50 → 2641.52] So, you know, we'll see how other maintainers and other community members feel about my proposals.
[2642.00 → 2646.66] But one of the things that I am really interested in is our provider deployment model.
[2646.86 → 2653.70] So right now, the way provider packages work is it's essentially a stream of YAML, which is a bunch of different CRDs.
[2653.70 → 2666.32] And then it's a reference to an image that lives, you know, on a registry somewhere or is already in your cluster that you run, that runs the controllers for all of those different resource types that you're installing.
[2666.82 → 2672.66] Now, the way that we actually set up that controller for you when you install a provider is we create a Kubernetes deployment.
[2672.86 → 2674.60] And that's the only way we do it right now.
[2674.88 → 2676.56] That doesn't have to be the case, right?
[2676.58 → 2679.76] A deployment is one way to manage a workload within a Kubernetes cluster.
[2680.18 → 2682.30] You could also create a Native function.
[2682.30 → 2685.20] You could create something external to your Kubernetes cluster.
[2685.32 → 2689.36] It could be a Lambda function on AWS that had access to your Kubernetes cluster.
[2689.80 → 2699.46] And you can also start to think of things as more granular than our kind of monolithic providers we have right now, where you can think of just custom logic that you need to run.
[2699.54 → 2701.62] That's kind of the glue between your different providers.
[2702.26 → 2704.74] So those are a lot of different options.
[2704.74 → 2709.28] But essentially, you can imagine there is an interface, right, for different provider deployment models.
[2709.28 → 2713.62] And you can say, I'd like to use my provider and install my provider.
[2714.00 → 2718.24] And I wanted Cross plane to use this deployment engine for it to set that up.
[2718.34 → 2719.76] And I can manage it in a certain way.
[2720.06 → 2725.50] What that also gives you the ability to do is you may not manage your core Cross plane control plane,
[2725.72 → 2729.54] but you may manage some of the custom logic that you want to introduce into it.
[2729.54 → 2737.66] So obviously, thinking of a hosted control plane model, you can think about that an external organization could run your control plane for you.
[2737.88 → 2745.46] But you kind of do that last mile API interaction where you supply credentials and that sort of thing on your own infrastructure and your own AWS account.
[2745.88 → 2749.82] So thinking about some flexibility around that and some partitioning as well.
[2749.82 → 2753.92] Right now, when you install provider AWS, you get all the provider types installed.
[2754.30 → 2755.70] You really shouldn't have to do that.
[2756.04 → 2766.10] And so really customizing and making more granular provider installs and API extension mechanisms are something that's going to be top of mind for me over the next six months to a year.
[2766.30 → 2768.50] I have so many questions to that.
[2768.64 → 2773.10] We are out of time, but I really want to hear what Jared is thinking about for the next six months.
[2773.50 → 2773.84] Awesome.
[2774.00 → 2774.20] Yes.
[2774.20 → 2780.98] Quick thing for Dan there is that, you know, you kind of mentioned that it's a community driven project and, you know, he has his own proposals, etc.
[2781.50 → 2784.18] And the community can always weigh in and see if they are good ideas.
[2784.62 → 2789.28] Historically speaking, the Dan's proposals tend to be pretty well accepted and good ideas.
[2789.74 → 2792.92] So what he's saying there probably will be something the community likes.
[2793.38 → 2793.48] Yeah.
[2793.50 → 2797.54] So for me, I'll just quickly throw in two things that I think are really exciting over the next six months.
[2797.92 → 2800.64] They're provider coverage and then custom compositions.
[2800.94 → 2804.06] So provider coverage, we'll have a lot more to share about that pretty soon.
[2804.20 → 2813.04] But basically doing, you know, code generation to automatically generate cross-plane providers for the full surface area of a cloud providers API.
[2813.42 → 2815.94] You know, like AWS has like almost 700 resources.
[2815.94 → 2824.46] So being able to have a cross-plane provider to do all of those resources and have, you know, very full coverage is very, very exciting.
[2824.58 → 2825.76] And that's coming along pretty soon.
[2825.76 → 2827.78] And then the other one, custom compositions.
[2828.26 → 2837.60] You know, the composition engine is fairly powerful where you can compose together all of your resources and infrastructure and then provide those as a high level abstraction to your developers.
[2837.60 → 2838.60] It's a powerful model.
[2838.60 → 2839.28] It's a powerful model.
[2839.40 → 2841.60] But then there are some things we can do to improve that.
[2841.90 → 2851.74] If you want to do some custom logic or, you know, emulating or, you know, flow control or anything like that, we're enabling a way to do that with the language of your choice.
[2851.74 → 2868.84] So to be able to kind of extend the composition engine and be able to write however you want to, whatever language you want to, some logic and, you know, details about generating custom compositions at runtime, which will kind of open the door to really any scenario that anyone can think of.
[2869.00 → 2874.44] So that'll be a nice kind of last mile thing for scenarios that aren't really covered with the default machinery right now.
[2874.44 → 2878.40] Well, all I can say is please continue blowing my mind the way you are.
[2878.64 → 2880.80] There's a very special way that you blow my mind.
[2880.88 → 2883.00] Every single time I talk to you, this is amazing.
[2883.46 → 2884.18] Thank you very much.
[2884.58 → 2886.94] The other thing which I would like to say is stay cool.
[2887.54 → 2893.78] Cross plane is really cool and just keep doing what you're doing and keep reconciling and enjoying Rubicon, but especially reconciling.
[2893.90 → 2894.60] So thank you, Dan.
[2894.72 → 2895.28] Thank you, Jared.
[2895.40 → 2896.00] This has been a pleasure.
[2896.18 → 2896.36] Awesome.
[2896.54 → 2896.86] Right on.
[2896.92 → 2898.40] Thank you so much for having us again, Gerhard.
[2898.48 → 2899.58] Always love to be on the show.
[2899.84 → 2900.16] Absolutely.
[2904.44 → 2905.44] Thank you.
[2910.44 → 2913.76] This episode is brought to you by our friends at Ray gun.
[2914.00 → 2916.34] Have you ever wondered how users are really experiencing your software?
[2916.82 → 2925.08] When you unlock real user insights, you'll be able to identify and resolve front end performance issues and ensure your application is consistently delivering superior experiences.
[2925.52 → 2934.42] Ray gun will deliver a daily performance summary to keep your finger on the pulse of your website with an overview of your slowest pages, Core Web Vitals, user sessions, and user sessions.
[2934.44 → 2938.38] This gets sent straight to your inbox or Slack channel of your choice.
[2938.72 → 2945.84] Join thousands of performance focused, customer-centric software teams who use Ray gun every single day to deliver flawless experiences to their customers.
[2946.16 → 2948.40] Again, Raygun.com.
[2948.40 → 2962.24] So I know, David, that this is your first Rubicon.
[2962.76 → 2968.16] And I am very curious to hear, what was it like for you?
[2968.16 → 2969.32] It was very interesting.
[2969.32 → 2969.36] It was very interesting.
[2969.80 → 2975.48] So I really enjoyed the hybrid format of this Rubicon because unfortunately I couldn't be there in person.
[2975.82 → 2977.96] So I would like to go there in person.
[2978.38 → 2983.24] But unfortunately, there was still a travel ban for most Europeans.
[2983.24 → 2994.14] So it was still very interesting to participate virtually and to listen to talks and being able to reach out to people and to ask questions.
[2994.64 → 2994.92] Okay.
[2995.08 → 2995.94] Did you Slack?
[2996.02 → 2997.10] How did you reach out to people?
[2997.22 → 2997.64] Zoom?
[2997.86 → 2999.22] How did that work for you?
[2999.46 → 3002.50] Yes, mainly over the Meeting Play platform.
[3002.50 → 3007.90] So when I was attending a talk, I could just ask my questions, and they got live answered.
[3008.14 → 3009.68] So that was a nice experience.
[3010.02 → 3014.62] There was the possibility to reach out via Slack, but I didn't use Slack too much.
[3015.28 → 3016.48] What about Zoom?
[3016.62 → 3019.00] Were there any Zoom sessions that you attended?
[3019.32 → 3021.82] I know that Priyanka used to do Happy Hour.
[3021.82 → 3029.92] I don't know whether she did this Rubicon, but that was one of my favourite sessions at the previous Rubicon year, which was also a virtual one.
[3030.10 → 3031.40] No, no Zoom sessions.
[3031.40 → 3033.48] To be honest, I missed all Zoom sessions.
[3033.80 → 3036.44] I wasn't aware that those Zoom sessions exist.
[3036.62 → 3037.36] Did you attend some?
[3037.64 → 3038.72] Yeah, that's what I said.
[3038.82 → 3039.62] Not this one.
[3039.94 → 3044.98] I attended the previous one and that was actually my favourite part of the conference at Rubicon EU.
[3045.14 → 3047.22] This was, I was going for a different experience.
[3047.56 → 3050.62] I was going more like, you know, talking to people like I'm talking to you.
[3050.92 → 3052.06] I attended a few talks.
[3052.40 → 3056.08] There were some specific ones that I really enjoyed, and I wanted just to get a bit more involved.
[3056.60 → 3059.24] There were virtual office hours, which I participate in a few.
[3059.24 → 3061.18] So I had a slightly different experience.
[3061.40 → 3065.44] Closer to what I would have had if I had gone there in person, which I also couldn't do.
[3065.76 → 3068.12] So this was less of a virtual.
[3068.22 → 3074.14] I tried to make it less of a virtual one for me and more of an in-person without being there, which is a bit, sounds a bit weird.
[3074.14 → 3079.52] But I enjoyed talking to people as much as I could, which is what happens when you're there, right?
[3079.56 → 3081.94] It's less about the talks, and it's more about the interactions.
[3082.32 → 3083.52] So that's what I did.
[3083.76 → 3087.30] I know that this was not just your first Rubicon.
[3087.46 → 3089.90] It was your first Rubicon as a speaker.
[3090.18 → 3090.64] That's correct.
[3090.64 → 3091.56] How was that for you?
[3091.78 → 3092.50] Tell us about it.
[3092.60 → 3095.76] It was a lot of fun and the experience was very good from start to end.
[3095.76 → 3101.88] So I first applied, I think a few months ago and directly after Rubicon Europe.
[3102.30 → 3109.26] And I was actually listening to Ship It, episode two, where some tips were given on how to submit an abstract.
[3109.86 → 3116.64] So I submitted my abstract, I think just two days after the episode came out and it worked.
[3116.64 → 3120.24] I was lucky and from then on the communication was very well.
[3120.60 → 3128.74] So there were very good contents being given to the speakers on how to prepare with checklists and deadlines.
[3129.24 → 3132.50] And the communication was very good from start to end.
[3133.12 → 3135.64] So especially Cody was answering very quickly.
[3136.04 → 3136.76] So that was nice.
[3137.24 → 3137.36] Yeah.
[3137.42 → 3141.78] So I pre-recorded the talk and submitted it, I think one month before the conference.
[3141.78 → 3143.56] So that was the beginning of September.
[3143.56 → 3149.62] And thereafter I was very relaxed because once I submitted the talk, I knew nothing can go really wrong.
[3150.36 → 3154.56] So I would just be there, the talk would play, and then I jumped for the Q&A.
[3155.04 → 3158.08] So it was a very relaxed and nice experience of all.
[3158.42 → 3163.80] I attended the talk, I have to say, and I really enjoyed it, especially how quickly you're answering questions.
[3164.14 → 3167.04] And I think that is something unique about pre-recorded talks.
[3167.04 → 3173.46] Maybe the interaction isn't, obviously it's not the way you would interact if you were given it in
[3173.46 → 3178.54] person, and you had a connection with the audience because, well, you're not there, you can't see the audience.
[3179.02 → 3181.70] So in that case, I think a pre-recorded talk makes sense.
[3181.94 → 3185.20] But the highlight of that is that you can answer questions as they come in.
[3185.46 → 3188.12] And it was great to see you answered some of those questions.
[3188.38 → 3189.76] I mean, some of them were tough ones.
[3189.76 → 3198.32] And not only was the talk really polished, by the way, because you could take your time to record and re-record and get it just right.
[3198.66 → 3200.88] Your video editing skills are perfect, by the way.
[3200.98 → 3204.76] I know that you've edited it yourself, and it was great.
[3204.98 → 3207.42] Like I really genuinely enjoyed watching it.
[3207.94 → 3211.66] So from my perspective as a viewer, it was great.
[3211.80 → 3212.38] Thank you very much.
[3212.38 → 3214.48] From your perspective, you're welcome.
[3214.80 → 3222.40] During the talk, what was it like when you could basically you were attending your own talk, and also you were answering questions?
[3222.52 → 3223.22] What was that like?
[3223.48 → 3225.16] So the experience was very good.
[3225.30 → 3229.04] And I think the talk being pre-recorded has many advantages.
[3229.04 → 3234.54] So for both speaker, but also for the attendees, because for the attendees is just frictionless.
[3234.82 → 3236.24] They have a better experience.
[3236.24 → 3242.78] They can ask questions live when they don't understand something and I can directly answer via live chat.
[3243.42 → 3244.06] So that was good.
[3244.42 → 3247.70] And as you mentioned, you can just pre-record the video.
[3247.86 → 3249.20] So you can have multiple tries.
[3249.36 → 3250.70] You can edit it if you want.
[3251.38 → 3257.16] And to be honest, I was even having some parts of the videos which I had to edit and pre-record five times.
[3257.62 → 3258.10] Wow.
[3258.18 → 3260.26] Just because the demo didn't work, for example.
[3260.76 → 3265.28] And it just results in a better end version, which you can then also share.
[3265.28 → 3265.32] Yeah.
[3265.90 → 3270.20] So the questions came in, and I could just answer them during the talk.
[3270.20 → 3278.62] And as the video was playing, I couldn't even pay attention to the video itself because I was focusing only on the Q&A part.
[3279.06 → 3281.14] And also the conversation thereafter was great.
[3281.34 → 3286.62] So my problem was a bit that my video was 32 minutes and I had 35 minutes in total.
[3286.84 → 3289.14] So just three minutes left for Q&A.
[3289.14 → 3291.02] So that was a bit short.
[3291.48 → 3295.52] But you can always continue conversation after the talk.
[3295.98 → 3301.12] So are you saying that you wish the talk was shorter so that you would have had more time for Q&A?
[3301.48 → 3301.78] Yes.
[3301.78 → 3310.30] So if I were to do the talk again, I would shorten it probably by three or four more minutes just to leave enough room for questions in the end.
[3310.42 → 3316.32] Because I think that's one of the most valuable parts of the talk so that you have a vivid discussion.
[3316.32 → 3320.16] Because that's the most important part of a talk, the discussion in the end.
[3320.28 → 3325.12] It's less about us telling something to people or teaching about a certain concept.
[3325.12 → 3327.50] It's more about the discussion, which is valuable.
[3327.50 → 3332.96] So that you get feedback from the users, and you see which parts they don't understand.
[3333.14 → 3334.76] You see what they are interested in.
[3334.96 → 3337.72] The questions they ask about around certain topics.
[3337.82 → 3340.78] So certain topics come up more often than other topics, for example.
[3341.44 → 3343.98] And you even see like how advanced the users are.
[3344.14 → 3348.86] So I was a bit surprised because people joined and didn't even know what rapid MQ is.
[3349.06 → 3353.90] Which made it think me that maybe I should have introduced rapid MQ even better at the start of the talk.
[3353.90 → 3359.96] So I think the level at which the talk was, was intermediate experience, I believe.
[3360.10 → 3361.26] It wasn't the beginner talk.
[3361.26 → 3363.04] I also think you're right.
[3363.16 → 3366.92] Making it shorter is great because there are two rules.
[3367.38 → 3368.52] Don't give out all the information.
[3369.00 → 3370.62] And there's, I won't tell you the second rule.
[3371.36 → 3371.88] That's it.
[3372.40 → 3373.46] I'm curious now.
[3375.14 → 3376.08] Do you hold it for the end?
[3376.94 → 3378.16] The point is, no, no.
[3378.26 → 3380.40] I mean, there are two rules, and you only say one, right?
[3380.60 → 3382.18] Like don't give out all the information.
[3382.62 → 3383.06] That's it.
[3383.90 → 3384.30] Okay.
[3385.78 → 3386.74] Now I get it.
[3386.84 → 3387.32] Now I get it.
[3389.02 → 3396.02] So the idea being that you want the audience, I mean, that's basically what prompts the questions, right?
[3396.02 → 3401.08] If you tell them half the story, I mean, there's so much more that you could tell them.
[3401.44 → 3403.36] But what do they want to know?
[3403.44 → 3406.62] And then they come to you asking about questions that you haven't thought about.
[3407.08 → 3410.90] You haven't given like, it's more about telling user what's possible.
[3410.90 → 3413.08] Getting users excited.
[3413.96 → 3415.56] Making them imagine things.
[3415.56 → 3418.82] And then see what they do with that.
[3418.82 → 3420.82] I mean, was it exciting enough?
[3421.00 → 3422.06] What are they thinking?
[3422.42 → 3425.34] What do they wish you had told them that you haven't?
[3425.44 → 3430.76] Because for time reasons, for the conversation reasons, as you mentioned, it's about the discussions.
[3430.76 → 3437.26] And the way you generate discussions is by making it interesting and short and letting them decide, well, what shall we do next?
[3437.70 → 3439.02] It doesn't always work like that.
[3439.08 → 3440.58] Obviously, you have to know your audience.
[3441.12 → 3442.74] But I think that's what happened here.
[3442.74 → 3444.76] So it was very compressed, was very condensed.
[3445.22 → 3446.36] Many concepts were introduced.
[3446.64 → 3447.76] And that's what it was meant to be.
[3447.88 → 3450.38] You know, I'll give you a taste from many different things.
[3450.38 → 3452.72] And then you tell me what you would like to know more.
[3453.36 → 3461.10] I'm wondering if, had you maybe spent more time in Slack, you could have continued some of those conversations there.
[3461.36 → 3461.88] I don't know.
[3461.88 → 3467.86] But what I do know is that another talk which I attended, that was Liz Rice's talk on EPF.
[3468.06 → 3469.92] In the talk, the Q&A didn't work.
[3470.18 → 3472.26] Like, we could ask questions, but she couldn't answer.
[3472.66 → 3474.62] And then we moved into Slack.
[3474.74 → 3477.54] And then we had a good conversation, like, between the different people there.
[3477.70 → 3479.06] It was mostly question answering.
[3479.22 → 3484.04] But also someone, I forget their name, they added some extra information.
[3484.38 → 3488.20] And it was good to see, like, in the Slack channel, that conversation.
[3488.20 → 3494.54] So I think that's a good idea to, you know, say, hey, if you want to know more if you want to talk to me, I'll be there.
[3494.88 → 3495.50] Let's hang out.
[3496.10 → 3497.62] So, again, it's just an idea.
[3498.10 → 3500.32] Who knows if it works out until you try it.
[3500.76 → 3510.26] Okay, so what I'm hearing is that for first speakers, I think that having the talk pre-recorded may be a better experience.
[3510.26 → 3518.92] Because that stage fright, that, like, you know, being there for the first time, being overwhelmed by emotions, being overwhelmed by, you know, what's happening.
[3519.12 → 3520.58] There's, like, too much stuff happening, right?
[3520.88 → 3523.22] Especially at a big conference like Rubicon.
[3523.52 → 3525.20] So it can be a bit overwhelming.
[3525.64 → 3530.22] So I'm wondering if this is a good idea of starting your Rubicon experience, you know?
[3530.36 → 3531.72] I mean, how did you feel?
[3531.76 → 3532.64] Did you feel relaxed?
[3532.76 → 3537.80] Did you feel, like, what was the predominant feeling as you were giving this talk and as you were preparing for the talk?
[3537.80 → 3543.62] So as I started the talk, I was very relaxed because I knew that everything was pre-recorded.
[3543.78 → 3545.78] So nothing could go really wrong.
[3546.04 → 3552.46] I know that it can be intimidating when you go on stage because if you do a live demo, for example, many things can go wrong.
[3553.00 → 3558.04] So the talk being pre-recorded is just much more comfortable for the speaker.
[3558.46 → 3558.60] Okay.
[3558.70 → 3561.82] Yeah, so I could fully focus just on the questions part.
[3562.26 → 3564.60] And that was very valuable to the attendees.
[3564.60 → 3567.06] So what are you thinking about next Rubicon?
[3567.06 → 3570.12] Will you attend it in person, virtually?
[3570.40 → 3571.44] Will you give a talk?
[3571.52 → 3573.18] Would you prefer to give a talk virtually?
[3573.60 → 3575.18] Or would you like a pre-recorded one?
[3575.36 → 3577.38] Or would you prefer to give a talk in person?
[3577.48 → 3578.02] What are you thinking?
[3578.48 → 3584.66] So if I have the chance to go to a conference in person, I would go there in person because it's really about meeting the people.
[3585.30 → 3586.92] So for me, a conference has two sides.
[3586.92 → 3592.84] First side is really learning something, hearing talks, and having technical conversations.
[3593.46 → 3599.32] And the second part is meeting people and getting to know contributors to other projects.
[3600.02 → 3604.50] And that second part came a bit short for me, this Rubicon, just because it was virtual.
[3604.50 → 3608.78] So for the Europe Rubicon next year, I try to go there in person.
[3609.24 → 3611.74] Are you thinking of giving a talk or submitting one?
[3611.88 → 3612.66] I would like to.
[3613.18 → 3620.94] So if the talk, let's imagine that it gets accepted, are you thinking of giving it in person or pre-recording as you have this time?
[3621.08 → 3623.00] The next time I would give it in person.
[3623.34 → 3623.66] In person.
[3623.66 → 3625.12] Just to also practice.
[3625.60 → 3625.82] Yeah.
[3626.12 → 3630.50] So what I'm looking up here, I just wanted to confirm because I sometimes get his name wrong.
[3631.14 → 3636.04] So there's this person that I admire when it comes to public speaking.
[3636.04 → 3638.52] His name is Matt Abrahams.
[3639.00 → 3642.92] And he gave a couple of talks about memorable communication.
[3643.58 → 3645.22] He even wrote a book, a very good one.
[3645.68 → 3647.30] Small one, but important one.
[3647.62 → 3649.70] Speaking out without freaking out.
[3649.90 → 3653.54] He had a tech talk, and he has a couple of great talks online on YouTube.
[3653.66 → 3656.70] About how to make your communication memorable.
[3657.26 → 3660.84] How to deal with anxiety while giving talks publicly.
[3661.24 → 3666.14] Or, you know, there's like different types of talking where you prepare, and the ad hoc ones would just happen.
[3666.70 → 3670.56] And that really helped me to become a more confident speaker.
[3670.92 → 3678.02] So it may not work for you, but I would recommend checking it out and see if there's something valuable there that, you know, relates to you.
[3678.30 → 3679.86] So that's what I would say.
[3679.94 → 3681.50] It helped me, and may help you.
[3681.66 → 3681.84] Cool.
[3681.84 → 3684.18] So what did you enjoy the most about this Rubicon?
[3684.40 → 3687.80] I enjoyed most that there were so many different tracks I could choose from.
[3688.70 → 3692.02] So the whole ecosystem is very wide.
[3692.26 → 3695.58] So I think there were around eight, nine or even ten tracks in parallel.
[3696.02 → 3696.12] Yeah.
[3696.24 → 3698.42] There were a lot of topics and talks to pick from.
[3698.94 → 3700.68] So that was a very good experience.
[3701.12 → 3701.94] Choose the variety.
[3702.08 → 3703.16] Yes, it is a big conference.
[3703.28 → 3703.58] You're right.
[3703.90 → 3705.46] It's one of the biggest ones I know.
[3705.94 → 3707.68] And it's just like so diverse.
[3707.68 → 3709.58] I love the diversity of Rubicon.
[3709.68 → 3713.08] I'm not aware of any conference that gets diversity better.
[3713.28 → 3715.24] And I mean diversity from all perspectives.
[3715.54 → 3716.44] Any favourite talks?
[3716.78 → 3719.06] Anything that stood out that was memorable?
[3719.60 → 3721.72] Because we spoke about memorable communication.
[3722.02 → 3723.00] I didn't watch.
[3723.18 → 3723.72] There were too many.
[3723.72 → 3729.50] So for me, it was quite late since I'm in Europe.
[3729.86 → 3734.70] So on Wednesday, my talk started at half past 11.
[3735.14 → 3739.40] So before that, I just watched one talk to see how things are working with the platform.
[3739.40 → 3745.04] And thereafter, I was too tired to continue watching talks like at 1 a.m..
[3745.64 → 3745.72] Yeah.
[3745.84 → 3751.04] The next day, I was watching one, which was about a new generation of Nuts, just to see
[3751.04 → 3754.24] how the Nuts messaging system works compared to RabbitMQ.
[3754.64 → 3756.36] So I enjoyed watching that.
[3756.92 → 3761.38] You do know that all these talks, first, you can watch them on demand in the platform
[3761.38 → 3763.76] before they become available on YouTube.
[3763.76 → 3768.64] So what I tend to do, and this is what I've done.
[3769.02 → 3773.74] While I haven't watched the talks as they happened, only a few, what I've done, I would
[3773.74 → 3775.92] go back to the previous day, what I've missed.
[3776.04 → 3779.70] Because you're right, like three, four o'clock, staying up until three, four o'clock, it doesn't
[3779.70 → 3780.40] really make sense.
[3780.76 → 3781.94] Well, at least not to me.
[3782.42 → 3787.02] And what I have done next day, I would go over the previous talks, go over all of them,
[3787.36 → 3789.84] see if there's something that resonated with me.
[3789.84 → 3793.90] And if it did, I would watch parts of it or the parts that really stood out.
[3794.28 → 3798.90] And that was a good experience because I could consume the talks much quicker before they
[3798.90 → 3800.00] become available on YouTube.
[3800.10 → 3803.70] So I could consume a lot more content and content that was relevant for me.
[3803.78 → 3808.52] That is actually one of my favourite parts of a virtual conference where all this is recorded
[3808.52 → 3810.46] and it's available as it happens.
[3810.94 → 3812.52] So I enjoy the platform.
[3812.66 → 3816.92] I think the platform enables you to consume and to connect to the conference in a different
[3816.92 → 3817.14] way.
[3817.30 → 3818.04] I thought that was good.
[3818.04 → 3819.94] What was the most valuable content to you?
[3820.78 → 3823.32] I really enjoyed EPF, I have to say.
[3823.76 → 3827.30] It's something like the whole EPF ecosystem, super, fascinating.
[3827.94 → 3833.02] Liz Rice's talk, cloud native superpowers with EPF, because I just love the kernel.
[3833.30 → 3838.02] I just love that observability, understanding what's happening inside the kernel.
[3838.48 → 3840.46] That's the talk that really resonated with me.
[3840.54 → 3845.78] It's something that I picked up on at last Rubicon, but this one, I could focus a bit more
[3845.78 → 3847.06] on the EPF ecosystem.
[3847.06 → 3849.94] I didn't even know that there's actually an EPF foundation.
[3850.46 → 3852.46] I learned about that at this conference.
[3852.96 → 3859.06] And yeah, it's just fascinating networking and the kernel and performance and metrics
[3859.06 → 3860.70] and that sort of thing.
[3860.92 → 3866.30] My most important takeaway about EPF is that it's all about kernel events.
[3866.62 → 3868.56] And events, you know, I mean, I love eventing.
[3868.70 → 3870.02] It's a great concept.
[3870.40 → 3873.50] And I think the way it's implemented, like the underpinnings are really, really solid.
[3873.50 → 3876.34] I can see some amazing things coming out of this.
[3876.84 → 3880.08] Have you used EPF in your projects you're working on?
[3880.64 → 3884.60] Not yet, but all that is going to change in the next few months.
[3885.14 → 3890.08] So parka.dev, that's one of the first things that I'll be setting up.
[3890.18 → 3891.44] And the next one will be Cilium.
[3891.70 → 3894.12] Cilium with Hubble and a couple more things.
[3894.12 → 3899.04] I think the level of observability from a kernel perspective is unique.
[3899.34 → 3901.38] I haven't seen anything like that before.
[3901.72 → 3907.56] And now that you mentioned that, I think the only utility that I've used that uses EPF
[3907.56 → 3910.86] under the hood was net data, but not extensively.
[3911.02 → 3915.10] Only, you know, like at a brief level, superficial level.
[3915.36 → 3915.96] It's good.
[3915.96 → 3920.86] And it's not much different than it was before with EPF or since it added EPF integration.
[3921.14 → 3925.24] But that's the first one that I have used with EPF, now that I remember.
[3925.58 → 3926.90] What else would you like to talk about?
[3927.52 → 3929.80] One good experience was speaker support.
[3930.06 → 3935.30] So there was a dedicated Slack channel and support was answering with the response time
[3935.30 → 3935.92] less than a minute.
[3936.60 → 3941.80] So when we asked a question, it just got flagged and someone was saying they will look up the
[3941.80 → 3943.48] answer or get in touch with us.
[3943.90 → 3945.58] So that was really great support.
[3945.58 → 3949.62] Well, that sounds like VIP speaker support to me.
[3950.02 → 3951.86] And I'm glad that it worked so well in practice.
[3952.10 → 3952.48] It was.
[3952.64 → 3952.94] It was.
[3953.36 → 3957.98] Yeah, I'm really happy when ideas like that work well out in practice, you know, because
[3957.98 → 3959.56] you never know what's going to happen.
[3960.00 → 3964.00] But it just goes to show that Rubicon is a really well-organized event.
[3964.34 → 3967.52] And there's like so many moving parts to it.
[3967.60 → 3971.76] It's just crazy how much happens behind the scenes.
[3971.76 → 3976.72] And big props to all the organizers and to everyone that made it happen.
[3977.08 → 3979.92] It was difficult because it was both in-person and virtual.
[3980.42 → 3982.40] And I think the combination worked really well.
[3982.58 → 3985.16] But next time, I'm also thinking of going in-person.
[3985.56 → 3988.80] So Valencia, next year, I would very much like to be there.
[3988.86 → 3989.30] And who knows?
[3989.44 → 3990.08] Maybe we'll meet.
[3990.38 → 3991.08] Wouldn't that be nice?
[3991.08 → 3991.52] Right.
[3993.52 → 3994.02] Okay, David.
[3994.10 → 3995.34] Well, thank you for making the time.
[3995.70 → 3996.80] This was an absolute pleasure.
[3997.30 → 3999.58] Looking forward to meeting you at the next Rubicon.
[3999.74 → 4000.54] Thank you for having me.
[4000.54 → 4021.30] I'm Jared Santo, Go Times producer and a loyal listener of the show.
[4021.30 → 4025.86] This is the podcast for diverse discussions from around the Go community.
[4026.34 → 4029.72] Go Times panel hosts special guests like Kelsey Hightower.
[4029.72 → 4035.36] And sometimes you can leverage a cloud provider and make margins on top.
[4035.44 → 4036.64] That's just good business.
[4037.08 → 4040.72] But when we're at the helm making the decision, we're like, yo, forget good business.
[4041.32 → 4045.52] I'm about to deploy Kafka to process 25 messages a year.
[4046.60 → 4048.26] It's nerd pride, right?
[4049.04 → 4051.52] Picks the brains of the Go team at Google.
[4052.08 → 4056.18] You don't get a good design by just grabbing features from other languages and gluing them together.
[4056.18 → 4061.68] Instead, we tried to build a coherent model for the language where all the pieces worked in concert.
[4062.38 → 4065.30] Shares their expertise from years in the industry.
[4065.82 → 4067.50] Don't expect to get it right from the start.
[4067.78 → 4069.08] You'll almost definitely get it wrong.
[4069.16 → 4071.18] You'll almost definitely have to go back and change some things.
[4071.70 → 4076.80] So, yeah, I think it goes back to what Peter said at the start, which is just made your code, write your code in a way that is easy to change.
[4077.44 → 4078.94] And then just don't be afraid to change it.
[4079.20 → 4081.88] And has an absolute riot along the way.
[4081.88 → 4086.26] Yeah, you know that little small voice in your head that tells you not to say things?
[4086.96 → 4087.96] What is that?
[4088.78 → 4089.74] How do you get one?
[4091.36 → 4092.28] You want one of those?
[4092.30 → 4093.56] Is it like an in-app purchase?
[4094.22 → 4095.72] It is go time.
[4096.12 → 4099.88] Please select a recent episode, give it a listen, and subscribe today.
[4100.32 → 4101.52] We'd love to have you with us.
[4101.52 → 4114.18] I'll ask that Stephen was afraid to ask.
[4114.26 → 4115.68] And afraid, I'm doing air quotes.
[4116.22 → 4118.36] What even is six stories?
[4119.30 → 4120.86] So, that's a funny story, actually.
[4120.98 → 4125.12] That question came from a chat between me and Stephen, and we were just messing around a little bit.
[4125.16 → 4127.34] So, I was actually the one that asked that question to Stephen.
[4127.82 → 4128.32] I see.
[4128.98 → 4130.14] That's the story there.
[4130.14 → 4135.90] Yeah, he has a funny habit of dropping my name off and then posting our conversations, which I'd love to read on Twitter.
[4136.00 → 4136.38] He's great.
[4137.96 → 4139.40] Okay, so what did he answer?
[4140.64 → 4141.78] What do you ask if that?
[4141.92 → 4142.50] He just didn't.
[4143.74 → 4148.46] Yeah, so SIG Store is an open source project that's part of the Linux Foundation.
[4148.94 → 4154.14] It's not like a lot of traditional open source projects because there's a bunch of awesome code on GitHub and the community.
[4154.14 → 4161.38] But it also has some production infrastructure that that community is operating as a public benefit for the rest of the open source world.
[4161.38 → 4163.22] So, there's a bunch of code, which is awesome.
[4163.32 → 4163.80] You can fork it.
[4163.86 → 4164.58] You can contribute to it.
[4164.62 → 4170.16] But we also maintain a running copy of that code for people to use day-to-day and use in production.
[4170.16 → 4172.22] So, it's a couple different components.
[4172.44 → 4179.34] But overall, the goal of the SIG Store project is to make it easy and free to sign and verify open source software.
[4179.82 → 4181.90] We were heavily inspired by the Let's Encrypt model.
[4182.02 → 4186.62] So, if you're familiar with Let's Encrypt, what Let's Encrypt did operating a free certificate authority for web browsers.
[4187.16 → 4191.66] They made it so all the web traffic became encrypted over a couple of years.
[4191.66 → 4198.92] CS have been around since the early 90s, but we just weren't seeing much movement in the percentage of web traffic that was encrypted.
[4199.12 → 4203.96] All the websites still had that red X at the top years and years ago, if you remember what it was like before Let's Encrypt.
[4204.24 → 4209.02] And then they solved the problem by making it free, easy, and automated to do it.
[4209.12 → 4213.84] So, now with one line in your Kubernetes AMLS now, you can just get free certificates for everything.
[4214.40 → 4221.18] And not overnight because a ton of hard work went in from the Let's Encrypt people compared to the overall timeline the internet's been around.
[4221.18 → 4223.80] The shift was immediate almost.
[4224.24 → 4226.98] So, we tried to do the same thing for open source software.
[4227.82 → 4229.72] How is this different from PGP?
[4229.90 → 4230.94] Yeah, that's a great question.
[4231.20 → 4232.68] So, PGP has been around for a while.
[4232.92 → 4237.28] PGP is a bunch of open source standards for cryptographic operations.
[4237.60 → 4245.96] So, this includes things like signing, verification, but also things like encryption of files, of messages, of all of these different things.
[4246.34 → 4249.82] So, PGP is kind of like a huge cryptographic kitchen sink.
[4249.82 → 4256.42] And it also provides some basic primitives for kind of PKI and key distribution and things like that are pretty opinionated.
[4256.70 → 4265.94] If you've ever heard of like key signing parties and the PGP web of trust and stuff like that, it's a really cool, really elegant model that just unfortunately hasn't caught on too much today.
[4265.94 → 4268.48] So, SIG Store takes a slightly different approach.
[4268.74 → 4271.96] We use some different encryption standards, some slightly more modern ones.
[4272.30 → 4278.96] And particularly, we really rely on things like transparency logs, which kind of weren't really around back when PGP got started.
[4279.08 → 4284.42] They've really taken off across the browser ecosystem in probably the last decade.
[4284.42 → 4286.54] I think it hasn't been quite that long.
[4286.66 → 4288.24] But they have a lot of benefits.
[4288.50 → 4290.16] More PGP is completely decentralized.
[4290.78 → 4292.64] Transparency logs are slightly more centralized.
[4293.26 → 4297.60] But they provide some cool guarantees where there's a central operator, but you don't actually have to trust them.
[4297.94 → 4300.10] So, you get a lot of the benefits of both worlds.
[4300.28 → 4302.14] Somebody can run a service for you, which is easy.
[4302.26 → 4303.02] Everybody can find it.
[4303.08 → 4303.82] Everybody can use it.
[4304.06 → 4305.66] But you don't actually have to trust that operator.
[4305.66 → 4307.88] The only thing you have to trust is if they'll keep the thing running.
[4308.32 → 4314.78] And people can make backups and mirrors, but they can't tamper with that log, which eliminates a lot of the problems with centralized infrastructure.
[4315.38 → 4315.42] Okay.
[4315.68 → 4321.44] So, one of the things that I always use PGP for is signing my Git commits.
[4321.70 → 4321.80] Right.
[4321.94 → 4329.60] So, I'm wondering what else should I be signing, and what should I be using from the SIG Store ecosystem to sign things?
[4329.88 → 4330.08] Yeah.
[4330.18 → 4332.54] So, signing Git commits is a pretty important topic.
[4332.54 → 4339.50] Like, there's like the git commit dash capital S flag, you know, which uses your PGP key ring, which is set up in your computer to sign those commits.
[4340.24 → 4342.80] That integration is actually baked pretty heavily into Git.
[4342.98 → 4345.34] So, there's, you know, dozens of different ways to sign things.
[4345.46 → 4346.60] SIG Store isn't the only way either.
[4346.82 → 4349.42] But Git is pretty coupled to PGP today.
[4349.74 → 4351.24] There's actually a bunch of ongoing work.
[4351.24 → 4357.44] Some of the Git core maintainers and some other contributors to start refactoring that and making it so that Git can use other techniques to sign things.
[4357.44 → 4362.54] And so, we're helping with that work to hopefully make SIG Store also kind of like a first-class citizen in the Git signing world.
[4363.38 → 4365.46] But separately, you know, you want to sign everything.
[4365.62 → 4367.06] It's kind of where we're going here in this world.
[4367.56 → 4368.46] Signing commits is great.
[4368.58 → 4373.10] They can be used to kind of back up and, you know, provide other guarantees about who actually authored those commits.
[4373.62 → 4378.90] As they travel from your computer to GitHub to forks across GitHub to package managers and everything like that.
[4379.24 → 4381.54] That's just one link in the supply chain.
[4381.54 → 4385.82] Software supply chain security has been a huge hot topic over the last couple of years.
[4386.78 → 4390.04] And signing commits is kind of the first step, right?
[4390.16 → 4390.94] You're on a computer.
[4391.10 → 4392.26] You're typing code on your keyboard.
[4392.46 → 4394.34] That is the birth of software, right?
[4394.40 → 4396.36] As that code gets entered into your editor and stuff.
[4396.46 → 4397.80] And so, signing that makes a lot of sense.
[4398.30 → 4403.78] As it gets pushed up to a repository, and it gets tagged, you want to sign those tags too, so somebody knows that the release was authorized.
[4404.64 → 4409.74] As those tags get pulled down and compiled into artifacts, it makes sense to start signing those too.
[4409.74 → 4412.58] And that's where SIG Store is starting to see the most adoption right now.
[4413.04 → 4422.94] And signing various release artifacts that could be zip files or tarballs or more commonly today we're starting to see container images used for, you know, generic package management artifacts.
[4423.68 → 4428.72] And so, one of the projects in SIG Store called Cosign is, you know, dedicated to signing container images.
[4429.30 → 4438.32] And the kind of cool thing is because the container image standards have gotten so pervasive, we're starting to see people cram other things into container images that aren't even container images.
[4438.32 → 4438.88] Oh, yes.
[4438.88 → 4446.36] So, like the new WebAssembly modules have a little specification for how to store those in a container image without having to build a whole new package manager.
[4446.86 → 4452.20] So, all of these artifacts that come out, you know, from your build system, from your CIC system are very important to sign too.
[4452.28 → 4454.10] Because there are tons of different attacks that could happen.
[4454.30 → 4459.86] And then kind of lose that link between an opaque binary blob and the source code repository it actually came from.
[4459.86 → 4468.78] I think Go has possibly the best time when it comes to signing because you can do from scratch, and then you don't worry where from scratch comes from.
[4469.04 → 4469.68] I think.
[4469.96 → 4470.38] I think.
[4470.52 → 4471.84] Because from scratch it's just empty.
[4471.92 → 4472.58] There's nothing there.
[4472.74 → 4475.42] But what about when you do, for example, from Ubuntu?
[4475.74 → 4477.14] That happens still quite a bit.
[4477.14 → 4483.86] Can you use cosine to check that from Ubuntu that not just that layer, but everything underneath has been signed?
[4484.04 → 4485.04] Does that exist today?
[4485.36 → 4485.60] Yeah.
[4485.76 → 4490.40] So, we're talking about kind of base images and image hierarchies and stuff here when it comes to container images.
[4490.86 → 4491.10] Yeah.
[4491.24 → 4492.04] A couple of things there.
[4492.24 → 4500.32] Go has some awesome support for kind of static compilation of a Go binary, which means you can throw it into a container image without any of the other operating system runtime stuff.
[4500.72 → 4500.84] Yeah.
[4500.86 → 4502.32] So, if you do from scratch, that's awesome.
[4502.46 → 4502.78] You don't have.
[4502.88 → 4504.04] There's no base image to check.
[4504.04 → 4506.94] The only thing in there is your binary and some configuration.
[4507.64 → 4508.94] So, you can sign that resulting image.
[4509.06 → 4510.88] In that case, you know, there's no base image to check.
[4510.96 → 4514.54] And you can actually look at a container and prove that it was from scratch later after it was built.
[4514.94 → 4516.52] There would only be one layer inside of that.
[4516.62 → 4517.28] You don't have to worry.
[4517.90 → 4524.78] There's been some other recent work in the OCI or the Open Containers Initiative to start propagating a lot more metadata around.
[4524.96 → 4525.04] Right?
[4525.04 → 4533.34] One of the issues is that it's been around for a while is that if you did from Ubuntu and threw a Go application into there, it's really hard to figure out after it was built that it was actually from Ubuntu.
[4533.34 → 4535.16] Or which Ubuntu that was.
[4535.38 → 4544.52] But a couple of months ago, one of my colleagues, Jason Hall at Red Hat, finally got a new field approved in the OCI specification for a standard base image annotation.
[4545.00 → 4552.50] So, build tools can start setting that in these JSON manifests to indicate which Ubuntu was used, where it was found, what the digest of that was at that time.
[4552.50 → 4554.00] And you can kind of actually check that later.
[4554.10 → 4555.68] So, you don't even really need to trust that tool.
[4556.08 → 4558.64] So, it's all about kind of leaving these breadcrumbs around.
[4558.86 → 4563.68] And so, now that we have that new breadcrumb, you know, from the fairy tale, you know, you can follow that back.
[4563.76 → 4568.16] You can find the Ubuntu image, and you can check to see if that was signed by the original publisher.
[4568.66 → 4568.82] Yeah.
[4568.82 → 4572.02] So, this is something that just in the last couple of months has started becoming possible.
[4572.28 → 4572.30] Yeah.
[4572.50 → 4573.20] That's really cool.
[4573.20 → 4583.22] A good use case there, if you want to see that in practice, is actually something kind of fits right between From Scratch and Ubuntu, which are the distro-less base image suite, if you're familiar with those.
[4583.34 → 4583.54] Yes.
[4583.66 → 4583.86] Yeah.
[4583.90 → 4585.82] So, they're way closer to From Scratch.
[4585.92 → 4589.44] They have just a couple of other files you might need, even if you have a static Go application.
[4590.04 → 4597.30] Things like CA certificates, time zone data, they're just kind of a bunch of small text files that your application might need or expect to be in certain places.
[4597.30 → 4601.96] And those are actually built and signed with the SIG store tooling.
[4602.06 → 4602.38] Interesting.
[4602.56 → 4605.14] And they have a bunch of other cool properties, like they're reproducible.
[4605.36 → 4611.24] And so, we have a bunch of different build systems reproducing those builds and publishing and kind of proofs that they reproduce them.
[4611.32 → 4615.92] And so, you can look all of that up in our transparency log and verify it all the way back to the Form Scratch.
[4616.08 → 4619.20] As far as I know, distro-less is a concept that comes from Google.
[4619.44 → 4622.24] And I'm wondering, is that something that you were involved with, distro-less?
[4622.48 → 4622.72] Yeah.
[4622.72 → 4626.60] So, I started that project with Linker Workers Map more years and years and years ago.
[4626.60 → 4630.50] So, we kind of did it as a proof of concept to show what some of this stuff looked like.
[4630.58 → 4634.80] We were playing around with the Basel tool set at that time, and we got reproducible container builds working.
[4635.06 → 4635.70] It was pretty cool.
[4636.16 → 4637.24] He gave a talk at a conference.
[4637.38 → 4639.44] I think it was like a Frog swamp up.
[4639.60 → 4641.60] And we just kind of kept playing with the repository.
[4642.16 → 4643.88] Didn't really expect much to come out of it.
[4644.02 → 4650.20] And then a couple of years later, like what happens in open source, the Kubernetes release engineering team, so Stephen Augustus and his crew,
[4650.20 → 4655.38] moved all the Kubernetes-based images from, I think, Debian or something like that to distro-less.
[4655.38 → 4656.98] Without even really telling us.
[4657.08 → 4661.88] And so, all of a sudden, overnight, this became like a piece of critical infrastructure for the entire container ecosystem.
[4662.32 → 4664.24] What started is like a little hobby project.
[4664.94 → 4665.14] Wow.
[4665.44 → 4667.78] I'm connecting some very important dots right now.
[4667.98 → 4669.76] Why we don't have the time to go into this.
[4669.82 → 4674.18] You have no idea how relevant this is to many of the topics and threads that I have in the background.
[4674.38 → 4678.10] I intend to come back to this in a few months, maybe a few weeks, but I'm thinking months.
[4678.10 → 4681.36] But I would like to talk about the big news right now.
[4681.84 → 4684.88] And that is the Chain guard About page.
[4686.56 → 4688.76] That's one of my favourite About pages.
[4689.48 → 4690.94] Can you tell us the story about that?
[4690.98 → 4691.22] So, okay.
[4691.26 → 4694.34] So, first, let me explain how it works because I love that.
[4694.34 → 4703.26] So, if you go to chainguard.dev or slash about, and you click on the faces of the different people that are part of Chain guard, something amazing happens.
[4703.50 → 4704.90] And I'll let you discover that.
[4705.44 → 4708.06] But can you tell us the story behind it, Dan?
[4708.64 → 4709.00] Sure.
[4709.10 → 4709.24] Yeah.
[4709.24 → 4714.30] My version of the story is that we announced Chain guard, our new company, a couple of weeks ago.
[4714.62 → 4718.78] Scott Nichols, one of our co-founders, was working very hard on that website to get it set up.
[4719.02 → 4721.10] I can't do any kind of design at all.
[4721.26 → 4723.54] I'm terrible at front-end stuff and everything like that.
[4723.54 → 4725.98] So, you know, I hadn't even really been paying too much attention to it.
[4726.48 → 4728.12] And the website went out, and it was awesome.
[4728.46 → 4732.12] And then everybody on Twitter just started laughing and telling all these jokes about the About page.
[4732.16 → 4733.34] And I had no idea what was happening.
[4733.46 → 4735.04] And they were talking about all of these Easter eggs.
[4735.20 → 4738.62] And it took me a couple of days before somebody finally showed me what was happening.
[4738.90 → 4743.54] But, yeah, Scott put in a really fun Easter egg about my hair here that we're talking about now.
[4743.58 → 4748.14] Where if you click on anybody's faces on the About page, you get a pretty cool effect.
[4748.54 → 4748.82] Okay.
[4749.04 → 4749.32] So.
[4749.84 → 4750.90] That is your hair, too?
[4751.48 → 4751.88] Okay.
[4751.88 → 4756.70] I think it's a Photoshopped, exaggerated version of my hair.
[4757.06 → 4757.28] But, yeah.
[4758.50 → 4760.34] Has the pandemic something to do with it?
[4761.46 → 4761.70] Okay.
[4761.84 → 4762.06] Yeah.
[4762.14 → 4765.22] So, my hair has had a couple phases in the last few years.
[4765.50 → 4768.38] But, yeah, I basically haven't gotten it cut since the pandemic started.
[4769.00 → 4772.00] There was a brief phase where I have very curly hair.
[4772.12 → 4774.22] And it was kind of just kind of going out like this for a while.
[4774.36 → 4775.96] But as you can tell now, it kept growing.
[4776.08 → 4777.58] It has now collapsed under its own weight.
[4777.58 → 4778.98] And it's fallen down.
[4779.18 → 4779.32] Yeah.
[4779.36 → 4782.16] So, those pictures are a little, that hair is a little outdated.
[4782.32 → 4783.94] But it did look like that at one point in time.
[4784.14 → 4784.64] That's crazy.
[4784.84 → 4786.68] That is my favourite part, by the way.
[4787.56 → 4790.78] I think he was looking at the analytics stats for our page.
[4790.86 → 4792.14] Because we put a little analytics thing on there.
[4792.14 → 4795.00] And the About page has more views than anything else on the website right now.
[4795.30 → 4798.64] So, we'll just pile on top of that.
[4798.82 → 4800.18] So, that's the most important page.
[4800.98 → 4801.36] All right.
[4801.60 → 4803.62] The effect on Kim, I think it looks the best.
[4804.34 → 4805.56] I tried to pull the faces.
[4805.90 → 4807.64] But I think on her, it suits her.
[4808.48 → 4808.84] Yeah.
[4808.88 → 4811.22] I didn't even realize he did it for all the faces at first.
[4811.34 → 4812.18] I thought it was just mine.
[4812.34 → 4812.44] Yeah.
[4812.48 → 4815.94] It took me a little bit to realize the full extent of the Easter egg.
[4816.46 → 4819.24] Any other Easter eggs that you're aware of that we should check out?
[4819.24 → 4820.18] Not that I'm aware of.
[4820.18 → 4821.28] You can ask Scott Nichols.
[4821.56 → 4822.70] He probably hit a few more.
[4823.48 → 4824.52] Stop working on features.
[4825.00 → 4826.24] Give us more Easter eggs.
[4827.14 → 4827.50] Perfect.
[4827.62 → 4831.64] So, why do you think that the world needs Chain Guard, Dan?
[4831.68 → 4831.88] Yeah.
[4831.92 → 4833.06] I think we need something here.
[4833.24 → 4837.44] So, I've been working on software supply chain security for probably the last greenish years.
[4837.52 → 4839.18] Kind of, you know, full-time almost.
[4839.66 → 4841.80] I got worried about it a little bit before then.
[4842.26 → 4842.84] But, yeah.
[4842.86 → 4845.30] I've been doing kind of nothing but that for about the last three years.
[4845.42 → 4846.50] Most of that time was at Google.
[4847.28 → 4850.22] And I'll tell you, three years ago, nobody even understood it.
[4850.30 → 4851.46] The term wasn't around.
[4851.94 → 4853.00] Nobody cared about it.
[4853.06 → 4854.52] We were kind of running around telling everybody,
[4854.52 → 4856.74] you should be paying attention to what goes into these containers.
[4856.74 → 4858.58] And everybody said, we have other problems.
[4858.70 → 4859.22] This is fine.
[4860.04 → 4863.98] Until probably a year and a half ago is when things started to turn around.
[4864.02 → 4869.70] We started getting all these reports of different open source libraries being attacked or taken over by malicious actors.
[4869.70 → 4873.70] Companies started having internal attacks, insider threats.
[4873.70 → 4882.10] Finally, the kind of huge one, the tipping point was the famous attack on SolarWinds back in December of last year, the sunburst attack.
[4882.52 → 4885.32] And that kind of led to, you know, the downstream effects of that.
[4885.42 → 4890.66] All the customers at SolarWinds had the impact kind of led to the whole shift kind of overnight.
[4890.80 → 4893.44] And people saying, hey, we haven't paid attention to this for years.
[4893.48 → 4894.02] What's going on?
[4894.06 → 4895.14] Let's go try to fix this.
[4895.14 → 4895.62] Yeah.
[4895.78 → 4897.20] Led to, you know, government regulations.
[4897.44 → 4899.12] The EU is working on new standards.
[4899.36 → 4910.10] The U.S. government put out an executive order calling for institutions to start figuring out what to do and kind of change the way that we build software to fix all of this, make it more secure.
[4910.28 → 4915.64] Leave a lot more of this kind of verifiable breadcrumbs we talked about around to make a lot of these attacks harder.
[4915.64 → 4918.22] I'm really glad that the world is taking this seriously.
[4918.38 → 4919.10] It was high time.
[4919.64 → 4921.68] And thank goodness nothing worse happened.
[4921.84 → 4924.38] But it is obvious that we have to act fast on this.
[4924.50 → 4931.56] And I'm glad that you, first, are a small team of crazy people that really believe in this.
[4931.80 → 4935.02] I think that is the best way of driving change.
[4935.38 → 4937.60] And I'm glad that many other companies are paying attention.
[4937.86 → 4943.62] So I'm sure over the next year, next two years, this will just grow in popularity and importance.
[4943.62 → 4947.42] And I'm glad that someone like you is steering this.
[4947.48 → 4948.62] And I tell you, I mean Chain Guard.
[4949.36 → 4950.10] Well, thank you.
[4950.46 → 4953.52] So I know that you're back from Rubicon now.
[4954.02 → 4956.28] Rubicon is over for you, at least in person.
[4956.50 → 4958.14] What was it like to be there in person?
[4958.32 → 4959.90] It wasn't as weird as I thought.
[4960.08 → 4962.38] You know, I hadn't been around big crowds of people in a while.
[4962.48 → 4963.34] You know, it's been a long time.
[4963.46 → 4967.08] I was at one smaller conference a couple of weeks ago just starting to warm back up to it.
[4967.16 → 4968.62] And it was just awesome to see the energy.
[4968.62 → 4977.52] And, you know, I could tell the whole community needed this to kind of just get back together, set aside some time to talk about open source and kind of relax a little bit.
[4977.92 → 4981.46] Because as things start to get back to normal, it was exhausting, though.
[4981.56 → 4982.46] I'll say that.
[4982.70 → 4983.92] You know, it's a long week.
[4983.98 → 4985.46] Those conference sessions are long days.
[4985.48 → 4988.42] And I think I just forgot how tiring these conferences can be.
[4988.68 → 4991.44] I know that you had also Supply Chain Security Con.
[4991.82 → 4994.94] I almost called it Supply Chain Con, which would have been crazy.
[4994.94 → 4995.94] No, no.
[4996.04 → 5002.32] Supply Chain Security Con, Kim referred to it as a negative one event, which I think is important in relation to Rubicon.
[5002.46 → 5003.10] I really like that.
[5003.40 → 5004.10] How is that?
[5004.24 → 5004.42] Yeah.
[5004.54 → 5007.58] So Supply Chain Security Con was a day negative one event.
[5007.68 → 5008.74] I think I kind of made up that term.
[5009.20 → 5014.50] Rubicon has kind of had a long history of having day zero events or co-located events the day before the conference.
[5015.12 → 5017.88] There's just been so many topics to cover in so long since we've had a Rubicon.
[5018.16 → 5019.76] The organizers decided to have two of those.
[5020.12 → 5022.78] So the Monday of this week, the conference officially started on Wednesday.
[5022.78 → 5027.86] But the Monday of this week, we started off with a day negative one event called Supply Chain Security Con.
[5028.30 → 5032.22] The Continuous Delivery Foundation and a bunch of other companies helped sponsor and put together.
[5032.88 → 5033.28] Okay.
[5033.82 → 5038.64] So this makes me think of the coolness wall at Top Gear.
[5038.86 → 5039.72] I don't know if you remember that.
[5039.82 → 5042.74] I don't know if you watch Top Gear, but they had a wall, and they used to rank cars.
[5043.30 → 5045.66] And Sub-Zero were the really cool ones.
[5045.94 → 5049.70] The really, really like Sub-Zero is like the coolest car category they had.
[5049.70 → 5053.12] So negative one sounds like a bit like Sub-Zero to me.
[5053.34 → 5054.44] I think there's a link there.
[5055.06 → 5058.62] So as we are preparing to wrap this up, I have two more questions.
[5058.94 → 5060.28] Your favourite Rubicon moment?
[5060.68 → 5062.22] What is coming next in the six months?
[5062.48 → 5066.48] Oh, my favourite Rubicon moment was the talk from John Johnson Jr.
[5066.78 → 5071.12] and Dan Magnum on crazy things you can do with OCI registries.
[5071.40 → 5071.74] Oh, yes.
[5071.74 → 5075.72] I can't wait until that recording gets posted, but you might have seen some of the buzz around on Twitter.
[5075.96 → 5081.24] But they actually built a chat application that worked inside OCI compliant container registries.
[5081.76 → 5082.60] And that was just awesome.
[5082.82 → 5086.46] They answered the actual Q&A for the talk using this chat application.
[5086.78 → 5092.08] So the audience was there asking questions and layers and container images were getting thrown around to make it all work.
[5092.50 → 5093.54] But that was awesome.
[5093.64 → 5094.52] That was my favourite moment.
[5094.52 → 5094.96] Amazing.
[5096.22 → 5098.90] What's happening in the next six months for Chain Guard, for you?
[5099.44 → 5100.14] Anything interesting?
[5100.44 → 5101.08] We're getting a haircut.
[5102.24 → 5102.68] Probably.
[5103.08 → 5103.52] Probably.
[5103.70 → 5105.08] It's getting a little long at this point.
[5105.66 → 5109.94] But yeah, for Chain Guard, we're figuring out what we're going to be doing, getting our feet under ourselves
[5109.94 → 5115.70] and just trying to stay focused and double down on the awesome momentum we've had in SIG Store
[5115.70 → 5119.48] and continuing to push that forward across all the different language ecosystems
[5119.48 → 5122.90] and package managers and container images around the world.
[5122.90 → 5126.64] So yeah, look for hopefully even more SIG Store adoption than we're already seeing
[5126.64 → 5129.10] and then us starting to figure out what we're doing as a company.
[5129.52 → 5131.02] Dan, thank you very much for making the time.
[5131.30 → 5132.50] This has been an absolute pleasure.
[5132.74 → 5136.16] I'm looking forward to next time and I hope it won't be that long before we meet again.
[5136.48 → 5137.14] Thank you very much.
[5137.62 → 5138.72] Thanks a lot for having me.
[5142.22 → 5144.66] Thank you for tuning into another episode of Ship It.
[5144.88 → 5146.72] I enjoyed making it for you.
[5147.12 → 5150.44] This is just one of the podcasts for developers that we ship.
[5150.44 → 5154.20] Go to changelog.com forward slash master for the rest.
[5154.82 → 5160.78] You can join me and the rest of our community at changelog.com forward slash community.
[5161.42 → 5162.96] There are no imposters in our Slack.
[5163.38 → 5164.60] Everyone is welcome.
[5164.98 → 5169.06] Huge thanks to our partners Vastly, Launch Darkly and Minor.
[5169.34 → 5172.70] Thank you, Break master Cylinder for all our awesome beats.
[5173.14 → 5174.32] That's it for this week.
[5174.54 → 5175.38] See you next week.
[5175.38 → 5202.44] We'll be right back.
[5202.44 → 5204.26] Game on.
[5204.26 → 5208.20] tab

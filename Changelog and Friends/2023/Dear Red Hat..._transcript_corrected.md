[0.00 → 20.60] Welcome to Change Login' Friends, a weekly talk show about pirating open source software.
[21.12 → 24.90] Thanks to our partners for helping us bring you awesome pods each and every week.
[24.90 → 30.52] Shout out to FASI.com, Ply.io, and Typesense.org.
[31.02 → 32.18] Okay, let's talk.
[37.14 → 39.92] So we're here with an inflammatory enigma.
[40.94 → 41.98] It's Jeff Deerling.
[42.04 → 45.32] I read that on your Twitter bio, so I assume that's what you are.
[45.58 → 46.34] Hey, Jeff.
[47.00 → 51.94] That actually has to do with my IBD, internal bowel disease, and I don't even remember.
[52.16 → 52.54] Oh boy.
[52.54 → 56.04] I have Crohn's disease, so my doctor called me that one time.
[56.20 → 60.30] But I think if you work at Red Hat, you might agree with my doctor.
[60.32 → 64.80] I thought maybe it was on point, you know, for the recent current events.
[64.94 → 67.80] I thought, wow, he has been inflaming things a little bit around here.
[68.14 → 68.64] For sure.
[69.42 → 71.50] I would call it kicking hornet's nest, really.
[71.96 → 77.68] I feel like they put this post out there, they being Red Hat, and you responded very clearly.
[77.68 → 80.28] In some cases, calling them dumb.
[81.08 → 82.34] Literally calling them dumb.
[82.96 → 85.08] You know, and laying out all the reasons.
[85.30 → 91.16] But like, can you explain what exactly is happening right now to kind of give some context to this conversation?
[91.84 → 92.08] Yeah.
[92.08 → 98.56] I mean, I've worked in the Red Hat ecosystem from the earliest time that I got into Linux.
[98.74 → 104.08] The first thing that I ever did on Linux was I bought Red Hat 5.2 in a CD on the back of a book.
[104.08 → 106.28] And that was when it was Red Hat Linux.
[106.50 → 113.18] And that was when the whole enterprise thing and the licensing games and things hadn't been really started yet.
[113.52 → 115.90] And it was kind of a heady time in the Linux world.
[116.18 → 123.34] And that was when they were going from like, this is a hobbyist thing to this is a commercial thing to this is an enterprise thing.
[123.36 → 126.80] And we're fighting Microsoft and fighting all these big, huge things in Unix.
[127.04 → 127.36] Right.
[127.60 → 129.50] So I wasn't super involved back then.
[129.54 → 131.02] I was doing graphic design more.
[131.16 → 131.94] So I was on a Mac.
[131.94 → 134.44] But as the years went on, I kept following it.
[134.58 → 140.78] And then I got back into the ecosystem when I needed to host my graphic design things, which are nowadays web projects.
[141.28 → 142.78] I needed to host them somewhere.
[143.00 → 144.52] And CentOS was the only option.
[144.60 → 153.92] I wasn't going to spend hundreds of dollars a month or, you know, a thousand bucks a year or whatever, just to host my little blog or the little small business website or whatever.
[154.08 → 159.00] And CentOS was seen as this thing that was enterprise-y but free.
[159.40 → 161.10] So, yes, I was a freeloader.
[161.10 → 163.26] But that got me into the ecosystem.
[163.50 → 164.22] So, does it?
[164.58 → 169.06] I started figuring out how to automate things with Bash and how to do more Linux-y things.
[169.16 → 172.14] I found out about other Linux distros through CentOS, all the stuff.
[172.20 → 176.86] But it was my gateway drug into the Linux ecosystem where I was a Mac guy, really.
[176.86 → 182.32] And I used Windows and managed Windows NT and did a little Novel stuff at work.
[182.42 → 183.98] But I was generally a Mac guy.
[184.18 → 194.32] And that really got me into the Linux ecosystem to the point where when Ansible came out, I was big on the Ansible train and wrote basically the book on Ansible for a long time.
[194.32 → 198.20] Besides all that, I would say that I am a contributor.
[198.62 → 200.50] I'm not completely a freeloader anymore.
[200.50 → 208.24] But when I saw the statements that were being made around this whole CentOS thing where it's like we took CentOS, then we killed CentOS.
[208.30 → 209.62] And we came out with CentOS Stream.
[209.62 → 217.72] If you reread those blog posts, the words seem very disingenuous from an interpretation of somebody who used CentOS.
[217.90 → 220.42] It's like, well, CentOS Stream will allow you to contribute more.
[220.60 → 225.44] It's like, well, I wasn't asking to contribute to Red Hat Linux or Red Hat Enterprise Linux.
[225.44 → 227.58] I was asking to contribute to the ecosystem.
[227.78 → 228.46] I used Fedora.
[228.64 → 230.22] I did all kinds of things.
[230.30 → 231.34] I promoted Fedora.
[231.48 → 232.40] I promoted CentOS.
[232.40 → 240.56] And I even, at a couple places where I worked, I deployed systems that had over 1,200, 1,300 Red Hat licensed systems.
[241.18 → 245.10] So, you know, it's like my gateway into that world was CentOS.
[245.10 → 250.84] So the words that they used when they said basically like all these users, you can just use Stream.
[251.58 → 256.76] There's a reason why Rocky and Alma came up out of that mess and became so popular.
[256.76 → 263.94] Because so many people, especially little hosting companies, I know a ton of people who manage hosting for nonprofits or small businesses and things.
[264.24 → 266.68] There's no way that they could use Red Hat Enterprise Linux.
[266.90 → 268.50] And they enjoyed using CentOS.
[268.62 → 277.14] So when Rocky and Alma came in, they switched to those because it's like, well, you know, you got Debian, which is usually an option, or this other thing that is supported for five or ten years.
[277.14 → 284.22] And it seems like they didn't consider that portion of the community at all when they were making these decisions.
[284.22 → 297.12] It sounds like it was completely a commercial side thing where it's like, you know, CIQ or whoever is taking customers and using free software built on top of Red Hat or rebuilt.
[297.36 → 302.68] They don't contribute anything to the ecosystem when, in fact, many of the employees there actually do contribute upstream.
[303.30 → 306.54] But, of course, those things, we can ignore that because all they're doing is rebuilding Red Hat.
[306.54 → 313.92] But I think, to me, the thing that offended me and the reason I said, are you dumb, is because it was just such a smack in the face.
[314.10 → 316.94] Like, this is most of the sysadmins I know.
[317.42 → 323.20] Almost all the homemakers I know who are in the Red Hat ecosystem pretty much to a T came in through CentOS.
[323.68 → 327.44] And when CentOS was taken away, we were all like, oh, my gosh, the world is ending.
[327.64 → 330.68] But then Rocky and Alma came in, and we're like, okay, we'll stay in the ecosystem.
[331.20 → 331.26] Right.
[331.26 → 335.52] And now those are, you know, enemy number one, it seems.
[335.52 → 339.10] And the craziest thing was early on in this, I said, Red Hat, are you dumb?
[339.28 → 340.54] I really wanted to make a point.
[340.62 → 343.62] I wanted to talk to some of the people internally at Red Hat who I had worked with.
[343.80 → 346.38] Like, look, this is going to blow up in your face.
[346.44 → 347.44] This is a dumb decision.
[347.66 → 350.36] You need to figure out a way to make the community not hate you.
[350.84 → 359.92] Then they came out with a second blog post that basically it implied that hobbyists and hackers would not be good for the commercial Linux ecosystem.
[359.92 → 361.34] And it's like, yeah, hold on a second.
[361.42 → 363.54] That's kind of where everything comes from.
[363.74 → 364.10] Yeah.
[364.28 → 365.34] You're high and mighty power.
[365.44 → 367.50] You're $34 billion sale to IBM.
[368.12 → 368.98] Where did it come from?
[369.02 → 372.08] It didn't come from Microsoft and the Unixes.
[372.48 → 375.10] It came from the community of hobbyists and hackers.
[375.66 → 383.54] And then they, you know, Mike McGrath clarified in a post on LinkedIn that never on their official blog or anywhere that, oh, we don't mean you when we're talking about freelancers.
[383.54 → 386.04] We just mean the rebuilds or the rebuilders.
[386.04 → 386.22] Right.
[386.32 → 387.52] They always call them the rebuilders.
[387.86 → 390.98] And it's like, well, but I'm still in those communities.
[391.22 → 395.80] So you kind of mean me, but you also kind of don't just because I contribute some things upstream.
[395.94 → 401.72] But in my philosophy, open source free software is about the community, the users.
[402.20 → 404.36] You don't have to contribute to be part of that.
[404.90 → 411.26] And for a lot of people, the first thing you do is just grab a project, and you might change one line of code or a comment and recompile it.
[411.34 → 412.36] Like, that's a step.
[412.36 → 420.44] But they're saying philosophically, their thing is if you go into it, it's like, well, CIQ was taking these contracts and starting to sell it.
[420.54 → 422.08] And it's like, well, that's a different thing.
[422.14 → 426.88] That I'm talking open source philosophy, free software, the ecosystem, the community.
[426.88 → 428.78] They're talking about commercial things.
[429.30 → 441.78] And what I see as their end user license agreement workaround, I see that kind of like playing with the community and kind of playing fast and loose with what brought them to where they were.
[441.78 → 444.84] Because Red Hat came out of the Linux ecosystem.
[445.26 → 448.82] Red Hat uses a kernel that is developed by other people, not just them.
[449.28 → 452.02] So you can tell I'm a little passionate about this.
[452.12 → 452.40] For sure.
[452.80 → 453.48] Rightly so.
[453.48 → 462.54] I mean, Red Hat wants to control, you know, the downstream that comes from an enterprise Linux that is based upon RHEL, essentially.
[462.54 → 471.44] And by locking up and no longer providing these distros or their downstream to Rocky, Alma, etc.
[471.44 → 480.48] They essentially are locking out their ability to, not impossibly, but just hardly be bug-free, bug-compatible, which is their biggest ploy.
[480.62 → 485.02] Like, hey, we want to give you what CentOS was in an enterprise Linux free and open source way.
[485.10 → 486.92] And that's just, they want to control it.
[486.92 → 487.20] Yeah.
[487.36 → 496.60] Which, from an IBM billion dollars, you know, IPO-ed Red Hat prior to acquisition, totally makes sense to, as a business control.
[496.78 → 500.76] But you have to take into account, like you had said, the community and the users.
[501.04 → 505.26] And I don't know about you, Jeff, but I'm not in the same community and only one community.
[505.32 → 506.86] I'm in many different communities.
[506.98 → 511.76] So I may, like you had said, not contribute in this way or that way, but I'm also over here, over there.
[511.76 → 518.86] And so they don't take those multifaceted user types into play whenever they make this kind of moves.
[518.94 → 520.84] It's sort of, we want to stop CIQ.
[520.96 → 521.90] We want to stop all the Linux.
[521.96 → 523.64] We want to stop what Rocky's doing.
[524.12 → 528.80] But as a part of doing that, we hurt everybody else because this is what happens.
[529.42 → 529.82] Yeah.
[529.92 → 538.62] And the other part of that, too, is like from the business side, as somebody who does, I don't have as much infrastructure today as I did a few years ago back when I was consulting.
[538.62 → 544.14] But from the business side, when I see this thing with CentOS 8, they said, here's CentOS 8.
[544.50 → 545.08] It's 2019.
[545.38 → 548.06] We're going to have 10 years of maintenance to 2029.
[548.52 → 549.50] Two years into that cycle.
[549.66 → 550.36] Oh, wait a second.
[550.48 → 551.34] No, we're not anymore.
[551.46 → 555.14] It's going to be CentOS Stream, which is a different thing entirely and only gets five years of maintenance.
[555.36 → 561.14] That was like throwing a bomb into the community of thousands of users of CentOS, myself included.
[561.38 → 568.56] I had just finished migrating all of my Ansible work, all my CI environments, all my servers and things that ran that stuff.
[568.62 → 570.06] Over to CentOS 8.
[570.52 → 574.54] And like a week after I finished the last one, that's when that announcement came out.
[574.54 → 575.72] So that was like, bam.
[576.04 → 576.38] Ouch.
[576.58 → 577.12] Thanks a lot.
[577.48 → 580.08] So my trust level goes from here to like down here.
[580.16 → 580.38] Right.
[580.64 → 582.98] I was consulting for Red Hat at this time, too.
[583.46 → 586.46] So I was like, oh, my gosh, this is absolutely wild.
[586.60 → 587.64] I can't believe they did this.
[587.74 → 591.12] But I couldn't say much about it because I was consulting for Red Hat.
[591.60 → 592.38] You can't do that.
[592.52 → 592.76] Yeah.
[592.78 → 593.86] You can't poop on your employer.
[594.04 → 595.76] I don't consult for them anymore.
[595.76 → 596.00] Yeah.
[596.06 → 597.46] Now you can say what you like, though.
[598.86 → 599.62] You're free, Jeff.
[599.68 → 600.04] You're free.
[600.38 → 600.88] Say what you want.
[600.96 → 605.24] So in a couple of years later, you know, Rocky and Alma come up out of this.
[605.54 → 611.46] And people like me are like, thank you for saving all this work I did to convert all my ecosystem to CentOS 8.
[611.56 → 612.78] Now I can just move to Rocky 8.
[613.30 → 614.38] Red Hat 9 comes out.
[614.74 → 618.48] Sources are still being published like they promised they would when they killed CentOS.
[618.88 → 621.26] And we're all like, OK, I'm going to upgrade to 9.
[621.26 → 635.38] So I had just gotten about halfway done with my Ansible migration to Rocky Linux 9 for all my test environments to test all my stuff for Red Hat Enterprise Linux, because I have a ton of users who do use Red Hat Enterprise Linux for my roles.
[635.96 → 637.28] So I'm halfway through this process.
[637.28 → 641.18] And it's like, OK, you know, it's hard this time because I'm not switching to another thing entirely.
[641.18 → 643.16] It's just changing a couple of strings here and there.
[644.06 → 646.28] Halfway through, they announce, oh, you know what?
[646.32 → 647.76] We hate downstreams.
[647.90 → 649.00] It's like, are you kidding?
[649.34 → 652.02] They're like, oh, you know, you can get free licenses.
[652.30 → 654.10] You can get 16 free developer licenses.
[654.24 → 656.52] I'm like, I have over 150 roles.
[657.06 → 658.74] I have over 25 playbooks.
[659.18 → 661.58] Tons of these are being used by Red Hat Enterprise Linux.
[662.04 → 666.66] And you're saying I can take 16 licenses and try to integrate that with my CI environments.
[667.30 → 674.24] And then, you know, after I said that on Twitter, somebody reached out and said, oh, we'll get you one of those infrastructure, like open source infrastructure licenses.
[674.24 → 675.84] It's like, that's not the point.
[675.84 → 676.36] Yeah.
[676.36 → 680.90] Part of the value of that was all the people who could develop for it.
[680.96 → 688.08] And now we have problems with Apple maintainers are needing to get these special licenses to try to get their packages built for Red Hat Enterprise Linux.
[688.08 → 696.58] It seems to me that there was something like some impetus that was probably, I don't know, maybe a VP got offended or something by one of the business contracts.
[696.74 → 703.18] Some people mentioned the NASA thing when Rocky said that, oh, we got three NASA contracts or something for three machines.
[703.18 → 722.56] I don't think it's that, but like something had to have happened that triggered this because it was a pretty sudden and B, there were so many like second level effects that happened that I just like anybody that's in the ecosystem that develops for Red Hat, you would see this like, oh, maybe let's not double down on it right now.
[722.58 → 724.28] Let's let's let this do a little bit.
[724.34 → 726.04] Let's figure out a better way to message this.
[726.44 → 727.80] Let's maybe help people.
[728.00 → 730.24] They keep saying like, oh, just rebase off of stream.
[730.24 → 735.10] Well, maybe if they had announced like, you know what, we were going to do 10 years of Git sources.
[735.24 → 739.54] Now we're going to do five years, and we're going to help these people rebuild off of stream.
[739.62 → 740.72] We're going to give them more options.
[740.82 → 746.80] We're going to help figure out ways to make stream more stable because they still had in their documentation stream is not meant for production.
[747.34 → 758.42] But those two layers of trust destroying exercises with CentOS 8 being killed and then the sources being killed both times early in the release cycle when everybody had started to port things.
[758.42 → 764.40] Those two things make me question anything Red Hat can say about any of their products.
[764.90 → 773.16] And that's why I also am like, well, Ansible, Ansible, the community version that I use, which I don't pay for, is downstream of Ansible automation platform.
[773.38 → 779.88] If that becomes a problem, if people like me sell services for Ansible, but don't use Ansible automation platform, am I the enemy?
[779.98 → 780.76] Am I the freeloader?
[780.76 → 781.24] Yeah.
[782.06 → 783.40] It's a serious question.
[783.72 → 785.78] The Ansible community is structured a little differently.
[785.96 → 789.16] So I don't have as much fear, but I do still have fear.
[789.24 → 791.38] And I didn't have fear a few weeks ago.
[791.58 → 792.04] Now I do.
[792.40 → 797.06] What's weird to me is the you said they kind of despise their downstreams.
[797.06 → 798.14] And it seems like that.
[798.20 → 806.00] Like if you read the TechCrunch did an article today, or maybe it was yesterday about the Size angle to this, which we'll get to, I'm sure, the fork.
[806.00 → 809.08] And they had quotes from Red Hat in there.
[809.18 → 816.52] I don't think it's from, I think it's from Gunnar Ellison, Red Hat's VP and GM for Red Hat Enterprise Linux.
[817.32 → 832.14] And in that article, they likened Alma and Rocky to AWS, which has infamously taken open source projects and provided hosted versions, kind of on top and just kind of crushing the little guy, so to speak.
[832.36 → 832.56] Right?
[832.70 → 833.54] Quote unquote, little guy.
[833.54 → 835.36] We're talking about Elastic, which is not little.
[835.36 → 842.80] But there are littler ones who have their software basically reposted and provided by AWS and a huge competitor.
[843.48 → 848.20] And Red Hat is likening Rocky Linux to AWS in that way.
[848.64 → 850.52] It's like he says they provide zero value.
[850.94 → 852.12] They're like leeches.
[852.50 → 855.06] That's not quoting, but that's the impetus that you get.
[855.36 → 856.22] And you have to be careful.
[856.34 → 864.92] Every time that you mention anything like that, all of a sudden, what I've found is on LinkedIn and Twitter especially, there are tons of Red Hat employees will say, well, quote me that.
[864.92 → 866.06] And like, where did we say that?
[866.12 → 867.40] It's like the word freeloaders.
[867.58 → 872.50] I have heard the word freeloader used in conversation, both working at Red Hat and afterwards.
[872.78 → 874.68] But they've never put it in a blog post.
[874.78 → 875.14] Right.
[875.28 → 877.88] But, you know, people are like, they never said freeloaders.
[877.98 → 881.58] It's like, read the words and look up the definition of freeloader.
[881.70 → 883.60] Like, you're going to see the correlation there.
[883.60 → 888.62] And then Mike put out a blog post saying, yes, we did use the word freeloader, but we're going to stop using that.
[889.68 → 892.26] So I hate that it's a semantic game.
[892.34 → 894.24] I hate that they're playing the games at the GPL.
[894.34 → 898.44] And I hate that they're having to talk about, well, you know, if it gets to a legal battle, we'll probably win.
[898.64 → 900.70] It's like, that's not the spirit of open source.
[900.86 → 903.92] You know, people have said, stop talking about the spirit of open source.
[903.96 → 905.16] It's all about the legal rules.
[905.16 → 913.50] It's like, no, the whole movement comes out of this idea of community, of the fact that software, the bits, are not the thing that provides value.
[913.58 → 914.26] It's the services.
[914.56 → 915.92] It's the support and things like that.
[915.96 → 918.72] And that's how people like me saw Red Hat before.
[918.88 → 924.00] But now I see that Red Hat wants to basically be a consumer of the open source code.
[924.08 → 927.42] And then they want the value stream to end with Red Hat Enterprise Linux.
[927.82 → 929.04] And they can capture all of it.
[929.04 → 936.24] Whereas before, it hit Enterprise Linux, and they let the downstreams also profit off of it, which makes the whole community better, in my opinion.
[936.82 → 942.10] But obviously, the people at IBM and Red Hat who do the calculations don't see it that way anymore.
[942.76 → 943.38] Yeah, for sure.
[944.02 → 945.38] Well, I think it's a matter of scale.
[945.96 → 947.48] Profit scale, like revenue scale.
[947.58 → 950.54] Like, they're at a point now where they're capturing a lot of value.
[950.62 → 951.88] They're also providing a lot of value.
[952.36 → 958.84] Adam Jacob was on the show talking about how much they profit off of Kubernetes by doing what they do.
[959.46 → 959.86] Amazing.
[960.02 → 961.08] Like, they're capturing a lot of value.
[961.78 → 971.14] But I did read that their Red Hat's net revenue increases are on a downswing, like 12%, 10%, 8% the last three quarters.
[971.40 → 972.84] So you see that number going down.
[972.92 → 974.82] They're still more profitable than were the previous quarter.
[974.88 → 976.90] They're still positives, but they're less positive.
[977.22 → 978.54] You know, and nobody wants to see that direction.
[978.88 → 979.32] That's right.
[979.44 → 980.26] Don't go down, go up.
[980.26 → 982.32] And you have pressure to capture so much more.
[982.40 → 983.86] And then you see people like Rocky Linux.
[984.02 → 985.84] Maybe they say, yeah, we got a NASA contract.
[985.90 → 988.42] And you're sitting over there thinking, like, well, I need more contracts.
[989.08 → 992.58] You know, I can see where you could have that in a competitive environment.
[992.58 → 995.58] Like, you'd be like, ah, man, they're out there capturing some value.
[995.66 → 1001.32] We need to get all the value because, you know, we've got to make up for that $34 billion price tag.
[1001.40 → 1003.12] You know, we have to be valuable inside of IBM.
[1003.26 → 1004.32] I'm just speculating.
[1004.38 → 1005.66] But I can see where you would come to that.
[1006.10 → 1007.04] The scale is just massive.
[1007.04 → 1012.26] There's also a lot of people, especially Red Hat, are saying, well, IBM had nothing to do with this.
[1012.62 → 1016.10] And I think anybody outside of Red Hat can say that's BS.
[1016.36 → 1017.68] It's not sure.
[1017.88 → 1019.30] IBM didn't make the decisions.
[1019.72 → 1024.10] But if IBM had never bought Red Hat, would this exact same decision have been made?
[1024.10 → 1025.68] I don't think it would be.
[1025.76 → 1028.14] And I don't think it would be promoted in the same way.
[1028.62 → 1034.00] When you buy a company for $34 billion and say, you're going to be free, you're going to be able to do what you want.
[1034.54 → 1040.58] I can tell you there are things that happen internally that would not happen had IBM never owned Red Hat.
[1041.04 → 1045.94] Not just in Enterprise Linux, but in OpenShift, in Ansible, and in other communities.
[1045.94 → 1051.28] These integrations that have to be built up and ways to promote the commercial products on IBM's side.
[1051.92 → 1060.28] So anytime that that gets brought up, I think it is disingenuous to say this is IBM's fault and Red Hat had nothing to do with it and Red Hat is dead.
[1060.72 → 1067.20] I still see Red Hat as being kind of alive inside there, but it's not the same Red Hat that it was five, six years ago.
[1067.66 → 1071.86] If you had to create a perfect world for Red Hat, what should they have done?
[1071.86 → 1082.04] Instead of making this blog post and locking up the Git RHEL repos and stuff like that, what do you think would have been positive from a monetary standpoint and a community standpoint?
[1082.22 → 1082.86] What could it have done?
[1083.00 → 1091.22] I think if they wanted to have their cake and eat it too, they could have gone down this path towards, you know what, we're going to close down Red Hat Enterprise Linux sources.
[1091.78 → 1094.62] We're going to put them behind the paywall like they did, which is legal.
[1095.08 → 1099.62] And, you know, that was initially a lot of people said, oh my gosh, they're going closed source.
[1099.62 → 1104.74] It's like they're not closing source, they're not violating GPL by putting the code behind the paywall.
[1104.82 → 1107.62] You only have to distribute the code to people you distribute the binaries to.
[1108.06 → 1110.94] There can be philosophical discussions on whether that's in the spirit.
[1111.06 → 1124.50] I think it is because, you know, companies can make money off of the software, but you have to provide the sources and have to not encumber those sources with any restrictions, which that's still a point of argument, I think, in the community.
[1125.08 → 1125.56] Define that.
[1125.62 → 1126.48] It's the hard part, right?
[1126.48 → 1139.88] What I would say is if they wanted to do this, they should have said, you know what, we see this trend, and we're going to give this downstreams five years, let's say, to show a little more good faith.
[1139.98 → 1151.14] Like, it's okay to build support off things, but we don't want you to build support being a bit for a bit compatible or bug for bug compatible with Red Hat Enterprise Linux, which Rocky has always made that kind of their advertising tagline.
[1151.14 → 1157.72] Basically, like, you guys are offending us, let's figure out a way for you to stop offending us and still be part of this ecosystem.
[1158.18 → 1159.84] And we're going to give you a five-year deadline.
[1160.06 → 1163.98] If at the end of that, you're still doing this, we're going to do this closure.
[1164.24 → 1168.40] That would have still ignited a firestorm, but not a nuclear bomb, you know?
[1168.40 → 1168.96] Yeah.
[1169.06 → 1186.70] And it comes back to that trust after the first CentOS death to CentOS stream, the second one happening so early in the cycle of Red Hat 9, that's where it really grates against, I think, all of our, outside of Red Hat, all of our inner, like, what are you thinking?
[1186.84 → 1189.16] Like, the timing of this is terrible.
[1189.76 → 1193.08] At least give a timeline and say this is what we're doing.
[1193.08 → 1198.20] As a dumb example of this, I was pretty hot about this sometimes.
[1198.38 → 1203.18] And one, I put up a PR on one of my Ansible projects basically saying, you know what?
[1203.24 → 1209.44] I could throw a nuke into my thing, too, by making it so that all my roles fail on Enterprise Linux unless you agree to their EULA.
[1209.98 → 1214.34] I put it up there with a note saying, like, unlike Red Hat, I'm going to do this.
[1214.40 → 1216.60] I'm going to throw this nuke down, but I'm not going to merge it.
[1216.70 → 1220.72] I'm not going to actually deploy it unless my community is okay with it.
[1220.72 → 1223.64] So I put it out there and tons of people are like, this is stupid.
[1223.74 → 1224.70] You're an idiot, blah, blah, blah.
[1225.16 → 1226.90] I can't believe you'd ever do something like this.
[1226.94 → 1228.24] It would actually restrict our freedoms.
[1228.36 → 1230.30] It's like, I didn't do it, though.
[1230.34 → 1230.96] That's the point.
[1231.06 → 1239.52] Like, if I'm going to do something that I see this could upset my community of users, maybe I should tell them about it first because that's the right thing to do.
[1239.52 → 1248.64] But they just basically threw a nuke into the downstream ecosystem, coupled with the fact that there were so many in the first two or three days, there were a lot of articles.
[1249.10 → 1253.72] There was one in particular on LinkedIn that tore into Gregory Further, who I've never met.
[1254.04 → 1257.74] I've had one email with him ever, and that was after all this stuff happened.
[1258.24 → 1259.28] I don't know much about him.
[1259.40 → 1262.36] I don't know much about his history besides what I've read online.
[1262.36 → 1268.22] But they were, like, tearing into him, saying he's, like, this terrible person and CIQ is horrible and the way that Rocky was structured.
[1268.64 → 1270.12] Like, where did this come from?
[1270.24 → 1271.68] Like, nobody ever asked about this.
[1272.04 → 1272.90] They were posting about it.
[1272.92 → 1283.22] And then I saw other stuff, and it leads me to believe that this was, I don't know, internally I'm thinking that there must have been some conversations with essays, with marketing, with maybe PR.
[1283.34 → 1285.50] I don't know about, like, here's why this is happening.
[1285.54 → 1287.48] But they didn't release that stuff publicly.
[1287.48 → 1297.84] And then there were comments on Reddit from Mike McGrath about, you know, some underhanded business decision, and he's not going to talk about it because he doesn't want to, you know, throw someone under the bus or whatever.
[1298.58 → 1299.02] I don't know.
[1299.10 → 1304.18] It felt very weird, the whole way that that first two or three days went especially.
[1304.98 → 1315.76] And then at this point, it's, you know, Red Hat, if you talk to their VPs and see all the interviews, they're always talking about the commercial side interests and how it's bad business to let your competitors just take your stuff for free.
[1315.76 → 1317.14] But they don't talk at all.
[1317.22 → 1324.10] They address none of the trust issues, community issues, the open source and free software philosophies.
[1324.20 → 1332.86] And that's, I think, the big difference that I see with the current kind of thing at Red Hat versus 10 years ago, everybody was like, Red Hat is the open company.
[1333.14 → 1333.16] Right.
[1333.30 → 1334.28] They develop upstream.
[1334.66 → 1336.56] They give free stuff downstream.
[1336.94 → 1338.52] They are part of the community.
[1338.52 → 1341.32] And they still do so much.
[1341.62 → 1352.40] And I just hate to see some of that jeopardized because some of the great contributors who work inside of Red Hat, some of them have emailed me and DMed me and said, hey, thanks for saying your piece because I feel some of that rage too.
[1352.98 → 1360.26] You know, I think some of them feel the same way, but they're not going to say it because, like I said, back when I was consulting with Red Hat, I wasn't going to throw them under the bus.
[1360.82 → 1361.72] But they had to feed you.
[1361.84 → 1362.10] Right.
[1362.10 → 1368.00] Some of this we did cover with Greg way back in episode 427.
[1368.90 → 1370.38] And it was the rise of Rocky Linux.
[1370.74 → 1374.34] We haven't talked to Greg or Gregory since then.
[1374.38 → 1374.96] That was 2021.
[1375.24 → 1376.58] It was January 2021.
[1376.74 → 1381.26] When Rocky first came out, it was really before even the RESF.
[1381.36 → 1383.68] I forget the full exposure of the name.
[1383.68 → 1392.84] And the RESF was just the foundation and the structure they created to essentially ensure that Rocky was community and not Greg or a particular person.
[1392.84 → 1399.94] While they are board members, and they have chair seats and stuff like that, they're not the only – he's not the only person that could say so.
[1400.40 → 1404.60] So there are tons of stuff I don't want to cover in there because he mentioned legal and all the juice basically.
[1404.60 → 1411.14] So the things you alluded to is covered for the most part in there from him directly about some of the history.
[1411.30 → 1420.56] There is some bad blood in the water that goes back to CentOS prior to Red Hat's acquisition of it, which I think this is all from that.
[1420.76 → 1431.30] That conversation we have with Gregory in many ways is a precursor to this conversation because that was sort of the beginning of all the mess that came with CentOS, that shift, etc.
[1431.30 → 1444.76] And now we're here now with sources being withheld and Rocky and Alma being, in quotes, the bad guys because they're just decompilers or redistributors essentially like you had mentioned before.
[1445.26 → 1447.64] Meanwhile, hanging back here is Oracle.
[1448.94 → 1449.74] That's right.
[1449.96 → 1453.90] The whole time they've been doing things 50 times worse by many people's standards.
[1454.36 → 1456.66] Well, Oracle is the big winner in this whole mess, isn't it?
[1456.66 → 1457.36] So far, at least.
[1457.42 → 1462.30] Well, maybe Size ends up being, but we should mention the Oracle's epic press release.
[1463.06 → 1472.22] This is like when you have, well, I don't want to draw analogies that are too strong, but this is just like when somebody comes in and just smacks somebody else when they're down, so to speak.
[1472.22 → 1477.12] And they did a perfect job, and I covered it in Changed Dog News, as people on the pod probably heard.
[1477.26 → 1479.28] And I was just impressed by this press release.
[1479.38 → 1483.86] I just loved it as just a person who enjoys whatever technology companies.
[1483.86 → 1488.64] Yeah, I mean, it's a popcorn moment for me because I don't have a dog in this hunt at all.
[1489.26 → 1496.16] I mean, I have a dog in the greater open source community, and I want all of us to thrive, and I want people to be able to capture value.
[1496.32 → 1497.16] I want them to give value away.
[1497.26 → 1502.26] I want everybody to do well, and I hope the best for all these entities except Oracle.
[1502.42 → 1502.96] No, just kidding.
[1503.40 → 1503.98] Oracle 2.
[1504.28 → 1508.06] I wish the best for them, especially after this press release, which did kind of be like, you know what?
[1508.14 → 1509.22] These people—
[1509.22 → 1511.68] Back up those words to some action, and we'll see what happens.
[1511.68 → 1512.60] Yeah, exactly.
[1512.70 → 1516.42] If this wasn't merely a cheap shot, then this could be cool, you know?
[1516.78 → 1519.42] And that was weird, Jeff.
[1519.42 → 1523.76] I think you said on Monday, this is the first time you find yourself agreeing with Oracle on anything.
[1524.34 → 1525.10] So, you know?
[1525.42 → 1525.64] Yeah.
[1525.78 → 1533.40] As somebody who uses VirtualBox and uses Java and all these different things and has built businesses off of a lot of their technologies,
[1534.16 → 1536.72] I never have ever been like, man, I love Oracle.
[1536.72 → 1541.56] I've never said that, and I still don't, but I'm like, that was good, Oracle.
[1541.68 → 1542.50] That was pretty good.
[1542.82 → 1543.60] For sure.
[1543.76 → 1548.30] I want to quote Adam Jacob here on this because he tweeted this, and I just was like head nodding big time.
[1548.36 → 1554.48] He said, we've reached a part of the story where people who should know better are straight-facing Oracle, in quotes,
[1554.62 → 1560.48] is a better friend to open source than Red Hat because they wrote a blog post punching their competitor.
[1560.96 → 1561.70] You all need to do better.
[1561.70 → 1568.46] I mean, that's a good summarization of how most should respond because, yeah, we should do better.
[1568.68 → 1570.22] But at the same time, that was a good dunk.
[1571.82 → 1577.04] There were so many lines in that that's like, man, the sarcasm is just like oozing out of that word.
[1577.74 → 1582.90] It was the longest single segment of changelog news that I've done because I had to quote so many parts of it,
[1582.96 → 1585.26] and they had like a there was a quote inside a quote.
[1585.36 → 1586.80] It was a lot of work for me to cover this.
[1586.84 → 1589.72] And at the end of it, I felt like, did I just give way too much time to this?
[1589.80 → 1590.20] I don't know.
[1590.20 → 1591.06] Let's ship it and see.
[1591.70 → 1595.96] I do want to say that I'd love to get Edward Scriven on, who penned that post.
[1595.96 → 1601.42] I'd love to talk to someone like that that's essentially is second too none to the CEO of Oracle,
[1601.62 → 1603.68] who wrote this post, who has these opinions.
[1603.78 → 1608.34] I'd love to get the insider view from someone like that about their plans, essentially.
[1608.82 → 1613.82] SUSE has put theirs down, forking RHEL, taking investment, and hopefully having, you know,
[1613.88 → 1619.40] what could be, I guess, a RHEL fork, essentially, for us to all standardize against with Enterprise Linux.
[1619.40 → 1620.32] So we'll see.
[1620.42 → 1621.78] But I'd love to get their take.
[1622.16 → 1625.98] To Oracle's credit, they do contribute a lot upstream to Linux.
[1626.52 → 1627.74] It's not like they only take.
[1627.90 → 1628.18] Right.
[1628.50 → 1630.52] Red Hat might want to paint them in that corner.
[1631.10 → 1632.72] But they have done a lot.
[1632.80 → 1634.18] They have some great devs.
[1634.18 → 1636.82] But we don't expect them to be the open company.
[1637.36 → 1639.88] They've never advertised Oracle, the open company.
[1640.20 → 1642.42] Red Hat always says, we are the open company.
[1642.74 → 1644.28] Of course, now they've kind of changed that.
[1644.34 → 1649.42] I've noticed the past three days, I keep seeing this phrase, we develop in the open.
[1649.92 → 1651.68] And we are an enterprise software company.
[1651.76 → 1655.48] That's a completely different mindset than we are the open company.
[1655.48 → 1660.32] I have the open organization from Jim Whitehurst, who is not there anymore.
[1660.78 → 1665.02] But when you lose that mentality, that's when I think you can start saying, like, you know what,
[1665.08 → 1667.94] the community is not as important as the profit for the next quarter.
[1668.36 → 1672.52] I think that some of the people that are making these shifts are not the people that were steeped
[1672.52 → 1676.16] in the free software ecosystem that came up through CentOS.
[1676.72 → 1678.82] A lot of these people came up through Enterprise.
[1679.14 → 1682.14] You know, they worked in other enterprise software companies, and they came over to Red Hat,
[1682.14 → 1684.24] and they're like, oh, that's cool that you have this open source stuff.
[1684.32 → 1687.76] It's great that you can pull in more value without having to hire all the developers
[1687.76 → 1689.88] for all the little random things in the Linux kernel.
[1690.44 → 1693.52] Sure, we do great stuff, but it's great that we can pull in a lot more.
[1693.94 → 1696.52] If you're Apple, you know, they rely on free BSD.
[1696.68 → 1699.28] If you're Microsoft, you actually did write, like, everything.
[1700.12 → 1704.90] So I saw somebody joke in one of the articles that maybe there will be Microsoft RHEL soon.
[1705.20 → 1705.64] Oh, maybe.
[1706.02 → 1706.70] For Azure.
[1707.32 → 1711.90] I want to give you some credit too, Jeff, because in your I'm Done With Red Hat Enterprise,
[1711.90 → 1716.36] Linux video, you did say, you kind of called this post from Oracle.
[1716.48 → 1720.58] You said, wouldn't it be ironic if Oracle were the ones who knocked Red Hat down a peg?
[1720.96 → 1721.30] Really?
[1721.52 → 1723.08] That's kind of what this post is.
[1723.24 → 1724.98] Did you have some inside info on that, Jeff?
[1725.04 → 1725.80] Did you get tipped?
[1725.92 → 1726.76] No, not at all.
[1726.82 → 1730.10] So day three, I was just thinking when I was writing the script to this, I was like,
[1730.16 → 1731.16] I'm furious.
[1731.78 → 1732.94] I want to get that across.
[1733.44 → 1737.84] And I also want to give people a good overview of what the situation is and where it's going
[1737.84 → 1738.24] from here.
[1738.24 → 1742.38] I saw immediately, like, Red Hat, it's hypocritical what they did.
[1742.96 → 1745.74] And I think anybody outside of Red Hat saw that.
[1746.20 → 1749.74] But there's a lot of people internally at Red Hat that kind of can't see that because
[1749.74 → 1750.62] of where they are.
[1750.78 → 1755.46] But I saw immediately, like, of all the companies in the world, there's only really one.
[1755.82 → 1757.20] Like, CIQ can't.
[1757.48 → 1761.88] Rocky Linux, Alma Linux, Cloud Linux, all these different groups that are doing the downstreams
[1761.88 → 1763.78] that are basically getting torn apart by Red Hat.
[1763.90 → 1765.66] None of them could come back with anything.
[1765.66 → 1768.38] But Oracle has bazillions of dollars.
[1769.02 → 1770.04] They could do something.
[1770.36 → 1772.26] So I mentioned, like, wouldn't it be funny?
[1772.78 → 1775.96] And I never thought it would happen because I was like, Oracle is...
[1775.96 → 1776.36] You caught it.
[1776.42 → 1777.22] Maybe they were listening.
[1777.62 → 1778.36] And they're like, we should?
[1778.84 → 1779.96] Damn, but we should do this.
[1780.32 → 1784.42] I mean, you know, Oracle, they have so much money, and they have so many contracts in their
[1784.42 → 1787.44] database, all this stuff, which I hated working with the few times I had to.
[1787.86 → 1789.82] You know, they didn't have to say anything.
[1789.82 → 1794.62] And they would still be the victor here compared to Red Hat because nobody expected them to
[1794.62 → 1795.62] do anything amazing.
[1795.96 → 1798.76] But then they come out with a blog post, and I'm like, yeah.
[1799.30 → 1800.62] Two things that are interesting about that.
[1800.66 → 1802.94] First, I mean, kick a guy when he's down.
[1803.10 → 1805.44] You know, they're just like, we're about to just come out and kick you while you're down.
[1805.82 → 1810.70] But then also, it's interesting in that post how they referred to it almost exclusively
[1810.70 → 1811.30] as IBM.
[1811.64 → 1815.98] That's why in my news coverage I said, you know, Oracle smacks IBM.
[1816.24 → 1817.04] Because they really did.
[1817.04 → 1821.18] I mean, they're talking IBM, of course, Red Hat is there, but they're really kind of
[1821.18 → 1823.26] blurring those lines, and you can see who they're coming after.
[1823.68 → 1826.00] And they're really talking about, well, it's all about money.
[1826.28 → 1829.70] And it appears like, yeah, it's hard to say it's not.
[1830.36 → 1831.84] They aren't wrong, but they're also not right.
[1831.94 → 1837.18] And there are a lot of Red Haters that I personally know that I've been in conversation with outside
[1837.18 → 1840.12] of, you know, the Jeff Deerling hates Red Hat type thing.
[1840.70 → 1845.12] And I think it's disingenuous to go that far that they did.
[1845.12 → 1847.52] But on the flip side, it is what it is.
[1847.82 → 1851.62] Like Ansible, when I started working with Ansible, was independent.
[1852.22 → 1853.36] Then it got bought by Red Hat.
[1853.70 → 1854.90] But it was still Ansible.
[1855.00 → 1856.16] But then it was Red Hat Ansible.
[1856.28 → 1859.50] And I started seeing some things change, like some of the structure, the way that it was,
[1859.98 → 1863.86] like how are we going to allocate all our resources and getting things into the, you know,
[1864.04 → 1866.94] paid ecosystem outside the open source area.
[1866.94 → 1872.52] And then now it's, you know, Red Hat Ansible automation platform, you know, by IBM is what
[1872.52 → 1873.18] I call it.
[1874.02 → 1878.56] Because there are parts of it now that it's like these resources that were focused on making
[1878.56 → 1884.10] Ansible a better product are now focused on making Ansible tie into, you know, Z and to
[1884.10 → 1888.46] the power platform and all these other things that never would have happened had IBM not
[1888.46 → 1888.84] bought it.
[1889.00 → 1890.48] So there's a point.
[1890.60 → 1892.72] But it's also, I think some people overplay that point.
[1892.72 → 1894.24] Yeah, it is what it is.
[1894.32 → 1897.96] You gave you a little bit of your story about, you know, getting into Red Hat or learning
[1897.96 → 1899.90] about Red Hat back in the day.
[1900.10 → 1902.64] I wanted to share my first interaction with Red Hat.
[1902.78 → 1907.22] So in college, I was into Linux, but I didn't know Red Hat at first.
[1907.42 → 1911.24] I did run Fedora a few times, but then ended up in the Debt and Ubuntu side of things.
[1911.74 → 1916.02] But I remember one time I knew who Red Hat was, like from the hat, you know, and like
[1916.02 → 1918.04] Fedora and this whole thing.
[1918.36 → 1919.24] And Shadow Man.
[1919.56 → 1920.42] Yeah, exactly.
[1920.42 → 1923.84] And I remember one time, and I just had a disdain for Windows.
[1924.06 → 1925.64] I had gotten that far, right?
[1925.68 → 1927.08] Like I was like not going to run Windows.
[1927.22 → 1930.08] This was 2002 back in the day.
[1930.42 → 1935.94] And I remember I went to Mega Mart, which is just a local retail or big box electronics
[1935.94 → 1936.32] store.
[1936.74 → 1939.74] I used to just cruise the software aisles, you know, back when we bought software off the
[1939.74 → 1940.00] shelf.
[1940.32 → 1940.82] In boxes.
[1941.30 → 1944.82] Yeah, I would go down like when I was, it was right next to my university and at lunch
[1944.82 → 1948.30] hour, I'd just go there and cruise, you know, and I'd check out the DVDs, and I'd check
[1948.30 → 1948.90] out the software.
[1948.90 → 1953.68] And I remember looking at all the windows, you know, whatever it was, XP probably back
[1953.68 → 1953.94] then.
[1955.06 → 1963.48] And then I saw a box, Red Hat Linux, really cool box with a red fedora on it and the Shadow
[1963.48 → 1963.74] Man.
[1964.12 → 1965.96] And I knew that this was free software.
[1966.12 → 1967.30] Like I knew what Red Hat was.
[1967.30 → 1968.92] I knew what fedora was.
[1969.08 → 1974.68] And I'm like, these people are selling something in a box store that's totally free.
[1975.28 → 1976.22] How cool is that?
[1976.28 → 1977.06] And I just loved them.
[1977.14 → 1978.66] I thought it was like the coolest thing ever.
[1978.88 → 1982.20] And I had the utmost like hacker respect for Red Hat ever since.
[1982.26 → 1986.22] I've just always had good vibes because I'm like, you know, it takes some chutzpah or whatever
[1986.22 → 1988.44] it's called to just go and put a box to buy.
[1988.62 → 1988.76] Yeah.
[1989.32 → 1991.70] In a store where you can go just go download it for free.
[1991.78 → 1993.84] I'm like, maybe they just hope nobody knows that.
[1993.94 → 1995.96] I don't know who would buy this box, but it's cool.
[1996.22 → 1997.18] And I like it.
[1997.24 → 2000.32] So I've had a long time respect for Red Hat and still do.
[2000.60 → 2002.36] They still put out lots of awesome stuff.
[2002.36 → 2008.54] It's just you see the changes that happen under circumstances that we're in.
[2008.58 → 2009.46] And it just is what it is.
[2009.70 → 2011.08] People say that I hate Red Hat.
[2011.20 → 2011.78] I don't.
[2011.92 → 2016.64] The reason why I pointed these things out is that I'm like, hold on, like, come back.
[2016.72 → 2017.90] This isn't what you said you would do.
[2018.02 → 2019.04] Come back to the light side.
[2019.24 → 2020.40] Come back to the light side.
[2020.62 → 2022.32] There's a path, and they're diverging this way.
[2022.34 → 2024.10] And I'm like, come back this way.
[2024.18 → 2024.38] Yeah.
[2024.62 → 2026.20] And I'm willing to forgive.
[2026.20 → 2030.52] It's going to take a lot more after those two blog posts, after the things that employees
[2030.52 → 2034.98] have said on, you know, all over the place at this point, after some of the perspective
[2034.98 → 2039.28] shifts that I see that I would not have dreamt of five years ago.
[2040.16 → 2044.26] But I still want to see them succeed because I mentioned in a couple posts, like they're
[2044.26 → 2046.46] the too big to fail of Linux right now.
[2046.64 → 2053.74] If they're not backstopped, then maybe proprietary software can make inroads back in on the enterprise.
[2054.18 → 2054.34] For sure.
[2054.34 → 2060.88] I don't know if Seuss is quite big enough to step in Red Hat's role if Red Hat does
[2060.88 → 2062.82] start failing in enterprise Linux.
[2063.84 → 2068.46] And there's also arguments from the other side with, you know, Kubernetes and container
[2068.46 → 2072.56] infrastructure and cloud-based computing that maybe none of this matters at all.
[2072.68 → 2074.18] Like, who cares about enterprise Linux?
[2074.36 → 2079.82] But if you look around, pretty much all clouds run on servers and the servers run an operating
[2079.82 → 2080.24] system.
[2080.24 → 2084.72] And a lot of those operating systems are one of the top three or four Linux operating systems.
[2085.30 → 2089.84] So, you know, look in my home lab, even the servers that run containers right now, they're
[2089.84 → 2090.46] all running Debian.
[2090.58 → 2094.74] I just finished migrating the last one off of Rocky, but it is still important.
[2094.98 → 2099.94] And you can't, like containers just don't magically wash away the importance of enterprise Linux.
[2100.72 → 2101.98] Was that migration because of this?
[2102.02 → 2103.28] Because you were in that migration phase?
[2103.44 → 2103.66] Yes.
[2103.82 → 2107.46] Most of them are running Debian because it's Raspberry Pi OS, which is based on Debian.
[2107.46 → 2112.06] But I had a couple other servers that were running Rocky, and I was like, forget this.
[2113.42 → 2117.10] And I mentioned in my blog post, I'm not supporting Red Hat Enterprise Linux anymore.
[2117.30 → 2122.54] So if something starts failing on Rocky, I'll just kind of drop that support because it's
[2122.54 → 2124.76] not worth it to me at this point.
[2125.02 → 2125.28] Yeah.
[2125.76 → 2128.20] Which stinks because I still, I have my Rocky Linux shirt.
[2128.60 → 2129.58] This is another funny thing.
[2129.68 → 2133.62] One Red Hat employee was like, well, you obviously you're paid by CIQ and Rocky.
[2133.62 → 2138.70] And I'm like, I've never, I received a t-shirt and two stickers, one of which is on my wall
[2138.70 → 2139.08] over there.
[2139.62 → 2141.88] That's the extent of my relationship with Rocky Linux.
[2142.10 → 2146.54] They sent me the shirt because I used them in a video when I set up something at one point
[2146.54 → 2147.78] and they're like, hey, do you want a shirt?
[2147.84 → 2148.32] And I'm like, sure.
[2148.76 → 2149.58] Because I like t-shirts.
[2149.70 → 2151.04] I don't go to conferences as much.
[2151.10 → 2153.02] So I got to get t-shirts through the mail now.
[2153.16 → 2153.26] Yeah.
[2153.38 → 2154.30] Got to get your swag somehow.
[2155.12 → 2155.88] Send it to me.
[2157.12 → 2160.16] Is this something you think that Red Hat is going to walk back?
[2160.16 → 2163.50] Because sometimes when you follow up this big, like you said, nuclear bomb, when you
[2163.50 → 2168.74] do this kind of thing that does kind of cause an explosion and there's a lot of blowback,
[2169.22 → 2174.78] there's a lot of disdain, sometimes those decisions get walked back.
[2175.44 → 2176.14] I don't think so.
[2176.22 → 2183.20] Mostly because the response I've seen after Oracle and after Seuss's blog post is, well,
[2183.28 → 2184.40] that's what we wanted to happen.
[2184.70 → 2185.58] It's like, what?
[2185.58 → 2188.22] I don't know what they're trying to do at this point.
[2188.70 → 2192.16] It doesn't make sense to me, but I'm not, I don't have an MBA.
[2192.60 → 2193.86] I'm not a great businessman.
[2194.40 → 2196.14] I don't think they're going to walk it back though.
[2196.22 → 2197.40] It doesn't feel like it.
[2197.72 → 2203.02] What I think that they could still do without walking it back is help people with CentOS
[2203.02 → 2204.94] stream more than they did.
[2205.42 → 2210.50] One thing that I've seen, which is ridiculous, is a lot of essays are mentioning, well, everybody
[2210.50 → 2211.52] can just switch the stream.
[2211.68 → 2214.42] It's like, well, your documentation says don't run it in production.
[2214.42 → 2214.90] Yeah.
[2215.08 → 2219.44] So you're telling everybody, the thousands and thousands, you're telling HPC and educational
[2219.44 → 2223.32] markets, these hosting providers just switch the stream, but you're saying it's not stable
[2223.32 → 2224.28] enough to run in production.
[2224.52 → 2225.60] You got to solve that.
[2225.70 → 2231.32] So solve that issue, help Rocky and Alma rebuild, you know, maybe give them some support in it
[2231.32 → 2232.36] to show good faith.
[2232.80 → 2236.18] But I don't think that's going to happen because they've basically excoriated them.
[2236.80 → 2236.88] Yeah.
[2237.16 → 2240.58] I don't think that they're going to walk it back, but I still think that they could do more
[2240.58 → 2242.38] to make it not so bad.
[2242.50 → 2244.80] But I don't see any signs that that's happening.
[2244.80 → 2248.62] I can understand their offence to Rocky and Alma.
[2248.84 → 2251.24] I can understand the offence completely.
[2251.88 → 2256.12] Something that I've learned in my life, though, is whenever, and maybe they're just so big,
[2256.14 → 2261.46] like you said, to fail, that this isn't a concern for them, is that whenever you come
[2261.46 → 2267.00] to a table with a decision with no plans to negotiate, you forfeit all opportunity to
[2267.00 → 2273.78] have empathy for the other side and to essentially fine tune things to be cohesive for everyone,
[2273.90 → 2276.20] not just the one side of decision you came to the table width.
[2276.54 → 2281.56] And like you had said, maybe they could have given them five years to say, help us understand
[2281.56 → 2284.76] how you're a positive, not a negative to our goals and the community.
[2284.76 → 2289.78] Are you simply just a copy of us with support, you know, bug for bug compatible?
[2289.92 → 2294.26] Are you just a copy of us with support models that essentially is RHEL, but not RHEL?
[2294.88 → 2296.62] Because if that's the case, then we don't like that.
[2296.70 → 2297.84] We think we want to limit you.
[2298.08 → 2302.88] But they made this choice because of that, it seems that impacts everybody.
[2303.14 → 2307.04] I think it would be in their best interest to have, like you had said, CentOS Stream
[2307.04 → 2312.70] be back to CentOS Waze, where it is production ready and available to everybody because that
[2312.70 → 2317.90] helps the Red Hat Enterprise Linux brand be the de facto, kind of what they have been,
[2317.96 → 2321.58] which is why we're all in this conversation, because they have been the Enterprise Linux
[2321.58 → 2322.02] standard.
[2322.50 → 2329.80] To me, that makes the most sense to remain and be and solidify that standard, not just
[2329.80 → 2334.90] kill off some competitors and lock down your source code to only those who subscribe, essentially.
[2335.62 → 2335.68] Yeah.
[2335.84 → 2340.82] I keep seeing this statement, all of our code, everything in Red Hat is in CentOS Stream.
[2340.82 → 2343.72] It's like, well, that's not entirely true.
[2344.60 → 2347.28] 99%, probably more than 99% is.
[2348.00 → 2354.16] And in terms of the whole complete source availability, it doesn't meet that standard.
[2354.28 → 2358.66] But the license agreement saying you can download the sources if you have an account and you
[2358.66 → 2361.42] have a subscription in good standing, that does meet it.
[2361.50 → 2366.04] But they can't make that statement that everything is in stream, because what they're trying to
[2366.04 → 2367.90] say is, why are you doing this downstream?
[2368.02 → 2370.04] We have this upstream, which is better, and it has everything.
[2370.04 → 2375.10] It's like, well, if they did their work all in stream, and if they coordinated the releases,
[2375.26 → 2379.08] especially the minor releases through stream, that's one thing, but they don't.
[2379.24 → 2382.32] They kind of, Red Hat is kind of a little bit of a fork of stream.
[2382.44 → 2384.66] It's not a big fork, but it's a downstream of stream.
[2384.86 → 2386.70] So it's not one-to-one identical.
[2387.48 → 2390.44] But they're trying to sell it as that to the press, I think.
[2390.70 → 2392.36] Anyone like us can kind of see through that.
[2392.42 → 2393.18] It's not identical.
[2393.18 → 2398.24] They've tried selling stream for three or so years now, and nobody outside the Red Hat
[2398.24 → 2403.68] ecosystem, like the Red Hat Enterprise Linux subscribers themselves and Red Hat, has bought
[2403.68 → 2404.18] into it.
[2404.54 → 2409.48] I don't know how they're going to change that without changing stream and making it better.
[2409.72 → 2412.30] Even in a home lab, stream is not cool.
[2412.46 → 2415.92] Like, if you can't run it in prod, sure, my Plex server may not be important to anybody
[2415.92 → 2417.26] else besides my immediate family.
[2418.12 → 2419.56] But I don't want it to be down.
[2419.64 → 2420.90] It's production to you, man.
[2420.98 → 2421.74] It's production to you.
[2421.82 → 2423.14] It's production to me, right?
[2423.56 → 2425.04] Yeah, and somebody can run it.
[2425.12 → 2428.96] You know, it might be more stable in Fedora, but I'm not going to run Fedora for any of
[2428.96 → 2429.48] my servers.
[2430.16 → 2432.16] I'll run it for a workstation, but not servers.
[2432.68 → 2437.58] As a guy whose run Debian on servers my entire career, I just wonder, you know, why not just
[2437.58 → 2439.00] come on over where the water's warmer?
[2439.20 → 2440.42] Jeff, it sounds like you're here now.
[2440.52 → 2441.38] It sounds like you joined.
[2441.50 → 2441.84] I am.
[2442.26 → 2443.46] I mean, personally, I am.
[2443.46 → 2449.52] I still, I respect my users and a lot of them are still on Red Hat, Rocky Linux, Amal
[2449.52 → 2449.80] Linux.
[2450.10 → 2450.30] Right.
[2450.58 → 2451.60] Some are on Oracle.
[2452.06 → 2455.86] So I don't just want to cut them off like Red Hat likes doing.
[2456.34 → 2459.80] So that's why I'm like, I'm maintaining the support until it breaks.
[2460.26 → 2462.56] If it breaks, and it's like, oh, you just need to bump a version somewhere.
[2462.62 → 2462.98] That's fine.
[2463.00 → 2466.72] But if it breaks, and it's like, oh my gosh, I have to re-architect this for Red Hat 10.
[2467.04 → 2468.10] I'm not going to do that.
[2468.14 → 2469.76] I'm going to drop the support at that point.
[2469.76 → 2475.98] But I've heard from tons of organizations that have everything in the Red Hat ecosystem.
[2476.32 → 2480.62] A lot of them don't subscribe to Red Hat because they have people that can understand it enough.
[2480.72 → 2482.52] They don't need the support, that kind of thing.
[2483.02 → 2484.54] So now they're like, well, what do we do?
[2484.66 → 2488.98] You know, we could go to Debian, we could go to Rocky and hope that Rocky keeps doing
[2488.98 → 2493.36] their little piracy thing that's not actually piracy because I saw the fun meme of like,
[2493.48 → 2497.00] I am now an open source pirate, pirate open source software.
[2497.00 → 2498.48] It's so funny.
[2499.24 → 2502.18] Yeah, you know you're epic when you're pirating open source.
[2502.70 → 2506.46] But I still see a lot of those people and I want to help them as much as I can.
[2506.58 → 2509.38] But on the flip side, I'm happy in the Debian world.
[2509.94 → 2513.06] And I know that a lot of people are like, oh, you should use Nix or use this or, you know,
[2513.08 → 2514.40] there's a million other distributions.
[2514.86 → 2515.50] Nix is hard.
[2517.16 → 2517.52] Sorry.
[2517.70 → 2517.86] Yeah.
[2517.96 → 2518.58] Nix is hard.
[2518.72 → 2520.02] I can't help but admit it.
[2520.30 → 2520.80] It's hard.
[2520.88 → 2522.10] There are lots of good options.
[2522.48 → 2522.80] Arch.
[2523.02 → 2524.12] Arch is the cool one.
[2524.12 → 2526.12] I switched to Arch one time in production.
[2526.62 → 2527.20] Yeah, by the way.
[2527.78 → 2531.38] Because I got by the weight enough times that I was like, I feel like I'm missing out on
[2531.38 → 2532.20] something with Arch.
[2532.40 → 2536.70] And so I put a new customer on Arch Linux and all everything, literally every other server
[2536.70 → 2537.70] I was maintaining was Debian.
[2537.84 → 2539.92] I was like, I'm going to learn Arch.
[2540.14 → 2541.60] And then I stopped.
[2542.82 → 2543.90] Not because it's not good.
[2543.98 → 2549.10] I mean, their documentation is almost every search ends up somewhere in Arch, you know.
[2549.90 → 2550.82] They're great for that.
[2550.82 → 2551.44] Oh, yeah.
[2551.80 → 2555.72] It's just like different enough that I'm like, why am I spending time figuring out how to
[2555.72 → 2560.10] do this particular thing in Arch when I already know how to do it on the other side?
[2560.18 → 2563.14] So when you talk about your users, I'm not familiar with your business.
[2563.26 → 2564.58] Can you tell like, what do you mean by that?
[2564.66 → 2565.62] Like, what do you host and stuff?
[2565.94 → 2572.08] My downstream open source users who 99.9% of them use my software and never contribute back,
[2572.30 → 2572.64] basically.
[2573.12 → 2577.76] So the people who make my product, which is open source software, what it is.
[2577.76 → 2582.00] Ansible is used by hundreds of thousands at this point.
[2582.24 → 2588.02] And my roles for Ansible and some of my collections and some of my playbooks have been downloaded
[2588.02 → 2590.24] at this point billions of times.
[2590.54 → 2595.00] A lot of those are CI instances running tests and things, but they're used very widely, I
[2595.00 → 2595.44] would say.
[2596.10 → 2601.06] And Ansible being something that was bought by Red Hat and came out of the Red Hat ecosystem
[2601.06 → 2604.98] and came back into the Red Hat proper is used a lot in Red Hat.
[2605.24 → 2607.16] And none of my roles are certified.
[2607.82 → 2612.36] That's when, you know, Red Hat works with a vendor to make certified roles that are kind
[2612.36 → 2614.86] of blessed in the Ansible automation platform and all that.
[2615.20 → 2619.10] But I can see the usage and the issues that come in and things.
[2619.12 → 2623.76] And there's a lot of people that use Red Hat Enterprise Linux and use my roles because my
[2623.76 → 2627.34] roles are decently well maintained, which you can't say for a lot of things.
[2627.34 → 2630.78] Not as well nowadays as they were five or six years ago.
[2630.94 → 2637.12] I used to run a hosting service for Apache Solar, and that was for Drupal websites, basically.
[2637.26 → 2640.90] And that was profitable, but also it was something that took a lot of time.
[2641.16 → 2646.60] And if five or six OS upgrades into it and five or six architecture changes, I was moving
[2646.60 → 2647.40] everything to Kubernetes.
[2647.60 → 2648.38] And I was like, you know what?
[2649.04 → 2651.20] This isn't the thing that I love to do in life.
[2651.24 → 2652.72] So I closed off that service.
[2652.76 → 2655.78] And I also had another service called Server Check-in for uptime monitoring.
[2655.78 → 2661.80] Um, those both use those roles and I probably used 50 or 60 roles for different things.
[2662.22 → 2662.34] Gotcha.
[2662.58 → 2667.08] And now I use about 15 or 20 of them day to day and then 20 or 30 more.
[2667.40 → 2671.06] So some of the roles that I don't use as much, like I don't deploy GitLab anymore.
[2671.06 → 2675.68] So that role has not gotten much love, but there are still plenty of users that use it to
[2675.68 → 2678.24] the point where I still maintain it enough that it will work for them.
[2678.74 → 2682.62] If you look at one of my roles and see, I haven't committed anything to it for two years.
[2682.62 → 2686.16] You might want to think about forking that role, which I'm perfectly happy with.
[2686.52 → 2686.54] Yeah.
[2686.56 → 2687.48] You know, take my work.
[2687.80 → 2692.22] I use the MIT license, which is much more like take everything I've ever done and steal
[2692.22 → 2692.42] it.
[2692.78 → 2694.14] Like, take it from me, please.
[2694.46 → 2695.14] Here, take it.
[2695.24 → 2697.00] It's like no warranty, but that's about all.
[2697.32 → 2697.54] Yeah.
[2697.70 → 2702.46] So, you know, I've, I've considered changing my licensing strategies to GPL just because
[2702.46 → 2705.22] I've seen like the whole idea is based on trust.
[2705.22 → 2709.84] I trust that, you know, I'm going to give you all my work for free, and you could take
[2709.84 → 2710.70] it and profit off it.
[2710.76 → 2715.68] I don't care, but I trust that you'll see that this is a good thing, and you'll do some
[2715.68 → 2718.30] other good stuff with it, you know, or you'll contribute back.
[2718.34 → 2721.92] You'll send me a patch or, you know, you'll help somebody else that uses this thing.
[2722.12 → 2724.08] Or you'll say like, Hey, Jeff is cool.
[2724.16 → 2725.64] Like that's, that's nice too.
[2726.12 → 2726.24] Yeah.
[2726.24 → 2730.60] But at this point I'm like, well, maybe I can't trust because basically the all the
[2730.60 → 2735.26] people that want MIT licensing are corporations that don't want to deal with the poisoning
[2735.26 → 2738.16] of free software philosophy into their ecosystem.
[2738.64 → 2739.00] Right.
[2739.56 → 2742.00] I always picked MIT as well for two reasons.
[2742.00 → 2745.36] The first one was I just wanted as many people to benefit as possible.
[2745.36 → 2747.58] And I just figured the freer, the freer.
[2747.72 → 2751.64] And I understand how that's maybe perhaps short-sighted and can definitely be argued
[2751.64 → 2751.96] against.
[2752.02 → 2755.94] But I was like, just free, you know, as, as gift as I can be, which is like, do whatever
[2755.94 → 2756.42] you want with it.
[2756.84 → 2760.38] And the other one was because I never had a project that I felt like this one's really
[2760.38 → 2760.72] good.
[2760.90 → 2765.86] You know, I feel like my open source is always like, yeah, I take it, you know, have fun
[2765.86 → 2768.32] kids, but make it as easy to steal as possible.
[2768.56 → 2770.32] So are you sure you want to take this?
[2770.36 → 2770.74] Go ahead.
[2770.80 → 2771.46] You can have it.
[2771.46 → 2776.24] But I didn't have any answerable rules that were perfect, you know, which I think
[2776.24 → 2777.42] changes the calculus, perhaps.
[2777.92 → 2777.98] Yeah.
[2778.06 → 2783.64] And I think that part of that too, is my philosophy and open source comes out of, you know, I always
[2783.64 → 2784.90] took before I gave.
[2784.90 → 2788.46] And one of the first communities where I gave back finally was Drupal.
[2788.66 → 2792.20] And in Drupal, the whole ecosystem is completely different.
[2792.42 → 2796.84] Drupal is, I wouldn't say it's an order of magnitude less revenue than Red Hat itself,
[2796.84 → 2800.86] but it's a very substantial amount of revenue for all the companies in that ecosystem.
[2801.40 → 2802.96] But there's an understanding.
[2803.32 → 2805.88] It's just a thing because all of us came out of that.
[2805.96 → 2807.68] Like we took and then we gave back.
[2807.86 → 2811.30] There's a saying, you come for the code, and you stay for the community.
[2811.30 → 2812.08] Mm-hmm.
[2812.32 → 2817.44] Everybody supported each other, and it was GPL v2 and companies would build their own distributions
[2817.44 → 2818.12] based on it.
[2818.22 → 2823.06] But all those distributions, there was never a question like, oh, and you give everybody
[2823.06 → 2823.72] the source code.
[2823.94 → 2826.02] Like you could always build on everyone else's.
[2826.08 → 2827.48] Nobody would ever pull any tricks.
[2828.12 → 2829.78] Nobody would ever try to restrict it.
[2829.78 → 2832.16] And sometimes conversations like that would happen.
[2832.28 → 2835.30] I worked at one of the biggest Drupal providers out there, which is Acquit.
[2835.78 → 2838.28] And sometimes someone would come in and say, well, why can't we do this thing?
[2838.36 → 2841.54] Well, the immediate answer was because that's not in the spirit.
[2841.74 → 2844.36] Like we're going to kill our community if we do that.
[2844.42 → 2844.90] So don't.
[2845.00 → 2846.42] And then it's like, okay, yeah, that's fine.
[2846.88 → 2852.72] But on the Red Hat side, a lot of people come in through enterprise software, through proprietary
[2852.72 → 2853.74] software companies.
[2853.74 → 2858.70] And they just have never been raised with that philosophy through their open source life.
[2858.90 → 2861.36] And they see open source as like this thing.
[2861.64 → 2862.20] It's a feature.
[2862.68 → 2864.14] And it's not the feature.
[2864.54 → 2866.62] Like open source, the software is open source.
[2866.72 → 2867.52] And that's a thing.
[2867.84 → 2870.60] It's not, oh, and the software comes out of this open source thing.
[2870.66 → 2871.10] And that's cool.
[2871.66 → 2875.38] It's something you really don't understand if you're really in the muck of it.
[2875.52 → 2880.00] You know, like if you've maintained a system or deployed software or built software, like
[2880.00 → 2883.00] you only really understand the philosophies of open source truly.
[2883.74 → 2887.32] If you've been in the mix, you know, if you're a purveyor or an outsider to some degree,
[2887.88 → 2889.24] just helping things move along.
[2889.34 → 2891.32] It's kind of hard to really understand the spirit of open source.
[2891.40 → 2895.84] If you haven't been part of hearing people's stories like we have on this show for many,
[2895.96 → 2900.82] many years and being advocates for open source, because not because Jared and I particularly
[2900.82 → 2905.00] have the kind of software you have out there used by the users you have.
[2905.10 → 2908.22] It's because we understand the empathy we have for our fellow developer.
[2908.22 → 2913.44] And we want to see their freedoms be preserved and the things they thrive for and the things
[2913.44 → 2917.90] they put their work into be free in the way they wanted to be free.
[2918.08 → 2921.78] And that's what open source really is, because my street line, Jared probably shared to some
[2921.78 → 2925.36] degree his, but I came through WordPress into open source.
[2925.74 → 2930.18] The fact that K2 had CSS available, and it was an open source theme.
[2930.18 → 2933.96] I learned what it was like to theme a website with CSS.
[2934.20 → 2937.22] This is back when CSS was taking over tables way, way back in the day.
[2937.64 → 2939.46] And that's my street line into software.
[2939.56 → 2940.38] I didn't go to school for it.
[2940.38 → 2941.16] I don't have a CS degree.
[2941.72 → 2945.80] You know, I work for an IT company in biz dev, which I was very good at.
[2946.18 → 2950.38] But I started to understand open source by way of being a user, like you had said, a taker
[2950.38 → 2952.56] of it, not ever a contributor.
[2952.66 → 2957.00] And I'd said, as much I've given back to open source is like almost nothing in comparison
[2957.00 → 2961.82] to my usage of it, you know, maybe through this show and the things we do, we've given
[2961.82 → 2962.24] back.
[2962.48 → 2962.50] Yeah.
[2962.50 → 2964.10] There's no way we can repay that debt.
[2964.40 → 2964.80] Right.
[2964.96 → 2965.26] Yeah.
[2965.48 → 2970.66] And, but that's like, you don't get that unless your kind of have a version of that straight
[2970.66 → 2971.00] line.
[2971.30 → 2976.28] If you just come through proprietary software, and it is like you had said, just a feature
[2976.28 → 2982.26] or just those users who want freedom, whatever, who cares, then you're going to have that perspective.
[2982.26 → 2986.98] But if you've been in the thick of it to learn what you learned, to do what you do, or to
[2986.98 → 2991.80] go where you go, then you'll understand what it means to have the spirit of open source
[2991.80 → 2995.34] and what it means to have free software and whatever way you want to describe free.
[2995.64 → 3000.40] That cuts right back to the line in that second blog post, like Red Hat, what was it?
[3000.44 → 3005.44] They said like, rebuilds like Rocky and Alma are a real threat to open source and one that
[3005.44 → 3009.44] has the potential to revert open source back into a hobbyist and hackers only activity.
[3009.44 → 3013.00] It's like all of us are hackers and hobbyists.
[3013.12 → 3013.44] Yes, please.
[3013.44 → 3019.52] Internally at Red Hat, almost everyone I know started out as a hobbyist on Linux or in whatever,
[3020.02 → 3021.42] and they came into that ecosystem.
[3021.68 → 3025.40] So I think that they meant that as a diss, and it is in a business sense.
[3025.48 → 3027.84] It's like, oh my gosh, we have this professional thing.
[3027.90 → 3029.88] We don't want it to become a hobbyist thing anymore.
[3030.10 → 3031.94] Like that's what it was back when it was really weird.
[3031.94 → 3037.56] And it was on IRC and, you know, ICQ and things and Usenet, you know, these are terrible
[3037.56 → 3037.96] things.
[3038.06 → 3039.42] It's like, well, we all see that.
[3039.50 → 3039.80] And we're like.
[3040.06 → 3040.96] The good old days.
[3041.28 → 3041.66] That's still.
[3041.66 → 3042.50] Yeah, that's still true.
[3042.62 → 3044.00] Everything came from there.
[3044.18 → 3045.82] Like if we want to go back to that.
[3045.88 → 3046.02] Yeah.
[3046.08 → 3047.82] Just, you know, cut off Red Hat.
[3047.92 → 3048.48] This is awesome.
[3050.06 → 3050.20] Yeah.
[3050.22 → 3050.94] I read that too.
[3050.98 → 3054.70] And I was like, okay, I know who's writing this because they just don't have the same
[3054.70 → 3055.62] perspective as I have.
[3055.62 → 3060.66] It's like, I always gravitate towards the weird, towards the obscure, towards the hacker
[3060.66 → 3061.84] and the free and the cool.
[3062.00 → 3064.20] And the, you know, like that's the cool stuff.
[3064.64 → 3065.94] They also said we had to pay our people.
[3066.34 → 3070.60] That was the other thing was like this hobbyist, you know, hackers only thing.
[3070.60 → 3071.86] And then we have to pay people.
[3072.08 → 3073.28] That was our reasoning, essentially.
[3073.34 → 3074.62] Those are the two kind of main things.
[3074.82 → 3075.92] We have to pay developers.
[3075.92 → 3076.88] So we must do this.
[3077.12 → 3078.46] Well, you know, really?
[3079.02 → 3079.62] Yeah, you do.
[3079.70 → 3080.98] But that's not the only way.
[3080.98 → 3085.88] I feel very sorry for the people who were laid off, which disproportionately seemed to affect
[3085.88 → 3087.04] the open source communities.
[3087.26 → 3092.48] For example, opensource.com being basically cut off, the Fedora community manager being
[3092.48 → 3096.40] cut out, you know, but I feel for, you know, it is tough to go through layoffs.
[3096.66 → 3101.00] But that's after a quarter where they said that OpenShift just made a billion dollars.
[3101.20 → 3101.34] Yeah.
[3101.52 → 3104.48] And profits are down, but they're still profits.
[3104.48 → 3109.18] And you're saying, oh, my gosh, oh, please don't hate us because we got to pay our developers.
[3109.32 → 3112.10] It's like, well, then maybe cut your profits a little bit.
[3112.18 → 3115.80] But they can't because, you know, it's a for-profit corporation, and they have to please
[3115.80 → 3117.52] their investors and the board and all that.
[3117.94 → 3119.62] But it's like you can't use that line.
[3119.82 → 3121.96] If they were a not-for-profit, sure.
[3122.20 → 3123.40] You know, we want to pay our developers.
[3123.56 → 3127.44] And, you know, in the Drupal community, we have had that conversation because the Drupal
[3127.44 → 3130.92] Association, which is a not-for-profit, has had hard decisions.
[3130.92 → 3136.80] When times get tougher, how do we keep these developers who are working on the Drupal
[3136.80 → 3138.82] infrastructure employed and pay them?
[3139.28 → 3142.46] And so we all band together and the community contributes, and we get that.
[3142.54 → 3146.38] But you don't get that when you're a for-profit company advertising billions of dollars of
[3146.38 → 3150.38] profits in your new market segments that are leeching off the Kubernetes ecosystem.
[3151.00 → 3154.54] Sure, you can contribute back, but you didn't build all of Kubernetes yourselves.
[3155.24 → 3155.40] Yeah.
[3155.44 → 3156.20] No sympathy.
[3156.20 → 3161.08] What do you think about the future of open enterprise Linux as a standard?
[3161.32 → 3162.26] It has been RHEL.
[3162.48 → 3164.80] This change may change things.
[3165.26 → 3166.98] SUSE obviously said they're going to fork it.
[3167.26 → 3168.16] They've got an investment.
[3168.84 → 3172.12] Oracle put down there, smacked down there, their little slap in the face.
[3172.90 → 3176.34] What do you think is going to happen with the open enterprise Linux standard going forward?
[3176.68 → 3179.80] Well, they say that history doesn't repeat itself, but it rhymes.
[3179.80 → 3185.36] And I was not deeply involved back when the whole SEO thing happened.
[3185.56 → 3190.02] But that was kind of what happened back then when Red Hat Linux became Red Hat Enterprise Linux.
[3190.22 → 3192.24] And then eventually out of that came Fedora.
[3192.64 → 3197.74] And there was this movement to try to get like this community-based distribution that all these
[3197.74 → 3198.74] companies work together with.
[3198.82 → 3199.20] What was it?
[3199.24 → 3199.64] Novel.
[3199.76 → 3202.22] And I forget all the companies involved in it.
[3202.22 → 3206.54] But basically the same kind of thing happened, and we're back there again.
[3206.98 → 3211.96] You know, I can't predict whether Red Hat is this is like a downhill slope for Red Hat
[3211.96 → 3215.08] or if this is a steady state for Red Hat.
[3215.30 → 3220.58] I don't think it's going to increase Red Hat's revenues for the next year or two.
[3220.72 → 3223.80] I think maybe for a quarter or two, they might have locked in some more contracts.
[3224.16 → 3227.12] Just from the people who read all the press and say like,
[3227.16 → 3230.06] oh my gosh, I'm building this stuff on Alma or Rocky.
[3230.06 → 3232.14] I got to stop that and move back to Red Hat.
[3232.22 → 3233.46] Because I need the support.
[3233.98 → 3238.64] But I don't think they're building that long-term relationship and the long-term trust.
[3238.78 → 3243.00] And like I said, I brought companies into Red Hat in my consulting work
[3243.00 → 3246.20] because I had, you know, learned on CentOS and I said,
[3246.28 → 3248.14] you need the support, and I'm not going to be there for you.
[3248.16 → 3249.10] So here, use Red Hat.
[3249.48 → 3250.38] And they could afford it.
[3250.38 → 3251.10] So they did.
[3251.62 → 3253.10] People like me are not going to do that.
[3254.02 → 3260.18] You're going to lose all of those leads, which maybe that's 10% or 12% or something.
[3260.18 → 3264.94] Maybe it's not a huge majority, but that's a lot of the long-term relationships are built out of that.
[3265.00 → 3266.86] And they just said, nope, gone.
[3267.18 → 3269.32] Like that they provide no value was the words.
[3270.16 → 3273.56] I want to key on one thing too, because I've been watching you on YouTube for a while, Jeff,
[3273.62 → 3279.40] probably at least a year, maybe two years when I got into Raspberry Pis more and Pi Hole and just home lobby stuff.
[3279.44 → 3280.50] So probably several years.
[3280.50 → 3285.40] And I think as I've watched you, you're in that obvious hobbyist and hacker.
[3285.60 → 3289.54] Like you're just, you're literally tinkering and trying to like to break things in most cases.
[3289.54 → 3290.54] Like, will this even work?
[3290.60 → 3292.32] Will this Pi Hole NAS scale?
[3292.46 → 3296.22] Like, will it actually be able to transmit data across the LAN at speeds I think?
[3296.36 → 3298.04] Can you do a petabyte on a Raspberry Pi?
[3298.30 → 3299.60] You've done all these crazy things.
[3299.66 → 3302.94] And so I think in many ways you find ways to innovate, and you're in that category.
[3302.94 → 3308.52] And if you, I'm sure you've even helped many companies who come to you with saying, hey, Jeff, here's my product for free.
[3308.66 → 3311.60] You don't have to talk about it, but if you like it, do a video.
[3311.64 → 3313.30] And I'm sure you've done it at least a couple of times.
[3313.62 → 3315.08] So you've profited those companies.
[3315.10 → 3316.88] You've helped them in some way, shape or form.
[3317.50 → 3318.44] And you're a tinkerer.
[3318.68 → 3327.58] And so if you PO the tinkers like you, which I'm sure there's many like you who don't have YouTube channels and don't do all the things you do, but do them in the behind the scenes.
[3327.58 → 3334.76] If you cut this kind of people out from a RHEL standpoint, and you don't bring customers to RHEL anymore, that is bad.
[3335.66 → 3336.08] Right?
[3336.18 → 3336.66] That's just bad.
[3336.66 → 3337.72] But it provides no value.
[3338.04 → 3338.72] No value.
[3340.76 → 3341.70] It's just crazy.
[3341.94 → 3344.62] And the other thing that I think about too is like seeing the responses.
[3345.12 → 3346.56] Obviously, there are a lot of red hatters.
[3347.22 → 3355.50] I mean, for me, if somebody attacks my family or my organization that I like being affiliated with or Drupal, let's say, I'm going to feel offended by that.
[3355.60 → 3356.52] That's just human nature.
[3356.52 → 3359.80] So I don't take offence to their kind of lashing back out.
[3360.18 → 3364.92] But outside the Red Hat community, I haven't ever seen someone say like, man, they did the right thing.
[3365.00 → 3368.42] I've seen a lot of, you know, you shouldn't be so harsh on them.
[3368.68 → 3370.98] But yeah, they shouldn't have done that that way.
[3371.14 → 3373.16] That's like as positive as I'll get.
[3373.16 → 3380.20] And someone mentioned this morning, I think at this point, I try not to respond to anything because it just raises my blood pressure a little bit.
[3380.28 → 3385.06] And right now I'm trying to work on a video that I've been working on for six months and I just need to finish this darn thing.
[3385.06 → 3389.60] And I started working on it when I saw the I think somebody on YouTube reported the thing.
[3389.68 → 3392.06] And then I was like, there's no way that Red Hat is actually doing this.
[3392.08 → 3395.24] And I read the blog post, and I'm like, oh my gosh, I have to say something.
[3395.36 → 3396.64] And that's when I posted Red Hat.
[3396.74 → 3397.22] Are you dumb?
[3397.70 → 3399.60] I was like, that's the only words I could come up with.
[3399.96 → 3403.46] But there's nobody that I've met that's like, that was right.
[3403.88 → 3408.04] There's a few business type people who I don't know from open source, but I know from other things.
[3408.04 → 3410.04] And they're like, why are you so angry about this?
[3410.14 → 3415.68] It's like, but once you explain, like it's the open source side of things, they're like, oh, okay, I can see how you're offended.
[3416.06 → 3421.30] From a purely business mind, yeah, it's somebody's taking your product and basically re-stamping it.
[3421.72 → 3423.58] Yeah, that's terrible from a business side.
[3424.04 → 3433.38] From a community side, the way that it was handled, the way it was announced, the way it was rolled out, the way that they're responding still in things, it just smacks me the wrong way.
[3433.38 → 3439.18] You said you couldn't predict the future, but we have a mutual friend, somebody you quoted, Corey Doctorow.
[3439.38 → 3440.10] He's been on the show.
[3440.20 → 3443.78] He's said the word and should have vacation on this show before and explained it in detail.
[3443.96 → 3445.48] We'll link that in the show notes to a few listeners.
[3445.96 → 3448.78] But he may have predicted to some degree what may happen here.
[3448.80 → 3451.60] He says, quote, here is how platforms die.
[3452.02 → 3453.78] First, they're good to their users.
[3454.34 → 3458.46] Then they abuse their users to make things better for their business customers.
[3458.46 → 3463.94] Finally, they abuse those business customers to claw back all the value for themselves.
[3464.28 → 3465.02] Then they die.
[3465.58 → 3469.48] I'm not sure if that's a prediction necessarily, but what was the show title, Jerry?
[3469.54 → 3470.64] He just wrote the book on it.
[3470.64 → 3471.18] What is it called?
[3471.70 → 3472.64] Gateway Capitalism?
[3473.28 → 3473.64] Choke point.
[3473.78 → 3474.68] Choke point Capitalism.
[3474.72 → 3475.04] That's right.
[3475.14 → 3477.96] This is an example of, this is a choke point.
[3478.62 → 3483.88] I almost invited Corey on this show to talk with us because I figured he'd have some angle, but he has so much to say.
[3483.94 → 3484.44] I thought I would like.
[3484.88 → 3487.22] I cited that in my video on this.
[3487.22 → 3489.52] And that video, I was never going to make that video.
[3489.62 → 3493.12] Even after I read that thing, I was going to make my one blog post, Red Hat, are you dumb?
[3493.26 → 3500.42] And then after I posted that and got so much backlash from Red Hat employees, I put, I'm not going to support Red Hat and Enterprise Linux moving forward.
[3500.84 → 3501.88] That was going to be the end of it.
[3502.00 → 3504.96] But after those two things, and then that third blog post.
[3505.28 → 3505.86] I'm done.
[3506.08 → 3510.26] I was like, no, I'm going to make a video on this because they're not seeing anything.
[3510.26 → 3515.86] So if they had not responded in the way that they did, I would have never made the video that has half a million views.
[3516.02 → 3519.16] And right now is the number one video I've ever made on my YouTube channel.
[3519.36 → 3520.80] Like I would have never done that.
[3520.92 → 3524.28] I would have never made the decision to stop supporting Red Hat Enterprise Linux.
[3524.96 → 3525.66] I don't know.
[3525.74 → 3530.00] For me, it's like this is a demarcation line and they have crossed it.
[3530.10 → 3533.86] And they look like they're turning further that way in their response.
[3533.86 → 3538.36] And like I said, I still think that they could come back, but they're not right now.
[3538.56 → 3541.72] And all the things that I'm doing, I'm like, please come back.
[3541.80 → 3545.48] Like I still want to be part of that, but not as much anymore.
[3545.48 → 3549.30] And at this point, you know, like I said, I've moved over to Debian for all my servers.
[3549.78 → 3554.48] I think I have one Red Hat 7 server running backups right now in the cloud.
[3554.98 → 3559.12] And I don't like touching my backup servers because once they're running, you don't want to touch them.
[3559.50 → 3560.72] So I'm just waiting until that one's done.
[3560.78 → 3561.78] Then I'm going to move it to Debian.
[3561.78 → 3565.72] What do you think is going to happen or should happen to Rocky and Alma?
[3565.80 → 3569.40] What should they do as a response to this?
[3569.72 → 3570.42] What are their options?
[3571.02 → 3576.24] I don't like the business side of what I never knew what CIQ was coming into all this.
[3576.64 → 3579.48] I knew there was Rocky Linux and Alma Linux, and they solved my problem.
[3579.70 → 3582.78] And that problem was I was using CentOS for all my testing and stuff.
[3582.92 → 3585.46] And that went away and stream was not a good replacement.
[3585.86 → 3588.62] So I switched to Rocky and I could have switched to Alma.
[3588.78 → 3590.26] It was kind of 50-50.
[3590.26 → 3592.94] They both were kind of like, here's the thing.
[3593.04 → 3596.20] And I was trying to figure out which one is going to have the longer runway.
[3596.44 → 3604.18] And it seems like both have equal footing in terms of how stable they've been and how quickly they've gotten releases out and how they've adapted and things.
[3604.84 → 3610.06] But I mean, on the business side, I didn't know anything about CIQ until this whole thing blew up.
[3610.06 → 3616.12] I still don't know if they were underhanded because, like I said, I could sell support services for Ansible.
[3616.22 → 3620.98] As long as I say I'm not Red Hat, I'm just Jeff Deerling selling support services for Ansible.
[3621.12 → 3625.40] I don't see anything wrong with that from a business perspective because it's a downstream thing.
[3625.80 → 3635.42] That is where, like, if CIQ did do all this and was trying to get contracts selling Red Hat but not Red Hat and all that, I don't know exactly how that happened.
[3635.42 → 3637.54] And, you know, yeah, that seems a little shady.
[3637.90 → 3638.82] But on the flip side.
[3638.92 → 3639.68] Where did you hear this stuff from?
[3639.80 → 3640.86] What posts were that in?
[3641.00 → 3642.06] Where did you get this information?
[3642.56 → 3646.44] In a bunch of posts on LinkedIn from Red Hat Solutions Architects, basically.
[3646.66 → 3648.36] Can you share those links with us so we can put them in the notes?
[3648.78 → 3649.54] I can, yeah.
[3649.62 → 3652.76] And there was an InfoWorld article, I think, too, that implied as much.
[3653.22 → 3657.42] I think it was Matt Hesse wrote an article where I was like, did Red Hat write this or did you write this?
[3657.50 → 3657.80] I don't know.
[3657.80 → 3663.44] But, yeah, I don't know where, you know, Alma seems to be, like, the thing that got sucked into all this.
[3663.72 → 3668.64] And it seems like the attacks were all against CIQ and, by extension, Rocky Linux.
[3668.80 → 3680.36] That's what it felt like to me from all the posts that I saw on LinkedIn and from the implications in posts on Reddit, especially by Mike McGrath, who wrote those two blog posts that are on Red Hat's blog.
[3681.24 → 3685.64] Alma, they seem like they still don't 100% have a path forward.
[3685.64 → 3689.12] They said, like, we're in this, we're going to help you, we're going to do this.
[3689.36 → 3697.92] And, you know, I think one thing on the table is just going to stream and, like, following the major releases and switching to a five-year support plan.
[3698.42 → 3700.26] So I don't know where they're going to go.
[3700.50 → 3705.12] With Rocky, I think that they're, so far, it seems like they're just going to pirate open source.
[3705.26 → 3706.10] Like, that's their plan.
[3706.46 → 3710.24] And I think that's kind of fun because it's, like, memeable.
[3710.56 → 3713.90] Like, I'm going to steal open source software.
[3713.90 → 3719.18] You know, that doesn't compute, but that is the reality that we're in at this point.
[3719.52 → 3722.74] You know, I was thinking, like, if they wanted to, I have a Red Hat subscription.
[3723.14 → 3725.96] If they want to burn mine, I'll download one point release.
[3726.04 → 3726.46] That's fine.
[3727.76 → 3729.20] I'll be part of that cause.
[3730.56 → 3731.06] I love it.
[3731.14 → 3732.42] So that's crazy.
[3732.68 → 3738.40] You can, like, not literally employ, but employ folks who are willing to give you the sources.
[3738.82 → 3739.50] Give you the sources.
[3739.50 → 3743.68] Red Hat burner accounts to try to steal open source code.
[3743.90 → 3744.04] Right.
[3744.60 → 3752.72] I still think that given enough money and enough good lawyers, someone could fight the LA restrictions.
[3753.14 → 3758.68] Because the restriction basically says, you are free to do whatever you want with the open source software, the source code.
[3758.68 → 3765.50] But if you share it, if you exercise your right to share it, which the open source code says, you must not restrict the right to share it.
[3765.78 → 3768.48] If you do that, we'll end our business relationship with you.
[3768.84 → 3774.70] To me, that, like, as a Joe Blow on the street, that really sounds like coercion or intimidation.
[3774.70 → 3786.34] But because there's a contract versus a copyright, the copyright is the code, the contract is the LA, apparently, according to many legal experts I've spoken to, that's fine.
[3786.44 → 3792.30] It's okay to intimidate someone with your business relationship if it's just a copyright thing.
[3792.78 → 3799.02] That, you know, you copy the code, and then we'll terminate the thing, even though the code says in its license that you can't intimidate me.
[3799.02 → 3805.88] You know, it doesn't make sense, and it doesn't seem moral or ethical, but apparently it's legal.
[3806.04 → 3812.42] And that's from every person that I've talked to in corporate open source law that I've spoken to four different people now.
[3812.62 → 3815.06] All of them said they're pretty sure that they're in the clear.
[3815.26 → 3818.32] Like, they don't see any reason why this is going to be a problem.
[3818.78 → 3827.92] But like I said, I think if you had enough lawyers and enough money, which, again, Oracle is the only company on the planet that probably has the case and the lawyers that could back it up.
[3827.92 → 3837.16] I think that they're the only company that could make a challenge if they set things up where they pulled the code out of the Red Hat subscription and open sourced it.
[3837.52 → 3841.60] If I did it, I would just get my account terminated, and then I'd be like, oh, I hate you, Red Hat.
[3841.76 → 3842.94] And then nothing else.
[3843.08 → 3843.92] Then you'd be out of money.
[3844.04 → 3844.26] Yeah.
[3844.66 → 3846.76] I would run out of money in the first week.
[3846.92 → 3847.72] I guarantee it.
[3848.12 → 3849.10] The first day.
[3849.10 → 3850.26] And that's, you know, Red Hat.
[3850.76 → 3855.84] I think Red Hat's banking on that, that nobody would dare challenge it because it's shaky ground.
[3856.22 → 3857.42] But there is ground there.
[3857.92 → 3861.46] But it would require so much money and so much effort that nobody's going to do that.
[3862.26 → 3865.36] Well, let's end on something happier, something joyous.
[3865.48 → 3869.02] What's, if you want to talk about it, what's the six-month-long video you've been working on?
[3869.18 → 3869.88] What is it?
[3870.16 → 3871.16] When is it going to be out there?
[3871.58 → 3872.80] Have you heard of Mr. Beast?
[3873.20 → 3874.50] I have heard of Mr. Beast.
[3874.50 → 3881.76] So, Network Chuck and I went to Mr. Beast's studio, and we worked on a project for his
[3881.76 → 3883.26] one to a hundred video.
[3883.46 → 3888.16] The one where he put ages one to a hundred in little boxes, and they all had competitions.
[3888.56 → 3888.76] Okay.
[3888.90 → 3892.84] So if you watch that video, there are many points where they do votes and they hit a button.
[3892.84 → 3897.22] And one time a guy smashes it with his elbow a few times, which is like, oh, don't do it too much.
[3898.46 → 3899.50] They press buttons.
[3899.50 → 3902.52] And then when they reveal the vote, the rooms light up different colours.
[3903.58 → 3905.78] Chuck and I worked on that project.
[3906.10 → 3910.44] And I have, there are stories, many of which I can't tell.
[3910.58 → 3911.32] There are stories.
[3911.86 → 3913.48] How many are going to make it into the video?
[3913.48 → 3919.50] So I actually, just before the show, I finished writing my first draft.
[3919.74 → 3921.86] This has been months I've been working on this.
[3922.18 → 3928.40] I actually used AI to transcribe all the footage that I did into a huge document.
[3928.82 → 3932.58] And then I used another AI to summarize all that so that I would have the ability to
[3932.58 → 3935.36] know in my brain all the things I said so I could start writing a script.
[3935.84 → 3941.10] After months and months and having 13 hours of footage, I finally have a rough draft that
[3941.10 → 3946.12] is 42 minutes long, and I need to cut out at least 15 or so minutes to make it manageable.
[3946.96 → 3951.20] So that's my task this week is to try to get that down to like 25 minutes or so.
[3951.66 → 3953.18] And then it's still going to be a slog.
[3953.74 → 3954.46] When's the published date?
[3955.14 → 3956.90] I'm hoping in a week or two.
[3957.02 → 3958.72] My goal is the end of this month.
[3958.78 → 3965.34] So by the end of July, because I'm going to LTX and LTX is a conference run by Linus Tech
[3965.34 → 3966.86] Tips, the YouTube channel.
[3967.26 → 3971.06] And it has a lot of the YouTube creators in the tech space, especially PC building.
[3971.24 → 3973.24] We have a Home lab panel there, actually.
[3973.38 → 3974.18] That'll be kind of fun.
[3974.50 → 3974.82] That's cool.
[3974.90 → 3976.42] I think it'll be live-streamed on Float plane.
[3976.52 → 3978.78] I hope it'll be available afterwards, maybe on YouTube.
[3979.00 → 3982.02] But a lot of the Home lab YouTube community will be there.
[3982.12 → 3986.84] Wendell from Level on Techs and Patrick from Serve the Home, a bunch of other great folks.
[3987.08 → 3990.76] But at LTX, I have a couple big projects I've wanted to finish by then.
[3991.40 → 3996.10] So I have to finish editing this video like within a week or two so that I can work with
[3996.10 → 4000.68] the Mr. Beast folks because they also, they've grown to the size where now they have to care
[4000.68 → 4001.52] about legal things.
[4001.92 → 4004.78] You know, a lot of smaller YouTubers, it's like, oh, you're filming something and there's
[4004.78 → 4005.44] somebody in the shot.
[4005.52 → 4006.26] It's not a big deal.
[4006.64 → 4009.58] But like with Mr. Beast, it's like, we have the shot here.
[4009.62 → 4010.62] You got to cut that part out.
[4010.66 → 4011.46] And then I got to re-edit.
[4011.66 → 4013.50] And, you know, so I'll have to do all that stuff.
[4013.50 → 4018.74] So I have to finish the edit like next week so that we can re-edit by a week or two after
[4018.74 → 4020.42] that if I want this out by the end of the month.
[4020.52 → 4022.86] But I just said, I have to finish this thing.
[4023.00 → 4023.94] I've been working on it.
[4024.14 → 4031.80] I actually spent probably 50 or 60 hours testing things after the whole thing was over to validate
[4031.80 → 4033.78] things that we learned while we were there.
[4034.26 → 4037.26] For example, static electricity, button signalling.
[4037.84 → 4042.32] I've got a high speed camera to test some things with arcade buttons and different types of
[4042.32 → 4047.28] buttons that we used to validate some of the things that we found when we scaled it up
[4047.28 → 4049.30] to 100 rooms in a huge place.
[4050.08 → 4054.44] So, and I couldn't use Raspberry Pis because they were not in existence back then.
[4054.66 → 4054.96] Right.
[4055.16 → 4055.46] Not anymore.
[4055.58 → 4060.16] I ended up using these little things called LE potatoes, which are like Raspberry Pis.
[4060.16 → 4063.82] But as you'll see when I do the video, they had their own set of problems.
[4064.36 → 4065.58] Le potatoes, huh?
[4066.14 → 4067.20] Le potato, yeah.
[4067.50 → 4067.76] Wow.
[4068.04 → 4071.96] Well, we'll have to get you back after LTX then sometime to kind of dive into some
[4071.96 → 4072.46] home lobby things.
[4072.54 → 4075.04] We've been looking forward to talking about home lab stuff.
[4075.16 → 4081.50] I've been paying attention to you, Techno Tim, Wendell from Level 1, many others, of course.
[4081.90 → 4084.12] And I love talking about that stuff.
[4084.16 → 4089.16] And we have yet to really break the mould on talking about home lab stuff here on any of
[4089.16 → 4094.32] our shows because it's mostly around software development, infrastructure and cloud, but
[4094.32 → 4098.54] not so much like your own personal cloud or things you do behind the scenes at your house.
[4098.88 → 4101.06] Home lab has opened my eyes to a lot of things.
[4101.06 → 4105.78] You know, I've always had a little bit of something like one or two Raspberry Pis doing things.
[4105.90 → 4110.84] But when I got into it a couple of years ago, I've learned so much more with deployment,
[4111.24 → 4116.80] what makes certain software packages easier for it applies to small business, too, because
[4116.80 → 4118.64] you don't have a team of sysadmins.
[4118.72 → 4122.54] You usually got like the IT guy or a couple IT guys and an intern.
[4122.54 → 4134.52] So it really opened my eyes to the ecosystem around open source software for server type things and sharing and all that versus proprietary solutions for some things.
[4134.66 → 4139.36] Like I think at this point, I don't have anything proprietary running in my rack right now.
[4139.56 → 4141.18] I still have a bunch of stuff on my computer.
[4141.18 → 4143.54] But at this point, it's all open source on the rack.
[4144.00 → 4145.96] Is Unify's OS proprietary?
[4146.30 → 4146.50] Nope.
[4146.84 → 4147.94] I do not use Unify.
[4148.22 → 4148.84] So that is...
[4148.84 → 4150.08] I thought you had like something in there.
[4150.34 → 4152.38] No, all these YouTubers use Unify.
[4152.58 → 4153.12] Well, I do.
[4153.28 → 4154.54] So I have Netgear.
[4154.62 → 4155.40] Techno Tim does.
[4155.48 → 4156.34] Well, I guess just Tim.
[4156.58 → 4156.80] Yeah.
[4156.96 → 4157.32] Yeah.
[4157.40 → 4161.82] I mean, Unify, Ubiquity makes great stuff.
[4161.90 → 4162.08] Yeah.
[4162.20 → 4162.78] That's for sure.
[4163.24 → 4164.30] But it's A, expensive.
[4164.80 → 4165.94] And I try to go cheap.
[4166.48 → 4170.10] And B, I feel like I learn more when I don't have my handheld as much.
[4170.40 → 4173.24] Like when you have to get into the weeds on things, I like that.
[4173.56 → 4174.30] It is expensive.
[4174.78 → 4178.22] What do you use then as your primary gateway and like router and firewall?
[4178.22 → 4181.16] Drop some hardware and some software.
[4181.48 → 4184.22] Right now, it's an Asus running...
[4184.78 → 4185.60] What is their thing?
[4185.66 → 4186.70] It's not OpenWrt.
[4187.00 → 4188.90] The Merlin WRT or whatever.
[4189.10 → 4189.96] The Merlin firmware.
[4189.96 → 4192.64] And then I have this guy here.
[4192.76 → 4194.36] You can't see it if you're listening to a podcast.
[4194.36 → 4201.84] But I have this router box that was recommended by Serve the Home that has four 2.5 gig ports.
[4202.30 → 4204.58] And that'll be replacing that.
[4204.62 → 4206.28] I actually did that at my office already.
[4206.80 → 4211.12] I am building out a new office slash studio because the kids here at home...
[4211.12 → 4211.52] Too loud.
[4211.58 → 4212.60] ...make recording difficult.
[4214.38 → 4216.12] I have no idea what you're talking about.
[4216.24 → 4218.24] So I already have one there, and I'm going to put one in here.
[4218.24 → 4223.98] So then most of my switches are microtick because the price is right, the features are good, and they're quiet.
[4224.28 → 4225.22] Quiet is big for me.
[4225.42 → 4228.28] That's what Gerhard recommended, Jerry, when we talked to him last.
[4228.54 → 4229.20] Yes, he did.
[4229.68 → 4231.14] Yeah, microtick is what he recommended.
[4231.22 → 4233.12] Is that easily available in the U.S.?
[4233.12 → 4234.20] That was like a European brand.
[4234.52 → 4235.74] Most of the time they are.
[4236.18 → 4238.12] During the pandemic, things were wild.
[4238.32 → 4240.94] I had to buy one from Europe and then switch out the power cord.
[4241.20 → 4241.48] Gotcha.
[4241.48 → 4246.24] But nowadays, almost all their gear is available now through resellers here in the U.S.
[4246.72 → 4247.50] Cool stuff.
[4247.84 → 4249.06] I'm looking forward to that video.
[4249.98 → 4250.66] Get her done, will you?
[4250.86 → 4252.08] Jeff Deerling on YouTube.
[4252.28 → 4253.12] Watch all his videos.
[4253.22 → 4255.00] I watched not all, but some.
[4255.62 → 4259.92] Paid attention to some of the cleanup process you had for your new office.
[4260.72 → 4266.26] I'm planning to watch your all-flash NAS fight here shortly because I just love hosting data.
[4266.26 → 4268.06] I'm a sucker for ZFS.
[4268.06 → 4269.32] I just love hosting data.
[4269.78 → 4273.38] It's called the Pocket NAS.
[4273.58 → 4276.36] This was built by one of those hackers and hobbyists.
[4276.92 → 4283.08] These things are cool because it drives forward open source things like Open Media Vault, which is recommended for this thing.
[4283.68 → 4287.70] More users means more eyes on bugs, more bug reports eventually.
[4287.94 → 4290.96] If you get 100 more users and one of them is a contributor, that's awesome.
[4290.96 → 4291.36] Yeah.
[4292.32 → 4294.50] Do you have any unpopular opinions, Jeff?
[4294.70 → 4295.22] Any chance?
[4296.18 → 4297.94] Besides all the ones you just shared about Red Hat?
[4298.38 → 4298.78] Yeah.
[4300.02 → 4303.16] Some of those are not quite unpopular, but popular.
[4303.66 → 4303.96] No.
[4304.36 → 4307.60] I mean, for me, I still like to build my own stuff a lot of times.
[4307.80 → 4311.76] A lot of people use Not Invented here, you know, pull in all the things and rely on everything.
[4312.36 → 4317.66] But if you look at my Ansible roles, like most of those are based, most of my infrastructure is built on stuff I wrote.
[4317.94 → 4320.42] Which is funny because I have tons of users.
[4320.42 → 4326.04] But for anyone who really wants to get into it, I would say, like, fork my stuff and maintain it on your own.
[4326.04 → 4329.82] Don't use my stuff because you can make it better for your own infrastructure.
[4330.16 → 4331.22] For infrastructure especially.
[4331.42 → 4337.12] But for software too, I think after seeing the way that Drupal has gone and the way that other communities have gone,
[4337.12 → 4341.92] I kind of do see more value nowadays in building your own stuff.
[4341.92 → 4349.48] Even if you're redoing some things, instead of the Node.js approach where you have, like, to do a hello world, you have 350 libraries imported.
[4349.48 → 4349.88] Yeah.
[4351.32 → 4352.28] I like that one.
[4352.36 → 4352.74] I'm with you.
[4352.96 → 4354.44] It's popular with me.
[4354.92 → 4358.48] It's unpopular in some circles, the whole, like, anti-NIH.
[4359.44 → 4359.72] Yep.
[4360.24 → 4361.74] Well, it is a continuum, right?
[4361.80 → 4363.40] Like, it's a spectrum, right?
[4363.52 → 4365.20] You have dependency hell on one side.
[4365.76 → 4369.42] And you have, like, NIH to the nines on the other side.
[4369.66 → 4372.98] And we all have to figure out where we live on that spectrum.
[4372.98 → 4376.68] And I'm definitely more onto the NIH side of the fence.
[4376.92 → 4383.46] But you don't want to live on either extreme because you're either, you know, just gluing together other people's code endlessly.
[4383.90 → 4387.82] Or you're writing your own firmware for your ASUS.
[4388.40 → 4388.50] Yeah.
[4388.62 → 4394.94] And maybe Red Hat, the best opportunity out of all this is we can all write our own operating systems and maintain our own Linux distros.
[4394.94 → 4395.74] I think that's the takeaway.
[4396.06 → 4396.80] That's what they want us to do.
[4396.82 → 4397.74] That's the takeaway.
[4398.00 → 4398.56] That's what they want us to do.
[4398.86 → 4400.06] You can't have this one anymore.
[4400.14 → 4400.40] Bye.
[4401.16 → 4402.12] Well, Jeff, hey, thank you.
[4402.12 → 4406.30] I know that you got this Mr. Beast video that you just mentioned and all these things on your shoulders.
[4406.56 → 4407.52] I emailed you yesterday.
[4407.60 → 4408.28] You said yes.
[4408.38 → 4409.26] So I appreciate you.
[4410.14 → 4412.30] You know, maybe this is the end of your rant.
[4412.38 → 4412.78] I don't know.
[4412.84 → 4415.14] Maybe the end of all the things you had to say.
[4415.24 → 4416.32] Or at least, you know, a...
[4416.32 → 4419.20] Well, it depends on who comes in to beat the dead horse tomorrow.
[4419.28 → 4419.56] Right.
[4419.82 → 4421.18] First it was Oracle, then Seuss.
[4421.30 → 4424.00] It could just be a stepping stone on our way to somewhere else.
[4424.52 → 4430.16] But I appreciate you coming on, sharing your thoughts, and riff with me and Jared here on Change Looking Friends.
[4430.16 → 4431.36] It's been a blast.
[4431.36 → 4432.66] Yeah, thank you.
[4432.70 → 4433.34] Bye, friends.
[4433.80 → 4434.24] Bye.
[4434.24 → 4435.24] Bye.
[4440.58 → 4441.26] All right.
[4441.40 → 4442.84] That's the scuttlebutt for this week.
[4443.46 → 4448.60] Definitely check out Jeff's YouTube channel and let us know in the comments if you'd like to hear from him more on the show.
[4448.60 → 4451.44] Oh, and check out our YouTube as well if you haven't yet.
[4451.64 → 4456.06] We post clips from all of our pods, unpopular opinions, you know, just the good stuff.
[4456.60 → 4459.16] Find it at YouTube.com slash changelog.
[4459.16 → 4464.50] Thanks once again to our partners, fastly.com, fly.io, and typesense.org.
[4464.50 → 4469.52] And thanks, as always, to Break master Cylinder for ensuring we have the bagginess beats and all the biz.
[4470.00 → 4474.60] Coming up next week, changelog news on Monday, an awesome interview with Steve Edge on Wednesday,
[4475.06 → 4479.84] and our friends Brian Cantwell and Steve Tuck from Oxide Computer Company on Friday.
[4480.30 → 4482.58] That's a pretty good lineup, if I do say so myself.
[4483.24 → 4484.08] Okay, that's it.
[4484.18 → 4484.96] This one's done.
[4485.22 → 4486.96] But let's talk again real soon.
[4486.96 → 4487.96] Bye.

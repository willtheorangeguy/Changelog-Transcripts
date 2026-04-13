[0.16 → 5.76] Welcome to Ship It, a podcast about ops, infrastructure, and migrations.
[6.28 → 12.54] I'm your host, Gerhard Lazy, and today I talk to Mark Ericsson about all the things
[12.54 → 14.82] that we could be doing on the new platform.
[15.20 → 17.22] This is a follow-up to episode 50.
[17.84 → 19.66] Mark specializes in Elixir.
[20.00 → 26.74] He hosts the Thinking Elixir podcast, and he also helps make Fly.io the best place to
[26.74 → 29.76] run Phoenix apps, such as changelog.com.
[30.00 → 35.36] In the interest of holding our new platform right, we thought that it would be a great
[35.36 → 40.72] idea to talk to someone that does this all day, every day, for many years now.
[41.12 → 46.82] We touch up on how to run database migrations safely, and how to upgrade our new application
[46.82 → 49.22] config to the latest Phoenix version.
[49.62 → 54.70] We also talked about some of the more advanced platform features that we may want to start
[54.70 → 58.12] leveraging, like the multi-region PostgreSQL.
[58.12 → 63.24] Huge thanks to Vastly for shipping our episodes superfast all around the world.
[63.64 → 65.60] Check them out at Fastly.com.
[65.60 → 78.44] This episode is brought to you by MongoDB, the makers of MongoDB Atlas, the multi-cloud application
[78.44 → 79.30] data platform.
[79.82 → 84.74] Atlas provides an integrated suite of data services centred around a cloud database
[84.74 → 87.30] designed for scale, speed, and simplicity.
[87.78 → 92.20] You can ditch the columns and the rows once and for all, and switch to a database loved by
[92.20 → 94.84] millions for its flexible schema and query API.
[95.36 → 98.70] When you're ready to launch, Atlas layers on production-grade resilience, performance,
[98.96 → 101.90] and security so you can confidently scale your project from zero to one.
[102.26 → 104.62] Atlas is a truly multi-cloud database.
[104.94 → 110.40] Deploy your data across multiple regions simultaneously on AWS, Azure, and Google Cloud.
[110.80 → 111.92] Yes, you heard that right.
[112.00 → 115.26] Distribute your data across multiple cloud providers at the same time.
[115.50 → 117.34] The next step is to try Atlas Free today.
[117.34 → 118.70] They have a free forever tier.
[118.96 → 122.24] Prove yourself and your team that the platform has everything you need.
[122.68 → 124.76] Head to mongodb.com slash changelog.
[124.88 → 128.56] Again, mongodb.com slash changelog.
[133.90 → 137.90] We are going to ship in three, two, one.
[137.90 → 159.24] So we talked in episode 50 with Adam and Jared about migrating changelog.com from Kubernetes,
[159.84 → 161.58] LIKE specifically to Fly.
[161.58 → 168.86] And we have Mark from Fly joining us today to ensure that I'm holding it right.
[169.56 → 170.20] Welcome, Mark.
[170.68 → 171.08] Thanks.
[171.34 → 171.86] Glad to be here.
[172.30 → 173.92] Do you know what it means, holding it right?
[174.14 → 176.16] It sounds like, you know, it's a tool.
[176.44 → 177.92] And am I doing this right?
[177.96 → 178.80] Am I going to hurt myself?
[179.08 → 179.30] Yeah.
[179.82 → 180.56] That's what it means to me.
[180.76 → 188.80] We have plenty of experience of holding those tools wrong, starting with Vastly, the CDN.
[189.20 → 189.98] Sometimes Kubernetes.
[189.98 → 194.48] So I, you know, we just tend to hold them wrong, or I tend to hold them wrong.
[194.60 → 196.80] And I want to make sure that I'm holding it right.
[197.28 → 204.44] So my expectation is that after today's conversation with you, I will be holding Fly, Elixir and
[204.44 → 209.00] the combination much, much better than we were doing with Kubernetes and Elixir.
[209.42 → 212.04] So let's see how that works out in practice.
[212.86 → 218.60] So how long have you been running or being, how long have you been involved with Elixir applications,
[218.80 → 218.96] Mark?
[218.96 → 220.18] About six years.
[220.94 → 221.34] Okay.
[222.20 → 224.20] And what did you do before that?
[224.28 → 225.32] What did you do before Elixir?
[225.58 → 229.38] I started programming way long ago, like when I was, you know, younger.
[229.82 → 234.92] And, but really most recently before Elixir, I was in the Ruby world and doing Ruby on Rails
[234.92 → 235.36] development.
[235.36 → 239.56] And prior to that, it was, I was in C sharp, you know, .NET.
[239.56 → 244.24] And then when I learned Rails, it was like, oh my gosh, this is such a better way to do
[244.24 → 248.10] web development than what was, you know, even pre MVC with .NET.
[248.10 → 250.22] So I fell in love with Rails.
[250.22 → 251.34] Like, that's what I want to do.
[251.58 → 257.34] And then eventually I discovered Elixir and that's really captured my attention.
[257.34 → 260.20] It was like, oh my gosh, this is, this is the way I want to be doing development.
[260.46 → 261.06] Nice.
[261.06 → 262.56] And I made that switch.
[262.78 → 262.88] Yep.
[263.24 → 263.54] Okay.
[263.54 → 268.32] So when you were doing Ruby on Rails, where did you use to deploy your applications?
[268.64 → 269.42] How did that work?
[269.68 → 272.76] Yeah, we had gone through multiple different jobs.
[273.00 → 277.52] Sometimes the companies were large enough where we had our own operations teams and they
[277.52 → 278.36] managed all of that.
[278.42 → 279.76] It was completely invisible to me.
[279.86 → 283.10] So I was just among the pool of developers, right?
[283.60 → 288.72] And then other places, much smaller companies, development and management of those servers fell
[288.72 → 289.92] to our responsibility.
[289.92 → 296.42] And we would have problems where sometimes we would be on a server and the server would
[296.42 → 296.88] just die.
[297.00 → 298.30] And we didn't really know why.
[298.74 → 299.82] And so you restart it.
[300.28 → 303.56] And eventually it was like, you know, it'll just be easier if we went to Heroku.
[303.92 → 310.26] So we just, even though it was more expensive, it was moving the app to run on Heroku when
[310.26 → 316.48] we had Rails, just because we didn't have the platform experience for maintaining that.
[317.60 → 318.04] Okay.
[318.04 → 322.94] So self-hosted on Bare Metal or VMs for a while.
[323.54 → 324.68] Cristiano, maybe.
[324.98 → 325.10] Yep.
[325.48 → 325.70] Yep.
[326.12 → 326.74] That was there.
[326.84 → 327.30] I remember.
[327.66 → 331.54] Mina, a puppet chef that was used as well for deployment for a while.
[331.80 → 332.94] And a couple of others.
[333.20 → 334.28] Ansible came along.
[334.56 → 334.82] Docker.
[335.28 → 337.20] How was your Docker with Ruby on Rails?
[337.28 → 339.08] Did you have such a phase?
[339.22 → 340.34] We never really went that way.
[340.52 → 340.82] Okay.
[341.10 → 345.48] It was more of, we were just deploying the code up and starting up like that.
[345.64 → 345.78] Yeah.
[345.78 → 346.22] Yeah.
[346.22 → 351.48] And then Heroku, like the huge past movement that changed a lot of things.
[351.48 → 355.64] I remember when it came along, and I resisted, and I resisted until Cloud Foundry got me
[355.64 → 356.08] eventually.
[356.28 → 358.44] So I got the build packs experience in Heroku.
[358.98 → 360.16] And then Elixir came along.
[360.80 → 365.16] And I'm not sure whether the experience is better now that it was seven, eight years ago
[365.16 → 370.70] of running Erlang apps, Beam VM apps specifically on Heroku.
[370.70 → 374.46] But I remember the Elixir build pack and the Erlang build pack were not very good.
[374.54 → 375.90] Again, seven, eight years ago.
[376.06 → 377.94] Did you deploy any Elixir apps on Heroku?
[378.32 → 379.12] I never did.
[379.28 → 379.50] No.
[379.74 → 380.00] Okay.
[380.10 → 384.04] So I think you saved yourself a lot of pain because I think we were like both around the
[384.04 → 385.08] same time doing this.
[385.14 → 387.46] And it was just like, you know, not very nice.
[387.82 → 391.36] And then you went to Elixir and then what did you do then?
[391.46 → 394.52] Did you continue with Heroku or actually, no, sorry.
[394.58 → 395.50] You just said that you didn't.
[395.58 → 397.08] So what did you do when you had Elixir apps?
[397.18 → 398.10] Where would you deploy them?
[398.18 → 398.88] How would you run them?
[399.24 → 399.42] Yeah.
[399.50 → 404.58] So I was at a company where we had quite a few Ruby apps that were still Ruby on Rails.
[404.74 → 407.26] And we were starting a migration to Elixir.
[407.40 → 409.98] So we had multiple large services.
[410.16 → 414.62] It wasn't like the microservices, but they were services with single responsibilities.
[415.26 → 422.68] And so we started to, initially, they were just on AWS EC2 instances that we were just managing
[422.68 → 423.14] ourselves.
[424.12 → 427.36] And then it was, you know, we could do better.
[427.36 → 430.02] It would be easier to manage this if it was in something like Kubernetes.
[430.82 → 433.84] So we actually went with AWS EC2 or...
[434.38 → 434.74] EKS?
[435.44 → 435.76] Yes.
[436.02 → 442.98] So we actually went with the Amazon EKS as the managed Kubernetes server, which was super
[442.98 → 443.26] helpful.
[443.56 → 446.96] So we didn't have to deal with that, but we still had to deal with, okay, now we have
[446.96 → 448.74] these Ruby apps and these Elixir apps.
[448.74 → 453.90] So yes, we turned to Docker for those, getting those all containerized and then being able
[453.90 → 458.94] to have the services be expressed and defined to have these different apps talk to each
[458.94 → 460.36] other in our Kubernetes cluster.
[460.62 → 460.90] Okay.
[461.02 → 466.80] I'm curious to know how much of those operational concerns of the production runtime concerns
[466.80 → 469.90] leaked into how you develop apps.
[469.90 → 474.24] So when you had Elixir, did you run a local Kubernetes cluster?
[474.40 → 479.16] How would you make sure that it works in production before you go to production?
[479.42 → 480.90] I mean, did you have such problems?
[481.22 → 482.00] That's a good question.
[482.16 → 486.44] So I was the one who kind of introduced Kubernetes at that company.
[486.68 → 491.56] So I was the one who went through Minimum, figuring it out, went through several books and
[491.56 → 492.96] trying to understand it all.
[492.96 → 496.76] And once I got it, it's like, okay, this is how we can do this.
[497.22 → 501.08] I think it does influence how we build our apps.
[501.54 → 502.10] It can.
[502.34 → 505.70] Sometimes I don't think it's even necessarily a conscious decision, like, oh, this will
[505.70 → 506.72] be an easier way to do it.
[506.98 → 511.76] It's just, if you're aware of how it's being deployed, you might make choices.
[512.02 → 515.56] Just say, just that it's kind of in the background of your mind.
[515.84 → 520.82] I'm also thinking about the specific versions that you use, because if you develop on a Mac,
[520.82 → 525.40] and I think the majority does on macOS, you install Erlang, right, for like an Elixir
[525.40 → 525.92] application.
[526.58 → 527.76] Which version do you install?
[528.06 → 528.94] How do you install it?
[528.98 → 531.14] How does it link against the system libraries?
[531.92 → 533.44] OpenSSL, how do you solve that problem?
[533.62 → 536.12] Do you even test with OpenSSL in development?
[536.24 → 537.26] Do you even configure that?
[537.78 → 543.18] And if you do, how does that version of OpenSSL correspond to the production version?
[543.34 → 545.48] And then you have a database, or maybe you have other systems.
[545.58 → 549.24] And before you know it, you have like this huge setup that every single developer has
[549.24 → 553.52] to figure out on their machine, and it will be different, maybe even between other developers.
[553.92 → 557.32] You have different macOS versions, maybe someone wants to develop on Linux.
[557.56 → 560.68] And before you know it, you have like this sprawl, like these different ways of developing
[560.68 → 561.14] things.
[561.32 → 566.12] And we all know that if it works on your machine, it doesn't mean it works, right?
[566.76 → 567.30] It's true.
[567.30 → 572.56] So how do you handle that problem with the version of Postgres SQL?
[572.86 → 577.14] Because I'm imagining there will be a database with a version of Erlang when you work locally
[577.14 → 579.10] versus when it runs in production.
[579.30 → 580.76] Did you have any such issues?
[581.10 → 583.04] You know, like you bring up Postgres, right?
[583.20 → 587.86] Like certain features are available in different versions of Postgres that aren't available in
[587.86 → 588.12] others.
[588.12 → 591.68] And it is a choice you have to make as a team.
[592.06 → 597.96] And really, it is a you kind of, I think the team has to decide what do we value?
[598.20 → 600.56] What do we want to say is a minimum requirement?
[601.10 → 603.14] So we're all on this version of Elixir.
[603.24 → 605.68] We're all on this version of Ruby.
[606.34 → 611.40] And yeah, if you're on a Mac, then sometimes the OpenSSL issue becomes an issue.
[611.40 → 616.30] And when the macOS gets updated, myself, I run on Linux.
[616.30 → 622.12] And so, yeah, I was that guy who is like the one on Linux who's creating that little friction
[622.12 → 622.42] there.
[622.68 → 622.80] Yeah.
[622.94 → 626.32] And you would say to everyone, everybody run Linux and no one would listen.
[626.56 → 627.56] And you get so frustrated.
[628.04 → 629.10] But it's so much better.
[629.50 → 632.22] And hey, it's going to be running on Linux and the server, right?
[632.34 → 632.68] Exactly.
[633.56 → 635.94] They would ask you which Linux version.
[636.06 → 636.84] And you go, oh, you know what?
[636.88 → 637.34] It doesn't matter.
[637.42 → 638.94] It's a different operating system in production.
[639.14 → 640.04] All that matters is Linux.
[640.14 → 641.08] Different kernel version.
[641.44 → 642.42] Let's ignore that part.
[642.58 → 643.04] It's Linux.
[643.16 → 643.98] That's what we care about.
[643.98 → 646.88] Yeah, I'm not running CentOS on my desktop, right?
[647.44 → 647.84] Okay.
[648.32 → 650.64] By the way, what do you run on your desktop?
[650.72 → 651.38] I'm very curious.
[651.66 → 654.48] It's an Arch Linux based distro.
[654.76 → 655.04] Okay.
[655.26 → 656.16] How do you install Erlang?
[656.48 → 656.86] Erlang?
[657.48 → 659.44] I use a tool called ASD.
[659.56 → 663.62] It is a version manager for lots of different tools.
[664.12 → 668.50] So I use it to manage my Erlang version, my Elixir version.
[668.76 → 670.48] It'll also do Node and Ruby.
[671.12 → 672.64] And it can even do things like Postgres.
[672.64 → 680.66] And what I like about that is there is a file that it generates called a .tool-versions.
[681.14 → 685.00] And that records the different versions of the tools that ASD is using.
[685.40 → 688.22] And so some people can actually check that into a project.
[688.22 → 693.12] So you can create a global one that might sit in your home directory or a local one that's
[693.12 → 695.40] specific to a project, which I really like.
[695.40 → 699.42] So as I change directories around and, oh, I'm going to be going over here to this older
[699.42 → 700.38] Ruby project.
[700.58 → 705.32] As I change into that, it activates the older version of Ruby that's appropriate for that
[705.32 → 706.80] particular project.
[706.80 → 710.66] And the same thing when I'm going to between different Elixir applications.
[711.10 → 712.50] Like I haven't upgraded this one yet.
[712.56 → 715.98] It's on an older version of OTP, the Erlang version and Elixir.
[716.22 → 717.58] So I like that.
[717.64 → 718.34] That's my preference.
[718.34 → 723.06] Okay, I have never used ASD, but I'm curious now.
[723.40 → 728.84] I'm very curious how it compares to NixOS, which is something that I've recently picked
[728.84 → 730.94] up on my Linux host.
[731.34 → 735.48] I don't use it because like my development is spread across a number of machines.
[735.98 → 741.62] There's an iMac, there's a MacBook Pro, and I use this Linux host, which is a fairly new
[741.62 → 741.86] one.
[742.10 → 744.74] I love that it's fanless, no fans.
[744.74 → 748.64] Even like the MacBook Pro has fans and the iMac definitely has fans.
[748.86 → 752.52] I can tell even if it's a Pro, I mean, wow, they can get really loud sometimes.
[753.18 → 758.68] And I'm curious to see how ASD works because what I used to do, and even now for changelog,
[759.06 → 765.14] we have a make file and the make file resolves a bunch of dependencies, especially from an
[765.14 → 766.12] operational perspective.
[766.44 → 770.28] So subject we're using, glycol we're using now.
[770.28 → 776.30] It installs a specific version locally in the .bin directory, the .bin being local to
[776.30 → 777.64] whichever directory we are in.
[777.94 → 779.72] It doesn't have our managed Postgres SQL.
[779.88 → 781.36] For that, we're using Docker Compose.
[781.58 → 783.38] And on a Mac, the experience isn't very good.
[783.58 → 784.94] On Linux, it's slightly better.
[785.38 → 790.44] But I still think that like the native workflow, you know, like not having any containers, not
[790.44 → 792.10] having any VMs, it's much, much better.
[792.52 → 796.36] Now, the flip side to that is if you can spin up a VM where you can do your development,
[796.36 → 801.74] these become almost like non-concerns because we just spin up a VM based on, or like a host,
[802.04 → 802.22] right?
[802.34 → 804.64] Whether it's a VM bare metal doesn't really matter.
[805.14 → 808.28] And that tends to like GitHub code spaces, I'm thinking.
[808.52 → 811.08] That is a very interesting proposition for sure.
[811.58 → 812.84] ASD, I will check it out.
[812.92 → 816.98] I'm just curious how it compares to NixOS and the things that I've been learning there,
[817.04 → 822.42] because I really think like those namespaces where you get the exact versions, those directories
[822.42 → 823.18] where you go.
[823.18 → 826.40] I mean, they're just as a concept, super, super important.
[826.78 → 830.82] Then how do you make sure that what you run locally and what you develop against is what
[830.82 → 831.58] you get in production?
[831.88 → 832.66] Like, is that important?
[832.76 → 834.86] Did you ever find that being an important thing?
[835.22 → 838.88] Well, I think it's interesting just that you mentioned NixOS because I've been hearing
[838.88 → 840.52] about it in the Linux space.
[840.86 → 842.08] It is a very different thing.
[842.16 → 845.40] It's more of a it's like an alternative to Docker, right?
[845.42 → 849.76] It's like a declarative expression of this is what the system should look like.
[849.76 → 851.24] And then it can bring that up.
[851.24 → 852.62] It's something I've been wanting to play with.
[852.72 → 854.74] So I'll have to pick your brain some other time about that.
[854.96 → 855.06] Okay.
[855.58 → 860.74] As far as the difference between production environment and the versions of things and
[860.74 → 864.74] local development, it really hasn't been that much of an issue.
[864.96 → 869.20] Usually it would be something that we might feel between members of the same team as we're
[869.20 → 869.82] checking out.
[869.82 → 872.62] Someone adds a new library, for instance.
[873.30 → 876.70] And then there might be an issue that we discover at that time.
[876.96 → 882.40] But in terms of avoiding those problems on production, it's always, I count on a staging
[882.40 → 883.60] environment, right?
[883.64 → 889.98] That I'm going to be deploying to a production-like environment, may even have access to like a
[889.98 → 891.52] backup of the production data.
[891.52 → 896.00] And I'm going to do some basic sanity checks there.
[896.44 → 900.50] Like in any kind of like where I care about uptime, I care about the service that I'm providing
[900.50 → 901.12] to my customers.
[901.38 → 902.82] I'm going to use a staging environment.
[903.74 → 904.18] Okay.
[904.28 → 905.88] So we already have three.
[906.14 → 908.96] We already have a local development environment.
[909.26 → 912.64] We have a staging environment, and we have a production environment.
[912.64 → 916.04] And I think that is like the starting point for the majority.
[916.58 → 918.40] Some of us like to write tests.
[918.40 → 921.04] So then you have a testing environment as well.
[921.12 → 925.16] So now we have four places where we need to make sure that things are in sync because
[925.16 → 929.22] otherwise versions are in sync, you know, upgrades whenever you do any security patches.
[929.68 → 931.22] What is the impact on performance?
[931.44 → 933.36] What is the impact on latency?
[933.68 → 934.78] Whatever the case may be.
[934.92 → 936.24] Performance means different things.
[936.80 → 940.06] Let me just clarify that with latency and throughput.
[940.76 → 945.26] And while, okay, like in some cases you need like staging, you don't do this maybe in
[945.26 → 945.62] staging.
[945.62 → 951.14] But I know that, for example, changing the open SSL library or upgrading your kernel will
[951.14 → 953.78] have certain performance implications and heart bleed.
[953.88 → 954.66] Oh my goodness me.
[954.74 → 955.54] I still remember that.
[955.64 → 957.24] And all the Intel patches.
[957.58 → 959.54] And so those were like pretty bad ones.
[959.66 → 962.08] And then why is my application 50% slower?
[962.18 → 962.78] Nothing changed.
[962.88 → 963.80] Oh, there's this new library.
[963.84 → 967.58] And before you know it, two months have passed, and you're still trying to figure out what
[967.58 → 968.06] went wrong.
[968.56 → 973.54] So, okay, let's put up in that because I think we're getting a bit ahead of ourselves.
[973.54 → 977.60] But the one thing which keeps coming up are versions.
[978.14 → 982.64] And when we started with the Changelog app, which is an Elixir app, I forget which version
[982.64 → 985.62] it was, but it was definitely not 1.6.
[986.00 → 991.12] So our application was generated a couple of years ago, three at this point, maybe four.
[991.44 → 992.08] I lost count.
[992.38 → 995.36] I don't know which version of Phoenix we're using then, but things are very different.
[995.36 → 999.30] So is there something for us to do there, do you think?
[999.60 → 1002.30] How do we reconcile this old app?
[1002.38 → 1004.52] How do you even know what is new in Phoenix?
[1005.14 → 1009.34] That is a problem I faced a lot, like even just in Rails, right?
[1009.60 → 1013.32] If you've been in the Rails space, or I think it's the same with any framework, you know,
[1013.38 → 1017.80] I don't have any personal experience, but I can imagine Django and everything else has
[1017.80 → 1023.24] the same kind of situation where I generate an app, and it's using some template to start
[1023.24 → 1025.32] out a lot of my files, which I then customize.
[1026.14 → 1031.98] And I had the same problem with Rails that we have in Phoenix, which is I started it, it
[1031.98 → 1033.12] was generated a bunch of files.
[1033.26 → 1038.94] I've customized the configs and everything has drifted from what it originally was.
[1038.94 → 1044.10] And now I've tried to continually keep current with what version I'm on.
[1044.44 → 1048.82] Like I'm wanting to move my version of Phoenix or Rails to be newer and newer and newer.
[1049.02 → 1054.34] And I might even go through the changelog notes to see what are the things I need to change.
[1054.44 → 1057.52] But still, the generated files are not the same, right?
[1057.58 → 1059.06] It's still going to be different.
[1068.94 → 1073.78] This episode is brought to you by our friends at Ray gun.
[1073.98 → 1078.60] They give software teams instant visibility into the quality and the performance of their
[1078.60 → 1079.02] software.
[1079.50 → 1082.90] And I'm here with John Daniel Track, co-founder and CEO of Ray gun.
[1083.26 → 1088.56] JD, talk to me about the joy a team feels when they're able to find and resolve an issue,
[1088.68 → 1094.32] even before a customer has a chance to get upset or reach out to support about the issue.
[1094.60 → 1095.28] Talk to me about that.
[1095.60 → 1098.52] Well, I find it pretty exciting to be able to hit it off early.
[1098.96 → 1101.08] So and being able to tell people that you resolved something.
[1101.22 → 1105.14] So maybe they come through, you know, and they do report an issue, and you can say, cool,
[1105.22 → 1107.28] we don't need to ask you for any more context.
[1107.42 → 1109.66] We've got all the details, and can have this fixed tomorrow.
[1109.92 → 1112.92] It turns an at-risk customer into an absolute raving advocate.
[1113.16 → 1114.26] So that's a huge win.
[1114.36 → 1116.16] And then the other thing that was a little bit embarrassing.
[1116.44 → 1119.84] We launched Ray gun, but we had these other products and we instrumented them.
[1120.02 → 1124.16] And that's when we realized this less than 1% of our users would ever actually report
[1124.16 → 1124.60] a problem.
[1125.02 → 1127.72] And so you're sitting there thinking your software is actually not bad.
[1127.72 → 1130.58] And actually, it's really, terrible.
[1130.66 → 1133.92] And that's hurting all of your conversion rates, business performance here.
[1134.08 → 1135.02] These aren't really dev tools.
[1135.10 → 1136.32] They're actually business tools.
[1136.88 → 1137.00] All right.
[1137.00 → 1140.02] If you want to see how this dev tool impacts the entire business,
[1140.16 → 1144.00] head to raygun.com to learn more and start your 14-day free trial.
[1144.12 → 1145.46] No credit card required.
[1145.92 → 1150.58] Join thousands of customer-centric software teams who use Ray gun every single day
[1150.58 → 1153.04] to deliver flawless experiences to their customers.
[1153.32 → 1154.96] Again, raygun.com.
[1154.96 → 1173.94] So I would like to understand how can we upgrade the files that we're generating in our application?
[1174.10 → 1176.20] First, how can you even tell what the differences are?
[1176.56 → 1178.44] Because it's not something that we do often.
[1178.44 → 1184.50] So we can talk about the practical steps of figuring out what the diff is between
[1184.50 → 1189.38] the latest version of Phoenix and the one that we're using, which I don't even know what it is.
[1189.54 → 1192.80] It doesn't really matter because it's the differences, reconciling those differences.
[1192.98 → 1196.20] First, understanding what they are and knowing how to reconcile them.
[1196.38 → 1196.56] Yeah.
[1196.56 → 1200.46] And because it's been such a long time, I think we have a lot of work to do.
[1200.82 → 1203.04] I mean, we're not even using Erlang releases.
[1203.66 → 1204.26] Ah, yes.
[1204.34 → 1205.44] Or Elixir releases.
[1205.44 → 1206.34] And that's a big one.
[1206.60 → 1210.54] We're still like, you know, slinging around Docker images, container images.
[1211.06 → 1213.46] Maybe there's a better way, and we don't know about it.
[1213.70 → 1217.22] But first it starts with the configs and the stuff which is generated.
[1217.66 → 1217.84] Yeah.
[1217.88 → 1223.66] One of the things I've done to help figure out what's changed is I'll generate a version of a
[1223.66 → 1229.18] Phoenix app and of like this older version of Phoenix that I'm migrating from and then
[1229.18 → 1232.82] generate a new one with the new one, the new version that I'm wanting to target.
[1232.82 → 1236.40] And then I'll like merge diff the whole directories.
[1236.66 → 1236.84] Okay.
[1237.12 → 1238.58] And just see what's the difference.
[1238.72 → 1241.36] And then I can manually make the adjustments.
[1241.68 → 1247.58] I do have a friend who created a tool that I can share with you that you can possibly put in the
[1247.58 → 1248.14] show notes.
[1248.26 → 1248.98] Yeah, that's a good idea.
[1249.12 → 1250.88] Because that only gets you so far.
[1250.88 → 1255.54] Because one of the things that you realize is when you generate your project, you generate
[1255.54 → 1256.90] it with other libraries.
[1256.90 → 1262.34] Like with Phoenix, there are some other libraries that you might use to generate your user authentication
[1262.34 → 1263.32] system.
[1263.60 → 1269.80] And that library is, it's not like devise in the Ruby community, which is a whole library
[1269.80 → 1272.44] that does a lot through kind of behavioural magic.
[1272.80 → 1277.74] But it generates this, like the one in the Phoenix world, it generates a bunch of files and
[1277.74 → 1279.02] lets you customize them.
[1279.02 → 1283.54] So the version of that needs to be updated as well and considered.
[1283.54 → 1292.16] So like the resource that I'm sharing is one where you can say, I'm going from this version
[1292.16 → 1295.24] of Phoenix to this new version.
[1295.24 → 1298.14] And here are the flags that were included.
[1298.54 → 1298.84] Okay.
[1299.02 → 1300.06] The generator diff.
[1300.20 → 1301.14] I'm looking at it now.
[1301.64 → 1301.90] Okay.
[1301.90 → 1304.12] We'll share a link in the show notes.
[1304.42 → 1305.20] That's a good one.
[1305.48 → 1309.62] So is this just for Phoenix or is this for other things as well?
[1309.82 → 1310.38] Just for Phoenix.
[1310.48 → 1310.70] Okay.
[1310.70 → 1312.54] This is specifically for Phoenix.
[1312.62 → 1316.98] And there are other tools that will do the same type of thing, but this one you can say,
[1317.08 → 1322.24] well, I know I did mine with binary IDs or I did mine with MySQL instead of Postgres.
[1322.78 → 1324.92] And all these different flags.
[1325.12 → 1329.68] So you can set those flags and see what does that look like for my old version to my new
[1329.68 → 1330.02] version.
[1330.02 → 1330.54] Okay.
[1330.54 → 1337.08] So while the config files and like these files, which get generated, that this tool is great.
[1337.58 → 1342.86] And I'm even thinking, as you mentioned, I can see myself generating a new Phoenix project
[1342.86 → 1348.02] with the version that I'm targeting and then diffing it, maybe specific directories, not everything
[1348.02 → 1352.32] with the version that I'm going from just to figure out, you know, what I need to change.
[1352.32 → 1359.02] But it's also the changes in how things get tested, built, but also deployed.
[1359.16 → 1360.72] I know there are Erlang releases.
[1361.32 → 1364.32] Do you call them Erlang releases or do you call them something else in the Elixir community?
[1364.66 → 1364.82] Yeah.
[1364.98 → 1369.46] We just call them releases that we are generating releases or building a release.
[1369.66 → 1369.92] Okay.
[1370.26 → 1371.68] So we don't use that.
[1372.00 → 1377.68] We just, you know, run the commands, the mix commands in the context of a container.
[1377.68 → 1378.92] We generate the image.
[1379.06 → 1380.76] I mean, I think, I think there's a Docker file.
[1380.94 → 1384.60] I think I forget exactly how this works, but you know, we just run those commands.
[1384.88 → 1389.74] We generate the container image, which is, you know, ready for production, bundle all like
[1389.74 → 1390.66] compile assets.
[1390.84 → 1392.46] We still use, is it Node.js?
[1392.70 → 1394.24] I think a yarn, something like that.
[1394.30 → 1396.36] Like there's like a yarn compilation.
[1396.92 → 1401.50] We, ES built, I think it's the new tool we talked about going to ES built, which we're
[1401.50 → 1402.12] still not using.
[1402.62 → 1407.50] So these are two examples of things that we would want to use, but are there others?
[1407.50 → 1411.86] Are there other, I know, better ways of doing this in the Elixir community that we don't
[1411.86 → 1412.36] know yet?
[1412.66 → 1415.02] Well, I think there's a lot of benefit to releases.
[1415.34 → 1417.32] You're already doing Docker, which is good.
[1417.58 → 1422.82] But like one of the problems I had previous experience is that we're just loading our source
[1422.82 → 1429.32] code into the Docker container and saying on startup, it was just, okay, mix compile on
[1429.32 → 1431.54] mix Phoenix server run kind of a thing.
[1431.54 → 1436.12] And depending on how large the project is going through the whole compilation process
[1436.12 → 1437.76] can take time.
[1437.88 → 1443.52] And it would cause our automation setup to say the container is not responsive.
[1443.52 → 1444.64] It must not be okay.
[1444.64 → 1446.02] It's not healthy, and I'm going to kill it.
[1446.36 → 1450.94] So the benefit of releases is you're shipping compiled code.
[1451.08 → 1455.96] It's a smaller, like you're the actual, you know, Docker layers that are getting pushed
[1455.96 → 1456.90] out are smaller.
[1456.90 → 1460.12] So that's faster, but it just starts up a lot faster.
[1460.56 → 1460.64] Okay.
[1460.88 → 1466.42] So would you still use Docker containers or container images with releases?
[1466.72 → 1467.06] I do.
[1467.22 → 1467.38] Yeah.
[1467.60 → 1467.92] Okay.
[1468.12 → 1468.40] Okay.
[1468.60 → 1474.66] Is there something, a resource in the Elixir community that you go to when it comes to running
[1474.66 → 1477.70] it in production using container images or something else?
[1477.78 → 1480.08] Is there such a resource that you know of or use?
[1480.08 → 1485.44] For running in production or for like the step before that is like building the release and
[1485.44 → 1488.12] getting the Docker container all set up?
[1488.22 → 1488.80] I think both.
[1489.02 → 1492.54] But the goal is to how do we deploy into production?
[1492.88 → 1498.78] And like, these are the steps and the releases is the current-recommended way of doing that.
[1498.92 → 1502.64] The end goal is how do I run my Elixir app in production?
[1502.64 → 1510.36] Well, the Phoenix documentation includes a little section on deployment where they have
[1510.36 → 1515.40] deploying to guides that are specific to a few different hosting providers, Heroku,
[1515.98 → 1522.16] Fly.io, Gig elixir, and just how to do releases in a generic sense, you know, not specific to
[1522.16 → 1522.74] any platform.
[1522.92 → 1525.36] That's, I think, a good place to start.
[1525.36 → 1530.80] Like to say, I want my deployment to be set up.
[1531.00 → 1534.40] And then separately, it's how do I get it into production?
[1534.40 → 1536.54] And how do I maintain it?
[1536.58 → 1537.56] How do I observe it?
[1537.64 → 1539.32] How do I manage it?
[1539.62 → 1539.78] Right.
[1539.92 → 1541.54] Is that kind of also what you're thinking?
[1541.96 → 1543.12] It is, of course.
[1543.22 → 1544.72] Like all those, like our follow-up concerns.
[1544.84 → 1550.40] The first one is how do I get it out there in a way that is efficient, in a way that,
[1550.46 → 1553.54] you know, I'm using the platform strengths, whatever the platform is.
[1553.54 → 1555.00] And that is a good one.
[1555.06 → 1557.82] So I will include you in the show notes and maybe go over it myself because I know it's
[1557.82 → 1558.52] changing a lot.
[1559.22 → 1563.32] And in my mind, like once you have container images, like the case is closed.
[1563.80 → 1566.20] We have container images, like we'll get them around.
[1566.42 → 1568.90] That is like the currency that we trade in.
[1569.04 → 1573.12] But I'm wondering if that is still true when it comes to platforms.
[1573.12 → 1577.98] Like is that still the best approach or the recommended approach when it comes to a platform
[1577.98 → 1582.56] now that we migrated from Kubernetes to Fly.io, to a PaaS?
[1582.56 → 1583.04] Yeah.
[1583.20 → 1589.18] So with Fly, we still do recommend with an Elixir app going through Docker and preferably
[1589.18 → 1590.02] even releases.
[1590.68 → 1592.58] Just I think that gives the best experience.
[1592.94 → 1599.36] And with the newer versions of Phoenix, like that's Phoenix 1.6.3 and later, it has a lot
[1599.36 → 1600.72] of that built into it.
[1601.18 → 1607.28] So what that means is I can, the Fly tooling, I can say, you know, Fly, I want to deploy my
[1607.28 → 1607.52] app.
[1607.52 → 1610.94] And it actually says, oh, I'm aware that this is a Phoenix app.
[1611.06 → 1613.92] I'm going to run some of these Phoenix commands that I know are there.
[1614.42 → 1619.10] And so it can run to generate releases and just do a lot of that config for you.
[1619.32 → 1621.52] So it helps get you there.
[1621.70 → 1623.66] But that's on the newer apps, right?
[1623.68 → 1625.88] So like that's kind of where this comes back to.
[1626.02 → 1631.98] Well, if I'm not, if I generated my app on an older version of Phoenix, all my config may
[1631.98 → 1632.78] not be the same.
[1632.82 → 1633.88] It might not look that way.
[1633.88 → 1634.36] Right.
[1634.66 → 1636.42] So it can't do all of that.
[1636.70 → 1638.68] So we do have some documentation on how to do it with Fly.
[1639.10 → 1640.96] That's the long form way.
[1641.14 → 1644.60] Like, hey, here's how you can do it on any version of Elixir that you or Phoenix that
[1644.60 → 1645.60] you're coming from.
[1645.98 → 1652.00] But yeah, at Fly, we still do recommend the Docker and releases just as a smooth process.
[1652.32 → 1652.50] Okay.
[1652.84 → 1654.90] So I already have my first two steps.
[1655.04 → 1656.72] The first one is reconciled the config.
[1657.02 → 1661.86] Make sure it's using the latest version so that we can use releases properly.
[1661.86 → 1668.00] And then use releases in the same context of container images, which will make them smaller
[1668.00 → 1669.68] and quicker to boot.
[1669.84 → 1672.36] That's the one thing which I found myself adjusting.
[1672.90 → 1677.74] And there wasn't the concept of a startup probe when I looked, which is something that we're
[1677.74 → 1682.58] using communities just to like not run the readiness probes or the liveness probes too
[1682.58 → 1684.90] early because the app is slower to boot.
[1684.90 → 1689.42] And there's actually something, and maybe you can tell me if this is a good idea or not.
[1689.50 → 1696.12] There's something that we do when we on boot, which in practice, it works really well because
[1696.12 → 1702.04] we not only trigger a database backup where we used to before we deploy the new version.
[1702.16 → 1707.38] So as the new version is coming up of the app, we run a database backup before we run migrations.
[1707.88 → 1713.00] So if there's anything in the migrations that messes it up, we can go, we have a backup ready
[1713.00 → 1713.66] to go back to.
[1713.88 → 1714.60] Do you do that?
[1714.90 → 1716.16] I mean, let's just stop here for now.
[1716.30 → 1719.14] Do you, did you ever find the need to do this?
[1719.48 → 1725.42] There's one company I've worked at where they would sometimes need to go back.
[1725.70 → 1728.98] I only remember one occasion where it's like, oh, I'd had to restore an older version of
[1728.98 → 1731.12] the database to recover something that had gone wrong.
[1731.74 → 1734.48] I typically don't do that.
[1734.48 → 1739.08] And the main reason is, is because some of the things that we've just learned over time,
[1739.08 → 1744.86] we learned it a lot in the Rails community with migrations and just what, what makes a safe
[1744.86 → 1745.52] migration.
[1746.20 → 1751.52] So I'm going to share a link to an article that we have on the Fly website, the blog,
[1751.64 → 1754.12] where we talk about safe Ecto migrations.
[1754.32 → 1759.90] Ecto is the database layer that's specific to Phoenix, but a lot of the same principles
[1759.90 → 1763.48] came from the Rails community and the lessons learned there.
[1763.90 → 1769.44] And really it's just about, well, I don't want to actually do data migrations when I'm
[1769.44 → 1772.44] doing my data structure migrations.
[1772.64 → 1777.36] So I might structure my tables, add a new field, change an index, something like that.
[1777.68 → 1782.00] And then there's the separate process of, you know, I really need to just fix some data
[1782.00 → 1785.98] that happened and how we can run those separately.
[1785.98 → 1790.34] So then when they're run separately, we can actually write unit tests around the code
[1790.34 → 1794.06] better and test that, yes, it's catching these different situations.
[1794.86 → 1801.56] But yeah, I do understand the concern and of being able to either test a migration on
[1801.56 → 1806.74] a test database before you actually run it on your production data, and then being able
[1806.74 → 1807.86] to restore back.
[1808.08 → 1808.38] I get it.
[1808.48 → 1812.08] Sometimes it's necessary, even with all the careful planning that we do.
[1812.32 → 1813.42] Sometimes you need that.
[1813.42 → 1813.86] Okay.
[1814.34 → 1819.80] So if you were to implement a database backups before running the migrations in the context
[1819.80 → 1821.56] of Fly, how would you do that?
[1821.86 → 1826.04] What is the way that, you know, with everything that you know, you would say, yes, this is
[1826.04 → 1826.20] good.
[1826.30 → 1829.24] This is how, this is what I think would work best.
[1829.48 → 1829.70] Okay.
[1829.72 → 1830.60] So pause.
[1831.48 → 1832.94] I don't actually know how to do that.
[1833.06 → 1833.32] Okay.
[1833.46 → 1838.42] Like what I mean is Fly's Postgres databases are not managed databases in the way that Heroku
[1838.42 → 1839.34] has managed databases.
[1839.34 → 1845.28] They're set up and configured for you, but they don't have like people who are observing
[1845.28 → 1849.42] them and taking proactive measures to, you know, oh, you're about to run out of disk space,
[1849.70 → 1851.16] you know, doesn't have that stuff.
[1851.50 → 1851.58] Okay.
[1852.10 → 1855.34] So I need to reconsider a few things if that's the case.
[1856.06 → 1858.86] It's like half managed, but not like fully managed.
[1859.02 → 1859.28] Okay.
[1859.52 → 1859.74] Right.
[1859.74 → 1865.16] Because like some things are done for you, but if you get things wrong, you know, it's
[1865.16 → 1866.74] up to you to fix it.
[1866.82 → 1867.72] Is that what you're telling me?
[1867.94 → 1868.20] Yes.
[1868.32 → 1874.34] And so they, there are automated nightly backups, and I believe that there is a way to trigger
[1874.34 → 1876.26] manually that you want a backup to run.
[1876.50 → 1877.68] I'm just not sure how to do that.
[1877.78 → 1877.96] Okay.
[1877.96 → 1878.86] I'd have to check the docs.
[1879.20 → 1879.42] Yep.
[1879.62 → 1879.90] Okay.
[1879.90 → 1882.54] I see this January 22nd, Postgres backups.
[1883.32 → 1887.94] Your best bet would be to install iron on a separate app or a VM you run elsewhere and
[1887.94 → 1889.90] have it do the PG dump for you.
[1890.14 → 1890.40] Okay.
[1890.60 → 1893.82] So that's something that we used to do on Kubernetes.
[1894.18 → 1899.56] We would use to run a Postgres stateful set, single instance, no replication.
[1899.94 → 1905.20] When we would use to back up every hour, the backup would be just a cron job that used to
[1905.20 → 1905.88] run cron job.
[1906.08 → 1906.20] No.
[1906.44 → 1907.48] What do they call them?
[1907.56 → 1909.08] I have got the naming already.
[1909.08 → 1910.90] Oh, the naming Kubernetes.
[1911.26 → 1911.46] Yeah.
[1911.50 → 1911.78] Yes.
[1911.98 → 1912.68] Scheduled jobs.
[1912.90 → 1913.40] That's the one.
[1913.50 → 1913.86] Thank you.
[1914.10 → 1914.46] Yes.
[1914.62 → 1914.82] Yes.
[1914.90 → 1915.12] Yes.
[1915.50 → 1920.56] So the scheduled job would run every hour or create a pod, you know, create a job, create
[1920.56 → 1921.78] a pod, run the backup.
[1921.94 → 1924.14] We just, it just used to run PG dump.
[1924.26 → 1925.32] Very, very simple.
[1925.72 → 1926.04] Did we?
[1926.18 → 1927.96] Yes, we did compress it.
[1928.00 → 1930.08] And then we just like stream it to AWS S3.
[1930.22 → 1931.22] Super, super simple.
[1931.70 → 1936.62] When the application, when a new instance would be deployed, we would have any containers that
[1936.62 → 1938.04] would run this, would run the backup.
[1938.04 → 1940.00] And I don't think they would run the migration.
[1940.14 → 1941.78] No, it would do a full backup.
[1942.32 → 1944.18] It would sync the assets to S3.
[1944.48 → 1948.10] We don't have that issue anymore because the assets are now stored on S3.
[1948.54 → 1949.98] So we don't do that.
[1950.02 → 1953.86] But we would run a DB backup part of the pod coming up.
[1953.86 → 1957.52] And then the application would start and a couple of extra things would happen before
[1957.52 → 1959.68] the Phoenix server run would happen.
[1960.20 → 1961.90] So that's, that's how that would work.
[1962.02 → 1968.02] So something equivalent, I think in Fly would be to, as Kurt mentions here in this community
[1968.02 → 1973.12] post, I'll share the link, is to run this scheduled job on a separate app.
[1973.12 → 1979.44] And then when the app would boot, maybe trigger this backup from the application instance, maybe.
[1979.72 → 1981.02] I can see that working for sure.
[1981.36 → 1987.36] So we talked about a few things, but I think we're just like getting warmed up because Fly
[1987.36 → 1993.34] changes a lot of things for us when it comes to single instance, multiple instance.
[1993.34 → 1999.04] And while we migrated to Fly, and we only run on Fly, the expectation is that we will run
[1999.04 → 2001.44] in multiple places.
[2001.72 → 2005.76] So Fly is one of the origins, as I refer to them from the perspective of the CDN.
[2005.82 → 2006.54] There is a CDN.
[2006.72 → 2011.30] But there are some discussions that we had before we start recording this, which make me rethink
[2011.30 → 2011.92] some of that.
[2012.08 → 2015.76] But the point still stands that we will have more than a single instance.
[2016.12 → 2022.26] So when we enabled multiple application instances, we've hit this issue that Jared talked about
[2022.26 → 2026.36] when it comes to ETS tables and the app instances not clustering.
[2026.76 → 2030.12] So first, why might we want to do that?
[2030.36 → 2032.96] Why might we want to cluster the application instances?
[2033.64 → 2038.06] And is there anything in the Fly platform that we can leverage?
[2038.72 → 2045.36] Well, clustering Elixir applications is something that's unique to the Beam, really, the Erlang
[2045.36 → 2046.04] virtual machine.
[2046.54 → 2052.18] And there's so many other platforms or languages and frameworks like Ruby.
[2052.26 → 2055.22] or node that just don't have a concept of this.
[2055.62 → 2059.04] So you tackle those problems differently.
[2059.16 → 2062.24] But when you're talking about Elixir, it's like, well, we have some extra tools in our
[2062.24 → 2062.66] toolbox.
[2063.10 → 2064.28] There are some more things we can do.
[2064.78 → 2069.26] And I think one of the reasons that we want to be able to cluster is because...
[2069.96 → 2074.54] So in Kubernetes, you could do cluster where the nodes could discover the other.
[2075.08 → 2080.36] An Elixir node in one pod could discover one running in another one through the lib cluster
[2080.36 → 2080.90] library.
[2080.90 → 2084.04] And you could do a Kubernetes way of the library.
[2084.04 → 2088.44] It would query the Kubernetes interface and query for where are the other nodes that I
[2088.44 → 2088.88] can talk to.
[2088.90 → 2090.48] And they could actually link up that way.
[2091.02 → 2095.90] Within Fly, there is a DNS way that the apps can query for each other.
[2095.90 → 2101.76] So one of the things that's interesting to know about Fly is in the background, internally,
[2101.76 → 2111.50] there's an IPv6 network that all of your applications are able to talk on and discover other applications
[2111.50 → 2113.60] running in that private network.
[2113.78 → 2118.04] And it's actually done through WireGuard, which is a great technology.
[2118.04 → 2125.82] And what that means is I have the ability for my apps to use lib cluster as well, the same
[2125.82 → 2129.88] library, to discover and link up to the other nodes.
[2130.10 → 2134.76] So that works great when my two apps are sitting side by side in the same data centre.
[2135.14 → 2140.76] And that also works when my app is in a new region somewhere else in the world.
[2140.76 → 2147.46] That IPv6 network still connects them privately, and they are able to connect up and sync.
[2147.78 → 2152.04] And that right there is like, I don't know how to do that.
[2152.28 → 2158.80] With AWS, even multi-region, getting my app to do that was something that was just beyond
[2158.80 → 2161.76] me and the people that I had access to.
[2162.44 → 2164.78] So it was just like, oh, we're just not going to go.
[2165.10 → 2167.00] Multi-data centre, that's too hard.
[2167.68 → 2169.62] So Fly actually made that simple.
[2169.62 → 2174.62] And that's one of the reasons I was very excited about trying to tell people in the
[2174.62 → 2176.16] Elixir community about Fly.
[2176.32 → 2177.92] And that's why I took the job at Fly.
[2178.28 → 2179.62] It's like, no, this is really cool.
[2179.84 → 2184.48] This is like magic that we can do things with Elixir now that other people can't do.
[2199.62 → 2203.82] This episode is brought to you by our friends at Source graph.
[2203.90 → 2206.46] They recently launched a new feature called Code Insights.
[2206.78 → 2209.76] Now you can track what really matters to you and your team in your code base.
[2209.92 → 2214.02] Transform your code into a durable database to create customizable visual dashboards in
[2214.02 → 2214.40] seconds.
[2214.88 → 2217.74] Here's how engineering teams are using Code Insights.
[2218.00 → 2221.98] They can track migrations, adoption, and deprecation across the code base.
[2221.98 → 2225.48] They can detect and track versions of languages or packages.
[2226.02 → 2229.28] They can ensure the removal of security vulnerabilities like Log4j.
[2229.56 → 2234.82] They can understand code by team, track code smells and health, and visualize configurations
[2234.82 → 2235.84] and services.
[2236.42 → 2238.98] Here's what the engineering manager at Prezi has to say about this new feature.
[2238.98 → 2244.60] As we've grown, so has a need to better track and communicate our progress and our goals
[2244.60 → 2246.92] across the engineering team and the broader company.
[2247.30 → 2252.04] With Code Insights, our data and migration tracking is accurate across our entire code
[2252.04 → 2257.64] base and our engineers and our managers can shift out of manual spreadsheets and spend
[2257.64 → 2259.32] more time working on code.
[2259.70 → 2260.06] End quote.
[2260.42 → 2264.34] The next step is to see how other teams are using this awesome feature.
[2264.34 → 2269.48] Head to about.sourcegraph.com slash code dash insights.
[2269.74 → 2271.22] This link will be in the show notes.
[2271.34 → 2276.06] Again, about.sourcegraph.com slash code dash insights.
[2276.30 → 2278.20] And by our friends at Retool.
[2278.56 → 2284.08] Retool helps teams focus on product development and customer value, not building and maintaining
[2284.08 → 2285.14] internal tools.
[2285.54 → 2288.38] It's a low-code platform built specifically for developers.
[2288.76 → 2294.26] No more UI libraries, no more hacking together data sources, and no more worrying about access
[2294.26 → 2294.76] controls.
[2295.26 → 2299.58] Start shipping internal apps to move your business forward in minutes with basically zero
[2299.58 → 2303.26] uptime, reliability, or maintenance burden on your team.
[2303.56 → 2305.34] Some of the best teams out there trust Retool.
[2305.46 → 2312.62] Bred, Coinbase, Plaid, DoorDash, Legal Genius, Amazon, All birds, Peloton, and so many more.
[2313.02 → 2317.70] The developers at these teams trust Retool as their platform to build their internal tools,
[2317.86 → 2319.14] and that means you can too.
[2319.14 → 2322.50] It's free to try, so head to retool.com slash changelog.
[2322.62 → 2326.22] Again, retool.com slash changelog.
[2332.14 → 2342.92] So I know a thing or two about Erlang clustering, its strengths, its weaknesses.
[2342.92 → 2349.28] We will not go there because it is a rabbit hole in multiple ways, but I'm really curious
[2349.28 → 2355.98] about running multiple nodes of the application distributed across the whole world by simply
[2355.98 → 2356.82] scaling the app.
[2356.94 → 2358.02] That sounds super simple.
[2358.38 → 2361.00] Now, I know there's a lot of stuff that needs to happen in the background.
[2361.26 → 2365.72] We're not going to look into networking, the whole VPN, the wire guard.
[2365.92 → 2367.04] I'm amazed by it.
[2367.04 → 2371.10] I think it's just like what it enables, especially when you run Fly CTL locally.
[2371.48 → 2372.32] I think it's really cool.
[2372.70 → 2375.06] Database backups connecting to like private instances.
[2375.26 → 2376.08] It's really, really cool.
[2376.46 → 2382.02] But I'm really curious about running multiple instances of the same app and what it means
[2382.02 → 2383.66] for pushing out updates.
[2384.18 → 2385.62] How does that work behind the scenes?
[2385.66 → 2391.10] Like, how do I get my update, my application update out there when you have maybe 10 instances
[2391.10 → 2394.12] running, when there's a database migration involved?
[2394.12 → 2395.72] How does that work in practice?
[2395.94 → 2400.30] Like, that sounds, I won't say like a recipe for disaster, but you need to be a bit more
[2400.30 → 2406.22] careful with what migrations you're running when the new version may affect the existing
[2406.22 → 2407.06] running versions.
[2407.54 → 2407.82] Yes.
[2408.04 → 2411.92] So the resource I shared earlier is about safe ecto migrations.
[2412.16 → 2417.36] And that is one of those things that you just have to be aware of when you're in any large
[2417.36 → 2422.00] environment where you have many different nodes, like even if they're not clustered, right?
[2422.00 → 2425.88] I've got a bunch of servers, and they're going to be running different versions of my app
[2425.88 → 2429.12] at any given moment as a deployment is rolling out.
[2429.52 → 2430.82] And my database changes.
[2431.60 → 2432.34] What does that mean?
[2432.86 → 2437.68] So there are strategies we have to take for how do I make a change to my database that I want
[2437.68 → 2441.78] without breaking an older version of my app that's reading from it?
[2442.32 → 2442.44] Right.
[2442.44 → 2447.66] And that's just a generic situation that we have to deal with when we're wanting to provide
[2447.66 → 2453.18] non-interrupted service or like that the user's not going to all of a sudden get hit in error.
[2453.50 → 2454.54] Their query failed.
[2454.94 → 2457.82] So there are strategies for doing that.
[2458.04 → 2463.48] And like sometimes that's a multi-stage deploy where you might go halfway to the migration,
[2463.96 → 2468.30] to the full change that you want in one deploy, and then follow it up afterward with the second
[2468.30 → 2469.56] deploy that finishes it.
[2469.56 → 2471.62] And like there are strategies for that.
[2471.78 → 2477.28] But to answer your question, the way Fly does it is it's a rolling deploy where a new one
[2477.28 → 2482.68] will go out, and it has to, health checks have to pass before it's considered, okay, it's
[2482.68 → 2483.22] up and good.
[2483.80 → 2488.06] And then it will roll out to the all the other instances.
[2488.72 → 2493.90] And there's a special instance that's run very first that runs the migrations.
[2493.90 → 2495.88] It doesn't actually run the app.
[2496.26 → 2499.20] It runs, it starts it up just enough to run the migrations.
[2499.56 → 2501.06] Not to actually run the full instance.
[2501.06 → 2502.82] So it says, okay, can we run the migrations?
[2502.98 → 2504.06] Because we're only going to run them once.
[2504.18 → 2508.36] We don't, we don't need to run them every app having, say, I'm going to run the migrations
[2508.36 → 2512.72] now and trying to do that and discovering, oh, it's already been done or, you know, having
[2512.72 → 2515.40] to deal with any kind of locks or queries or anything like that.
[2515.78 → 2515.90] Interesting.
[2516.08 → 2521.02] So you have one instance that's going to run on the primary database, assuming you might
[2521.02 → 2521.94] have read replicas.
[2521.94 → 2527.78] And then once that's good, then you have the instances that roll out one at a time.
[2528.48 → 2528.52] Okay.
[2528.58 → 2534.28] So you do have that situation where your app is going to be in multiple states where your
[2534.28 → 2538.24] database is in your application that doesn't know anything about these database changes.
[2538.24 → 2542.16] It's the older version where it needs to at least not break.
[2542.42 → 2542.68] Okay.
[2542.70 → 2543.60] So that's interesting.
[2543.60 → 2550.84] So if we run the migrations explicitly on container startup, how is that going to work
[2550.84 → 2551.64] with a primary?
[2551.98 → 2558.22] I mean, will every single app instance coming up still run the same migrations and realize,
[2558.40 → 2559.52] oh, this has already run?
[2559.88 → 2561.24] Is that how that's going to work?
[2561.66 → 2565.14] Well, actually we recommend not running them on container startup.
[2565.50 → 2565.62] Really?
[2565.98 → 2566.44] Yes.
[2566.62 → 2571.86] So when you create a fly app, it generates a fly.TOML file, T-O-M-L.
[2571.86 → 2575.84] And in there, there is a little section called deploy.
[2576.36 → 2581.10] And you say, this is my release command, and this is what runs my migrations.
[2581.44 → 2586.76] And so the tooling looks for that and says, I'm going to run that special in a little container.
[2587.12 → 2589.94] Make sure that that's how my database migrations are run.
[2590.44 → 2590.68] I see.
[2590.78 → 2590.94] Okay.
[2590.98 → 2592.56] So that's another one for my checklist.
[2593.08 → 2598.72] Remove the database migrations from the container startup and use the fly tooling to do it for me.
[2599.22 → 2599.62] Interesting.
[2599.62 → 2604.98] Or maybe at least have some way of detecting, oh, I'm running in fly, this container image.
[2605.34 → 2606.58] Don't run this command.
[2607.14 → 2609.42] Fly is going to handle it via the configuration.
[2609.74 → 2610.66] That makes sense.
[2610.96 → 2616.40] Well, honestly, it's probably not going to break anything if you still have it in your database
[2616.40 → 2623.58] or in your Docker container, just because database locks are already something that the migrations do.
[2623.58 → 2630.38] So you can't get into a contention where they're trying to make competing migrations at the same time.
[2630.62 → 2636.06] And I think if a migration has already run, if it's running, if the same migration tries to run from a different container,
[2636.06 → 2640.70] it's the same thing as trying to apply the migrations again, but they've already been applied.
[2640.70 → 2642.12] So I think there's like a version.
[2642.56 → 2649.38] I don't know exactly how it works in Elixir, but I assume from what I used to know from my Ruby on Rails days.
[2649.88 → 2650.10] Okay.
[2650.42 → 2653.20] So just like it's like a knob says, oh, yep, I've already applied this.
[2653.26 → 2654.36] There's nothing for me to do.
[2654.52 → 2656.24] So it's like an idempotent operation.
[2656.50 → 2657.68] Just move on.
[2657.68 → 2660.18] So maybe there's nothing to do there.
[2660.38 → 2667.08] Maybe when it comes to sharing the cache, and I think this is something that you mentioned as well,
[2667.24 → 2671.50] the ETS tables, where we store, where we cache the website content.
[2671.96 → 2675.14] So I'm wondering whether we have to do that at all.
[2675.24 → 2678.36] And there's like live view, there's like multiple things coming together here.
[2678.42 → 2682.70] But when it comes to sharing the cache between the application instances,
[2682.70 → 2687.56] now that we have multiple ones, what is the recommended way in Fly?
[2687.86 → 2693.54] So I'm not sure how much of this you covered for your listeners, but just for you, dear listener,
[2693.68 → 2695.26] who might be like, what is ETS?
[2695.52 → 2697.86] So ETS is an Erlang term storage.
[2698.12 → 2705.62] It is an in-memory cache that's very fast, but it's specific to Elixir, Erlang, and the Beam languages.
[2706.42 → 2710.94] And so, yeah, you can store anything in ETS, which is really handy because it doesn't have to go through
[2710.94 → 2712.70] some other external serialization.
[2713.24 → 2714.56] It's like a binary format.
[2714.56 → 2719.76] But the problem that we're talking about here is that, yeah, you only have, it's in-memory on that instance.
[2720.06 → 2725.82] So when you add now a second instance in the same data centre, even, they both have their own copy of that cache.
[2726.22 → 2731.30] And I think the problem that you guys were describing was a situation where you release a new episode,
[2731.30 → 2736.94] and the instance that I'm connecting to when I release that episode invalidates the cache.
[2736.94 → 2742.16] Everything goes great on that instance, but my visitor who comes to the other instance,
[2742.70 → 2745.54] that cache is still the old value, and it doesn't show up.
[2745.94 → 2746.30] Is that right?
[2746.72 → 2747.34] Yes, that's right.
[2747.70 → 2748.98] That's exactly what happened now.
[2749.30 → 2752.30] A lot of this stuff happened between episode 50 and 51.
[2752.80 → 2756.76] And while you're tuning into episode 51, which follows exactly episode 50,
[2756.82 → 2760.66] where we talk about the fly migration, there's a lot of stuff that happened in between.
[2760.66 → 2770.88] And exactly as Mark points out, we have the issue where a cache from one instance was different from the cache of another application instance,
[2771.10 → 2776.54] which means that sometimes the episode would be there on one request, and another request the episode would not be there.
[2776.82 → 2778.78] And we have multiple layers of caching.
[2779.16 → 2781.42] So first, we have a cache in the CDN.
[2782.12 → 2785.70] Then we have a cache on the application instance.
[2785.70 → 2789.44] And I don't think the fly proxy does anything caching-wise.
[2789.58 → 2791.56] It just like passes through all the requests.
[2791.82 → 2799.72] But we have two layers of caching, the CDN and the ETS cache, which is specific and local to every application instance.
[2799.90 → 2802.38] And you have multiple, well, you may have different caches.
[2802.82 → 2805.52] No, you will have different caches if you don't cluster.
[2806.24 → 2813.54] So when you cluster those applications, what happens with the ETS caches, which are application instance specific?
[2813.54 → 2823.40] So when you cluster the application, and you have now these two instances that are clustered, ETS is still unique and individual to those running instances.
[2823.62 → 2826.20] It doesn't automatically become a shared cache.
[2826.58 → 2832.48] There is a thing called GETS, which is distributed ETS, but that has a lot of other complexity.
[2832.48 → 2852.12] So honestly, just thinking about this situation you guys were describing, like what I think is the smoothest way that also gives you the opportunity to have new features that you could add to your application is when you have clustering, Phoenix has the ability to do Pub Sub built into it.
[2852.22 → 2854.22] So Pub Sub being published and subscribe.
[2854.22 → 2861.22] So what you can do is when the apps cluster to each other, they can just, you have the ability to notify.
[2861.44 → 2866.50] Like when one instance receives new episode, that's an important message.
[2866.58 → 2869.04] That's when you care about other instances knowing about.
[2869.32 → 2878.78] So you can publish that message out, and they all subscribe to that, and they can say, oh, now I know I can just either update my cache or I can invalidate the whole cache and just let it get rebuilt.
[2879.18 → 2880.28] You know, whatever makes the most sense.
[2880.28 → 2886.74] But then if you have that publish and subscribe ability, then you can do fun things when you have live view.
[2886.82 → 2893.60] So live view being it's a WebSocket connection to the browser where the user is actually getting live updates.
[2893.68 → 2895.26] They can actually push to the user.
[2895.44 → 2908.60] So say you have a live view page that shows as people are listening to and playing a current episode, you could actually have a little notification like pop up in the corner that says new episode was just released.
[2908.60 → 2909.66] Be the first to hear it.
[2909.66 → 2912.18] And they could just get that real time.
[2912.38 → 2914.98] So you can start doing fun things like that.
[2915.08 → 2916.90] And Pub Sub makes that really easy.
[2917.12 → 2917.22] Yeah.
[2917.66 → 2922.38] I was looking at the Lifeboats app that Chris was blogging about.
[2922.38 → 2924.58] And I thought that was really cool.
[2925.12 → 2934.24] And I liked that it had like the same element or like the same area of MP3s, audio, listening with multiple people like to the same tracks.
[2934.24 → 2938.12] And we all listen to the same, same track, same audio file.
[2938.46 → 2939.86] I thought that was really cool.
[2939.86 → 2947.48] And I think there's a lot that the changelog.com application can do and can learn from the Lifeboats app.
[2947.68 → 2949.36] How involved were you with that, Mark?
[2949.98 → 2951.08] Did you contribute to that?
[2951.56 → 2953.52] Or did you think, wow, this is amazing?
[2953.72 → 2955.70] I did not directly commit code to that.
[2955.90 → 2960.12] I was involved with some of the discussion and just early versions of it.
[2960.12 → 2963.44] And I got access to the repo and was digging around it.
[2963.50 → 2964.46] It's like, how did Chris do that?
[2964.52 → 2965.46] Oh, that's really cool.
[2965.56 → 2967.66] Let me copy that idea from something else I'm working on.
[2968.10 → 2982.04] That's really what part of the goal with this app is, is it's to be an example of this is a good way to build a Phoenix application that solves some of these, like tackle some of these larger problems.
[2982.04 → 2997.00] Like, you know, people always assumed in order to do anything like a Spotify interface where I can continually navigate around while I have music playing and go to different pages, then I have to have like a single page app with a whole JavaScript front end.
[2997.60 → 3003.94] And what the Lifeboats app is showing is actually, no, you don't have to have any front end big JavaScript app.
[3004.12 → 3006.60] It can all be server rendered, and you can still have that ability.
[3007.06 → 3009.52] And so it's really intended to be an example app.
[3009.52 → 3013.90] So I encourage you and anyone else who's wanting to dig into something like that to check it out.
[3014.16 → 3015.10] I think that's really cool.
[3015.38 → 3024.54] And I think Jared, if he's not already all over it, I think he will be very soon because there's a lot to learn and a lot that we can do better for the changelog.com app.
[3024.86 → 3033.26] And because we are already on fly, and we can leverage all these things like the platform itself, some of the primitives that the platform provides.
[3033.26 → 3041.72] The amazing Elixir friendliness and the thinking that goes into connecting your application, your runtime to the platform.
[3042.02 → 3045.66] I think there's a lot there that I'm pretty sure we haven't dug into fully.
[3046.14 → 3049.58] Like Fly Postgres, you mentioned that package.
[3049.98 → 3052.82] Do you call it a package or do you call it like an Elixir dependency?
[3053.18 → 3054.76] It's a hex package.
[3054.90 → 3055.48] A hex package.
[3055.72 → 3055.84] Okay.
[3056.10 → 3056.34] Yeah.
[3056.34 → 3057.48] Yeah, on hex PM.
[3057.82 → 3058.66] So that's a good one.
[3058.94 → 3068.34] How it optimizes the connection to the database, read replicas versus write replicas or like the write master, whatever the case is.
[3068.50 → 3075.58] I haven't looked into all the details, but there's a lot of interesting stuff on fly that we can do with Elixir releases.
[3075.58 → 3079.08] And I'm wondering, do we even need a CDN?
[3079.48 → 3089.36] I know it's a crazy idea, but if we configure all these things correctly, and if we have our application distributed across all the fly regions, I mean, it sounds a bit crazy.
[3089.36 → 3091.84] But if we did that, would we even need a CDN?
[3092.26 → 3094.94] Now, that is a very interesting proposition for sure.
[3095.60 → 3098.08] And Live View, an amazing technology.
[3098.40 → 3101.66] I'm sure we will come back to this in the not too distant future.
[3101.66 → 3109.60] But a thing which I would like to talk about now, Mark, is about Thinking Elixir, your podcast that you've been running for a few years now.
[3110.00 → 3110.50] Is that right?
[3110.74 → 3111.84] Yeah, it's been over a year.
[3112.22 → 3113.88] We're 96 episodes.
[3114.04 → 3114.78] It's a weekly show.
[3114.98 → 3115.06] Yeah.
[3115.32 → 3115.50] Yeah.
[3115.54 → 3118.58] So I would say almost two years, 52 with some breaks.
[3118.70 → 3120.80] So like when you have 100, you're close to two years.
[3121.00 → 3121.26] Okay.
[3121.72 → 3126.34] Is there an episode that you recommend me listen to?
[3126.64 → 3129.96] And don't say the future one with Jared that you're going to record.
[3129.96 → 3131.44] I'll definitely listen to that one.
[3131.66 → 3132.30] Okay.
[3134.58 → 3137.30] No, actually, there's one of them that was a recent one.
[3137.50 → 3138.48] There's a couple, actually.
[3138.58 → 3139.12] They were recent.
[3139.56 → 3142.74] They're the things that changed my thinking.
[3143.62 → 3145.76] And one of them was episode 93.
[3145.88 → 3146.96] So this was not that long ago.
[3147.06 → 3148.08] It was April 5th.
[3148.68 → 3152.32] And it was Preventing Service Abuse with Michael Lucas.
[3153.00 → 3154.06] And it's just that idea.
[3154.06 → 3162.74] So he's coming at it from a security-focused perspective and wanting to say that and thinking
[3162.74 → 3163.56] about security.
[3163.70 → 3166.06] But not like, oh, I'm trying to prevent cross-site scripting.
[3166.16 → 3166.64] It's not that.
[3166.64 → 3171.76] It's more about people are going to try and abuse my website by having me accidentally
[3171.76 → 3174.32] send out spam or unintentionally.
[3174.46 → 3175.86] Like I'm not trying to enable that.
[3175.90 → 3180.78] But they're able to abuse my site to send out spam because maybe I offer invites that
[3180.78 → 3181.78] someone can invite someone.
[3181.78 → 3188.76] So I learned about some different techniques and Plug being a part of the Elixir Phoenix
[3188.76 → 3191.08] framework for handling requests.
[3191.42 → 3195.22] Some tooling that's built in to Plug so we can do those kinds of things.
[3195.28 → 3200.82] We can say, I'm going to use ETS tables and do rate limiting so you can't just keep brute
[3200.82 → 3203.16] forcing password attempts and things like that.
[3203.70 → 3206.34] So I think that's really important sometimes.
[3206.34 → 3212.20] And when we're in the smaller stage, either personal projects or small companies, we sometimes
[3212.20 → 3217.18] maybe have our services abused just because we're not even aware of those.
[3217.28 → 3221.74] And that was like one of those like, yes, I need to dig in deeper on that and start applying
[3221.74 → 3222.00] that.
[3222.56 → 3222.60] Okay.
[3222.64 → 3223.44] So that's a good one.
[3223.54 → 3229.90] Episode 93 on my list plus a hundred and something I'm thinking with Jared talking about
[3229.90 → 3231.30] change log on fly.
[3231.46 → 3232.28] That's what I'm thinking.
[3232.38 → 3232.60] Okay.
[3232.92 → 3233.70] I love that idea.
[3233.90 → 3234.18] Perfect.
[3234.18 → 3239.06] As we are preparing to wrap this up, I'm wondering what is the key takeaway that you
[3239.06 → 3243.10] would like our listeners to remain with from our conversation?
[3243.28 → 3247.22] There's a lot of fun stuff we didn't really get to, but I just think some of the
[3247.22 → 3247.98] things are fascinating.
[3248.10 → 3253.96] You mentioned it like the Fly Postgres library where we're having to think about we have a
[3253.96 → 3259.60] distributed app because I think what Fly really enables is the ability to have a globally
[3259.60 → 3260.40] distributed app.
[3260.50 → 3263.06] You tease this idea about a CDN, right?
[3263.06 → 3269.56] But if I'm actually able to, like the whole point of a CDN is to get the serving up of
[3269.56 → 3274.54] assets closer to my users so that it reduces the time and makes it a better experience.
[3274.88 → 3279.82] Now with Flymen actually makes it easier to run my whole server closer to the users.
[3279.82 → 3285.74] And if I can have my app distributed widely enough, that's, and I know where my audience
[3285.74 → 3291.56] is, then yeah, you kind of start to question, do I need that whole extra layer of my CDN?
[3291.92 → 3295.20] Because those assets are served by my app anyway.
[3295.34 → 3299.52] And if my app is already there, maybe I don't actually need a CDN.
[3299.60 → 3301.16] It really depends on what you're doing with the CDN.
[3301.16 → 3308.20] But I think that the takeaway I want people to come away with is that, wow, Fly is actually
[3308.20 → 3312.26] something that lets you do something that you couldn't easily do before.
[3312.76 → 3317.10] And especially if you're an Elixir, because obviously, you know, I run the Thinking Elixir
[3317.10 → 3317.60] podcast.
[3318.38 → 3319.80] Elixir is like what I love.
[3320.10 → 3321.60] It's the language that I love.
[3321.62 → 3323.26] And I love talking about it.
[3323.26 → 3328.04] And I want people to be able to come experience the things that you and I are experiencing,
[3328.20 → 3332.56] like, hey, functional programming, that solves a bunch of problems of state management,
[3332.70 → 3334.96] that object-oriented stuff that just causes problems.
[3335.56 → 3339.72] How many numerous bugs that we dealt with that are just state management like that?
[3340.20 → 3344.80] Anyway, I just hope people are willing to try Flout, even if it's not Elixir, you know,
[3345.04 → 3347.08] just whatever language you're working in.
[3347.56 → 3350.34] If you can put it in Docker, you can run it on Fly.
[3350.34 → 3356.90] And there's lots of tooling that we have to make going multi-region even easier, be it
[3356.90 → 3359.54] Rails or Node or Django or Java.
[3359.80 → 3366.60] You know, there are ways to start to take that multi-region and do things you couldn't do before.
[3367.34 → 3373.06] I really like that, especially since I have an appreciation, a special appreciation for
[3373.06 → 3377.28] Erlang, the Beam VM, which precedes Elixir, which precedes Changelog.
[3377.58 → 3378.74] I've seen its value.
[3378.74 → 3379.94] I've seen its potential.
[3380.34 → 3381.88] I've seen its abuse.
[3382.30 → 3384.92] And I've seen how well it handles all of it.
[3385.48 → 3390.62] And I'm surprised just by how resilient the system is, Erlang specifically.
[3391.04 → 3391.78] I really like it.
[3392.04 → 3392.96] I think there's a lot there.
[3393.12 → 3399.42] And I think that Kubernetes was taking us on a path that has a lot of advantages.
[3399.42 → 3406.16] But it also forgot some of the things that run times like Erlang just do so easily.
[3406.16 → 3410.90] The clustering part, the hot code reloading, the supervision trees.
[3410.90 → 3416.72] It's almost like you're running a very complex Kubernetes system inside Kubernetes when you
[3416.72 → 3419.42] run Elixir and Erlang and you don't even realize it.
[3419.42 → 3421.34] And microservices as well.
[3421.76 → 3425.94] Erlang has been doing it for decades before, you know, microservices were a thing.
[3426.00 → 3427.02] So there's like a lot there.
[3427.02 → 3430.16] And I really like, and I appreciate it from that ecosystem.
[3430.16 → 3430.26] Awesome.
[3430.90 → 3432.74] Mark, it's been a pleasure talking to you.
[3432.84 → 3434.38] Thank you very much for joining me on Ship It.
[3434.50 → 3435.84] I'm looking forward to next time.
[3436.02 → 3436.34] Thank you.
[3436.62 → 3436.98] My pleasure.
[3436.98 → 3466.96] Thank you.
[3466.98 → 3469.12] That's it for this week.
[3469.52 → 3470.30] See you all next week.
[3470.86 → 3476.44] As for my last thing, we will start the Rubicon EU episode series next week.
[3476.66 → 3479.04] If you want to be part of it, reach out.

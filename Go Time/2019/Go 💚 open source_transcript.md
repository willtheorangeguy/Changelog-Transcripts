[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.22 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to linode.com slash Changelog.
[15.52 --> 18.24]  This episode is brought to you by DigitalOcean.
[18.56 --> 23.08]  DigitalOcean makes it super simple to launch a Kubernetes cluster in minutes.
[23.08 --> 27.28]  The DigitalOcean Kubernetes platform empowers developers to launch their containerized
[27.28 --> 33.06]  applications into a managed production-ready cluster without having to maintain or configure
[33.06 --> 34.38]  the underlying infrastructure.
[34.80 --> 38.98]  They seamlessly integrate everything with the rest of the DigitalOcean stack, including
[38.98 --> 43.90]  load balancers, firewalls, object storage spaces, and block storage volumes.
[44.42 --> 49.10]  They even have built-in support for public and private image registries like Docker Hub
[49.10 --> 50.16]  and Quay.io.
[50.50 --> 55.20]  Developers can now run and scale container-based workloads with ease with the DigitalOcean platform.
[55.20 --> 59.68]  Learn more and get started for free with a $50 credit at do.co slash Changelog.
[59.80 --> 62.98]  Again, do.co slash Changelog.
[77.98 --> 83.36]  Welcome to GoTime, a podcast featuring a diverse panel and special guests discussing cloud
[83.36 --> 87.72]  infrastructure, distributed systems, microservices, Kubernetes, Docker.
[88.16 --> 89.24]  Oh, and also Go.
[89.46 --> 93.04]  We record live every Tuesday at 3 p.m. Eastern, noon Pacific.
[93.48 --> 97.54]  Join the community of Slack with us in real time during the show in the GoTime FM channel
[97.54 --> 98.42]  and go for Slack.
[98.64 --> 99.30]  Follow us on Twitter.
[99.40 --> 100.68]  We're at GoTimeFM.
[100.96 --> 106.20]  Listen live at changelog.com slash live or subscribe at changelog.com slash GoTime.
[106.48 --> 107.62]  And now on to the show.
[107.62 --> 115.84]  Welcome, everybody, to our GoTime podcast on May the 28th of 2019.
[116.48 --> 117.62]  I am Mark Bates.
[117.66 --> 119.70]  We've got a couple of great guests with us today.
[119.80 --> 124.76]  As always, the wonderful, fantastic, and exuberant Johnny Borsico.
[124.98 --> 125.58]  How are you doing, Matt?
[125.66 --> 126.38]  I am doing well.
[126.44 --> 126.80]  How are you?
[127.10 --> 127.62]  All right.
[127.66 --> 128.12]  All right.
[128.14 --> 129.88]  I like to give everybody a big welcome here.
[129.94 --> 133.80]  I'm trying to be like Matt, but polite if we can.
[133.80 --> 136.34]  So that's a tall order for me, too.
[136.48 --> 138.16]  So it's polite, Mark.
[138.22 --> 139.50]  You're going to get the best you're going to get.
[139.88 --> 145.20]  And of course, the wonderful, the talented, and the even better than Johnny, Carmen Ando.
[145.24 --> 146.06]  How are you doing, Carmen?
[147.56 --> 148.00]  Hello.
[148.76 --> 152.02]  And apparently it's somebody's birthday today, isn't it, Carmen?
[152.44 --> 153.72]  It is.
[154.20 --> 157.44]  And Johnny wanted to sing happy birthday to you, didn't you, Johnny?
[157.44 --> 157.84]  Oh.
[158.84 --> 159.36]  Wow.
[159.58 --> 162.10]  That was out of left field, but okay, sure.
[163.80 --> 164.36]  Yeah, that was it.
[165.26 --> 166.32]  It was perfect.
[166.68 --> 166.96]  Wow.
[167.06 --> 167.72]  What a delivery.
[168.10 --> 168.12]  Please.
[168.16 --> 168.40]  Okay.
[168.50 --> 172.32]  Well, we might have to cancel this episode early if no one's going to participate in the fun.
[172.42 --> 172.62]  Aw.
[173.46 --> 174.36]  Anyway, welcome.
[174.90 --> 175.84]  I'm very excited.
[176.10 --> 179.30]  So Matt couldn't be here today with us.
[179.60 --> 185.90]  I think he's off with all the GopherCon EU peeps doing GopherCon EU funness in the Canary Islands.
[186.38 --> 189.28]  So he entrusted me to guide the ship.
[189.28 --> 192.36]  We're going to talk about open source this week.
[192.36 --> 198.76]  So I think it's going to be kind of an interesting show because I know, Johnny, you don't contribute a lot to open source, correct?
[199.24 --> 201.10]  No, not through code.
[201.56 --> 203.14]  But that's definitely something we can get into.
[203.24 --> 207.42]  There are lots of ways to contribute to a community, but definitely not a whole lot of code.
[208.18 --> 209.14]  Yeah, that's what I thought.
[209.14 --> 216.68]  And so we're going to – I'm really curious to your opinions as a primarily of a user's perspective, if that makes any sense at all.
[216.80 --> 219.40]  Like, you know, somebody who just uses open source.
[219.64 --> 220.68]  So we're going to talk about that.
[220.80 --> 225.22]  And, of course, Carmen, you work for a small startup these days, don't you?
[225.22 --> 225.62]  Sure.
[228.42 --> 228.66]  Sure.
[229.00 --> 231.80]  If that startup is named Golang.
[232.96 --> 233.40]  Golang?
[233.96 --> 234.36]  Yeah.
[234.64 --> 238.24]  So I used to work for Travis DI, which is an open source company.
[238.24 --> 243.02]  And I contributed pretty much exclusively both in code and non-code at Travis.
[243.24 --> 244.22]  But now I'm at Google.
[244.86 --> 247.40]  And I do open source for Google.
[247.40 --> 247.88]  Okay.
[248.36 --> 257.74]  So obviously we're going to talk about that in a little bit because I think there's something we definitely want to talk about around Google and obviously Go as an open source project.
[258.30 --> 262.30]  But let's talk a little bit about some of the work you did at Travis.
[262.42 --> 264.74]  What was your primary, like, open source role there?
[264.80 --> 266.52]  What was the stuff you're working on that was open source?
[266.90 --> 275.80]  So we were on the build infrastructure side and we were trying to automate pipelines for golden image mastery on VMs.
[275.80 --> 285.18]  Meaning, you know, you wanted to test your code and you have certain language runtimes or add-ons or operating systems.
[285.44 --> 293.26]  And once that was parsed, it was going to give you back an image that already has this stuff on it as part of your build.
[293.34 --> 296.40]  And we wanted to write code that automated that.
[296.40 --> 307.00]  And the other part was the worker, which was kind of the person, the thing that would run the automation workload for the jobs once they started.
[307.12 --> 308.08]  And that was written in Go.
[308.86 --> 319.58]  And so I did all of the, I did a lot of code and also a lot of, like, issue gardening and a lot of community gardening in the repos that I was responsible for.
[319.58 --> 323.38]  So I asked you that question because I knew what Travis does.
[323.46 --> 324.66]  Know what Travis does.
[324.72 --> 326.08]  They still technically do what they do.
[326.70 --> 327.86]  I knew you worked there.
[328.22 --> 336.16]  But what I think is an interesting perspective I definitely want to touch on in a little bit is the fact that that's a company that was based and is an open source company.
[336.56 --> 339.04]  Its primary model was through open source.
[339.22 --> 340.46]  So I think that's pretty interesting.
[340.52 --> 341.24]  But I want to back up.
[341.32 --> 344.62]  And, Johnny, I want to ask you, what is open source to you?
[344.86 --> 346.08]  That's a very Matt question.
[346.14 --> 347.10]  It was from his docs.
[347.10 --> 349.48]  I can say it with a cheeky accent if you want.
[350.34 --> 353.02]  I will not attempt to sound like Matt.
[353.12 --> 356.00]  He's got a unique, unique accent of his own.
[356.20 --> 358.68]  Well, he attempts to sound like everybody else.
[358.76 --> 360.16]  Can't we try to sound like him?
[360.20 --> 360.72]  That's true.
[361.12 --> 361.90]  You've already tried.
[361.90 --> 362.56]  Yeah, yeah.
[363.88 --> 367.14]  We should all do our impressions of Matt doing his impression of Francesc.
[367.40 --> 369.88]  But no, seriously, Johnny, back to you.
[369.96 --> 372.44]  What does open source mean to you?
[372.52 --> 374.92]  Okay, I can tell you what I used to think open source was.
[374.92 --> 379.78]  It was basically, to me, it was free software, free stuff, right?
[379.78 --> 380.52]  You could go online.
[380.76 --> 389.64]  And if you are a user of software, basically, I remember when I didn't want to buy a full-on Microsoft Office suite or something.
[389.74 --> 392.22]  I went and found open source alternatives, right?
[392.90 --> 393.80]  There's been a few.
[394.06 --> 394.68]  Open Office?
[394.88 --> 396.06]  Yeah, Open Office was one of them.
[396.20 --> 397.20]  There's been a few over the years.
[397.20 --> 400.72]  But basically, to me, it was like, okay, a way of saying, oh, free stuff?
[400.94 --> 401.12]  Sure.
[401.30 --> 403.30]  I'll get some of that, right?
[403.30 --> 419.14]  But over the years, obviously, as an engineer who uses open source software, every time I get a package from the web to incorporate into my projects and use that and actually deliver value for business, I'm using open source software.
[419.14 --> 435.04]  So my appreciation of what open source is, right, and sort of the innovation that it brings forth, I've definitely learned to appreciate that more, even if I can't always contribute back, especially some of the things I work on at my day job.
[435.04 --> 445.92]  I can't always sort of – not every company has a sort of giving or able to sort of give away some of the things that it does, especially things that are sort of a core to their business.
[446.42 --> 464.16]  But every opportunity that one gets, right, you should be trying to contribute back because the same way you sort of leverage and sort of bring in these open source components into your own world to actually deliver value, that's actually – you're getting something for free indeed, but it's actually creating value.
[464.16 --> 471.14]  So you need to be able to sort of send some of that back for somebody else to sort of be able to sort of leverage that, right, the pay-forward kind of model.
[472.04 --> 480.62]  So you mentioned that you've never – you know, a lot of the companies you work for don't open source their projects, which is quite common, you know, obviously.
[480.80 --> 482.10]  We all have private repos.
[483.26 --> 488.50]  But have you ever worked for a company that just won't use open source at all?
[488.50 --> 504.14]  I've been fortunate enough to not have worked directly for those companies, but I have worked on projects for other like third-party companies through my employer that basically did not want to use any open source at all.
[504.14 --> 520.72]  And usually that sort of – the problem came with sort of legal and licensing, especially with projects that did not have any sort of specific explicit licensing and the repository themselves where you couldn't tell whether you were allowed to use the software for profit or not.
[521.14 --> 526.94]  And whenever the sort of – the waters were kind of murky, legal sort of always basically say, nope, you can't have that in there.
[527.96 --> 530.52]  Yeah, legal's always – legal's great at that sort of stuff, aren't they?
[530.52 --> 534.22]  I remember – ran into very similar things.
[534.60 --> 546.38]  I was doing a couple projects for Apple and every time we wanted to use a new gem, we had to submit it in writing to legal, wait for them to review the license and all that sort of stuff.
[546.64 --> 550.88]  And then it would have to get a pass through their security department too.
[551.20 --> 552.64]  That's an interesting take.
[552.76 --> 554.26]  Let's – Carmen, let's switch to you.
[554.42 --> 558.54]  Let's – I mean open source, it's not just about free, right?
[558.54 --> 560.42]  I mean it's also about the software.
[560.60 --> 566.12]  I mean Johnny talked a lot about, you know, I didn't have to pay for it, which is a great part of open source and something I love.
[566.52 --> 569.56]  But there is kind of this security issue.
[569.78 --> 577.10]  And I'm assuming, Travis, you must have dealt with some security issues when people are just uploading any old code to your servers.
[577.10 --> 578.10]  Oh, yeah.
[578.40 --> 581.44]  I mean really we're giving them a remote execution environment.
[581.98 --> 585.90]  And so we had to constantly think about how we wanted to gate that and isolate it.
[586.16 --> 596.50]  And because it was running on cloud providers, we also heavily worked with cloud providers to try to provide like micro segmentation and micro isolation and all these security buzzwords.
[596.50 --> 602.50]  I think that there's – in terms of security, that is becoming less and less of a thing.
[602.68 --> 611.28]  I think more and more people are paying attention to open SSL and other sort of vital pieces of digital infrastructure that keep the internet safe.
[611.28 --> 619.38]  And they're finally getting corporate sponsors to say, you know what, we need to have people who can dedicate full-time brain power to this.
[619.48 --> 619.96]  And they are.
[620.26 --> 631.60]  And so I love that they're providing cycles or engineers to do exactly that because they're realizing that when the code is open and you can lead the horse to water but you can't make it drink.
[631.86 --> 637.06]  And so, yes, there's one thing about having it open but there's another essence of security hardening.
[637.06 --> 645.06]  And I think that more and more people are now realizing – like I think Heartbleed was the first moment where people realized, uh-oh, right?
[645.70 --> 651.62]  People used this so much but they didn't realize that it was being put together by toothpicks and glue.
[652.08 --> 654.02]  Most of the world is.
[654.72 --> 655.88]  Most of the world is, right?
[655.94 --> 656.30]  Exactly.
[656.52 --> 664.06]  And I think that those are the toothpick and glue projects that are now being used in thousands of open source projects are now getting a critical review.
[664.06 --> 667.44]  And they're getting brain power to security harden it.
[668.16 --> 668.64]  Yeah.
[668.86 --> 675.22]  You know, I know someone reached out to me with a security issue very recently on one of my packages.
[675.54 --> 679.34]  I'm not going to say which one as we work to fix it.
[679.48 --> 685.48]  But, yeah, it's – you know, I love that there are people out there who are looking for that sort of stuff.
[685.48 --> 691.22]  But as a user, how do I know if what I'm about to take in is safe?
[691.72 --> 692.96]  You know, it's open source.
[693.04 --> 694.34]  I'm about to use something.
[695.00 --> 700.68]  You know, Johnny was saying like early in his days, you know, he didn't – you know, he used it because it was free.
[701.06 --> 703.46]  But, you know, fine, you load up OpenOffice because it's free.
[703.54 --> 706.68]  But, you know, if you're not a developer, you don't know what's inside of it.
[707.26 --> 708.44]  It could be anything.
[708.44 --> 717.06]  How do we protect ourselves against that sort of open source stuff when we're, you know, trying to review a package or a tool to use?
[717.66 --> 719.72]  That's a problem that a lot of people are working to solve.
[719.84 --> 724.56]  I know GitHub just came out with their GitHub Universe product announcement about exactly this.
[725.10 --> 734.04]  They have a security net tab open now where you can have responsible disclosure and, you know, things like checksums out of the gate as part of the GitHub infrastructure.
[734.40 --> 735.78]  So you don't have Matt in the middle attacks.
[735.78 --> 740.70]  And so I see GitHub is really – you're listening to users and coming up with solutions for that.
[740.96 --> 748.04]  And I think that because GitHub is increasingly the place to have your code hosted, having them do that was a big step forward.
[748.24 --> 750.58]  Because otherwise, really, you just didn't know.
[750.80 --> 751.58]  You just don't know.
[752.10 --> 752.90]  No, you really don't.
[752.96 --> 753.56]  That's the problem.
[754.16 --> 754.48]  Yeah.
[754.68 --> 755.48]  Yeah, totally.
[755.72 --> 756.78]  It's totally scary.
[757.12 --> 757.72]  It is scary.
[757.82 --> 761.86]  It's almost like – and I know I've done this time and again.
[761.86 --> 765.70]  I'll find a package out there that does something that I want.
[765.82 --> 770.64]  Maybe it's a – you know, it helps me solve a particular problem and I don't want to sort of reinvent that wheel.
[770.92 --> 774.86]  So I don't necessarily want to copy and paste or do anything sort of funky.
[775.04 --> 778.30]  Basically, I'll just bring in the dependency into my project.
[779.02 --> 783.50]  And then, you know, like a few days later, I'll be like, huh, that was a pretty sizable package.
[783.64 --> 785.00]  What else does it do, right?
[785.00 --> 792.80]  So it's like you – after the fact, right, you simply trust that because the code is open source, you can simply bring it in and it's safe.
[793.06 --> 798.18]  Even if the originator of the project, right, doesn't have sort of ill intent, right?
[798.18 --> 802.50]  Even if they're not malicious, they're not trying to create something to create, you know, backdoors in your software and whatnot.
[802.50 --> 817.36]  But because not everybody codes with security first, right, as sort of a mindset, it's very easy for – to have, you know, to basically to open up, right, basically yourself to attack, right?
[817.40 --> 821.52]  To make the surface area, right, for attack, right?
[821.60 --> 827.82]  Through that package that you bring into your project, it's so easy to actually expose yourself in that way, right?
[827.82 --> 832.32]  So which is – these days, I'm a little bit more cautious about sort of the package that I'm bringing in.
[832.44 --> 836.78]  You know, I might spend, you know, like an hour or two looking through the code and saying, is there anything obvious, right?
[836.78 --> 841.62]  I'm not a security expert, but maybe there are some things in there that are obvious that I've seen before that I can be like, you know what?
[842.00 --> 843.28]  Huh, this doesn't look quite good.
[843.34 --> 846.78]  Maybe I'll open up a PR or talk to somebody or something, right?
[846.78 --> 854.64]  Or at least maybe just say, you know what, this part of the project or this particular project for reason X, Y, and Z, like maybe I can find an alternative, right?
[854.64 --> 869.96]  So there's a certain level of trust, right, that I think is we simply assume that just bringing the package into our project and it solves our problem, that we can simply trust it also from a security standpoint, which I think is – I don't know if there's a solution for that, honestly.
[870.56 --> 873.38]  Yeah, I think we're at an inflection point, right?
[873.46 --> 877.46]  And that first inflection point was left pad in the Node.js world, right?
[877.46 --> 894.46]  Where Node has this problem of all these modules and they're just bloated and you can – and beginners who are just kind of – they trust that the person that's taken the time to package this up and send it up to NPM is going to have some sort of verification or process, right, through that.
[894.46 --> 907.14]  And so, yeah, we're kind of at the inflection point where we realize, wait a minute, that people who are responsible for hosting some of this stuff, like package management places and infrastructure need to really think about that.
[907.58 --> 910.12]  And that's why I like that GitHub is partnering with a lot of them.
[910.18 --> 919.64]  But the other thing is like the attack vector, I can't – I think it also was in the Node world where someone gained maintainer access and then was doing – fiddling with the code.
[919.64 --> 921.90]  I can't remember which one it was.
[922.06 --> 930.26]  But, you know, everyone sort of faulted the maintainer for sort of blindly trusting someone who just simply asked, hey, can I have maintainer access?
[930.46 --> 934.42]  Sure, because we have maintainer burnout, which we'll talk about later, I'm sure.
[935.24 --> 937.04]  Well, maintainers get burnt out?
[937.14 --> 939.08]  I know nothing about that.
[939.12 --> 939.48]  Aw.
[939.64 --> 940.68]  Nothing at all.
[941.60 --> 944.50]  But no, the security tools that are going out there are great.
[944.50 --> 952.40]  But sometimes just plain old regular bugs open a security hole that, you know, an automated tool isn't going to find.
[952.86 --> 956.20]  You know, we can only catch so much that's automated, right?
[956.22 --> 958.70]  Because sometimes just bad code.
[959.52 --> 962.28]  Like Johnny said, maybe you're not looking at it from a security perspective.
[962.38 --> 966.02]  But even if you are, sometimes you just type the wrong thing.
[967.32 --> 970.10]  We type the wrong thing sometimes, and that's what bugs are.
[970.22 --> 971.44]  But sometimes they're dangerous.
[971.44 --> 977.52]  Given time as well, so you might release, you know, a package or a piece of software today, right?
[977.56 --> 980.52]  And then everything might be okay, right, from a security standpoint.
[980.74 --> 987.16]  But over time, as new vulnerabilities are discovered, your package may become unsafe to use, right?
[987.18 --> 991.76]  Because you have, you yourself have some dependency or something you're relying on, which is not unsafe.
[991.76 --> 1000.32]  So I think it's a very large scale kind of problem that I don't think any one individual is going to be able to solve.
[1000.40 --> 1010.18]  And I think it's sort of a, I think there's some responsibility there that sort of falls onto the NPMs of the world or the anywhere where you kind of host code, right?
[1010.22 --> 1014.72]  The Githubs of the world, anywhere you host code that they can do a lot more, right?
[1014.72 --> 1020.94]  And they can have a lot larger impact, right, on being able to catch some of those issues because they're hosting so much of that code.
[1021.60 --> 1021.84]  Right.
[1021.98 --> 1024.06]  Yeah, they've got the heuristics behind it, don't they?
[1024.48 --> 1024.70]  Yeah.
[1025.08 --> 1030.46]  And I mean, there was a common practice, and it's still around, but Patch Tuesday, right?
[1030.52 --> 1037.38]  That's what security or sysadmins did for many, many years because they recognized that this was always going to be a moving target.
[1037.58 --> 1039.22]  And you always had to send patches in.
[1039.22 --> 1044.56]  So, yeah, recognizing that it's always going to be a moving target, and code rot is a thing.
[1054.44 --> 1057.44]  This episode is brought to you by our friends at Rollbar.
[1057.56 --> 1060.52]  Move fast and fix things like we do here at Changelog.
[1060.64 --> 1063.28]  Check them out at rollbar.com slash changelog.
[1063.54 --> 1065.86]  Resolve your errors in minutes and deploy with confidence.
[1065.86 --> 1069.04]  Catch your errors in your software before your users do.
[1069.40 --> 1075.68]  And if you're not using Rollbar yet or you haven't tried it yet, they want to give you $100 to donate to open source via Open Collective.
[1075.78 --> 1080.74]  And all you got to do is go to rollbar.com slash changelog, sign up, integrate Rollbar into your app.
[1080.82 --> 1084.82]  And once you do that, they'll give you $100 to donate to open source.
[1085.22 --> 1088.04]  Once again, rollbar.com slash changelog.
[1088.04 --> 1101.14]  So let's move to the maintainer side, Carmen, since you brought that up.
[1102.00 --> 1104.06]  You know, it's an interesting topic.
[1104.18 --> 1108.36]  Why don't you tell us a little bit about what it's like to be an open source maintainer?
[1108.36 --> 1110.78]  Well, I have a cool story about my...
[1110.78 --> 1112.00]  You have tons of cool stories.
[1112.06 --> 1112.66]  That's why you're here.
[1113.44 --> 1114.20]  Yeah, yeah.
[1114.52 --> 1120.34]  Well, so one of my first jobs when I was 20 years old, one of my summer jobs in college between...
[1120.34 --> 1123.76]  In the summer was to be a hotel desk clerk, right?
[1124.36 --> 1133.80]  And when we were both interviewing and as well as getting oriented to the job, me and all the other summer workers at this desk,
[1133.80 --> 1146.16]  the person who was onboarding us made it very clear that we were going to be asked a lot of repetitive questions over and over and over again.
[1146.36 --> 1147.80]  I see where the story's going now.
[1147.98 --> 1148.34]  Yes.
[1148.34 --> 1149.34]  But we also...
[1150.00 --> 1151.08]  And we were like...
[1151.08 --> 1152.08]  And she also warned us.
[1152.18 --> 1158.60]  You also will be encouraged to think of things like signs that they can read to get their questions answered.
[1158.76 --> 1160.06]  So you'll put signs up, right?
[1160.20 --> 1163.44]  Or maybe you'll have a brochure that would explain a lot of things.
[1163.44 --> 1172.62]  And you could do everything in your power to try to explain to customers how things work, where to find things, where to go for things, what you don't need.
[1173.10 --> 1181.08]  But you'll never, ever, ever succeed here if you don't get over the fact that you're going to get asked a lot of repetitive questions.
[1181.32 --> 1183.96]  And if you cannot handle that, then you need to not work here.
[1184.34 --> 1186.36]  And this served me well.
[1186.60 --> 1187.82]  This served me well.
[1187.82 --> 1193.22]  Because when I moved into a maintainer space, that is exactly how open source works.
[1193.44 --> 1195.68]  But on steroids, if you will, right?
[1195.80 --> 1197.62]  It really is just...
[1198.24 --> 1203.62]  It's like not just one hotel desk, but maybe, gosh, 99 concurrently.
[1204.52 --> 1210.62]  And you have, you know, 10s or 20s or, you know, hundreds of guests all clamoring for things.
[1210.62 --> 1212.70]  And you write a document to maybe clarify.
[1212.70 --> 1214.68]  And you try to make that document visible.
[1214.68 --> 1218.30]  Or you try to even have bots to do these kind of things.
[1218.30 --> 1220.98]  And yet the inquiries will still stay the same.
[1220.98 --> 1222.06]  And they will still occur.
[1222.24 --> 1224.78]  And that is the nature of maintainer burnout.
[1225.32 --> 1225.52]  Wow.
[1225.58 --> 1227.00]  That was really good.
[1227.00 --> 1228.00]  That was...
[1228.00 --> 1230.40]  Okay.
[1230.50 --> 1231.72]  I think that's the end of the show.
[1231.72 --> 1238.36]  Somebody has thought about this topic before and is highly passionate about it.
[1239.16 --> 1244.58]  Is this coming from a place of deep emotion here, Carmen?
[1244.76 --> 1245.68]  It feels like it.
[1245.98 --> 1249.84]  I mean, you know, I've just given a lot of thought about it.
[1249.94 --> 1253.84]  I've been both on the contributor side and the maintainer side.
[1253.84 --> 1256.78]  I now work in open source strategy at Google.
[1256.78 --> 1260.50]  And I work for a programming language where I just got hired.
[1260.50 --> 1266.60]  And I really want to think deeply about how the experience can be improved for everyone involved.
[1266.60 --> 1266.94]  Right?
[1267.44 --> 1272.38]  And so the maintainers of a programming language, it's like sort of a different beast entirely.
[1272.38 --> 1277.38]  It's kind of my whole headspace lately about how to onboard people coming to go.
[1277.58 --> 1282.58]  Whether you're just a user in the way that Johnny described the user, a consumer of the thing.
[1282.58 --> 1286.72]  Or you're going to be a person that eventually becomes a contributor of the thing.
[1286.78 --> 1288.48]  And these are very different audiences.
[1288.48 --> 1294.88]  But they are unique paths in terms of how you want to engage with the language.
[1295.60 --> 1297.68]  So, yeah, I think about it a lot, Mark.
[1299.14 --> 1304.50]  I also give a lot of thoughts to what it's like to be an open source maintainer.
[1304.74 --> 1304.86]  Yeah.
[1305.20 --> 1308.58]  For those of you unfamiliar, I run a few projects out there.
[1308.58 --> 1314.84]  I have basically at this point in my life, when I'm not training, which is what I do.
[1314.98 --> 1317.48]  You know, Corey, Lanou, and I travel around the world.
[1317.56 --> 1318.32]  We do training.
[1318.42 --> 1319.88]  We train gophers all around the world.
[1319.92 --> 1320.62]  And it's fantastic.
[1320.76 --> 1324.68]  But when I'm not doing that, I basically just write open source software.
[1325.52 --> 1330.66]  Your analogy of the hotel was so, so accurate.
[1330.66 --> 1334.80]  You know, it's funny because, yeah, you do.
[1334.92 --> 1337.80]  You write docs and you put together websites.
[1338.12 --> 1350.98]  Or, you know, in my case, I do videos and blog posts and, you know, all these sorts of things in an effort to, like you said, make it easier for people and to help them answer their own questions.
[1350.98 --> 1360.80]  But invariably, I still, you still get the GitHub issues or the Slack messages where the response is just to drop a link to the document itself.
[1362.44 --> 1362.84]  Right?
[1362.98 --> 1365.60]  The let me Google that for you kind of approach.
[1366.56 --> 1367.44]  You get those.
[1367.58 --> 1370.78]  But, you know, those, like you said, and those can be maddening.
[1370.92 --> 1376.10]  They can be infuriating because you keep saying to yourself, why do I write the docs if no one's reading the docs?
[1376.10 --> 1376.58]  Yes.
[1377.48 --> 1378.00]  Right?
[1378.48 --> 1382.24]  And if you Google, like literally go now into your search browser.
[1382.70 --> 1388.02]  I use Google, but, you know, go at any web search.
[1389.02 --> 1391.98]  And just type in why are maintainers.
[1392.62 --> 1395.12]  The autofill would be, like, why are they so horrible?
[1395.62 --> 1403.48]  And it's such a bad, you know, it really is a lack of understanding that you, you know, like you've never worked a summer job behind a hotel desk.
[1403.76 --> 1404.20]  Right?
[1404.20 --> 1413.32]  Or maybe you weren't in the registration volunteer for conferences or something or any kind of thing that's going to require repetition ad nauseum.
[1413.54 --> 1416.18]  There's a reason why maintainers are the way they are.
[1416.38 --> 1422.22]  And just trying to say, well, why are they that way goes a long way forward and towards being a better contributor.
[1423.10 --> 1423.56]  Yeah, totally.
[1423.78 --> 1429.02]  So, you know, I mean, I know I occasionally can get snippy and I try not to.
[1429.02 --> 1440.26]  But occasionally, like I said, it happens, you know, when you're responding to the same thing or the thing that really gets me as a maintainer is the this is broken bug.
[1440.26 --> 1445.00]  I feel like we all know what that is.
[1445.08 --> 1449.06]  And the title is usually XYZ is broken or doesn't work.
[1449.66 --> 1451.64]  You know, some super blanket.
[1452.40 --> 1455.56]  There's, you know, it just it's not working.
[1455.56 --> 1460.84]  And then they say, I tried to use software X and it doesn't work.
[1460.90 --> 1462.58]  And that's like the whole ticket.
[1463.88 --> 1467.78]  You know, and you're just like, look, I want to help.
[1468.02 --> 1469.56]  Please, like, give me some more information.
[1470.40 --> 1473.56]  Like, do the give us a repo, like a reproducible thing.
[1474.30 --> 1474.74]  Right.
[1474.80 --> 1476.26]  Like, fill in the information.
[1476.54 --> 1478.94]  You know, do the go ENV stuff we've asked for.
[1478.94 --> 1481.14]  Like, help us help you.
[1482.14 --> 1486.12]  And they're automated tools that GitHub and GitLab are even including in that.
[1486.22 --> 1486.32]  Right.
[1486.38 --> 1487.62]  With via issue templates.
[1488.02 --> 1488.20]  Right.
[1488.24 --> 1493.62]  If you go and click on an issue template, you have a pre-filled set of questions that they want you to ask.
[1493.92 --> 1499.68]  And it is quite frustrating to see that people who file issues or bugs ignore those questions.
[1500.00 --> 1500.24]  Right.
[1500.70 --> 1504.06]  And then you try to say something like, please fill out all of these.
[1504.06 --> 1506.18]  If you cannot fill out all of these, then don't.
[1506.28 --> 1508.90]  Please go take it to a discussion forum or somewhere else.
[1509.20 --> 1515.40]  Because there's the psychological effect of I look at the number of open issues and it's growing by hundreds or thousands.
[1515.96 --> 1518.10]  In Go's case, it's like something like 4,000.
[1518.50 --> 1532.22]  And so then you have a lot of time gardening and triaging and just doing a lot of toil work to the point where you can't even get to the actual work of feature requests or patches or anything like that.
[1532.22 --> 1534.36]  And it's, you know, it's a real problem with them.
[1534.36 --> 1538.96]  And it's kind of the, I love Jen Schiffer on Twitter.
[1539.12 --> 1540.82]  She did that 80s meme generator.
[1540.82 --> 1544.04]  And it was like, eight open sources of prison.
[1544.34 --> 1548.88]  And it just made me laugh because those who've been in it understood exactly what that meant.
[1549.26 --> 1549.96]  I'll have to find it.
[1550.42 --> 1551.68]  Yeah, please do find that.
[1551.96 --> 1556.48]  Johnny, as a contributor, what do you do to help the maintainers?
[1556.54 --> 1559.92]  And we're going to talk about why maintainers do what they do in a few minutes.
[1559.92 --> 1563.80]  Because we don't, you know, obviously we complain a lot, but we do it for a particular reason.
[1563.80 --> 1567.70]  But tell us, like, you know, what can contributors do to help the maintainers?
[1567.80 --> 1572.18]  What do you try to do when you're opening tickets or issues or pull requests?
[1572.66 --> 1580.36]  Well, first thing I do is if there is an issue template, I don't delete the template when I open up a ticket.
[1580.36 --> 1585.44]  I don't delete it and then start, you know, going, you know, ad hoc description of what the problem is.
[1585.52 --> 1586.74]  The questions are there for a reason.
[1586.92 --> 1591.46]  So basically that's the maintainer helping me help them find what my problem is, right?
[1591.54 --> 1599.90]  So basically my job as a follower of an issue is to actually provide all the necessary pieces of information.
[1600.28 --> 1602.44]  Sometimes some of it may apply, some of it may not.
[1602.56 --> 1607.00]  But the idea is that basically you put yourself in the maintainer's shoes, right?
[1607.00 --> 1612.00]  When they receive that ticket, if you were to receive your own ticket, how would you feel, right?
[1612.04 --> 1615.58]  If the information you asked for to help you troubleshoot wasn't available, right?
[1615.62 --> 1618.42]  You'd probably, you know, it'd drive you mad, right?
[1618.42 --> 1624.10]  So if you are looking for a fast resolution to your problem, you kind of follow the rules of the template, right?
[1624.16 --> 1629.24]  So that's the first thing I'd do is, and second, you know, I might even try to, you know, if I know what the problem is,
[1629.48 --> 1632.48]  especially if I know what the problem is, I just open up a PR to fix it.
[1632.64 --> 1635.14]  I mean, it's not that complicated, right?
[1635.14 --> 1638.20]  So I'll strike that, but we can still leave it in the recording, but I'll strike that.
[1638.28 --> 1643.36]  And the reason for that is a lot of times there's some fear and trepidation there.
[1643.88 --> 1651.40]  Basically, there's the imposter syndrome where you mean like, well, like, I don't feel like I'm competent enough to submit, you know, a pull request today.
[1651.60 --> 1654.46]  And there's that factor of it, and that's totally fine.
[1654.90 --> 1662.34]  Well, there's also the factor with a pull request of should I, you know, ask for permission to make this pull request first?
[1662.82 --> 1664.00]  Right. Yes. Yeah.
[1664.00 --> 1678.24]  Right. Because I've had to reject PRs, not because I didn't want people contributing, but because it wasn't in line with what we, what the fix could be or should be or what the project is trying to do or X, Y, and Z.
[1678.34 --> 1683.42]  You know, usually it's around adding a feature as opposed to any, you know, a bug fix of any sort.
[1683.48 --> 1684.22]  Usually it's a feature.
[1684.30 --> 1687.08]  It's anything that's kind of changing or bloating the project.
[1687.44 --> 1690.22]  You know, I always feel like you should ask for permission first.
[1690.22 --> 1690.86]  Yeah.
[1691.34 --> 1704.08]  There's a growing body of practices that sort of show, okay, when is, where should I go to first ask about what before I do anything as regarding pushing code out, right?
[1704.08 --> 1706.16]  Like a PR or anything.
[1706.48 --> 1709.72]  And part of it is using the contributors.md document.
[1709.84 --> 1716.26]  So GitHub, again, is listening to users and trying to grow that best practices by having a community tab.
[1716.32 --> 1719.28]  And that community tab is things like, hey, do you have a code of conduct?
[1719.46 --> 1722.92]  Hey, do you have a contributing.md document at the root of your repository?
[1723.78 --> 1727.32]  And does that have specific instructions for how you want to contribute?
[1727.32 --> 1733.18]  And, you know, there are some really good open source projects that have made use of that.
[1733.46 --> 1735.28]  And then there are some that go, that don't.
[1735.64 --> 1743.22]  But I think every time that you go in, there's some things that both maintainers can do to help contributors get a sense.
[1743.40 --> 1747.92]  But again, with the caveat that no matter what you do and no matter how much you try to communicate,
[1748.42 --> 1752.82]  you're always going to have to take those hotel desk kind of repetitive questions and deal with it.
[1752.96 --> 1756.16]  And that's where I feel like, you know, the idea of maybe shifts, right?
[1756.16 --> 1761.42]  Like, you know that, okay, I'm going to go into open issues and that this is my shift.
[1761.54 --> 1766.46]  And it's a mental psychological shift where I'm not going to look at it for, you know,
[1766.58 --> 1769.68]  three days off or four days or whatever it can be.
[1769.72 --> 1771.88]  Because sometimes that's the burnout, right?
[1771.92 --> 1772.68]  The expectations.
[1773.32 --> 1777.62]  And also that's one thing in the contributor.md document that you can have in the markdown document,
[1777.70 --> 1783.86]  which is like, please expect a response of, you know, and you can even commit it and version control it.
[1783.86 --> 1789.20]  And if you're going to go on vacation, you know, and no one else is stepping up to maintain some of the libraries that you maintain,
[1789.42 --> 1794.54]  that can be the living document that says, please note, you know, there will be no, you know,
[1794.78 --> 1799.08]  code review or PRs or issues responding for two weeks because the maintainer is on vacation.
[1799.24 --> 1804.96]  And I mean, there's also a status on your user space for GitHub as well.
[1804.96 --> 1806.22]  So people can see that.
[1806.86 --> 1809.48]  If you have a popular project, right?
[1810.22 --> 1814.90]  And there's a part of me that believes that the more popular the project,
[1815.14 --> 1819.80]  the more the onus falls on you as the creator of the project or the maintainer of a project
[1819.80 --> 1825.60]  to also be willing to take on, you know, that sort of the analogy, right?
[1825.64 --> 1830.12]  Of the clerk behind the desk who has to answer the same questions over and over again, right?
[1830.12 --> 1836.72]  Because we know users don't read, you know, and since, you know, coders and programmers and contributors,
[1836.98 --> 1839.68]  they also people, the chances are they're not going to read either.
[1839.80 --> 1844.18]  So to you, as a creator of something, you're like, why are you asking me this?
[1844.26 --> 1846.68]  Like, it's in the code or it's in the read me, right?
[1846.72 --> 1850.36]  Like, you didn't read, you know, you could easily get snippy, right?
[1850.42 --> 1850.86]  And be like, what?
[1850.96 --> 1853.00]  Go read the doc, like RTFM, right?
[1853.06 --> 1854.58]  Like, you could just go read the doc.
[1854.58 --> 1861.30]  But then there's a certain expectation that comes with you being also like an educator, right?
[1861.30 --> 1865.96]  You have to sort of educate people on how to use that piece of software that you created.
[1866.08 --> 1868.10]  So there's a bit of responsibility there as well.
[1868.16 --> 1868.86]  And I totally agree.
[1868.98 --> 1872.70]  It can get, you know, sort of repetitive and mundane and sort of, you know, frustrating.
[1873.12 --> 1876.70]  And that's definitely a contributing factor to burnout.
[1877.02 --> 1881.86]  But I think there's a certain expectation, right, that comes with having an own process project,
[1881.96 --> 1882.78]  especially when it's popular.
[1882.78 --> 1885.34]  It's like the old dev adage, right?
[1885.62 --> 1888.14]  I hope your open source project is successful.
[1891.26 --> 1894.12]  It's a thing that you do.
[1894.24 --> 1895.36]  But I mean, I don't know.
[1895.48 --> 1900.76]  So I find that there's definitely a period, you know, like what Johnny was talking about,
[1900.82 --> 1907.50]  the big projects where I think as an open source maintainer, you also need to step off the gas
[1907.50 --> 1910.56]  a little bit when your project starts reaching a certain size.
[1910.56 --> 1916.08]  You have to say to yourself, this is bigger than me now.
[1916.20 --> 1918.82]  I can't do it all by myself anymore.
[1920.22 --> 1922.10]  I need community help.
[1922.18 --> 1925.28]  I need to bring on other kind of core maintainers.
[1925.80 --> 1927.14]  I know that's what happened with Buffalo.
[1927.30 --> 1932.94]  And I couldn't imagine not having, you know, the Buffalo core team helping me out, you know,
[1932.94 --> 1936.30]  because it's just too much to do.
[1936.46 --> 1939.90]  And so you've got to, as a maintainer, you need to back off a little bit too.
[1940.26 --> 1942.72]  So you've got to, especially when you start getting snippy.
[1942.86 --> 1947.48]  When you start getting snippy, I think that's your sign that it's time to take a break,
[1947.56 --> 1952.56]  take a little bit of a break and maybe try to help ask other people to start helping.
[1952.56 --> 1955.64]  Because we often don't do that.
[1955.70 --> 1958.64]  We don't ask for the help from the community when we really should.
[1959.28 --> 1959.30]  Yeah.
[1959.44 --> 1964.00]  I noticed that you asked for help in a tweet roughly two or three weeks ago, Mark,
[1964.06 --> 1965.62]  for a certain library in Buffalo.
[1965.62 --> 1968.10]  And I really, I retweeted it because I've been there.
[1968.24 --> 1968.96]  And I'm like, yeah.
[1969.96 --> 1970.14]  Yeah.
[1970.30 --> 1971.20]  It was a packer.
[1971.24 --> 1976.06]  And I'm still, you know, looking for, not even necessarily maintainers, but just people to,
[1976.46 --> 1980.34]  you know, and this is something that if your company doesn't, like Johnny, for example,
[1980.34 --> 1984.00]  maybe you're not in a position where you can contribute code to open source.
[1984.16 --> 1989.06]  But, you know, if you use projects, go and help triage their issues.
[1989.06 --> 1991.32]  It's a great way to help a project.
[1991.86 --> 1997.02]  Just go through them, answer some of them, being like, oh, this is clearly just an environmental
[1997.02 --> 1997.74]  issue.
[1998.12 --> 2000.18]  Have you turned, you know, GoMods on.
[2000.78 --> 2002.16]  Turn it on, everything's going to work.
[2002.22 --> 2003.32]  You know, that sort of stuff, right?
[2003.40 --> 2008.36]  Like take some of those things off the maintainer so they can work on the parts of the project that
[2008.36 --> 2012.56]  you're, don't, you don't feel you're capable of being able to contribute to yet.
[2013.04 --> 2016.62]  So, yeah, I mean, I always, I think that's a great way to help a project and there's no
[2016.62 --> 2017.36]  coding involved.
[2017.44 --> 2018.72]  It's just triaging issues.
[2018.84 --> 2020.08]  I couldn't reproduce this.
[2020.10 --> 2023.16]  Or can you give us better steps to reproduce this?
[2023.26 --> 2028.06]  Like, you know, that's if you're a community member and you're looking to help, that's how
[2028.06 --> 2029.82]  you can, I think that's how you can do it.
[2030.08 --> 2033.50]  Let's talk about why open source maintainers do this stuff.
[2033.50 --> 2038.90]  I mean, we just complained for 20 minutes about documentation and repetitive questions
[2038.90 --> 2039.50]  and issues.
[2039.80 --> 2042.24]  But why do maintainers do it?
[2042.60 --> 2043.68]  Carmen, why do you do it?
[2044.44 --> 2046.44]  Why do I maintain open source projects?
[2046.82 --> 2048.42]  Yeah, not just because of work.
[2049.34 --> 2058.32]  I feel like whether it was the case of Travis or Go now, I feel like I'm part of a cause,
[2058.44 --> 2058.58]  right?
[2058.62 --> 2060.82]  I'm contributing to a cause, right?
[2060.82 --> 2065.42]  I'm contributing to a thing that is going to better other people's lives.
[2065.62 --> 2069.26]  And I think that's also where the massive network effects are happening in like one
[2069.26 --> 2073.22]  of the most popular Go open source projects, which is Kubernetes, right?
[2073.26 --> 2078.34]  You have this sense that you're in a movement or you're part of history where you're making
[2078.34 --> 2080.66]  things better for the next generation, right?
[2081.10 --> 2081.98]  And that's the way I do it.
[2082.54 --> 2083.34]  That's a valid reason.
[2083.88 --> 2087.04]  Johnny, I know you don't run very many open source projects.
[2088.16 --> 2088.64]  I do not.
[2088.64 --> 2093.32]  I feel like, you know, would you like to respond to the question?
[2093.58 --> 2095.40]  I mean, you know a lot of maintainers.
[2095.64 --> 2097.74]  You know, I mean, what's the word in the street?
[2099.62 --> 2100.46]  Word in the street.
[2102.08 --> 2104.68]  What's the scuttlebutt on open source maintainers?
[2105.20 --> 2106.24]  What's the scuttlebutt?
[2106.78 --> 2110.30]  I'm going to use just terms from like the 20s for the rest of the show.
[2111.44 --> 2112.12]  Hear, hear.
[2112.38 --> 2112.66]  Wow.
[2112.80 --> 2113.74]  I'm a cool cat.
[2114.10 --> 2114.46]  Let's be honest.
[2114.46 --> 2114.70]  Yeah.
[2115.58 --> 2116.46]  Real hept cat.
[2116.72 --> 2117.08]  Go on.
[2117.18 --> 2118.14]  Yeah, you can use that.
[2118.28 --> 2119.08]  You can use a cool cat.
[2119.18 --> 2119.64]  Yeah, for sure.
[2120.42 --> 2121.92]  No, but here's the thing, though.
[2122.68 --> 2125.86]  So I see most of what I'm involved in.
[2125.98 --> 2129.48]  Again, because, you know, I think we said at the start of the show, there's lots of ways
[2129.48 --> 2130.72]  to contribute, right, to open source.
[2130.80 --> 2135.66]  I think some of the ways that I contribute the most, right, the most often is basically
[2135.66 --> 2137.38]  through a community organizing, right?
[2137.38 --> 2144.06]  So that is definitely not a direct approach to contributing, but definitely something
[2144.06 --> 2146.14]  that sort of helps feed the community around it.
[2146.18 --> 2148.22]  So it's on the sort of periphery a little bit.
[2148.62 --> 2153.94]  Actually, that's one of the very reasons why I got involved in sort of a community, sort
[2153.94 --> 2156.08]  of a stewardship, if you will, if you want to call it that.
[2156.56 --> 2158.54]  Wait, can I pause you for a second?
[2158.64 --> 2163.00]  Because I think what we've stumbled on is something, or at least what I may have just
[2163.00 --> 2167.58]  had the realization on, you know, we're talking about open source maintainers, and Carmen and
[2167.58 --> 2170.54]  I are talking about open source maintainers of code.
[2170.78 --> 2173.36]  You're an open source maintainer of community.
[2174.14 --> 2179.60]  Yeah, I want to be clear that when I say I'm a maintainer, I say I'm a maintainer of the
[2179.60 --> 2184.12]  ecosystem, the people who are a part of it, and especially efforts.
[2184.12 --> 2191.60]  Like when I think of what Johnny is for Go, he's absolutely a vital, like essential contributor,
[2191.60 --> 2193.00]  as are you, Mark, right?
[2193.08 --> 2196.82]  And as are anybody, because you think about it, it's like, if you're going to build a
[2196.82 --> 2200.96]  big thing and no one uses it, then the failure is on the fact that you've made it very hard
[2200.96 --> 2202.80]  to either use or understand or whatnot.
[2203.02 --> 2206.48]  And so we need the people to help train and onboard, right?
[2206.52 --> 2208.38]  And that is exactly where Johnny sits.
[2208.78 --> 2212.62]  And it's just as important, if not just as important as the code.
[2212.74 --> 2214.08]  And it's same with you, Mark.
[2214.20 --> 2219.32]  Like the fact that you go around and in-person training, and you also try to scale that by doing
[2219.32 --> 2224.52]  go for guides with Corey, yeah, those are absolutely vital contributors.
[2224.56 --> 2227.10]  And they're just as vital as the people who commit code.
[2227.98 --> 2229.18]  Oh, I couldn't agree more.
[2229.28 --> 2233.02]  I just like the idea of open source community maintainer or something.
[2233.56 --> 2236.10]  The title kind of just jumped into my head.
[2236.18 --> 2240.34]  But yeah, I mean, you know, open source, you know, I've been talking about open source
[2240.34 --> 2242.46]  from a coding perspective most of the episode.
[2242.66 --> 2246.76]  And, you know, I just kind of realized, yeah, there's more to it than, yeah, I kind of just,
[2246.76 --> 2250.90]  I've known this for 20 years, but in terms of this conversation.
[2251.58 --> 2253.66]  So Johnny, unpause, keep going.
[2253.90 --> 2257.14]  You're, you know, after Carmen said all his wonderful things about you.
[2257.40 --> 2257.82]  I know, right?
[2257.90 --> 2258.40]  Thank you, Carmen.
[2258.76 --> 2259.80]  That was very nice of you.
[2260.16 --> 2261.34]  It's her birthday too.
[2261.44 --> 2262.46]  You wouldn't even sing to her.
[2262.50 --> 2262.78]  Go on.
[2262.86 --> 2263.66]  I know, I know.
[2263.78 --> 2265.48]  Yeah, I might have to rectify that whole singing thing.
[2267.12 --> 2268.26]  You've got a lovely voice.
[2268.60 --> 2272.32]  Well, I mean, that's the beauty of community, right?
[2272.36 --> 2274.00]  There are many, many ways.
[2274.00 --> 2276.70]  If you look, you will find ways to contribute to your community.
[2276.92 --> 2277.78]  It could be code.
[2278.06 --> 2280.08]  It could be organizing, you know, a meetup.
[2280.14 --> 2281.94]  It could be, you know, helping out at conferences.
[2281.94 --> 2287.06]  It could be just bringing together, you know, like pointing newbies, right, to the community
[2287.06 --> 2287.80]  in the right direction.
[2287.88 --> 2292.98]  There are lots and lots and lots of ways to actually contribute to a community that basically
[2292.98 --> 2295.70]  has nothing to do with actually contributing code.
[2295.84 --> 2297.40]  That's precisely why I did it.
[2297.40 --> 2302.10]  Because I found myself in a position where I was like, man, like, I really want to, like,
[2302.10 --> 2303.38]  be of help.
[2303.48 --> 2305.04]  I really want to contribute something.
[2305.44 --> 2312.40]  But, you know, call it luck or being unlucky, whatever the reason is, you know, every company
[2312.40 --> 2318.50]  I've worked at, basically, they haven't had sort of a strong sort of a feel for contributing
[2318.50 --> 2323.76]  code back to, you know, the community, right, in which we, basically, of the software, the
[2323.76 --> 2324.72]  technologies that we use.
[2324.72 --> 2329.78]  So, basically, I found myself in a position where I'm like, like, how can I, like, make
[2329.78 --> 2330.32]  a contribution?
[2330.48 --> 2332.68]  How can I give back, right, in some way?
[2333.00 --> 2337.12]  And the best way I could find without actually doing code was to get involved in community
[2337.12 --> 2337.86]  organizing, right?
[2337.94 --> 2341.86]  It was to get involved and actually help other people who maybe are in a position to contribute
[2341.86 --> 2343.22]  code to actually do that, right?
[2343.46 --> 2345.56]  There's something about bringing people together, right?
[2345.74 --> 2348.20]  And it's something I completely stumbled upon, right?
[2348.22 --> 2349.80]  I didn't know what it was.
[2349.80 --> 2354.64]  I didn't have any preconceived notions about it, but, you know, organize, bringing people
[2354.64 --> 2359.02]  together and actually seeing sparks fly, like, really, like, seeing people get together and
[2359.02 --> 2364.38]  talking about ideas and working together and pairing on some stuff or learning about some
[2364.38 --> 2364.48]  stuff.
[2364.56 --> 2370.36]  I mean, in that room, you bring people together and it's magical.
[2370.62 --> 2374.04]  And if you know what to look for, you can actually witness, like, almost like a miracle
[2374.04 --> 2374.70]  happen, right?
[2374.72 --> 2379.62]  Of collaboration, of people getting to know each other, of people sort of making long, like,
[2379.62 --> 2381.88]  long-lived friendships, right, from these events.
[2382.08 --> 2387.28]  I mean, I've learned to look for these things and I enjoy every moment of it, every event,
[2387.40 --> 2390.48]  every meetup, every conference I've ever been a part of and helped organize.
[2390.82 --> 2394.38]  Like, I look for these things and I can guarantee, I see it every time.
[2394.46 --> 2395.84]  There's something beautiful about that.
[2396.02 --> 2400.60]  That's, to me, that's the way I've been able to contribute and have an impact where,
[2400.72 --> 2405.08]  you know, that perhaps I don't even know, but I could maybe never have if I was just
[2405.08 --> 2405.72]  contributing code.
[2405.96 --> 2408.04]  Sorry, Johnny, your mic was off during all that.
[2408.12 --> 2408.80]  Can you repeat that?
[2409.62 --> 2411.10]  You even got jokes.
[2411.12 --> 2412.74]  You are such a troll.
[2412.88 --> 2413.90]  You are awful.
[2414.32 --> 2414.92]  I'm terrible.
[2415.44 --> 2418.74]  No, what you say is 100% correct, though.
[2418.88 --> 2421.16]  It is an amazing experience to say, though.
[2421.46 --> 2422.38]  It really is.
[2422.74 --> 2425.48]  We are so lucky to have you in our community.
[2425.66 --> 2426.50]  That's all I have to say.
[2426.76 --> 2428.38]  Like, because of all of this.
[2428.44 --> 2430.84]  Like, I wish I could clone a thousand of you, Johnny.
[2431.62 --> 2434.24]  Yeah, but we wouldn't be able to find that many MC Hammer pants for him.
[2436.48 --> 2436.88]  False.
[2436.96 --> 2438.02]  Don't put rumors out there.
[2438.02 --> 2440.54]  I can't even remember if that was on the air or not.
[2440.68 --> 2441.82]  It wasn't on the air.
[2441.98 --> 2443.24]  So we're going to have to strike it.
[2443.56 --> 2444.56]  Strike that from the record.
[2444.76 --> 2445.04]  From the record.
[2445.12 --> 2446.16]  Strike that from the record.
[2447.58 --> 2452.82]  If you want to know more about MC Hammer pants, hit us up in the GoTime FM channel and
[2452.82 --> 2453.16]  we'll tell.
[2453.40 --> 2455.80]  No, hit Carmen up in the GoTime channel.
[2455.90 --> 2459.42]  I'm not going to be answering questions about MC Hammer pants for the rest of the afternoon.
[2459.78 --> 2461.36]  Talk to Mark about his pants.
[2461.60 --> 2462.54]  Mark, do you still have your pants?
[2462.62 --> 2463.40]  Your MC Hammer pants?
[2463.40 --> 2464.78]  Yes, never mind.
[2465.36 --> 2467.32]  That was going to go somewhere it probably shouldn't have.
[2467.42 --> 2470.92]  Okay, so, you know, these are all wonderful things.
[2471.00 --> 2480.74]  And we've talked about a variety of different ways that we think about open source, that we interact with open source from legal, security, maintaining users, community, that sort of stuff.
[2480.74 --> 2489.96]  This episode is brought to you by GoCD.
[2490.34 --> 2497.54]  With native integrations for Kubernetes and a helm chart to quickly get started, GoCD is an easy choice for cloud native teams.
[2498.06 --> 2505.54]  With GoCD running on Kubernetes, you define your build workflow and let GoCD provision and scale build infrastructure on the fly for you.
[2505.54 --> 2521.38]  GoCD installs as a Kubernetes native application, which allows for ease of operations, easily upgrade and maintain GoCD using helm, scale your build infrastructure elastically with a new elastic agent that uses Kubernetes conventions to dynamically scale GoCD agents.
[2521.84 --> 2529.48]  GoCD also has first class integration with Docker registries, easily compose, track, and visualize deployments on Kubernetes.
[2530.02 --> 2533.02]  Learn more and get started at gocd.org slash kubernetes.
[2533.02 --> 2535.66]  Again, gocd.org slash kubernetes.
[2544.54 --> 2558.98]  Let's talk, or let's spend kind of the last few minutes or last 15 minutes here talking about that very recent blog post that came out where the opinion was that Go is Google's language and it's not ours.
[2558.98 --> 2562.30]  That Go is not a true open source language.
[2562.42 --> 2565.06]  It just happens to have its source open.
[2565.76 --> 2573.78]  And that Google makes all the decisions and he pointed to modules as kind of the big example of all that.
[2573.90 --> 2578.40]  So I think that fits in with a subject matter on open source.
[2579.56 --> 2583.92]  Since they're decidedly saying that Go is not open source.
[2583.92 --> 2589.38]  So I'm going to turn this, I guess, over to you, Carmen, since you're either Go representative, right?
[2589.44 --> 2590.04]  Is it true?
[2590.52 --> 2592.66]  Is this salacious report true?
[2593.06 --> 2599.20]  Is Google, you know, is Go's Google language language or is it the communities or is it both?
[2599.20 --> 2604.46]  I think it's kind of a very interesting question to answer, right?
[2604.80 --> 2606.14]  I assumed it would be.
[2606.36 --> 2615.16]  If you think about open source as you think about a democracy, right, there's still representative democracy, right?
[2615.26 --> 2624.54]  And I sort of think of the people who are the core team of Go, that yes, they are all employed by Google.
[2624.54 --> 2635.62]  But does that mean that they – so I think that the person that wrote the article wanted to sort of make the connection that what Google wants is what they're going to make Go do.
[2635.98 --> 2637.34]  I think that's the essence, maybe.
[2637.92 --> 2643.90]  I think that Google does not influence what the Go core team wants, right?
[2643.98 --> 2646.76]  And I think that that is always going to be the case.
[2647.14 --> 2652.54]  I also think that, you know, Go is a useful language, but it also is a key piece of software infrastructure.
[2652.54 --> 2661.18]  And as a result, there's always going to be – and I think this is the true for whether you're talking about other key pieces of software infrastructure or other languages.
[2661.52 --> 2665.02]  There's always a small group that are the key deciders.
[2665.66 --> 2673.62]  And I think that the conversation is talking about the difference between this democracy or open source and what we call like open governance, right?
[2674.16 --> 2678.36]  And Go is open source, but the governance is indeed at Google.
[2678.36 --> 2686.82]  And this compares to something like – I would think about things like – I guess Kubernetes is a good example, right?
[2687.00 --> 2688.14]  It's both open source.
[2688.88 --> 2699.72]  And in a way, it's being moved away from Google to a governance model that is CNCF, which is the Cloud Native Computing Foundation, right?
[2699.72 --> 2709.38]  So, you know, should go move to maybe the Cloud Native Computing Foundation and the way that Python is and the Python Foundation or C++ is, maybe.
[2709.68 --> 2720.86]  But I still think that, you know, for the last 10 years or 12 years that the language has been alive, I think that the people who – we kind of want to focus on the individuals, right?
[2720.86 --> 2725.86]  And so those are the three founders, which are Robert and Rob and Ken.
[2726.28 --> 2732.74]  And then, of course, the people who joined the project shortly after, people like Ian Lance Taylor and then, of course, Russ, who came on as tech lead.
[2732.84 --> 2736.16]  And then people who have been working in the garbage collector and the compiler and the tooling.
[2736.34 --> 2739.00]  And I just met all of these people last week.
[2739.10 --> 2743.36]  We were at our annual Go team, annual planning.
[2743.36 --> 2761.16]  I think that it was quite eye-opening for me having just joined Google and finally meeting these people in person to see just how much they care to get it right and how much they care to make sure that the responsibility that they have, that the changes that they make are going to be the changes that you use going forward.
[2761.34 --> 2764.92]  I just wish people were in the room that I was in to sort of see this.
[2764.92 --> 2767.32]  But, yeah, indeed, very much.
[2767.42 --> 2773.04]  I believe that every successful software project has a small set of final deciders, right?
[2773.36 --> 2779.58]  But I don't think it's a true, like, sort of free-for-all, everyone can have a voice.
[2779.72 --> 2782.50]  It is more of a representative democracy, right?
[2782.68 --> 2783.90]  But it's still a democracy.
[2784.36 --> 2787.20]  And I think that that is kind of what I think is going to be the issue.
[2787.30 --> 2791.64]  And I think that we've had the history of modules as I saw it.
[2791.64 --> 2795.60]  So I was not a part of the Go team at that point, but I was kind of on the outside looking in.
[2796.12 --> 2799.60]  Gosh, just a lot of misunderstandings on a lot of sides.
[2799.60 --> 2806.20]  And the misunderstanding stemmed from expectations and this kind of, like, quid pro quo of how things were done in other ways.
[2806.28 --> 2812.40]  And it just highly reminds me of, you know, what my reality is may not match your reality.
[2812.40 --> 2815.74]  And what I think I'm saying is not what you're thinking I'm saying.
[2815.86 --> 2820.00]  And it was, like, kind of this mind-bending thing that happened with modules.
[2820.00 --> 2828.30]  So I want to get back to modules in a minute because I think there's more to it than just the rollout of modules.
[2829.34 --> 2832.04]  But, Johnny, I mean, what's your take on this article?
[2832.16 --> 2833.42]  I'm sure you have an opinion.
[2833.80 --> 2834.96]  I'd love to hear it.
[2835.42 --> 2835.72]  Yes.
[2836.74 --> 2839.30]  It's not a strong opinion, though.
[2839.30 --> 2850.42]  So because the reason I say that is because, like Carmen, I do believe there must be, like, a strong governance, right, around a project.
[2850.52 --> 2854.72]  Otherwise, it becomes, you know, too many things to too many people.
[2855.00 --> 2860.98]  And it sort of loses its stress, right, because it's trying to be too many things and trying to do too many things.
[2861.48 --> 2864.60]  And I think that's really true of everything in the world.
[2864.60 --> 2867.66]  We tell people, like, hey, stop spreading yourself so thin.
[2867.86 --> 2868.96]  Like, be focused, right?
[2869.06 --> 2871.02]  So I think it goes a very focused language.
[2871.34 --> 2885.76]  And because of that, it requires sort of a focused team, a focused leadership team around what should be in there in order to keep it true to its essence and what should be and what basically can be sort of worked around or what things shouldn't be in there at all.
[2885.86 --> 2887.20]  So it's the same.
[2887.54 --> 2892.30]  You know, I could extend that whole thing to arguments around features of the language.
[2892.30 --> 2893.74]  You know, hey, we should have this.
[2893.74 --> 2895.60]  Why doesn't the language have this and that and the other?
[2896.08 --> 2900.72]  I mean, these are all, you know, fine opinions and, you know, everybody can have one.
[2900.78 --> 2901.14]  It's okay.
[2901.70 --> 2912.36]  But I think at the end of the day, you know, I think I'm willing to put my trust in the team that brought the language this far, you know, after so many years, you know, 12 plus years.
[2912.36 --> 2920.32]  I'm willing to trust that they will sort of keep the community's needs at heart and their decision making.
[2920.32 --> 2921.76]  Because guess what?
[2922.18 --> 2927.90]  If you don't like the language, if you don't like the community, you are free to not use it.
[2928.14 --> 2929.34]  You are free to leave.
[2929.44 --> 2933.44]  Nobody is forcing you, right, to be part of this or to use it.
[2933.98 --> 2935.82]  You have that freedom, right?
[2935.82 --> 2946.08]  So for those of us who are sort of who are okay, again, I'm not saying that, you know, the again, to use the module rollout thing as an example.
[2946.08 --> 2948.82]  I'm not saying, you know, we get it perfectly.
[2948.92 --> 2951.08]  I'm not saying that the Go team always gets it perfectly.
[2951.20 --> 2951.92]  Nobody can.
[2952.18 --> 2952.34]  Right?
[2952.40 --> 2952.92]  We're people.
[2953.12 --> 2956.30]  So there's going to be ways things could have gotten better.
[2956.46 --> 2956.52]  Right?
[2956.58 --> 2957.42]  It's always 2020.
[2957.42 --> 2963.70]  But I think the bottom line is I trust the Go team to have the community's best interests at heart.
[2964.24 --> 2965.34]  You know, I brought it out.
[2965.40 --> 2967.00]  I think because I thought it was an interesting article.
[2967.00 --> 2968.08]  And I'm not going to lie to you.
[2968.10 --> 2973.00]  A lot of what was said in that post rang true with me.
[2973.30 --> 2978.90]  A lot of the things that were discussed in there have happened to me.
[2978.90 --> 2988.14]  Um, the big difference I feel between myself and the poster of that blog post whose name I can't recall off the top of my head.
[2988.48 --> 2996.58]  Um, it seemed as though it came as a revelation to them that Google is behind this language very recently.
[2996.58 --> 3006.10]  Whereas for me, I, when I got into the language, you know, six, seven years ago, um, you know, it was Go 1-2 and it was from Google.
[3006.10 --> 3009.02]  And in my mind, it has always been Google's language.
[3009.12 --> 3011.52]  It wasn't even on GitHub, mirrored on GitHub at the time.
[3012.16 --> 3018.16]  Um, so for me, you know, I, I do think they care about the community and I know that because I know a lot of the core team.
[3018.68 --> 3029.10]  Um, but I do think that in the, historically in the past, it has been very Google driven or at least appeared to be Google driven by the Go team, if that makes sense at all.
[3029.10 --> 3037.22]  I think that the, the, um, the driven by the Go team were actually the set of constraints that were happening at Google at the time.
[3037.30 --> 3037.70]  Right?
[3037.82 --> 3041.44]  So Go, their source code is a big, huge monorepo.
[3041.44 --> 3041.52]  Go.
[3042.00 --> 3051.86]  And the build system is kind of one, the reason why they decided to re, you know, kind of invent Go in the first place because C++ build times were just super long.
[3052.24 --> 3059.76]  But, um, the fact that they had such a good, um, infrastructure that now of course is open source in the form of Kubernetes via Borg and whatnot.
[3059.92 --> 3065.58]  That also, um, is part of the reason why they didn't understand the need for dependency management.
[3065.58 --> 3065.94]  Right?
[3066.32 --> 3068.44]  They didn't, they couldn't kind of foresee it.
[3068.44 --> 3069.76]  And so that wasn't malicious.
[3070.04 --> 3071.20]  It wasn't maliciously done.
[3071.28 --> 3072.46]  It was simply a blind spot.
[3073.00 --> 3075.42]  Oh, I don't think anybody would say that that was maliciously done.
[3075.52 --> 3077.12]  So let's talk about modules.
[3077.24 --> 3078.54]  It's the elephant in the room.
[3078.58 --> 3080.88]  I think we keep, we keep dancing around it here.
[3081.28 --> 3090.92]  Um, you know, we, I think the rollout of modules has been discussed to death and I don't really want to talk about Sam and Russ and who said what, when.
[3090.92 --> 3101.88]  Um, I think, you know, at least in my opinion, what that article was saying was more the actual implementation of that package management came from Russ.
[3102.14 --> 3109.56]  Uh, it was kind of thrown out there and the community felt as though they had been kind of, okay, we're, we're put on this path now.
[3109.56 --> 3112.68]  Um, and there's still a lot of problems with them.
[3112.74 --> 3121.80]  They're still early, but we, you know, I, I know a lot of community feels that it's being moved too fast, uh, against, you know, people saying that we've got all these issues.
[3121.80 --> 3132.18]  Um, you know, I saw Corey Lanoue tweeted, I think yesterday that, uh, he's loves go, but he's keeps running to all these module issues like every day and it's really driving him crazy.
[3132.70 --> 3134.58]  Um, and I think that's what they're talking about.
[3134.64 --> 3141.98]  They're talking about the fact that an implementation of something as important as package management was done by the go team.
[3142.10 --> 3145.94]  Uh, I'm not even going to say by Russ, you know, by the go team just as a whole.
[3146.42 --> 3151.62]  Um, cause I don't think Russ, you know, I think Russ is a great guy and I don't besmirch him what he came up with.
[3151.80 --> 3158.24]  Um, but as the team kind of came out with this thing and the community was just told this is what it's going to be.
[3158.64 --> 3161.62]  Um, and that's, that's hard for us.
[3162.04 --> 3164.16]  You can imagine how that feels to us as a community.
[3164.16 --> 3181.66]  So it wasn't just the, you know, who said what, when part of it, we've got this solution in place that, you know, those of us writing large scale packages and applications are, are feeling the burn, uh, on some of those decisions that we didn't necessarily want.
[3181.66 --> 3188.76]  Or asked for, um, the downloading the internet problem, for example, um, where it's very possible to just download.
[3189.44 --> 3193.00]  It's many, many, many more packages than you actually want.
[3193.46 --> 3196.30]  Um, just because you can have all the different revisions in there.
[3196.30 --> 3204.76]  Um, so I think that's what the article was talking about was that feeling of the Go team said, this is it.
[3204.78 --> 3206.70]  We're going to, we're going to do it now, you know?
[3206.70 --> 3213.42]  Um, and I think, you know, so how is the Go team planning on addressing that feeling that's coming out of this sort of article?
[3213.42 --> 3214.48]  Well, they've listened.
[3214.96 --> 3221.06]  And so what was going to be modules shipped in Go 113 in August is now no longer the case.
[3221.68 --> 3226.98]  And so they're going to take a step back and let people, you know, find ways to help more people migrate.
[3227.24 --> 3231.96]  And then they can revisit it for a possible 114 ship, which is in February.
[3232.40 --> 3232.86]  Right.
[3232.92 --> 3234.94]  So that's a stay of execution, if you will.
[3234.94 --> 3238.66]  Uh, Justin Liggett just recently put Kubernetes on modules.
[3238.84 --> 3245.84]  And I think that was a milestone moment to show like big projects that needed some sort of solid dependency management solution did it.
[3246.06 --> 3248.98]  And I kind of want to evangelize how they did it.
[3249.04 --> 3250.48]  Because of course it wasn't going to be easy.
[3250.58 --> 3253.26]  And it's not going to be like one, two, three, this is how we did it.
[3253.28 --> 3256.08]  It did take some real research to get it right.
[3256.22 --> 3257.18]  But they did get it right.
[3257.26 --> 3258.28]  And I think that was a win.
[3258.40 --> 3261.70]  Because I think the rest of us, what we're looking for is, well, how does it look like?
[3261.72 --> 3262.56]  And how did you do it?
[3262.60 --> 3263.60]  And how can you help me?
[3263.60 --> 3265.52]  Because it's hard to really get it right.
[3265.90 --> 3270.40]  And especially when you're a moving target and the packages that you depend on are moving targets.
[3271.18 --> 3273.62]  And so I think that Go, first of all, listened.
[3273.76 --> 3277.52]  And now they're saying, yeah, let's just take some time and let them live side by side.
[3277.68 --> 3279.34]  Both whether you want to use the module.
[3279.90 --> 3282.10]  Modules or whether you want, don't want to use them.
[3282.38 --> 3284.96]  And so that's going to live side by side as a choice.
[3285.20 --> 3288.50]  Rather than putting it on as the default option in 113.
[3288.72 --> 3291.46]  And I don't know if enough of that was published or not.
[3291.46 --> 3294.08]  I'll share the issue where that was announced.
[3294.26 --> 3295.74]  And that was relatively recent.
[3295.98 --> 3296.86]  I think there's that.
[3296.96 --> 3299.66]  And I think that the Go team is thinking a lot about that.
[3299.70 --> 3300.64]  And they want to get it right.
[3300.72 --> 3302.42]  And they want to listen to the community.
[3302.68 --> 3303.04]  So yeah.
[3303.22 --> 3308.22]  And I think it's one of those things where, gosh, you know, they spent so much time thinking about.
[3308.70 --> 3311.94]  Because when you really think about that, this isn't the sort of standard library.
[3312.16 --> 3314.42]  This is kind of a workflow, a tooling problem.
[3314.42 --> 3321.68]  And that's kind of where I'm not sure if non-modern day programming languages really cared about workflow or tooling, right?
[3321.76 --> 3326.22]  That's another inflection point of what it means to develop a programming language in 2019.
[3326.62 --> 3329.30]  In their most recent years when we live in a distributed world.
[3329.96 --> 3330.18]  You know?
[3330.32 --> 3334.50]  Otherwise, that packaging was done via, like, gosh, CD-ROM back in the day.
[3334.50 --> 3340.34]  And now it's really kind of like, well, and you have to be very, very careful about kind of the libraries that you imported and whatnot.
[3340.46 --> 3346.38]  And it kind of harkens back to the beginning of the episode, which is how do you trust what you bring in is really going to be safe?
[3346.82 --> 3350.42]  And now it's like, how do I trust all these dependencies, dependencies?
[3350.78 --> 3356.38]  When I just, we've moved faster than we ever had before because we can build on the shoulders of giants.
[3356.38 --> 3359.46]  But how do we make sure that these giants aren't really, you know, trolls?
[3359.46 --> 3368.40]  So, yeah, I think that that is something that is, I think, just going to be an interesting when you kind of look at it from, like, the historical lens.
[3368.58 --> 3370.04]  Like, this is an interesting problem.
[3370.18 --> 3372.16]  And I think Go really deeply cares.
[3372.42 --> 3377.88]  And, you know, we have probably another eight months to kind of think about it.
[3377.94 --> 3381.36]  And if the community, and they're continuing to keep their ear to the ground of the community.
[3381.36 --> 3385.10]  If they feel like the community is still saying, uh-uh, this is too hard.
[3385.22 --> 3387.12]  I'm just, you know, my workflow is broken.
[3387.36 --> 3388.04]  It's been broken.
[3388.04 --> 3389.88]  I just want to be productive again.
[3389.96 --> 3390.86]  This is really painful.
[3391.52 --> 3392.30]  They'll stay okay.
[3392.40 --> 3393.54]  Let's give a stay of execution.
[3393.64 --> 3397.18]  And I think all open source projects have been, have kind of felt that.
[3397.26 --> 3403.08]  And if you look at, like, the canonical model for Ubuntu long-term support, that was an interesting history, right?
[3403.22 --> 3408.38]  Like, I remember when, oh, God, it was precise, was going end of life.
[3408.38 --> 3422.68]  But it was a shock to have some people who are super, like, early adopters see that so many enterprises were depending on end of life, like, to be, like, not just five years, but rather, like, eight or nine years, right?
[3422.68 --> 3428.88]  And people were like, well, why can't you just, like, you know, rebuild for, you know, a new version of Ubuntu?
[3429.28 --> 3432.82]  And so many enterprises had to kind of go into why not.
[3432.94 --> 3442.22]  And I think that we're kind of getting the same lesson learned here for not necessarily the runtime version, but the tooling.
[3442.22 --> 3444.52]  Johnny, you've been quiet for a while.
[3445.28 --> 3450.12]  Yeah, so that's because I usually make sure that whatever I have to say is not better left unsaid.
[3451.10 --> 3451.82]  Fair enough.
[3453.28 --> 3455.84]  Do you have anything you'd love to say on the subject?
[3456.54 --> 3461.24]  Well, this whole time that you were having this, you and Carmen was going back and forth.
[3461.24 --> 3466.16]  I kept thinking that if the module rollout has gone out smoothly, I don't know.
[3466.30 --> 3468.60]  I don't think we'd be having this debate.
[3468.72 --> 3469.86]  I don't think we'd be having this discussion.
[3469.86 --> 3477.72]  I think it's very easy to sort of look at things that have some friction in them and some point blame and find blame, right?
[3477.84 --> 3484.02]  It's like my, I guess my personal approach, right, to, especially because we're talking about open source, right?
[3484.02 --> 3494.30]  My personal approach to open source software is that I expect that there will be some things that don't work perfectly for me, right?
[3494.36 --> 3495.96]  But my definition of perfect is, right?
[3495.96 --> 3501.26]  I expect that some things will not always work, that I may have to troubleshoot.
[3501.26 --> 3510.76]  I expect that some things will not always be smooth, that I may have to come up with some solutions, some instrumentation around some of the problems while issues get fixed.
[3511.08 --> 3518.82]  There are certain expectations that I bring with me when I'm bringing open source software or open source tooling or programming languages.
[3518.82 --> 3521.18]  Like I know everything is a trade-off, right?
[3521.48 --> 3534.96]  So that is why, like I said before, my opinion is not basically ironclad on this because I understand that the team is trying to do, the Go team is trying to do sort of the right thing for the community in the long haul.
[3534.96 --> 3547.34]  Right now we're having a bit of pain and the whole dependency sort of management thing has always been, you know, painful for Go because again, when the language was created, that wasn't sort of the, at the forefront, right?
[3547.42 --> 3549.52]  Of, of sort of the concerns, right?
[3549.56 --> 3550.54]  For rolling out the language.
[3550.76 --> 3552.78]  So we're dealing not with it now.
[3553.06 --> 3554.46]  We, you know, things will be bumpy.
[3554.46 --> 3555.36]  Things will be rough.
[3555.36 --> 3569.52]  And I, as a, as a user of the language, as a, as a, as a participant of this, in this community of this, of this technology platform, like I understand that and I'm willing to be patient and wherever I can, I'm willing to contribute, right?
[3569.52 --> 3570.40]  To make it better.
[3570.40 --> 3574.50]  And, and I have less sort of a, overall, I have less complaints about things.
[3574.50 --> 3576.80]  I suppose that's why I'm, that's, that's, that's my approach.
[3576.88 --> 3579.92]  That's my stance, generally speaking, when I, when it comes to open source software.
[3580.30 --> 3581.58]  I love you, Johnny.
[3581.74 --> 3582.62]  I really do.
[3582.62 --> 3584.84]  You, you're just so positive and upbeat.
[3584.96 --> 3586.36]  You're just an amazing person.
[3586.48 --> 3587.02]  You really are.
[3587.10 --> 3587.98]  No, I mean that.
[3588.08 --> 3588.22]  I do.
[3588.34 --> 3589.94]  Like Carmen was gushing on you earlier.
[3589.98 --> 3591.18]  I'm going to gush on you now.
[3592.14 --> 3592.54]  Okay.
[3592.68 --> 3593.58]  Well, you know what, kids?
[3593.82 --> 3595.78]  We're getting near the end of the show here.
[3596.08 --> 3597.48]  You know what the music means.
[3598.06 --> 3609.52]  So since we're talking about open source, I just want to ask each of you real quick, give me an open source project you're, you're kind of playing with these days or kind of smitten with or just find really interesting right now.
[3609.82 --> 3610.92]  Johnny, you, you first.
[3610.92 --> 3613.70]  Ooh, let me see.
[3614.48 --> 3621.92]  I've been, well, a lot of the services I've, I've, I've currently working in a microservices architecture.
[3622.90 --> 3631.42]  Basically, basically we have a ton of microservices doing a lot of different things within, within our, basically our ecosystem of, of, of applications.
[3631.42 --> 3644.10]  And the, would the project I use, um, as basically two projects I use, um, quite frequently in these, in, in, in sort of the, in building in these components is basically the echo from lab stack is a sort of a nice router.
[3644.10 --> 3645.90]  I've used that for, for years now.
[3645.90 --> 3651.78]  And it's, you know, nine, it covers 99% of my use cases and every now and then there's something, something odd.
[3651.88 --> 3654.28]  And I kind of have to, you know, see why it does what it does.
[3654.46 --> 3655.56]  Again, it trade offs, right?
[3655.56 --> 3662.88]  If it, if it, if it, if it, if it's a benefit to me, 99% of the time, I'm not going to, you know, ding it for, and it doesn't do something like an edge case and whatnot.
[3662.88 --> 3666.90]  Um, but, uh, also using a gorilla mux, um, for, for a lot of that stuff too.
[3667.34 --> 3671.14]  Um, and I've actually, um, been, started using more and more of a, um, gRPC.
[3671.38 --> 3677.32]  So these projects are, are basically my sort of my bread and butter, um, for the kind of, kind of work I'm doing right now.
[3677.32 --> 3679.52]  So a big shout out to the maintenance of those projects.
[3680.16 --> 3683.94]  I, it's already been a show, but of course I give love to Athens.
[3683.94 --> 3692.62]  I just think it's both an interesting, um, way to enrich the ecosystem, but also just how they are so welcoming to open source people.
[3692.88 --> 3694.56]  Um, and of course Kubernetes.
[3694.86 --> 3701.88]  I mean, it's, I wish I could have, um, thought about that a little bit more so it gives some love to some open source projects that need some more discovery.
[3702.56 --> 3710.20]  Uh, you know, because there's certainly a lot out there and the ones that are out there are really the ones that do kind of like the Unix philosophy, right?
[3710.22 --> 3712.56]  They might do one thing, but do one thing really well.
[3712.66 --> 3718.14]  So maybe some of these web router libraries, because, you know, the standard library doesn't have one.
[3718.24 --> 3719.34]  I won't, I won't.
[3719.34 --> 3732.46]  But yeah, but the fact that they're out there and that they kind of are trying to solve a problem that the standard library has said rightly so, I think, rather than focus on an implementation, just say, you know, let's let third party libraries do it.
[3732.60 --> 3737.22]  And so I just really like any kind of those kinds of libraries where I'm reaching for again and again.
[3737.22 --> 3738.18]  All right.
[3738.32 --> 3740.50]  I want to give a shout out to both.
[3740.68 --> 3747.52]  I've already done it once, the Buffalo Corps team, but also everybody who's contributed to any of my projects over the years.
[3747.60 --> 3749.28]  I don't care what language it was in.
[3749.36 --> 3750.22]  Thank you so much.
[3750.94 --> 3755.68]  Hopefully it was, uh, hopefully I was nice to you and I thank you so much for all your contributions.
[3755.68 --> 3762.10]  Uh, the one thing I will, I, I'm going to throw out is a project called Pigeon, uh, which is not one of mine or Buffalo's.
[3762.16 --> 3770.82]  It's, uh, works with parser expression grammars, um, which I have been playing a lot lately and they let you build your own little parsers and essentially little languages.
[3771.42 --> 3775.16]  Um, so Pigeon's the Go implementation on that and that's been pretty fun to play with.
[3775.26 --> 3777.38]  So if you're looking to do that, check that out.
[3777.38 --> 3785.46]  But anyway, uh, thank you so much to Johnny and Carmen and to Adam and the crew at Changelog and of course I'm Mark Bates.
[3786.00 --> 3787.06]  Why wouldn't I be?
[3787.56 --> 3794.30]  Um, saying be a good, be a good contributor, be a good community member, help your maintainers out.
[3794.60 --> 3795.50]  Thank you very much.
[3795.92 --> 3797.32]  And that's go time, everybody.
[3797.52 --> 3797.96]  Bye.
[3798.48 --> 3798.92]  Bye.
[3799.88 --> 3800.24]  Bye.
[3804.42 --> 3805.14]  All right.
[3805.14 --> 3807.74]  Thank you for tuning into this week's episode of go time.
[3807.88 --> 3810.28]  If you're not yet, hang with us and go for slack.
[3810.38 --> 3812.14]  We have a channel called go time FM.
[3812.58 --> 3813.28]  Look it up.
[3813.30 --> 3821.14]  You'll find us hang with us during the live shows, connect with other members of the community, share stories, share codes, share coffee recipes, whatever.
[3821.36 --> 3822.48]  It's a lot of fun.
[3822.66 --> 3826.58]  Also, we have discussions at changelog.com on every episode.
[3826.68 --> 3828.98]  Head to changelog.com slash go time.
[3829.08 --> 3831.68]  Find this episode and discuss it with the community.
[3831.68 --> 3836.24]  Of course, thank you to our sponsors, digital ocean roll bar and go CD.
[3836.24 --> 3841.80]  Also, thanks to fastly, our bandwidth partner roll bar for helping us move fast and fix things.
[3842.10 --> 3843.90]  And Linode for hosting the changelog platform.
[3844.50 --> 3847.26]  Our music is produced by the mysterious break master cylinder.
[3847.78 --> 3851.80]  And if you want to hear more awesome podcasts like this, subscribe to our master feed.
[3851.88 --> 3853.54]  It's one feed to rule them all.
[3853.78 --> 3856.18]  Plus some extras that only hit the master feed.
[3856.28 --> 3861.34]  Head to changelog.com slash master or search for changelog master in your podcast client.
[3861.42 --> 3862.10]  You'll find us.
[3862.40 --> 3863.26]  Thanks for tuning in.
[3863.48 --> 3864.30]  We'll see you next week.
[3864.30 --> 3865.30]  Bye.
[3894.30 --> 3895.30]  Bye.
[3895.30 --> 3896.30]  Bye.

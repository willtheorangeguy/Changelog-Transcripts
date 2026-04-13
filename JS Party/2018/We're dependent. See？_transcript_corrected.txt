[0.00 → 6.70] Bandwidth for Changelog is provided by Vastly. Learn more at Fastly.com. We move fast and fix
[6.70 → 11.42] things here at Changelog because of Rollbar. Check them out at Rollbar.com. And we're hosted
[11.42 → 17.10] on Linde servers. Head to linode.com slash Changelog. This episode is brought to you by
[17.10 → 21.82] Gauge. Gauge is a free and open source test automation tool by ThoughtWorks with a goal
[21.82 → 26.42] of taking the pain out of test automation for acceptance tests. To help with this,
[26.42 → 30.60] Gauge supports specifications and markdown, which are easy to read and easy to write.
[30.96 → 36.48] Reusable specifications to simplify your code, which makes refactoring easier and less code
[36.48 → 42.78] means less time maintaining your code. And finally, integration. Use Gauge with your favourite tools
[42.78 → 50.38] and IDEs in the ecosystem of your choice, like Selenium and Sari Pro. CI and CD tools like Good,
[50.38 → 56.22] Jenkins, Travis, and IDE support for Visual Studio, VS Code, IntelliJ, and more.
[56.42 → 63.92] Head to gauge.org slash JS Party to learn more and give it a try. Once again, gauge.org slash JS Party.
[63.92 → 82.62] Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays
[82.62 → 89.14] at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live. Join the community and slack with us
[89.14 → 94.18] in real time during the show at changelog.com slash community. Follow us on Twitter. We're at
[94.18 → 96.74] JSPartyFM. And now on to the show.
[99.52 → 105.68] Welcome to JS Party. Thank you for joining us on this lovely Thursday afternoon or morning,
[106.12 → 111.46] depending on where you are. Today's topic is going to be fascinating, and it's a little bit of
[111.46 → 117.26] a follow-up on last week's topic. We're going to be talking about third-party and open-source
[117.26 → 122.70] dependencies. You know, how do we use them? When do we use them? And how do we support the ecosystem
[122.70 → 131.42] of open-source dependencies? Joining the conversation today, we have myself, Safia, Chris, Nick, and Kevin.
[131.70 → 135.86] How are you all doing? Good. Wonderful. Super. I guess I'm supposed to say terrific.
[135.86 → 141.70] True. We could just get all the adjectives out there. Throw in a supercalifragilisticexpialidocious
[141.70 → 148.70] too. Is that an adjective or a noun? Would I say I'm having a supercalifragilisticexpialidocious day?
[148.98 → 154.20] I think it's a flexible word. I think it is both an adjective and a noun. It's quite atrocious.
[154.90 → 163.90] Oh boy. All right. So let's dive into today's conversation. So following some of what happened
[163.90 → 169.68] last week with the event stream debacle, a lot of people have been having discussions about
[169.68 → 175.62] supporting open-source using open-source. And I figured we would continue that conversation with
[175.62 → 180.46] a little bit of a focus on how we interact with dependencies as software engineers.
[181.32 → 186.60] So the first question that I'm really curious to know about from you folks is, how do you decide
[186.60 → 194.40] when to use a third-party dependency or library during your development process? What is the
[194.40 → 200.44] criteria in which you say, all right, it's time for me to bring in another library, something outside
[200.44 → 204.98] of my control into this code that I'm writing? We're talking JavaScript, right? So the answer is,
[205.02 → 209.56] does a package exist? I mean, that's our approach, right?
[209.58 → 213.92] This is JavaScript, but if you're working in ecosystems that are, you know, like Java or Ruby,
[213.92 → 219.84] feel free to bring in those discussions as well. I'd be curious to know if this is like something
[219.84 → 226.50] language specific, if the environment and language you're working in kind of dictates the criteria
[226.50 → 233.92] that you use when selecting dependencies, because each programming language kind of has a different
[233.92 → 239.74] profile around like third-party dependencies and package management and stuff like that.
[239.74 → 241.64] But let's go with JavaScript for now.
[242.02 → 246.48] Well, it was a little bit of a tongue-in-cheek answer, but sort of saying, you know, in this
[246.48 → 252.98] ecosystem, the tendency is to always reach for a third-party package. And I suppose what you're
[252.98 → 257.92] highlighting is that that is probably not always and everywhere the right tendency. But I think it is,
[258.04 → 263.70] you know, something that is almost, you know, cultural more than anything is like different
[263.70 → 269.72] language ecosystems have different cultures about and different ease of installation, right? Like if it
[269.72 → 277.56] requires manually pulling things in and doing a local build as compared to a simple add align or do
[277.56 → 282.44] an NPM install save, like that's going to change how easy or hard it is. And that's going to
[282.44 → 285.60] dramatically lower the barrier to pulling dependencies in.
[286.06 → 288.02] Yeah, totally agree with you on that.
[288.38 → 293.74] I feel like I don't fit in because I don't like doing that. I don't like pulling in very small packages.
[293.74 → 299.28] I like pulling in bigger packages that I don't want to write or don't feel like I have the skills to
[299.28 → 303.94] write properly. So you'll never see me writing my own crypto or anything like that.
[304.46 → 313.88] But for small things like a simple, I don't know, custom filtering or custom like functional method
[313.88 → 318.40] for an array, I would probably just write that myself and then write tests for it.
[318.40 → 323.20] I'm curious to know, do you do that for things? One of the most common use cases for me for small
[323.20 → 329.76] packages is like trying to figure out if a string contains an email or a link or stuff like that.
[329.82 → 337.14] It's mostly like parsing and other mundane tasks that I don't have the patience to deal with.
[338.08 → 342.90] Does that fall under your criteria of things that you would write on your own or would you bring
[342.90 → 344.68] in a third party dependency for that?
[344.68 → 345.92] That's a good question.
[346.16 → 351.32] I would always bring in something or look for something. I mean, at the end of the day,
[351.34 → 360.46] if it's going to save me time, I'm probably going to go for it. I find I have the most success or I
[360.46 → 367.06] mean, maybe it's the other way around. I have the most failure when I try to implement something
[367.06 → 377.58] myself, which is, it turns out to be much more nuanced than I expected. And so like, for example,
[378.24 → 387.14] you know, getting an executable in the user's path, that is not always a straightforward
[387.14 → 394.28] thing to do. And so in that case, I'd want to pull in some package to do that for me because it's
[394.28 → 400.34] going to, you know, hopefully cover more edge cases and corner cases than I would have thought
[400.34 → 408.08] of. So yeah, the way I run into trouble is, is just trying to hand roll things that are
[408.08 → 412.74] just naively do it. You know what I mean? So, yeah.
[412.74 → 418.88] I guess I start from there, and I just naively do it and then use that as a learning experience. If I,
[419.24 → 425.20] like, if it does get more and more complex, then I will reach for something or look, look to see
[425.20 → 430.84] what's out there. But I don't know, I guess it's good that we have differing approaches to this.
[431.30 → 435.72] Chris, I think you brought up one of the key questions that I tend to ask myself when I'm
[435.72 → 442.24] looking at is how much time is this going to save? You know, is this something that is a really
[442.24 → 449.64] complex thing or is this something that is like a three-liner that I could also do myself?
[450.88 → 457.74] How close is the library to my desired behaviour, right? So like, if it's exactly what I need,
[457.92 → 463.16] that's going to save me a lot more time than something that I'm going to have to push and
[463.16 → 468.70] mould and move around and hack around often to get it to do what I want. And also how well
[468.70 → 474.38] supported is the library, right? Like if I run into an issue, is this something where if I file
[474.38 → 478.14] an issue, somebody is likely to fix it? Is it something where if I submit a pull request,
[478.28 → 483.06] somebody is likely to merge it? Or am I going to be, you know, having to, you know, if I run into
[483.06 → 487.92] issues, support my own different branches of this library to get it to work?
[488.26 → 493.22] Well, I mean, it seems like two different questions to me. One is, do you want to pull in
[493.22 → 498.52] some third-party dependency to solve this problem? If the answer is yes, then how do we choose which
[498.52 → 504.00] one? Because if you're looking at NPM, there's going to be 10 things out there that do roughly
[504.00 → 509.02] what you want. And so how do we, how do we pick them? You know, once you've decided to use a
[509.02 → 515.48] dependency, you know, what goes into that decision? And yeah, I definitely say, you know, for me,
[515.48 → 522.50] the major red flag is if I go and look at something and see, oh, this hasn't been updated in two years,
[522.62 → 531.26] forget it, you know, that's not going to fly. I'm going to want something that has, you know,
[531.34 → 538.72] recent, and depending on what kind of package it is, how recent. If it's more of a larger thing,
[538.72 → 544.60] I would want active development. If it's one of these tiny modules, you know, maybe something in the
[544.60 → 550.52] last six months, you know, that sort of thing. But yeah, there's a lot of, I mean, and then of
[550.52 → 555.96] course it depends, you know, what context you're doing this in. If you're doing it at work, if you're
[555.96 → 562.74] doing it in a like for a hobby project, et cetera, et cetera, where you work obviously has a lot to do
[562.74 → 563.36] with that as well.
[563.68 → 568.82] When it raises kind of an interesting question, when you talk about like maintainer ship is,
[568.92 → 572.90] and this is something that I think, like, frankly, I haven't thought about that much,
[572.90 → 578.08] but it's come up a lot recently, you know, with the event stream hack and other things is like,
[578.38 → 584.18] how do you determine which maintainers you can trust, right? Is this, you know, activity that's
[584.18 → 589.52] in the last six months, is that from the same people that we started this package? Or is that
[589.52 → 593.52] from somebody brand new who we don't know if they built up trust or not?
[593.82 → 599.82] That's tough too, because the like, it's just a rabbit hole of trust because the that project might
[599.82 → 604.72] rely on a project that brings in 10 other projects that brings in, you know, a hundred other projects.
[605.16 → 611.46] And can you trust all the way down? Do you trust everyone along that, that chain to, to have verified
[611.46 → 612.32] everything?
[612.88 → 619.56] I think a big part of bringing in third party dependencies is about risk management and how
[619.56 → 624.56] much risk you're willing to have in your application. Because I'm not going to say that
[624.56 → 629.74] we're going to live in a world where you get access to free open source packages that are always secure
[629.74 → 638.14] and mostly bug free with reliable and well-versioned APIs. Well, we might be able to, if people fund that,
[638.38 → 644.90] but we'll be discussing that later. So stay tuned. But yeah, I think a big part of it is just like,
[644.90 → 651.18] what are your organizations and your own like risk management techniques for a code base? Like
[651.18 → 656.68] one of the interesting things that kind of like struck me about the event stream issue.
[656.90 → 662.06] And I think a couple of other things is there's usually such a like a huge time span between
[662.06 → 668.50] when people realize that something fishy is going on. And then when it actually like becomes,
[668.50 → 674.08] um, I guess, mainstream news. So in the case of event stream, for example, there was like a
[674.08 → 680.82] five day gap between when somebody was like, seems like there's some malicious code in here.
[680.82 → 686.28] And when it was actually discovered, what the malicious code was and how it was impacting users
[686.28 → 694.10] and how it worked and all that. Um, and in those five days, there was like not a ton of engagement,
[694.10 → 701.62] at least not as much as there was after those five days. Um, and I found it kind of interesting that
[701.62 → 709.14] very few people who had like installed event stream or had it as a dependency were like watching the
[709.14 → 715.46] repository on GitHub. Admittedly, it can get a little noisy, but it's one of those things where I feel
[715.46 → 723.24] like for me as an open source maintainers, um, people's engagement with third party dependencies
[723.24 → 730.04] ends at install time. And they're not willing to participate in like technical discussions about
[730.04 → 736.18] the future of the project or just keep up to date on what's going on and, um, what's being merged,
[736.18 → 743.46] who's doing the merging and develop like a personal understanding of the project. Um, and I feel
[743.46 → 750.30] like that's the distinction between you installing a dependency and you're installing an open source
[750.30 → 755.72] packages. I do think you have to engage with the open source part of it to like be able to effectively
[755.72 → 757.48] use it in your own code.
[757.48 → 762.40] That sounds like a pretty big ask, especially when you look at the dependencies of dependencies issue,
[762.50 → 769.86] right? Like the example I've been using is like, if I install a vanilla empty view application or react
[769.86 → 776.44] application from one of their templates, I end up with a thousand packages in my repository, right?
[776.50 → 782.94] From start new project that is using this framework. There are a thousand dependencies. Uh, there's no way I
[782.94 → 787.06] have the bandwidth to engage with a thousand communities. I don't even know what, you know,
[787.48 → 789.52] 950 of those dependencies are.
[790.10 → 795.44] Yeah. I don't think you necessarily have to engage with like every dependency, but there are the key
[795.44 → 799.94] ones that you need to do. So for example, in that case, you would engage with the community that's
[799.94 → 805.06] working on managing that. Like, I guess it was, were you saying it was like create view app or something?
[805.52 → 810.94] Uh, views coming from Vue CLI, but I mean, the event stream one is, is like, that's sort of the
[810.94 → 815.50] the example of the weakness of that, right? Because that's two or three levels down. This is a tiny library
[815.50 → 822.32] that happened to get picked up to handle this, you know, it, and it ended up targeting this Bitcoin
[822.32 → 831.24] wallet. That was probably, I want to say two or three layers up the dependency chain. So I think
[831.24 → 838.80] putting it on the individuals is probably doomed to fail. Like we need to, to put some sort of process
[838.80 → 845.54] and technology helping solution in there. Um, whether it's, you know, a system around validating
[845.54 → 851.30] dependencies and marking which ones like are validated and have, you know, maintainers that
[851.30 → 857.20] are, have been consistent or, or some way, like we're trying to do this with security audits right
[857.20 → 865.08] now with NPM audit. Um, I say we, the community, uh, NPM is trying to do this. Um, but that's, uh,
[865.08 → 871.16] sort of reactive in the sense it's going out and auditing things. And then when something has been
[871.16 → 875.56] shown to be a security problem, then it puts it in there. But I think we need a proactive version
[875.56 → 883.94] of that, of how are we marking libraries as well-maintained or, you know, unmaintained and
[883.94 → 888.50] marking changes of maintainer ship and tracking that through all of our tools.
[888.50 → 896.90] Yeah. And I think even if that proactive, um, those proactive solutions end up being technical
[896.90 → 902.76] before you put something technical into place, you have to have a like person to person understanding
[902.76 → 908.58] of an open source project and who's maintaining it and actually follow a particular project that
[908.58 → 918.20] you're invested in as part of your ecosystem before just, um, rolling out a technology solution.
[918.20 → 924.48] And I think, again, this might be my bias being someone who's hard to maintain a few projects is
[924.48 → 930.62] people do tend to be reactive. They only come in when there's like a problem or, you know,
[930.66 → 936.54] you've been discussing like an architectural issue for like months, and then they come in at like
[936.54 → 943.72] the end of the discussion with an idea or feedback. And it's, it's a little frustrating when people
[943.72 → 950.58] feel like they're owed a certain amount of attention from a project when they're not giving it to it.
[950.80 → 956.02] Oh yeah. Yeah. I mean, I've had those where you have this architectural discussion for months and
[956.02 → 960.74] months and months, and then at the end of it, you do a first implementation and that's when everybody
[960.74 → 964.52] wants to give feedback and say, what are you doing? Why is it, why are you architecting it this way?
[964.54 → 968.12] This is terrible. And you say, we've been having this discussion and literally begging you
[968.12 → 976.28] to contribute your ideas. But once again, so we could, you could take that as a way to blame
[976.28 → 979.60] people, but I'm not sure that that's actually going to make it better. Cause that's, that's just
[979.60 → 984.62] kind of how people are. It's not just, it's not limited to open source, right? Like people react
[984.62 → 991.44] to things that impact them. They don't go out searching for things. So like we need some way to,
[991.76 → 997.20] like if we're, if we're looking for this to be an individual demand or individual sort of ethics
[997.20 → 1001.96] problem, it's never going to solve the problem because people can't, they're overwhelmed.
[1002.22 → 1006.58] Don't think it has to be on the individual, but it certainly has to exist at the level of at least
[1006.58 → 1011.56] like an engineering team. Do you think that there's a problem that there's a disconnect between
[1011.56 → 1015.98] the source that you can view, and what might actually be in an NPM package?
[1015.98 → 1024.94] Yeah, that's definitely like another tricky thing is like the thing that's on the NPM registry
[1024.94 → 1033.22] is not the thing that's on GitHub.com and that void does cause a lot of problems again,
[1033.30 → 1035.18] especially with like third party dependencies.
[1035.86 → 1041.34] Yeah. I think you need a way to have visibility. I'm not sure that you can require, because people
[1041.34 → 1045.50] don't have to host their code on GitHub. That's one private company, but there needs to be some
[1045.50 → 1049.18] way to transparently see what is the code that got released in this package.
[1049.18 → 1054.72] Sure. But a lot of teams, if they were going to do a security audit, they'd probably start
[1054.72 → 1059.38] at GitHub and be looking at the code and, or I mean, where the code is hosted and looking
[1059.38 → 1064.06] at the source code of it to try and understand it and see that there's no, like trying to
[1064.06 → 1068.74] make a determination that there are no vulnerabilities, but what they're actually getting from an NPM
[1068.74 → 1070.96] install could be completely different.
[1071.46 → 1077.30] Yeah. I think you might be able to, well, so once again, it's, it's hard, it's hard to make
[1077.30 → 1082.80] requirements across entities. I mean, you could, there are things you could do with hashing,
[1082.92 → 1086.92] right? So you say, okay, we're going to do a hash of exactly the source code at this point
[1086.92 → 1091.08] and then publish that anywhere. Like if I look at a release on GitHub and I look at a release
[1091.08 → 1096.50] on NPM and have that be a way to verify that. But you could also have NPM say, we're going
[1096.50 → 1099.82] to host the code in a way that you can browse it, for example.
[1100.44 → 1104.94] Yeah. There's, you still run into problems though, I think, and I'm not advocating for this kind
[1104.94 → 1109.72] of thing. I just think that it, it's a gray area where problems can easily come up. But like
[1109.72 → 1116.04] on Dojo, for example, we write in TypeScript and then publish UMD packages to, to know, or to NPM.
[1116.66 → 1122.54] And I certainly want, wouldn't want to force the users of it to have to compile our TypeScript.
[1122.72 → 1127.30] They can just bring it in and use, and use the UMD. But I wouldn't want to have that on GitHub,
[1127.46 → 1133.80] the UMD part either. So it's a it's just a problem area, but I'm not sure that there's really
[1133.80 → 1134.60] a solution.
[1135.14 → 1140.24] That's fascinating. Yeah. I wonder how you would, like, could you have a like,
[1140.32 → 1146.04] here's the compiled, like at compile time, it generates something that you then check in.
[1146.16 → 1147.28] I don't know how you'd do that.
[1147.66 → 1147.84] Yeah.
[1148.02 → 1152.52] And you can't guarantee once again, that it's the same. Like anything that is checked in
[1152.52 → 1156.50] deliberately could be maliciously manipulated, right? It's got to be something that's generated.
[1156.50 → 1165.38] Um, I, I, I feel like this is, it's like, we're, we're talking like people don't know
[1165.38 → 1169.70] what they're deploying. I mean, uh, if you don't know what you're deploying, that's,
[1169.80 → 1170.96] that's a problem. Sure.
[1171.14 → 1173.10] Well, that is what happened with event stream, right?
[1173.48 → 1180.04] Yeah. Uh, and, and I mean, if you, okay, say you've solved that problem, and you know what
[1180.04 → 1185.02] you're deploying. And so you're in your development environment, you NPM installer, yarn installer,
[1185.02 → 1191.46] whatever you have your lock file. I mean, you're, you're going to see what's, what's in your
[1191.46 → 1196.08] node modules and, and, and, you know, if everything's working properly, that's what you're going to
[1196.08 → 1203.94] get when you deploy it. Um, you would look in there, uh, you might, obviously if you, if you look
[1203.94 → 1209.00] at the GitHub repo, that's not always going to be the same stuff. So you have to look at your,
[1209.00 → 1215.00] your node modules, but I mean, uh, I, I guess I'm, I'm, I'm,
[1215.02 → 1224.78] I wasn't present for the chat last week. Um, but, uh, yeah, it's, uh, I don't know if we're,
[1224.88 → 1230.28] if we're going down that road into back into the discussion about event stream and stuff, but,
[1230.28 → 1237.92] um, yeah, it's, that, that's a tough problem. And, and, and, you know, if you, you can either pin
[1237.92 → 1241.90] your dependencies or something and then manually validate everything that you pull in,
[1241.90 → 1248.64] or you can just trust people not to do stuff bad and deploy things. And it's all about,
[1248.64 → 1253.72] you know, how much time it's going to take and how much risk you're willing to accept. I mean,
[1253.72 → 1259.44] at the end of the day. And so it's either, it's either you hand check everything or, or, or have
[1259.44 → 1265.04] some tooling that to, to, to help you do that, you know? Um, yeah. I think the interesting thing
[1265.04 → 1272.70] about event stream, it was definitely like very edge Casey in the world of, um, in the world of
[1272.70 → 1277.32] like dependency related security issues. There were just like a lot of fascinating things that
[1277.32 → 1282.32] happened with that. Um, but I think you highlighted something really important,
[1282.40 → 1287.52] which is having knowledge about what you're actually deploying. Um, and I think that's just
[1287.52 → 1293.88] another criteria for deciding whether you are going to use a library is,
[1293.88 → 1298.48] do you have a certain amount of confidence about the code that's written? Um, it's quality,
[1299.14 → 1306.12] it's like longevity. Um, have you just like done a look through as an engineer to see if it checks
[1306.12 → 1311.66] all the boxes without even looking at its dependencies or anything? Um, sometimes I find
[1311.66 → 1317.10] that that's something that I don't do often, uh, which I'm ashamed to admit. Um, and certainly
[1317.10 → 1323.04] like engineering teams I've worked with, um, there is definitely not a ton of like looking through
[1323.04 → 1330.12] things to validate the code, the license, um, and like code quality and all that. Um, but I think
[1330.12 → 1335.94] it's getting better with like tools like that exist that allow you to confirm those things.
[1336.08 → 1339.76] I'm going to take issue with the statement that most people know what they're deploying.
[1339.76 → 1347.48] Uh, I just ran for, for fun. I ran install, create react app, which is I think what a lot of people
[1347.48 → 1355.12] use to start building their React applications. Uh, NPM tells me that running that to create a blank
[1355.12 → 1364.46] react app added 1775 packages from 679 contributors. Uh, so if I go in there and I look in my node
[1364.46 → 1380.22] modules, LS node modules, um, I have, I see packages like topo tr46, uh, sago, um, INI internal IP
[1380.22 → 1391.24] invariant, he hash base. Uh, like I have no idea what a lot of these packages are. And my intuition
[1391.24 → 1396.36] is that most people who are deploying react apps also have no idea what any of these packages are
[1396.36 → 1402.16] because they're probably two or three or four, or even, you know, I don't know how deep the tree goes,
[1402.16 → 1410.44] but like if I deploy a React app built on this, like I'm, I make, I am assuming that none of these
[1410.44 → 1417.02] contain an obfuscated malicious code piece of code. Yeah. Um, so I think I'd, like I was saying before,
[1417.02 → 1422.88] I think the issue of like deep dependencies, um, I'm forgetting the word for it now. The thing
[1422.88 → 1427.00] that's like a dependency of a dependency it's on the tip of my tongue. Oh my goodness.
[1427.66 → 1432.56] Nested dependency or sub dependency. I guess that might be the word. I think like, that's always
[1432.56 → 1438.08] just gonna transient dependencies. There are ways to Mark reader in the chat. Yeah. Transient dependencies.
[1438.08 → 1445.16] Thank you, Mark. Um, I think that's always going to be a little unsolvable just because at that point
[1445.16 → 1453.10] you're like, if someone truly wants to figure out an exploit, they will. And it's very hard to be
[1453.10 → 1458.70] proactive about those to a certain extent. Like there's a lot of safety checks you can do and like
[1458.70 → 1464.68] tests and validations and stuff like that. But I think if somebody really wanted to do something
[1464.68 → 1472.72] malicious using some, you know, transient dependency, they could, but I think it's unfair to ask people
[1472.72 → 1478.58] to check those deep down dependencies, but it is fair to have them be aware of like how create react app
[1478.58 → 1484.86] works, what's being loaded and the general architecture of the project. Like that's a reasonable ask. Um,
[1484.94 → 1491.70] yeah. And what it's using just as at like top level dependencies, um, anything deeper than that.
[1491.70 → 1497.80] I think that's where you need to have like automated tools doing the checking and just pray that people
[1497.80 → 1502.74] in the world are good and won't try to mine bitcoins, um, all the time.
[1503.26 → 1508.68] I think that that's a good, a good place to start. And then you do get a little bit more
[1508.68 → 1516.24] security through the, the trust of something like create react app, which is huge and hugely popular.
[1516.24 → 1521.92] Uh, there's a little bit of comfort in if there is a problem, it's probably going to be found out
[1521.92 → 1528.34] pretty quick. Um, and you can kind of lean on that a little bit, but you might be bitten just like in
[1528.34 → 1530.26] the case of event stream, you might be bitten for a while.
[1530.90 → 1537.58] So I think this discussion around kind of how do you do security checks and audits and what is the
[1537.58 → 1544.62] process for bringing in a third party library is a good segue into the next segment, which is what are
[1544.62 → 1550.96] some of the processes and steps that companies have for deciding whether to bring in, um,
[1551.26 → 1555.62] external dependencies. Uh, we'll be talking about that right after the break.
[1562.02 → 1567.62] This episode is brought to you by our friends at roll bar. Check them out at robot.com slash change
[1567.62 → 1573.32] log, move fast and fix things like we do here at change law. Catch your errors before your users do
[1573.32 → 1577.86] with roll bar. If you're not using roll bar yet, or you haven't tried it yet, they have a special
[1577.86 → 1585.78] offer for you. Go to robot.com slash change log, sign up and integrate roll bar to get $100 to donate
[1585.78 → 1591.82] to open source projects via open collective. Once again, robot.com slash change log.
[1596.32 → 1596.82] Okay.
[1603.32 → 1610.36] So I'm curious to know, uh, for where you currently work now or where you've worked before or any
[1610.36 → 1616.52] interesting processes you've heard from other companies, um, do you have a checklist or a
[1616.52 → 1621.36] process for bringing a library into your code base, and what does that process look like?
[1621.70 → 1626.34] So, yeah, I mean, uh, for most of my career, that's been the case. There's really no process. Does it,
[1626.34 → 1630.60] does it do what you want? Will it, will it help us ship, you know,
[1630.60 → 1638.10] yeah, at it, who cares? Right. That's, that's the, the, the process has been no process. Um,
[1638.56 → 1647.82] uh, now I am, uh, at a larger company and, um, so it really just, it depends on what you're building
[1647.82 → 1652.78] and who you're building it for. Um, you know, different clients will have different requirements.
[1652.78 → 1660.08] Um, and so, you know, that might be certain licensing requirements. Um, you know, but, uh,
[1660.08 → 1665.22] if we're building anything at all, uh, at a bare minimum licenses are going to be checked. Um,
[1665.78 → 1675.38] you know, but, uh, I, I, I don't know. Um, I, I imagine it varies per, per team to team, uh,
[1675.38 → 1681.92] a little bit as well in, in, in, in so far as, uh, how stringent they are about, about adding new
[1681.92 → 1688.16] dependencies. Um, and maybe that's typical of any large company. Yeah. I work for a consulting
[1688.16 → 1693.06] company, so I get to work with a lot of different teams, and it's kind of the same thing. It depends,
[1693.06 → 1696.88] uh, and varies from team to team. Sometimes we just come in, and they've already got
[1696.88 → 1702.54] what they think we need all set up, and we're just going to work with that. And we have to go through
[1702.54 → 1707.46] an approval process if we want to bring in something else. Other times we'll let them know
[1707.46 → 1711.60] what we want to build, and they'll, they might give us direction on like, Oh, use angular, use this.
[1711.92 → 1718.10] And we might put that, and we'll actually put in our, uh, contracts with them. Like this is the
[1718.10 → 1721.70] open source that we're going to use. And I won't list everything. I'll say like, Oh, we're going to
[1721.70 → 1727.94] use angular, uh, but not the 10,000 dependencies that come with angular. I'll just put angular and
[1727.94 → 1733.92] assume that they understand that. Um, and then, but, but then if we need to bring in something else,
[1733.92 → 1739.84] it's usually just a discussion about why we think we need it. And, uh, yeah, license licenses are
[1739.84 → 1744.38] checked as well. But, uh, assuming that there are no problems there, then it's pretty easy to,
[1744.38 → 1745.86] to justify it.
[1746.18 → 1750.88] And do, uh, you know, typically check the licenses all the way down the dependency tree?
[1751.06 → 1754.10] Uh, good question. No, probably should.
[1754.26 → 1758.92] That's kind of an interesting question, right? If, if a framework, for example,
[1759.46 → 1765.62] asserts that it's MIT licensed, what happens if it pulls in code that is, for example, GPL licensed?
[1765.62 → 1771.68] Um, companies won't use it. That's what happens. If they notice.
[1772.06 → 1776.96] That's the thing. I think I, like I try and check the licenses of the, the direct dependencies that I
[1776.96 → 1785.10] will think of, uh, or, or need, uh, and then rely on trusting the, um, those projects to have done the
[1785.10 → 1791.20] due diligence on the dependencies that they need and so on, uh, which isn't perfect of course, but it's,
[1791.20 → 1797.48] it's all about whether they notice, I guess. Right. As, as a side note to this, um, there's,
[1797.64 → 1803.52] uh, at least for like JS foundation projects and, and, and maybe even, um, they have like a free
[1803.52 → 1809.38] thing for open source projects. There's this thing called FOSSA, F O S S A. And what they do is they
[1809.38 → 1817.14] automate license checks of open source projects. And so like Mocha has this setup where you can go and
[1817.14 → 1822.78] look at the read me, and it has like this information from it's like FOSSA analysis, which, which talks
[1822.78 → 1829.52] about all the licenses used, um, all the way down our dependency tree. And so if you have something
[1829.52 → 1837.94] like that, um, on your open source project, that might be able to help, um, people who want to adopt,
[1837.94 → 1843.36] uh, enterprises that, that worry, uh, more about licensing than, than maybe your average company.
[1843.36 → 1848.30] So, um, that's something to check out. It's called, uh, FOSSA F O S S A.
[1848.58 → 1856.18] Mark reader on the Slack channel also just posted a link to a node package called the NPM license
[1856.18 → 1864.42] crawler. Um, and it looks like it is, uh, basically a license checker for all the dependencies in your
[1864.42 → 1870.98] node modules. Um, and it just spits out a report of all the different licenses you're bringing out
[1870.98 → 1877.12] or bringing on. Um, so I think that accomplishes a similar task if you want to, you know, just be
[1877.12 → 1880.96] running the checks yourself as part of your process. Thank you for sharing that Mark.
[1881.30 → 1885.42] Ooh, I'm going to run that on my creation react app empty thing and see what happens.
[1885.86 → 1887.22] Oh, I'd be curious to see too.
[1887.84 → 1892.98] Okay. So what do I need to do? Install it globally and run it.
[1892.98 → 1901.44] I guess the thing that you see, um, often in these types of tools is projects that have no license at
[1901.44 → 1908.54] all. So what do we do with these? Yeah. That I think the onus is definitely on the maintainer.
[1908.54 → 1913.12] Uh, if you, I think if you do see that, you could probably just reach out to them and request that
[1913.12 → 1920.56] they add a license. I think most of the time it's just a lack of knowledge, um, or time on behalf of
[1920.56 → 1926.92] the person who made the package to add a license. Um, I think GitHub has made that a little bit
[1926.92 → 1933.90] easier by adding the license as their, one of their dropdowns in like package creation. Um,
[1933.96 → 1938.80] and just by like hiding it a little bit more in their UI and having it as part of their like
[1938.80 → 1947.52] checklist for project health. I'd love to see how those kinds of UX UI decisions on GitHub's part
[1947.52 → 1953.78] have changed how many projects, new projects emerge with valid licenses to start. But, um,
[1953.98 → 1957.98] I think the licenses are, are, are one front to explore. I'm curious to know,
[1958.08 → 1964.80] have you worked at any organizations where they have had, um, security teams that will audit packages,
[1964.80 → 1971.60] um, before bringing them into your code base? I have. Yes. And that, uh, that resulted in one guy,
[1971.60 → 1978.82] um, manually reading source code and then determining whether it could be used on a project.
[1979.20 → 1981.48] Interesting. I don't think it was efficient.
[1982.02 → 1988.76] Yeah. Was this person like a security expert who was used by different engineering teams within the
[1988.76 → 1994.54] company, or what was the relationship like between that person and the engineering team? Were they part
[1994.54 → 2000.28] of the team? They were more, um, like security was more of their main thing, and they would work on
[2000.28 → 2005.16] that. Um, and they, so you, anytime you wanted to bring in a dependency, you'd have to go through
[2005.16 → 2009.52] them, and they'd have to, uh, put their approval. And I know that they ran some, some automated scans,
[2009.52 → 2015.26] but then also did some manual things that I wasn't aware of. Um, but the results were almost always
[2015.26 → 2020.42] comical. Sounds like you might have some interesting stories, but we don't have to dive into them. Um,
[2020.42 → 2028.98] I have worked at, um, organizations where you had to fill out a form, um, before you brought a third,
[2028.98 → 2036.08] um, third party dependency in, or started using some external like SAS service or whatever. Um,
[2036.20 → 2042.44] and they were checking for things like, Oh, is this, uh, software project or this, uh,
[2042.76 → 2049.44] SAS service like HIPAA-compliant? Do they serve their website through SSL? There was like a couple of like
[2049.44 → 2054.86] questions that you would have to fill out, um, um, and submit just to like engineering managers
[2054.86 → 2061.22] about the project before you could use it. I think that's like the most level of process I have seen
[2061.22 → 2065.40] at any of the organizations I've worked on where you kind of have to like go out of your way to
[2065.40 → 2069.42] like check things yourself and fill out the information. And then you're also like
[2069.42 → 2073.44] responsible for certifying that the information you provided is accurate.
[2073.44 → 2081.12] And if like goes wrong, um, or something is off, you like have responsibility over that.
[2081.60 → 2086.96] I have the answers now, by the way, of the licenses invented. It took me a while to put together the
[2086.96 → 2093.46] bash string to, you know, separate out their nonsense and strip white space and sort it and unique it and
[2093.46 → 2099.50] all that. But, uh, I count, let's see. One, two, three, four, five, six, seven, eight, nine, 10,
[2099.50 → 2107.38] 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27 unique license strings,
[2108.22 → 2118.72] um, including combos. So it says Apache 2.0 or MPL 1.1. Uh, some that I've never heard of.
[2118.72 → 2121.50] What is WTFPL? I've never heard of that.
[2122.04 → 2127.02] I think it's whatever the want. I'm cursing a lot in this podcast episode. I'm sorry.
[2127.02 → 2134.44] Um, so there's WTFPL, there's ISC, which I also don't know what that is. Um, that's the default one,
[2134.74 → 2140.92] the default one. Okay. If you like did NPM unit, uh, it gives you ISC as your license string in there.
[2141.18 → 2149.22] Okay. Uh, yes, there's some that are various versions of CC creative commons, different ones,
[2149.22 → 2160.18] MIT X 11. Interesting. MPL 2.0 public domain unknown HTTP. Interesting. Um, and one that's just
[2160.18 → 2166.98] says C license in license.md. So the, uh, tool is not perfect, but it gives you a sense of the
[2166.98 → 2173.22] varieties, no GPL showing up. So I guess I can keep using create react app, but please don't license
[2173.22 → 2179.00] your code under creative commons. Yeah. Kind of wonders. I wonder if it lets me dig into which
[2179.00 → 2186.40] ones come from which license. Uh, I think I can output to like a CSV or something that would let
[2186.40 → 2192.98] me see that, but yeah, kind of interesting exploration of like, what is CC by 4.0 versus
[2192.98 → 2200.04] CC by 3.0. I think there are different versions of the creative commons license. I might be wrong
[2200.04 → 2205.22] though. Yeah. Interesting that people would use that for coded dependencies. Yeah. I've never seen
[2205.22 → 2211.64] that. Um, it would be neat to see which projects are doing that in particular. So if no one has
[2211.64 → 2218.34] anything else to share on, you know, organizations having a process for bringing in external libraries,
[2218.34 → 2226.86] I'd love to jump into the discussion on how both you as an individual and then your company, um,
[2226.86 → 2234.12] contributes to a healthy open source ecosystem. And what does that relationship look like? Um,
[2234.30 → 2240.00] and what you and your organization can do to make sure that open source packages are thriving.
[2240.24 → 2246.26] So I think we can take a little bit of a break, and then we'll jump into that discussion. I'm sure
[2246.26 → 2257.74] it's going to be, be an interesting one. This episode is brought to you by DigitalOcean,
[2257.74 → 2264.70] the simplest cloud platform for developers and teams deploy, manage, scale faster and more
[2264.70 → 2270.20] efficiently on DigitalOcean. Managing infrastructure is easy for teams, whether you're running one virtual
[2270.20 → 2275.68] machine or thousands, use our special link to get a hundred dollar credit for DigitalOcean and try it
[2275.68 → 2284.14] today for free. Head to do.co slash changelog. Once again, do.co slash changelog.
[2298.32 → 2304.52] So we're back. We are discussing ways that your organization can contribute to a healthy open
[2304.52 → 2310.42] source ecosystem. Uh, during the break, we got a conversation going about non-traditional ways
[2310.42 → 2315.80] that your company can fund open source projects. One of the things that was mentioned is donating
[2315.80 → 2322.04] engineering time to an open source project. Um, so having somebody who's got like a day or a couple
[2322.04 → 2328.36] of hours a week to contribute to open source software that their company uses. Um, and we were just
[2328.36 → 2334.54] kind of talking about whether that's considered a form of funding, um, and coordinating all that
[2334.54 → 2338.02] and other fun things. So we're going to continue the conversation from there.
[2338.58 → 2344.24] So yeah, this idea of people versus money is fascinating because there's kind of multiple ways
[2344.24 → 2351.86] that a company might, uh, have their own engineering time focused on open source. Like you have the Facebook
[2351.86 → 2359.74] model where they have a set of Facebook open source projects that Facebook engineers work on. Um, and
[2359.74 → 2366.52] they probably also have some folks who work on third party things, but really like there's this like
[2366.52 → 2373.20] corporate run, uh, open source project type model. Um, then there's the model where folks will
[2373.20 → 2378.62] literally, you know, they're using a technology, and they'll hire somebody who is a core developer
[2378.62 → 2383.26] there and have them dedicate either part or full time towards working on that. So for example,
[2383.90 → 2389.92] uh, Elm as a language, as I understand it, the creator of Elm is higher or was hired by a company
[2389.92 → 2395.66] that uses Elm, and he is paid just to work on Elm, uh, because they use it. They want to ensure the
[2395.66 → 2400.74] robustness of the tools. They're depending on things like that. And then there's the I use this project
[2400.74 → 2406.52] and I'm allowed to put some time into, you know, say I run into a bug, I can go and fix it and submit
[2406.52 → 2413.34] that back or things like that. Like all of these are different models, uh, within the sort of context
[2413.34 → 2420.20] of we're spending engineering time to support open source. The one that I've had the most kind of
[2420.20 → 2426.78] interaction was, is probably two and three, uh, which are situations where, you know, I think with
[2426.78 → 2433.04] something like react, it's a little bit different because Facebook was the person or the entity that
[2433.04 → 2439.76] open source the project. It was something internal that was then made public. Um, so I think that's a
[2439.76 → 2447.92] little bit different from like someone independent of any company starting a project, um, and then
[2447.92 → 2454.10] getting support for that. And the examples that I've worked in it, it's generally the way the
[2454.10 → 2459.66] relationship works out is the open source project has some sort of roadmap or some sort of action items
[2459.66 → 2465.98] that need to get done. Um, and the company that is going to be funding engineering time on those
[2465.98 → 2472.06] action items has some sort of like interest in seeing them be done for their own internal reasons
[2472.06 → 2479.04] or whatever. And they make, I guess, an in-kind donation or a commitment to have their engineers
[2479.04 → 2486.52] working on it and collaborating actively with, um, the open source contributors who are not affiliated
[2486.52 → 2493.40] with that company. Um, there's always like an interesting, like, dynamic when you have like a team of
[2493.40 → 2498.92] people who are just open source contributors, uh, who've like started the project or very invested in it.
[2498.92 → 2505.32] And then a group of people who get paid to work on it by their companies for a certain amount of time.
[2505.32 → 2510.52] Like they tend to like to come in with different perspectives on how, like how to solve things and how to allocate
[2510.52 → 2522.44] resources just by virtue of their different situations. Um, and then the third, I think is like more of like the
[2522.44 → 2530.36] Ruby model. Um, I have not had an experience personally with that one yet. So I would say two is the one that
[2530.36 → 2532.20] I've had the most experience with.
[2532.20 → 2534.60] What's, what's the Ruby model?
[2535.02 → 2541.32] Oh, um, that's the one where like, because a company is invested in a technology succeeding,
[2541.64 → 2546.26] they have an engineer working on it. Um, and I think that's the case for like Shopify,
[2546.26 → 2552.58] which is deeply invested in Ruby, um, Basecamp, which obviously created Ruby and is still deeply
[2552.58 → 2558.66] invested in it for rails. Yeah. Rails. Um, so things like that, where you are like,
[2558.66 → 2566.32] I guess it connects a little bit more so with two, but I think in the case of two, it's more than
[2566.32 → 2571.38] one or two people working on something. It's like a whole team that's partly contributing to open
[2571.38 → 2577.42] source. What, what I've kind of picked up on, um, um, you know, I haven't worked at a super mega
[2577.42 → 2582.20] corp for very long, about a year. And before that I worked for small companies, but with these larger
[2582.20 → 2588.10] companies, it seems, and, and my, my interactions with people at larger companies, it's often,
[2588.10 → 2597.08] it's the case that it is really difficult. Like it's, it's so difficult for a, uh, a developer
[2597.08 → 2603.16] who uses some third party dependency to actually contribute because there's a bunch of bureaucracy
[2603.16 → 2609.38] involved. Uh, it's going to get signed off by legal and all this stuff. Um, and you know,
[2609.40 → 2614.38] the more dependence it, I mean, where are you getting the big problems? It's like, it's like these,
[2614.38 → 2621.54] there are more dependencies you pull in. Like if you're in a JavaScript ecosystem, um, the, the
[2621.54 → 2627.06] harder, the harder it even becomes because you can't, you can't spread it. It's just like way
[2627.06 → 2633.86] too much red tape. You know, if there's like 20, 20, uh, projects you want to contribute to versus one,
[2633.86 → 2642.60] you know what I mean? And so, you know, I, I think a, a, a, a, a question that we can, I mean,
[2642.68 → 2649.32] I don't have any magic solutions, but something we can start thinking about is how, how can we make
[2649.32 → 2655.84] it is easier for, for larger companies and their, their legal departments or what have you, um, to,
[2655.84 → 2662.54] to, to allow their developers to contribute to these, to, to these open source projects. Um,
[2663.46 → 2670.64] you know, maybe that is some sort of certification. Um, I don't know, but, um, you know, I'm, I'm
[2670.64 → 2676.30] certainly no lawyer, but, uh, yeah, that's, that's, that's kind of a problem I've, I've noticed. And,
[2676.30 → 2681.34] um, I don't know, I just, I'm not sure where to go on that one.
[2681.34 → 2686.24] That's fascinating. Actually. Um, if you look at what Tide lift is doing on the financial
[2686.24 → 2691.36] side or what some of the foundations like the JS foundation do on the financial side, right? Those
[2691.36 → 2698.14] are organizations that are set up to allow big companies to financially contribute to the projects
[2698.14 → 2703.04] that they're involved in without having to create relationships with all the individual developers.
[2703.78 → 2708.96] Um, I wonder if you could set up a similar sort of arrangement where they, you know, are asserting
[2708.96 → 2713.06] things about those licenses such that legal doesn't have to check them all out individually,
[2713.06 → 2717.36] but rather can say, okay, these are all okay for our people to contribute to.
[2717.88 → 2723.92] Yeah, that's, that's a cool idea. I wonder about though, if you were to take a foundation,
[2724.50 → 2732.24] um, say the whatever the merged node and JS foundation looks like, um, you know, hypothetically,
[2732.24 → 2741.12] uh, and, and you, you wanted to add this thing to it that said, okay, um, you know, you are a member.
[2741.26 → 2748.58] And so we have, um, I don't know, vetted all these projects. I mean,
[2749.24 → 2755.32] basically anybody who would be a member of, of that, I mean, this is a trade foundation, any, any,
[2755.32 → 2763.68] any member company, um, would need to vet any project added, you know what I mean? And so that
[2763.68 → 2772.46] would potentially cause some conflicts where a, um, you know, maybe a project wants to join the
[2772.46 → 2778.80] foundation, but it competes with a product, um, owned by one of the member companies. You know what I
[2778.80 → 2785.86] mean? I, I, I feel like that's something that needs to happen separately, um, from at least a
[2785.86 → 2791.36] trade organization for that reason that it's just like, there's too much potential for conflict.
[2792.30 → 2796.58] That's, that's interesting. Right. So the vetting is not just sort of legal standpoint,
[2796.58 → 2800.32] but are we contributing to something that is potentially a competitor and things like that?
[2800.84 → 2807.48] Oh yeah, absolutely. I mean, yeah. Companies are not just worried about the licensing. They want to
[2807.48 → 2813.42] make sure that we're not contributing to a competitor. So. There's only so much that like
[2813.42 → 2819.74] an independent open source project can do from some of my experiences with it. It's not actually
[2819.74 → 2826.38] as hard to get all the paperwork done as some people might make it seem. It's just, yeah,
[2826.52 → 2832.68] obviously I think it depends on what team you're in and like, it's very specific situations, but I think
[2832.68 → 2838.68] for some of the people I know who work at big mega corps and contribute to open source projects I'm
[2838.68 → 2845.10] affiliated with, um, it's not like the worst thing in the world. Could it be easier? Yes, but it's not
[2845.10 → 2851.60] like boundary setting or, um, like a complete barrier to open source. And I think an organization
[2851.60 → 2857.76] has to figure out internally to set up a smooth and quick process, uh, for getting people into a
[2857.76 → 2862.28] position where they can quickly contribute to open source projects that the company has vetted out.
[2862.28 → 2867.42] And it's one of those things where if your organization is committed to making it happen
[2867.42 → 2873.38] or values open source, they're going to invest the time in making that process smoother. Um,
[2873.44 → 2878.44] and if they're not interested or super committed to open source, then it's not going to be as big
[2878.44 → 2886.42] as a priority for them. Um, so I think I generally tend to place the onus on the company with money and
[2886.42 → 2893.98] lawyers to figure this out as opposed to the community because openly, ultimately it is an
[2893.98 → 2899.38] internal process, not something that open source projects has had too much say in.
[2899.38 → 2904.56] Yeah. And another perspective that they could potentially take is from a marketing perspective.
[2904.56 → 2910.30] Um, if you're allowing your developers to occasionally contribute to open source projects,
[2910.30 → 2915.78] that's a big marketer for, uh, future developers that you want to hire in a lot of cases.
[2915.78 → 2921.70] Yeah. I've definitely seen that a lot of companies where, um, you know, they have one person come in
[2921.70 → 2925.98] and start contributing into a project, and they realize there's this like whole talent pool that
[2925.98 → 2930.60] they wouldn't have had access to through their traditional recruiting means. And recruiting is
[2930.60 → 2936.12] really expensive, especially for engineers. And it can definitely pay off if you use open source
[2936.12 → 2941.84] contributions as a recruiting pathway. Absolutely. And if you look at, uh, someone's GitHub repo,
[2941.84 → 2947.44] when you're thinking about hiring them, uh, you should only do that if you're also actively letting
[2947.44 → 2952.86] your employees contribute to open source. Yep. What do you all think about the trend towards
[2952.86 → 2959.42] funding people to work outside of companies on open source projects? So whether that's through
[2959.42 → 2963.32] formal organizations, like I know the Ruby community has Ruby together where they were
[2963.32 → 2968.22] fundraising and trying to get, you know, and they, they literally hired people to work for Ruby
[2968.22 → 2973.04] together to work on Ruby infrastructure. But then there's also these more informal things like, uh,
[2973.04 → 2977.78] open collective projects, getting themselves funding via that people doing stuff on Patreon,
[2977.78 → 2984.30] um, or the Tide lift subscription, trying to fund, uh, essentially developers to directly work on
[2984.30 → 2990.74] open source outside the context of a company. I have experience with that. Um, there have been
[2990.74 → 2997.14] two occasions in my life where I've been funded to work on open source. One was through a grant from
[2997.14 → 3003.40] a nonprofit entity to the open source project I worked on. And the other time was a private
[3003.40 → 3010.12] donation from a company that was invested in the project. Um, so it wasn't like Patreon or open
[3010.12 → 3015.36] collective. It was kind of like a bit more, I guess, formalized would be the word for it. Um,
[3015.36 → 3022.44] and I found it really valuable, like just having like two weeks or like a six-month contract to just
[3022.44 → 3029.30] be paid to work on something and invest all my time in it was such a huge boon to the open source
[3029.30 → 3036.88] project because I had the time to just focus on something and like get it done. And it was also
[3036.88 → 3042.60] just like fun for me to be paid for something that I love to work on, which is like ultimate life goal
[3042.60 → 3049.38] for a lot of people. Um, so I think when it is like a private company or a grant from a foundation
[3049.38 → 3056.20] or a nonprofit group or a government to work on something, um, it can be like really successful
[3056.20 → 3063.74] and great. Um, and I've also seen situations where they've actually been able to like employ entire
[3063.74 → 3070.60] teams of people because they got, you know, multi-million dollar grants for a project. Um,
[3070.60 → 3077.38] the Patreon thing, I don't have too much experience with. I don't know how I feel about it because I
[3077.38 → 3083.16] feel like with Patreon and like open collective and stuff like that, a lot of it comes down to
[3083.16 → 3091.86] celebrity a little bit. Um, and people are more likely to donate to the maintainers and contributors
[3091.86 → 3098.10] who are most visible in a community. And that might be the person who's most active and doing the most
[3098.10 → 3102.60] work, but it might also not be. So yeah, those things are always tricky because they tend to be
[3102.60 → 3108.26] mostly funded by private individuals as opposed to companies in the case of Patreon specifically
[3108.26 → 3116.26] and generally spread through word of mouth or social media where, um, being a name in the industry
[3116.26 → 3121.94] plays a big role in how likely you are to get funded. So I think those are like the two thorns with that
[3121.94 → 3128.20] situation. Yeah. It seems like open collective in particular and the successful folks I've seen
[3128.20 → 3133.46] on Patreon actually try to bring companies into it. Like the individual donation stuff really doesn't
[3133.46 → 3138.38] scale very easily. And it's a question of like, should it be individual engineers donating? Like
[3138.38 → 3144.66] that seems like a pretty sketchy way to support this stuff. Um, you know, where, where I've seen some
[3144.66 → 3150.38] more success, people are essentially making a business out of it, right? Like, uh, Evan, you who does,
[3150.38 → 3160.36] um, view JS, like the big donors are doing it because it gets them a their, it gets their brand
[3160.36 → 3166.40] and a link on the pages of the docs and things like that, that send over. So it's, you're turning
[3166.40 → 3174.66] it into a business essentially. Um, it, I'd love to see something, you know, where we were well funding
[3174.66 → 3179.18] people to work in this. Because I feel like, you know, this is the, you know, the infrastructure of
[3179.18 → 3183.82] modern software open source is where like, this is what makes modern software much more productive
[3183.82 → 3189.48] and eat faster to get to things than, uh, it was five or 10 or even, you know, however long ago.
[3190.16 → 3196.34] Uh, but I, I'm not sure these models are scalable. Like I'm wondering, is there a scalable model out
[3196.34 → 3203.00] there for funding independent open source development? So I, I missed the last minute or two of the
[3203.00 → 3210.70] the chat, but, um, you know, I, I feel like, yes, that is, that's, it, it doesn't work for everybody.
[3210.70 → 3218.08] It doesn't work if you, you know, aren't, uh, you aren't freelancing. It doesn't work if you're
[3218.08 → 3223.32] already working two jobs. It doesn't work if you're a single parent, like it, like you can't pay
[3223.32 → 3230.22] somebody, uh, like a thousand dollars a month and, and, you know, pretend that's enough to live on.
[3230.22 → 3239.08] So, I mean, if we want to go funding people and I mean, uh, what the Holy grail is, you need to
[3239.08 → 3246.02] pay people essentially a competitive salary. And a lot of people and me included, uh, you know,
[3246.02 → 3251.46] I have, I have kids in a, in a, in a, in a mortgage and stuff, and I'm not gonna, I'm, I don't want to
[3251.46 → 3255.18] be a freelancer anymore. I want, I want health insurance if you're in the United States, you know,
[3255.18 → 3261.32] it's, uh, it's, it just, gosh, well, that's another thing too, you know, health insurance
[3261.32 → 3266.96] for open source, uh, developers, but yeah, it's just, it doesn't, it doesn't work for
[3266.96 → 3272.60] everybody. It, it can, it can be difficult to, if a project in particular is receiving
[3272.60 → 3278.78] funds instead of an individual, it can be difficult to, um, it's like political about what you do with
[3278.78 → 3286.56] that money as well. And so, yeah, I, you know, uh, what I, what I would love to see, you know,
[3286.60 → 3292.94] at least for, for my project is just given, give me your development time. You know, you don't,
[3293.02 → 3300.54] you don't need to, you know, try to, that's, that's what I think is really going to, to sustain
[3300.54 → 3307.96] open source. Um, we need that in, in addition to, to funding. Um, and, you know, I saw this,
[3308.06 → 3313.20] this, this great thread on Twitter. I don't have it handy about, you know, how, how donations are
[3313.20 → 3318.46] incredibly problematic for a lot of companies because it's like, you need a you need a product
[3318.46 → 3323.08] order, you know, it's like you need to be purchasing something in order to spend money.
[3323.62 → 3328.82] Um, and they make it really difficult to just give money away. And so what are you buying?
[3328.82 → 3335.02] Um, one solution was, well, you're buying support. And it's like, I'm thinking, you know what? I'm,
[3335.06 → 3341.32] I don't want to, I don't, I'm not a support desk. I'm, I'm a developer. Furthermore, I don't want to support my
[3341.32 → 3346.80] project. I want to maintain it. Um, and, and I don't want to be on call or what have you,
[3347.30 → 3354.50] you know, it's, uh, support is also not the one, you know, be all solution for it unless you're,
[3355.16 → 3358.54] I don't know, red hat or something, but we all know how that ended.
[3358.82 → 3361.12] The billion dollar acquisition, right?
[3362.54 → 3364.50] Who was it that acquired them again?
[3364.76 → 3365.00] IBM.
[3365.40 → 3372.96] Okay. Right. Right. Um, in both of my cases, there was a nonprofit entity that, um, companies were able
[3372.96 → 3379.60] to donate their funding to. So unfortunately I'm a little misinformed about how it worked internally
[3379.60 → 3386.02] from their end. Um, but it, because they were working with another incorporated entity to process
[3386.02 → 3391.66] the funding, it was a little bit easier, and they had their stuff worked out internally. And I think
[3391.66 → 3397.50] that's what tends to be the most helpful is when it's a corporation talking to another corporation
[3397.50 → 3404.38] and sorting things out that way, as opposed to like a corporation donating to a Patreon or an open
[3404.38 → 3412.38] collective. Um, I think open collective technically is a 501 C3. Um, and all the projects under its
[3412.38 → 3416.46] umbrella are physically sponsored projects. So it might work a little bit more smoothly.
[3416.88 → 3418.46] Open collective is a for-profit.
[3418.46 → 3425.48] Oh, okay. Cancel that. I am misinformed on the topic. Um, for the group I'm affiliated with,
[3425.48 → 3431.44] the parent organization is a 501 C3 and all the open source projects under its umbrella are
[3431.44 → 3436.12] physically sponsored entities. Um, so it tends to work out easier just because there is like
[3436.12 → 3442.82] an incorporated tax entity behind all of these open source projects. Um, I guess that is not the
[3442.82 → 3448.50] case for open collective, which is interesting because not how I understood it. Um, but yeah,
[3448.50 → 3456.80] someone on Twitter made the hilarious joke that, um, if a company has a fax number, then
[3456.80 → 3463.08] corporations will like move really quickly to work with it because it's supposed to be like established
[3463.08 → 3469.46] and prestigious. Um, kind of just a tongue in cheek comment about how companies like to work with
[3469.46 → 3474.28] older established organizations. So all you have to do to get funding for your open source projects
[3474.28 → 3479.64] is got a fax number, um, and start putting it on your letterhead and your read me.
[3479.64 → 3486.72] In the request, the request for commits podcast, um, you know, rest in peace. The, um, you know,
[3486.72 → 3495.80] there was a great episode about, uh, grants for open source work. Uh, and so, um, and it's,
[3495.80 → 3503.22] it's kind of, yeah, yeah, you can get grants, but, um, I was thinking, you know, I want to apply for a
[3503.22 → 3509.16] grant. And so I started looking into it, and it turns out like I wanted to apply for, what was it?
[3509.98 → 3515.50] Mozilla's thing. So Mozilla has a like an open source grant they give out. And it turned out it
[3515.50 → 3523.54] was really, they, they really did not want to give a grant to an individual. They only were really
[3523.54 → 3529.16] comfortable giving a grant to an entity of some sort. And so that, that's also kind of a
[3529.16 → 3536.06] stumbling block, I think for, for a lot of people. Um, you know, maybe, yeah, it's you, you, if you're
[3536.06 → 3541.46] just an individual, you're going to need to find some, some sponsorship, maybe by a foundation or
[3541.46 → 3548.18] somebody who wants to, you know, I don't even know how that works or why it is the way it is, but,
[3548.18 → 3553.54] um, that it, there's just, it's, that's kind of tough. Yeah. Well, and you know, there's lots of
[3553.54 → 3557.66] people trying to solve this problem because I think we acknowledge that it's a need, but the
[3557.66 → 3562.36] dollar figures that people are able to get to right now are still so low, right? Like if I look at open
[3562.36 → 3568.28] collective, the most successful project on open collective is web pack. I think largely because
[3568.28 → 3574.56] it had Sean Larkin doing incredible marketing for it. Um, and their yearly budget is just under
[3574.56 → 3583.84] $400,000, which is enough to pay for two full-time engineers, maybe three, maybe, um, you know,
[3583.92 → 3590.28] Tide lift is a fascinating, uh, proposition there, you know, sort of packaging things together
[3590.28 → 3594.56] and saying, we're going to provide professional support in a way that funds maintainers, Ada,
[3594.62 → 3601.44] Ada, Ada. I look for, you know, very popular packages on there, like Babbel, their monthly
[3601.44 → 3608.62] estimate of how much money would flow through to Babbel is $10. Babbel core is 40, um, Ruby on
[3608.62 → 3615.48] rails, $400 per monthly. So like, we're talking very small amounts of money here. And there have
[3615.48 → 3622.90] been a couple of folks who managed to support themselves with Patreon's, but yeah, it's, it's a
[3622.90 → 3628.56] rough market. Like there's, it's infinitely easier to get yourself a consulting gig. If you're wanting to
[3628.56 → 3633.90] do this type of thing, uh, you know, and be independent, which is what this involves. Um,
[3634.12 → 3639.28] so yeah, I don't, I don't know what the solution is. None of the, the attempts out there seem to be
[3639.28 → 3645.30] getting anywhere close to scale. I think some good action items for anyone who's listening, um,
[3645.72 → 3650.90] and does want to like to give back to the community or start to be more formal about this is start
[3650.90 → 3656.26] talking to your engineering management about figuring out a way to dedicate some of your time
[3656.26 → 3662.02] to contributing to an open source project in your stack. Um, it's probably going to take a lot of
[3662.02 → 3667.34] effort, but you know, depending on how management feels about it and how things work at your company,
[3667.34 → 3672.58] you can get into a position where you're spending a couple of hours a week, just contributing to
[3672.58 → 3678.74] open source. Um, that's one avenue if your company doesn't have the infrastructure to like to donate to an
[3678.74 → 3686.18] entity or all of that stuff. Um, and then also one of the things that I thought was fascinating
[3686.18 → 3691.56] is if you're using an open source project, just email people and ask them to come in for a training
[3691.56 → 3697.94] or a talk and pay them for it and have that serve as like a purchase they can make. If the contributor
[3697.94 → 3703.64] is willing, that always works as well. Um, so there are a lot of avenues for you if you're willing to
[3703.64 → 3709.66] advocate for it to, um, have your company engage and contribute to unhealthy open source ecosystem.
[3710.32 → 3715.82] And you can help without diving into code. There are lots of additional things like project
[3715.82 → 3722.40] management goes a long way in open source or even just triaging issues and being able to,
[3722.40 → 3727.44] you know, help somebody filed an issue. You know, does this have all the information we would need to
[3727.44 → 3730.78] reproduce it? All those different things. Like there are many, many ways to contribute.
[3730.78 → 3736.90] Yeah. That's a great point too. That's true. But at the same time there, you know, there isn't this
[3736.90 → 3743.98] like culture, uh, this like hacker ethos around project managers or seemingly designers as well.
[3744.16 → 3752.06] It's really tough to find somebody who's a designer who wants to, you know, contribute regularly. And, uh,
[3752.38 → 3758.04] yeah, that's, it's, it's interesting. We say like, yeah, we, we want this stuff, but I feel like
[3758.04 → 3766.04] some of that needs to come up from those, those industries or those professions. I don't know.
[3766.16 → 3772.62] Yeah. I think a big part of it is just starting to phrase open source contributions, not as, um,
[3772.78 → 3777.92] code contributions or whatever, but really as a way to build your personal brand and advance your
[3777.92 → 3785.00] career and your skill set outside the walls of a like corporate entity. Like the work you do in open
[3785.00 → 3790.14] source is your work and your way of showing your skill set and talent. And you don't need anybody
[3790.14 → 3796.44] else to like vouch for it or work in that ecosystem. So tying it into someone's personal brand and career
[3796.44 → 3803.22] is a great way to incentivize them to contribute to open source as opposed to just, Oh, come hack with
[3803.22 → 3806.78] us, which is, and might not necessarily suffice for a lot of people.
[3806.78 → 3812.02] I mean, that's cool. If you, if you have time, you know, after work to do it, but I mean, what I'd
[3812.02 → 3817.86] really love to see is, is this coming from, from the companies that, that gets so much value from,
[3818.12 → 3823.68] from open source, pushing their, you know, their project managers and designers and their technical
[3823.68 → 3829.62] writers and everybody else, you know, to, to contribute to these projects. I don't know. I don't know how to
[3829.62 → 3833.98] make that happen obviously, but I feel like that's, that's what should happen.
[3833.98 → 3841.26] I do have hope for the future as bigger companies, um, like Microsoft and Google start to be more
[3841.26 → 3846.28] visible about how they're engaging with open source. I think that kind of acts as a lighthouse
[3846.28 → 3855.16] and, um, like a model to follow for other companies in the industry. So I think overall there's hope.
[3855.54 → 3860.50] Yeah. Um, I, I think we do need to be very careful about how we're talking about this because,
[3860.50 → 3865.30] you know, talking about it as a brand builder is like, that falls into the same trap as like
[3865.30 → 3869.72] free internships, right? Like these are ways to get ahead. If you already have the privilege of
[3869.72 → 3875.42] having time and money to be able to do things. Uh, but we have companies making billions of dollars
[3875.42 → 3880.96] on open source software, right? And so long as we bill it as this is something that you're doing to
[3880.96 → 3888.66] improve, you know, to get ahead, we're leaving out huge numbers of people. And we're not, uh, sort of
[3888.66 → 3892.14] putting the responsibility on the people making money from it, right? Like that's an exploitative
[3892.14 → 3898.14] environment, just like free internships are. And I totally get free internships if you don't have
[3898.14 → 3902.96] any money, but tech companies have money. Yeah. I think they, so I should clarify this,
[3903.12 → 3908.42] the like personal brand thing was like not promoting free internships. I'm like very well aware of how
[3908.42 → 3913.66] exploitive open source can be. Um, but I think the important thing to know is that
[3913.66 → 3920.38] all of these different motivations can exist in a healthy ecosystem with each other. You can be an
[3920.38 → 3927.34] open, you can be a for-profit entity that funds time for your employees to work on open source because
[3927.34 → 3932.00] you care about their own brand and their own career advancement. You also care about some of the
[3932.00 → 3938.42] marketing and recruitment work that open source will help you do. Um, like there's a lot of ways to
[3938.42 → 3944.58] kill two birds with one stone or like multiple birds with one stone just by contributing to open
[3944.58 → 3949.58] source. And it's a way for you to benefit your company, um, to benefit the ecosystem, benefit your
[3949.58 → 3955.26] employees, benefit your recruitment efforts. It's like not just one thing. There's so many different
[3955.26 → 3962.44] ways to market it and look at it. And it's kind of just about who you're messaging. Um, and like,
[3962.44 → 3967.04] what are the particular benefits that you share with them? Because the message is different when
[3967.04 → 3972.06] you're trying to get Google to, you know, fund your project versus getting the government to fund your
[3972.06 → 3977.82] project versus getting a foundation, um, versus just like getting college students to be more
[3977.82 → 3982.32] engaged. Like there's all of these different, it's all marketing in the end. That's what I'm saying,
[3982.34 → 3988.00] I guess. Um, exactly. Yeah. I think, I, I think it, there are a lot of ways that can help people.
[3988.00 → 3992.00] Yeah. You're like the more, the older I get, the more I believe that life is all marketing.
[3992.00 → 3999.66] That's, I really think so too. That was a fascinating segment. Um, ran about as long as
[3999.66 → 4005.76] expected. And I think we learned a ton of different things, um, and had a lot of fascinating
[4005.76 → 4012.48] ideas come up. Thanks everyone for joining us on this edition of JS Party. Uh, if you have any links,
[4012.70 → 4018.74] uh, they will be down in the description, um, along with the transcript for this podcast recording.
[4018.74 → 4022.02] Thanks again for joining us, and we will see you next time.
[4024.68 → 4030.62] All right. Thank you for tuning in to JS Party this week. Tune in live on Thursdays at 1 PM U.S.
[4030.74 → 4035.66] Eastern at changelog.com slash live. Join the community and Slack with us in real time during
[4035.66 → 4040.72] the shows. Head to changelog.com slash community. And do us a favour, share this show with a friend,
[4041.02 → 4045.70] read us in Apple podcast, go into Overcast and favourite it. And thank you to Vastly,
[4045.70 → 4050.12] our bandwidth partner at the fastly.com to learn more. And we move fast to fix things
[4050.12 → 4054.72] right here at changelog because of roll bar. Check them out at rollbar.com. We're hosted on
[4054.72 → 4059.28] Leno cloud servers at the leno.com slash changelog. Check them out and support this show.
[4059.66 → 4064.00] Our music is produced by Break master Cylinder, and you can find more shows just like this
[4064.00 → 4067.32] at changelog.com. Thanks for tuning in. We'll see you next week.
[4067.32 → 4079.70] I'm Tim Smith and my show away from keyboard explores the human side of creative work.
[4079.96 → 4085.24] You'll hear stories sometimes deeply personal about the triumphs and struggles of doing what
[4085.24 → 4092.02] you love. I need to give myself permission to not overdo it. If I know that the weather forecast is
[4092.02 → 4095.66] perfect tomorrow and I don't have to do a podcast tomorrow and I could go to the beach,
[4095.66 → 4098.56] maybe I go to the beach, maybe I do something that does not work.
[4098.96 → 4103.90] New episodes premiere every other Wednesday. Find the show at changelog.com slash AFK
[4103.90 → 4105.70] or wherever you listen to podcasts.

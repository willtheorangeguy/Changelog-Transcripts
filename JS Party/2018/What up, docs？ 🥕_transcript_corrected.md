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
[56.42 → 63.94] Head to gauge.org slash JS Party to learn more and give it a try. Once again, gauge.org slash JS Party.
[63.94 → 82.62] Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays
[82.62 → 89.14] at 1 p.m. Eastern, 10 a.m. Pacific at changelog.com slash live. Join the community and slack with us
[89.14 → 93.90] in real time during the show at changelog.com slash community. Follow us on Twitter. We're
[93.90 → 96.74] at JSPartyFM. And now on to the show.
[99.74 → 105.56] Welcome to JS Party, everyone. Today's episode is super exciting. We're talking about, once again,
[105.66 → 110.48] everybody's favourite topic. I always feel like every time we come on, or I come on as MC,
[110.48 → 117.04] we're talking about a super fun topic. And today's topic is documentation. My working title for it
[117.04 → 120.24] was What's Up, Doc? Oh, nice.
[120.24 → 127.10] From the cartoons. But I don't know if Disney's going to come down and rain hell upon us for using that.
[127.34 → 130.12] I think it's worth finding out. I think we should try and see what happens.
[130.24 → 134.72] I know. We should test that. All right. So joining me today, we've got Nick Needed,
[134.72 → 141.66] got Chris, we've got Erode. Howdy, everybody. Hello. Hi. I want to just dive in with what I
[141.66 → 147.10] think is the most important question to answer whenever you're trying to start any documentation
[147.10 → 153.56] effort, whether it's in open source or in your company or wherever, which is how do you get
[153.56 → 160.30] people to actually care about documentation in general? We're all busy people, busy developers,
[160.30 → 164.70] and sometimes documentation is one of those things that's at the bottom of the list of concerns.
[164.72 → 169.90] And maybe not even on it. So how do we get people to put it towards the top and start
[169.90 → 174.46] dedicating more time and money to it? That was a tough question. It's okay if the answer is,
[174.52 → 179.16] we have no idea. Yeah, that's my answer. I mean, it seems kind of like
[179.74 → 187.34] getting your company to care about testing. That's maybe a little easier sell with all the
[187.34 → 194.22] studies around how an agile workflow and continuous integration can help you.
[194.72 → 205.84] But documentation, there just isn't that science there. It's tough. I have no idea how you get that
[205.84 → 214.54] to become important unless you build your organization out with a culture that says,
[214.74 → 217.34] you know, this is important to us and make it a core value.
[217.34 → 222.82] I think it starts with individuals. And I think specifically, you have to first convince yourself
[222.82 → 228.38] that this is important. And I think many of us fall down there. I know I certainly have in the past.
[228.62 → 235.20] Some of that is because I work on such small teams, in fact, often a team of one. So that documentation
[235.20 → 242.20] almost only exists either in my head or on inline comments, which, you know, are actually worth their
[242.20 → 248.58] weight in gold if they're contextual and not out of date over time. So that's one way of like slowly
[248.58 → 253.26] convincing yourself that documentation is worth it is to return to your code after six months,
[253.40 → 258.74] eight months, 12 months, and realize that it's insufferable. And you cannot understand what's going
[258.74 → 265.52] on without some good inline documentation and then branching out from there. But we also have to
[265.52 → 272.52] convince ourselves that it's worthwhile. And like you said, Safia, or maybe it was Chris, the ROI or
[272.52 → 279.62] like the benefit is not super tangible or immediate. And a lot like with tests, although like you said,
[279.68 → 287.70] with tests regressions, eventually upper management or the decision makers realize, okay, this is going to
[287.70 → 292.12] reduce our total cost of ownership. I wonder if there are such studies around documentation,
[292.12 → 296.12] but I think we have to convince ourselves first. And that can be sometimes very hard to do as well,
[296.12 → 301.44] because it's not the funnest thing to do. It's often the last thing that we do. And if we're not
[301.44 → 307.26] writing our stuff specifically for a broad audience, we often think, you know, do I really need this?
[307.36 → 310.72] And the answer is lots of times yes, even though we tend to decide no.
[311.26 → 316.74] Yeah, you bring up a good point that I started to think about, which is what are the financial returns
[316.74 → 322.30] for having good documentation for your code base. And I don't know, again, if there's anyone who's
[322.30 → 327.20] done anything quantitative around this, but I imagine that when you're thinking about onboarding
[327.20 → 333.10] or implementing new features or refactoring, the more documentation you have, the less time those
[333.10 → 339.60] like very pricey developers spend trying to figure out how to do something and more time they spend
[339.60 → 343.86] doing it because the documentation is already there. Again, I'm not sure if there's any,
[343.86 → 350.78] you know, solid research on that. But if anyone is listening live and has heard of some research
[350.78 → 356.68] around this topic, let us know on the Slack or on Twitter. I'd love to see more and learn more
[356.68 → 359.12] about something more rigorous evidence for that.
[359.42 → 363.86] I think it's important to point out there's, you know, there's internal documentation and then
[363.86 → 370.60] there's, you know, client facing, this is how you consume our API type documentation. And
[370.60 → 378.62] I can see those being two very, two very kind of different efforts with different people involved
[378.62 → 381.52] and, you know, different priorities.
[382.18 → 386.62] And I think the one thing that, that becomes a problem is, is once you convince yourself that
[386.62 → 391.24] you need the documentation, and you get it written, and it's all nicely written, things don't stay the
[391.24 → 397.24] same. So things will change over time. And there's oftentimes not really an automated way to
[397.24 → 403.78] know whether the documentation is updated or needs updating. And so then it becomes just this
[403.78 → 409.60] terrible thing, this terrible black box out in the world that may or may not be accurate.
[409.84 → 415.08] And nobody really wants to go spend the time to update it because it's often very verbose and
[415.08 → 416.36] just a lot of work.
[417.06 → 419.66] The only thing worse than no docs is wrong docs, right?
[419.94 → 420.18] Yeah.
[420.32 → 420.68] Right.
[420.68 → 421.32] Yeah.
[421.60 → 421.80] Yeah.
[421.80 → 430.16] We, um, found at an old company of mine, it was, we, we had a very complex, uh, software
[430.16 → 438.64] project, uh, product. And, um, you know, we had people doing, uh, basically guides or tutorials.
[438.64 → 445.44] Um, it's, you know, it's reference documentation, it's how to be, uh, and a big part of this would
[445.44 → 452.82] be creating actual, like, here's a screenshot. Here's even a video in some cases of how you
[452.82 → 460.72] get X thing done, but it doesn't scale when you're developing rapidly. It, it, things need
[460.72 → 466.40] changing all the time. And so, you know, the, the faster you want to release, well, uh, you're
[466.40 → 472.62] going to be waiting, um, for the documentation team to make their new screenshots. And, and,
[472.62 → 481.24] oh, oh my God. No, it's, that's difficult. And I think at some level it, it means, um,
[481.48 → 486.42] well, you know, your user interface, maybe you shouldn't be making software that that's
[486.42 → 492.18] so complicated, you know, uh, and, and, and have a user interface that's, that's much more,
[492.18 → 498.72] um, kind of discoverable and obvious, but that's kind of a that's a barrel of something.
[498.72 → 502.66] So I was thinking about this and I actually saw a funny tweet this morning from Khalil
[502.66 → 507.38] tweets, um, who is a JavaScript developer. Maybe you'll know him from, is it nested loops?
[507.54 → 513.90] The, the reggae style JavaScript band that performs at JS comp sometimes, uh, interesting
[513.90 → 518.54] guy. And I think he's on the reactive podcast, which is pretty cool as well. And, uh, it was
[518.54 → 522.90] just timely. So I, I jotted it down. He said, it turns out not writing documentation when
[522.90 → 527.88] you write internal libraries creates a huge hurdle for onboarding developers who knew.
[528.84 → 533.44] And, uh, that's a fact. And as you don't, you only, you only learn that in retrospect,
[533.44 → 538.60] right? When you see those new developers coming in and fumbling over things for too long, because
[538.60 → 542.50] you assumed your internal libraries were self-documenting code or whatever we tell
[542.50 → 544.90] ourselves. Um, and that comes back to bite you.
[544.90 → 550.30] Yeah. On, on Dojo, we, um, when we hire on new developers at Site Pen, we, uh, do have
[550.30 → 554.66] them go through the Dojo documentation, and we do often learn a lot from that and, and get
[554.66 → 562.28] tweets or not get tweets. We get PRs made to, to our repos. Yeah. Uh, but we, we've also
[562.28 → 567.82] kind of like the benefit of having it be in the open, uh, like with an open source project
[567.82 → 573.72] is that you get to, um, kind of outsource that a little bit too. So, uh, like we have a
[573.72 → 578.22] discord set up, and we'll often get, you know, I tried to do this step in the documentation
[578.22 → 582.70] or in, in the tutorial, and it didn't work. Can you help me out? And we can often, it
[582.70 → 586.78] helps us find, to pinpoint the locations where things are wrong and then isolate those
[586.78 → 593.00] and fix them. But that's not something that can happen on closed projects. So there's
[593.00 → 593.44] problems there.
[593.44 → 598.18] Yeah. I've had experience with documentation in both the open source ecosystem and then
[598.18 → 603.36] like on projects and internal work and stuff like that. And it's always easier to make
[603.36 → 609.82] documentation a big effort in the open source ecosystem because a it's often big companies
[609.82 → 615.32] who are consuming your open source library. So when they are the ones who have to come
[615.32 → 619.96] in as the outsiders to figure out how to use something, they're way more invested in funding
[619.96 → 625.72] or supporting work to document it. And then B, there's tends to be like a more, I guess,
[625.78 → 631.36] like fun and welcoming culture around documentation and open source. There's like conferences, like
[631.36 → 636.90] read the docs or, um, I know projects that have done things like documentation sprints where
[636.90 → 641.24] everyone just comes in for a sprint. That's like a week long and nobody writes any code.
[641.42 → 646.70] All you write is documentation. It doesn't matter if you're an ACE developer or a designer or
[646.70 → 651.70] whatever, everyone's just focused on writing documentation. And I don't think there's that
[651.70 → 659.52] same kind of need and B like structure and methods for pushing for through documentation
[659.52 → 666.00] in closed companies. One of the best companies I've worked out where they had really great
[666.00 → 673.82] documentation was at a large financial institution. Um, and I remember I was 17 years old. I'd gotten an
[673.82 → 680.10] internship as a software engineer with this company the summer before I started college. And on my first
[680.10 → 685.86] day there, they linked me to their documentation page, and they had literally like every line of
[685.86 → 692.62] code, every concept, every tool, everything outlined in their organization. And then they also not just
[692.62 → 699.62] had the code documented, but also kind of the financial and the non-technical side of things documented
[699.62 → 704.80] too for their engineers. And for them, it was twofold. They were doing a lot of hiring and working with
[704.80 → 710.78] contractors. So they needed that documentation in place to like to have people on board very smoothly
[710.78 → 715.88] and get, be productive quickly. Um, but there was also another interesting dimension to it was that
[715.88 → 721.60] it was kind of part of their auditing process where they would have to show this documentation or have
[721.60 → 727.42] documentation written out for the software that they produced. Um, whether it was like internally or
[727.42 → 732.18] for external customers. So there was like that, I think that was, there's that interesting pressure when
[732.18 → 737.76] you have like an external auditor coming in and documentation is one of the things they look at
[737.76 → 743.00] when they're trying to figure out if you're up to compliance or standards. Um, so maybe that's what
[743.00 → 748.84] we need. We just need a giant body to come in and audit everybody and make sure you have docs written.
[749.24 → 753.56] No, thanks. I was, I was obviously joking about that. That'd be horrible.
[753.90 → 758.52] Curious if you think that the auditing was the, the impetus or the, the reason for the documentation
[758.52 → 764.30] culture, or if that was something that perhaps emanated down from the founders or just from your
[764.30 → 768.78] own, you know, your take from an, from an intern's perspective, like where did that culture come from?
[768.82 → 771.76] Did it, was it there from the beginning? Was it there because of auditing? What was the actual
[771.76 → 772.96] reason for it?
[772.96 → 777.88] It definitely felt like a big part of it was for auditing. One of the things that struck me about
[777.88 → 782.60] the organization in general was that so many of the technical decisions that were made and like the
[782.60 → 789.74] project management decisions were dependent on like auditing requirements and compliance and
[789.74 → 796.74] regulations and Ada, Ada, Ada, Ada. It was like a whole other world where, um, and I think in
[796.74 → 801.74] that situation where it's like, like in the world of finance, it's completely rightful for them to have
[801.74 → 807.72] a lot of regulations and compliance to uphold, but that was a huge impetus for a lot of the decisions
[807.72 → 812.84] they made around documentation and testing and what kind of, I don't know, this is probably a
[812.84 → 817.08] common one that people have heard of, but what kind of open source packages they use and stuff
[817.08 → 817.54] like that.
[818.12 → 821.80] So I'll call Chris here in the chat room, uh, since you're also here on the call, Chris,
[821.84 → 828.16] talking about test suites as kind of, a proxy or maybe a low fidelity documentation that at least
[828.16 → 835.86] has the advantage of less likely to be outdated versus pure pros. You want to expand on that,
[835.86 → 838.94] Chris, or does that pretty much explain what you're talking about there in the chat room?
[839.48 → 846.46] Um, yeah. So, I mean, I mean, uh, you mentioned that the, the tweet about, uh, you know, we're not
[846.46 → 853.32] writing documentation, um, you know, creates a problem for onboarding people. Right. And somebody
[853.32 → 860.64] in that thread mentioned that, you know, you, that basically they ask, you know, is what's the
[860.64 → 865.92] matter? Aren't the aren't the tests good enough? And, you know, the, you know, you just run it.
[865.98 → 870.92] Well, they don't really replace like actual documentation, but I mean, however you feel
[870.92 → 876.98] about that, I don't, I don't really have an opinion, but I mean, assuming your test coverage
[876.98 → 884.12] is good, it's often more, you know, it, it, and, and your, your build is green. Then the tests
[884.12 → 895.54] reflect reality. Well, there's, there's nothing, um, that says the, the English or, or in whatever
[895.54 → 903.44] language that, that you're describing your API with, um, is, is necessarily correct. Uh, there's,
[903.62 → 911.80] there are ways to, you know, run CI against example code and, and that would be a good way to catch
[911.80 → 918.60] problems. Um, and, and suggest to somebody working on the documentation that, you know,
[918.66 → 924.72] this, this area needs to be updated because the examples broke. So I need to readjust my
[924.72 → 929.72] assumptions about how this work and works and maybe, um, you know, change my phrasing or, or
[929.72 → 935.46] whatever I need to do to, to, to change the description of the, of the, uh, of the API surface.
[935.46 → 943.70] But there, there's nothing, there's no like automated tooling to make sure your documentation
[943.70 → 947.96] is, um, current and correct in that way.
[948.70 → 952.58] That comment brings up a fascinating distinction. The comment specifically about,
[952.78 → 956.60] well, you know, our, isn't your test suite good enough documentation for your code base.
[956.84 → 962.28] And I think it helps to determine whether it's an open source project or an internal project,
[962.28 → 968.04] what is the audience and the goal of the documentation? Because I think what tests replace
[968.04 → 975.60] is like API documentation. Um, and then you've got other types of documentation that your project
[975.60 → 981.06] might need, which is things like reference guides or like play by play tutorials and things like that.
[981.24 → 987.64] And so I often think, I think it's not a gap of like documentation in general, although that is
[987.64 → 993.52] the case, it's more about a specific type of documentation that doesn't exist because people
[993.52 → 998.82] aren't aware of the audience that they need to serve with that documentation and what the goals
[998.82 → 1003.78] of that audience are. Um, so I think it's, it's, it's interesting because you have to kind of exercise
[1003.78 → 1009.30] this whole other part of your brain. That's all of those kinds of writing principles you learned
[1009.30 → 1015.10] from elementary school onwards, like figure out who your audience is, like learning what they want,
[1015.10 → 1022.40] um, appealing to their emotions, catering your language to them. Um, and all of that stuff,
[1022.44 → 1028.70] which I think is interesting and a kind of fun break away from the coding part of things. Um,
[1029.18 → 1034.70] but, but yeah, that's been my observation is that it tends to be more about figuring out what,
[1035.32 → 1040.00] who the people who are going to be reading your documentation are and what it is they want
[1040.00 → 1045.40] and moving from there. I was just thinking about this, this premonition of somebody asking,
[1045.40 → 1049.88] aren't your, isn't your test suite, you know, somewhat good enough to be your documentation
[1049.88 → 1055.16] to that. Perhaps I would say, what test suite are you talking about? What is, what are these tests
[1055.16 → 1061.30] you're referring to? Or it's often the case where you come in on a project and the tests aren't,
[1061.42 → 1066.96] not all of them pass. And people just don't even rely on, like they don't rely on it at all. So that's,
[1066.96 → 1070.56] that's another problem. It's like outdated docs, right? Tests that don't pass and you just,
[1070.68 → 1073.90] you just ignore them. Well, that one's been failing for months. Just leave it.
[1075.86 → 1081.66] It's just a flake, right? A 10-month-long flake. And then there's the case where your tests,
[1081.84 → 1087.12] although your coverage number might be pretty high, your tests are actually not a good reflection of
[1087.12 → 1092.98] the like intricacies of your API. Because I think that's sometimes where it might be at odds. Like you
[1092.98 → 1097.96] might be covering lines of code and like branch statements, but you're not really getting at,
[1098.38 → 1102.68] like, I don't know how I feel about that statement that tests are documentation. Because I don't think
[1102.68 → 1109.64] there's like things that are in people's brains that aren't captured by tests, even good coverage
[1109.64 → 1114.38] tests. Yeah. I'm not explaining myself very well right now, but hopefully you all and everyone
[1114.38 → 1119.12] listening understands my like jumbled words. And the test might not be written in a way that you would
[1119.12 → 1123.14] really interact with, with that code. They might be like, like unit tests, for example,
[1123.14 → 1128.62] would be trying to test a single unit. And that may not be how you, you necessarily work with it.
[1128.66 → 1134.18] And maybe the code doesn't have higher level tests, like integration that they can look at,
[1134.20 → 1138.06] or they don't have them with as much fidelity as, as the, the unit tests, for example.
[1138.52 → 1140.00] Yeah. That's a great distinction.
[1140.34 → 1144.08] Maybe we can get into this during the tooling section, but I am thinking of at least one or two
[1144.08 → 1148.74] efforts out there. I'm going back to this idea of, you know, really documentation that stays
[1148.74 → 1153.74] up to date and perhaps is executable or has, I think there are tools that where you have,
[1154.18 → 1161.30] at least for inline docs, um, contracts between the documentation and the functions that are
[1161.30 → 1165.80] exercised. And like Chris, you were talking about working that into CI. I know there are efforts there.
[1165.86 → 1168.38] I can't think of what they are at the top of my head. Maybe I can find during the break
[1168.38 → 1175.24] where people are actually having this, uh, relationship between the code being described
[1175.24 → 1180.98] and the, uh, comments or the document, the inline docs that are right above it. And you can actually
[1180.98 → 1185.76] run those through and, um, at least make sure they're not wildly outdated. Kind of cool.
[1186.06 → 1190.08] Yeah. I know exactly what you're talking about. And I also can't think of the name, which is
[1190.08 → 1192.12] rather unfortunate in this case.
[1193.34 → 1198.50] That being said, we are about a third of the way through, and there's a lot to discuss and share.
[1198.50 → 1202.78] Uh, we're going to take a break, but right after the break, we're going to start to answer a question
[1202.78 → 1207.14] that's probably musing in you all's mind, which is, let's say you've got everybody committed to
[1207.14 → 1211.90] documenting some code. Uh, what are some tools you can use to start making the documentation
[1211.90 → 1216.52] effort easier in your code base? Um, all that is right after the break.
[1216.52 → 1227.86] This episode is brought to you by our friends at Rollbar. Check them out at rollbar.com slash
[1227.86 → 1233.32] changelog. Move fast and fix things like we do here at changelog. Catch your errors before your
[1233.32 → 1238.54] users do with Rollbar. If you're not using Rollbar yet, or you haven't tried it yet, they have a special
[1238.54 → 1246.44] offer for you. Go to rollbar.com slash changelog, sign up and integrate Rollbar to get $100 to donate.
[1246.52 → 1252.50] Open source projects via open collective. Once again, rollbar.com slash changelog.
[1265.22 → 1270.36] And we're back in the last segment. We talked about how you can get people to start caring about
[1270.36 → 1275.10] documentation in your organization. Now we're going to talk about something else. That's also
[1275.10 → 1280.00] interesting, which is what kind of tools can you start to use to make writing documentation easier
[1280.00 → 1286.14] and get people to adopt it more readily? So anyone have recommendations for documentation tools they
[1286.14 → 1291.30] like in particular? I think Markdown has been phenomenal for documentation. It makes it so easy
[1291.30 → 1297.26] to, to write docs that look good and have syntax highlighting, uh, specifically with like GitHub
[1297.26 → 1302.42] readies and, and things like that, but it just makes it really easy to have decent looking docs from the go.
[1302.42 → 1310.30] One of the ones that I wrote down was style guides, which is a documentation tool for react components.
[1310.30 → 1318.64] And it allows you to spin up a live server and develop your React component and document it using
[1318.64 → 1324.14] a Markdown file, um, in one go. Um, and the place where I've had experience with that is actually in
[1324.14 → 1329.94] the open source project I helped maintain called interact. We've got style guidance documentation set up for
[1329.94 → 1335.98] react components. And one of the biggest benefits of it actually ended up not being related to documentation
[1335.98 → 1344.34] at all, but related to getting new contributors onto the project, because what it allows us to do is spin up a
[1344.34 → 1351.80] quick live server with the documentation where new contributors can start to fix bugs or add features to a single
[1351.80 → 1359.60] component in a silo away from wherever that component is used, um, in the app. And that makes it really easy
[1359.60 → 1365.16] for people to focus on the things that need to be fixed or addressed. Um, and not have to worry about like,
[1365.24 → 1370.48] Oh, you know, this component is used here. So I have to go in this file to fix it. No, it's just,
[1370.88 → 1376.40] here's the component file. Here's the Markdown file. Here's the command you run to set up your live server.
[1376.40 → 1380.78] Be free. Write the docs, write the code. It's like magical.
[1381.86 → 1386.02] Fly little bird. I, this is really cool. So I haven't seen this yet. So I'm just over here
[1386.02 → 1392.44] kind of munching on its, uh, docs or at least it's sales pitches on the homepage. And, uh, I think,
[1392.48 → 1398.46] I mean, just the React, the component style development, I think has been a boon for opening
[1398.46 → 1405.38] up tools like this. Um, isn't there a storybooks tool as well? And just like this idea of interacting,
[1405.38 → 1412.78] uh, with the code and the output product, as well as reading the documentation in line. Uh, it also
[1412.78 → 1418.10] reminds me a little bit of, uh, literate programming. Is anybody familiar with the concept
[1418.10 → 1422.88] of literate programming? It was gaining steam, I think probably five or 10 years ago with people
[1422.88 → 1428.46] like Jeremy Askesis and others, but I haven't heard about it recently. Is this something you all are
[1428.46 → 1434.80] familiar with? Uh, no. Yes. It's the notion of kind of, I might be familiar with it in one specific
[1434.80 → 1439.02] context, but I'll let you explain it for everybody else. Yeah. So, I mean, I am, I'm,
[1439.02 → 1443.88] I'm only a surface level familiar with it as well. I've, I guess, consumed some literate programming.
[1443.94 → 1448.92] I've never tried to write it, but I think it was Don Knuth that, uh, that invented it or at least
[1448.92 → 1454.16] described it. And the idea is that the program should tell a story much like you would write
[1454.16 → 1464.24] a novel or a narrative. And so, um, alongside interspersed with the code is snippets and
[1464.24 → 1471.56] examples and prose, uh, that really kind of weave a story to describe what this code is doing. And
[1471.56 → 1478.66] the, the programs that I've seen documented in this way have been, um, it's almost an art. I think
[1478.66 → 1483.06] that's probably the reason why it's, it's talked about and done, but isn't like massively used.
[1483.06 → 1488.94] Um, but we'll definitely link to more information on that in the show notes, but just looking at the
[1488.94 → 1493.48] react style guide, and I think the most popular project that I remember that was documented in
[1493.48 → 1498.64] a literate programming style was coffee script, or maybe it was underscored. So Jeremy Askesis,
[1498.86 → 1505.02] uh, was the creator of underscore JS and coffee script. And he was a big proponent of literate
[1505.02 → 1508.94] programming. So you'll see some of his stuff documented in this way. And if I can find one,
[1508.98 → 1512.16] I'll show throw that in the show notes too, because it's definitely a different style and something to
[1512.16 → 1517.48] appreciate. I think it's very difficult, much like writing a novel, it's very difficult to weave a
[1517.48 → 1523.34] tail around your code and not exactly agile as, you know, as your software changes, if I'm sure your
[1523.34 → 1529.10] story must change as well. But that being said, seeing this React style guide and seeing the
[1529.10 → 1534.50] the description kind of right in there with the code and with the examples, it reminds me at least
[1534.50 → 1536.08] of this style of docs.
[1536.72 → 1543.36] I've, I've seen, um, that style literate, the literate style, um, of documentation, and it's
[1543.36 → 1550.30] pretty cool. But if we're having trouble getting people to write documentation at all, um, literate,
[1550.34 → 1557.30] this literate programming, it just seems like another level, a higher level of effort that,
[1557.30 → 1564.04] you know what I mean? It's just, it's, as Jared said, it's, it looks harder.
[1564.50 → 1567.22] Than just even writing basic docs.
[1567.34 → 1570.72] That's why I think I appreciate it. It's like an aspirational documentation.
[1571.12 → 1575.38] I can provide a little bit of insight. So it's hilarious that you mentioned that because
[1575.38 → 1580.50] the open source project that I maintain is actually a project called Interact, which is,
[1581.06 → 1587.36] we call it an interactive notebook app. Um, but the idea is that you can, it's a desktop application.
[1587.36 → 1595.02] There's also a web app version, and you can build literate programming documents. So you can have,
[1595.02 → 1604.16] uh, notes in as first with executable code cells that, um, you can run as like code that you would
[1604.16 → 1609.98] usually run. And the way that it's mostly used actually is not by programmers, but by like data
[1609.98 → 1616.68] scientists and analysts to document their analytics code. Um, so when you're, you know, doing some kind
[1616.68 → 1620.46] of research, and you've like written up some script to do some math or something like that,
[1620.46 → 1627.46] you would use literate programming to explain, you know, how you derived the math, how you drive the
[1627.46 → 1631.98] parameters for the particular code that you're writing. And just kind of like, it's almost like
[1631.98 → 1640.64] writing a proof for, um, math problems. Um, and did I hear a few people just shudder because of the
[1640.64 → 1645.46] fear? Um, no, that was just an interesting comparison. But now that you mentioned it.
[1645.46 → 1654.14] Yeah. So I would say I, I think of the context I've seen it used most is not to document like APIs,
[1654.14 → 1660.78] but it's more to document like references or situations where you're actually using a particular
[1660.78 → 1668.74] library. Um, or I guess here's a good way to put it where most of the effort to come up with a
[1668.74 → 1674.40] particular bit of code is like behind the scenes and situations where you're like doing machine
[1674.40 → 1679.02] learning, and you've done like a lot of parameter tuning beforehand, and you figured out what parameters
[1679.02 → 1684.18] you need for a particular model. And now you need to write some plain text in English to explain that
[1684.18 → 1689.90] to whoever's reading it. Um, and, and things like that. So I think it's got like a time out of place.
[1689.90 → 1694.12] I'm a big advocate for it, obviously, because I work on this open source project, but I think it's a
[1694.12 → 1699.48] fascinating paradigm. Um, not just in the example I gave you, but also in early education,
[1699.48 → 1705.80] um, teachers really like using it when they're teaching kids how to code, cause it allows you
[1705.80 → 1710.46] to kind of like, you know, make a worksheet that explains what a particular piece of code is and
[1710.46 → 1716.50] have, um, your students fill in the code that they need to program and all that. Um, so I guess just
[1716.50 → 1721.40] the it's, it's, it's one of those things where I think it's got applications outside the world of
[1721.40 → 1726.86] engineering and more in the world of where like other disciplines start to interact with software.
[1727.44 → 1734.38] If it's good for early learners, um, do you think it would be good for, um, you know, just
[1734.38 → 1741.72] tutorials, I suppose, or, or writing guides or, or maybe even something like in the way that people
[1741.72 → 1750.50] use glitch now? Um, what I mean, would that be something that, I mean, it's, it seems like if
[1750.50 → 1755.26] you want to run one of these things, you can run a Jupiter. I mean, cause this is Jupiter based.
[1755.66 → 1762.72] I mean, if you have this like workbook, can you run it? Like you probably just can't run it on your
[1762.72 → 1767.74] web, like documentation website, right? You'd have to download the runtime and all that.
[1767.74 → 1774.56] There are, um, there's a service called binder, which is basically just kind of like, um, a backend
[1774.56 → 1779.92] as a service for these types of documents that allows you to connect to all the like compute
[1779.92 → 1784.88] resources that you need, um, and the execution resources that you need to run it. And, um, the
[1784.88 → 1790.80] way I've seen it applied is when somebody is like running a tutorial workshop on like a package or
[1790.80 → 1796.02] something at a conference, they will write up their tutorial in a Jupiter notebook, put it up on the
[1796.02 → 1801.86] web, spit it up to point to binder, which is this like, um, resources, a service, I guess. And then
[1801.86 → 1807.24] just have folks interact with that. So you can run it in the cloud. Um, and I think there's like
[1807.24 → 1813.10] Azure has a service where you can run notebooks in the cloud too. And it's getting to be like
[1813.10 → 1815.48] pretty integrated with different cloud providers too.
[1815.80 → 1821.78] Yeah. There's this also this thing that NPM seems to partner with called run kit. Like it used
[1821.78 → 1827.30] to be called something else. I can't remember, but, um, yeah, whenever you view a module on
[1827.30 → 1835.28] npmjs.com, you can click like try it in run kit and it, it will load up like, um, I don't know,
[1835.28 → 1844.14] some example code in this essentially a notebook. Um, I don't, I don't know. This is probably
[1844.14 → 1851.00] unrelated to, to Jupiter, but it's a kind of similar idea, but I mean, I haven't seen people
[1851.00 → 1858.26] use this sort of thing very often. So maybe there's something that is preventing people from
[1858.26 → 1863.42] wanting to use a notebook for, for guides and tutorials.
[1863.78 → 1869.12] Yeah. I know it's pretty popular in the Python world. So it might just be a methodology that
[1869.12 → 1874.76] hasn't been completely translated to JavaScript yet, but I'm working on that. Um, so yeah.
[1874.76 → 1882.44] One of the aspects or the characteristics of the Python community is a huge emphasis and, uh, on
[1882.44 → 1888.28] spectacular docs. And so if anything, you know, I love the idea of prop, uh, cross propagation of
[1888.28 → 1893.00] ideas, like the good stuff, like let's spread that around to all these different environments. Right. So,
[1893.00 → 1899.08] um, if, if us JS folks could steal anything from the Python folks, it would be their documentation,
[1899.08 → 1905.78] not just the results, but just how much they value it. And I think read the docs is, is a great example
[1905.78 → 1910.34] of that. So what about more traditional things? I mean, isn't everybody, I mean, for API docs or for
[1910.34 → 1917.72] library documentation, um, Chris, you have Mocha is, is Mocha documented with like JS doc. Is that like
[1917.72 → 1923.90] still what people use pretty much? Um, is it up to snuff? What's the situation for kind of traditional
[1923.90 → 1931.26] library or, um, like a library API and not like a rest API style docs? Is it still JS doc? Uh,
[1931.26 → 1942.00] essentially, I mean, JS doc popularized this idea of doc, doc strings or, and, and tags in your, um,
[1942.62 → 1949.06] in your document. And so you'll use a multi-line comment and then there you'll have at something,
[1949.06 → 1958.18] um, like at, um, I don't know, parameter and you can use this tag and describe your, your parameters.
[1958.18 → 1966.90] And so there's, there are a few things. So JS doc has been around for a long time and, um, you know,
[1966.94 → 1974.28] it's, it's, uh, it has issues like as a so it's, it's, it's two things. It's, it's kind of like a
[1974.28 → 1983.10] specification for, uh, these tags you can use, but it's also, um, a thing which you give it your
[1983.10 → 1989.28] code and it, it, it poops out documentation. And so it's, it's problematic as a tool because it's,
[1989.38 → 1995.46] you can't really consume it programmatically. Anyway, it's just, people have tried to write a
[1995.46 → 2003.94] replacements for JS doc, but it, it, it's the, the problem space in JavaScript, especially, um,
[2003.94 → 2010.70] because it's a dynamic language is its difficult enough that all of this institutional like
[2010.70 → 2015.36] knowledge or whatever you want to call it, uh, the, the, the problem domain that, that, that
[2015.36 → 2024.18] JS doc has kind of attacked over the, over the years is, is so wide and, and, and complicated that
[2024.18 → 2030.50] these newer projects that are trying to do the same thing are really having a tough time. Um, I think
[2030.50 → 2037.02] getting the, the coverage, uh, across all of these different tags. And so, um, you know,
[2037.06 → 2042.52] even some projects have written custom tools to, and, and, you know, they'll, they'll define their
[2042.52 → 2048.60] own custom tags. Like for example, um, Angular, I remember this is the first one I saw. So Angular,
[2049.18 → 2058.26] I don't know, one or what have you, um, they wanted to document, right? And so Google had, uh,
[2058.26 → 2066.12] Google closure, which, uh, it was a compiler, but it's also consumed these JS doc tags. And I don't
[2066.12 → 2073.14] quite understand the history of that, but for, for reasons, um, you know, it, I think it was that
[2073.14 → 2079.50] the dependency injection model didn't really make a lot of sense to what JS doc was doing. Um,
[2080.38 → 2087.00] Angular had to write its own tool kind of, and, and have its own doc strings, and it would parse its,
[2087.00 → 2094.64] its source code and, and output it out, output its own API documentation. And it was so specific
[2094.64 → 2101.16] such that if you were writing an Angular library or third-party module, you couldn't really consume
[2101.16 → 2107.86] what the Angular team was using to, to describe their own code. And so it's, it's just a really
[2107.86 → 2113.80] difficult problem with JavaScript to generalize and get coverage and be able to describe in these tags
[2113.80 → 2118.04] because JavaScript is so expressive, like everything that your language can do.
[2118.74 → 2124.94] So, um, TypeScript though, like in, in flow and that sort of things, I haven't seen too many tools
[2124.94 → 2129.90] around it, but I can only imagine the stories better there simply because you have types and
[2129.90 → 2135.02] because you have types, and they're, you know, they're kind of self-documenting and all this,
[2135.12 → 2141.38] um, that solves quite a few of the problems. And I would imagine it's much easier. Um,
[2141.38 → 2147.32] essentially, I mean, I, I can only guess because I haven't seen any code or anything to generate
[2147.32 → 2153.36] API documentation from, from TypeScript sources, um, then from, from JavaScript, because all you have
[2153.36 → 2160.74] in JavaScript are just these doc tags or these tags and these doc strings, you know, from JS doc a long
[2160.74 → 2168.40] time ago. You know, this probably JS doc came, came out probably ES3 era. Um, and it's hard to evolve
[2168.40 → 2173.60] ever since then, you know, it's, uh, it's a it's a tough nut to crack for JavaScript. And I don't
[2173.60 → 2180.94] think there are really, um, there's no, there's no really killer tool that's come out since that has
[2180.94 → 2187.88] just kind of disrupted for lack of a better word, you know, what JS stock is doing. And so Mocha uses
[2187.88 → 2195.14] JS stock. Um, it works okay. You know, I'm not in love with it, but we have some API documentation,
[2195.14 → 2201.14] which is automatically generated from, from our doc strings and our code comments. And that's cool.
[2201.26 → 2206.68] That's actually a fairly recent addition. We had the doc strings, but we've nobody ever bothered to
[2206.68 → 2212.26] run it through the documentation generator. Um, it'd be nice to have, you know, something that,
[2212.26 → 2217.88] I don't know, it seems to work well enough for our means, but I can definitely see, you know,
[2217.88 → 2225.98] maybe if we wanted a more flexible template and things like that, uh, because just doc is really
[2225.98 → 2233.12] the whole, it's the whole can of worms. It's, it's input, output, emulating, et cetera. Um, so
[2233.12 → 2237.62] that's, that's the story I have for Mocha and, uh, JS stock.
[2238.00 → 2242.22] I can speak to TypeScript a little bit, uh, because it is a little bit of a different story there,
[2242.22 → 2247.76] uh, better or worse, but there, there is a tool called type doc that is very much the
[2247.76 → 2253.32] the JS stock syntax, but, uh, you don't have to fill out nearly as much because it can just ask
[2253.32 → 2258.20] the TypeScript compiler, what, what's this type? So if you're like naming the parameters, uh, you can have
[2258.20 → 2263.16] a code comment above your, your function and then say at parameter, and then just give a description of
[2263.16 → 2267.54] what that is. And it will figure out, Oh, that's a string or that's a Boolean or whatever, uh, based on
[2267.54 → 2272.20] the types. Um, and that's really cool. The TypeScript compiler itself has,
[2272.22 → 2277.58] um, the ability to, to like to pass it a token and say, give me JS stock comments for this,
[2277.58 → 2282.32] if it has any, and it'll return you the JS stock comments. And then you can parse that yourself
[2282.32 → 2288.00] if you're just using the compiler API. So it's, it's easy to, to build out tools and then, um,
[2288.30 → 2293.08] kind of going back to JavaScript a little bit, the TypeScript compiler itself can take JS stock
[2293.08 → 2298.16] style comments and actually infer from that the types in your JavaScript code. And I know that that's
[2298.16 → 2301.96] what, I think that's what a web pack is doing where they're adding JS stock style
[2301.96 → 2306.60] comments with types about everything. And then they're getting the, uh, type support that they
[2306.60 → 2311.86] need without converting fully to TypeScript by having TypeScript parse the JS stock comments for that
[2311.86 → 2312.36] information.
[2312.56 → 2318.74] I'm curious to know with type doc, do you know if there's a good support for generating documentation
[2318.74 → 2326.78] from, um, TS stock strings in a mono repo of packages? This is a very specific problem that I've
[2326.78 → 2331.76] been running into since yesterday, trying to get JS stock to run against a mono repo.
[2332.14 → 2336.60] It has been a while since I've looked at it. So I, I can't really speak to that, unfortunately.
[2337.06 → 2341.30] Okay. But yeah, when we talk about some of the problems with JS stock, that's the one that I ran
[2341.30 → 2345.78] into recently where it's kind of the standard hasn't caught up with some of the more modern,
[2345.78 → 2348.76] I guess, project scaffolding methodologies.
[2349.28 → 2354.96] Yeah. And one thing that we do with type doc is we take the, uh, so type doc has the ability to
[2354.96 → 2360.32] parse your code and then generate this object that represents your code, uh, and everything
[2360.32 → 2364.90] in it. And then it will pass that to a renderer and render everything out. We actually don't
[2364.90 → 2370.02] use that because, uh, I think we didn't like the way that the default type doc renderer looks.
[2370.38 → 2376.94] Um, and so instead we have output a JSON file that has everything in it. And then we parse that
[2376.94 → 2382.08] ourselves into a custom renderer and, and then render our docs from that. And it just gives us a
[2382.08 → 2387.08] little bit more information, a little bit more, um, uh, customization that we can do specifically
[2387.08 → 2391.06] around making it easier to search and, um, and find docs faster.
[2391.66 → 2393.56] That doesn't sound like a trivial undertaking.
[2393.96 → 2394.14] No.
[2394.32 → 2401.16] Yeah. All right. We are coming up close to the second third of the hour. Uh, this is a really
[2401.16 → 2405.20] interesting segment. I learned a ton. I know I'm going to, as soon as I get home to start
[2405.20 → 2409.38] to investigate type doc and see where I can start to use it and some of the documentation
[2409.38 → 2414.92] work that I'm doing. Um, so in our next segment, we're going to come back and talk about some
[2414.92 → 2420.74] examples of documentation that exists out in the wild that are really great. Uh, leave you out with
[2420.74 → 2422.94] some inspiration, all that when we're back.
[2429.82 → 2435.58] This episode is brought to you by our friends over at dot tech, a new top level domain extension
[2435.58 → 2440.82] to consider when purchasing your next domain for your next big idea. Dot tech is a domain
[2440.82 → 2445.42] extension specifically intended for the tech community. And more often than not, I don't
[2445.42 → 2450.78] know about you, but when I search for you all to consider for a big idea, the.com, the.net,
[2450.78 → 2456.70] and many others are already taken, or they're quite costly to register. So with one year starting at
[2456.70 → 2462.62] 499 and five years starting at 2499, when you use our special code change log, they're super
[2462.62 → 2469.30] affordable to grab snag and use head to get dot tech to get started. Once again, get that tactic
[2469.30 → 2474.46] to get started and use our code change log or click through using the link of the show notes
[2474.46 → 2480.78] and by our friends over at digital ocean. What we love most about digital ocean is one click installs
[2480.78 → 2487.18] deploys that are super easy. It doesn't really require you to know much about a server to get up and running
[2487.18 → 2495.82] one click installs for node.js to an SSD cloud server in literally 55 seconds or even less. And the same
[2495.82 → 2501.58] experience you can have with a one click install you can have with pretty much anything you build out
[2501.58 → 2508.86] by taking a snapshot of your droplet. You can build out the best JavaScript app friendly server and
[2508.86 → 2515.10] literally deploy it with no time at all. Manage your own stuff, run your own stuff, deploy to digital ocean,
[2515.10 → 2523.02] make life easy for you head to do.co slash change log, pay less, deploy more, build better web apps
[2523.02 → 2529.10] with digital ocean and a free $100 credit. Once again, do.co slash change log.
[2529.10 → 2550.22] And we are back for the third segment. We're going to talk about some examples of documentation that is out in the wild that we really like.
[2550.94 → 2554.22] Does anyone want to share some of their favourite documentation?
[2554.22 → 2555.90] I do. Please do.
[2555.90 → 2562.14] I just said that I didn't have anything, but then I thought of something so, and I just wanted to say it before
[2562.14 → 2571.02] anybody else did. I really love MDN. It's not the prettiest thing in the world, but it's like it's
[2571.02 → 2582.14] it's something I can really count on to be to have accurate information. If you know it's good that they help you
[2582.14 → 2589.66] understand like the history of the API of the JavaScript API and yeah I just the effort at
[2589.66 → 2598.14] NBM is just it's phenomenal, and I love it, so I'm glad that exists. I'm glad you know people kind of stopped
[2598.14 → 2603.58] going to w3 schools and are more often looking at MDN now so.
[2603.58 → 2609.42] Do you remember when MDN first launched, and it was like there was a concentrated effort to get its search
[2609.42 → 2614.78] rank above w3 schools, and they came out and said everybody linked to MDN from their personal websites
[2614.78 → 2621.26] and from blog posts and from Stack Overflow and whatnot so that we can get this to rank higher than w3 schools
[2621.26 → 2626.14] and it worked, and it was pretty cool because markedly better.
[2626.14 → 2632.30] And I think they're working on making it output as a parsable output as well so you can ingest pieces
[2632.30 → 2635.34] of the documentation into your own stuff if you need which is really cool.
[2635.34 → 2636.14] That is cool.
[2636.14 → 2637.02] That is neat.
[2637.02 → 2640.62] But I really like I really like that you can just figure out something that you need like
[2640.62 → 2646.94] oh how do I use fetch again, and you just type fetch MDN into your search and you're there. It's its so great.
[2647.50 → 2652.54] Well speaking of API docs I think I'll give a shout-out to Stripe who I believe
[2652.54 → 2660.78] changed the game with regard to how people were documenting APIs as services. The way that they
[2660.78 → 2670.62] have example code that's executable it's copy pasteable snippets for not just any language you know
[2670.62 → 2676.14] a specific language but like all supported languages including curl in case you haven't quite
[2676.14 → 2683.26] picked a language yet and just the information architecture I think a lot of companies have
[2683.26 → 2689.98] come behind Stripe and basically jacked their style which is great for the world because it's its very
[2689.98 → 2697.26] easy to browse easy to peruse, and they even do the Stripe always sweat the details they do this
[2697.26 → 2703.34] little thing where they're in they'll integrate your personal info into the documentation if you're signed
[2703.34 → 2707.82] in and so if you're perusing their doc signed in, and they have a code snippet that requires like
[2707.82 → 2713.82] an OAuth token or whatever happens to be, and they will actually put your test API key into like the
[2713.82 → 2720.46] curl code so that you can actually copy and paste it and not have to swap it in yourself, so I love Stripes
[2720.46 → 2724.94] docs always have, and I think they really drilled it with a developer focused API
[2726.86 → 2731.18] and I think that a lot of different companies have taken a Stripes example and run with it and that's
[2731.18 → 2737.18] awesome too I guess following on with Stripe one of the documentations that I wanted to mention was
[2737.18 → 2742.38] actually Twilio's which kind of adopts similar philosophy to Stripe you know you've got your
[2742.38 → 2747.50] copy and paste snippets for a lot of languages it integrates some of your personal key codes
[2748.70 → 2755.26] and one thing I really like about it, I think Stripe does this too is its goal-oriented documentation so
[2755.26 → 2760.54] when you head over to their home page one of the first things you see is it says hey do you want to
[2760.54 → 2765.26] learn how to make phone calls with Twilio do you want to learn how to send text messages do you want
[2765.26 → 2773.42] to learn about WebRTC and so it comes in catering to what the end goal is, and I really dig that
[2774.30 → 2780.54] yeah I think the one that I really like is Chai I was just trying to think of one and one that I end
[2780.54 → 2787.18] up using quite a lot because we use Chai for a lot of our assertions is that, and I just appreciate that
[2787.18 → 2792.78] it's really easy to search for the different types of assertions because that seems to be always
[2792.78 → 2796.78] the thing that I'm forgetting about you know is there something more specific than strict equal
[2796.78 → 2803.90] that I can use, and it makes it really easy to find that but now with TypeScript I get a lot of
[2803.90 → 2810.30] that for free because I get auto-completion, and it just lets me know that, but also it pops up with
[2810.30 → 2813.98] the doc comment which is basically the same stuff that's on the website and just lets me know
[2813.98 → 2820.30] another good one that I think of that I often use and always appreciate is a little Dom library called
[2820.30 → 2827.10] umbrella JS and so this would be a good example if you are writing a JavaScript library that has
[2827.90 → 2834.86] somewhat of a small surface area but just a bunch of simple functions you can call and things that
[2834.86 → 2839.18] I appreciate about this so it's think of it like a modern little jQuery just smaller and a little bit
[2839.18 → 2843.98] less functionality, but everything can fit on one page and that's a nice little hack for people
[2843.98 → 2848.06] who don't want to build a search function into their docs but want it to be all searchable is
[2848.06 → 2853.58] just put everything on one page if you're is your surface area is small enough, and we can command f or
[2853.58 → 2858.54] control f our way to finding what we need without having to go page to page so that's a nice little
[2859.42 → 2863.98] feature without writing any code which is like my favourite kind of feature yeah and one of the things I
[2863.98 → 2869.18] noticed that I really liked about this umbrella JS website kind of links back to a previous topic of
[2869.18 → 2874.94] conversation is it's got a little link to their test suite so you can run their tests and view the
[2874.94 → 2879.82] execution like right next to the documentation basically that's super neat oh that's cool yeah
[2879.82 → 2884.78] it's a well-designed site altogether so umbrella js.com will link that one up as well, and I didn't have
[2884.78 → 2889.42] a chance I was going to hop over and see how they're actually building their docs if they're using a tool
[2889.42 → 2894.46] but it might just all be I'm looking at their website now it looks like maybe just all handwritten
[2894.46 → 2900.06] documentation.html so probably not generated, although this doesn't look like handwritten
[2900.06 → 2904.30] HTML so maybe check that out because lots of times you say oh that's really great I wish I could just
[2904.30 → 2908.30] have the same thing, and you go find out they're using a tool, and you can use that tool as well but
[2908.30 → 2915.02] maybe not the case here either way a great example to emulate this isn't really an example of great
[2915.02 → 2922.14] documentation, but it's a great add-on to documentation and that's code sandbox or similar
[2922.14 → 2929.42] tools where like we use that on dojo for our tutorials, and you can walk through everything
[2930.14 → 2933.98] without having to set up an environment at all you just click this link, and you're set up with
[2933.98 → 2939.10] the full environment with an editor with completion and everything right there, and then you can change
[2939.10 → 2942.86] the code and run it and just getting that immediate feedback can often be
[2942.86 → 2948.54] uh be the big difference that makes you understand something that much quicker probably a good time
[2948.54 → 2953.26] to tease our upcoming show on code sandbox don't you think nick yeah totally not my intention there
[2953.26 → 2959.10] uh, but we're we're going to be talking about uh talking about code sandbox uh next week with um
[2959.66 → 2965.58] eves van horn so that'll be a show to check out stay tuned for that should we get a fun episode
[2965.58 → 2971.34] mark your calendars make room don't schedule anything during that time be there so one uh I guess
[2971.34 → 2978.70] tendentially related tool that I will point out if you're on macOS is a tool called dash
[2979.42 → 2985.82] which is not an uh it's not documentation, but it's a tool that wraps documentation and the cool thing
[2985.82 → 2992.94] about it is uh it's an indie dev, and he's gone and normalized all kinds of API docs that fit directly
[2992.94 → 3000.86] into a singular tool so whether it's JavaScript or even the MDM docs or SQLite or jQuery or
[3000.86 → 3008.14] git you name it react they've been normalized into a singular place which are then taken offline
[3008.86 → 3014.86] and has a really slick interface um I love it on airplanes because you don't have to worry about the
[3014.86 → 3019.26] the internet even if you have it being slow or if you don't have it then you have your docs with you
[3019.26 → 3025.18] at all times um it's a free app with in-app purchase but um something definitely worth checking
[3025.18 → 3029.50] out I don't know if there are cross-platform or other platform alternatives, but there's something
[3029.50 → 3035.10] great about having single access into all kinds of API docs and also having them offline is just
[3035.10 → 3044.06] killer yes dash is awesome i ever since I found dash um I've used it religiously it's pretty much the
[3044.06 → 3051.74] only way I look up anything um highly recommended if you haven't tried it yet yep and the website for
[3051.74 → 3057.66] dash does mention a tool called velocity which is a window equivalent for that nice I wanted to give a
[3057.66 → 3063.34] shout out to another documentation resource that I thought was great, and it's actually GitHub um
[3063.34 → 3068.06] and I would say it's not necessarily their API documentation but more they're like how to be and
[3068.06 → 3073.02] their reference guide I think they do a perfect job of having you know the text content that's I think
[3073.02 → 3078.62] on like docs.GitHub.com, and then they've got their video content on their YouTube channel, and they do
[3078.62 → 3085.02] perfect job of making sure that git is super accessible to people in addition to obviously providing
[3085.02 → 3091.42] like the GitHub web app yeah that documentation is super helpful uh if you need to tell somebody
[3091.42 → 3097.26] how to do something specific with GitHub or sorry with git GitHub usually has documentation
[3097.26 → 3102.06] for that so you can just send them a link a couple of guides I'll also mention here as we get towards the
[3102.06 → 3109.66] end uh if you're looking for examples of not just like API docs, or you know web service docs but guides
[3109.66 → 3114.38] and you're saying what does a good guide look like I will throw out two the first one is the
[3114.38 → 3120.46] Ruby on Rails guides uh which are spectacularly useful very great architecture of the way
[3120.46 → 3125.42] they're laid out uh high level, and yet they'll drill down uh into specifics as you need them with
[3125.42 → 3131.26] a link out to specific uh code samples or to specific you know sections of the actual API docs
[3131.26 → 3135.42] if you want to learn more and then secondly GitHub has great open source guides as well which are very
[3135.42 → 3139.98] high level all about you know they're they're kind of an intro to getting into open source and how to
[3139.98 → 3144.94] get and how to do these different things um, but they're very well laid out and very well written
[3144.94 → 3150.86] and so another place to look for inspiration if you're looking for how to write good guides yeah
[3150.86 → 3155.42] those are all the perfect resources thank you so much for joining us everybody hopefully this
[3155.42 → 3162.46] conversation was inspiring informative motivating um, and you got everything you needed to go out and start
[3162.46 → 3169.26] writing some documentation whether it's open source or closed source whatever source it is um thanks
[3169.26 → 3175.26] again for joining us you can find links to all the things that we mentioned at the description below
[3176.14 → 3178.06] um, and we will see you next week
[3181.10 → 3187.98] all right thank you for tuning in to JS party this week tuning live on Thursdays at 1 p.m us eastern at
[3187.98 → 3192.38] changelaw.com slash live join the community and select with us in real time during the shows
[3192.94 → 3198.62] the changelaw.com community and do us a favour share this show with a friend or just have a podcast
[3198.62 → 3203.42] go into overcast and favourite it and thank you to fast our bandwidth partner head to
[3203.42 → 3208.14] facet.com to learn more, and we move fast and fix things right here at change law because of Rollbar
[3208.14 → 3213.26] check them out at rollbar.com we're hosted on leno cloud servers at leno.com
[3213.26 → 3218.46] slash change law check them out and support this show our music is produced by break master cylinder and
[3218.46 → 3223.58] you can find more shows just like this at changelaw.com thanks for tuning in we'll see you next week
[3223.58 → 3236.22] I'm Tim smith and my show away from keyboard explores the human side of creative work you'll
[3236.22 → 3241.98] hear stories sometimes deeply personal about the triumphs and struggles of doing what you love
[3241.98 → 3247.34] I ended up in hospital with burnout I just kept ignoring the way that it was making me feel and
[3247.34 → 3252.94] just kept powering through it and then eventually my body started to give me physical symptoms to say
[3252.94 → 3258.06] like hey you should stop and listen to me new episodes premiere every other Wednesday find the
[3258.06 → 3272.06] show at changelaw.com slash AFK or wherever you listen to podcasts

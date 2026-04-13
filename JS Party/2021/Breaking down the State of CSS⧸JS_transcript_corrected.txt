[0.00 → 13.44] If we look at the changes in how much people are using different things, there has been dramatic change both in the libraries and tooling space, but also just in the underlying features of CSS, right?
[13.44 → 16.68] So there's a dramatic increase in folks using CSS Grid.
[16.78 → 20.00] There's a dramatic increase in folks using custom properties.
[20.56 → 27.34] And those are things that allow you to do stuff that you used to need a lot of tooling to do.
[27.34 → 31.82] And in some cases, they let you do things that you basically couldn't do at all, even with tooling.
[32.20 → 37.66] So there's quite a bit of innovation in what the underlying platform supports and how much people are able to use that.
[37.82 → 40.84] At the same time, there is also this change in framework.
[42.44 → 45.02] Bandwidth for Change Log is provided by Vastly.
[45.34 → 47.22] Learn more at Fastly.com.
[47.46 → 49.74] Our feature flags are powered by Launch Darkly.
[50.02 → 51.82] Check them out at LaunchDarkly.com.
[52.06 → 53.92] And we're hosted on Leno cloud servers.
[53.92 → 57.82] Get $100 in hosting credit at Leno.com slash Change Log.
[58.62 → 60.02] What's up, JS Party people?
[60.14 → 64.88] Have you ever wondered if you could be offering a faster, less buggy experience for your customers?
[65.44 → 70.62] Well, with Ray gun Error and Performance Monitoring, you have all the information you need at your fingertips
[70.62 → 76.12] to quickly find and fix errors and performance issues across your tech stack down to the line of code.
[76.46 → 79.30] Ray gun makes it easy to monitor the impact of your performance improvements,
[79.30 → 84.92] quickly identify issues across web and mobile apps, and see how your code performs in the hands of your customers.
[85.42 → 89.00] This saves you time, this saves you money, and this saves your sanity.
[89.34 → 93.96] Head to Raygun.com to join thousands of customer-centric software teams who use Ray gun every single day.
[94.26 → 98.14] Again, Raygun.com to give them a try with a free 14-day trial.
[98.14 → 123.06] Welcome to JS Party, your weekly celebration of JavaScript and the web.
[123.36 → 125.30] We have some great episodes in the pipeline.
[125.30 → 130.30] Next week, Ben Coe from Google joins Abel and Divya to talk testing coverage.
[130.66 → 132.58] After that, Yep, Nope returns.
[132.78 → 133.70] That's our debate show.
[133.86 → 135.10] I think this one's going to be heated.
[135.40 → 140.88] And it only gets better from there, so subscribe now at jsparty.fm or in your favourite podcast app.
[141.08 → 143.02] Just search for JS Party, you'll find us.
[143.42 → 145.42] Let's break down some survey results, shall we?
[145.48 → 146.88] Hey, it's party time, you all.
[146.88 → 155.94] Hello, JS Party people.
[156.18 → 159.50] Welcome back to another week of partying about JavaScript and the web.
[159.60 → 160.20] I'm K-Ball.
[160.30 → 161.56] I will be your host this week.
[161.78 → 168.06] And with me today to discuss the state of star surveys, where star equals CSS or JS,
[168.06 → 170.88] I have the one and only Jared Santo.
[171.08 → 171.44] Hey, Jared.
[171.64 → 173.04] I thought we were going to be the stars.
[173.68 → 174.64] We could change it up.
[174.90 → 176.90] State of the stars survey.
[177.34 → 178.92] I thought we were just going to talk about how we're doing.
[179.30 → 180.10] How are you doing, Jared?
[180.44 → 181.56] I'm doing quite fine.
[181.66 → 182.44] Thanks for having me.
[182.80 → 183.46] You're a star.
[184.06 → 184.48] All right.
[184.56 → 189.56] The other friend panellist star joining me today is the one and only Nick Needed.
[189.62 → 190.10] Hello, Nick.
[190.52 → 191.06] Ahoy, ahoy.
[191.56 → 192.02] How's it going?
[192.46 → 193.40] Making it through.
[193.40 → 195.76] We are in 2021 now, for real.
[195.86 → 200.38] Not like the last episode that I recorded for 2021 when we were recording it in 2020.
[200.64 → 201.50] We were faking it.
[201.78 → 205.86] So excited to be here last year was a bit, but we made it.
[205.98 → 210.30] Though if by virtue of speaking or listening to this podcast, you made it.
[210.82 → 217.14] You are here in 2021, and we are going to talk about what's changing in JavaScript and CSS.
[217.14 → 223.10] And we're going to jump into that by looking at the state of JS and state of CSS surveys.
[223.40 → 225.58] That were done and published at the end of last year.
[225.66 → 228.82] There's a state of JS 2020, state of CSS 2020.
[229.34 → 236.64] And one of the fun things about that is we can actually look at the differences between what was going on in 2020, what people said, and what was going on in 2019.
[237.04 → 238.36] Talk about those trends.
[239.26 → 243.38] We can prognosticate about whether they missed something.
[243.72 → 247.34] But yeah, let's start with just kind of talking about those surveys.
[247.44 → 248.76] Because we talked about them before.
[249.30 → 251.28] What strikes you guys when you think about these surveys?
[251.28 → 254.42] Because I know when we talked about doing it, some folks were like, oh, those surveys.
[254.54 → 256.04] And some folks were like, yeah, those surveys.
[256.54 → 257.62] I like surveys.
[257.98 → 259.18] I like to look at data.
[260.32 → 263.02] And I appreciate the work that goes into these surveys.
[264.28 → 266.90] We've, of course, broke them down in the past.
[267.16 → 269.44] And doing surveys is hard.
[269.98 → 274.86] In fact, we've at Changelog thought about doing surveys and talked to folks about doing some surveys.
[275.12 → 276.70] And we're always like, do we really want to do surveys?
[276.70 → 278.48] Because it's tough to do well.
[278.62 → 282.36] And you open yourself to all sorts of criticism, which I don't like criticism.
[282.54 → 283.96] I just prefer to be a star.
[284.68 → 289.14] And so I just appreciate Sasha and the team and everybody who works on these.
[289.50 → 291.60] Because it's tough to do well.
[291.68 → 294.98] And they've come under some criticism because of how they've been conducted over the years.
[295.08 → 296.96] And I'm sure we'll dive into all that.
[296.96 → 300.78] But I do enjoy just looking at what's going on, seeing the changes over time.
[300.98 → 305.16] And then talking about it, I think some of these things have to be taken with a grain of salt.
[305.44 → 308.50] But that being said, it's good conversation pieces.
[309.20 → 309.22] Yeah.
[309.38 → 314.94] And I really like that it validates all of my conceptions about JavaScript and CSS of today.
[315.02 → 315.42] That's sweet.
[315.60 → 317.24] And when it doesn't, then I don't like it.
[317.30 → 318.12] Then it's biased.
[319.48 → 321.06] That's the real value of surveys, right?
[321.06 → 326.10] The ones that tell you that all your priors are correct and all the other guys or gals' opinions are wrong.
[326.10 → 326.34] Yeah.
[326.86 → 329.66] Just survey yourself, and you'll bet 1,000, you know?
[331.06 → 332.12] Sample size one.
[332.48 → 333.84] All the answers are correct.
[334.10 → 334.60] Moving on.
[334.86 → 339.56] Well, and that is one of the most interesting both critiques that has been levelled at these surveys,
[339.68 → 342.68] but also one of the things that they've worked on and done well is like,
[342.80 → 345.42] how do you determine what's the sample for your survey?
[345.54 → 346.76] Who is being surveyed?
[347.06 → 352.96] And if you're doing a scientific survey with the purpose of trying to sort of prove something,
[352.96 → 358.12] then you want to figure out kind of what the population is that you're trying to understand
[358.12 → 361.28] and survey a representative sample.
[362.32 → 367.76] Here we're trying to kind of get a sense of just the broadest possible swath of the web,
[367.80 → 370.60] and I think they've taken the spray and pray approach, which is like, okay,
[371.02 → 375.38] push this in as many directions as we possibly can so we can get the most possible data
[375.38 → 380.74] and worry a little bit less about does this accurately model any particular population
[380.74 → 382.14] within the web dev community.
[383.34 → 385.86] As a result, we have lots of data to look at.
[386.12 → 392.56] As you do this, do be a little bit careful in drawing conclusions about the representation
[392.56 → 395.02] of all of JavaScript or all of CSS.
[395.02 → 399.70] And one of the things they do nicely is they print out the demographics of who it was
[399.70 → 403.58] that answered the survey so that you can see who is this representative of.
[404.28 → 411.60] And if you come in with a feeling about what the web industry looks like or what your company
[411.60 → 416.08] looks like, you can get a sense of whether this data is likely to be representative of you.
[417.12 → 420.16] Plus, you have to ask yourself, like, how much does it really matter as well?
[420.16 → 425.48] You know, like, so other people are digging this particular technology, and so does that
[425.48 → 429.28] mean that I need to be using that technology, or does that mean that I'm less than because
[429.28 → 430.72] I use this other technology?
[431.02 → 436.14] And, you know, it's worth understanding what other people are doing, what they appreciate,
[436.38 → 438.98] what they're moving away from, what they're moving towards.
[439.50 → 443.14] But all those are just data points for, you know, you and your life and your work and your
[443.14 → 444.92] team to make decisions.
[445.68 → 449.06] And so that's why I say take it with a grain of salt, because even if this survey was like
[449.06 → 454.50] 100% the actual facts of the world of JavaScript and CSS, like, that doesn't mean that it informs
[454.50 → 455.72] your context whatsoever.
[456.12 → 458.96] So, grain of salt, still enjoyable to look at.
[459.06 → 461.82] And of course, confirming your priors is always fun.
[462.24 → 465.94] So, you know, we're here to see if TypeScript's doing awesome or...
[465.94 → 466.24] Oh, yeah.
[466.54 → 467.14] We don't have to look.
[468.06 → 468.76] We know.
[469.28 → 470.42] We just know.
[470.42 → 475.18] I mean, the new government website that just was relaunched after the inauguration,
[475.66 → 476.70] folks were tearing it down.
[476.70 → 477.10] Yeah.
[477.10 → 477.88] It's using jQuery.
[478.44 → 479.10] Not a problem.
[479.48 → 480.96] So, they're still like...
[480.96 → 485.60] That's one of the wealthiest governments in the world doing their website, and they're
[485.60 → 486.22] using jQuery.
[486.42 → 489.74] So, if you're using jQuery, no shame, even if it's not showing up in this survey.
[490.80 → 492.74] Lots of different stuff there.
[493.08 → 493.66] Okay, cool.
[494.14 → 498.46] So, before we dig in, we've talked about values, pros and cons.
[498.64 → 502.40] But the team has also, behind these surveys, has also talked a little bit about what they
[502.40 → 503.62] want to do moving forward.
[503.62 → 509.24] I know some of the big changes that they made coming into 2020 from 2019 is they improved
[509.24 → 513.40] the breadth of demographics that they were looking for, and they did a lot more in terms
[513.40 → 519.88] of pulling in information from the community about learning, where to learn from, what to
[519.88 → 524.44] learn, or what good resources are, which I think highlights that strength point you're
[524.44 → 529.22] talking about, Jared, of using this as a place to get a sense of what people are doing and kind
[529.22 → 534.26] of explore rather than use it to try to tell yourself if you're doing good or not.
[534.84 → 536.72] What are some of the other things they've said they're going to do?
[537.50 → 541.66] Yeah, well, I mean, I think it's worth giving a shout-out to Sasha Grief and Rafael Benítez,
[542.02 → 546.48] I believe is how you say his name, who is really the team behind both State of CSS and State
[546.48 → 546.80] of JS.
[546.96 → 548.02] And they've been doing it for many years.
[548.14 → 549.68] So, this is very much labour of love.
[550.52 → 551.98] A lot of people pitched in this year.
[551.98 → 556.48] So, they have a special thanks on their website, including some folks doing translations.
[556.68 → 557.58] So, that's really cool.
[558.26 → 561.02] And we've had Sasha on this show, I believe.
[561.12 → 562.48] We've definitely had him on the changelog.
[562.54 → 567.28] And we've talked about the trials and tribulations of doing surveys, the way that his branding,
[567.82 → 574.60] or I should say their branding and design is so good that it gives them a lot of clout,
[574.84 → 577.06] which is why some of the criticism comes with the clout.
[577.12 → 581.46] When you say this is the state of this, you are making yourself authoritative.
[581.46 → 584.00] I mean, their websites are always spectacular.
[584.40 → 585.20] So, shout out to all that.
[585.32 → 590.10] They also know that it can be improved year by year, just like anybody would do with a
[590.10 → 591.38] project that they care about.
[591.70 → 593.92] And so, like you said, K-Ball, they've made some improvements this year.
[594.72 → 599.28] Sasha recently tweeted that he wanted to do some new stuff in 2021 for the next round,
[599.64 → 603.52] which I'm sure will be coming out soon, at least the survey part, maybe not the results.
[604.16 → 609.68] They want to start measuring disabilities among respondents, which, of course, would help us
[609.68 → 614.02] with our allay decisions, our accessibility decisions and information around that.
[614.54 → 616.12] Improve the translation process.
[616.22 → 620.84] Of course, the more languages you can get to, the better sample leans you can have of the world
[620.84 → 623.30] writ large, not just the U.S. and English.
[623.72 → 628.02] They want to do a better job of highlighting minorities voices, whether by gender, race,
[628.12 → 631.84] geography, et cetera, in their results through data visualization.
[631.84 → 636.44] So, just a few things that he put out that they would like to do this year and just continue
[636.44 → 639.70] to improve and refine what these surveys are.
[640.26 → 646.44] I do like that they see the criticisms that come from this, and they respond to it, honestly
[646.44 → 647.12] and openly.
[647.88 → 651.66] And that's really reassuring because it's a hard problem to solve, no matter how you look
[651.66 → 651.92] at it.
[651.92 → 659.56] Coming from a conference organizer perspective, we always strive for having perfect, diverse
[659.56 → 664.98] in both the people that are coming, the speakers, and in the opinions that are being thrown out
[664.98 → 668.00] at the conferences, trying to have a diverse opinion across all of that.
[668.42 → 674.50] It's not easy, but it's much easier when it's a finite set of people, like 10 to 20 speakers
[674.50 → 677.56] that you're picking out and trying to set the tone with that.
[677.56 → 682.98] With this, you're trying to expand beyond the audience.
[683.20 → 687.82] And they call out in a blog post that there are two white guys trying to do this on Twitter,
[688.18 → 693.40] which is predominantly white male, and trying to reach out through that.
[693.84 → 700.18] And it's hard when you're trying to get thousands more, as opposed to like 10 to 20 more for a conference.
[700.82 → 705.44] Yeah, and if you look at the demographic trends that they have over time, they are trending
[705.44 → 706.18] more diverse.
[706.18 → 712.14] You know, they're getting a wider range of folks from different countries around the
[712.14 → 712.38] world.
[712.56 → 717.02] They started measuring languages, primary languages, and they're getting more and more diversity
[717.02 → 717.42] there.
[717.82 → 719.30] There's somewhat more gender diversity.
[720.30 → 725.70] There's definitely room to grow on that dimension, but they're acknowledging it as an issue, and
[725.70 → 726.74] they're moving in the right direction.
[726.74 → 745.90] This episode is brought to you by Source graph.
[746.28 → 748.82] Source graph is code search for every developer and team.
[749.06 → 752.30] Easily search across all the code that matters to you and your organization.
[752.30 → 757.32] Find example code, explore and read code, debug issues, and so much more.
[757.58 → 762.14] And I talk with Bung Liu, CTO and co-founder of Source graph, and asked him to share what
[762.14 → 766.74] code search is, what developers and teams are missing out on, and how Source graph provides
[766.74 → 768.66] code search to every developer in the world.
[768.66 → 774.80] If you've worked inside a Google or a Facebook or any one of these huge, well-respected
[774.80 → 779.16] technology companies, chances are you've used something like code search before, and you
[779.16 → 781.42] know the value that it provides to your team.
[781.50 → 786.52] You know that almost every single engineer inside these organizations uses it on a daily
[786.52 → 786.96] basis.
[787.20 → 791.66] If you've never had that experience, chances are you may not know what you're missing out
[791.66 → 791.88] on.
[791.88 → 796.46] You know, the term code search sounds a lot like, you know, grew or the search inside
[796.46 → 796.90] your editor.
[797.26 → 799.26] And that's what a lot of people think when they first hear it.
[799.32 → 801.02] But it's really about much more than that.
[801.12 → 806.74] It's really about connecting you as a developer to the broader universe of code and code-related
[806.74 → 811.02] data that's relevant to you, that you need at hand in order to enter that, you know,
[811.02 → 816.50] magical flow state of, you know, being in your editor, writing code quickly, making rapid
[816.50 → 818.80] progress towards that feature bug fix that you're working on.
[818.80 → 823.08] It's really about making all that contextual information accessible at your fingertips.
[823.60 → 827.88] And what that means is, think about every single repository, every single file, and every
[827.88 → 834.16] single language, every single diff, and every single open source dependency or maybe closed
[834.16 → 836.20] source dependency that's shared across your organization.
[836.36 → 839.00] All that is searchable through a single text box.
[839.42 → 843.66] And that's really powerful because it means all this friction is eliminated between you and
[843.66 → 845.12] understanding that broader world of code.
[845.20 → 846.86] You don't have to clone stuff down to your local machine.
[846.86 → 848.70] You don't have to mess around with editor config.
[849.44 → 853.72] You don't have to be constantly bugging people on other teams who may not even know who you
[853.72 → 857.58] are in order to teach yourself how all that code works.
[857.96 → 863.50] What Source graph is, is really a way for the rest of us, the people who don't work inside
[863.50 → 869.64] the Googles, the Facebook's, to get a tool that gives us access to that sort of information
[869.64 → 871.54] readily and at our fingertips.
[871.54 → 875.98] It's really about bringing this type of tool that a lot of the larger technology companies
[875.98 → 880.64] have developed and invested hundreds of millions of dollars into making for the productivity
[880.64 → 884.84] of their own engineers and making that accessible to every single developer in the world.
[884.96 → 885.50] All right.
[885.52 → 888.78] If code search powered by Source graph sounds like something you and your team could use,
[888.84 → 893.28] head to info.sourcegraph.com slash changelog and click the button that says try Source graph
[893.28 → 893.78] now.
[893.98 → 897.10] You can install it locally, deploy it to a server or to a cluster.
[897.48 → 900.40] They have a quick start guide that takes less than five minutes to install Source graph using
[900.40 → 902.58] Docker. So it's too easy to give a try.
[902.76 → 906.22] Again, head to info.sourcegraph.com slash changelog.
[930.40 → 939.90] All right. So coming back into it, let's talk about what stood out in the state of CSS survey
[939.90 → 942.76] and what you're taking away from it. Let's start with you, Jared. When you looked at this
[942.76 → 946.22] state of CSS 2020, what did you notice? What stood out to you?
[946.70 → 951.64] For me, what stood out is that people are generally people who responded to this survey. Let me
[951.64 → 958.22] preface that. They generally like CSS quite a bit, which is somewhat funny when we talked about a few
[958.22 → 963.72] weeks back, why people complain about CSS so often. Because even since that conversation,
[963.90 → 968.28] I put a post out on changelog.com as well, just like reviewing some of the reasons that we thought.
[969.04 → 973.06] I've seen so much complaining about CSS over the last few weeks, just on Twitter alone,
[973.58 → 977.94] that it seems like it's like the whipping boy or girl, depending on how you think of CSS,
[978.74 → 983.94] of the community. I mean, there's just so much complaining and rabble-rousing and debating and
[983.94 → 987.94] stuff. And just like, wow, very interesting. And then the survey says, you know, people are
[987.94 → 994.30] generally pretty happy with CSS, which I think is appropriate and cool. Because let's face it,
[994.30 → 999.50] it's a very powerful set of tools and technologies. And there's so much that people accomplish on the
[999.50 → 1004.40] web and build amazing things. I just love going to a website and being like, wow, this website's
[1004.40 → 1009.70] amazing. And the person that put this CSS together really knows their stuff. I mean, that's such a great
[1009.70 → 1014.56] feeling and celebrating that. And so just seeing that, you know, of course, there are things that
[1014.56 → 1018.26] could be better. There are things that are hard to learn, things that are hard to use, waiting for
[1018.26 → 1023.52] browsers to support X, Y, or Z. There's all these little intricate details. But in general, people do
[1023.52 → 1030.52] like CSS. And that was just really nice to see. And then secondly, I think the trending thing is no
[1030.52 → 1035.02] surprise, because we've been talking about it recently, is that Tailwind has really taken over the
[1035.02 → 1040.16] mind share, I think, of the front-end CSS space in 2020.
[1040.80 → 1044.18] So you think that that's, does that support the idea that people love CSS?
[1045.08 → 1047.92] I mean, it's a CSS framework, so they love it.
[1047.94 → 1049.82] Well, you don't really like CSS with it.
[1051.28 → 1057.64] Well, like I said, I mean, there are reasons why it's difficult. And one of the things that Adam said
[1057.64 → 1062.10] on the show that we did, we're referencing back to our episode we did late last year with Adam
[1062.10 → 1068.54] With and up tailing CSS, why it has been difficult and can be difficult to really feel like you've
[1068.54 → 1077.42] mastered it, is because the best practices have not historically congealed to a place where it's
[1077.42 → 1083.32] like, here is how you do it, right? There were different takes, a lot of experimentation, things
[1083.32 → 1089.80] go in and out of style, technology changes, you know, RWD, responsive web design really shook
[1089.80 → 1095.58] up the CSS best practices landscape. But now it's probably a decade ago now. And utility
[1095.58 → 1101.32] classes are starting to be something that a lot of people are congealing around. And of
[1101.32 → 1107.46] course, Tailwind provides that set of utility classes. And so seems like a radical idea, you
[1107.46 → 1112.58] know, tachyons, is Burma another one? There are a handful of these things over the years that
[1112.58 → 1118.16] have been saying, let's do CSS with these utility classes, which seem they're non-semantic,
[1118.16 → 1122.20] et cetera, et cetera. And it really makes things better. And it seems like that's starting to
[1122.20 → 1127.16] become, I don't know if it's a best practice cable. What do you think? It's becoming popular-er
[1127.16 → 1128.56] and Tailwind's leading that charge.
[1128.78 → 1134.50] Yeah. I mean, I think similar to what we've seen in the JavaScript ecosystem, like there are
[1134.50 → 1144.16] ongoing both questions and trends around what are the right abstractions to use. And the types
[1144.16 → 1150.02] of abstractions that are going to make sense in a CSS environment that is visual and spatial and
[1150.02 → 1157.40] essentially applying to, or intended to apply to wide varieties of screen dimensions and things like
[1157.40 → 1163.04] that, like the problem space of CSS, that's a very different problem space than you encounter in
[1163.04 → 1168.48] JavaScript. And so it's not surprising that the ideas about what's going to make sense there
[1168.48 → 1175.10] are not the same. I think we went a little overboard on the semantic CSS approach because it modelled
[1175.10 → 1180.28] closer to how we were used to thinking about things in more imperative programming languages like
[1180.28 → 1187.60] JavaScript. And that turns out to have some challenges when you shifted into that visual space.
[1187.82 → 1192.12] I wanted to jump back a little bit to what you said about people liking CSS, because I think
[1192.12 → 1197.22] it highlights one of the challenges in this type of survey is I think there might be a selection bias.
[1197.22 → 1204.94] The people who chose to take the state of CSS survey, they break down demographics by reported
[1204.94 → 1213.36] skill level and CSS proficiency. And 61% of the people who answered this survey considered themselves
[1213.36 → 1219.06] experts in this with expert being defined as able to style an entire front end from scratch
[1219.06 → 1227.20] following a consistent methodology. That body of people have likely already put in a
[1227.20 → 1234.24] tremendous amount of work learning the mental models of CSS, which, as I mentioned, like CSS has a very
[1234.24 → 1239.00] different problem domain and mental model than most other programming domains you're going to end up
[1239.00 → 1243.64] with. And I think that that might be the source of a lot of hate. You know, a lot of the folks who hate on
[1243.64 → 1251.00] CSS, they have not made that shift into understanding the mental model. And because it's different, it feels painful.
[1251.00 → 1260.40] It's raw. It doesn't work right or how their heads are set up. So, you know, I think we should, you know, one, use this to say, yes,
[1260.44 → 1267.46] there's a large body of people out there who do love CSS. And for good reason. It's an incredibly powerful and interesting
[1267.46 → 1274.42] language. And I think that mental model is actually a fascinating one to wrap your head around. But not necessarily take this as
[1274.42 → 1280.72] representative of the community as a whole, because everyone who hasn't climbed that learning curve, from what I can see,
[1280.78 → 1281.76] they didn't take the survey.
[1282.26 → 1289.76] Yeah, good, perfect point. And perhaps a bright spot for those who are, you know, banging their head against CSS right now,
[1289.90 → 1295.90] maybe you're just getting started. It is one of the first things that you learn as well, right? Like HTML and CSS, and then
[1295.90 → 1301.56] JavaScript, I think you should learn them in that order. HTML, you can actually pick up in a day or two, because, you know, once you
[1301.56 → 1305.86] understand like the sideways tree, I'm saying like the basics, right? Like it takes a long time to master,
[1305.98 → 1310.88] of course, but it's not, it's so approachable, right? Like, okay, here's a tree structure, we nest
[1310.88 → 1316.62] things inside, we give them names, take a cheat sheet, memorize these elements, you know, and then
[1316.62 → 1321.20] attributes. And it goes from there. We learn forms, that kind of stuff. You can pick that up in a day.
[1321.66 → 1324.88] I've taught it to people, they've had no problem. Like mentally, they're just like, cool. And they're
[1324.88 → 1330.80] excited to come back for day two. And then day two, I used to do a three day, like real basic web development
[1330.80 → 1335.94] class. And it was like day one, HTML, day two, CSS, day three, how to make something hide,
[1336.10 → 1340.66] right? In JavaScript. So it was like the most basic JavaScript you could do. Day two, come back. And
[1340.66 → 1345.10] now it's time to start talking CSS. And it's, it can be a real struggle at first. Like you said,
[1345.14 → 1353.32] that mental model is not mapped as easily by anybody, probably by most folks, at least. But these
[1353.32 → 1359.88] experts, right, the 60% who can do it, they've made it through that way. They like it. They enjoy it.
[1359.88 → 1366.42] They're productive. And so for those of us who are in the mucky muck, right, trying to figure out the
[1366.42 → 1372.20] mental model, trying to figure out why it doesn't look the way that we want it to, if we power through
[1372.20 → 1378.36] and persist and persevere, likely at the end of that tunnel is a technology that A, is very powerful.
[1378.90 → 1383.72] And you can accomplish a lot and make money and make cool things and all that. But B,
[1384.48 → 1385.64] you'll probably end up liking it.
[1385.64 → 1390.30] One thing that the survey doesn't, I'm not sure, I haven't found it, at least, that it doesn't tell
[1390.30 → 1397.88] me is like the preference towards like more straight, more traditional CSS, or I would even
[1397.88 → 1403.06] put like SAS in there, but you're writing more like, you know, here's my style files versus here's my
[1403.06 → 1410.76] very tool optimized CSS that I'm writing either like with CSS and JS or with post CSS or some other
[1410.76 → 1416.26] tool that's helping me to write better CSS that's maybe more scoped to like a specific component that
[1416.26 → 1420.98] I'm working on or something. It doesn't really tell me, you know, if there's a preference more
[1420.98 → 1424.36] one way or the other when I look at this. Have you seen that?
[1424.92 → 1428.66] There's a little bit with the CSS methodology section, but it's not exactly what you're talking
[1428.66 → 1428.98] about.
[1429.42 → 1432.82] Yeah, that's where I was going. There's a little bit in that breakdown of technologies and
[1432.82 → 1433.58] methodologies.
[1433.58 → 1442.02] The methodologies are really like BEM versus SACS versus object-oriented CSS, etc. Utility
[1442.02 → 1447.80] CSS or atomic CSS. But it doesn't say like, you know, thinking in components like with CSS
[1447.80 → 1451.78] and JS or anything like that. That's actually its own separate area. So I don't think it addresses
[1451.78 → 1456.24] directly what you're referring to or there's no like traditional cascade, or I don't know what
[1456.24 → 1462.66] you call the way that we historically did it. What do you call that cable? The cascade style
[1462.66 → 1463.70] or nested?
[1464.02 → 1464.68] We call it CSS.
[1465.16 → 1466.06] Yeah, just CSS.
[1467.66 → 1469.34] Just start slapping stuff out there.
[1470.16 → 1473.66] But that could lead in like one way or the other. Like, do you actually like CSS? Or if
[1473.66 → 1478.54] you're writing this like, you know, very, very different variant that is, you know, hyperscoped
[1478.54 → 1484.66] and gets rid of the cascade and is in, I mean, not necessarily in JS, but, you know, more
[1484.66 → 1490.46] it's not traditional CSS, and it's kind of changing the rules of CSS. Is that making someone
[1490.46 → 1496.18] like CSS more because it's making it easier to use? And also is that kind of making people
[1496.18 → 1499.62] feel like they're more of an expert because there's so much tooling that you have to set
[1499.62 → 1500.12] up beforehand?
[1501.32 → 1503.56] These are great questions that I have no answers to.
[1503.56 → 1509.68] Yeah, no idea. I mean, I think one interesting thing in this space that actually contrasted
[1509.68 → 1515.62] a little bit with the JavaScript space is especially like if we look at the changes in how much people
[1515.62 → 1524.58] are using different things, there has been dramatic change both in the libraries and tooling
[1524.58 → 1529.70] space, but also just in the underlying features of CSS, right?
[1529.70 → 1535.82] So there's a dramatic increase in folks using CSS grid. There's a dramatic increase in folks using
[1535.82 → 1545.54] custom properties. And those are things that allow you to do stuff that you used to need a lot of
[1545.54 → 1550.76] tooling to do. And in some cases, they let you do things that you basically couldn't do at all,
[1550.92 → 1555.94] even with tooling. So there's quite a bit of innovation in what the underlying platform
[1555.94 → 1562.36] supports and how much people are able to use that. At the same time, there is also this change in
[1562.36 → 1571.22] framework. There's a lot of people using Tailwind that's dramatically changing. Many moves towards
[1571.22 → 1577.28] this sort of, as you highlight, like the more functional and utility-based CSS and away from
[1577.28 → 1585.92] some of the sort of more semantic CSS frameworks. And there's increasing amounts of CSS and JS.
[1585.94 → 1592.62] You know, folks using styled components, folks using CSS modules. There's a lot of movement
[1592.62 → 1594.58] in both dimensions of that.
[1595.30 → 1599.48] One of the areas that you mentioned movement, which I don't even know what this is, is object fit.
[1599.74 → 1601.28] Can you describe what object fit is?
[1601.72 → 1611.64] Yes. So object fit. Let's even look it up. So this is basically around how you can display images
[1611.64 → 1620.02] and videos at particular sizes within their containers. So for example, if you have images
[1620.02 → 1626.98] with different aspect ratios that all are going to have to go into a single container or a single
[1626.98 → 1633.80] component, how does it make sense to do those? Do you want to trim them? Do you want to have them
[1633.80 → 1638.34] cover the space? Do you want to have them be resized, so the entire thing is fit?
[1638.34 → 1645.56] Those used to be so hard to do. And you'd have to basically do a lot of hackeries to try to get it.
[1645.62 → 1650.46] And now you have a single property where you can say, okay, for this one, I want it to be contained,
[1650.56 → 1656.00] which means that the entire image should fit within this space and shrink it until that's possible.
[1656.10 → 1659.92] And that may mean white space on the outsides of in one dimension or the other, but that's fine.
[1659.92 → 1667.12] Or you can say, I want this to be covering the space, in which case it will trim a set of things,
[1667.20 → 1673.56] but it'll make sure that it's covering the entire thing. So it's giving you fine grain control of how
[1673.56 → 1676.48] images and videos are resized to fit their containers.
[1677.18 → 1682.34] And particularly for images, like I can remember times in the past where I inappropriately would
[1682.34 → 1687.00] use like a background image because I wanted that kind of feature. And that's not very accessible.
[1687.00 → 1690.66] So in this, you can use like an image tag or a video, like you said,
[1690.96 → 1694.04] and then just set this property and get the same result.
[1694.46 → 1698.92] Pretty cool. I did not know about that one. I will answer to using it in the 2021 survey.
[1699.62 → 1704.04] That gives us a good jumping off point. What did you all take from this survey of things that
[1704.04 → 1707.32] you want to either start using or at least dig into and learn about?
[1707.94 → 1708.76] Object fit.
[1710.68 → 1711.72] You're a star, Jared.
[1711.86 → 1716.34] Yeah, there you go. I'm going to be an object fit star next year. Honestly, at this point,
[1716.34 → 1723.04] I think the groundswell of interest and talking to Adam on the show, I think Tailwind CSS is on my
[1723.04 → 1727.22] list of things to actually pick up and try on a real project versus just toying around with and
[1727.22 → 1732.94] reading about and then moving on. So that's on my to-do list. And I wouldn't say this survey made
[1732.94 → 1737.76] me think that, but I was already kind of thinking it. And then I see this, and I'm like, you know what,
[1738.16 → 1743.92] let's give it a shot so I can talk about it in more expert terms and not just armchair quarterback
[1743.92 → 1747.02] terms. So that's, that's what I'm definitely going to do here soon.
[1747.62 → 1753.48] I would say the same. I've been using Tailwind on my continuously evolving blog. I just never post to.
[1753.58 → 1754.44] I didn't know you had a blog.
[1754.72 → 1758.38] Because I don't post to it. I just change the technology that runs it.
[1758.64 → 1762.88] You have fallen into that classic developer blunder where to get started with a blog,
[1762.88 → 1766.54] you have to build yourself a custom blog, and you end up in this never ending loop of
[1766.54 → 1768.34] iterating and tuning and never publishing.
[1768.34 → 1772.32] Yeah. You only have one post every couple of years, and it's about how you rewrote your blog engine,
[1772.56 → 1772.86] you know?
[1774.86 → 1777.88] So that's your goal for this year. You're going to rewrite it again with Tailwind.
[1778.60 → 1779.36] I've already started.
[1779.68 → 1780.04] Oh, okay.
[1781.74 → 1782.12] Why wait?
[1782.22 → 1785.02] Tailwind 2 came out, and it has a dark mode now. So I need to figure out how to
[1785.02 → 1789.00] integrate that before I can actually post anything. I can't post anything without a dark mode.
[1789.26 → 1789.70] That's true.
[1789.90 → 1794.92] Yeah. I think that that's interesting. I will say that like day to day, so like day to day,
[1794.92 → 1800.50] what I write is React and specifically like a lot of the components that we're using are
[1800.50 → 1808.72] stylized material UI components, like from the material UI React library. And in a lot of ways,
[1808.76 → 1816.02] I don't end up writing CSS a lot. I like writing CSS, but I don't end up doing it because I get to
[1816.02 → 1822.14] play within the components that they provide, which is like a box component, for example, or a grid
[1822.14 → 1827.64] component, which gives me like a flex box style grid that I can lay things out with. And then box,
[1827.72 → 1834.16] I can set specific margin and paddings. And I like that because when I'm not writing straight CSS,
[1834.40 → 1838.96] I know that what I'm writing and the way that I'm styling things on the page is conforming to the
[1838.96 → 1845.12] overall design system that we have. And I like that I have those guardrails on me. And I know that
[1845.12 → 1850.06] I'm only ever reaching out to real CSS when I have something that doesn't fit within those guardrails.
[1850.06 → 1857.42] So I have like a an extra justification for that. I will be interested to see how that evolves.
[1857.84 → 1863.26] This is my first experience with it. And I wonder where stuff like that will be next year.
[1863.86 → 1870.36] My largest active project is changelog.com. And the CSS on changelog.com was written not by myself,
[1870.68 → 1878.20] but by Cody Peterson and his team and is modified and extended by me now. And it's BEM. And I hit my
[1878.20 → 1881.82] head against it enough, especially when it comes time to like, hey, it's almost like I need more
[1881.82 → 1886.10] componentization and BEM is not providing it. And or maybe Cody style BEM. I'm not,
[1886.16 → 1890.24] I'm not here to throw any, neither BEM nor Cody under the bus. It's just the state of the world
[1890.24 → 1895.98] that I'm in. I just find myself being like, I want to use this thing over here. And in order to get that
[1895.98 → 1900.82] done, I just feel like it's way harder than it needs to be. So I'm excited about the utility styles
[1900.82 → 1907.12] idea and see if that eases some of my pains with my current site. So I'm thinking about
[1907.12 → 1911.80] just taking the main design of changelog.com and just seeing if I can port it, you know,
[1911.86 → 1916.58] look for look from its current over to the tail end and just see what that process is like. That's,
[1916.66 → 1917.88] that's kind of the working plan.
[1918.46 → 1922.68] So I'm also doing most of my, well, when I'm working in the front end these days,
[1922.68 → 1926.86] I'm doing most of my work in React, and it's styled components and largely using a
[1926.86 → 1932.34] existing design library to the extent possible. So I don't get to play with this stuff as much
[1932.34 → 1938.02] as I used to. But I think one of the fascinating areas that to me is only really
[1938.02 → 1942.32] getting explored by a subset of folks is the extent to which you can use custom properties
[1942.32 → 1950.80] to enable that type of almost state-driven component. So like in your example, Jared,
[1950.98 → 1956.76] I imagine a lot of those BEM classes have hard-coded values in them and that's part of what makes it hard
[1956.76 → 1960.10] to move them over to new locations where things are slightly different.
[1961.04 → 1964.72] But one of the really cool things about custom properties is you can actually,
[1965.22 → 1969.06] like they're scoped in the same way that CSS is scoped and they cascade. So you could,
[1969.20 → 1975.10] if you were to rewrite those all using custom properties, then you could have whatever their
[1975.10 → 1982.04] container is in the new location, override those custom properties and have it essentially work
[1982.04 → 1986.04] in both locations. So I think there's some really, fascinating stuff there.
[1986.04 → 1991.16] And I've only seen a few people digging into that. There was a post I read recently that I can dig
[1991.16 → 1997.88] up for the show notes that was talking about the ways in which you can actually use CSS custom
[1997.88 → 2004.04] properties to communicate state in general to your UI and using it as a way to, for example,
[2004.60 → 2011.66] communicate. You could set up an API that actually is what the API returns is a set of CSS custom
[2011.66 → 2017.78] properties, and you plug those CSS custom properties into your site, and it ripples through because it
[2017.78 → 2022.00] communicates a set of state. A bunch of other interesting things that could happen there.
[2022.20 → 2028.54] And so I feel like that's an area that is ripe for some more tooling and some more exploration
[2028.54 → 2032.96] about the possibilities. Like a lot of the use cases I'm seeing out there right now for custom
[2032.96 → 2037.38] properties are pretty straightforward. They're replacing SAS variables, which is great. I mean,
[2037.38 → 2043.20] being able to do what we used to do with SAS variables in CSS is phenomenal. Don't get me
[2043.20 → 2049.32] wrong, but I think there's something that has potential to allow us to reimagine some of the
[2049.32 → 2051.90] ways we write CSS and do some fascinating things.
[2052.72 → 2053.56] That sounds fascinating.
[2053.98 → 2054.38] If I turn...
[2055.10 → 2062.38] What if I have prefers reduced motion turned on? Will it still ripple through or will it just...
[2062.38 → 2068.20] That joke wasn't even worth trying a second time.
[2069.56 → 2070.80] But I tried it anyway.
[2072.40 → 2076.66] Sorry, I just got keyed in on when you're like, it just ripples through your site. I was like...
[2076.66 → 2078.78] Maybe I should have said it cascades through your site.
[2078.92 → 2079.84] Thank you. Much better.
[2080.94 → 2081.72] What does that mean?
[2082.10 → 2083.58] Kind of like a ripple effect.
[2084.02 → 2085.42] Except playing on the cascade.
[2087.52 → 2090.22] I write modern CSS. I don't know what a cascade is anymore.
[2090.22 → 2090.72] Right.
[2092.40 → 2098.60] I think that next year, maybe not next year, but this survey in three to four years, it'll
[2098.60 → 2104.12] just continue to become more interesting because of, specifically I'm thinking of Houdini and
[2104.12 → 2110.66] exposing a CSS parser API and some of the layout stuff that they're bringing. It's going to
[2110.66 → 2114.62] change what you can do with CSS, and it's going to make it so powerful. And it's going to be
[2114.62 → 2121.40] fascinating to see how that trickles into the everyday CSS frameworks and libraries
[2121.40 → 2125.08] that we use and what that will mean in the future for styling the web.
[2125.08 → 2147.86] Have you heard about Knowable? It is an awesome new platform for learning from the world's best minds.
[2147.86 → 2151.76] Anytime, anywhere, at your own pace, through audio.
[2151.76 → 2158.70] Learn about the performance benefits of a plant-based lifestyle from NBA All-Star Chris Paul or how to
[2158.70 → 2163.96] launch a startup from Reddit co-founder Alexis Ghanian. There's even a 10 lesson course from
[2163.96 → 2166.38] astronaut Scott Kelly. Here's a sneak peek.
[2167.94 → 2174.24] We learned a lot up there, but what can you learn from a life in space? The answers might surprise you.
[2174.66 → 2179.32] In this Knowable course, I want to share some of the things I've learned that you might not expect.
[2179.32 → 2185.40] Lessons about leadership on a dark night on an aircraft carrier in the middle of a churning sea.
[2186.26 → 2191.48] Lessons about the fear you feel with 7 million pounds of thrust exploding underneath you.
[2192.70 → 2196.76] And most of all, there's an idea out there that astronauts are always perfect.
[2197.64 → 2199.16] Failure is not an option, right?
[2199.16 → 2205.10] That's why I want to take you through some of my life experiences to show you how that's just not true.
[2206.10 → 2214.70] I believe every day, regular, human failure, if we handle it right, can be one of our greatest opportunities to learn, grow, and succeed.
[2214.70 → 2223.26] Knowable is accessible on your phone and on the web, and each audio course is broken out into individual lessons, usually around 15 minutes long.
[2223.64 → 2228.22] As a Changelog listener, you can get an annual membership to Knowable for 20% off.
[2228.70 → 2232.16] Get unlimited access to every Knowable audio course right now.
[2232.40 → 2239.58] Just download the Knowable app or visit knowable.FYI and use code CHANGELOG for that 20% discount.
[2239.58 → 2242.74] We put a link in your show notes for easy click-ins.
[2242.94 → 2247.66] Check out Knowable today and start learning from hundreds of top experts from around the world.
[2247.94 → 2250.90] Once again, that's knowable.FYI, code CHANGELOG.
[2262.04 → 2267.02] Okay, let's get back to it and dig into the state of JS 2020.
[2267.02 → 2269.72] Now, Nick, I know there was something you had your eye on there.
[2269.98 → 2271.62] Just had to see how TypeScript was doing.
[2271.80 → 2272.68] And what's the story?
[2272.88 → 2274.04] Surprise, it's on top.
[2274.68 → 2275.50] It's on top.
[2277.30 → 2289.38] Yeah, since 2017, in fact, every year of this survey, except for the first year, 2016, it's been in first place for the flavours of JavaScript, the preferred flavours of JavaScript.
[2289.78 → 2292.82] And in 2016, it was in second place.
[2293.22 → 2294.84] But it's remained in first place.
[2294.84 → 2295.74] It's very popular.
[2296.28 → 2308.72] And it's pretty cool seeing that it has nearly 88% of respondents really approve of it, meaning that they are interested in it or have used it and would use it again, which is extremely high.
[2308.84 → 2314.94] Like, we don't really have things that get that much universal approval, except for on this podcast.
[2314.94 → 2318.06] I don't like it.
[2318.22 → 2318.36] See?
[2318.40 → 2318.74] Just kidding.
[2321.34 → 2322.04] No reason.
[2322.74 → 2323.64] I just like to say that.
[2324.22 → 2326.66] I didn't take the jump for a long time.
[2326.78 → 2332.18] And then at my job, when I started there, what, a year and two months ago or whatever, they were using TypeScript.
[2332.34 → 2333.76] And so I started making the jump.
[2333.80 → 2336.00] And now I don't know how I'd live without it.
[2336.00 → 2336.44] Exactly.
[2337.64 → 2339.80] It's painful to write regular JS now.
[2340.28 → 2340.62] Why?
[2341.30 → 2342.70] Because you have Stockholm Syndrome?
[2343.62 → 2344.10] Probably.
[2344.82 → 2348.40] I used to think, like, oh, I've used Vim for 10 years, right?
[2348.46 → 2353.76] And for most of that, Vim was just an editor that really didn't give me much help.
[2353.84 → 2356.84] It didn't do, I didn't have completion turned on at all for anything.
[2356.84 → 2363.96] And I would just write straight JavaScript, and I'd have so much of the state of, like, what I'm working on built up in my head.
[2364.38 → 2366.60] And I would just be resetting it from memory.
[2366.68 → 2369.92] And, of course, I've gotten older now, which means I probably can't do that anymore.
[2370.62 → 2376.52] And the tools have just gotten so amazing that now I just rely on it for everything.
[2376.52 → 2388.30] And I'm constantly trying to figure out ways to creatively use TypeScript to make sure that things that normally aren't autocompleted can be autocompleted to make my life and everyone else's life easier.
[2388.38 → 2390.56] Because I also can't spell.
[2390.78 → 2394.36] And I can constantly just write things incorrectly.
[2394.62 → 2397.84] And I get that checked in and then realize later that I misspelled something.
[2398.16 → 2402.82] And, you know, I'm talking about things that aren't type checked, like keys to things.
[2402.82 → 2407.46] I will point out that function names get misspelled still.
[2408.06 → 2412.90] And autocomplete, in some ways, actually makes that worse because people will misspell it.
[2412.94 → 2414.18] You propagate the misspelling.
[2414.52 → 2419.36] People will misspell it once, and then they'll just, like, keep it going through everything.
[2420.00 → 2428.88] Nick, I think at this point, if Vim is doing most of the work for you, maybe your employer should just reduce your salary and make donations to the Vim working group.
[2428.98 → 2430.14] Don't you believe that's the case?
[2430.42 → 2432.04] We're going to have that stricken from the record, Jared.
[2432.04 → 2435.04] But, uh...
[2435.04 → 2437.80] Real developers have all the APIs memorized.
[2438.04 → 2438.72] Don't you know that?
[2438.80 → 2439.48] Come on, man.
[2439.62 → 2440.74] You got to have it internalized.
[2440.82 → 2444.40] Now, remember, Jared, it's about the value being provided.
[2444.64 → 2446.28] Like, it's the value-added tax, right?
[2446.40 → 2446.84] I agree.
[2446.94 → 2448.46] Vim is providing a lot of value.
[2449.12 → 2454.66] He might internally choose to pay Vim, but, like, that's a black box to his employer.
[2455.14 → 2456.62] Or it was until this podcast.
[2458.22 → 2461.40] Nick chooses to pay Vim by making mentions of it on podcasts.
[2461.40 → 2461.76] See?
[2462.06 → 2462.70] It's promotional.
[2462.90 → 2463.34] He's promotional.
[2463.44 → 2465.02] I'm like the guy from Office Space.
[2465.16 → 2468.86] I talk to Vim so that my employer doesn't have to.
[2468.92 → 2470.34] Your employer doesn't have to.
[2471.50 → 2473.46] Well, I think your employer would appreciate that.
[2474.02 → 2476.44] Let's hard transition away from TypeScript, shall we?
[2476.44 → 2477.44] Sure.
[2480.76 → 2481.80] Jared, what did you notice?
[2482.76 → 2487.92] People, more and more, do not think that building JavaScript apps is overly complex.
[2488.96 → 2490.58] I said that in a confounding way.
[2491.12 → 2492.64] People think it's getting less complex.
[2493.28 → 2497.34] From 2016 to 2020, opinions have started to shift.
[2497.34 → 2503.86] Maybe we're starting to see some, I don't know what you call it, centralization around certain things.
[2504.76 → 2515.00] Maybe the Cambrian explosion of frameworks and tools and build tools and stuff started to, like, kind of congeal around, generally speaking, React and Webpack.
[2515.00 → 2518.34] And other things kind of on the periphery of that.
[2518.54 → 2518.88] I don't know.
[2519.14 → 2520.48] Or why do you guys think it is?
[2520.58 → 2522.88] Has it gotten less complex in the last four years?
[2522.92 → 2528.84] Because the surrounding opinions, at least according to this survey, are that it's less complex now.
[2528.92 → 2530.90] Or I used to think it was complex and now I don't.
[2530.92 → 2533.52] Or I didn't take this before, and now I took it and I don't think it's complex.
[2534.04 → 2538.82] But overall opinion is going to disagree with that statement, that it's more, that it's complex.
[2539.34 → 2539.80] I don't know why.
[2539.80 → 2547.66] I would think that there's a huge correlation between thinking it's complex and writing your own Webpack config.
[2548.38 → 2552.58] Versus using something like Create React app and just getting to work on your project.
[2553.26 → 2558.18] So back in 2016 we all wrote our configs, and now we've just been using that config for the last four years, and it feels great.
[2558.34 → 2558.78] Exactly.
[2559.00 → 2559.88] That's factual for me.
[2560.42 → 2560.90] Good point.
[2561.40 → 2567.98] Somewhat related to that, I think there has been a rise in what I've kind of called meta frameworks or higher level frameworks.
[2567.98 → 2584.14] So this is things like Next and Next or Gatsby or other things where we're basically building, you know, there's still innovation happening at the level of the frameworks of React or Vue or Angular or Svelte or what have you.
[2584.56 → 2589.38] And we can talk about Svelte a little bit because that was one of the fun stars of this report.
[2589.38 → 2605.28] But there's also been tremendous emphasis ongoing one level up and saying, okay, we're going to wrap up a lot of the common problems that people are solving over and over again with these frameworks and just provide standardized ways to do them.
[2605.28 → 2610.62] And that, I think, has dramatically simplified the experience of building it now.
[2610.96 → 2615.90] And I don't know if I saw in this survey, it was probably there somewhere.
[2616.26 → 2617.98] I can look for that as we speak.
[2618.10 → 2631.10] But I think the adoption of those libraries has gone way up probably looking at this graph in that same time span of like 2018, 2019.
[2631.10 → 2631.54] Yeah.
[2632.74 → 2638.48] And Next.js overtook Express as the most popular backend framework, which was fascinating.
[2639.82 → 2641.00] Why do you think that happened?
[2641.64 → 2648.70] I think for a lot of the reasons that we've been talking about, it just provides a more cohesive experience for putting things together.
[2648.70 → 2652.54] And it kind of puts those rails in place a little bit for you to follow.
[2652.98 → 2654.70] So it feels like you're doing the right thing.
[2655.58 → 2660.84] Whereas Express can kind of be like a wild west of stringing things together.
[2661.10 → 2662.84] Fewer decisions to make.
[2663.20 → 2681.10] So my criticisms of the early Node.js JavaScript web-based community back when I was more on the Ruby side of the fence was that it was so micro and library focused that it was like assembling a transformer from parts.
[2681.94 → 2683.20] You had to pick everything.
[2683.40 → 2684.24] You had to make all your own decisions.
[2684.24 → 2693.14] And that's really empowering to a lot of expert level developers because they already have well-formed opinions, and they know what they like, and they don't like.
[2693.36 → 2695.84] They know what works well in this case and what doesn't.
[2696.24 → 2703.90] But for the rest of us, it's kind of like, I don't want to make a thousand decisions before I can say hello world or slightly better than hello world, right?
[2704.18 → 2706.68] Before I can serve my first dynamic web page.
[2706.68 → 2713.52] And there was way more configuration and choice than there was convention and opinionated things.
[2714.30 → 2724.20] And we've definitely seen more opinionated frameworks and tools coming out over the last few years in the JavaScript space and JavaScript developers adopting those things.
[2724.20 → 2733.68] And I think that that makes you feel like the whole process is less complex because just way fewer decisions to make, like you said, Nick.
[2733.82 → 2741.70] Another interesting thing that I saw on the backend satisfaction survey was the decline of Gatsby.
[2741.90 → 2743.98] It dropped five places in a year.
[2744.56 → 2747.66] It's almost like it got hit by a meteor, which also dropped five places.
[2750.88 → 2752.08] Well played.
[2752.08 → 2755.30] Those are two falling stars at this point.
[2756.06 → 2764.58] And it's hard to tell because a lot of these items that are being put in here in 2020, it got a lot more data.
[2764.78 → 2766.96] There's a much broader data set being put there.
[2767.08 → 2771.14] But I think there was a lot of disillusionment with Gatsby in this last year.
[2771.20 → 2780.16] There was a lot of people refuting the performance claims and saying essentially that they were gaming the benchmarks.
[2780.16 → 2788.88] Yeah, I guess the thing that ties those two particular frameworks together is that they're both open source but venture backed.
[2789.38 → 2790.10] They venture backed?
[2790.32 → 2791.30] At least business backed.
[2791.60 → 2792.36] I know that's true.
[2792.54 → 2794.24] I'm not sure if Meteor was venture backed or not.
[2794.24 → 2812.52] But when we mix those things together, business concerns, open source concerns, it goes back to the open core problem of what goes in the open source and what is a commercial feature, which every open core style company has to decide over and over again.
[2812.52 → 2819.42] And in the case of Gatsby, it's not typical open core, but it's like open build.
[2819.88 → 2821.22] I don't know how you call it.
[2821.28 → 2826.38] Anyway, the commercial side and the open source side definitely have that give and take.
[2827.22 → 2829.68] And so I'm not saying that's the reason why these things are falling out of favour.
[2829.78 → 2833.72] I'm just saying it's interesting that both of those frameworks have that in common.
[2833.72 → 2839.92] Yeah, though the counterpoint is Next.js is primarily backed by Tercel, right?
[2840.00 → 2842.46] And they are also for-profit business.
[2842.70 → 2846.20] Though they, I think, sell more general purpose hosting.
[2846.44 → 2849.44] So it's not just about their framework.
[2849.56 → 2853.48] Where Gatsby, I think their business stuff was all just about the framework.
[2853.48 → 2869.60] Yeah, it's like Tercel has enough of a dividing line between Next.js and their hosting services that maybe that somewhat, that conflict of interest, which is effectively what we're talking about, doesn't mean you're not doing it right.
[2869.64 → 2871.96] But that conflict is there, and you have to navigate that.
[2872.12 → 2875.46] Maybe their conflict is not quite as tightly tied, right?
[2875.52 → 2877.52] Because Gatsby is Gatsby, so to speak.
[2877.52 → 2883.36] And I'm not sure what the details behind Meteor's business model was because I was never in that community.
[2884.04 → 2889.44] But yeah, I mean, a lot of these things do have corporate backing, whether they're tied to the product or not.
[2889.54 → 2896.28] It's just that it seems like when you're tied directly to the product, it's more difficult to navigate that relationship for people.
[2897.22 → 2906.46] Yeah, well, and in Gatsby's case, I think you ran into a very specific conflict of interest where the product was about speeding up the build.
[2906.46 → 2911.98] And so if they did a good job at speeding up the build in the open source project, the product became more obsolete, right?
[2912.02 → 2919.52] So you not only have decisions to navigate, but you have like direct conflict between what's better for the open source project and what's better for the business.
[2920.74 → 2922.86] But Svelte, on the other hand...
[2922.86 → 2929.90] Svelte was the rising star here in terms of coming out of nowhere in 2019
[2929.90 → 2937.04] and being the top-ranked front-end framework for 2020.
[2938.50 → 2945.42] Just slightly beating out React, which had kind of been on and off holding that top spot for a while.
[2945.54 → 2948.04] Vue stepped in the top spot for one year in 2018.
[2948.86 → 2951.96] And really, like, they're all kind of bunched towards the top.
[2952.40 → 2952.50] Yeah.
[2952.50 → 2955.94] But yeah, Svelte is kicking butt and taking names.
[2956.60 → 2961.38] Yeah, it's worth noting that this is based on overall satisfaction, interest, usage, and awareness.
[2961.78 → 2966.28] And that like the percent differences are like 1% or 2% here or there.
[2966.50 → 2972.26] So it's not like, you know, 40% more people chose Svelte over React.
[2972.26 → 2977.78] We're talking like literally in this case, it's 1% difference on the satisfaction chart.
[2978.10 → 2982.00] 89% for Svelte and 88% for React.
[2982.00 → 2987.94] But yeah, definitely new kid on the block last year and top of the block this year.
[2988.56 → 2993.06] Well, and one of the other interesting things there is like the vast majority of those folks
[2993.06 → 2996.30] are not saying they've tried it, they liked it, and they want to use it again.
[2996.46 → 2999.22] They're instead saying, I've heard about it, and I'm interested.
[2999.80 → 3001.34] I know why it overtook in 2020.
[3002.02 → 3006.64] There's a blog post that they have from July 17th called Svelte Loves TypeScript.
[3007.68 → 3009.24] Where they have 50% introduced support.
[3009.24 → 3009.98] Stop it.
[3010.62 → 3011.62] Don't do that to us.
[3012.00 → 3015.30] Oh, that reminds me about a good blog post we should write.
[3015.78 → 3017.08] JS Party loves TypeScript.
[3019.08 → 3021.34] Is that all you got to do to get number one?
[3021.74 → 3022.02] Apparently.
[3022.56 → 3026.96] The other fascinating thing looking at this like overall rankings chart
[3026.96 → 3035.30] is the extent to which both Angular and Ember have crashed and burned over the last few years.
[3035.30 → 3039.08] Ember is never one of the super top frameworks.
[3039.08 → 3041.20] But Angular, I mean, look at them.
[3041.34 → 3049.84] They've gone from 2017, 66% kind of satisfaction, interest usage, however, that's getting broken out,
[3050.08 → 3053.94] down to 42% second from the bottom.
[3053.94 → 3058.26] This is where the bias of the survey kind of shows, I think, though.
[3058.32 → 3064.64] Because I still feel like, just from my own anecdotal experience, Angular is king in the enterprise.
[3064.64 → 3070.46] So if you guys are looking at the rankings chart, and you're on the first tab, you're looking at satisfaction,
[3070.66 → 3072.30] you have to click over to interest and usage.
[3072.50 → 3074.82] So when you click over to usage, it changes things quite a bit.
[3074.82 → 3075.24] Oh, I see how that is.
[3075.24 → 3077.42] Okay, so Angular is quite a bit.
[3077.42 → 3077.60] Oh, yeah.
[3077.68 → 3079.26] Now you're at 56% usage.
[3079.98 → 3083.02] What Svelte is topping is the satisfaction and the interest.
[3083.78 → 3086.96] It's definitely not topping the usage, right, because it's still pretty new.
[3087.14 → 3087.98] So you got to click through.
[3088.56 → 3091.48] Angular is still greatly used, but the satisfaction is down.
[3091.86 → 3092.34] There we go.
[3092.62 → 3093.38] Yeah, that makes sense.
[3093.46 → 3099.38] So Angular is number two in usage, but second to last place in satisfaction.
[3099.90 → 3100.20] Yeah.
[3100.28 → 3101.04] I totally buy that.
[3102.08 → 3104.84] Well, I mean, some of it's like you're forced to use a thing at your job.
[3105.24 → 3106.84] You know, like that's a real thing, right?
[3106.84 → 3109.28] Like, well, we're using Angular, so you're going to use Angular.
[3109.46 → 3113.62] And it's like, whether it's on merit or not, we just have bad feelings when it's
[3113.62 → 3115.54] like, oh, my boss made me do this.
[3115.62 → 3119.44] And the more and more enterprise you are, the less and less agency you have as an individual
[3119.44 → 3121.80] developer to choose your tools, right?
[3121.88 → 3125.94] And so anything that's big in the enterprise, I think, is naturally going to struggle in a
[3125.94 → 3126.76] satisfaction survey.
[3127.20 → 3128.02] That's just my opinion.
[3129.06 → 3129.64] Subtype script.
[3131.60 → 3132.60] That's just your opinion.
[3133.36 → 3135.00] Actually, no, it's not, because it did really well.
[3135.00 → 3135.38] Oh, darn it.
[3135.86 → 3140.94] That is an interesting point, because if I look at these graphs side by side, the satisfaction
[3140.94 → 3148.38] and the usage, Angular's satisfaction numbers plummet when their usage numbers skyrocket.
[3149.38 → 3153.58] So a lot of folks are suddenly having to use this thing and ain't liking it.
[3153.58 → 3154.28] Mm-hmm.
[3154.28 → 3158.64] So one cool thing, as we're going a bit meta about the charting, one cool thing I've done
[3158.64 → 3164.24] this year is they've integrated some qualitative data as well, which is like random shout-outs
[3164.24 → 3166.22] from different developers, which I think is really cool.
[3166.34 → 3170.28] Like whenever you're just staring at charts and data and numbers, you know, you can get
[3170.28 → 3173.50] kind of like that blank stare and sometimes misread things.
[3173.50 → 3179.04] But as you scroll some of these, they'll have different people giving their qualitative kind
[3179.04 → 3179.52] of picks.
[3181.22 → 3186.46] And like, for instance, Cassidy Williams on the opinion section, her pick was Ben Hong.
[3186.46 → 3192.42] So she then links out to Ben Hong and like gives him a shout-out and says why he's doing
[3192.42 → 3194.00] awesome stuff for the community.
[3194.12 → 3197.78] So I think that was a nice touch this year, adding those little things, because it breaks
[3197.78 → 3203.40] up the data, and it also allows individual voices to be heard versus just like, here's
[3203.40 → 3204.16] what everybody said.
[3204.52 → 3204.84] Cool idea.
[3204.84 → 3209.24] And when you actually filled out the survey, I thought it was kind of cool that they showed
[3209.24 → 3212.80] you how you ranked compared to everyone else who's previously taken it.
[3213.70 → 3220.38] So like if you said, oh, you know, 3% of what our typical survey user does in my case,
[3220.48 → 3221.02] in some cases.
[3221.46 → 3223.58] They tell you at the very end, or they tell you right after you answered?
[3224.04 → 3225.16] Yeah, at the very end, I believe.
[3225.44 → 3225.76] Okay.
[3225.96 → 3227.64] Because I'd use that to change my answers.
[3228.64 → 3229.32] What's this one?
[3229.72 → 3230.50] That would be bad.
[3230.82 → 3231.30] That would be bad.
[3231.80 → 3232.16] Cool.
[3232.16 → 3234.84] Well, same question we asked in CSS.
[3235.12 → 3240.00] Based on this, anything you are particularly looking to check out this year?
[3240.28 → 3244.52] And Nick, TypeScript is not a valid answer for you, because I know you've already checked
[3244.52 → 3245.02] this out.
[3247.28 → 3250.94] Yeah, I'll go first and say that I really want to try out Svelte.
[3251.36 → 3254.18] I've seen, you know, not just this, but blog posts about it.
[3254.32 → 3259.72] And overall, in just like random discords and slacks that I'm in, it does seem like it's
[3259.72 → 3264.16] a satisfactory library that people generally like to use.
[3264.30 → 3265.32] And I want to know why.
[3266.08 → 3267.56] So I need to play around with it.
[3268.72 → 3271.68] I gave Svelte a try back in 2019.
[3272.28 → 3275.24] I did a talk at All Things Open about it, just like an intro talk.
[3275.40 → 3279.62] And so that allowed me an opportunity to dive into it and to build a little thing, like
[3279.62 → 3283.28] a little one-page app with Svelte that I used at the conference.
[3283.28 → 3285.26] And it was lots of fun.
[3285.34 → 3286.12] I really liked it.
[3286.16 → 3287.82] I just haven't revisited it yet.
[3288.22 → 3293.74] So looking at this and just thinking in general, a technology that I am going to give a shot
[3293.74 → 3295.72] this year, I've never used Next.js myself.
[3296.14 → 3302.50] So I like the idea of a hybrid, you know, mostly JAM stack, but also with some backend possibilities
[3302.50 → 3305.88] and pre-rendering a bunch of stuff, but then allowing for updates.
[3305.88 → 3312.32] I think it looks like it's a very flexible tool that is up my alley.
[3312.66 → 3314.46] So I am going to give Next.js a try.
[3314.64 → 3315.26] At least I want to.
[3315.88 → 3316.56] What about you, K-Ball?
[3317.26 → 3317.54] Yeah.
[3317.66 → 3321.90] So I have tried Svelte and I have played with Next a little bit, though nothing serious.
[3323.10 → 3325.04] Both phenomenal pieces of work.
[3325.18 → 3327.46] So definitely check those out and enjoy them.
[3327.92 → 3333.04] The one that I'm actually looking at that I'd heard show up a little bit on my radar before,
[3333.04 → 3338.30] but that I haven't tried out, and it showed up at the top of the satisfaction list for
[3338.30 → 3344.70] the testing category is the new testing library that I think was Kent C. Dodds putting it together.
[3344.94 → 3347.84] And I think he put it together as a part of writing a course.
[3348.38 → 3352.76] But I've heard a few things trickling through, and it looks like the people who are trying
[3352.76 → 3354.10] it is loving it.
[3354.26 → 3359.46] So that's on my radar for this year is trying out the testing library.
[3360.00 → 3361.36] I have tested that.
[3361.84 → 3362.44] What's it called?
[3362.44 → 3364.44] I believe it's called testing library.
[3366.04 → 3366.78] No, seriously.
[3366.90 → 3367.30] What's it called?
[3368.84 → 3370.92] I have tried it, and it's pretty nice.
[3371.28 → 3371.82] I like it a lot.
[3372.40 → 3372.96] What makes it sad?
[3373.06 → 3373.84] So you've tried it, Nick.
[3374.10 → 3375.50] Is it different or new?
[3375.60 → 3377.34] I mean, I'm most familiar with Mocha.
[3377.62 → 3378.36] What's different about it?
[3378.40 → 3380.90] Like, why would I be more satisfied, or why would I give it a shot?
[3381.38 → 3386.82] So I'm probably going to get this totally wrong, but it seems like is a tool written to
[3386.82 → 3391.72] help you write tests in the way that I think Kent C. Dodds kind of prescribes, which is
[3391.72 → 3395.58] writing a lot of tests that are mostly integration style tests.
[3395.58 → 3399.30] And so this gives us, and I've only used it in the context of React.
[3399.30 → 3403.46] So it gives me like this render method that I can call, and I can render any component that
[3403.46 → 3403.80] I want.
[3404.32 → 3406.42] And then I have this screen object that I import.
[3406.88 → 3409.32] And from that screen, it's basically like my computer screen.
[3409.32 → 3411.38] And so I can do queries to find things.
[3411.74 → 3414.98] Like it just makes it really easy to traverse the DOM, get at what I want.
[3415.44 → 3419.48] And then I use a Jest, what are those libraries called?
[3419.74 → 3424.54] Like the, the Jest assertion library that adds in a bunch of like testing library
[3424.54 → 3428.16] specific or, or DOM, I guess, specific assertions.
[3428.34 → 3431.32] So I can just say like, you know, expect that this element is visible.
[3431.48 → 3436.36] And when I fire this event and testing library makes it really easy to fire events on buttons
[3436.36 → 3443.02] or, or whatever, then, you know, I can assert and expect that, that a button or modal is
[3443.02 → 3443.76] now showing up.
[3444.16 → 3449.90] And so I'm testing from the perspective of the user rather than just writing unit tests,
[3449.90 → 3454.04] which might not really represent the state of the application.
[3455.04 → 3460.68] So it's closer to something like a Selenium or that type of testing?
[3461.42 → 3465.98] Yeah, but not doing anything in regard to like the Selenium APIs.
[3465.98 → 3469.24] I forgot what those are called, but like you're not controlling a browser.
[3469.42 → 3473.26] You're still just like, it has a virtual DOM, and you're working within that virtual DOM
[3473.26 → 3477.64] to manipulate the DOM nodes within, but not a, not a real browser.
[3478.36 → 3479.60] Which probably keeps it pretty fast.
[3479.88 → 3482.98] Might be worth getting Kent on the show and haven't, I haven't heard about this.
[3483.22 → 3488.72] And I definitely think it's interesting if you have a new testing library.
[3488.96 → 3492.56] First, we'll get our crack team of marketers on, on the case, and we'll get Kent
[3492.56 → 3493.58] a better name for this thing.
[3493.58 → 3497.16] Unless it's like the testing library, then I guess he's already dominated the industry.
[3498.02 → 3501.18] I mean, if you search for testing library right now, it's number one.
[3501.38 → 3503.94] So like, all right, maybe he wins, and we don't need to rename it.
[3503.96 → 3505.22] That might actually be pretty brilliant.
[3507.08 → 3513.24] But you know, in 2020 or 2021 to come up with a new testing library and then have it be enjoyed
[3513.24 → 3515.60] by many people, it has to kind of have its own view of the world.
[3515.60 → 3519.74] And so I think maybe it'd be a good show is bringing him on and talking about it.
[3520.36 → 3524.96] Would you use it alongside like a unit testing library or, or can also just do unit testing
[3524.96 → 3525.34] as well?
[3525.98 → 3527.22] Yeah, I'm using it within Jest.
[3527.38 → 3532.44] So I'm writing typical Jest tests and I have some unit tests kind of interspersed within
[3532.44 → 3533.08] there as well.
[3533.08 → 3538.56] But then most of it is driven through testing library and, and rendering my components that
[3538.56 → 3538.84] way.
[3539.40 → 3539.58] Neat.
[3539.78 → 3544.78] So it's, it's more of a replacement for, um, oh, what now I'm forgetting the name of
[3544.78 → 3548.04] that, that library that was really popular in React.
[3548.26 → 3549.32] You know what I'm talking about?
[3549.70 → 3550.18] Let's see.
[3550.24 → 3553.62] There's Cypress, Playwright, Storybook, Puppeteer, Mocha.
[3553.78 → 3556.10] I'm just reading the different testing libraries on the webpage.
[3556.46 → 3556.70] Ava.
[3557.06 → 3560.28] No, I can't, I cannot believe I can't remember the name of it.
[3560.68 → 3561.60] Web driver IO.
[3565.06 → 3565.46] Okay.
[3565.48 → 3566.50] I've exhausted the list.
[3566.92 → 3568.78] And I'm Googling for it and I can't find it.
[3568.84 → 3569.36] So it's not.
[3569.76 → 3571.30] Maybe it was just in your head, Nick.
[3572.50 → 3572.88] Enzyme.
[3573.48 → 3573.88] That's it.
[3574.18 → 3575.08] Oh, okay.
[3575.18 → 3576.28] It's more of a replacement for enzyme.
[3576.72 → 3577.18] All right.
[3577.44 → 3581.18] Well, Kent, if you're listening, hit us up.
[3581.22 → 3583.36] We'd love to have you on the show to talk about testing library.
[3584.10 → 3584.42] Absolutely.
[3584.42 → 3587.16] One more thing I want to try this year on build tools.
[3587.44 → 3588.04] Yes, build.
[3588.82 → 3589.12] Oh, yeah.
[3589.46 → 3590.28] Pure speed, baby.
[3590.48 → 3590.96] I love it.
[3591.28 → 3592.58] Let's just go as fast as we can.
[3593.66 → 3599.70] And this is the Go-based JavaScript build tool that's high on satisfaction and pretty new.
[3599.86 → 3600.96] I think it came out last year.
[3601.22 → 3602.32] Very low on usage.
[3602.64 → 3604.68] 6% usage because new.
[3605.54 → 3609.38] And pretty low on awareness, 26%, but 94% satisfaction.
[3609.38 → 3616.26] So definitely want to give that a try because the faster things build, the better, in my humble opinion.
[3616.90 → 3616.96] Yeah.
[3616.96 → 3630.06] And this year, I think in April, the last version of Node that doesn't support, I think that's 10.x, that doesn't support the ES module syntax will be end of life.
[3630.32 → 3633.92] So then we will have that in Node for sure everywhere.
[3633.92 → 3644.06] And so it'll be fascinating to see how that works and kind of along the whole lines of the Fred K. Shop pipeline, seeing how that grows over the next couple of years.
[3644.62 → 3646.90] How up to date do folks run Node?
[3647.14 → 3648.36] Just generally, Node developers.
[3648.54 → 3653.30] Are they generally on the latest major release or do people stay behind?
[3653.30 → 3661.66] I suspect it depends on whether you're writing Node apps or you're using Node as a way to render a web application.
[3662.28 → 3663.78] I'm referring more to apps.
[3664.08 → 3664.70] I don't know.
[3665.70 → 3667.00] I guess I'm asking a question.
[3667.02 → 3667.78] I can tell you that we're writing.
[3667.92 → 3668.42] How would you know?
[3668.46 → 3669.18] Well, we could take a survey.
[3669.88 → 3670.02] Yeah.
[3670.60 → 3671.02] Yeah.
[3671.08 → 3674.74] I'm not confident in our ability to get representative samples after all.
[3675.10 → 3677.34] In our surveys, nobody liked reggaeton.
[3677.58 → 3679.06] I mean, come on.
[3679.46 → 3680.72] That actually might be representative.
[3680.72 → 3685.74] Nick, I ask you because you're a little more plugged into corporate America than I am.
[3686.30 → 3690.00] Just generally, like Node developers, in your experience, not a survey.
[3690.98 → 3699.40] Do people generally want to keep their Node apps running the latest Node or do they lock one version, and they're running Node from three years ago or what?
[3699.88 → 3701.30] I've seen a lot of both.
[3701.68 → 3706.18] But mostly I think that it tends towards trying to run the latest LTS version.
[3706.72 → 3707.24] Makes sense.
[3707.24 → 3712.56] Well, definitely we should see a pickup of things like ESBuild and Snowpack and whatnot after that, after April.
[3712.92 → 3719.58] So I would expect the next survey to have, because the interest is high, and the satisfaction is high on these things, you'd expect a usage spike.
[3719.72 → 3722.08] So maybe we can check back next year on that front.
[3722.46 → 3723.30] Sounds good.
[3723.30 → 3728.66] Well, with that, I think we have sufficiently beaten these surveys to death.
[3729.18 → 3740.04] Thank you both, gentlemen, for exploring this, for not sticking too much in TypeScript land when we're talking about everything else, and for joining me in the bad puns.
[3740.04 → 3740.60] It's popular.
[3740.94 → 3741.56] I can't help it.
[3742.20 → 3742.56] All right.
[3742.56 → 3744.72] With that, we're going to sign off.
[3744.88 → 3746.20] Thank you, JS Party people.
[3746.56 → 3748.04] Enjoy your week.
[3748.26 → 3750.92] We'll catch you next week with another party.
[3751.42 → 3755.16] Remember, we record live on Thursdays, 10 a.m.
[3755.48 → 3757.68] Jared will tell you that again, but really join us.
[3757.78 → 3760.72] It's what makes this a party is when we're all hanging out on Slack.
[3761.26 → 3763.96] You all are making fun of us at the same time as we're making fun of us.
[3764.08 → 3764.76] It's a good time.
[3765.16 → 3765.40] All right.
[3765.48 → 3765.90] Take care.
[3766.08 → 3767.88] And this is K-Ball signing out.
[3767.88 → 3773.72] We do record live, just like K-Ball said.
[3774.02 → 3776.16] Subscribe and watch on our YouTube channel.
[3776.42 → 3778.72] That's YouTube.com slash changelog.
[3778.82 → 3781.80] And join our community Slack where all the chatter is.
[3781.80 → 3784.28] We hang in the JS Party channel during the show.
[3784.46 → 3787.12] Head to changelog.com slash community to sign up.
[3787.32 → 3788.28] It'll cost you $0.
[3789.16 → 3793.94] Congrats to Maxime Dupree and Eddie Link for winning those free Tests Summit tickets.
[3794.28 → 3796.24] Follow us on Twitter for upcoming giveaways.
[3796.24 → 3797.98] We are at JS Party FM.
[3798.54 → 3801.06] Music for JS Party is provided by Break master Cylinder,
[3801.30 → 3804.08] and we are sponsored by awesome people at Companies Who Get It.
[3804.24 → 3807.54] Thanks to Vastly, Linde, and Launch Darkly for having our back.
[3807.86 → 3808.62] Stay tuned.
[3808.76 → 3811.74] We have special guest Benjamin Coe from Google on the next episode.
[3812.00 → 3814.24] That one will hit your podcast feed next week.
[3814.24 → 3842.12] I have to decide if I want to leave that ripple part in and take it out.
[3842.12 → 3843.02] Yes.
[3844.40 → 3846.04] All the white space.
[3846.48 → 3846.78] The white space.
[3847.08 → 3848.30] All of it just standing there.
[3848.80 → 3849.58] What if I...
[3849.58 → 3850.80] First, I fumbled it.
[3851.12 → 3852.48] Then it wasn't funny anyway.
[3853.18 → 3854.50] So it was like a double whammy.
[3855.82 → 3858.76] It's hard to say preferred reduced motion off the top of your head.
[3859.10 → 3860.46] Prefers reduced motion.
[3860.88 → 3862.38] Yeah, that was really difficult.
[3862.38 → 3865.16] Well, my friend respect.
[3865.38 → 3866.66] I've got one full of photos.
[3866.90 → 3867.66] And then...
[3867.66 → 3869.32] My friend said to me,
[3869.32 → 3869.70] I'll see you later.
[3869.70 → 3871.54] Heavenly woos.
[3871.54 → 3872.44] 했습니다 impostor.
[3872.68 → 3873.36] Equal Shark.
[3873.72 → 3874.36] I know.
[3874.60 → 3875.34] ι supremacy
[3875.34 → 3875.70] Erica cars.
[3875.70 → 3876.40] I know.
[3876.40 → 3877.58] It's just a little scary opportunity here.
[3877.72 → 3880.28] Let's go help.
[3880.38 → 3880.98] Today...
[3880.98 → 3881.72] Today...
[3881.72 → 3882.28] Is there a voice.
[3882.30 → 3882.82] Today...
[3882.82 → 3883.32] Wednesday...
[3883.32 → 3884.26] Tonight...
[3884.26 → 3884.80] Twitter...
[3884.80 → 3885.44] Today...
[3885.44 → 3885.82] Today...
[3885.82 → 3886.22] Ladies on...
[3886.22 → 3887.28] Night...
[3887.28 → 3887.80] Ohio...
[3887.80 → 3888.00] lover...
[3888.00 → 3888.22] Today...
[3888.22 → 3888.78] Playings...
[3888.78 → 3889.26] East...
[3889.26 → 3889.84] City...
[3889.84 → 3890.92] ...
[3890.92 → 3891.22] огμεlass.

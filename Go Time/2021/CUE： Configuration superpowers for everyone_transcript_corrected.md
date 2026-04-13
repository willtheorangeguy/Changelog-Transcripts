[0.00 → 0.94] Okay, right.
[1.16 → 1.86] So, okay.
[1.92 → 4.02] That is quite unpopular to not give an opinion.
[5.42 → 8.16] And in the spirit of Q, that's quite meta as well.
[8.40 → 9.28] You know.
[9.76 → 11.36] I trimmed my unpopular opinion.
[11.64 → 11.82] Yeah.
[13.66 → 14.98] That's a Q joke, isn't it?
[15.14 → 15.48] It is.
[15.56 → 15.80] Yeah, yeah.
[15.84 → 16.66] Yeah, I don't get it yet.
[16.90 → 19.42] But I'm going to learn Q, and then I'm going to come back and listen.
[19.56 → 21.02] I'm going to be loving that.
[23.36 → 25.86] Bandwidth for Change Log is provided by Vastly.
[26.18 → 28.04] Learn more at fastly.com.
[28.04 → 30.58] Our feature flags are powered by Launch Darkly.
[30.86 → 32.66] Check them out at LaunchDarkly.com.
[32.90 → 34.90] And we're hosted on Leno Cloud Servers.
[35.14 → 38.64] Get $100 in hosting credit at Leno.com slash Change Log.
[38.98 → 39.78] What's up, Gophers?
[39.84 → 43.96] This episode is brought to you by Modish, a podcast from the team at Heroku,
[44.42 → 47.46] exploring code, technology, tools, tips, and developer life.
[47.78 → 49.72] There's a ton of great episodes on the Modish podcast,
[50.00 → 51.78] so I'd encourage you to check it out and subscribe.
[51.90 → 54.92] But in particular, I want to bring to your attention the recent episode
[54.92 → 57.38] featuring Cornelia Davis, the CTO of WeWork's,
[57.38 → 59.40] talking about cloud native, cloud native patterns,
[59.40 → 62.44] and what it really means to be a cloud native application.
[62.80 → 63.44] Here's a sneak peek.
[63.80 → 65.52] Can you define Git Ops?
[65.86 → 69.10] Maybe give a formal definition and talk about what some of the implications are?
[69.36 → 71.92] I think that the simplest formal definition
[71.92 → 75.44] actually doesn't involve the word Git at all.
[75.68 → 79.02] It is cloud native operations is the way that I think of it.
[79.02 → 84.66] Now, let me draw an analog there in that one of the things I didn't mention in my intro
[84.66 → 87.84] is that I'm also the author of a book called Cloud Native Patterns.
[88.20 → 92.52] And that book is targeted at developers, software developers, and architects
[92.52 → 96.90] who are building these highly distributed applications,
[97.10 → 98.76] these microservice-based applications,
[98.76 → 102.76] and helping them understand all the patterns that you have to put in place
[102.76 → 106.58] to be able to make these microservices-based apps work
[106.58 → 109.86] in this ever-changing environment that they run in.
[109.86 → 111.80] All right, links are in the show notes,
[112.02 → 114.74] or head to heroku.com slash podcast to listen and subscribe.
[115.38 → 119.34] Again, check the show notes for links or heroku.com slash podcasts.
[128.76 → 137.74] Let's do it.
[138.40 → 139.38] It's Go Time.
[140.16 → 141.52] Welcome to Go Time,
[141.74 → 144.84] your source for diverse discussions from around the Go community.
[145.40 → 149.80] We record the show live on Tuesdays at 3 p.m. U.S. Eastern.
[149.80 → 153.64] Watch along with your eyeballs at YouTube.com slash changelog
[153.64 → 158.66] and participate in the live chat by joining the Go Time FM channel of Over Slack.
[158.76 → 160.40] Okay, let's cue this one up.
[160.54 → 161.28] See what I did there.
[161.56 → 162.48] Here we go.
[171.22 → 174.16] Hello, and welcome to Go Time.
[174.74 → 179.82] Welcome to a very special Dickensian festive episode today.
[179.82 → 183.56] I'm Ebenezer Raya, and today, dear reader,
[184.22 → 187.50] I, O reader, you're going to be visited by three spirits,
[187.50 → 193.22] the ghosts of configuration past, present, and configuration yet to come.
[194.08 → 199.36] Today, we're talking about Q, which is a new language that lets us define,
[199.62 → 202.40] validate, and generate text-based data,
[203.06 → 207.58] like config files, APIs, database schemas, and even code,
[207.64 → 210.16] which sounds crazy, but don't worry.
[210.16 → 213.28] We're going to unpick it today with this expert panel.
[213.74 → 219.24] We're joined by the creator of Q, a long-time Googler,
[220.28 → 222.58] a founding member of the Borg team,
[223.04 → 225.36] which is what inspired Kubernetes, if you didn't know,
[225.86 → 226.76] a Go team member.
[227.80 → 229.46] It's only Marcel von Loosen.
[229.78 → 230.40] Hello, Marcel.
[230.66 → 230.96] Hey there.
[231.68 → 233.64] Not on the Go team anymore, by the way.
[233.80 → 234.38] I'm sorry.
[234.62 → 234.94] Oh, yeah.
[235.18 → 235.56] That's okay.
[235.56 → 236.64] Did you get fired?
[236.78 → 237.38] Don't answer that.
[237.50 → 237.72] I didn't.
[238.26 → 239.00] It's okay.
[239.54 → 242.34] We're also joined by Paul Jolly.
[242.52 → 244.98] Paul created PlayWithGo.dev.
[245.58 → 251.42] He's a Go contributor and organizer of the Golang Tools Working Group.
[251.72 → 252.08] Hi, Paul.
[252.48 → 252.86] Hi, Matt.
[252.88 → 253.16] How are you?
[253.72 → 254.38] Good, mate.
[254.42 → 254.96] Welcome back.
[255.22 → 256.18] Thank you very much indeed.
[256.72 → 257.64] You're always welcome.
[257.64 → 262.60] We're also joined by Roger Pepe, who's a current influxes,
[262.90 → 265.82] long-time Go contributor, and this blew my mind.
[266.12 → 268.44] Roger suggested the error type.
[268.92 → 270.76] So we're going to have to talk about that at some point.
[272.10 → 276.88] The also organizer of the Golang Northeast meetup since 2015.
[277.76 → 278.24] Hello, Roger.
[278.42 → 279.34] Welcome to Go time.
[279.62 → 280.18] Hey, how's it going?
[280.82 → 281.60] Happy to be here.
[281.62 → 282.06] Yeah, not bad.
[282.62 → 282.92] Yes.
[283.42 → 284.06] Thanks for coming.
[284.06 → 286.42] It's an honour to have you all here,
[286.42 → 288.74] and I'm very excited about Q,
[289.06 → 293.64] especially because it feels to me like something that I haven't really seen before.
[294.44 → 302.66] So maybe, Marcel, you could give us a bit of an overview of what Q is and why it exists.
[302.96 → 307.26] Yeah, so like 15 years ago, as part of being on the Borg team,
[307.32 → 311.28] I created this configuration language because we needed something to control Borg.
[311.84 → 314.88] And I wanted to do something completely different.
[314.88 → 318.40] Originally, but then we wanted to keep it simple,
[318.56 → 322.56] and we created GCL, which in the end grew quite complex.
[323.68 → 327.00] So I did that together with Robert Gruesomer, by the way.
[327.10 → 331.02] So that's also a little pre-Go history there.
[331.74 → 335.60] And then Rob Pike was an advisor on that team also,
[335.60 → 338.70] and he kept saying, like, you have to do composition, right?
[338.70 → 342.94] And what I originally wanted to do was this composition model.
[343.14 → 346.32] But after eliminating that already, we sort of forgot about it.
[346.48 → 349.22] And, you know, the answer was right in our face right there,
[349.28 → 351.40] but we never, you know, never got back to it.
[351.96 → 357.22] And basically, you know, then GCL started having inheritance, big mistake.
[357.64 → 359.58] Didn't have typing, big mistake.
[359.92 → 362.88] And so Q is now a way to fix all that.
[362.88 → 366.78] Great. And what problem does it solve?
[366.86 → 368.46] Like, what's its core mission?
[368.84 → 370.48] I mean, it promises a lot, doesn't it?
[371.12 → 376.54] So the original problem that I wanted to solve with it is basically a configuration, right?
[376.92 → 382.92] So if you look at, so at my previous job, I worked with natural language, right?
[382.96 → 385.14] And basically natural language grammars.
[385.44 → 388.32] And if you think about it, these are very large configurations.
[388.32 → 394.30] So if you see in cloud, right, people that have, like, 100K lines, configurations, or more,
[394.40 → 395.46] it's a struggle, right?
[395.48 → 397.46] And it's really hard to keep these.
[397.96 → 401.24] Whereas if I looked at these grammars, it works fine, right?
[401.28 → 403.86] Like, you had distributed teams, many people working on it.
[404.60 → 405.82] Not a problem, right?
[405.86 → 408.80] I mean, it was daunting, but it was not a problem.
[409.64 → 413.54] And essentially, if you look at it in cloud computing, it's not solved, right?
[413.58 → 416.64] Like, configuration languages tend to be way too complex, right?
[416.64 → 419.18] But it's, and if you keep it simple, it also gets complex.
[419.88 → 422.92] You know, it's always, it feels a little bit out of control, right?
[422.96 → 428.74] And this queue is designed to get control back of configuration and manage it at scale, yet
[428.74 → 429.42] keep it simple.
[430.12 → 430.34] Hmm.
[431.30 → 431.74] Yeah.
[431.86 → 436.96] So I don't know, like, maybe we could just dig into some of the things it does.
[436.96 → 441.52] I mean, are there example use cases that we'll all recognize?
[441.74 → 447.16] Because, like you say, with something that's so flexible like this, that you could almost
[447.16 → 453.02] use it to do all kinds of things that, and I suppose you're going to get a lot of people
[453.02 → 455.84] doing things that you wouldn't even have imagined yourself, right?
[456.12 → 456.26] Yeah.
[456.70 → 456.98] Yeah.
[456.98 → 459.02] One of them is testing, for example.
[459.02 → 459.74] Hmm.
[460.16 → 466.28] So I've written one of my own first queue-based table-driven tests recently, and it's really
[466.28 → 466.74] a breeze.
[466.84 → 468.10] It's so easy to write.
[468.88 → 471.90] And actually, I think Raj was the first who pointed it out.
[472.02 → 473.94] It's a very good use case for queue.
[474.64 → 482.08] And there was recently a blog from Next who was using it also for cross-language test generation.
[483.16 → 486.44] That's an unexpected use case where it really came in handy.
[486.44 → 492.08] I guess, Marcel, one of the good use cases is actually the tutorial that's for Kubernetes
[492.08 → 494.26] that's on the queue website itself.
[494.34 → 496.56] Is it worth you're just chatting through that one?
[496.66 → 501.84] That's a good example of where queue is truly a configuration language.
[502.54 → 502.64] Yeah.
[502.74 → 509.32] So one of the things that that example shows, when I created GCL, I had this other use case
[509.32 → 509.78] in mind, right?
[509.78 → 514.50] Like with these grammars, and there's lots of really deep-going automation you can do if
[514.50 → 516.68] you have a really declarative configuration language.
[517.62 → 520.46] So this was a little bit of promise with GCL as well, right?
[521.56 → 527.28] And because it's also declarative, you do have some automation around it, but the real
[527.28 → 529.30] automation never materialized, right?
[529.32 → 531.48] You see that also with successors of GCL.
[532.00 → 537.44] They also promised the automation also never really materialized, or maybe people didn't
[537.44 → 540.42] know what I meant with you can automate, right?
[540.42 → 546.34] And one of the things in this Kubernetes demos is also where I show like a tiny little bit
[546.34 → 548.32] of what you can do with queue, right?
[548.36 → 551.86] If you have a model like queue in terms of automation.
[552.10 → 559.16] So for example, one of the key things which sets it apart from other configuration languages,
[559.70 → 561.84] so it's type system, right?
[561.86 → 563.98] It doesn't really separate types from values.
[564.08 → 565.22] So values are types.
[565.22 → 569.44] And basically, so you can use queue as a validation language, right?
[569.46 → 574.14] Like you can specify, you know, like constraints or like what do you expect your configuration
[574.14 → 575.10] to look like?
[575.64 → 577.72] And this in itself is already very useful, right?
[577.72 → 582.54] So very often if you try to put structure on something, you start with the validation rules,
[582.62 → 582.78] right?
[582.80 → 587.12] You sort of narrow down like what is it, what I think it means, right?
[587.14 → 588.60] You find errors, right?
[588.60 → 589.58] So this is very different.
[589.76 → 593.30] You don't even focus on emphasizing at first, right?
[593.30 → 598.26] You try to focus the errors like you validate what you have until you get it right, right?
[598.28 → 601.50] Until you get it as many details, as many errors to catch.
[602.38 → 607.00] And then there is a this is the first in a, you know, possible long series of automation.
[607.20 → 609.18] So the first one is called queue trim.
[609.68 → 614.38] It's like once I have this validation, I can say, well, you know, now start rewriting my
[614.38 → 619.16] configurations and eliminate all the fields that I can already derive from my validation,
[620.00 → 620.22] right?
[620.22 → 625.68] So the validation rules that I write is at the same time also the emulating, right?
[625.72 → 627.24] So there is no inheritance in queue.
[627.46 → 629.52] It works very differently, right?
[629.58 → 634.50] But this is a very different way of eliminating boilerplate, if you will.
[634.62 → 634.72] Yeah.
[634.76 → 639.48] So if I had a JSON object then, and I needed this, you know, because of course in JSON,
[639.68 → 641.88] there is no, there aren't really any rules.
[642.00 → 646.18] You can just, I could have a field with any type, you know, it's not constrained.
[646.18 → 650.16] And there is that JSON schema project, and there are a few other projects that aim to sort
[650.16 → 650.82] of address that.
[651.60 → 657.20] But so if I have a JSON object, and it has a particular shape that just has to be, I can
[657.20 → 662.58] use queue to describe that shape and then validate it programmatically.
[662.98 → 663.74] Maybe I could mention.
[663.88 → 667.62] So what, what, one of the things that I tend to do, like one of the really nice uses for
[667.62 → 673.28] queue in a very kind of lightweight way is like, I recently joined Influx, for example.
[674.10 → 675.26] There's lots of configuration.
[676.26 → 681.50] There's, there's lots of configuration around and which you, you're like, oh, I'm unfamiliar
[681.50 → 681.96] with this.
[682.06 → 682.94] I don't know what this is.
[682.98 → 685.40] And there's no documentation or little documentation.
[685.64 → 688.70] And maybe there's some documentation, but it's pretty poor.
[688.80 → 689.74] You don't know what this is.
[689.86 → 694.88] And you could just take that JSON file or that YAML file and just write some queue alongside
[694.88 → 698.68] it and sort of start to refine your idea of what it is.
[698.76 → 700.56] And queue will tell you, oh, no, this is wrong.
[700.72 → 701.26] Oh, okay.
[701.28 → 702.08] I got that rule wrong.
[702.22 → 704.96] And you could just gradually refine it because of the nature.
[705.10 → 709.38] And it's, for me, the syntax is really natural.
[709.84 → 714.58] You're like, if you compare to something like JSON schema, which is, you know, written in,
[714.94 → 720.54] I'm not sure anyone would say that JSON schema is a natural way to specify schema for YAML.
[721.02 → 721.22] Right.
[721.22 → 724.54] But if you write some queue, you can show it to someone that doesn't know queue.
[724.54 → 726.28] And they'll be like, oh, yeah, I understand that.
[726.56 → 730.68] It's kind of like a, like a, all this is a pseudocode, except its real code.
[732.40 → 733.28] So that's nice.
[733.34 → 738.62] Then you talk about being able to build the validation for some JSON, but presumably you
[738.62 → 739.86] can do that at scale as well.
[739.94 → 745.12] So if you've got lots of JSON data, you may be looking at just one document, and you describe
[745.12 → 747.88] a rule, you could run it against all of it.
[747.96 → 750.28] And it will tell you whether they all actually match that.
[750.34 → 753.76] Or if actually in some cases, this is a number and not a string for some reason.
[754.54 → 759.40] If these things have been manually edited, you tend to find places where there are inconsistencies,
[759.60 → 761.64] which people have never realized, you know?
[761.70 → 764.38] So I, you know, you have a big open API spec or something.
[764.46 → 766.08] You're like, okay, I'll write a rule against that.
[766.14 → 768.02] And it's like, oh, here's an inconsistency.
[768.14 → 768.52] Okay.
[768.62 → 768.92] Right.
[768.92 → 770.78] You know, game on.
[771.38 → 771.54] Yeah.
[772.24 → 773.46] Bugger it raised that issue.
[773.46 → 777.50] One of Q's strengths to my mind is that there's Q the language.
[777.92 → 782.56] There's the Q command, much like there is the Go command that complements the Go language
[782.56 → 783.00] as well.
[783.54 → 789.16] And much like Go has got a standard library, Q has a standard library as well, which enables
[789.16 → 791.42] you to write tools in that use Q.
[791.42 → 796.68] And one of the great powers of the Q command itself, which is the sort of the parallel of
[796.68 → 803.78] the Go command and the Q APIs is that you can almost seamlessly translate between these
[803.78 → 807.70] data formats as well, whether it be JSON, YAML, JSON schema.
[807.70 → 814.82] And so this is, again, a strength that I like is that as kind of Roger was saying, you can
[814.82 → 820.02] find yourself in a situation where you're working with some JSON or working with some YAML or working
[820.02 → 824.56] with some proof with just any different formats of either data or schema.
[825.32 → 831.26] And Q enables you to actually translate between those and effectively define conveniently as
[831.26 → 834.06] sort of source of truth for, okay, here is my schema.
[834.20 → 837.42] I want this to be defined in JSON schema, for example.
[837.70 → 840.60] Um, because actually there's a preexisting schema there.
[840.60 → 846.22] So let me work with that, but instead let me, I want to write some extra validation in
[846.22 → 846.90] Q over here.
[847.00 → 849.92] And the ability to combine those things is super powerful.
[849.92 → 854.50] So I end up just doing a lot of hacking using the Q command itself to, as Roger suggested,
[854.82 → 860.06] just validate data, um, in the first instance against various sorts of schema sources.
[860.44 → 860.92] Yeah.
[860.94 → 867.38] One other use case that has gone quite big actually is, uh, so Into, they're using a Q to generate
[867.38 → 870.14] their open API from their protocols, right?
[870.14 → 872.14] So they're reading the protocols converted to Q.
[872.46 → 876.96] And so there are a few reasons why you want to do this extra step from going from proto to
[876.96 → 877.96] Q to open API.
[878.44 → 881.80] So first, the mappings are not that trivial, right?
[881.84 → 885.38] I sometimes get a bug report for queues like, oh, this mapping is really weird.
[885.70 → 886.14] Right.
[886.14 → 889.82] And it's like completely blew up from what proof is to, to open API.
[889.82 → 894.68] But that's actually because, uh, the meaning is slightly different between the two, right?
[894.74 → 896.40] And Q captures that correctly.
[897.04 → 899.94] Um, so sometimes you just do get weird outputs, right?
[899.96 → 901.44] But that's basically because it's correct.
[901.74 → 905.38] The other thing is, uh, so this is where the composability comes in.
[905.68 → 907.86] So proof isn't very expressive, right?
[907.86 → 912.30] You just have basic types and, you know, there are some extensions to protocols where you can
[912.30 → 914.62] have expressions that validate the fields, right?
[914.62 → 919.90] Like very much like Jason schema, but if you want to have like cross type validation or
[919.90 → 921.60] more complicated validation, right?
[921.64 → 923.10] Like it's, it's hard to do.
[923.64 → 929.16] So even if you have such a pipeline, because Q is composable, you can throw in any additional
[929.16 → 932.48] kind of schema on top of it, and it will just combine it in the end result.
[932.90 → 937.64] So unlike we are with inheritance where you have to sort of specify the layering, right?
[937.64 → 940.14] And specify in which order you, uh, you would apply.
[940.92 → 944.48] Um, and we're also the semantics is always a kind of little bit shady.
[944.48 → 944.78] Right?
[944.84 → 948.38] Like, okay, you, you've applied the order, but is that really what you mean?
[948.46 → 948.70] Right.
[948.72 → 952.52] And every different ordering means something different and which one is the correct one.
[952.60 → 955.06] So that issue is completely gone in Q, right?
[955.06 → 958.22] Because there's no, uh, the order doesn't matter basically.
[959.58 → 964.74] Which is amazing for, for a programming language that way you can put things, two things together
[964.74 → 968.02] in either order, any order, you know, it doesn't make a difference.
[968.24 → 971.54] It leads to a real sense of kind of, it feels reliable.
[971.54 → 975.82] It feels like, you know, this says this, and it's true, you know, no one can take this away
[975.82 → 976.26] from it.
[976.76 → 977.20] Yeah.
[977.32 → 981.50] So it's interesting then this idea that it has a standard library because in my head,
[981.60 → 987.02] a validation thing, I mean, regex strings make sense for sure.
[987.26 → 992.84] Uh, even number ranges to say this, this has to be a number between these values, but what
[992.84 → 993.08] else?
[993.08 → 998.52] I mean, if it has a standard library for things like, um, changing strings and modifying
[998.52 → 1001.36] things, what does it look like?
[1001.56 → 1004.04] How do you actually tell it that?
[1004.18 → 1008.26] Well, so I think what Paul was referring to was more the, the libraries that you can, uh,
[1008.26 → 1010.10] use to use Q and other applications.
[1010.60 → 1014.22] So for example, there is a loader very much like in go, right?
[1014.22 → 1020.46] But there's also a workflow package, which allows you to basically have, um, a task graph
[1020.46 → 1023.46] defined in Q, and then it automatically analyzes dependencies.
[1023.46 → 1028.46] And you can use that for data driven, uh, workflow definitions, for example.
[1028.46 → 1033.64] So, so it's, it's, uh, there are kinds of a set of framework packages that you can use
[1033.64 → 1036.80] to build on top of Q and create whatever you want, right?
[1036.82 → 1041.58] In a sort of standardized way, but there is a standard, uh, library, but of course that's
[1041.58 → 1044.42] very constrained by it having to be hermetic, right?
[1044.44 → 1049.22] Like we don't want things to be modified or, but yeah, there, there are useful things
[1049.22 → 1053.04] like you want to be able to operate with time types and, you know, other kinds of things,
[1053.10 → 1056.46] some, some network IP addresses and stuff like that.
[1056.46 → 1060.32] So in a little bit more convenient way than having to code it in Q itself.
[1061.22 → 1066.50] It's just a nice way of being able to sort of more in a more expressive way, describe
[1066.50 → 1072.58] what constraints exist on the data that you're expecting or transforming that data that you
[1072.58 → 1076.92] have received in some way, shape or form, but as Marcel suggested in a hermetic way.
[1077.42 → 1083.66] So there's your regular strings package, for example, bytes package and others that allow
[1083.66 → 1089.70] you to not only manipulate or transform the data, excuse me, but express constraints in
[1089.70 → 1090.98] a slightly more expressive way.
[1090.98 → 1091.02] Yeah.
[1091.62 → 1095.78] So what, for example, you might insist that something is lowercase.
[1096.44 → 1098.48] So that's how, is that a real example?
[1098.80 → 1098.82] For example.
[1099.04 → 1099.18] Yeah.
[1099.50 → 1099.68] Yeah.
[1100.04 → 1100.32] Yeah.
[1100.46 → 1101.24] Ah, I see.
[1101.30 → 1101.70] That makes sense.
[1102.06 → 1102.22] Yeah.
[1102.24 → 1102.54] It's funny.
[1102.62 → 1105.04] I mean, you talk about the strings and the bytes packages and stuff.
[1105.04 → 1107.42] This sounds very like Go.
[1107.74 → 1110.60] Was this project inspired much by Go?
[1110.92 → 1111.22] Yeah.
[1111.30 → 1112.20] For various reasons.
[1112.30 → 1114.32] One of it was a bootstrapping reason, right?
[1114.38 → 1119.34] So the standard library, for example, was just, uh, me analyzing the Go standard library.
[1119.34 → 1120.36] What is hermetic?
[1120.54 → 1122.08] What can I translate directly?
[1122.32 → 1125.62] And then just generate most of it automatically, right?
[1125.64 → 1126.34] That's how that started.
[1126.44 → 1128.40] So it was written in a few hours, basically.
[1129.24 → 1134.64] Uh, of course, then there's a lot of tweaking afterwards, but yeah, I mean, clearly having
[1134.64 → 1137.78] been, I think it's almost 10 years I was on the Go team, right?
[1137.84 → 1142.00] So clearly there's a, uh, Go inspiration, but not, not exclusively, right?
[1142.00 → 1145.04] Like the string model is much more based on Swift, for example.
[1145.52 → 1145.76] Hmm.
[1146.36 → 1147.44] So what's that look like?
[1147.44 → 1149.04] What do you mean it's based on Swift?
[1149.64 → 1153.98] Well, so there are a lot of things where Go wouldn't work well for configuration language,
[1154.10 → 1159.28] like if it comes to, so in configuration, you often have this, this meta thing going
[1159.28 → 1163.52] on with strings where you have to substitute things in strings, but then you have to define
[1163.52 → 1165.88] strings where you have to substitute things in, right?
[1165.90 → 1169.46] So you have to, you have multiple layers of escaping, if you will.
[1169.60 → 1172.74] And, and, and Go doesn't, it just doesn't work very well, right?
[1172.74 → 1173.38] With the back tick.
[1173.38 → 1176.08] Uh, so it's actually a very hard problem.
[1176.08 → 1178.80] And I think Swift is the first language that got that right.
[1179.24 → 1183.88] And so I copied that model into Go and there's some other, you know, string like things that
[1183.88 → 1188.82] they did really well, like multi-line strings, very simple, straightforward way of doing it.
[1188.88 → 1189.48] Very clear.
[1189.66 → 1190.82] Only one way to do it.
[1191.36 → 1191.74] Right.
[1191.74 → 1197.64] So I'm looking at another configuration language here, but Roger knows.
[1198.04 → 1198.18] Yeah.
[1198.18 → 1201.38] It's really a syntactic thing rather than a data model thing, I'd say.
[1201.44 → 1203.78] And like, it contrasts so nicely with YAML.
[1203.92 → 1210.28] It's one of the main reasons why if I'm reading a YAML file, finding it hard to read, I'll convert
[1210.28 → 1214.98] it to Q, and then I can actually read it because there aren't like eight different types of strings
[1214.98 → 1219.14] or with slightly different rules, which YAML, maybe 16, I don't know.
[1219.18 → 1222.92] It's got a ridiculous number of ways of quoting strings and no one knows them.
[1224.78 → 1225.22] Yeah.
[1225.26 → 1229.78] That's definitely that thing of having one way to do something really helps with readability,
[1229.86 → 1230.22] doesn't it?
[1230.26 → 1231.70] Because of course, yeah.
[1231.70 → 1235.80] When you come to look at someone else's Q code, it's familiar already.
[1235.94 → 1237.64] And that's a that's a kind of Go principle.
[1237.64 → 1238.04] Yeah.
[1238.14 → 1239.38] So this is a very good point.
[1239.60 → 1244.02] Like, so for scripting language is not so important, right?
[1244.02 → 1247.76] Like if you write a script, and you do a one-off, you want to do something quickly, like being
[1247.76 → 1250.24] able to write things quickly, right?
[1250.24 → 1253.64] It's more important than being able to read it back later, and hopefully you'll throw it
[1253.64 → 1253.90] away.
[1255.24 → 1258.80] So with a programming language, you don't want that, but with a configuration language,
[1258.80 → 1261.20] these requirements should be even stricter, right?
[1261.20 → 1265.66] Because very often it's not only not somebody else from your team, but it's a different team
[1265.66 → 1267.94] like an SRE that has to look at it.
[1268.02 → 1271.20] And often in their not so good circumstances, right?
[1271.20 → 1273.24] Where there's some emergency where you have to fix things.
[1273.92 → 1279.00] So readability is even more important, and it's even more important to have no complexity,
[1279.22 → 1279.34] right?
[1279.34 → 1280.18] Or less complexity.
[1280.54 → 1283.94] And this is exactly what is the problem with, for example, GCL, right?
[1283.96 → 1287.42] Like guilty myself and many of the other configuration languages, right?
[1287.48 → 1289.64] They, you kind of need the complexity.
[1289.88 → 1294.96] That's why you go to a TSL in the first place, but then they, you know, you do want to readability.
[1294.96 → 1298.54] So you shouldn't have these complex constructs, right?
[1298.62 → 1301.64] Like that's, they really, it goes too far, right?
[1301.64 → 1303.36] And it really hurts readability too much.
[1304.12 → 1311.60] One other thing I'd kind of mention related to its relation, its connection with Go is
[1311.60 → 1315.44] that it does really well is, is that you've got Fund in the same way that you've got
[1315.44 → 1315.96] Go Fund.
[1316.08 → 1316.68] I was going to ask that.
[1316.80 → 1321.04] And that's something that, that, that, you know, like something like YAML, basically you
[1321.04 → 1321.82] can't do, right?
[1321.84 → 1325.52] You can't read it in, process it like an AST and write it out again.
[1325.52 → 1327.92] Because basically almost no one does that.
[1327.92 → 1332.16] So that means it's amenable to tool in the same way that Go is amenable to tooling.
[1332.28 → 1333.66] And that's a huge deal, I think.
[1334.28 → 1338.98] So for anyone not familiar, and there probably aren't many of our listeners slash watchers
[1338.98 → 1344.18] that aren't familiar with Go Fund, what, what does that do then for the Q code?
[1344.18 → 1350.66] So it means that you can, for example, if the language evolves, and we want to change
[1350.66 → 1355.06] things in a backwardly compatible way, we can do that by reading in the code and automatically
[1355.06 → 1355.94] transforming it.
[1356.18 → 1360.68] And like Marcel has been fantastic, like in the early days of the Go project, like I've
[1360.68 → 1363.12] been involved in Go since basically day one.
[1363.50 → 1366.56] And in the early days, the language was changing quite fast.
[1366.76 → 1372.78] But people kept on continuing to use the language because the core team was very good about
[1372.78 → 1377.06] maintaining backward compatibility, or rather, when they didn't maintain backward compatibility,
[1377.64 → 1382.74] they introduced a tool called Go Fix, which would actually automatically change your Go
[1382.74 → 1384.88] programs to use the new features.
[1385.48 → 1388.54] And that was the huge deal and still is actually for Go.
[1388.90 → 1393.70] So and I think that that's, that's a huge deal for, for Q and for configuration languages,
[1393.80 → 1395.38] because it's not just the language itself.
[1395.78 → 1401.28] It's if you change your configuration language yourself, you want to transform it, well, then
[1401.28 → 1401.92] you can do that.
[1401.98 → 1405.80] And you can still keep comments, for example, comments are really, really important.
[1405.98 → 1406.58] They're crucial.
[1407.06 → 1411.02] But you know if you've got JSON, for example, you can't have comments.
[1411.02 → 1414.50] If you've got YAML, well, if you transform your data, you lose the comments.
[1415.40 → 1423.22] But having the sort of like the Go Fund equivalent, one formatting style is critical from a readability
[1423.22 → 1424.10] perspective as well.
[1424.20 → 1430.14] So that's really the principal purpose, to my mind, at least of Fund is the formatting side
[1430.14 → 1430.48] of things.
[1430.48 → 1436.20] I think Roger's just described the where Fund goes to sort of like another level, providing
[1436.20 → 1442.42] this additional translation, or we've deprecated this feature in the next version.
[1442.68 → 1445.34] So it will automatically rewrite your Q.
[1445.90 → 1451.20] And that has, I think Marcel would agree, that has been one of the strongest bits of feedback
[1451.20 → 1456.36] that people have given is that there have been breaking changes because Q is not at V1 yet.
[1456.36 → 1462.90] And so in order to help people along that path, Fund has been a lifesaver.
[1463.02 → 1468.20] You just literally run it like you would Go Fund across a number of files or directories or packages,
[1468.20 → 1469.46] as the case may be.
[1469.86 → 1475.16] And you end up having migrated, for want of a better phrase, to the new version of Q with
[1475.16 → 1476.16] zero pain.
[1476.86 → 1477.70] Yeah, it's funny.
[1477.70 → 1485.74] I heard somebody talking about Go Fund and their view of it was, it's just a kind of nice feature to have,
[1485.82 → 1488.92] almost like you have a format document in an IDE or something.
[1489.32 → 1490.74] But it is different to that.
[1491.04 → 1492.60] It's the readability thing, isn't it?
[1492.66 → 1498.08] Again, everyone having the same layout and taking out any of that discussion around white space
[1498.08 → 1500.20] or where do we put braces or whatever.
[1500.20 → 1507.38] And the stuff that Roger was talking about, the fix, that sort of retrospective, you're almost like,
[1507.90 → 1510.34] again, sounds just like a nice to have.
[1510.50 → 1513.56] But that's really how you build trust, isn't it?
[1513.74 → 1517.68] Like, and if you could, that's the thing about Go, I think, that made it so successful
[1517.68 → 1522.24] was you could kind of rely on it, especially once it hit version one.
[1522.42 → 1526.84] You could really rely on that so that you knew your code was pretty safe.
[1526.84 → 1531.24] They're not going to just keep releasing new major versions, and you have to go back and rewrite
[1531.24 → 1534.02] things, or you get stuck on a previous version.
[1534.42 → 1539.38] So yeah, I think that turns out to be way more important, really, than people might realize.
[1540.24 → 1545.72] So Q, the language itself being amenable to tooling, i.e. writing tools that can work with
[1545.72 → 1551.24] Q, the language, is, again, critical for all the reasons that you just described.
[1551.74 → 1556.74] And it's kind of one of the main reasons that I really like Q is that I can imagine myself
[1556.74 → 1563.36] writing tools that work with Q in the same way that I write tools that work with Go,
[1563.44 → 1564.32] the language as well.
[1564.80 → 1569.50] And just to pick up on your point, Matt, about how powerful this can get, I think
[1569.50 → 1575.30] Russ Cox has actually just written a new refactoring tool for the Go language itself,
[1575.30 → 1580.98] which is kind of like taking Go to the next level of where people are making API changes,
[1580.98 → 1586.02] for example, and they need to help people migrate because they've made a breaking change or somewhat,
[1586.72 → 1590.92] for example, then that's the kind of thing that you want to be doing with Go.
[1591.06 → 1594.52] And that's absolutely the kind of thing that we want to be doing with Q as well.
[1594.60 → 1599.26] And that's, as Roger described, what Exempt has been fantastic with since day one.
[1599.26 → 1602.80] Yeah, and basically automation, that was also a big motivator.
[1603.08 → 1607.42] So in a larger setting, like a lot of the code and also configuration, right,
[1607.42 → 1610.70] it's very often generated or machine manipulated.
[1611.00 → 1613.14] It's just a part of life, right?
[1613.16 → 1617.80] So this is, it's not only a nice to have, I would say it's critical, right, to have these features.
[1617.80 → 1635.00] This episode is brought to you by our friends at Equinix Metal,
[1635.28 → 1638.04] globally interconnected, fully automated bare metal.
[1638.36 → 1643.04] Equinix Metal gives you hardware at your fingertips with physical infrastructure at software speed.
[1643.42 → 1645.82] Accelerate your workloads with fully automated bare metal,
[1645.82 → 1648.44] that's secure, powerful, and cost-effective.
[1648.96 → 1652.06] This is the promise of the cloud delivered on bare metal.
[1652.44 → 1656.98] Equinix Metal makes it easier than ever to take advantage of the unmatched global reach
[1656.98 → 1659.78] and connectivity ecosystem made possible by Equinix,
[1659.92 → 1665.04] which includes more than 220 data centres across 63 metros, making interconnection easy.
[1665.36 → 1668.32] And they're obsessed with making bare metal even more awesome.
[1668.66 → 1669.94] Seriously, check out these features.
[1670.42 → 1675.54] 60 Second deploys, hourly pricing, a customer success team that engages over Slack,
[1675.54 → 1681.64] x86, Intel, AMD, and ARM, single tenant, NVMe and SSD storage,
[1682.00 → 1686.86] RESTful API, first-class DevOps integrations, Equinix fabric integration,
[1687.32 → 1690.16] support for enterprise OSes and open-source Linux OSes,
[1690.94 → 1695.00] air-gapped installs without a public IP, no installed agent or keys,
[1695.36 → 1698.78] extensive open-source love and support, plus so much more.
[1698.78 → 1703.90] Visit info.equinixmetal.com slash changelog, get $500 in free credit to play with,
[1704.12 → 1705.42] plus a rad t-shirt.
[1705.74 → 1708.76] Again, info.equinixmetal.com slash changelog.
[1708.76 → 1738.70] Roger, I do have to ask you very quickly about you suggesting,
[1738.70 → 1740.54] the error type in Go.
[1741.04 → 1741.70] What's that about?
[1741.80 → 1743.32] Because it used to be OS error, didn't it?
[1743.34 → 1744.00] It was restrict.
[1744.34 → 1744.86] That's right.
[1744.92 → 1745.94] It used to be OS.error.
[1746.08 → 1750.98] And of course, like importing the OS package, you know, with all its baggage,
[1750.98 → 1754.74] every time you wanted an error, it's just not great.
[1755.12 → 1759.82] So there was a discussion, and they were thinking about different options.
[1760.00 → 1763.34] And there was quite a long thread in the Golang Nuts mailing list.
[1763.86 → 1768.90] They'd actually decided that what they were going to do, they were going to make a new package,
[1769.12 → 1771.24] perhaps called errors, and it would be an error type.
[1771.30 → 1773.86] And every time you wanted the error type, you would import that package.
[1774.18 → 1775.82] And I was like, no, no.
[1776.52 → 1777.78] That just doesn't seem right.
[1777.84 → 1779.26] It's such a low-level part.
[1779.46 → 1781.60] You shouldn't have to import something every time.
[1781.60 → 1788.98] And I just made a little suggestion in the thread saying, look, how about just predefining the error as an interface?
[1789.46 → 1797.76] In fact, at the time, I suggested it as, because at the time, the error, the standard, the OS.error had a string method, not an error method.
[1798.10 → 1798.18] Right.
[1798.18 → 1802.78] So I suggested that it would be type error with a string.
[1803.46 → 1804.76] And they changed that.
[1805.02 → 1807.00] But basically, that was my suggestion.
[1807.28 → 1810.38] And it's funny how a little thing, I probably didn't think about it very long.
[1810.84 → 1817.16] But that, you know, and actually, that was one of the really fantastic demonstrations of Go Fund and Go Fix,
[1817.16 → 1825.90] because there were hundreds of thousands of lines of Go in the wild that was using OS.error, you know, importing OS, whether it needed or not.
[1826.08 → 1829.60] And you could just run Go Fix, and it would just change it just like that.
[1829.88 → 1831.88] And it was like a kind of magic.
[1832.52 → 1834.04] That's a great discovery.
[1834.24 → 1836.08] It feels like that's a discovery, doesn't it?
[1836.22 → 1843.18] That rather than just a choice you could make, because interfaces in Go, because they're duct-typed or structural typing,
[1843.18 → 1847.88] then you don't need to import anything to work with errors.
[1848.10 → 1848.94] So that's brilliant, mate.
[1849.04 → 1851.74] So thanks for that, because that's really helped us out.
[1853.24 → 1860.36] There was a little bit of a discussion earlier today on Twitter, which is a website with a microblogging website.
[1861.12 → 1865.50] And it was Jana Dozen and Carmen And.
[1865.98 → 1871.80] And they were kind of discussing whether you say Slang or Q.
[1871.80 → 1874.02] I'm getting the sense that we say Q.
[1874.22 → 1875.46] So what are the rules?
[1875.60 → 1877.72] When do we use Slang?
[1878.12 → 1880.52] And could you describe this in Q?
[1882.72 → 1883.98] I don't think so.
[1884.10 → 1885.80] It's not Turing complete, for one.
[1887.94 → 1891.48] So I think it's very similar to Go, right?
[1891.50 → 1897.14] It's really Q, but if I search for it, I search Slang, because I just get better results.
[1897.70 → 1898.80] So there you go.
[1899.12 → 1899.44] Okay.
[1899.44 → 1900.38] No pun intended.
[1901.80 → 1902.50] That's great.
[1903.16 → 1910.16] So, Marcel, something you mentioned earlier, which is baffling me still, you said values are types.
[1910.66 → 1910.84] Yeah.
[1910.96 → 1915.10] So could you elaborate a little bit on what that means and the implications of it?
[1915.88 → 1916.32] Yes.
[1916.56 → 1921.00] So if you look at Q, I try to visualize it now with my words, I guess.
[1921.00 → 1928.84] So if you look at JSON, you just have this string for the field colon value, which can be a string integer or another object.
[1929.16 → 1931.02] So in Q, it looks very similar.
[1931.18 → 1935.38] You can drop the quotes here and there, not on the right-hand side, but on the left-hand side of the colon.
[1935.38 → 1941.30] And then on the right, instead of saying, for example, a string, you can say it is a string, right?
[1941.36 → 1944.52] So you can say instead of the value, you can specify it's a type.
[1944.52 → 1948.00] And syntactically, it looks the same, right?
[1948.00 → 1950.48] But it's not only syntactic, it's also semantic.
[1950.88 → 1952.28] Everything is ordered in a hierarchy.
[1952.56 → 1958.54] So a concrete string, like mat, is an instance of the type string, right?
[1958.56 → 1961.22] But they're ordered in the same hierarchy.
[1961.22 → 1965.06] So I can say it must be greater or equal than M, right?
[1965.16 → 1967.56] Which then mat is an instance of that too.
[1967.66 → 1969.40] So you have constraints, and they're all ordered.
[1970.04 → 1975.54] And you can carry that forward and basically say all configurations are ordered like that, right?
[1975.66 → 1977.70] So you can define an ordering for all of them.
[1978.56 → 1982.34] And more specifically for the mathematically inclined, it's a lattice.
[1982.34 → 1993.64] So that means that for every two values or configurations, if you combine them, there's always a unique instance that's the greatest instance of both of them.
[1993.90 → 1996.08] So that's where commutativity comes from, right?
[1996.42 → 1998.56] So that basically means you can combine in any order.
[1999.06 → 2004.84] It's a mathematical construct, basically, in which all these values and types are defined.
[2004.92 → 2006.02] So it sounds a little bit complicated.
[2006.16 → 2007.08] It's really very simple.
[2007.18 → 2011.34] And one way to view Q, for example, is if you have two forms, right?
[2011.34 → 2016.54] Like you can see Q as a form, like data as a form, if you will.
[2016.64 → 2017.86] And there are gaps in there.
[2018.16 → 2020.38] So you might still have to fill out some fields.
[2020.50 → 2022.04] Some of them might already be filled out.
[2022.62 → 2028.30] And let's say like two people have partially filled out a form, and you now want to combine it.
[2028.40 → 2029.96] But it's a form about the same person.
[2030.36 → 2031.82] One person filled out the address.
[2031.96 → 2034.56] The other person filled out the dependents or whatever.
[2035.54 → 2038.44] Now you're combining this form, but you're giving it to a third person.
[2038.44 → 2042.90] And it's just a matter of filling out wherever the gaps were left by the other.
[2043.38 → 2047.30] But now you see that the last name is different, for example, in both forms.
[2047.94 → 2049.88] Now, you know it's about the same person.
[2049.88 → 2052.26] So one of them must be wrong, right?
[2053.86 → 2059.14] So what you do at inheritance, you say like, well, we'll pick the last one and that will be the name, right?
[2059.14 → 2063.04] What Q will say is like, well, no, like one of them is wrong.
[2063.10 → 2067.02] There's no way for me to tell just based on this form which one is wrong, right?
[2067.04 → 2068.24] So I'm going to bill here.
[2068.30 → 2069.42] You're going to fix this, right?
[2069.44 → 2071.74] You're going to tell me what's the right name, right?
[2071.80 → 2075.08] And this is basically how Q operates.
[2075.08 → 2077.22] And this is because you have this restriction.
[2077.22 → 2080.22] I can actually order everything nicely.
[2080.98 → 2083.16] And that's what it means that types are values.
[2083.24 → 2084.26] Does that make any sense?
[2084.86 → 2086.42] Yeah, it does make some sense.
[2087.04 → 2091.44] There's a perfect tutorial on the Q website, which is Qlang.org.
[2091.54 → 2094.08] And that's C-U-E-Lang.org.
[2094.28 → 2101.28] That walk through the basics of Q that introduced this concept of types being values really well.
[2101.28 → 2109.72] And they also show and explain how the syntax is very JSON-like, which is unsurprising because it's a superset of JSON.
[2110.32 → 2121.22] And so that will help people orient themselves around how the schema part of Q, if you like, fits in with the JSON, with the data part,
[2121.38 → 2126.64] and how the two of them combine, Matt, as you were saying earlier on, in the way that JSON doesn't,
[2126.64 → 2131.78] where you've got JSON schema being a different thing altogether, really, to JSON the data itself.
[2132.20 → 2140.88] In Q, you've got this concept of the schema, for want of a better word, and the data sitting alongside each other in the same file, potentially,
[2141.54 → 2150.76] where the data, as Marcel was saying, is effectively just a more specific and concrete version of a field than the schema,
[2150.88 → 2152.72] which could just be the type, for example.
[2153.88 → 2156.34] So that is quite strange, isn't it?
[2156.34 → 2158.82] Is that a new concept?
[2158.98 → 2161.68] Are there other examples of things that behave like that?
[2162.56 → 2165.48] Well, so really, this comes from logic programming.
[2166.28 → 2173.02] So if you really think about, like, data log, prologue, you really have this, you know,
[2173.06 → 2176.80] it's all about reasoning with insufficient or partial data, right,
[2176.82 → 2180.32] where you have gaps that you try to fill in by trying to walk over this.
[2180.32 → 2187.36] So in natural language processing, this Q-like thing, right, so it works very much the same as that.
[2187.42 → 2189.98] You also have this, that is this organization.
[2190.76 → 2199.12] And it was basically invented because it was, so prologue didn't really scale to address dealing with grammars, right?
[2199.12 → 2206.02] Like, not because it couldn't, but because it was too hard to understand and, like, order sort of still did kind of matter, right?
[2206.04 → 2207.42] And it was like complicated rules.
[2208.08 → 2213.86] And this was basically a pure data way of describing what needed to be matched, right?
[2213.86 → 2214.84] What needed to be matched.
[2214.84 → 2218.64] So you don't really have integers and strings, right?
[2218.66 → 2220.96] It was more abstract in a way than that.
[2221.02 → 2226.00] But you did have this idea that the structure is at the same time the type, right?
[2226.06 → 2230.58] So it really comes from there that you have, that it's the same thing.
[2231.22 → 2235.52] Do people get that intuitively or does that take some learning?
[2235.96 → 2238.22] I think for computer scientists might take some learning.
[2238.22 → 2242.96] I think for a normal person, let's say, it's easier, actually.
[2242.96 → 2246.66] So one way to think about it, if you think about inheritance, right?
[2246.72 → 2249.18] You have, for example, a cat.
[2249.86 → 2251.94] And now I want to make it a dog, right?
[2251.96 → 2255.66] I say, like, well, okay, so I'm going to take the nose and make it wet.
[2255.74 → 2257.56] And it doesn't meow, but it barks, right?
[2257.56 → 2261.76] But I'm going to modify this cat and create a subclass that's a dog, right?
[2262.36 → 2266.08] So to a computer scientist, it's a completely normal thing to do, right?
[2266.08 → 2267.84] And nobody would even blink at it.
[2268.14 → 2270.74] To a normal person, this is insane, right?
[2270.76 → 2272.92] Like you say, like, well, you don't organize it like this.
[2272.96 → 2274.04] You have an animal, right?
[2274.04 → 2274.54] Or a mammal.
[2274.70 → 2275.36] And then you create a...
[2275.36 → 2278.02] No, but that's because they think you're really going to do this in the lab.
[2278.64 → 2278.84] Yeah.
[2278.98 → 2279.22] That's why.
[2279.60 → 2279.72] Yeah.
[2279.78 → 2280.24] That's why.
[2280.68 → 2280.90] Yeah.
[2281.20 → 2282.44] And this is like this, right?
[2282.48 → 2286.82] Like the way, I would say, actually, the way inheritance, with inheritance, you can organize
[2286.82 → 2289.58] things is very unnatural often, right?
[2289.58 → 2295.04] And so Q still has a hierarchy, but it's a hierarchy like normal people think about it, right?
[2295.34 → 2295.78] Basically.
[2295.78 → 2303.86] It definitely took me some time to wrap my head around the way in which you need to sort
[2303.86 → 2305.36] of think in Q.
[2305.64 → 2311.68] But I think one of the things is that I found is that once I sort of started getting, if
[2311.68 → 2316.38] you like, the concepts involved with Q and how to think in that slightly different way,
[2316.80 → 2321.44] as Marcel was saying, it actually just becomes a much more natural way to express, okay, this
[2321.44 → 2326.28] is the structure of the data that I'm expecting here, or these are the constraints on it.
[2326.28 → 2333.18] And then the tooling that you have with Q as well, just it ends up becoming, for me, it's
[2333.18 → 2335.72] a critical part of my workflow using Q now.
[2336.06 → 2340.14] Whatever project I'm working on, it's not that I'm trying to use Q, I just find myself
[2340.14 → 2345.38] naturally using it because it's a very natural way of describing data or constraining data.
[2345.88 → 2347.60] That's a very good sign, isn't it?
[2347.68 → 2352.22] When you actually just use it because it's working for you, you're not using it for the
[2352.22 → 2352.78] sake of it.
[2352.78 → 2357.82] I often end up just using it as like pseudocode almost, you know, I'm like, oh, what is this
[2357.82 → 2358.02] thing?
[2358.12 → 2362.38] Oh, I'll just write it out as Q because it just feels totally natural.
[2362.38 → 2364.46] And it doesn't feel like it gets in the way at all.
[2364.52 → 2365.46] It just enables.
[2367.08 → 2367.74] That's great.
[2368.18 → 2372.22] We mentioned earlier that you can drop the quotes in the keys or in the field names or
[2372.22 → 2372.92] something.
[2373.20 → 2376.08] But so what happens if you Q-thumped that?
[2376.42 → 2379.56] What's Q-thumped's opinion on quotes and things?
[2379.82 → 2380.26] That's fine.
[2380.26 → 2386.20] So labels are, because it's more restricted, so left of the colon, if you're doing a member
[2386.20 → 2391.54] name or whatever, it's just because it's so annoying to write the quotes there.
[2391.64 → 2396.50] It's just this little, you know, syntactic trick so that I don't need the quotes there.
[2396.66 → 2401.22] Except it's actually different in Q because if you don't put the quotes around the keys,
[2401.36 → 2402.42] it's actually an identifier.
[2402.86 → 2405.02] You can actually refer to it as a variable.
[2405.02 → 2411.12] And this is like a, you know, so you can say, you know, X colon five and without the quotes
[2411.12 → 2417.22] around the X and just like Jason, except later you can say Y colon X, and then they're both X and
[2417.22 → 2419.52] Y are going to be exactly the same value always.
[2420.00 → 2422.10] So that's, that, that's the difference.
[2423.16 → 2429.64] That kind of reminds me of symbols in Ruby because you could build maps with symbols and strings as
[2429.64 → 2430.94] keys in Ruby.
[2431.70 → 2436.38] While you think about that, Matt, I'll just say that I think that's the two things that
[2436.38 → 2438.54] you talked about there, the dropping of the quotes.
[2438.94 → 2443.10] And as Roger was saying, this ability to reference different values.
[2443.64 → 2443.74] Yeah.
[2443.90 → 2447.70] This is again, one of the things from, as a user of Q, i.e.
[2447.70 → 2452.10] somebody who's writing Q, one of the things that I really appreciate.
[2452.10 → 2457.24] Because you've got the tool authors and the system authors who are going to use Q because
[2457.24 → 2460.76] they want people to provide Q to configure their system or as input.
[2461.10 → 2466.90] But as a user of Q, someone who's writing Q, there are so many of these just amazing things
[2466.90 → 2468.80] that I have as part of the language.
[2469.02 → 2475.06] So Marcel was talking about string literals and the way they work, string interpolation,
[2475.44 → 2481.28] the ability to drop quotes, comments, this ability to do references, for example.
[2481.28 → 2486.84] The Q for all of these things as a user of Q, they're just the things that I've become
[2486.84 → 2489.10] so used to in things like Go.
[2489.34 → 2492.40] I kind of need these things in my configuration language.
[2492.86 → 2497.36] And that's where Q from a user perspective is so much more powerful, I think, than things
[2497.36 → 2498.40] like JSON and YAML.
[2498.56 → 2501.98] Not to replace them, but just as a complement often to those things.
[2502.32 → 2504.28] I sometimes need that flexibility.
[2504.28 → 2507.92] So I'll write it in Q, and then I'll export it to YAML, for example.
[2507.92 → 2508.36] Hmm.
[2509.56 → 2513.42] So the Q tools themselves then, what are they written in?
[2513.56 → 2514.20] Go, mostly.
[2514.88 → 2515.06] Hmm.
[2515.30 → 2516.68] And will that always be the case?
[2517.62 → 2522.68] Well, it's kind of a lot of work to, you know, like write all these tools again in something
[2522.68 → 2523.38] else, right?
[2523.38 → 2529.30] So I can imagine that at least the core language would be either cross-compiled or potentially
[2529.30 → 2530.42] even rewritten, right?
[2530.42 → 2532.18] In another language.
[2533.26 → 2536.26] But to rewrite the tools is...
[2536.26 → 2538.38] So especially if you're like with Go, right?
[2538.42 → 2542.44] Like all the loading and like the modules, all of this is very finicky, right?
[2542.50 → 2546.14] Like it's one thing to have a language specification.
[2546.14 → 2550.78] But the surrounding tooling is quite tedious to rewrite.
[2551.86 → 2556.66] I have to say, I would hope that the core language was ported to other...
[2556.66 → 2561.06] The core Q language was ported to other languages because I think that it would make a lot of
[2561.06 → 2565.18] sense, for example, to be able to use it on the browser, you know, the client-side browser,
[2565.32 → 2565.86] for example.
[2565.86 → 2572.20] Or from other languages, because I think it can add a lot as something as part of some
[2572.20 → 2576.20] running system, as well as used as a tool.
[2576.52 → 2583.24] There is an initial version of the Q Playground that needs to be updated to the latest alpha
[2583.24 → 2586.86] version, which is sort of now the kind of like the latest version.
[2587.44 → 2594.48] That Q Playground is compiled to WebAssembly in much the same way that some of the Go Playgrounds
[2594.48 → 2594.76] are.
[2594.76 → 2600.50] The actual Go Playground itself has got a real back end to it, but some of the Go Playgrounds
[2600.50 → 2606.54] are compiled to WebAssembly and there is a Q version of that, which at least demonstrates
[2606.54 → 2613.40] for now, not in the most efficient way, that you can have browser-based interpretation of
[2613.40 → 2617.16] Q, as well as exporting to YAML, JSON, etc.
[2618.16 → 2620.64] Yeah, the real value is in its design, isn't it?
[2620.70 → 2622.18] So it almost doesn't really matter.
[2622.18 → 2626.44] But yeah, of course, this is a Go podcast, and we all love to Go as well.
[2626.54 → 2627.92] So that makes sense.
[2627.92 → 2641.06] How often do you think about internal tooling?
[2641.40 → 2645.94] I'm talking about the back office apps, the tool the customer service team uses to access
[2645.94 → 2651.68] your databases, the S3 uploader you built last year for the marketing team, that quick Firebase
[2651.68 → 2657.08] admin panel that lets you monitor key KPIs, and maybe even the tool that your data science
[2657.08 → 2660.44] team had together so they can provide custom ad spend insights.
[2660.80 → 2663.98] Literally every line of business relies upon internal tooling.
[2663.98 → 2669.66] But if I'm being honest, I don't know many engineers out there who enjoy building internal tools, let
[2669.66 → 2672.88] alone getting them excited about maintaining or even supporting them.
[2673.34 → 2675.42] And this is where Retool comes in.
[2675.84 → 2681.82] Companies like DoorDash, Bred, Plaid, and even Amazon, they use Retool to build internal tooling
[2681.82 → 2682.76] superfast.
[2683.14 → 2687.66] Retool gives you a point, click, drag and drop interface that makes it super simple to build
[2687.66 → 2690.66] these types of interfaces in hours, not days.
[2690.66 → 2696.32] Retool connects to any database or API, for example, to pull data from Postgres, just write
[2696.32 → 2699.80] a SQL query and drag and drop a table onto the canvas.
[2700.34 → 2705.14] And if you want to search across those fields, add a search input bar and update your query,
[2705.56 → 2706.74] save it, share it.
[2706.88 → 2707.70] It's too easy.
[2708.08 → 2711.34] Learn more and try it free at retool.com slash changelog.
[2711.46 → 2714.36] Again, retool.com slash changelog.
[2720.66 → 2741.76] When do we think Q will be version one?
[2741.76 → 2745.90] And, you know, is there, are there big gaps?
[2746.06 → 2750.64] Are there still big kind of philosophical or conceptual problems to solve?
[2750.82 → 2756.28] When it comes to narrowing down the language, it's really talking about details right now,
[2756.40 → 2757.92] like really fine details, right?
[2757.94 → 2763.80] So I don't think, so there's a change probably coming up in the number model where we're going
[2763.80 → 2769.12] to say an integer is a subclass of a general number, whereas now there's a distinction between
[2769.12 → 2773.68] float and integer, and that doesn't always work out quite well.
[2774.24 → 2779.84] So the end result will be somewhere smack in the middle of go into versus floats and go
[2779.84 → 2781.30] constants, let's say.
[2781.90 → 2787.32] You will hardly know the difference because people, there is already a number type, right?
[2787.38 → 2790.38] Predeclared identifier, which people typically use.
[2790.50 → 2791.26] Float is discouraged.
[2791.38 → 2795.24] And if you use those, there's really, you won't know the difference between these two models.
[2795.24 → 2801.20] But, you know, it's a little bit, if you use the standard library, you might get some,
[2801.66 → 2802.88] will be a little bit more convenient.
[2803.58 → 2805.24] So there are some changes there.
[2805.48 → 2808.82] Can I be the first to suggest the error type, please?
[2809.00 → 2811.40] Well, there is, it's critical to any lettuce.
[2811.54 → 2812.90] So there is an error type.
[2813.04 → 2817.78] Although right now, people have said that the way it's written right now, it's a symbol,
[2817.88 → 2819.78] and it looks kind of offensive to some people.
[2819.92 → 2824.74] So we're probably going to change it to a pre-declared identifier named error.
[2824.74 → 2826.12] Is it the poop emoji?
[2826.26 → 2827.46] It is not the poop emoji.
[2829.08 → 2830.06] Okay, well, that's it.
[2830.12 → 2830.32] There you go.
[2830.36 → 2832.98] Maybe I could suggest the poop emoji for error type.
[2833.34 → 2833.50] Yeah.
[2833.90 → 2835.40] I can be the Roger Pepe of Q.
[2835.66 → 2835.90] Yeah.
[2836.00 → 2836.50] It's this.
[2836.66 → 2842.66] And, but yeah, so there are some, so performance is not great yet.
[2842.66 → 2843.84] And this is partly deliberate.
[2843.92 → 2846.58] It's been designed to be order N, right?
[2846.64 → 2847.24] Like O-N.
[2848.36 → 2851.04] But it's definitely not been implemented this way.
[2851.14 → 2853.44] So that's something that needs to be done.
[2853.44 → 2857.84] And basically the idea was to try out, it's written so that I can try out a lot of things
[2857.84 → 2858.32] fast.
[2859.12 → 2865.18] So deliberately, sometimes I added, you know, made it easier and made it slower essentially.
[2865.38 → 2868.08] But that would be one of the big next things to do.
[2868.08 → 2876.18] And yeah, so it's, you know, the errors messages should, they have become better already this
[2876.18 → 2879.08] last iteration, but they need to become a lot better.
[2879.28 → 2884.04] And there are some probably also a different model where an error message is not just a
[2884.04 → 2888.64] message, but really contains like a lot of context of where the error occurred so that
[2888.64 → 2892.72] you can do further analysis on it, which is important for configuration language.
[2892.72 → 2894.08] So these are there.
[2894.18 → 2895.16] Oh, it's really cool.
[2895.88 → 2898.22] Modules might be worth mentioning as well.
[2898.48 → 2904.52] Yeah, that's not so much standing in the way for 1.0 of the language, but we are, you
[2904.52 → 2911.26] know, wanted to adopt the MVS, right, of Go, which is actually perfect for dealing with
[2911.26 → 2912.96] configuration hermetically, right?
[2912.96 → 2917.78] So Go has this, sorry, Q has this concept of a module very similar to Go.
[2918.42 → 2921.84] So for example, this is for Go users, this might be interesting to know.
[2921.92 → 2924.10] So there's this thing called Get.
[2924.48 → 2931.44] So you can point to any Go package, and it will then look at the Go types of this package
[2931.44 → 2936.58] and create Q definitions for it, which you then can use in your Q code, right?
[2936.62 → 2940.36] So you don't have to like manually rewrite Go to...
[2940.36 → 2943.80] Well, it would also be a great way to learn Q, I guess, if you're familiar with Go, you
[2943.80 → 2946.04] could do that, and that'd be a great way to learn.
[2946.06 → 2947.52] It's quite straightforward to do, actually.
[2947.58 → 2948.86] It works with Kubernetes as well.
[2948.92 → 2953.38] So you can just take the whole Kubernetes code base, extract all the types, and so you
[2953.38 → 2956.42] immediately have a typed Kubernetes thing, right?
[2957.34 → 2963.68] So another thing, so in the Berlin Gopher Con, I gave a talk there, I gave a little bit of
[2963.68 → 2967.86] a demo there were, and it's just still in my client, but just to show you what's possible.
[2967.86 → 2974.10] So there I go basically from a Go binary or Go code, basically, directly, just Go code,
[2974.50 → 2976.46] directly to an open API specification.
[2977.22 → 2984.20] So basically what it does, I use Get to get the Go types, and then I separately, I use
[2984.20 → 2991.22] SSA to analyze the Go code, identify the validation code, and extract the constraints that these
[2991.22 → 2991.82] represent.
[2991.82 → 2998.30] And this is some barfed out Q that looks hideous, but I can then run Q definition,
[2998.52 → 3006.28] Q def, to combine the nicely documented simple structs I just extracted before with this barfed
[3006.28 → 3012.86] out Q, and it spits out a very nicely documented open API definition without any further human
[3012.86 → 3013.20] input.
[3013.20 → 3017.86] So this is the kind of things you could do with automation.
[3019.02 → 3020.08] Yeah, it's really cool.
[3020.24 → 3021.48] This is really exciting.
[3021.60 → 3026.10] It feels like I think everyone's going to sort of just go and start playing now with this,
[3026.24 → 3030.58] because it really, like, the possibilities seem, and, you know, the fact that it's solving
[3030.58 → 3034.44] those real problems that we all face every day probably I think is great.
[3035.18 → 3037.90] And of course, isn't it open source as well?
[3038.04 → 3038.86] It is, yes.
[3038.86 → 3042.94] So if people want to contribute, what should they do?
[3044.04 → 3047.66] Well, there are a bunch of issues in Qlang.org.
[3047.82 → 3052.98] So we have the one issue repo for, it's basically a big mono repo, right?
[3053.02 → 3054.58] So most of the development is there.
[3055.36 → 3059.24] And pick out an issue and see if you can fix it.
[3059.30 → 3062.36] Some of them are tagged with a good first issue.
[3063.50 → 3066.48] I'm not sure if they really are, but, you know.
[3066.48 → 3074.94] Actually, using Q itself and trying to come up with different ways that you think you might want to use Q
[3074.94 → 3083.98] and trying is actually a perfect way, sort of, especially in these pre-V1 days, of providing feedback.
[3083.98 → 3088.68] So, yes, of course, is the contribution to the Q code base itself.
[3089.18 → 3096.18] But actually using Q, that's where, sort of, if there are any rough edges, just finding those now has been great.
[3096.60 → 3099.34] And so those people who are using Q for lots of different things.
[3099.40 → 3105.62] So one of my favourite use cases, for example, is actually using Q to configure my GitHub Actions.
[3105.62 → 3115.94] So instead of writing YAML, I actually write my GitHub Actions definitions in Q and in almost all of my repos now.
[3116.54 → 3123.70] And that validates against the schema that GitHub published, which is published in JSON schema, as it happens.
[3124.04 → 3128.28] But that helped, you know, I think it was about six months ago, actually going through that process,
[3128.46 → 3133.48] helped uncover a few issues with the JSON schema interpretation in the Q project.
[3133.48 → 3138.62] So trying out all these different ways in which Q can be used is a massive, massive help.
[3139.10 → 3147.44] So any sort of feedback or bugs or problems that people find or suggestions that people have along those ways is going to be fantastically helpful too.
[3148.14 → 3153.42] Great. What a great way to contribute if you don't feel like you can get in and start working on the code base.
[3153.98 → 3156.82] Using it and reporting back is great.
[3157.32 → 3161.68] Well, it's that time, that great time for Unpopular Opinions.
[3163.48 → 3167.24] Unpopular Opinions
[3167.24 → 3167.48] Unpopular Opinions
[3167.48 → 3168.10] What?
[3168.22 → 3169.96] I actually think you should probably leave.
[3170.44 → 3175.48] Unpopular Opinions
[3175.48 → 3179.48] Unpopular Opinions
[3179.48 → 3184.84] So, who wants to kick us off? Who has an unpopular opinion?
[3185.90 → 3190.50] Well, let me start with one. I think I've alluded to it before already.
[3190.50 → 3205.50] But so to me, basically, inheritance is the biggest source of complexity in configuration languages and a great evil that should be avoided, you know, which might sound sensible after everything I explained today.
[3205.64 → 3210.90] But it does mean it eliminates most configuration languages as a useful tool.
[3210.90 → 3212.60] So, that might be unpopular.
[3213.04 → 3220.98] Well, I don't know if it's going to be unpopular to Go people because one of the nice things about Go is you can't build these complex type hierarchies.
[3221.24 → 3222.90] And I used to do C Sharp.
[3222.90 → 3234.58] And honestly, I would build, like, cathedrals out of time. Honestly, beautiful things. Generics. Generics with various conditions. Ah.
[3234.58 → 3256.18] And then, like, the next day when I'd go to try and look at it, I was like, no, no, I'll start again. And Go sort of doesn't have them. And so you can't tie yourself in knots in that same way. But we'll see. We do test these unpopular opinions, Marcel. And if you don't manage to, we actually poll them on Twitter to find out if they are indeed unpopular.
[3256.18 → 3265.18] Yeah. And if they're not, you have to come back on and think of another one. Yeah. That's the rule. Okay. I think that's a great one. Any others?
[3265.58 → 3275.64] Well, this isn't directly related to Q, but I just say that I think that tests can be more of a liability than an asset.
[3276.20 → 3281.08] Oh, interesting. They can be. In what way can they be?
[3281.08 → 3304.14] So I think a lot of people write tests that aren't very useful. You know, they're not telling you very much about how well the code works. And when your code changes, you have to change all the tests because maybe they're relying on, they're using mocks, they're relying on internals. And actually, the tests are worse than useless because they're not really telling you that the code works.
[3304.14 → 3311.70] And you have to change maybe twice as much code or three times as much code as you would if you didn't have any tests at all.
[3312.66 → 3320.16] And I think this is, you know, I'm a great believer in trying to do more end-to-end tests as much as you can.
[3320.16 → 3336.06] And I've been doing this with Q quite a lot in terms of building up libraries of, you know, corpuses. And you can do that really nicely in Q. It's a great format for putting, you know, if you've got a test data directory, you have a load of stuff in Q and you can maintain that really well.
[3336.06 → 3350.06] And the go code just reads it as JSON, doesn't care that it's all specified in Q. And that's, maybe that's a tenuous connection. But really, you know, I've seen, I spent too much time dealing with tests.
[3350.06 → 3380.04] Right. Yes. I'm actually with you on this one, Roger, entirely. I used to build cathedrals out of tests. Really complicated things. Beautiful structures. Yeah, I've learned kind of the hard way over time of just tests being a bit of an albatross around your neck versus, you know, compared to like, when you get them right, you definitely feel better.
[3380.06 → 3401.24] And you're right. When they're too brittle, when they're to bound to your code, you almost end up just saying the same thing twice, which doesn't really have any value at all, does it? So yeah, again, we're going to test this one, but I have a feeling that one's not going to be unpopular, but we'll see. Good one. Mr. Jolly.
[3401.24 → 3412.00] I don't have one. Unfortunately, mine was going to be a controversial one that it should, we should be all referring to this as Q as opposed to Q Lang, but we somewhat hijacked that earlier on, unfortunately.
[3412.48 → 3413.76] Ah, sorry, mate.
[3414.60 → 3418.88] I gave an unpopular opinion a couple of weeks ago, so I'm happy to sit out.
[3419.84 → 3424.22] Okay, right. So, okay. That's quite, that is quite unpopular to not give an opinion.
[3424.22 → 3428.36] And in the spirit of Q, that's quite meta as well.
[3428.62 → 3431.60] You know, I trimmed my unpopular opinion.
[3432.24 → 3432.40] Yeah.
[3434.30 → 3435.60] That's a Q joke, isn't it?
[3435.88 → 3436.56] It is. Yeah, yeah.
[3436.62 → 3441.82] Yeah, I don't get it yet, but I'm going to learn Q, and then I'm going to come back and listen. I'm going to be, I'm going to be loving that.
[3441.82 → 3451.82] Okay, well, that is all the time we have for today, but thank you, gentlemen, so much for coming on and telling us about this.
[3452.10 → 3458.86] It's definitely got me excited about Q. I can already think of a few different use cases where it really, I think, is perfect.
[3459.16 → 3462.68] So, I'll be one of those contributors trying things out.
[3462.68 → 3471.16] All that leaves me now is to say, you boy, down there, listen, is that prized turkey still in the window? Right.
[3472.00 → 3475.20] Go and get it then, and I'll give you a tuppence.
[3476.20 → 3479.48] I'll tell you, for these Victorian orphans, what are we going to do with them, Roger?
[3479.80 → 3482.16] Pop them in the workhouse, is what you were saying earlier, isn't it?
[3484.24 → 3484.64] Basically.
[3485.50 → 3487.00] Don't worry, this is getting edited out.
[3487.00 → 3493.92] So, thank you so much for joining us, Marcel, Paul, Roger.
[3494.28 → 3496.08] It's a pleasure, and thanks for listening.
[3496.52 → 3497.34] See you next time.
[3497.66 → 3498.20] Thank you, Matt.
[3498.36 → 3498.82] Thanks, Matt.
[3499.16 → 3499.44] Cheers.
[3503.52 → 3508.84] If this is your first time listening to Go Time, subscribe now at gotime.fm.
[3509.22 → 3513.66] Or search for Go Time in your favourite podcast app and hit the subscribe button there.
[3513.96 → 3514.70] You'll find us.
[3514.70 → 3517.54] And hey, while you're there, leave us a five-star review.
[3517.88 → 3518.62] We'd appreciate that.
[3519.30 → 3521.52] This episode was hosted by Matt Refer.
[3521.76 → 3525.76] It was produced by Jared Santo with music by the Beat Freak, Break master Cylinder.
[3526.18 → 3528.40] Go Time is brought to you by our awesome sponsors.
[3528.74 → 3531.86] Special thanks to Vastly, Launch Darkly, and Linde.
[3532.34 → 3539.10] On the next episode, panellists Angelica, Chris, John, and Johnny discuss why writing is an important discipline for software developers.
[3539.50 → 3540.52] Stay tuned for that one.
[3540.80 → 3542.88] It's hitting your podcast feed next week.
[3544.70 → 3574.68] We'll see you next time.
[3574.70 → 3604.68] We'll see you next time.
[3605.20 → 3605.26] Go Time.
[3605.26 → 3606.70] Go Time.
[3606.70 → 3607.74] Go Time.
[3607.76 → 3608.54] .
[3608.54 → 3610.78] Go Time.
[3610.78 → 3640.76] Thank you.

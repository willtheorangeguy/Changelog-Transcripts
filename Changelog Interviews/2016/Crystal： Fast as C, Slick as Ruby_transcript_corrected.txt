[0.00 → 1.40] I'm Ari Rosenzweig.
[1.70 → 2.70] And I'm Juan Ackerman.
[3.04 → 4.66] And you're listening to The Changelog.
[13.44 → 14.58] Welcome back, everyone.
[14.74 → 17.50] This is The Changelog, and I'm your host, Adam Stachowiak.
[17.62 → 24.68] This is episode 192, and we're talking today about Crystal Lang, fast as C, slick as Ruby.
[24.68 → 31.30] We had Ari Rosenzweig and Juan Ackerman on the show today talking about this awesome language.
[32.02 → 38.20] We covered so many awesome things, the language goals, how it's the best of both worlds between Ruby and C,
[38.78 → 44.02] and why if it's so close to and inspired by Ruby, why not just give their time and effort to Ruby instead?
[44.60 → 50.16] We talked about the new compiler, and we also discussed what's left before Crystal Can Go 1.0.
[50.64 → 53.30] Our first sponsor of the show is Total.
[53.30 → 56.20] Total, friends of the show, we love Total around here.
[56.26 → 59.64] Go to t-o-p-t-a-l.com.
[59.98 → 63.74] Or if you'd like a personal introduction to someone at Total, give me a shout.
[64.28 → 66.94] Email me at Adam at changelog.com.
[67.20 → 74.26] Whether you're an awesome engineer, an awesome designer, or someone looking for awesome engineers and awesome designers,
[74.80 → 75.88] give me a shout.
[75.88 → 80.30] I'd love to give you a personal introduction to someone at Total to get you on the right step forward,
[80.30 → 83.76] getting to that next great developer or designer working with you,
[83.92 → 87.52] or being that next great designer or developer working through Total.
[87.82 → 93.94] Living the dream, being able to travel the world and do all the things that Total provides to software developers and designers.
[94.40 → 97.38] Again, t-o-p-t-a-l.com.
[97.60 → 100.52] Or email me, Adam at changelog.com.
[100.78 → 102.00] And now, on to the show.
[102.00 → 112.74] Hey everyone, we're here today talking about Crystal Line.
[112.82 → 116.70] We got two awesome people from Buenos Aires, Argentina joining us today.
[117.18 → 118.88] Aria Bounsweet and Juan.
[119.68 → 120.84] I don't know how to say the last name.
[120.90 → 121.48] Help me out.
[121.50 → 122.36] How do you say the last name?
[123.24 → 124.66] I pronounce it Wagnerian.
[124.82 → 125.16] Wagnerian.
[125.32 → 125.68] Okay.
[126.68 → 127.92] Anyway, it works for you.
[128.14 → 128.50] That's fine.
[129.20 → 129.50] Gotcha.
[129.50 → 129.62] Gotcha.
[130.18 → 131.18] And Jared, you're here, of course.
[131.34 → 132.02] So, say what's up.
[132.50 → 133.04] I'm here.
[133.28 → 133.92] What's up, everybody?
[134.32 → 135.50] Guys, welcome to the show.
[135.92 → 136.52] No, thank you.
[137.04 → 138.40] Jared, we've been...
[138.40 → 139.18] This hit our radar.
[139.28 → 143.78] I don't know when it hit your radar, but our radar as our weekly email.
[144.62 → 147.82] When we shipped our issue 32, which was forever ago, basically,
[148.30 → 150.26] we talked about Crystal Line there.
[150.58 → 152.42] We've talked about it a couple of times here and there.
[152.50 → 156.52] It hasn't quite bubbled up too much, but we knew we wanted to get them on the show.
[156.52 → 160.84] We tweeted to you guys way back when, I think it was about at least six or seven months ago,
[160.84 → 164.48] that we were wanting to get a show started on this.
[164.78 → 169.54] But so, I guess, welcome to the show for once, which is awesome to finally get you on here.
[169.62 → 172.74] So, let's maybe start off with some introductions.
[173.10 → 175.82] So, with Ari, who are you, and what do you do?
[176.86 → 177.66] Hi, everyone.
[177.66 → 188.66] So, I'm a programmer, and I don't know what specifically to say, but...
[189.40 → 191.24] But you guys are both from Manu's, right?
[191.36 → 192.10] Manu's Technology.
[192.72 → 192.94] Yes.
[192.94 → 195.56] That's behind this language, and you're the Dev Lead.
[195.60 → 196.04] Is that right?
[196.56 → 197.04] Yes.
[197.22 → 197.46] Okay.
[197.64 → 198.38] That's right.
[199.20 → 199.52] Gotcha.
[199.92 → 201.10] And, Juan, how about you?
[201.10 → 206.14] Well, I've been working on Manu's almost from the beginning.
[206.78 → 209.12] That was like 12 years ago.
[209.64 → 212.56] I'm kind of a co-founder of this company.
[213.52 → 217.08] And, yeah, we do a lot of a bunch of stuff.
[217.68 → 220.28] Basically, software consulting.
[220.28 → 225.28] And, well, yeah, I'm pretty much...
[225.96 → 229.50] I have many roles here, like Dev Leader and programmer.
[229.82 → 230.72] I'm also a CTO.
[231.24 → 232.12] And, yeah.
[232.62 → 236.18] Yeah, Jared and I were talking about the homepage for your company, actually.
[236.40 → 238.50] Manus.com.ar.
[238.68 → 242.44] So, that's M-A-N-A-S.com.ar.
[242.94 → 247.38] And we're just talking about how it walks you through choosing if you're the right company for people to work with.
[247.38 → 248.98] So, that's pretty interesting.
[248.98 → 250.94] Well, that's interesting.
[251.14 → 254.96] And also related with how Manu's started.
[255.28 → 260.98] You know, I've been working for much software consulting companies.
[261.82 → 265.22] And one day, one of my best friends called me, and he said,
[265.32 → 267.40] Hey, I'm starting this company.
[267.50 → 268.20] They want to join me.
[268.74 → 271.00] And I said, Yes, of course.
[271.00 → 276.04] And even though I started with a much smaller salary,
[276.66 → 283.18] and the good thing is that we could decide what projects to take and which projects we don't.
[283.34 → 284.54] And so, we could decide.
[284.92 → 285.14] Right.
[285.28 → 286.74] Be a bit more selective then.
[287.34 → 288.10] Yeah, exactly.
[288.10 → 303.12] So, that's pretty much the inspiration of the company that we want to make the cool stuff and the things that we really know how to do and how can we make use of our best skills.
[303.12 → 312.44] Just to kind of paint a little bit of a word picture for the listeners, if you go check out their website, which is in the show notes, they have a little coloured meter in the centre.
[313.14 → 314.70] And it says, So, you're looking for a software company.
[314.78 → 316.14] Let's see if it's the right choice.
[316.14 → 319.40] And on the far left-hand side is tried Google.
[320.30 → 322.58] And as you work your way to the other side, it's, Oh, yeah.
[322.66 → 323.56] It's like they're very excited.
[324.14 → 330.36] There's a series of questions, which you can checkbox that kind of describes what kind of project you have.
[330.80 → 333.58] And as you check certain ones, it moves the meter left or right.
[333.96 → 334.50] So, check that out.
[334.56 → 335.92] It's definitely an interesting concept.
[336.16 → 343.24] And I think a nice way of you guys, you know, helping your customers self-select for more interesting projects.
[343.66 → 343.76] Yeah.
[343.76 → 343.82] Yeah.
[343.82 → 343.94] Yeah.
[344.32 → 355.22] So, we're here to talk about Crystal, which is a programming language that calls itself as fast as C and as slick as Ruby.
[356.56 → 367.12] If you hit up the homepage, crystallang.org, you'll find that there are a series of goals set out for the language, which is Ruby-inspired syntax,
[367.44 → 372.44] statically type checked, but without having to specify the type of variables or method arguments,
[372.44 → 377.78] a series of language goals for Crystal, the kind of language that you guys want it to be.
[378.40 → 382.24] And I was hoping that we'd start off with your kind of walking us through those goals.
[382.34 → 391.22] I believe there's about five or six of them and explaining what they are, what they mean, and why they're desirable in a programming language.
[391.22 → 394.76] So, the first one is Ruby-inspired syntax.
[397.18 → 402.68] That's like one of the things that motivated the creation of the language.
[402.68 → 408.06] And the second point, too, is that we really like Ruby syntax.
[409.02 → 410.98] It's very readable.
[411.20 → 411.94] It's elegant.
[411.94 → 415.28] So, that's basically it.
[415.78 → 422.66] So, just to add to the previous one, here at Manu's, we use Ruby a lot for many projects.
[422.96 → 424.18] We still use Ruby.
[424.98 → 431.40] In particular, we use Ruby on Rails because it's really fast to prototype a new project
[431.40 → 435.84] and come up with a solution that actually works in minimal time.
[435.84 → 439.82] So, that's what we love about Ruby and Ruby on Rails.
[440.42 → 448.56] And when we started with Crystal, we wanted to have the same feeling in our language.
[449.14 → 457.74] Like, with Ruby, you can always come up with an elegant solution for each algorithm or problem that you need to solve.
[457.88 → 459.50] And we wanted the same in Crystal.
[459.50 → 469.80] So, that's why we inspired on the syntax and also not only the syntax, but also the standard library and the feelings of the language when you're coding.
[470.82 → 477.66] But normally, one of the problems that we have with Ruby is the performance.
[478.24 → 487.04] For many projects, once the project grows, and we're starting to have performance issues,
[487.04 → 491.26] and we need to migrate some parts of the backend to another language.
[491.48 → 499.44] And we move parts of some projects to Slang, for example, or to Go, just to match with the performance requirements.
[500.14 → 504.76] So, we've been thinking why we need to move to another language.
[504.88 → 514.16] What if we could have a language that provides both the elegance of Ruby, but the performance of a compiled language?
[514.16 → 515.18] Mm-hmm.
[515.64 → 521.94] So, that's what motivates some of these goals for the language.
[522.38 → 528.38] Also, if you look at how many projects solve the performance issues in Ruby,
[528.84 → 536.74] most of the time, you have specific gems that re-implement some of the solutions in C language.
[537.04 → 537.22] Right.
[537.30 → 542.02] And nobody likes that, because who wants to write C language in this century?
[542.02 → 545.74] So, that would be the third goal.
[546.78 → 555.24] This is, it means, if you want performance, you don't need to re-implement part of your code in C.
[555.48 → 563.22] You have to be able to write your code just in Crystal and get the best of your CPU or other resources.
[563.22 → 570.20] Right. So, right now, if you're a Ruby programmer, and you want to have a specific section of code that needs to be highly performant,
[570.34 → 575.86] you'll often write that in C and then have a Ruby wrapper binding to that C layer.
[576.34 → 580.72] You know, kind of the most, or at least for me, the one I think of most often is like NoCogiri,
[581.20 → 583.84] or similar when it comes to parsing XML or HTML.
[583.84 → 586.66] You know, you have a C library in there.
[587.30 → 594.32] And the idea with Crystal is you still want to have that speed, but you don't want to have the C in there.
[594.62 → 596.68] So, everything's in Crystal, right?
[597.30 → 601.04] Exactly. You don't want to leave the language to get performance.
[601.04 → 609.46] And the next one you have there is to have compiled time evaluation and generation of code to avoid boilerplate code.
[610.22 → 611.66] Can you explain that one?
[611.94 → 617.54] That's another strong point about Ruby, the metaprogramming capabilities, right?
[617.74 → 620.00] And everybody loves that.
[620.00 → 630.90] And it's hard if it's not impossible to have the same kind of metaprogramming in a statically compiled language.
[631.04 → 631.34] Right.
[631.56 → 638.84] So, we introduce things like macros that are evaluated at different stages of the compilation
[638.84 → 647.84] that allow us to generate code that gives you the sense of having metaprogramming, but in a different way.
[648.50 → 649.92] So, you have these specific goals.
[650.02 → 655.50] You like Ruby, but you don't like certain aspects of it, specifically performance, the C bindings,
[656.22 → 660.66] the fact that you can have great tooling around type checking and whatnot.
[661.04 → 662.82] Or the dynamic types.
[663.98 → 666.70] And you decide enough is enough.
[667.02 → 669.50] We're going to write our own programming language.
[669.64 → 675.12] So, for me, I guess I'm kind of a small, I consider myself a small thinker.
[675.28 → 676.70] Like, I have small ideas.
[676.70 → 678.72] I'm an app developer.
[678.82 → 684.02] So, I think about applications more so than languages are very intimidating.
[684.86 → 690.46] So, when it comes to let's write our own language, that was, to me, that's a crazy idea.
[690.98 → 694.54] I love that people like you want to do this kind of things.
[694.54 → 697.96] And I like to use languages and study them.
[698.14 → 700.80] But to write my own is incredibly overwhelming.
[701.06 → 703.96] So, I guess the question is, whose crazy idea was this?
[704.42 → 708.40] And kind of how did you guys get up the gumption to actually write that first line of code?
[709.12 → 709.90] That would be Ari.
[709.90 → 710.78] Yes.
[711.32 → 713.16] So, that idea was mine.
[714.82 → 719.94] When I decided to do it, it wasn't like, okay, I'm going to make a language.
[720.24 → 721.94] It was just an experiment.
[722.42 → 725.54] I said, hmm, this idea is interesting.
[725.78 → 727.68] Let's see what I can do with it.
[727.68 → 731.00] And I started doing it alone.
[732.12 → 736.28] And then, eventually, I showed it to Juan.
[737.84 → 742.72] And he said, like, wow, this is a nice idea.
[744.22 → 747.32] I'll join and let's work together to make it work.
[748.24 → 752.74] But all the time, like an experiment, a hobby, something fun to do.
[752.74 → 757.62] So, it's not like this is our 10th language that we are implementing.
[758.06 → 759.70] And now we have experience.
[759.94 → 767.48] It was just we did the Lever, Parser, and all the stages as we learned things.
[768.44 → 771.66] Of course, we had experience with other languages before.
[771.78 → 774.02] So, we knew what we wanted.
[774.94 → 778.14] And that's basically the story of the beginnings.
[778.14 → 785.44] So, through the magic of Git commit histories, I went back and checked out your very first commit,
[785.94 → 790.82] which will help to give some timing around this project because it is a new programming language.
[791.04 → 792.86] That being said, it's almost four years old.
[793.52 → 796.68] So, you know, programming languages take a while to grow up.
[797.34 → 800.90] And something created in 2012 is definitely still a young language.
[801.44 → 804.16] But your first commit was September 4th, 2012.
[804.16 → 810.64] ARIA, it was yourself, which include a Lever, a Parser, an AST, a few other things.
[811.56 → 818.04] And it was completely written in Ruby at that time, which is interesting because, of course,
[818.32 → 822.46] it's the tool that you guys love, and you're kind of writing some of a replacement in it in Ruby,
[822.96 → 823.74] which is kind of cool.
[824.46 → 830.80] But at that point, when you hit that first commit, there was a fair bit of code there.
[830.80 → 833.94] Did you have a Crystal Hello World at that point?
[835.22 → 838.10] Well, in fact, there is another repository.
[838.96 → 845.60] It's under my account, Sterile, that also has Crystal, but it's not a fork.
[845.74 → 852.68] It was like the previous version of the language, which was not very good.
[852.68 → 858.22] Once Juan joined, we rewrote things from scratch.
[859.66 → 866.38] And so that was maybe one year or two years ago, before that first commit you found.
[866.94 → 867.26] Okay.
[868.92 → 875.24] I think there was a Hello World or something similar, but maybe with C bindings.
[875.24 → 879.78] So it goes back even further back into like what, like 2011, 2010, something like that?
[880.28 → 880.64] 2011.
[881.14 → 881.36] Yeah.
[881.70 → 882.40] That's what I was getting.
[882.46 → 884.90] I was trying to page back quickly as you said that.
[884.98 → 890.86] I went to your GitHub, which is GitHub.com slash A-S-T-E-R-I-T-E.
[890.98 → 893.08] So for those listening along, I'll go to the show notes too.
[893.14 → 893.76] That'll be there.
[894.30 → 895.42] But it goes back to 2011.
[895.90 → 900.96] And what's in the first version, I guess, of this since Jared's question was thinking 2012.
[901.12 → 901.78] What's in 2011?
[901.94 → 902.78] What's the Hello World there?
[902.78 → 905.22] I don't know.
[905.34 → 907.02] It was just something.
[907.44 → 909.54] It was a toy at that point.
[910.40 → 910.62] I think.
[911.40 → 911.88] Just ideas.
[912.68 → 912.94] Yeah.
[913.24 → 914.20] Just ideas.
[915.20 → 918.10] Some things with closures and how to.
[918.54 → 923.18] It was just maybe to learn how to start making a language.
[923.88 → 930.24] And then we said, okay, now that we learned a bit, let's go a bit more serious.
[930.24 → 933.90] Well, the truth is, these goals were not from the beginning.
[934.68 → 937.02] Ari started this like an experiment.
[937.80 → 945.38] And once we decided that this could be a good thing to do seriously, then we set up these goals.
[945.38 → 951.20] But from the beginning, it was just like an experiment that he was doing on his own.
[951.36 → 956.20] And when he showed me, it was like, well, you know, Ari is an extremely humble guy.
[956.70 → 961.36] And it seems like he didn't know what he has in his hands.
[961.36 → 966.76] And he showed me this, and they say, wow, this could be a big thing, you know.
[967.40 → 979.20] So one of the things that I think about when it comes to programming languages is, and I probably, a lot of people think about this because it's the part that we interact with, which is the semantics and the syntax and the way it looks.
[979.20 → 986.32] Crystal is, you know, its main selling point is slick as Ruby.
[986.70 → 988.08] Obviously, Ruby is a huge inspiration.
[988.68 → 993.66] Were you guys going for similar type of syntax?
[993.78 → 994.88] Were you trying to get identical?
[995.82 → 1006.70] Were you trying to, you know, port Ruby in such a way that you could actually like, you know, swap out the Ruby binary and swap in a Crystal binary and be able to run the same code?
[1006.70 → 1008.22] Or is it just inspired by Ruby?
[1008.22 → 1021.72] Well, in the beginning, we wanted, we started with something that was like 100% compatible with Ruby, but obviously the standard library was empty, and you couldn't do much.
[1022.28 → 1030.34] But we soon realized that that wasn't going to work because Ruby is very dynamic.
[1031.38 → 1034.40] And we wanted a statically typed language.
[1034.40 → 1041.98] So we had to make some concessions, like adding some types to generic type arguments.
[1043.88 → 1055.44] And at that point, we said, OK, we want to preserve that Ruby feeling when you program, but we won't make a Ruby compatible language.
[1055.44 → 1057.86] It won't be a Ruby implementation.
[1058.66 → 1063.52] We want to keep the feeling, but it's a completely different language.
[1063.52 → 1068.18] I just want to kind of go back to that, you know, that time in 2011, 2012.
[1068.98 → 1073.08] Maybe when you guys got serious in 2012 and said, OK, we're going to do this.
[1073.44 → 1076.26] And here we are, you know, it's just the beginning of 2016.
[1076.62 → 1078.78] So you got, you know, roughly four years into this.
[1079.58 → 1080.84] Tons of hours, I'm sure.
[1081.50 → 1085.28] We'll talk about it later, but you're now had people supporting you on Bounty Source.
[1085.28 → 1093.72] So it's been a large effort and if it's continued success, it'll be continued to be a larger effort as it grows and changes.
[1094.80 → 1098.96] And Adam, I'm kind of stealing your question here a little bit because you mentioned this in our pre-call, which is,
[1099.28 → 1109.50] if you love Ruby so much, why not just take all of that time and effort and money or whatever it was that you guys had put into Crystal
[1109.50 → 1118.00] and, you know, give that to Ruby over the years, you know, similar to some companies are coming out now.
[1118.46 → 1124.40] I think it was App folio recently announced that, you know, they want Ruby 3 to be three times faster.
[1124.92 → 1127.54] And so they're going to hire a performance developer.
[1127.90 → 1132.96] I can't remember the details exactly, but they're going to have somebody work with the Ruby core team in order to improve performance.
[1132.96 → 1139.56] From your guys' perspective, and maybe, you know, maybe it's because these weren't your original goals,
[1139.70 → 1144.52] but couldn't it be slick as Ruby and fast as Ruby as opposed to a whole new thing?
[1144.82 → 1149.54] And maybe with retrospect, you guys can look back and comment on that idea instead.
[1150.44 → 1156.56] Well, I think it's, I mean, Ruby could probably be much faster than it is right now.
[1156.80 → 1159.16] It could probably make a lot of improvements.
[1159.16 → 1173.22] But I don't really know they can actually match the speed and the efficiency of a language that complies to an executable binary,
[1173.48 → 1177.22] you know, like Crystal or Go or C, right?
[1177.36 → 1183.42] I mean, they can improve the current state, but they will never be able to match that kind of performance.
[1183.42 → 1192.08] So, uh, there's another thing that, uh, it's one of the it's the second goal that's, uh, statically type check.
[1192.70 → 1197.84] That's, uh, when, when, and it's really common in Ruby, and we've experienced it,
[1197.84 → 1201.52] that when you need to refactor a big code or make changes,
[1201.52 → 1207.38] unless you have like 150%, like more than 100, I don't know.
[1207.38 → 1211.00] You have to make, have tests, uh, everywhere.
[1211.68 → 1215.28] Uh, you, you are not sure that you're not breaking something.
[1215.28 → 1220.94] And eventually you get undefined method, uh, something at, at runtime.
[1221.80 → 1224.78] And that's like, that, that's not good.
[1225.16 → 1230.36] Uh, so with, uh, static type checks, uh, that issue is gone.
[1230.36 → 1236.44] And also as a side effect, you can like to compile your code and make it more efficient,
[1236.44 → 1238.44] but there, there are two things.
[1238.44 → 1240.96] So performance and static type checks.
[1241.36 → 1247.54] And I don't think they are going to add eventually static type checks to Ruby.
[1247.92 → 1255.34] Maybe they, they'll add, uh, type annotations, uh, but they will improve the error messages, maybe.
[1255.34 → 1264.08] But I don't think like you will be able to say, okay, check the types for my program because, uh, Ruby wants to,
[1264.16 → 1270.00] or at least I know that wants to prefer, uh, preserve that dynamic nature.
[1270.86 → 1274.82] It's really hard to change Ruby to a statically typed language.
[1275.56 → 1275.78] Agreed.
[1276.06 → 1277.14] 100%.
[1277.14 → 1282.02] Well, I think this is a good chance to stop for a moment, take a break.
[1282.02 → 1294.82] On the other side of the break, we want to track it between the time when you had a, a, a Ruby based compiler, uh, for crystal and how you got it to be completely self-hosting a crystal based compiler.
[1295.00 → 1300.34] Also want to ask you how you go about getting those syntax highlights on GitHub for a brand-new language.
[1300.50 → 1303.80] So stay tuned, and we will ask those questions after the break.
[1303.80 → 1310.02] Our friends, Linde are huge fans of the show and many of the developers that work at Linde.
[1310.42 → 1311.72] Listen to the show.
[1311.82 → 1313.14] They're huge fans of what we're doing here.
[1313.18 → 1314.32] They want to support what we're doing.
[1314.54 → 1317.62] And we want to invite you to try out Linde.
[1317.78 → 1321.54] One of the fastest efficient SSD cloud servers on the market.
[1322.00 → 1325.58] Use our code change log 20 to get $20 in credit.
[1326.04 → 1329.58] Basically two free months plan started just 10 bucks a month.
[1329.58 → 1336.02] They have eight data centres spread across the entire world, North America, Europe, Asia Pacific.
[1336.58 → 1339.88] They got hourly billing with a monthly cap on all plans and add on services.
[1340.24 → 1346.66] You get full root access for more control, run VMs, run containers, or even your own private Git server.
[1347.12 → 1352.82] You can enjoy native SSD storage for a gigabit network, Intel E5 processors.
[1353.10 → 1357.70] Again, use the code change log 20 to get a $20 credit with unlimited uses.
[1357.70 → 1358.60] Just tell your friends.
[1358.98 → 1360.94] It doesn't expire until the end of this year.
[1361.10 → 1362.88] So use it as many times as you want.
[1362.98 → 1363.52] Share it.
[1363.80 → 1364.64] Tell everyone you know.
[1365.06 → 1367.70] Head to Linode.com slash change law to get started.
[1370.20 → 1370.84] All right.
[1370.86 → 1372.92] We are back with Ari and Juan.
[1373.72 → 1379.98] Talking about Crystal Language, its history, why it exists, all the time and effort they put into it.
[1380.22 → 1385.24] And I got to admit, guys, you got a lot of people pretty interested in it.
[1385.24 → 1387.94] And so we're talking about 2012.
[1388.36 → 1393.14] You guys had a Ruby-based compiler and a syntax for the Crystal Language.
[1394.24 → 1398.42] But now if you go to the repository, it's 99.9% Crystal.
[1398.86 → 1402.74] So at a certain point, you had a self-hosting Crystal-based compiler.
[1403.38 → 1411.06] And I was hoping one of you can take us kind of, you know, a brief history of how you went from the Ruby-based compiler to the Crystal one, how long that took.
[1411.06 → 1412.74] And tell us about that.
[1413.40 → 1414.68] Code from Ruby to Crystal.
[1414.84 → 1424.86] Because we actually did the compiler in Ruby, hoping that because the syntax is similar, and also the standard library and so on,
[1424.86 → 1431.44] we would eventually be able to port the compiler quickly.
[1432.26 → 1441.40] That didn't turn to be quite true because Ruby's standard library is more or less complete.
[1442.14 → 1445.62] So we had to implement all of that in Crystal.
[1445.62 → 1450.50] So it was like, okay, let's try to port the compiler to Crystal.
[1451.30 → 1454.44] Oh, we are missing these things.
[1454.84 → 1455.96] So let's do them.
[1456.10 → 1458.24] Oh, we found these bugs in the compiler.
[1458.98 → 1460.18] So let's fix them.
[1461.18 → 1469.88] And everything we did to the compiler, which was written in Ruby, we had to port to the new compiler and so on.
[1469.88 → 1475.00] So it was like, it was a task that never seemed to end.
[1476.36 → 1482.46] But eventually we said, okay, let's stop fixing bugs in the current compiler.
[1482.60 → 1489.06] Let's try to make the next compiler in Crystal, work around some issues.
[1489.06 → 1492.22] And eventually we did it.
[1492.32 → 1494.74] I don't know how much it took, maybe one year.
[1495.18 → 1499.22] But it wasn't a year dedicated to porting the compiler.
[1499.48 → 1507.68] It was growing the current compiler, growing the standard library, fixing bugs and making new features and so on.
[1508.08 → 1512.74] It was a really fun task, I think.
[1512.74 → 1519.88] Once you get to compile a program that when you compile it again, it gives the same program.
[1521.36 → 1525.98] And then you say, okay, I don't need Ruby anymore for this.
[1526.20 → 1529.06] And I can go on with just this language.
[1529.38 → 1530.26] It's really cool.
[1530.26 → 1540.76] So you guys have, as of now, you have about 4,100, almost 4,200 stars, 335 forks, and 119 contributors.
[1541.06 → 1544.60] That's on the Manistee slash Crystal repository.
[1545.84 → 1550.98] So as I said, you've managed to kind of capture the hearts of people, and you've got people excited.
[1551.48 → 1556.22] When did you first announce Crystal to the open source community?
[1556.22 → 1559.34] And what was the decision making around that announcement?
[1559.44 → 1560.44] And then how was it received?
[1561.24 → 1565.48] I actually don't remember when was the first time we make this public.
[1565.88 → 1571.04] And I think it was in Hacker News or something like that.
[1571.38 → 1578.18] Of course, we immediately attracted attention from the Ruby community because of the similarities of language, of course.
[1578.18 → 1584.00] And, of course, many of them were expecting that we were doing a compiled Ruby.
[1584.50 → 1589.08] And many of them still do, I think, the same.
[1590.54 → 1595.86] So I think we decided to announce it or maybe make it public.
[1596.62 → 1602.42] It was public from the beginning, but we decided, I don't know, to post it in Hacker News or something like that
[1602.42 → 1609.34] to have a second opinion about the project because we thought it was something cool, something nice.
[1609.50 → 1612.86] But maybe others didn't think like that, or I don't know.
[1613.74 → 1620.90] And luckily and amazingly, the reception was amazing.
[1620.90 → 1624.18] And like a small community started to grow.
[1624.36 → 1629.48] There are people in Japan and Turkey giving talks, having small communities.
[1629.74 → 1634.08] It's really something I think we didn't expect that.
[1635.04 → 1643.28] And maybe all of that happened because Ruby's community and the people there are really nice and really helpful.
[1643.28 → 1645.12] And they want to collaborate.
[1645.34 → 1646.92] They want to do something good.
[1647.78 → 1653.04] And like it was transferred to this project somehow.
[1653.98 → 1660.18] Well, you might say that a programming language has officially arrived when it gets its first Rails-inspired web framework,
[1661.02 → 1664.46] which you guys now have Amethyst.
[1664.92 → 1667.22] I say you guys as in the Crystal community.
[1667.22 → 1669.26] It wasn't written by you two.
[1669.98 → 1671.36] But that one hit our radar.
[1671.36 → 1674.40] I think it was within the last six months or so.
[1675.06 → 1678.60] A kind of Sinatra-inspired Crystal-based web framework.
[1679.40 → 1681.58] So yes, Crystal has arrived in that regard.
[1682.64 → 1685.04] You said amazingly people received it well.
[1686.22 → 1692.42] Anybody in particular or any stories that you have of people using it that were a surprise to you
[1692.42 → 1698.70] or delighted to see Crystal projects such as Amethyst kind of coming out
[1698.70 → 1700.88] that you couldn't possibly have imagined?
[1701.02 → 1701.44] Anything like that?
[1702.24 → 1705.80] I think more than the code.
[1706.18 → 1710.96] I think like the community doing talks in countries.
[1711.46 → 1714.68] Like we searched the internet and found talks and said,
[1714.68 → 1716.88] Oh, look, they are talking about Crystal here.
[1716.94 → 1717.74] We didn't know that.
[1718.28 → 1719.32] They are doing stuff.
[1719.50 → 1726.96] Of course, the frameworks and the code is also something that's really helpful and nice.
[1727.52 → 1728.82] But I don't know.
[1728.88 → 1731.86] I enjoy more the surrounding community.
[1731.86 → 1736.18] And I don't know if Amethyst is the Rails' framework of Crystal.
[1736.42 → 1745.88] Like everyone's trying to do Rails for Crystal because maybe that's the most successful language for a project for Ruby.
[1745.88 → 1749.68] Now there's another one, Frost.
[1750.16 → 1752.90] That's in the early stages.
[1753.96 → 1757.58] And another one, Kamal, which is like Sinatra.
[1758.06 → 1766.12] But we really think of Crystal as being able to do other things like command line applications, web servers,
[1766.36 → 1769.16] maybe not using a huge framework.
[1769.16 → 1778.38] We try not to influence much about how a web framework would be designed in Crystal.
[1778.60 → 1778.90] We try.
[1779.14 → 1788.46] I mean, we have enough work to do making the language and making fixing bugs in the language and making perform better every day.
[1788.94 → 1796.18] And we let just other people in the community to create the frameworks around the language.
[1796.18 → 1799.44] And we want to focus on the language itself.
[1800.32 → 1803.40] Yeah, I was mostly saying that tongue-in-cheek about the web framework thing.
[1803.50 → 1809.28] It just seems like every new language pops some sort of Rails-inspired web framework.
[1809.50 → 1816.78] And sometimes the merits of that will invoke more excitement and sometimes not.
[1818.40 → 1819.60] Let's ask from this perspective.
[1819.68 → 1824.14] We're going to talk about the future here real quick about Crystal because you guys have a big change in the works.
[1824.14 → 1829.16] You announced it just a few weeks back, a big change coming to the programming language.
[1829.62 → 1830.74] And I want to talk about that in detail.
[1831.38 → 1837.60] But first, let's talk about an imaginary future where Crystal is as successful as you could possibly imagine.
[1838.04 → 1845.48] What's the ultimate end goal or success state look like for Crystal as a programming language?
[1845.58 → 1848.02] Feel free to go out there and share your hopes and dreams.
[1848.26 → 1853.28] What would be the awesome success story for Crystal looking back 10, 15 years from now?
[1853.28 → 1869.32] Well, for me, the most successful state would be the one that, I mean, when a developer wants to create a project that requires all the kind of stuff that you need right now,
[1869.44 → 1876.72] like performance and the ability to manage high amounts of concurrency.
[1876.72 → 1888.00] And you choose Crystal because it gives you that, but also gives you the benefits of a language that is similar to Ruby.
[1888.34 → 1894.98] You know, many people are choosing Go language right now or Erlang because of the concurrency capabilities.
[1894.98 → 1904.98] But they're not happy with the language itself because they feel so restricted in the object-oriented aspects.
[1905.98 → 1913.22] So in the future, I would like to choose Crystal because it matches both requirements.
[1913.22 → 1918.56] Speaking of the future, you recently wrote that post I mentioned before called The Future of Crystal,
[1919.52 → 1925.04] wherein you tell a bit of a Christmas story, which is kind of a fun read if you guys are interested.
[1925.22 → 1930.30] That's in the show notes about kind of an imagined future where Crystal becomes abandoned.
[1930.30 → 1939.12] And it's mostly due to these increased compile times, which seems to be only a small problem right now.
[1939.24 → 1943.24] But as you guys say in that little tale, it's a growing problem.
[1944.00 → 1946.08] And so you decided to rewrite the compiler.
[1947.14 → 1951.70] Can you tell a story on that decision and all that went into it?
[1951.70 → 1961.64] That question was always around like, okay, we are inferring types like this and the compiler works like this.
[1962.64 → 1972.50] And will it be able to handle like a huge project without you having to wait a lot of time?
[1973.26 → 1979.90] And from time to time, we thought about some solutions, but we didn't end up with many solutions.
[1979.90 → 1985.96] And eventually we realized that this way wasn't going to work.
[1987.02 → 1994.72] So it was kind of like in the beginning when we decided to add some types to generic types.
[1996.06 → 2004.14] We realized without that, the language couldn't continue evolving and adapting to greater needs.
[2004.14 → 2014.30] So this time we decided, or we concluded that we needed some type annotations for instance variables and a few other places.
[2015.30 → 2022.84] And with this, we have an algorithm, and we have an idea of how to make this scale for bigger projects.
[2022.84 → 2028.82] Because waiting for stuff to compile, it's not fun at all.
[2029.48 → 2031.60] And we want a language that's fun to use.
[2032.12 → 2034.00] So in all aspects.
[2035.14 → 2041.68] And adding type annotations here and there, just a few ones won't take that fun.
[2041.68 → 2049.04] Or it will take that fun less than having to wait a lot of time to compile your code.
[2049.54 → 2051.28] And we wanted to announce it.
[2051.70 → 2055.54] It's like we are working on the compiler, but not fully dedicated to it.
[2055.60 → 2059.08] It's like we are working on several things right now.
[2059.08 → 2064.02] But we wanted to announce it to know others' opinions.
[2065.64 → 2072.80] And to announce it to make sure we won't disappoint a lot of people later.
[2073.08 → 2075.94] The more we wait, maybe it's worse.
[2076.84 → 2080.08] When you say announce, you mean the fact that you're going to have to rewrite the compiler?
[2080.66 → 2081.66] Is that what you mean by that?
[2081.66 → 2088.54] That you'll have to add some more type annotations in some places.
[2089.30 → 2091.54] Like right now, you're not forced to do that.
[2092.52 → 2097.54] But once the new compiler arrives, you'll have to do that.
[2098.98 → 2108.98] And many complain because they say, no, in Ruby, you don't need to use type annotations.
[2108.98 → 2112.30] So, yeah, this is not a good decision.
[2112.76 → 2114.84] But it's a different language.
[2115.62 → 2119.92] So, it seems like we're hitting on a bit of the crux is the trade-offs.
[2120.34 → 2120.44] Right?
[2120.56 → 2123.04] Between your goals on...
[2123.04 → 2123.16] Right?
[2123.18 → 2123.84] You have two goals.
[2123.98 → 2125.72] Slick is Ruby and fast is C.
[2125.96 → 2129.12] And we know that the fastest C has a bunch of things in there.
[2129.14 → 2130.04] Like the type annotations.
[2130.18 → 2131.08] And it's not just speed.
[2131.68 → 2133.80] And it's hard to be a servant of two masters.
[2134.32 → 2136.96] And you have to pick one or the other in certain circumstances.
[2136.96 → 2142.96] And it seems like what you're finding out with the dynamism and the lack of types...
[2143.74 → 2150.08] Or excuse me, the lack of type annotations required currently is that the compiler suffers.
[2150.90 → 2155.34] And so, you have to make these decisions between, well, do we take the language this direction,
[2155.46 → 2161.96] which is further away from our Ruby syntax, our Ruby semantics, but closer to...
[2161.96 → 2164.10] But ultimately better?
[2164.42 → 2169.32] Or do we stick with this and possibly have these super long compile times in the future?
[2169.52 → 2173.00] And it seems like that's something that you guys have been struggling with.
[2173.02 → 2179.64] And you've decided to rewrite the compiler, add the type annotations, and kind of diverge further from Ruby.
[2179.70 → 2180.42] Is that a good summary?
[2180.42 → 2184.12] Yes, that's exactly it.
[2184.54 → 2187.32] We actually don't need to rewrite the compiler.
[2187.50 → 2191.82] We can just force type annotations and make it work like that.
[2191.94 → 2200.94] But with those type annotations, we can make a faster and more efficient compiler implementation.
[2200.94 → 2204.76] So, that's why we decided to completely do it.
[2205.24 → 2210.76] And it's also because now we have an idea of the whole language that we want.
[2210.90 → 2214.64] In the beginning, it was just growing as we added more features,
[2214.76 → 2221.02] but we didn't have the idea of how the language was going to look once finished
[2221.02 → 2225.02] or once having most of the features that we wanted.
[2225.02 → 2231.24] So, this is obviously a huge breaking change for all current users of the language, right?
[2232.18 → 2232.66] Yes.
[2232.80 → 2236.98] Their code's not going to compile anymore, probably, when they switch to the new.
[2237.52 → 2245.94] Yes, but on the other hand, we didn't hit 1.0 yet.
[2245.94 → 2253.54] So, in most of our releases, we break code because we take the opportunity.
[2253.92 → 2265.38] Since we are not at 1.0, we want to make sure we get the best standard library and compiler
[2265.38 → 2268.32] and language that we want before having to decide,
[2268.44 → 2272.64] okay, now we are going to be backwards compatible from now on.
[2272.64 → 2273.56] Mm-hmm.
[2274.28 → 2276.74] And it seems like if I was a current user of the language,
[2276.74 → 2282.18] I would be more concerned with the slowdown than I would be with the type annotations
[2282.18 → 2285.60] and with the changes to the language itself.
[2285.96 → 2289.26] Because it seems like a rewrite of the compiler is a huge undertaking.
[2290.10 → 2294.10] And as you said, there are lots of other aspects of the language that need building out,
[2294.62 → 2299.62] such as the standard library, but I think dependencies management
[2299.62 → 2302.14] and also a thing that needs to happen.
[2302.64 → 2304.44] Do you think this is going to set you guys back?
[2304.56 → 2305.40] Is it six months?
[2305.46 → 2306.14] Is it three months?
[2306.24 → 2309.98] Is there no setback as far as getting Crystal to that 1.0?
[2312.62 → 2312.98] Yes.
[2313.06 → 2315.50] I don't know how much time it will take.
[2316.34 → 2322.08] But in the meantime, we are continuing evolving the standard library,
[2322.30 → 2324.46] fixing bugs, adding some features.
[2324.46 → 2330.46] So it's not necessary for the compiler to be completed quickly
[2330.46 → 2337.12] because the upgrade or the migration path you need to do is really simple.
[2337.32 → 2339.22] You need to add some type annotations.
[2339.50 → 2343.08] But since the current compiler already infers those types,
[2344.08 → 2350.04] we'll probably make a tool that automatically adds those type annotations.
[2350.04 → 2358.12] So when we started, we had complete freedom of choosing when to break things, right?
[2358.34 → 2367.24] So after we make it public, and you start feeling that you have to maintain features
[2367.24 → 2371.72] or try to be backward compatible just because there is a community out there
[2371.72 → 2373.04] that is using the language.
[2373.38 → 2377.66] Well, we always try to communicate to our community
[2377.66 → 2383.44] that the language is not in production-ready state.
[2383.44 → 2392.60] So I think most of the people from our community is not just users of the language,
[2392.82 → 2396.70] but people that want to contribute to the evolution of the language.
[2397.24 → 2401.44] So I feel that making breaking changes is actually...
[2402.58 → 2410.28] Because we actually talk with them and share the decisions.
[2410.28 → 2415.52] So they actually feel they are parts of the decisions that we make in the language.
[2415.96 → 2418.88] So it's not that someone's going to get angry
[2418.88 → 2426.50] because we broke the compatibility with the previous versions.
[2427.50 → 2431.98] So at this stage, the current state of the project,
[2432.40 → 2437.40] we want to still be able to have freedom of breaking things.
[2437.40 → 2442.56] We think that we did things that are wrong in the past
[2442.56 → 2448.34] and we still want to make the best language that we can.
[2448.56 → 2450.58] So if we want to...
[2450.58 → 2454.32] If we have to maintain backward compatibility, that is not possible.
[2455.04 → 2455.16] Yeah.
[2455.48 → 2456.58] I mean, you're still exploring.
[2456.92 → 2458.42] I mean, you're pre-1.0,
[2458.42 → 2460.42] so it's not as if...
[2460.42 → 2464.46] You know, you even say on the top of your homepage,
[2464.96 → 2468.22] you know, we mentioned the bounty source,
[2468.32 → 2469.92] but that you're raising money,
[2469.98 → 2472.14] you can help fund it and become production-ready.
[2472.36 → 2474.20] So that means that you're still exploring,
[2474.30 → 2477.16] you're still kind of identifying where you're trying to go as a language.
[2477.46 → 2480.20] So to me, if someone's using it or adopting it,
[2480.26 → 2483.30] they can sort of take on those same risks.
[2483.52 → 2484.86] If you're going to use it for something,
[2484.86 → 2487.96] then you understand that things may or will change
[2487.96 → 2489.44] and you have to be okay with that.
[2489.82 → 2490.34] Yeah, that's true.
[2490.92 → 2493.60] So I went searching a little bit to find the feedback
[2493.60 → 2496.56] on that announcement because it is a big announcement.
[2498.24 → 2500.36] And like you guys said, you know,
[2500.64 → 2503.20] some people are...
[2503.20 → 2503.98] Well, you may not have said this,
[2504.04 → 2505.12] but I was at least thinking of it,
[2505.14 → 2506.32] is you'll have certain people,
[2506.40 → 2506.94] there'll be backlash,
[2507.12 → 2508.66] and there'll be other people that are all for it.
[2508.66 → 2510.58] And for the most part,
[2510.64 → 2512.80] it seemed like, somewhat surprisingly to me,
[2512.86 → 2516.04] it seems like most of the response was relatively positive.
[2516.78 → 2518.46] So that's probably great to see.
[2518.54 → 2521.72] There was, you know, some sad voices out there.
[2521.82 → 2523.90] So we need to take another break.
[2524.88 → 2525.84] But on the other side,
[2525.88 → 2528.90] I want to at least bring up one kind of contrary opinion
[2528.90 → 2531.50] to this move with the new compiler
[2531.50 → 2533.42] and see if you guys can, you know,
[2533.42 → 2534.54] your thoughts on that opinion.
[2534.94 → 2537.86] So we'll do that right after we hear from the sponsor.
[2537.86 → 2538.56] Be right back.
[2540.18 → 2541.14] Here at the Change Law,
[2541.24 → 2543.82] we have two emails we'd love for you to subscribe to.
[2543.90 → 2545.88] The first is Change Law Weekly.
[2546.38 → 2548.48] Now, we've been shipping this email for several years now.
[2548.58 → 2550.28] We ship it every single Saturday morning.
[2550.86 → 2553.52] It's everything that hits our open source radar.
[2553.66 → 2556.82] It's our editorialized take on what happened this week
[2556.82 → 2559.50] in open source and software development.
[2559.82 → 2563.12] Go to changelaw.com slash weekly to subscribe.
[2563.74 → 2566.14] And our second email is Change Law Nightly.
[2566.14 → 2568.10] Every single night we ship this email out
[2568.10 → 2571.96] covering all the top new and top star repos on GitHub
[2571.96 → 2574.80] at 10 p.m. Central Time.
[2575.42 → 2577.98] It's all the latest stuff on GitHub before it blows up.
[2578.06 → 2579.40] It's often our own radar.
[2579.80 → 2582.92] We're often creating shows and finding new people,
[2583.06 → 2584.04] finding new projects,
[2584.18 → 2585.26] putting things on our own radar
[2585.26 → 2586.78] based on what we find in there.
[2587.28 → 2588.82] So we'd love for you to subscribe to that.
[2588.92 → 2591.00] Head to changelaw.com slash nightly.
[2591.00 → 2592.68] And now back to the show.
[2595.96 → 2596.66] All right.
[2596.72 → 2598.94] We are back talking about the future of Crystal
[2598.94 → 2602.08] and the newly announced rewrite of the compiler.
[2602.80 → 2604.36] Guys, like I said before the break,
[2604.74 → 2608.14] mostly solid reaction from your users
[2608.14 → 2609.80] and your community about this decision.
[2610.02 → 2611.46] Seems like the right way forward.
[2611.62 → 2613.66] But as is always on the internet,
[2613.72 → 2615.06] there are some dissenting opinions.
[2615.06 → 2618.80] And unfortunately, I have copy and pasted one into my notes,
[2619.02 → 2624.20] which is really the only bad response out there.
[2624.34 → 2626.06] But I just want to see if you guys can address this.
[2627.66 → 2629.46] Anonymous, I'll leave it anonymous, says,
[2629.86 → 2632.58] sorry, but this is a huge damper on the appeal of Crystal.
[2633.24 → 2636.42] It's Ruby-like syntax and being mostly typeless
[2636.42 → 2637.60] was a differentiator.
[2637.60 → 2640.86] I suspected the types on array and hash
[2640.86 → 2643.16] would eventually be solved and removed.
[2643.56 → 2646.04] Going the opposite way removes much of the differentiation
[2646.04 → 2648.28] and puts it into a class
[2648.28 → 2651.50] of a number of new LLVM-based languages
[2651.50 → 2654.54] of which there are no shortage of.
[2655.40 → 2656.82] I'm assuming all negative responses
[2656.82 → 2658.14] are kind of in that same vein.
[2658.74 → 2661.00] So I just was curious about your thoughts,
[2661.16 → 2662.66] your reaction to that reaction.
[2663.74 → 2666.48] Of course, it's a reaction.
[2666.48 → 2669.46] I don't know if we don't like it,
[2669.56 → 2672.60] but we also agree on that reaction
[2672.60 → 2677.36] because maybe since we are so similar to Ruby
[2677.36 → 2678.24] in many things,
[2678.98 → 2683.18] people expect things to go closer to Ruby.
[2683.50 → 2684.60] But I don't know.
[2684.68 → 2689.04] I think it's not that of a big change.
[2689.58 → 2694.62] And it's true that there are many other LLVM-based languages
[2694.62 → 2695.30] out there.
[2695.30 → 2698.96] But I think Crystal has many features.
[2699.96 → 2701.92] One of the top features, I think,
[2702.42 → 2706.28] is blocks that are in Ruby and in Crystal.
[2706.50 → 2708.54] And I don't know if there are many other languages
[2708.54 → 2710.36] that have blocks.
[2710.92 → 2712.24] You can have closures,
[2712.42 → 2713.38] but it's different
[2713.38 → 2716.04] because you can break or do next
[2716.04 → 2717.72] and other things from a block.
[2717.72 → 2720.34] That makes it a bit different.
[2721.34 → 2726.88] And like many other things that we keep from Ruby,
[2727.56 → 2728.02] I don't know.
[2728.10 → 2733.50] My advice would be to wait and try it out once we finish it
[2733.50 → 2738.30] and to realize that it's not that of a big change
[2738.30 → 2742.96] because most of the time you're writing methods,
[2743.12 → 2743.92] you're writing code.
[2745.30 → 2747.20] For example, someone writes a library
[2747.20 → 2749.32] and you want to use it.
[2750.10 → 2751.84] You don't need to define new types.
[2752.04 → 2754.86] You just write a method, invoke methods,
[2754.86 → 2756.44] and stuff like that.
[2756.88 → 2758.86] And in those cases,
[2758.86 → 2761.32] you don't need type annotations.
[2762.32 → 2764.28] So I don't know.
[2764.34 → 2765.44] I think it's a matter of time
[2765.44 → 2768.52] to see if the reaction
[2768.52 → 2771.90] is just fear
[2771.90 → 2774.52] or something like that
[2774.52 → 2776.68] or it's something that's real.
[2777.92 → 2778.28] Well said.
[2779.12 → 2780.60] Aside from the new compiler,
[2781.88 → 2784.10] what are the other missing pieces?
[2785.10 → 2786.54] I think I mentioned dependencies.
[2786.84 → 2787.84] Maybe you can speak to that one
[2787.84 → 2791.94] before you guys are ready to call Crystal 1.0,
[2792.04 → 2792.76] production ready
[2792.76 → 2795.70] and available for general use.
[2796.06 → 2797.02] What else is missing?
[2798.04 → 2799.10] Well, for 1.0,
[2799.10 → 2803.36] we wanted to have proper support for concurrency.
[2803.36 → 2807.48] That means we want to go multithreaded
[2807.48 → 2811.52] and have a better GC.
[2813.92 → 2816.96] Actually, anything that makes Crystal
[2816.96 → 2819.74] to make better use of your hardware resources.
[2820.30 → 2821.10] Because right now,
[2822.00 → 2824.14] the master version works in a single thread.
[2824.88 → 2830.08] And it works better than a Node.js application,
[2830.08 → 2833.60] but we don't think our goal is
[2833.60 → 2836.54] to be a better language than Node.js.
[2836.72 → 2838.48] We want to make a language that,
[2839.02 → 2842.14] again, makes the best use of your hardware resources.
[2842.48 → 2845.34] So have a good concurrency support.
[2845.58 → 2848.28] That's one of the goals for 1.0.
[2848.28 → 2854.78] And personal is one of my preferred goals.
[2855.78 → 2860.60] Yes, that's one of the goals.
[2860.84 → 2864.40] I think Juan loves concurrency and efficiency,
[2864.82 → 2869.16] especially regarding how much your computer can do.
[2869.16 → 2874.12] Other goals are finishing the documentation,
[2874.84 → 2876.28] which is a huge task,
[2876.44 → 2877.48] not only for the language,
[2877.62 → 2879.02] but also the standard library.
[2880.46 → 2883.12] And then fixing bugs
[2883.12 → 2888.52] and maybe adding some features like,
[2889.34 → 2890.62] we have named arguments,
[2891.00 → 2892.70] but we want to enhance that.
[2892.70 → 2896.98] Maybe some other keywords like retry
[2896.98 → 2900.94] or just small features,
[2901.32 → 2903.60] small language additions.
[2904.66 → 2906.84] But I think that's basically it.
[2907.62 → 2912.16] Those are the main three missing things from Crystal.
[2912.84 → 2915.34] I think I teed up the dependencies' conversation.
[2915.56 → 2917.90] Could you just speak to that specific point?
[2917.90 → 2923.02] Well, we have a dependency manager.
[2923.76 → 2927.72] It was written by Julien Portlier,
[2928.54 → 2931.88] who is also collaborating with us.
[2933.18 → 2934.08] It's working.
[2934.20 → 2935.38] You can use it right now.
[2935.90 → 2937.00] It's decentralized.
[2938.14 → 2940.54] But we want it to be,
[2940.96 → 2943.40] like we don't want to have a central registry.
[2944.20 → 2945.64] And even though it's working,
[2945.64 → 2948.38] we want to continue a bit of work there
[2948.38 → 2951.72] to make sure it scales
[2951.72 → 2954.96] without needing a central registry.
[2955.30 → 2959.10] But in a way that you can still find things that you want.
[2959.76 → 2962.66] Maybe Juan can say something about that
[2962.66 → 2965.14] because he's also really interested in that.
[2966.16 → 2968.90] I can explain why we don't want
[2968.90 → 2972.60] a centralized repository of dependencies.
[2973.06 → 2973.88] Yeah, when Aria said that,
[2973.96 → 2975.26] that's what perked up in my ears.
[2975.26 → 2978.28] Why not a centralized repository for them?
[2979.16 → 2979.90] Well, the thing is,
[2980.00 → 2983.58] sometimes I think something that happens
[2983.58 → 2986.34] with the gems and the Ruby Gems repository
[2986.34 → 2991.84] is that someone takes some specific name
[2991.84 → 2996.50] for a library that have a very specific purpose.
[2996.88 → 2997.74] For example,
[2998.24 → 3000.70] you're going to make a Postgres driver.
[3000.70 → 3003.80] So someone creates the library
[3003.80 → 3005.60] and of course they name it Postgres
[3005.60 → 3006.94] and they publish it.
[3007.22 → 3010.26] And maybe then they abandon the library.
[3010.52 → 3013.84] Or maybe someone else comes with a better approach
[3013.84 → 3015.18] for making the same library.
[3015.48 → 3016.68] But the name is already taken,
[3016.78 → 3019.44] so you have to start using names like Postgres true.
[3019.94 → 3021.68] And someone has to know
[3021.68 → 3024.24] that the right version of the library
[3024.24 → 3027.56] is the one with the two or something like that.
[3027.56 → 3028.36] So instead of that,
[3028.40 → 3029.68] we want to make sure that
[3029.68 → 3033.22] there is no central,
[3034.02 → 3035.60] a common namespace
[3035.60 → 3036.86] that we want to,
[3037.24 → 3038.42] that we have to share
[3038.42 → 3039.98] and be the first
[3039.98 → 3041.96] to register
[3041.96 → 3042.98] and the name
[3042.98 → 3044.38] before other
[3044.38 → 3046.42] makes a worse library
[3046.42 → 3047.30] with the same name,
[3047.42 → 3047.78] you know.
[3047.78 → 3049.06] I remember when you looked up
[3049.06 → 3050.36] on rubygems.org too,
[3050.64 → 3050.96] you know,
[3050.98 → 3051.88] in the same vein of like
[3051.88 → 3053.74] if you had an idea for a gem,
[3053.80 → 3055.54] I remember Jared back in the day
[3055.54 → 3056.58] when Wynn was on this call,
[3056.66 → 3057.10] still yet,
[3057.28 → 3058.50] in the changelog.
[3059.68 → 3060.84] He's an API junkie
[3060.84 → 3061.48] and he would always,
[3061.88 → 3062.40] at the time,
[3062.46 → 3064.08] he was like writing Ruby wrappers
[3064.08 → 3065.22] for everything he could think of.
[3065.32 → 3065.86] It was LinkedIn,
[3066.08 → 3067.30] it was Cloud,
[3067.40 → 3067.76] it was this,
[3067.84 → 3068.26] it was that.
[3068.64 → 3069.46] And I can remember
[3069.46 → 3070.54] how excited he would get
[3070.54 → 3073.32] if he like searched for XYZ
[3073.32 → 3073.96] on Ruby Gems
[3073.96 → 3074.76] and it wasn't available
[3074.76 → 3075.16] and it would say,
[3075.16 → 3075.36] hey,
[3075.48 → 3076.28] make this yours.
[3076.28 → 3078.20] So in that same rut,
[3078.22 → 3078.90] I can kind of see
[3078.90 → 3080.04] coming from the roots
[3080.04 → 3082.32] of Crystal with Ruby
[3082.32 → 3083.30] and,
[3083.44 → 3084.42] you know,
[3084.48 → 3085.20] but to me,
[3085.28 → 3086.78] I'm wondering if that's a
[3087.06 → 3087.44] you know,
[3087.46 → 3088.98] I get the concern for that
[3088.98 → 3090.80] and maybe I'm taking it further
[3090.80 → 3091.34] than it should be,
[3091.40 → 3093.08] but I wonder if that should just be
[3093.08 → 3094.06] like the community thing
[3094.06 → 3095.82] and not like a repository thing
[3095.82 → 3096.16] because,
[3096.16 → 3097.86] you know,
[3097.92 → 3099.14] NPM is pretty huge
[3099.14 → 3100.94] and they've not had to deal
[3100.94 → 3101.84] with stuff like that.
[3102.00 → 3102.10] Like,
[3102.62 → 3103.42] in the end,
[3103.42 → 3104.92] the community will resolve
[3104.92 → 3107.24] who the canonical version is
[3107.24 → 3108.50] or what the best version is
[3108.50 → 3109.04] just by,
[3109.14 → 3110.78] you know,
[3111.06 → 3112.28] dependencies in other libraries
[3112.28 → 3114.80] rather than trying to solve it
[3114.80 → 3116.96] at the package manager level,
[3117.02 → 3117.50] so to speak.
[3118.18 → 3118.38] Yeah.
[3118.64 → 3118.88] And,
[3118.92 → 3119.18] and,
[3119.38 → 3120.90] and the truth is
[3120.90 → 3121.72] at the end,
[3121.80 → 3123.74] we probably don't have control
[3123.74 → 3124.30] about that
[3124.30 → 3125.34] and we don't want
[3125.34 → 3125.96] to have control.
[3126.06 → 3126.30] We may,
[3126.40 → 3127.78] maybe we can
[3127.78 → 3130.10] give some ideas
[3130.10 → 3130.76] to the community
[3130.76 → 3131.86] about how we think
[3131.86 → 3132.96] this will work,
[3133.04 → 3133.74] but we don't want
[3133.74 → 3136.10] to have the final decision
[3136.10 → 3137.28] and maybe someone comes
[3137.28 → 3138.86] with a better solution
[3138.86 → 3140.92] and we focus on the language.
[3141.02 → 3141.68] Someone else focus
[3141.68 → 3142.84] on the dependency manager
[3142.84 → 3144.70] and if it works better
[3144.70 → 3146.04] than what we thought,
[3146.32 → 3146.94] that's good.
[3147.42 → 3148.62] How are they handled right now?
[3148.70 → 3149.90] Is there any dependency
[3149.90 → 3150.72] management whatsoever
[3150.72 → 3151.28] right now?
[3151.80 → 3152.02] Yes,
[3152.04 → 3152.38] it is.
[3152.46 → 3153.44] It's called Shards.
[3153.72 → 3153.94] Okay.
[3153.94 → 3155.18] And it,
[3155.34 → 3156.56] right now it works
[3156.56 → 3158.80] with GitHub repositories.
[3159.16 → 3159.50] Okay.
[3159.66 → 3162.24] So it's using version repos
[3162.24 → 3162.64] or,
[3162.64 → 3163.04] you know,
[3163.12 → 3163.92] Git-based repos
[3163.92 → 3165.66] versus like a central repository.
[3166.34 → 3166.76] Exactly.
[3166.94 → 3167.08] Yeah.
[3167.12 → 3168.18] It uses the tags
[3168.18 → 3169.66] as versions.
[3169.98 → 3170.26] Gotcha.
[3171.00 → 3172.00] Let's talk about getting started.
[3172.10 → 3173.12] I know we've talked deeply
[3173.12 → 3173.56] about,
[3173.84 → 3174.24] you know,
[3174.34 → 3176.10] the various ins and outs
[3176.10 → 3178.42] of the living in the shadow
[3178.42 → 3178.84] of Ruby,
[3178.92 → 3179.38] so to speak,
[3179.38 → 3180.20] and growing up
[3180.20 → 3181.84] and hopefully becoming a 1.0
[3181.84 → 3183.28] and all the other things
[3183.28 → 3185.52] around Crystal language.
[3186.18 → 3187.06] Someone's out there listening,
[3187.22 → 3188.34] let's say they're new to it.
[3188.42 → 3189.28] They love Ruby.
[3189.42 → 3190.16] This is the first time
[3190.16 → 3191.22] they're hearing about Crystal.
[3191.86 → 3192.48] What do they do?
[3192.54 → 3193.24] How do they get started?
[3193.36 → 3194.50] How do they play with it?
[3194.56 → 3195.86] What's the very first things
[3195.86 → 3196.46] they can do
[3196.46 → 3198.20] to sort of test the water,
[3198.28 → 3198.76] so to speak?
[3199.34 → 3199.50] Well,
[3199.54 → 3200.46] right now we support,
[3200.60 → 3202.38] we have installers
[3202.38 → 3206.32] for Debian-based Linuxes
[3206.32 → 3209.90] and also Red Hat-based Linuxes.
[3210.40 → 3212.08] And also we have
[3212.08 → 3213.84] an official package
[3213.84 → 3214.68] in Homebrew.
[3215.18 → 3215.98] So the first thing
[3215.98 → 3216.44] you have to do
[3216.44 → 3217.04] is installed it.
[3217.14 → 3218.24] So we already
[3218.24 → 3219.50] provide packages
[3219.50 → 3221.38] for most of the platforms
[3221.38 → 3222.54] that we could support.
[3223.38 → 3224.54] And if you're using Homebrew,
[3224.64 → 3226.16] I like the flag
[3226.16 → 3226.62] you have there
[3226.62 → 3227.46] with LLVM,
[3227.54 → 3228.00] so if you're planning
[3228.00 → 3228.86] to contribute back
[3228.86 → 3229.34] to the project
[3229.34 → 3230.24] and you're using Homebrew,
[3230.46 → 3231.84] is that the same option
[3231.84 → 3232.42] on Arch Linux
[3232.42 → 3233.86] and the other options
[3233.86 → 3234.64] you can still
[3234.64 → 3236.18] pass a flag to,
[3236.26 → 3237.48] or do you get the LLVM
[3237.48 → 3238.16] by default
[3238.16 → 3239.46] on other package,
[3239.70 → 3240.08] I guess,
[3240.08 → 3240.94] not using Homebrew?
[3241.76 → 3242.06] No,
[3242.12 → 3243.06] unfortunately on Linux,
[3243.90 → 3244.68] the package is,
[3245.24 → 3247.00] maybe we need someone
[3247.00 → 3247.80] that understands
[3247.80 → 3249.00] a lot more than us
[3249.00 → 3249.94] about how to make
[3249.94 → 3250.72] a proper package
[3250.72 → 3251.78] to the different
[3251.78 → 3252.76] Linux distributions.
[3252.96 → 3253.08] But,
[3253.44 → 3253.70] you know,
[3253.78 → 3255.72] maintaining Linux packages
[3255.72 → 3257.40] is a big task,
[3257.40 → 3259.04] so maybe someone
[3259.04 → 3260.50] can help us with that.
[3261.16 → 3261.28] Well,
[3261.28 → 3262.02] we have a question
[3262.02 → 3263.00] coming up at the end
[3263.00 → 3263.94] that will probably help
[3263.94 → 3265.22] highlight some of those things,
[3265.40 → 3265.56] but,
[3265.62 → 3265.92] okay,
[3266.00 → 3267.14] so you've got
[3267.14 → 3267.90] different packages
[3267.90 → 3268.78] on Debian,
[3268.96 → 3269.28] Red Hat,
[3269.40 → 3269.82] Arch Linux,
[3270.38 → 3272.04] using Homebrew for Mac,
[3272.70 → 3273.36] and then you even
[3273.36 → 3273.90] have a tarball
[3273.90 → 3274.82] if you want to compile
[3274.82 → 3275.94] or pull down the source
[3275.94 → 3277.14] or from the source itself.
[3277.24 → 3278.12] You can go
[3278.12 → 3278.78] any of those directions.
[3278.96 → 3279.32] So what's,
[3279.66 → 3280.60] is there a web option
[3280.60 → 3281.62] if someone wanted
[3281.62 → 3282.24] to go and plug
[3282.24 → 3283.00] something into the web
[3283.00 → 3283.50] and not have to
[3283.50 → 3284.50] actually install locally?
[3285.28 → 3286.04] Is there an option
[3286.04 → 3286.50] for the web?
[3286.50 → 3289.24] There's play.crystallang.org
[3289.24 → 3291.04] Nice.
[3292.26 → 3293.10] Where you can,
[3293.60 → 3294.90] the best thing is that
[3294.90 → 3296.52] all of these tools
[3296.52 → 3297.16] like shards
[3297.16 → 3299.18] and play.crystallang.org
[3299.18 → 3301.80] weren't made by us.
[3302.32 → 3303.46] That's why I say
[3303.46 → 3303.96] it's amazing,
[3304.08 → 3304.24] like,
[3304.24 → 3305.58] people started evolving
[3305.58 → 3306.08] the language
[3306.08 → 3307.02] and the tools
[3307.02 → 3308.20] around it.
[3309.02 → 3310.08] So you can,
[3310.16 → 3310.36] yes,
[3310.40 → 3311.58] you can try code
[3311.58 → 3312.42] there
[3312.42 → 3314.24] in several versions
[3314.24 → 3314.92] of the language.
[3314.92 → 3318.04] and run it.
[3318.26 → 3318.46] Don't,
[3318.46 → 3319.12] don't try to run
[3319.12 → 3320.38] an HTTP server,
[3321.06 → 3321.34] but
[3321.34 → 3323.34] anything else?
[3323.84 → 3324.48] You know,
[3324.54 → 3324.90] and the
[3325.14 → 3326.18] we also mentioned
[3326.18 → 3326.68] at the top
[3326.68 → 3327.48] of your homepage,
[3327.48 → 3328.48] you've got
[3328.48 → 3329.66] fund crystal
[3329.66 → 3330.58] and help it
[3330.58 → 3331.44] become production ready.
[3331.56 → 3332.24] So we've mentioned
[3332.24 → 3333.62] at least in happenstance
[3333.62 → 3333.94] your,
[3334.02 → 3334.78] your bounty source,
[3334.88 → 3335.08] which
[3335.08 → 3336.62] to this date,
[3336.74 → 3337.98] $4,531
[3337.98 → 3339.00] have been raised.
[3339.00 → 3340.24] So each month
[3340.24 → 3340.46] you're getting
[3340.46 → 3341.44] around $1,100
[3341.44 → 3342.32] of support.
[3343.62 → 3344.52] We didn't go
[3344.52 → 3345.22] deeply into this,
[3345.28 → 3346.32] but it seems like
[3346.32 → 3347.68] the roots of,
[3347.68 → 3348.32] of crystal
[3348.32 → 3349.50] and at least
[3349.50 → 3349.96] the
[3349.96 → 3350.78] the motivations
[3350.78 → 3351.28] of it
[3351.28 → 3352.18] have some
[3352.18 → 3352.84] tie back
[3352.84 → 3353.24] to
[3353.24 → 3355.12] your company,
[3355.34 → 3355.52] Manu's.
[3355.62 → 3356.58] So you guys
[3356.58 → 3357.26] are both developers
[3357.26 → 3357.68] there,
[3358.28 → 3359.72] co-founder to a degree,
[3360.12 → 3360.82] CTO,
[3361.14 → 3362.22] early in the call
[3362.22 → 3362.58] you mentioned.
[3362.74 → 3363.08] So what,
[3363.18 → 3364.20] what is,
[3364.36 → 3364.96] what's happening
[3364.96 → 3365.64] with bounty source?
[3365.74 → 3366.20] How can people
[3366.20 → 3366.92] step in and,
[3366.92 → 3367.36] and I guess,
[3367.40 → 3367.88] support this?
[3367.88 → 3368.60] Is it one just,
[3368.70 → 3369.42] uh,
[3369.42 → 3370.44] financially supporting it?
[3370.50 → 3371.38] Is there other ways
[3371.38 → 3372.30] to step in and support
[3372.30 → 3372.92] crystal language
[3372.92 → 3373.64] moving forward
[3373.64 → 3374.92] to become fast
[3374.92 → 3375.46] to see and look
[3375.46 → 3375.86] like Ruby?
[3376.58 → 3377.32] So basically,
[3377.74 → 3378.34] uh,
[3378.78 → 3379.90] most of the time
[3379.90 → 3380.56] we spend,
[3380.58 → 3381.38] uh,
[3381.94 → 3382.64] doing crystal
[3382.64 → 3382.98] is,
[3383.08 → 3383.32] uh,
[3383.32 → 3384.06] our free time
[3384.06 → 3385.78] and
[3385.78 → 3387.56] as the project,
[3387.68 → 3389.20] project gets bigger,
[3389.20 → 3389.76] uh,
[3389.76 → 3390.72] there are more tasks
[3390.72 → 3392.74] and we'd really
[3392.74 → 3393.90] want to do it,
[3393.90 → 3394.56] uh,
[3395.68 → 3396.98] not in our free time.
[3396.98 → 3398.36] Uh,
[3398.36 → 3399.16] so,
[3399.52 → 3400.04] bounty source
[3400.04 → 3400.44] is,
[3400.44 → 3400.82] uh,
[3400.82 → 3401.40] one way,
[3402.14 → 3402.38] uh,
[3402.38 → 3403.38] one of the best ways,
[3403.88 → 3404.16] uh,
[3404.16 → 3405.02] you can help us
[3405.02 → 3406.00] to make that possible
[3406.00 → 3408.18] because we can work
[3408.18 → 3408.92] like,
[3409.48 → 3410.46] at work time
[3410.46 → 3412.08] and fully motivated
[3412.08 → 3412.84] and not tired
[3412.84 → 3413.52] from work.
[3414.36 → 3414.88] Um,
[3415.42 → 3416.28] but there are many options
[3416.28 → 3417.04] to contribute,
[3417.04 → 3417.42] like,
[3417.60 → 3417.96] uh,
[3417.96 → 3418.76] if you send,
[3418.76 → 3419.24] um,
[3419.24 → 3419.90] bug fixes
[3419.90 → 3421.18] or documentation,
[3421.18 → 3422.34] which is,
[3422.34 → 3422.60] uh,
[3422.60 → 3422.94] lacking
[3422.94 → 3424.44] and,
[3424.44 → 3425.56] uh,
[3425.56 → 3426.22] also additions
[3426.22 → 3426.90] to the standard
[3426.90 → 3428.40] library that you think,
[3428.72 → 3428.94] like,
[3428.98 → 3430.60] those are great ways
[3430.60 → 3431.14] to contribute
[3431.14 → 3432.62] because the less
[3432.62 → 3432.94] we,
[3433.24 → 3434.86] we need to do
[3434.86 → 3436.26] or we rely on the community,
[3436.26 → 3436.90] uh,
[3437.00 → 3437.48] the better.
[3438.16 → 3438.62] Well,
[3438.66 → 3438.90] fellas,
[3438.96 → 3439.54] it was definitely
[3439.54 → 3441.08] a fun time here
[3441.08 → 3441.88] talking with you
[3441.88 → 3443.28] about this language
[3443.28 → 3443.82] and obviously
[3443.82 → 3444.84] you've got some roots
[3444.84 → 3445.20] in Ruby
[3445.20 → 3446.04] but you're spreading
[3446.04 → 3447.28] your own wings
[3447.28 → 3448.70] and making your own path
[3448.70 → 3449.24] so it's always
[3449.24 → 3450.54] a fun direction to go.
[3450.54 → 3451.22] you know,
[3451.24 → 3451.34] we,
[3451.34 → 3452.02] we love having
[3452.02 → 3452.86] new languages,
[3452.86 → 3453.42] uh,
[3453.42 → 3454.42] here on the Change Log
[3454.42 → 3455.10] and always getting
[3455.10 → 3455.68] a deep dive
[3455.68 → 3457.26] into what you all are doing.
[3457.42 → 3458.00] Is there anything else
[3458.00 → 3458.82] you guys want to cover
[3458.82 → 3460.62] before we tail off the show?
[3460.78 → 3461.30] Anything else?
[3462.48 → 3463.30] I don't know.
[3463.46 → 3464.22] I don't think so.
[3464.66 → 3465.00] We,
[3465.06 → 3465.38] uh,
[3465.44 → 3466.12] enjoyed having you
[3466.12 → 3466.88] on the show today.
[3467.30 → 3467.86] Thank you so much
[3467.86 → 3468.56] for joining us
[3468.56 → 3469.72] and all listeners
[3469.72 → 3470.42] out there listening,
[3470.62 → 3471.82] thank you for tuning in as well
[3471.82 → 3472.36] but,
[3472.46 → 3472.62] uh,
[3472.62 → 3473.34] that's it for now
[3473.34 → 3474.04] so let's say goodbye.
[3474.70 → 3474.96] Bye.
[3475.10 → 3475.86] Thanks for coming on, guys.
[3476.10 → 3476.36] Okay.
[3476.50 → 3476.96] Thank you.
[3477.52 → 3477.84] Bye.
[3480.54 → 3500.06] Outro Music
[3507.32 → 3510.52] Outro Music
[3510.54 → 3540.52] Thank you.

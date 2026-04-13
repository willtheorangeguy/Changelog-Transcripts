[0.00 → 4.00] They look at what are the real problems that Gophers are having, and then they try to make
[4.00 → 6.16] it so that the Go tool can solve those problems.
[6.32 → 7.74] So we mentioned modules before.
[7.74 → 11.94] That was a real problem people were having of like, how do we incorporate open source
[11.94 → 18.22] software into our programs, into a way where we know what version we're getting in and
[18.22 → 20.66] what versions are coming out and all that works.
[21.08 → 24.78] And so this is another one where people have been doing lots and lots of tools over the
[24.78 → 29.00] years, including Packer and Go bind data and static and blah, blah, blah.
[29.00 → 30.04] The list goes on.
[30.40 → 32.26] And now we have it built into the Go tool.
[32.46 → 36.34] And so I think for those of us who have been using those tools, it's very exciting to see
[36.34 → 36.88] it built in.
[39.24 → 41.82] Bandwidth for Changelog is provided by Vastly.
[42.14 → 44.02] Learn more at Fastly.com.
[44.26 → 46.54] Our feature flags are powered by Launch Darkly.
[46.80 → 48.62] Check them out at LaunchDarkly.com.
[48.84 → 50.72] And we're hosted on Leno cloud servers.
[51.12 → 54.64] Get $100 in hosting credit at Leno.com slash Changelog.
[55.36 → 56.22] What's up, Gophers?
[56.22 → 61.14] This episode is brought to you by Modish, a podcast from the team at Heroku, exploring
[61.14 → 63.90] code, technology, tools, tips, and developer life.
[64.30 → 67.66] There's a ton of great episodes on the Modish podcast, so I'd encourage you to check it out
[67.66 → 68.20] and subscribe.
[68.34 → 72.12] But in particular, I want to bring to your attention the recent episode featuring Cornelia
[72.12 → 76.40] Davis, the CTO of WeWork's, talking about cloud native, cloud native patterns, and what
[76.40 → 78.88] it really means to be a cloud native application.
[79.26 → 79.86] Here's a sneak peek.
[80.26 → 81.96] Can you define Git Ops?
[82.30 → 85.54] Maybe give a formal definition and talk about what some of the implications are?
[85.54 → 91.88] I think that the simplest formal definition actually doesn't involve the word Git at all.
[92.18 → 95.44] It is cloud native operations is the way that I think of it.
[96.00 → 101.18] Now, let me draw an analog there in that one of the things I didn't mention in my intros
[101.18 → 104.26] that I'm also the author of a book called Cloud Native Patterns.
[104.26 → 110.84] And that book is targeted at developers, software developers and architects who are building these,
[110.90 → 115.76] you know, highly distributed applications, these microservice based applications and helping
[115.76 → 121.12] them understand all the patterns that you have to put in place to be able to make these
[121.12 → 126.30] microservices based apps work in this ever-changing environment that they run in.
[126.30 → 126.84] All right.
[126.88 → 130.42] Links are in the show notes or head to heroku.com slash podcast.
[130.54 → 131.38] Listen to subscribe.
[131.64 → 135.86] Again, check the show notes for links or heroku.com slash podcasts.
[135.86 → 155.38] Let's do it.
[155.94 → 157.02] It's go time.
[157.02 → 159.18] Welcome to go time.
[159.18 → 162.50] Your source for diverse discussions from around the go community.
[162.70 → 165.90] Thank you to Giuseppe Maria for requesting this episode.
[166.06 → 166.96] We hope you enjoy it.
[167.20 → 171.66] If this is your first time listening, be sure to follow the show on Apple podcasts or Spotify.
[172.06 → 177.20] Check out the deep back catalogue at go time.fm and join in the conversation on Twitter.
[177.34 → 179.06] We are at go time.fm.
[179.32 → 179.82] Okay.
[180.82 → 181.66] Here we go.
[181.66 → 192.40] Hello and welcome to go time.
[192.40 → 198.10] I'm Matt Raya and I think you should be able to paste without formatting by default.
[198.76 → 204.76] I don't think I should have to contort my hand into some kind of copy and paste claw in order
[204.76 → 207.64] to get the text not matching the source formatting.
[207.74 → 208.48] I've never wanted it.
[208.48 → 213.36] I believe that same key gesture is actually the Emacs one for save.
[214.12 → 214.74] Oh, well then.
[215.76 → 219.00] That's just a disaster waiting to happen, isn't it?
[219.94 → 221.38] Luckily, I use VS Code.
[222.14 → 226.98] Well, that voice you heard preemptively before his introduction, which is strictly against
[226.98 → 228.14] the rules, but there we go.
[228.64 → 230.08] They give you a sense of the man.
[230.96 → 231.44] It's...
[231.44 → 232.14] Oh, hi, Mark.
[232.38 → 233.44] It's Mark Bates.
[233.84 → 234.38] Hey, everyone.
[234.70 → 236.02] The man, the myth, the legend.
[236.58 → 236.86] Yeah.
[236.86 → 237.94] Well, you're a man, aren't you?
[238.06 → 238.34] Definitely.
[238.80 → 239.64] One out of three.
[239.76 → 241.42] No, I'm definitely a myth, actually.
[241.82 → 242.28] Oh, yeah?
[242.50 → 243.04] I'm pretty...
[243.04 → 243.80] I'm all myth.
[244.74 → 245.58] Just all myth.
[245.84 → 248.14] Well, hopefully we have some real people here too.
[248.56 → 249.42] Let's meet them.
[249.68 → 252.96] We're joined by Wayne Ashley Berry.
[253.40 → 253.72] Hello.
[253.96 → 256.64] Wayne is a principal engineer at GoDaddy.
[256.98 → 258.74] And Wayne, you're an artist, right?
[258.80 → 259.42] Welcome to the show.
[259.78 → 260.80] Thank you for having me.
[261.12 → 264.88] A long time listener and very excited to be on the show.
[265.28 → 265.90] You're very welcome.
[265.90 → 267.44] What sort of art do you do?
[267.44 → 270.60] I started drawing, and then I got into computer graphics.
[271.18 → 273.00] And it was all downhill from there.
[273.08 → 275.74] And that's actually what got me into programming in the first place.
[276.16 → 277.24] So that's why I'm here.
[277.96 → 278.62] Very cool.
[279.32 → 281.08] Well, hopefully we get to see some of that.
[281.16 → 282.46] Not on a podcast, obviously.
[282.46 → 285.80] But maybe you share your Twitter handle in the show notes.
[286.38 → 288.88] We are also joined by Carl Johnson.
[289.36 → 296.82] Carl is a software engineer with a PhD in philosophy and is the director of technology for Spotlight, PA.
[297.42 → 298.12] Is that right, Carl?
[298.30 → 298.88] Welcome to the show.
[299.00 → 299.20] That's right.
[299.70 → 300.00] Hi.
[300.34 → 301.20] Thanks for having me.
[301.50 → 302.32] No, thanks for coming.
[302.70 → 305.44] Today we're talking about Go Embed.
[305.44 → 308.36] This is a new thing that came in Go 1.16.
[308.92 → 311.74] And it lets you put files inside the binary.
[312.46 → 314.94] But why would you want to do such a thing?
[315.46 → 316.20] Tell us, somebody.
[316.72 → 318.76] Why wouldn't you want to do such a thing?
[319.06 → 320.14] Why is it useful then?
[320.66 → 321.54] Yeah, that's a great question.
[321.54 → 325.32] We've been doing it for years in a variety of ways.
[325.48 → 327.38] So it's really nice that we finally had this.
[327.54 → 333.54] This problem of wanting to do this, and I'll get to why we want to do it, has been here since the very beginning.
[333.74 → 338.90] So this is my little preamble to say I'm super excited about this release.
[339.10 → 340.80] And I'm super excited for embedding.
[341.26 → 342.74] Because why do we want to do it?
[343.10 → 345.80] We want to do it for so many different reasons, right?
[346.56 → 349.44] The one that everybody usually talks about is web apps.
[349.74 → 350.98] We want to build web apps.
[351.04 → 351.90] What do web apps have?
[351.94 → 352.66] They have images.
[352.80 → 353.54] They have style sheets.
[353.62 → 354.20] They have JS.
[354.42 → 356.14] They have templates, right?
[356.18 → 362.60] And wouldn't it be nice if all of that was self-contained, and we didn't have to have all those files on disk?
[363.18 → 364.54] We didn't have to manage that problem.
[364.88 → 366.48] And that's one of the reasons why, right?
[366.48 → 368.76] That's kind of the use case scenario.
[368.76 → 375.46] And when I first started doing Buffalo way back, I talked about how it was extracted from a real project.
[375.80 → 381.84] And embedding those files into that binary was part of that original project.
[381.84 → 385.22] Because they needed to be able to ship one binary that had everything.
[386.24 → 389.18] And so, like I said, this is a problem we've had as a community.
[389.62 → 392.06] And this goes any kind of application.
[392.06 → 393.58] But the canonical one is the web.
[394.76 → 395.12] Yeah.
[395.22 → 396.12] So, that's the point then.
[396.20 → 401.86] You get to put files that otherwise you have to corral and manage and remember to deploy alongside the binary.
[402.08 → 404.24] You get to put them inside the binary.
[404.96 → 406.12] Is it just for deployment?
[406.24 → 407.50] It makes deployment easier?
[407.70 → 410.26] Is that really the main reason why you do it?
[410.26 → 413.56] That's certainly the biggest reason, right?
[414.54 → 421.68] Because, you know, again, over the years we've had different solutions that have made the problem either kind of cumbersome or transparent.
[422.46 → 424.76] Some required you had to always compile in.
[424.82 → 426.56] And now that's a cumbersome thing.
[426.66 → 430.80] And that's kind of doing that because you need that advantage of probably deployment.
[431.10 → 433.74] Thankfully, the new solution, like a lot of the other ones, is transparent.
[433.74 → 439.16] So, yeah, you want to be able to deploy having that easy to ship binary.
[439.38 → 445.08] And whether it be to your web service or to your customers, like you can just package one thing.
[445.14 → 449.74] It has all your migration files, like just everything nice and tightly packed.
[450.16 → 451.54] It's just simpler and cleaner.
[451.66 → 452.54] It's just one thing.
[453.50 → 460.22] Well, another example is the Hugo static site generator, which was created by Steve Francia.
[460.46 → 462.70] That has internal templates.
[462.70 → 468.78] So it's a tool for creating your own website, and you give it your templates and tell it how to make your website.
[468.92 → 471.10] But it also has some internal templates.
[471.56 → 477.86] And right now, if you look at the source code for it, they have like the HTML files in one part.
[477.86 → 481.38] And then they have a Go file that is essentially the exact same file.
[481.40 → 484.32] And it has like a comment at the top saying auto-generated, do not edit.
[484.32 → 493.80] And they just have to keep them in sync that whenever the internal file changes, they change the Go file to match it.
[494.82 → 499.32] Do they probably have some kind of script or something that does that for them automatically, right?
[499.64 → 501.82] They have a Go generate script that does that.
[501.82 → 507.78] So that's an example where the Hugo binary is just one file.
[507.90 → 509.32] It's just a single executable.
[509.46 → 511.72] You can get it for Mac or Windows or Linux.
[511.90 → 514.18] And it has everything it needs in it.
[514.62 → 525.58] And so then that means that they have to go through this kind of annoying build process where they take these templates that they want to ship with it and turn them into Go code so that they can put it into the binary.
[525.58 → 528.62] Yeah. Buffalo, same thing, right?
[528.68 → 534.60] Anything that generates your code, that does like code generation, has their own templates that they need to ship.
[534.64 → 535.78] And it's a real pain.
[536.16 → 541.92] But that problem you were just talking about keeping those Go files in sync was such a pain.
[542.76 → 547.04] Because, you know, if you think about it, the only way you can get those files in is you have to create Go files.
[547.04 → 556.76] And so you need to either keep those Go files constantly in sync, like you said, on disk, so that if somebody does a Go get, they're going to get the embedded files.
[557.10 → 566.34] You know, or you have to set up the expectation that if you want the embedded files, you have to run this build script to get those files.
[567.00 → 569.20] You know, and that was a real pain too.
[569.32 → 571.20] In this new system, you don't have that.
[571.26 → 574.18] It's just like Go modules, much more streamlined.
[574.18 → 580.14] So, Wayne, have you used other solutions to solve this problem before Go embed?
[581.78 → 583.96] Packer and Packager as well.
[584.18 → 584.90] Never heard of those.
[585.34 → 585.98] I've heard of those.
[586.28 → 588.80] I think someone on this call might have heard of them.
[589.32 → 589.48] Yeah.
[589.64 → 595.72] And I'm sure the maintainer is happy that this is when 16 has come out and doesn't have to maintain any of that anymore.
[596.02 → 601.86] Well, that's true, though, because you really don't now have to build any more of these things again, Mark, right?
[601.92 → 602.14] Yeah.
[602.22 → 603.50] And it's not just me.
[603.50 → 607.06] I mean, like I said, this is a problem the community has been facing for years.
[607.58 → 611.12] Go bin data, static, you know, go rice.
[611.24 → 613.00] The lists go on and on and on.
[613.16 → 615.98] And those are just the ones, like, that we kind of know about.
[616.06 → 617.44] There have been so many over the years.
[617.60 → 619.50] And then I'm sure people have written their own.
[620.42 → 621.44] I definitely have.
[621.48 → 624.02] I've done it where I just needed an HTML file.
[624.02 → 627.36] And I start with just having a coast in the Go code.
[627.58 → 627.90] Right.
[627.90 → 630.30] But then they don't get any help with the IDE or anything.
[630.30 → 633.46] So then I had a separate HTML file.
[633.58 → 634.90] And then the little build script.
[634.96 → 636.14] I couldn't just do go build.
[636.34 → 641.76] I have to then run some of the things first that would do basically that thing that we talked about that Hugo was doing.
[641.76 → 647.10] But with Go embed, you can just use normal build tool chain, right?
[647.76 → 647.98] Yeah.
[648.16 → 653.34] There's a saying in architecture that you should pave the grass.
[653.44 → 653.72] I don't know.
[653.78 → 655.44] Maybe somebody knows the saying better.
[655.80 → 661.06] But the idea is, right, if you have a campus of some sort, like a college campus or whatever, and you have different buildings,
[661.36 → 664.30] and you're thinking about where should I put the sidewalks for it?
[664.68 → 666.82] Well, one way to do it is you just sort of guess.
[667.08 → 670.18] I guess people are going to want to go from building one to building three a lot.
[670.26 → 671.46] So let's build a sidewalk there.
[671.46 → 676.86] But another way to do it is you just put out a big grassy field, and you leave that for a year.
[676.98 → 681.94] And then you come back, and you see, oh, well, people are always walking from building three to building four.
[682.14 → 684.70] And I can see that because the grass is completely worn over.
[684.82 → 687.06] And I'm going to turn that into the sidewalk.
[687.48 → 694.74] And I think the Go team has been perfect about paving the grass, like paving, I don't know how to say this,
[694.84 → 698.18] but paving the areas that people are actually using, paving the footpaths.
[698.18 → 699.40] Is that the phrase for it?
[699.40 → 703.34] Because they look at what are the real problems that gophers are having,
[703.44 → 706.74] and then they try to make it so that the Go tool can solve those problems.
[707.14 → 708.54] So we mentioned modules before.
[708.68 → 713.74] That was a real problem people were having of like, how do we incorporate open source software
[713.74 → 719.46] into our programs, into a way where we know what version we're getting in
[719.46 → 722.06] and what versions are coming out, and all that works.
[722.06 → 726.90] And so this is another one where people have been doing lots and lots of tools over the years,
[726.96 → 731.30] including Packer and Go bind data and Static and blah, blah, blah.
[731.52 → 732.56] The list goes on.
[732.66 → 734.76] And now we have it built into the Go tool.
[734.96 → 739.58] And so I think for those of us who have been using those tools, it's very exciting to see it built in.
[740.04 → 743.64] Yeah, I think for me, this reminds me of when I started using Go.
[743.64 → 747.06] And you get this promise of a single tool chain.
[747.40 → 750.22] There's a built-in command for compiling, for testing.
[750.98 → 757.08] You get that single static binary that I've actually sent some binaries to people over Slack before.
[757.54 → 759.78] It's actually quite useful.
[760.48 → 764.82] Instead of email, you just embed the message in a binary just to use the feature.
[765.36 → 766.04] It's a nice idea.
[766.04 → 766.16] Exactly.
[767.36 → 770.80] And now it's kind of, you know, you start using Go, and then you realize,
[770.94 → 773.42] oh, I actually need these HTML files.
[773.54 → 774.54] I need these CSS files.
[774.62 → 778.30] And you start to lose sight of that simple deployment mechanism.
[778.80 → 781.36] And now we're back at that place where you don't need to figure out
[781.36 → 783.80] which tool do I need to use to embed files.
[784.00 → 785.36] Everyone can use the same tool.
[785.82 → 787.38] You can have standards across projects.
[787.38 → 793.52] And it's that true kind of original promise of Go that everyone's got these same tools that just work.
[795.00 → 795.80] That's great.
[796.04 → 797.40] What about secrets?
[797.80 → 801.94] Should you use Go Embed for embedding secret things in binaries?
[802.42 → 807.72] Or do you have to just assume that people are going to be able to still see them, see that content?
[808.60 → 811.64] I think you always have to assume that people can see everything.
[813.00 → 813.48] Yeah.
[813.48 → 820.00] If you're doing it as like, just I want to send this off to my server, I suppose it would be fine.
[820.76 → 823.34] As long as, you know, you keep the binary secret.
[823.34 → 832.28] If you're shipping it out to clients, clients could easily decompile the binary and remove the secret and spread it on the dark web.
[832.28 → 837.00] So it's probably not a good use case for that.
[837.22 → 840.24] It just depends on exactly what the nature of the secret is.
[840.24 → 840.84] Yeah.
[840.84 → 840.92] Yeah.
[841.06 → 851.48] One use case that you could use it for, kind of secret thing, is maybe an application that has the license built in for a particular client.
[852.48 → 852.92] Right?
[853.04 → 855.40] Where the worst thing that they're going to do is deconstruct the license.
[855.64 → 857.10] But, you know, pull it out.
[857.10 → 859.20] But it's going to be hitting a license server anyway.
[860.46 → 862.76] So if they mess with it, it's just going to break their binary.
[863.16 → 863.48] Yeah.
[863.84 → 865.60] So that's one kind of thing.
[865.72 → 871.66] Plus, you can have the Go tags that build the binary to that client's license model as well, right?
[872.02 → 872.26] Yeah.
[872.30 → 878.46] A similar issue that I've run into is trying to include the build version in a binary.
[878.46 → 881.52] So there are a couple different ways that you can do that.
[881.70 → 889.14] One way is if you use the Go linker, if you send a certain command to it, you can say, here's a string variable in my binary.
[889.30 → 890.46] Replace it with this.
[890.96 → 898.62] And so you can write a little script that says, when you build my binary, replace version string with the git hash that I want to have in there.
[898.62 → 905.14] The problem with that is that now you're really dependent on this script for anything to build your project.
[905.28 → 907.78] Otherwise, they just get like a blank string there.
[908.46 → 917.74] So another way that you could do this with Go embed is you could have the git hash written out to a simple text file called version.txt.
[918.16 → 925.00] And it could either be like a human-friendly version, like 1.2.3, or it could be a git hash or whatever you need.
[925.00 → 926.80] And then you can embed that in your binary.
[927.10 → 934.94] And when you're shipping it out and the client says, it's not working for me, you can say, well, run command-v and let me know what the version is.
[935.02 → 936.82] And then I'll tell you why it's not working.
[937.78 → 940.38] So Go embed works by putting files in.
[940.50 → 943.98] You can't, like with Go generate, run executables.
[944.14 → 945.26] You can't run a script or anything.
[945.26 → 952.28] No, but what Carl was just saying, one of the things about Go embed, and we haven't really talked too much about how it works.
[952.28 → 955.16] But it has basically two concepts.
[955.26 → 960.14] You can have a file system, which as you can imagine is a collection of files.
[960.76 → 965.96] And then you can also embed stuff directly to a string or a slice of bytes.
[966.28 → 968.04] Oh, so that's very interesting.
[968.04 → 972.12] So Carl's example, you could have a version string just like you do now.
[972.92 → 980.30] But you can use Go embed to embed the version number into that string or a slice of bytes directly.
[981.24 → 985.18] Yeah, I guess you'd still need to run a script before to prepare that other file.
[985.18 → 991.50] But it saves you from messing around with those fiddly flags, the linter flags or the linker flags that you have to pass in.
[991.64 → 997.56] Yeah, and the nice thing there is that you'll get a compiler error if the file that you expect isn't there.
[997.56 → 1009.20] As opposed to, you know, LD flags or some other hacky solution where sometimes you just get a silent error, and then you've shipped a binary with no version information in it at all.
[1010.08 → 1011.26] Yeah, that is very good.
[1011.62 → 1015.60] Someone needs to write a blog post about the modern way of solving that problem.
[1015.68 → 1016.74] I do it every time.
[1016.82 → 1018.28] I do it using those LD flags.
[1018.72 → 1020.22] That's how I've been doing it for years.
[1020.34 → 1020.62] Yeah.
[1020.74 → 1020.94] Same.
[1021.54 → 1022.84] I set the default to dev.
[1022.86 → 1024.62] I read my own blog post.
[1024.62 → 1033.48] I have to Google myself and then find my blog post that says what the LD flags are and look them up and just copy and paste and hope that I got it right when I wrote it.
[1033.74 → 1035.60] I think everybody copies and pastes.
[1035.60 → 1039.88] We all have one that we wrote somewhere for ourselves.
[1039.90 → 1041.74] We just copy and paste it around.
[1042.36 → 1047.40] We've actually got an internal command that generates the parameters for that flag.
[1047.76 → 1051.46] So you just pipe the output from that command into the go bold.
[1051.46 → 1054.60] Yeah, I see.
[1054.64 → 1055.08] This is great.
[1055.16 → 1058.24] We have all these old hacky solutions we could start getting rid of now.
[1058.24 → 1072.94] This episode is brought to you by our friends at Equinix Metal.
[1073.22 → 1075.96] Globally interconnected, fully automated bare metal.
[1076.32 → 1080.96] Equinix Metal gives you hardware at your fingertips with physical infrastructure at software speed.
[1081.36 → 1086.38] Accelerate your workloads with fully automated bare metal that's secure, powerful, and cost-effective.
[1086.38 → 1090.02] This is the promise of the cloud delivered on bare metal.
[1090.40 → 1097.74] Equinix Metal makes it easier than ever to take advantage of the unmatched global reach and connectivity ecosystem made possible by Equinix,
[1097.86 → 1102.98] which includes more than 220 data centres across 63 metros, making interconnection easy.
[1103.30 → 1106.24] And they're obsessed with making bare metal even more awesome.
[1106.62 → 1107.88] Seriously, check out these features.
[1107.88 → 1119.58] 60 Second Deployed, hourly pricing, a customer success team that engages over Slack, x86, Intel, AMD, and ARM, single tenant, NVMe and SSD storage,
[1119.94 → 1128.66] RESTful API, first class DevOps integrations, Equinix fabric integration, support for enterprise OSes and open source Linux OSes,
[1128.90 → 1136.70] air-gapped installs without a public IP, no installed agent or keys, extensive open source love and support, plus so much more.
[1136.70 → 1139.68] Visit info.equinixmetal.com slash changelog.
[1139.74 → 1141.84] Get $500 in free credit to play with.
[1142.14 → 1145.08] Again, info.equinixmetal.com slash changelog.
[1145.08 → 1167.08] Okay, so maybe we could explore a little bit more than about how Go Embed works.
[1167.08 → 1170.32] It's a kind of special comment, isn't it?
[1170.34 → 1171.86] And this is unusual in Go.
[1172.18 → 1179.98] It's one of the unusual things, I think, of the design, where specific comments have special meaning.
[1180.84 → 1183.02] Go generates another one, and there are build tags.
[1183.58 → 1185.90] But how does that actually, how does it work?
[1185.96 → 1190.12] How would you use Go Embed if you wanted to bring in a file into a string?
[1190.12 → 1196.80] It's actually quite pleasant and easy, fairly straightforward to use.
[1196.92 → 1197.94] I always say hesitant.
[1198.20 → 1203.10] I never want to say the word easy or simple because it's never that.
[1203.10 → 1208.80] Matter of fact, I struggled with trying to figure out how to embed files by an extension.
[1209.38 → 1210.20] And I'll say that in a minute.
[1210.20 → 1221.54] So basically what you do is you set up the variable you want to embed into, whether it's a string, a slice of bytes, or an embed.FS variable.
[1221.62 → 1223.14] Those are your kind of three choices.
[1224.00 → 1230.24] Somebody please stop me if I forgot one, but I'm pretty sure those are your three choices that you can put this directive above.
[1230.46 → 1234.94] So you get your little Go colon embed directive, and then you tell it what kind of files you want.
[1234.94 → 1244.50] And those files, and this is, as somebody who's written these systems, this is what I love, those files that you're asking for are relative to the source code.
[1245.36 → 1248.22] So there's this kind of consistency to it.
[1248.22 → 1262.50] If I'm in cmd slash foo slash main.go, and I reference templates slash CSS, it's going to expect templates to be right next to main.go and so on, right?
[1262.50 → 1270.08] And that sort of resolution can be really tricky to do if you don't have the Go tooling behind you.
[1270.20 → 1274.86] Like if you're not in the Go tooling, if you have to do it all after market, because those are the kind of problems you do.
[1275.28 → 1277.80] And it works for, like I said, all three of those.
[1277.88 → 1280.54] And you can do, you know, I want templates.
[1280.66 → 1282.70] So I can do templates slash star.
[1282.80 → 1285.48] So there's a wild card you can use.
[1285.62 → 1288.88] And you can also, you know, star.css, for example.
[1288.88 → 1295.78] What I, the struggle I came into was I had assets slash CSS slash and then a bunch of CSS files.
[1295.88 → 1300.42] And I just did, for my embed directive, assets slash star.css.
[1301.38 → 1303.34] So it was only looking in the one directory.
[1303.44 → 1308.16] So I needed another star, another slash to kind of recourse through all that.
[1308.18 → 1309.84] But once I figured that out, it was great.
[1309.84 → 1316.12] The gotcha there is that Go has a built-in pattern matching.
[1316.50 → 1319.06] It's in file path.match.
[1319.62 → 1322.06] And it kind of stinks, to be honest.
[1322.90 → 1329.18] It's not, I mean, it's fine for what it is, but it's purposefully very simple in the way that a lot of Go tools are.
[1329.18 → 1332.26] And so it doesn't support star.
[1332.64 → 1344.60] So if you're familiar with a lot of the JavaScript asset building tools, they'll have, you know, star slash star dot CSS will mean any CSS file anywhere underneath this particular path.
[1344.76 → 1348.04] And the Go file path matcher does not have that.
[1348.14 → 1352.04] It only supports a single star in a particular location.
[1352.04 → 1365.16] So if you say, go embed assets slash star dot CSS, it'll get any CSS files you have that are in the assets' folder, but not in the CSS folder that's underneath assets.
[1365.66 → 1367.78] So it's a little bit of a gotcha.
[1368.18 → 1368.92] Yeah, that's interesting.
[1369.06 → 1371.56] I kind of, I don't mind that though.
[1371.86 → 1379.04] Well, like I said, you could do that star, you could do an intermediate star, just the one star, and then it'll do all folders.
[1379.84 → 1381.72] Even no matter how deep they are?
[1382.04 → 1383.18] I don't know about that.
[1383.54 → 1384.68] Well, here's the thing though.
[1385.10 → 1389.08] In a way, it's better that it's just really clear and obvious.
[1389.22 → 1392.82] And if you want to embed more things, you have different, you know what I mean?
[1392.82 → 1408.52] It's almost like it would be hard to find what you were looking for potentially if you had lots of CSS files and a big directory structure with CSS files, say they're named the same, separated only by path, which happens if you've got theming and things sometimes.
[1408.90 → 1408.96] Yeah.
[1409.20 → 1410.00] It'd be tricky.
[1410.00 → 1415.16] The thing for me, I was like actually trying to, I had like nested JS files.
[1415.26 → 1420.88] I had a vendor directory, you know, and trying to find the files in the vendor directory.
[1421.20 → 1422.46] That's where I kind of ran into that problem.
[1422.52 → 1424.28] But it was such a simple thing.
[1424.28 → 1425.78] It is very basic.
[1426.10 → 1427.18] It is very simple.
[1427.74 → 1440.62] But what I was amazed at is my editor, I use Neovim with Vigo, and I was getting, I get Covet warnings if my pattern is wrong, if the files don't exist.
[1441.18 → 1442.56] Oh, nice.
[1442.56 → 1443.82] That's interesting.
[1443.82 → 1444.12] Yeah.
[1444.44 → 1449.46] So right there in my editor, I was getting a nice little warning saying, oh, that pattern doesn't work.
[1450.70 → 1451.48] That's nice.
[1451.56 → 1453.06] And it would be a build error too, right?
[1453.06 → 1453.30] Yeah.
[1454.02 → 1454.48] Yeah.
[1454.84 → 1455.08] Yeah.
[1455.14 → 1455.84] I believe so.
[1456.02 → 1456.14] Yep.
[1456.68 → 1456.86] Yeah.
[1456.96 → 1458.08] See, that is nice.
[1458.92 → 1468.02] Actually, I forgot that you can also specify multiple directories and multiple patterns if you're embedding into a file system.
[1468.02 → 1477.42] So my first take at this, I would have, you know, var CSS and embed the CSS directory in there and then var images and put images in there.
[1477.62 → 1482.36] But then you can actually just have var static and just embed everything in there.
[1482.88 → 1486.60] You just need to remember that they still exist in their directories.
[1486.92 → 1491.20] So you need to reference HTML slash index dot HTML.
[1492.08 → 1492.22] Yeah.
[1492.38 → 1494.36] So that's actually a perfect way to do it.
[1494.36 → 1512.08] So if you have var static or var FS, and then you say in the go embed comment above it, go embed assets slash CSS slash star dot CSS space assets slash JS slash star dot JS and then images and so forth.
[1512.12 → 1514.82] And you can put it all into a single file system that way.
[1515.32 → 1516.06] That's cool.
[1516.88 → 1517.02] Yeah.
[1517.12 → 1523.44] And you can also, if that line starts getting too long because it's just space separated, you can use multiple lines.
[1523.44 → 1524.28] Oh, really?
[1524.56 → 1525.46] I didn't know that.
[1525.46 → 1530.98] So you can have multiple go embed directives above the variable declaration.
[1531.62 → 1536.80] So you can do it really nice and, you know, one kind of line if you've got maybe two things, three things.
[1537.06 → 1540.00] But after that, you can put a nice even ordered list.
[1540.10 → 1542.32] You know, you can sort it and just make it all look nice, right?
[1542.44 → 1543.60] So that's really nice, too.
[1543.66 → 1547.72] So you can build up your static very deliberately that way.
[1547.72 → 1548.82] Just in a hurry.
[1548.82 → 1555.00] If you just do go embed assets, it will embed almost everything in the assets recursively.
[1555.00 → 1559.24] The things that it doesn't embed are dot files.
[1559.32 → 1562.04] So files that begin with dot, which you would kind of expect.
[1562.04 → 1565.56] It also doesn't embed files that begin with underscore.
[1566.62 → 1571.58] And the logic behind this is that Go will not compile files that begin with underscore.
[1571.58 → 1577.16] So if you have underscored my file dot Go, it will just be ignored by the Go compiler.
[1577.30 → 1580.74] I think that's a little bit weird, to be honest, the logic behind it.
[1580.74 → 1591.44] But if you find that that's a problem, if you explicitly name your underscore files or if you say assets slash underscore star, that's a way of working around that.
[1592.02 → 1592.10] Yeah.
[1592.20 → 1596.54] That pattern of using underscore file names is very common in the Ruby on Rails world.
[1596.74 → 1597.08] Yeah.
[1597.18 → 1598.68] For doing partials.
[1599.50 → 1604.96] So anybody who's kind of brought that theory over, that's a great little gotcha.
[1604.96 → 1612.36] I didn't know that, well, I didn't make that connection that it would do something like that, like throw away an HTML file that began with an underscore.
[1613.10 → 1617.80] If you say templates slash star dot HTML, it will include the underscore file.
[1617.98 → 1618.64] It's the default.
[1618.92 → 1625.26] If you just say embed templates, and you think, OK, now it's going to embed everything in templates and all the subdirectories of templates.
[1625.80 → 1630.16] Fortunately, it's the kind of error that you'll notice as soon as you try to use the partial, and it's not there.
[1630.54 → 1630.90] Yeah.
[1630.98 → 1634.42] Oh, here's, this is actually a really great segue to the tooling.
[1634.42 → 1640.46] The Go tooling will tell you what it expects to embed in your code.
[1640.82 → 1651.50] So if you run go list dash JSON, it's going to spit out kind of a JSON kind of build some basic kind of module and package information.
[1651.68 → 1654.12] And in that, it's going to be all the files it's going to embed.
[1655.64 → 1656.28] So if you, you know.
[1656.28 → 1659.00] Wasn't there a similar command in Packager where you could.
[1659.18 → 1659.38] Yeah.
[1659.46 → 1660.20] Packager list.
[1660.20 → 1661.52] Packager list and then see.
[1661.52 → 1661.88] Yeah.
[1662.18 → 1666.08] And I use that all the time because sometimes files would just disappear.
[1666.38 → 1669.56] And in your CI, you need to see what's actually going on.
[1669.94 → 1671.54] So that's a really nice way.
[1671.62 → 1675.06] And you can, obviously, you could test against that if you wanted to.
[1675.06 → 1679.24] But then you start testing against the language too, I think.
[1679.46 → 1683.40] But the tooling has kind of shows you that information.
[1683.54 → 1685.22] So if you are like, what is happening?
[1685.38 → 1687.74] What is actually being put in here?
[1688.68 → 1690.82] You don't have to go digging through debug logs.
[1690.92 → 1694.06] You can just quickly run go list dash JSON.
[1694.60 → 1696.72] Those are the six files it's embedding.
[1696.72 → 1699.34] I thought it was supposed to be embedding 106 files.
[1700.12 → 1701.28] My pattern's wrong.
[1702.30 → 1704.74] I'm missing a whole folder of stuff, right?
[1705.22 → 1709.70] So it helps you immediately jump back to where that problem is.
[1710.24 → 1714.52] It is interesting how in Go, generally, it's a very simple language.
[1715.06 → 1716.16] There's very little magic.
[1716.72 → 1721.50] But then sometimes you get these opinions baked in to the language.
[1721.50 → 1725.06] So, you know, automatically excluding files starting with an underscore.
[1725.46 → 1728.92] If you don't know about that, then it's not very clear.
[1729.16 → 1733.46] And it seems a little, feels a bit more like a framework than a language sometimes.
[1733.86 → 1738.32] Because, you know, the Go authors have taken opinions.
[1738.78 → 1743.18] And generally, I find it's best to just lean into them and enjoy them.
[1743.56 → 1746.44] And it just keeps everything nice and simple and clear.
[1747.00 → 1749.46] But you do need to figure out what those opinions are.
[1749.46 → 1751.92] That's a perfect way to put it.
[1752.40 → 1752.54] Yeah.
[1753.06 → 1754.36] Yeah, it's polite, wasn't it?
[1756.36 → 1757.52] Well, here's one.
[1757.90 → 1760.30] And we're not at the unpopular opinion section yet.
[1760.36 → 1765.10] But if you thought that the comments to magic comments in Go was weird,
[1765.56 → 1769.38] what's going on with this underscore import for embed?
[1769.56 → 1771.78] You have to import underscore embed.
[1771.78 → 1783.54] The reasoning behind this is that they don't want somebody who's using Go 115 or below to accidentally try to build something that requires an embed.
[1783.90 → 1785.42] And it looks like it works.
[1785.64 → 1787.82] And then you go to run it, and it doesn't actually work.
[1787.82 → 1794.34] And so to get around this, they require you to import the embed package anytime you use an embed.
[1794.74 → 1802.68] But if you're just embedding a file as a string or embedding a file as a slice of bytes, you don't actually use the embed package.
[1802.68 → 1806.90] So to get around this, you do import underscore embed.
[1807.26 → 1811.98] And that tells it, okay, I'm using the embed feature in this file.
[1812.16 → 1814.16] So make sure that it's available.
[1814.54 → 1820.66] But it's another one of those things where if you don't understand why it's there, it just sort of looks bizarre.
[1820.82 → 1825.38] Like I have to include this import that doesn't do anything for no reason.
[1825.90 → 1826.02] Yeah.
[1826.32 → 1827.54] But there is a reason.
[1827.54 → 1830.62] Well, we do that already in several places in Go.
[1830.78 → 1840.54] The registration of a database package is kind of a great way, a great example of that where they're doing it for the side effect.
[1840.70 → 1844.08] Now, we could argue whether they should be doing it for the side effect or not.
[1844.20 → 1844.78] We can't.
[1844.88 → 1845.62] They shouldn't.
[1845.84 → 1847.06] I've got my opinions.
[1847.64 → 1854.50] But the side effect is it gets registered to a global map when that happens, right, that driver.
[1854.50 → 1860.58] So there is precedent in the standard library for that type of technique.
[1861.02 → 1862.96] Doesn't necessarily mean I like it.
[1863.62 → 1875.16] This is even stricter than that, though, because with the database example, you only have to import it in your package main or import it one place in your entire program.
[1875.16 → 1886.34] But with this, every time you embed into a particular string or slice of bytes, you have to make sure that the import of embed is there or else it will say, you didn't import embed.
[1887.04 → 1889.64] See, that doesn't bother me too much.
[1889.78 → 1890.42] Yeah, I quite like that.
[1890.42 → 1895.68] As somebody who's, again, written these types of tools, I also look at that as a marker.
[1896.42 → 1901.60] Like, before I go and start parsing this whole go file, are they even using the package?
[1902.18 → 1905.20] If they're not using embed, why should I bother to parse this?
[1905.98 → 1912.66] So that, to me, that is less egregious than, say, the registration of a database driver.
[1912.66 → 1917.28] I tend to put all of my embedded resources in a single file.
[1918.02 → 1924.42] So top level, I have a resources' directory, resources.go, and that's the only place I'll embed anything.
[1924.72 → 1926.86] And then all other packages can import from there.
[1927.26 → 1929.54] They don't need to know about embeds at all.
[1930.02 → 1933.82] But it is one area where I hope that the tooling can maybe get a little bit better.
[1933.82 → 1947.78] Because, you know, if VS Code or Vim or Neovim could detect you're using 1.16, you have a Go embed directive in your code, it could just import that for you as opposed to not.
[1948.46 → 1949.24] I think it will.
[1949.40 → 1954.42] I'm sure Go imports will be updated with that functionality eventually if it hasn't been already.
[1955.24 → 1956.70] Yeah, I think so.
[1956.70 → 1969.14] I once put that to Brad Fitzpatrick about whether just importing a package and relying on the side effect of doing that, whether in retrospect he'd change that.
[1969.56 → 1973.12] And he looked at me in a way that said, yeah, you are the best.
[1974.18 → 1975.44] So, and that's Brad Fitzpatrick.
[1975.44 → 1979.54] I think he had just had some bad lunch, if I remember correctly.
[1979.62 → 1981.48] We had gone out to that really dodgy place.
[1981.66 → 1982.22] That's delicious.
[1983.06 → 1983.66] Yeah, well.
[1986.70 → 1996.94] This episode is brought to you by our friends at Retool.
[1997.30 → 2000.28] Retool helps you build internal tools fast and easy.
[2000.70 → 2005.22] From startups to Fortune 500s, the world's best teams use Retool to power their internal apps.
[2005.60 → 2008.92] Assemble your app in just a few minutes by dragging and dropping from pre-built components.
[2009.24 → 2013.84] Connect to most databases or anything with the rest, GraphQL, or GRPC API.
[2013.84 → 2018.18] Retool empowers you to work with all your data sources seamlessly in one single app.
[2018.52 → 2022.34] Retool is highly hackable, so you're never limited by what's available out of the box.
[2022.64 → 2026.24] If you can read it in JavaScript and in API, you can build it in Retool.
[2026.52 → 2029.68] You can use their cloud service or host it on-prem for yourself.
[2030.16 → 2033.30] Learn more and try it free at retool.com slash changelog.
[2033.58 → 2035.60] Again, retool.com slash changelog.
[2035.60 → 2050.92] Just a quick question, then I'll put this to all three of you.
[2051.48 → 2053.46] What's the best thing you've ever embedded?
[2055.18 → 2056.68] Mark, you can go first.
[2057.60 → 2059.28] Don't laugh away from the mic.
[2059.40 → 2060.06] We need that.
[2060.32 → 2061.26] I really need that.
[2061.26 → 2066.70] The best thing I've ever embedded is an ASCII image of Jim Wei rich.
[2067.50 → 2068.92] Oh, what a great answer.
[2069.36 → 2069.84] Thank you.
[2070.54 → 2072.48] Can anyone beat that as an answer?
[2072.86 → 2079.54] I have a similar answer, but I embedded an image of Pikachu in a test
[2079.54 → 2084.92] because we had an algorithm that was detecting prominent colours from images.
[2084.92 → 2089.80] So I embedded Pikachu in my test so that I could run that through my code.
[2090.84 → 2092.16] That's actually a great one.
[2093.02 → 2096.66] So Matt, you said at the top that I have a PhD in philosophy.
[2096.66 → 2102.38] It doesn't come up in my job very often, but it does for this, which is that I embedded a Quine.
[2102.38 → 2112.56] So a Quine is a kind of computer science joke named for WHO Quine, who was a philosopher, very active in the 60s.
[2112.96 → 2118.80] And it's a thing in computer science where you make a program that embeds itself, that can print itself out.
[2119.82 → 2124.22] And so if you want to make a program that can print itself out, all you have to do is say,
[2124.62 → 2129.80] go embed the name of your file.go and then print out the embed.
[2129.80 → 2133.76] So it's a recursive, it's embedding itself.
[2134.24 → 2135.40] That is amazing.
[2135.56 → 2136.86] That is very meta.
[2137.04 → 2140.92] And I feel like is the start of how Terminator happens.
[2141.56 → 2142.48] Like something like that.
[2142.48 → 2145.24] Yes, it embedded itself and then it just grew too complicated.
[2145.44 → 2148.36] Yes, Go embed is how Skynet starts.
[2148.46 → 2148.68] Yeah.
[2149.02 → 2154.58] Not the Amazon flying drones or any of that stuff, but this.
[2154.70 → 2157.22] It uses the AWS APIs to control those.
[2157.22 → 2159.84] Russ Cox has started Skynet off with the Go embed.
[2160.04 → 2160.68] Thanks, Russ.
[2161.24 → 2162.18] Go generate as well.
[2162.48 → 2170.10] That actually reminds me, there's a was it Russ Cox who did the draft design presentation on YouTube of Go embed?
[2170.64 → 2172.30] This was June last year?
[2172.30 → 2172.88] Yes, I believe so, yeah.
[2172.88 → 2180.22] And one of the first things that he did was embed a file, but in, within a function.
[2181.28 → 2186.54] And it's funny because that was the first thing I tried to do when 1.16 came out, but you actually can't.
[2187.00 → 2187.08] Yeah.
[2187.14 → 2193.62] You have to embed at a package level variable, which I don't know how I feel about, to be honest.
[2193.62 → 2194.06] Yeah.
[2195.20 → 2199.52] Interesting because a lot of us are trying to avoid global state altogether.
[2200.24 → 2204.56] But in a way, is it okay that this breaks that rule?
[2204.56 → 2219.70] So, the original, the very kind of earliest drafts of the proposal, I think even the ones before, kind of they went out to the public kind of thing, circulated around through some of us who had written this kind of packages.
[2219.70 → 2227.74] And that was one of my first comments was, why can't I do it at the function level?
[2227.90 → 2229.80] And I think people are really going to want that.
[2229.90 → 2231.36] And it's definitely going to come up.
[2231.40 → 2233.72] People don't like global, Ada, Ada, Ada.
[2234.24 → 2239.96] And I don't remember quite what Russ's exact issues were or problems with it.
[2239.96 → 2258.04] But he did make very valid points as to, A, both the technical issues around trying to make it work and also the practicality of why you would really want that kind of feature for something that is essentially a global pool, just like your file system.
[2258.92 → 2259.04] Right.
[2259.04 → 2261.64] Your file system is this globally accessible pool.
[2262.24 → 2262.76] Right.
[2262.76 → 2271.28] So, you don't have a separate globally accessible, a separate only pool within this function that doesn't even make sense conceptually.
[2271.90 → 2274.96] So, there was a lot of, he had a lot of interesting takes on it.
[2274.96 → 2283.06] If you get the earliest beta of Go 116, it actually did let you do embeds at the function level.
[2283.06 → 2292.84] But then the problem that people found as they were using it was that if you embedded a slice of bytes, someone could mutate that slice of bytes.
[2293.52 → 2297.28] And it wasn't clear what that should do.
[2297.78 → 2307.98] So, if I have a particular function, let's say that it embeds a file as a slice of bytes, and then someone changes the file, what does that mean?
[2308.12 → 2309.32] What are the semantics of that?
[2309.40 → 2310.64] Should that cause a crash?
[2310.78 → 2311.74] Should that be legal?
[2311.74 → 2314.24] Should it be the same when you rerun the function?
[2314.48 → 2316.18] It was just, it was too confusing.
[2316.44 → 2321.32] And so, then they decided, let's make it so that you can only do embedding at the top level.
[2322.14 → 2326.46] You know, logically speaking, that's the only level where it really makes sense to have embedding.
[2326.98 → 2334.78] And so, because that was the decision, they ended up dropping the feature of letting you do it in the function, which is kind of inconvenient.
[2334.78 → 2337.50] But it goes back to the idea of the Go authors.
[2337.50 → 2341.62] They have very kind of strong opinions.
[2341.88 → 2343.06] It's like not magical.
[2343.36 → 2344.32] It's simple.
[2344.32 → 2347.18] But at the same time, the opinions are very strong.
[2347.36 → 2354.48] And so, the opinion is, if you really need it, you can deal with it being a global and just don't use it wrong.
[2354.48 → 2356.20] But you can still change those.
[2356.30 → 2358.72] It's a variable in global space, right?
[2358.92 → 2359.70] You can change.
[2359.90 → 2365.50] So, in the case of embeds, the FS, you can swap out one FS for another FS.
[2365.76 → 2368.40] But the FSs themselves are read-only.
[2368.74 → 2369.62] They're thread-safe.
[2369.82 → 2372.24] So, they're meant to be used globally.
[2372.82 → 2374.16] And they're also read-only.
[2374.40 → 2376.88] So, you can't kind of mutate them.
[2377.06 → 2380.80] Unless you, like I said, unless you swap out an entire whole new FS.
[2381.62 → 2381.68] Gotcha.
[2381.80 → 2389.42] So, Matt, the issue I think you're talking about is that if you have the slice of bytes, and it's at the top level, you could, of course, change it.
[2389.80 → 2393.98] But if it was in a function, you could change it, and then you would rerun the function.
[2394.30 → 2400.02] And should you get a fresh copy that was the original, or should you get back the embedded one that just got changed?
[2400.02 → 2400.38] Hmm.
[2400.74 → 2407.92] If you're used to C or C-based languages, they have a concept of a static variable where every time you run it, it's the same variable.
[2408.24 → 2410.64] And if you change it, it's the same between runs.
[2410.86 → 2412.50] But there's no such concept in Go.
[2412.76 → 2416.10] So, they would have had to basically invent it for it to make sense.
[2416.60 → 2417.74] Yeah, that does make sense.
[2417.86 → 2419.56] And, you know, I'm kind of with you on this.
[2419.64 → 2421.06] I don't mind these restrictions.
[2421.50 → 2425.30] And it's about really learning the way, the right ways to do things.
[2425.36 → 2426.88] You can always pass arguments around.
[2426.88 → 2432.02] You could always pass a global into some other type or something else if that's what you want to do.
[2432.32 → 2434.20] And that is what is encouraged, by the way.
[2434.72 → 2440.88] You're encouraged to write your functions to take a FS.FS interface.
[2441.38 → 2443.20] So, then you can do that for testing quite easily.
[2443.30 → 2444.24] And then you can do that for testing.
[2444.58 → 2448.92] So, you know, you'd have a global CSS folder, let's say.
[2449.24 → 2452.20] But your function just takes a FS.FS type.
[2452.20 → 2464.62] So, you could pass in that CSS folder, or you can use the map.FS that's in the testing package for, you know, kind of creating your own fictitious file system for testing and just pass that in.
[2464.94 → 2469.66] Or you can write your own interfaces around all of this.
[2470.12 → 2476.40] You know, you can fulfill your own interface, those interfaces and do all sorts of wonderful, interesting stuff in the middle.
[2476.40 → 2483.46] But you're encouraged to take a FS.FS as your function and not refer to the global.
[2484.04 → 2486.46] That's kind of how they're getting around it a little bit too.
[2487.10 → 2489.72] What Mark is saying is there are two different types.
[2490.02 → 2496.16] There's the embed.FS, which is specifically used for embedding these groups of files.
[2496.16 → 2501.62] And now there's a new type called an Io.FS.FS.
[2502.02 → 2507.76] And that is an interface that lets multiple different types implement being a file system.
[2508.46 → 2514.24] So, embed.FS implements this interface, but also zip reader does.
[2514.90 → 2516.98] And also me.FS does.
[2517.38 → 2519.84] And they're working on making it so the tar text.
[2519.84 → 2526.58] So, if you ever are on the Go playground, and you know how there can be multiple files in there, that format is called text.
[2527.48 → 2533.14] That format, they're making a FS.FS implementation for it.
[2533.50 → 2539.76] So, just any different kind of format where you have a bunch of files together, you can make an implementation of FS.FS.
[2540.22 → 2544.52] And if your function or method takes a FS.FS, that can be put in there.
[2544.62 → 2549.46] It doesn't have to be an embed.FS that is hard-coded into the binary.
[2549.46 → 2551.92] It can be anything that you swap out in real time.
[2552.04 → 2553.98] Including the local file system.
[2554.24 → 2555.96] Including the local file system, right.
[2556.10 → 2559.70] There's a helper in the OS package to give you the look.
[2559.82 → 2563.46] I believe it's the OS package, I believe, that gives you the kind of just underlying OS.
[2564.30 → 2571.50] So, if you're just, you know, you're building a tool that's supposed to be looking at the underlying OS, and you're taking a FS, well, you just grab that and kind of pass it along through.
[2571.62 → 2577.58] So, that begs the question, do you think that should be bested practice if you're going to work with files in the local file system?
[2577.58 → 2581.50] Should we just use FS now and just use that abstraction because it's more versatile?
[2581.50 → 2583.66] Or would you still just use OS open?
[2584.32 → 2589.22] I'm planning on using it, to be perfectly honest, because it does make my testing.
[2590.02 → 2593.44] I write a lot of tooling that deals with the file system.
[2594.04 → 2594.10] Right.
[2594.10 → 2597.60] Everything from generators, transformers, reading and writing.
[2598.14 → 2602.52] The fact that I can just mock up my file system is wonderful.
[2603.34 → 2605.32] Is that interface read-only as well?
[2605.58 → 2607.56] Like the embed file system?
[2608.10 → 2608.34] Yeah.
[2608.54 → 2610.28] It is read-only at this time, yeah.
[2610.56 → 2613.84] Yeah, there's no, you can't add files to it and stuff like that.
[2614.06 → 2620.32] But like I said, there is a testing, in the FS testing package, there's a map FS that you can use for testing.
[2620.32 → 2623.48] So, here's all my different files that I want.
[2623.78 → 2635.74] So, since this happens at build time, is there a way that you can have a situation where you can just be editing the CSS files and just sort of refreshing things in order to see those updates?
[2635.82 → 2637.02] Or do you have to rebuild?
[2638.12 → 2638.58] You know what I mean?
[2638.64 → 2641.52] Like, is there a way to have a sort of passive mode where it will just read?
[2641.76 → 2645.52] Or would you just build that yourself in your particular case?
[2645.52 → 2650.58] So, that's where the FS concept, the FS.FS comes in.
[2650.92 → 2660.32] That you could have in your program, you know, depending on how you do command line arguments and flags and variable variables and whatever it is you do.
[2660.62 → 2665.30] But you could say, if this value is true, then use the embed.FS.
[2665.60 → 2670.96] And if it's false, then use the OS.FS and switch between those two as necessary.
[2670.96 → 2680.12] So, that could be a perfect way for development for things like Buffalo where you want to have things refreshing as the files get changed on disk.
[2680.32 → 2688.46] But then when it's time to build it and ship it either to the server or to the user, you can bake it in and make sure that it's concrete.
[2688.46 → 2695.88] I actually like that that's not the default behaviour because I don't often do that kind of work.
[2696.52 → 2709.08] And I found that with the pre-existing solutions, the third-party tools for doing this kind of thing, I would have so many problems with local file system, embedded files, you know, generated code that's lying around.
[2709.08 → 2716.42] And it would be so difficult to know which files were actually being read that I actually prefer this, that there's one way of doing it.
[2716.84 → 2723.28] You know, the files are always embedded the same way, whether you're running, you know, locally or shipping and deploying it somewhere.
[2723.80 → 2724.96] So, actually, I love this.
[2725.12 → 2734.04] But that interface is incredible as well because now that can kind of just, you know, go through all our libraries and the standard library as well.
[2734.04 → 2737.42] And it can become that common kind of point of abstraction.
[2737.42 → 2737.50] Yeah.
[2739.12 → 2742.12] And it's showing up in a lot of standard libraries places.
[2742.98 → 2747.26] Carl was talking about a bunch, but, I mean, like the HTTP package understands FS.
[2747.88 → 2748.46] What does that mean?
[2748.50 → 2750.72] You know, for doing, serving up static files.
[2751.60 → 2758.98] The templates' directory, a templates package, so you can parse an FS, right?
[2758.98 → 2765.08] So, again, those of us who maybe write code generators, being able to just parse an FS is wonderful.
[2765.08 → 2767.96] You know, there's a lot there.
[2768.70 → 2770.42] You can pipe them through in funny ways, too.
[2770.62 → 2774.18] Like, you could, say, distribute to your client a zip file.
[2774.72 → 2782.26] And then, because the zip file can now be used as an FS, you then turn the zip file into a template file system.
[2782.26 → 2793.26] And so, instead of, like, saying, here's this directory of templates and I need you to unzip it and put it in this particular place, just send them the one file that contains all the templates they need.
[2793.62 → 2797.18] And they can point it at that file and everything will happen automatically.
[2797.84 → 2798.38] Mm-hmm.
[2798.76 → 2800.10] That's good, isn't it?
[2800.88 → 2801.82] That is good.
[2802.10 → 2806.08] That's, you know, finally having interfaces around things like files.
[2806.34 → 2806.94] Yeah.
[2806.94 → 2808.58] That is wonderful.
[2809.60 → 2816.36] Like I said, you know, I don't know about a lot of other Go developers, but I'm constantly working with the file system.
[2816.52 → 2822.16] And I'm constantly trying to take files and process them through a pipeline.
[2822.70 → 2825.58] You know, first I want to convert the markdown to HTML.
[2825.94 → 2827.84] Then I want to run that through a Go template.
[2827.84 → 2838.54] Like, you know, all these sorts of different things or whatever it is, to be able to have interfaces so I can just kind of mutate and pass along a new version of this file down the chain.
[2839.14 → 2840.36] Just wonderful.
[2840.36 → 2840.64] Right.
[2840.98 → 2850.56] I look forward to the cloud providers also implementing it in the clients so that you can just use the file system that's in an S3 bucket or, you know, as a storage is available.
[2850.56 → 2858.44] And that's the other thing, too, is you could write interfaces now for S3 that, you know, they just look like regular files.
[2859.16 → 2867.66] And you can write a file system interface that talks to S3 or talks to a database, right?
[2867.68 → 2872.52] So you can use Postgres now as a virtual file system if you want to.
[2873.18 → 2873.56] Right?
[2873.68 → 2875.60] I mean, you could do all these different things.
[2875.60 → 2885.36] Like I said, you can use S3 as this virtual read-only file systems, but, you know, there's, you know, SQLite if you're doing, say, an embedded kind of thing.
[2886.14 → 2889.98] One of the nice features of Go has always been the IO package.
[2890.28 → 2892.78] When you're a new Gopher, it can be a little bit confusing.
[2893.00 → 2894.24] Like, what is package IO?
[2894.56 → 2896.12] What are these read and write methods?
[2896.46 → 2897.88] Why do I have to do them?
[2897.98 → 2899.68] Why can't I just use, like, a string?
[2899.68 → 2908.82] But when you get to understand them, how they work is basically an IO reader is a read-only file and an IO writer is a write-only file.
[2909.46 → 2913.34] And it lets you abstract away what exactly the file is.
[2913.40 → 2914.46] Is the file on disk?
[2914.60 → 2917.24] Is the file an HTTP response that you're reading?
[2917.58 → 2921.40] Is the file an S3 bucket somewhere that you're reading from?
[2921.40 → 2926.72] And so Go has always had a way of abstracting away an individual file using package IO.
[2926.72 → 2931.88] But now with package IO FS, you can abstract away a file system.
[2932.42 → 2935.70] And so it's not just the one file that you're looking at anymore.
[2936.16 → 2944.18] Because you could always say, you know, I'm getting this IO reader from S3, or I'm getting this IO reader from a zip file or whatever.
[2944.36 → 2946.22] But now you can have a whole system.
[2946.58 → 2949.50] Yeah, but IO readers don't have file sizes.
[2950.12 → 2952.02] They don't have mod times.
[2952.16 → 2953.54] They don't have any of those things.
[2953.54 → 2958.52] Right, so they don't have the properties of an actual file in terms of being a file on disk.
[2958.62 → 2959.50] They don't have a name.
[2959.70 → 2961.10] They don't have permissions.
[2961.80 → 2964.02] Right, and so now we can mock out all of those things.
[2964.40 → 2966.64] Yeah, and that's just super exciting to me.
[2967.70 → 2970.14] But I like to do terrible, awful things with code.
[2970.96 → 2972.18] I've seen some of it.
[2972.56 → 2972.70] Yeah.
[2972.84 → 2973.06] Great.
[2973.24 → 2975.34] Well, what's going to be abstracted next?
[2975.34 → 2976.44] All the things.
[2977.20 → 2982.34] It's actually time, if you check your time pieces, for Unpopular Opinions.
[2983.54 → 2988.42] Unpopular Opinions.
[2988.48 → 2989.34] You know what?
[2989.42 → 2991.18] I actually think you should probably leave.
[2993.68 → 2996.42] Unpopular Opinions.
[3000.20 → 3004.38] Okay, so who's got an Unpopular Opinion for us today?
[3005.04 → 3006.12] Carl, what do you think?
[3006.12 → 3008.62] So this is not really a Go opinion.
[3009.14 → 3014.42] This is more of kind of global open source software opinion I have, which is that there
[3014.42 → 3019.06] should be some sort of system for government funding of open source software.
[3019.78 → 3023.80] So if you think about science, in America we have the National Science Foundation.
[3024.06 → 3025.56] We have the National Institutes of Health.
[3026.06 → 3029.00] For art, we have the National Endowment of the Arts.
[3029.00 → 3031.20] And we have the Corporation for Public Broadcasting.
[3031.20 → 3033.72] So we have these different streams for funding.
[3034.22 → 3038.74] But in terms of open source software, right now there's basically just two ways to do it.
[3038.94 → 3045.42] One is what Go does, which is that there's a corporate sponsor, in this case Google, who
[3045.42 → 3050.24] is putting a lot of money and time into these features.
[3050.54 → 3051.46] So Go embed.
[3051.66 → 3054.48] Russ Cox did most of the actual development work on it.
[3054.48 → 3059.96] And I mean, if you just think about what his time costs, this feature probably costs Google
[3059.96 → 3064.76] somewhere in the ballpark of like $10,000, $50,000, right?
[3065.10 → 3068.46] Like just adding up how much time their engineers have put onto it.
[3068.50 → 3071.24] And that's not counting all the people who contributed to the issues.
[3071.80 → 3074.12] If you added up all that time, it would be even more expensive.
[3074.68 → 3078.58] And then the other way that we fund software is through kind of the Patreon model.
[3079.00 → 3081.48] So there are a couple different projects that are funded that way,
[3081.48 → 3088.46] like the Big programming language, where somebody will either go on Twitch or do something so that
[3088.46 → 3090.46] people are interested in seeing what they're doing.
[3090.60 → 3095.00] And then you give them money to keep them as individuals developing.
[3095.66 → 3099.10] But there's no real government funding of open source software.
[3099.86 → 3101.78] And I think it's something that really would be helpful.
[3102.24 → 3104.44] The pushback that I've gotten on this opinion is like,
[3104.50 → 3107.84] you're saying that the government should pay the left pad guy?
[3107.84 → 3111.38] I think that's a fair criticism.
[3111.88 → 3114.40] But I don't think that that would really happen in practice.
[3114.64 → 3119.60] Because if you look at how science is funded, usually the government will put together some
[3119.60 → 3120.40] sort of grant.
[3120.62 → 3125.98] And the grant will say something like, can you research how to cure the coronavirus?
[3126.88 → 3132.98] And then you go to that grant committee, and you say, I have these scientists working in my team.
[3132.98 → 3135.54] We have this theory about how we could build a vaccine.
[3135.90 → 3141.10] We've done these vaccines in the past that show that we're qualified to do this.
[3141.22 → 3144.28] And they evaluate your grant proposal and give it a score.
[3144.50 → 3147.32] And the proposals that score highest get the actual money.
[3147.84 → 3152.74] So in this case, there would be something like some sort of board of software funding
[3152.74 → 3157.88] where people would look at, oh, Go is a popular programming language.
[3157.88 → 3160.76] It has millions of developers worldwide.
[3161.30 → 3165.68] And they all say that they would be really excited to use this embed feature.
[3166.16 → 3172.34] So why don't we give $10,000, $50,000 to this developer and then get some number of months
[3172.34 → 3177.42] of his or her time, and they can work on the feature so that everyone else can benefit.
[3178.00 → 3181.42] So I think something like that, I don't see it happening anytime soon.
[3181.50 → 3183.34] That's why I'm putting it in unpopular opinions.
[3183.34 → 3188.18] It seems like everybody wants to cut government funding instead of increasing government funding.
[3188.84 → 3193.68] But I think it would really be helpful just to have like this third stream of ways that
[3193.68 → 3198.66] you could fund open source software and prevent, you know, developers from getting burned out
[3198.66 → 3203.74] or the situation where the corporation changes its mind about what it wants to work on and
[3203.74 → 3204.68] it walks away.
[3205.78 → 3206.74] Yeah, very interesting.
[3206.74 → 3211.92] Corey in Slack made the point, which is even the government systems themselves are using a
[3211.92 → 3213.66] lot of open source software.
[3214.14 → 3217.48] And so, you know, they even benefit with directed benefit.
[3217.92 → 3223.82] So I used to work with former guest of the show, Paul Smith at the ad hoc team, and they're
[3223.82 → 3224.20] great.
[3224.44 → 3226.94] They do as much as they can in open source.
[3228.14 → 3232.00] Anything that they can get permission from the government to make open source, basically
[3232.00 → 3232.62] they do.
[3232.88 → 3239.54] But I think that's just one angle of things, which is the angle of when the government builds
[3239.54 → 3242.26] its own software and there's no reason to keep it secret.
[3242.26 → 3244.12] They should probably open source it.
[3244.20 → 3248.82] But then there's another angle, which is for software that isn't necessarily useful to
[3248.82 → 3249.26] the government.
[3249.52 → 3255.28] There should be some way for the open source maintainers to be able to earn a living with
[3255.28 → 3255.48] it.
[3256.16 → 3257.00] Yeah, very interesting.
[3257.10 → 3262.06] We will put this to the public on Twitter polls, which is Go Time's flavour of democracy.
[3262.06 → 3266.78] And we'll find out if that is indeed popular or unpopular, but it's a good one.
[3267.12 → 3269.78] I have a potentially unpopular opinion.
[3270.38 → 3270.68] Okay.
[3270.84 → 3275.00] And it is that we should strive to use as few mocks as possible.
[3275.54 → 3279.00] And the amount of mocks should decrease over time.
[3279.28 → 3280.72] This isn't Go specific.
[3280.90 → 3282.08] It's just programming in general.
[3282.34 → 3287.80] And I actually used the philosophy that I heard from a band member once.
[3287.92 → 3290.62] And he said, you should practice how you're going to play.
[3290.62 → 3290.70] Yeah.
[3291.28 → 3297.00] So, you know, if you practice at home, and you've got your headphones on and your amp is on 2%
[3297.00 → 3303.52] volume, and then you're expected to walk onto stage, turn the amp up to 110%, and all of a sudden
[3303.52 → 3306.36] those skills transfer, that doesn't happen.
[3306.62 → 3312.54] So I think in software, if you're going to run your code against MySQL, then test your code
[3312.54 → 3313.52] against MySQL.
[3314.40 → 3315.84] There are obviously limitations.
[3315.84 → 3322.22] You know if you talk about billing, you don't want to start billing, you know, charging your own credit card or something
[3322.22 → 3322.72] like that.
[3323.10 → 3328.90] But often, you know, those kinds of services will give you emulators that you can run locally, things like that.
[3328.90 → 3341.06] And I find that it's actually been incredibly helpful for me over time because I got to the point where one of the services I've been working on for the past year, I actually haven't run it locally in a year.
[3341.40 → 3343.16] I've only run the tests ever.
[3343.70 → 3348.48] So someone asked me, go run main.go, what environment variables do I have to set?
[3348.98 → 3349.94] And I said, I don't know.
[3350.48 → 3353.80] You just, you know, you go write a test, and you run the test and that's how you know it's going to work.
[3353.80 → 3354.56] Mm hmm.
[3354.88 → 3355.14] Yeah.
[3355.76 → 3356.88] That's very interesting.
[3357.06 → 3359.90] I mean, you know, I do like that point.
[3360.16 → 3361.60] We will test that one, too.
[3361.88 → 3363.56] I never mock my database calls.
[3363.76 → 3364.00] Right.
[3364.06 → 3365.38] You always use a real database.
[3366.02 → 3366.28] Always.
[3366.82 → 3366.98] Yeah.
[3367.28 → 3369.34] Well, how do you consider FS.FS?
[3369.66 → 3371.56] Is that a mock or is that an interface?
[3371.92 → 3381.72] Like if in production you're using the embed FS, but in development you're using the OS.FS, do you consider that a mock or do you consider that something different?
[3381.72 → 3385.38] It's an implementation of an interface.
[3385.52 → 3386.80] Yeah, I can see what you're saying.
[3386.92 → 3387.62] What is a mock?
[3389.04 → 3392.20] It's what Matt does to mark the whole episode long.
[3392.64 → 3392.82] Yeah.
[3392.94 → 3393.92] And vice versa.
[3394.14 → 3396.22] Oh, I have an unpopular opinion.
[3396.72 → 3396.90] Okay.
[3396.94 → 3408.00] Before we do, though, I just want to say Roberto Claps made this point to your point, Wayne, that if you have code that uses random numbers, then your tests should also use random numbers.
[3408.00 → 3415.88] It's kind of common for us to want to control the seed in test code so that you have predictable tests.
[3416.10 → 3419.58] But in a way, that stops it being like the real world a little bit.
[3419.66 → 3422.28] And actually, it'd be better off if you were using random numbers.
[3422.72 → 3427.34] So that's an interesting point that extends to your point, Wayne.
[3428.80 → 3429.02] Yeah.
[3429.28 → 3433.34] If you've got nothing to say about that, then we'll listen to Mark's unpopular opinion.
[3435.30 → 3435.74] Right?
[3435.74 → 3438.92] Mine just popped into my head when we were talking about sandwiches.
[3440.06 → 3441.36] I, I know, right?
[3441.68 → 3444.22] I don't particularly care for bacon.
[3445.30 → 3445.72] Oh.
[3446.24 → 3446.66] Wow.
[3446.86 → 3447.92] You're kicked off the internet.
[3448.28 → 3450.86] I think it's highly overrated, to be perfectly honest.
[3451.04 → 3451.32] Right.
[3451.40 → 3452.18] Very unpopular.
[3452.66 → 3454.82] It's a wildly unpopular opinion.
[3454.98 → 3455.72] I get that.
[3456.36 → 3457.82] What would you rather eat?
[3458.06 → 3461.30] I would rather have sausages instead of bacon with, like, my eggs.
[3462.32 → 3462.68] Right.
[3463.18 → 3463.92] That's fair enough.
[3463.92 → 3465.48] Well, there are different types of bacon, isn't there?
[3465.50 → 3468.86] Because in England, the bacon is very different to, I've had it in the US.
[3468.94 → 3469.52] It is.
[3469.70 → 3469.94] Yeah.
[3470.06 → 3471.22] I don't care for either.
[3471.52 → 3471.78] Yeah.
[3472.14 → 3472.38] Yeah.
[3472.86 → 3473.38] Fair enough.
[3473.94 → 3475.52] I'm just against any kind of bacon.
[3475.76 → 3478.70] If you like really floppy bacon, you want to get yourself to London.
[3478.98 → 3481.10] Because you've got the floppiest bacon in town.
[3481.24 → 3482.06] I mean, in the world.
[3483.10 → 3484.44] So if floppy bacon's your thing.
[3485.14 → 3485.40] Yeah.
[3485.40 → 3488.82] Actually, an American friend of mine ordered a cocktail.
[3489.14 → 3492.46] And I guess in New York, this would be a thing, the normal thing.
[3492.98 → 3494.92] They asked for bacon in the cocktail.
[3495.24 → 3501.88] Which, if you imagine in New York, in a cool place with American style bacon that's like firm and sticks up, you know?
[3501.96 → 3503.28] The big piece of the British.
[3503.28 → 3505.94] A bit of floppy, you can't have that in your drink.
[3506.64 → 3507.66] Honestly, it's horrific.
[3507.88 → 3508.60] It gave me nightmares.
[3509.60 → 3509.80] Yeah.
[3509.88 → 3511.20] They wouldn't do it, but, you know.
[3511.20 → 3513.72] The appeal of that is not nearly as nice.
[3514.00 → 3514.82] But yeah, there you go.
[3514.84 → 3516.00] That's my unpopular opinion.
[3516.52 → 3518.26] Ah, well, we'll see how unpopular that is.
[3518.26 → 3525.76] It's probably not that unpopular with the vegans, but maybe with the carnivore listeners of us.
[3525.88 → 3526.80] Yeah, I think so.
[3527.06 → 3528.56] I do like plenty of other meats, though.
[3529.08 → 3532.38] Ah, well, you know, maybe we should save this for another episode.
[3532.62 → 3533.18] I think so.
[3533.30 → 3534.96] Or Mark just list his favourite meats.
[3535.26 → 3537.00] Favourite kinds of flat meat.
[3538.38 → 3542.46] You only have really, like, charcuterie is fine, because you can slip that under the door.
[3542.46 → 3544.80] But, you know, a juicy rib eye, no chance.
[3545.22 → 3545.68] That's right.
[3547.06 → 3547.46] Yeah.
[3547.84 → 3548.14] Okay.
[3548.24 → 3550.12] Anyone else got anything mental to add?
[3550.28 → 3551.30] Not mental, I shouldn't have said that.
[3551.38 → 3554.56] Anyone else got anything crazy to add?
[3555.26 → 3555.66] No.
[3556.30 → 3556.58] Nope.
[3556.94 → 3557.34] Okay.
[3557.34 → 3562.90] Well, we're running out of time, but, you know, we could just save a few minutes for some light chat.
[3564.34 → 3564.74] Carl.
[3565.14 → 3569.50] Nothing says light chat like telling everybody we're about to have a light chat.
[3569.86 → 3570.14] And go.
[3570.56 → 3572.26] This is the light chat section.
[3572.68 → 3572.84] Yeah.
[3573.54 → 3574.94] Carl, you've got a blog, haven't you?
[3574.98 → 3577.50] Because I've read about how to use Go Embed on your blog.
[3577.82 → 3584.30] What's the internet resource indicator for your, the uniform resource indicator for your blog?
[3584.30 → 3588.10] Uh, blog.carlmjohnson.net.
[3588.20 → 3589.54] That's M as in Matthew.
[3590.02 → 3590.34] Right.
[3590.66 → 3591.78] Is that what your middle name is?
[3591.86 → 3592.96] Oh, and Carl with a C.
[3593.48 → 3594.06] It is.
[3594.28 → 3594.78] Good name.
[3595.02 → 3595.38] Coincidentally.
[3595.90 → 3596.40] Yeah, good name.
[3597.22 → 3599.74] Um, Wayne, your middle name's Ashley, isn't it?
[3599.98 → 3600.72] It is indeed.
[3600.98 → 3603.32] Do you go by Wayne Ashley Berry or just Wayne Berry?
[3603.42 → 3603.74] I do.
[3603.86 → 3605.02] I like using my full name.
[3605.36 → 3606.08] I don't know why.
[3606.16 → 3607.86] I just, you know, it was given to me.
[3607.94 → 3608.80] So why not?
[3609.30 → 3609.52] Yeah.
[3609.64 → 3612.58] I knew I went to school with a kid called Ashley Berry.
[3613.04 → 3615.18] So this is what, that's actually really jarred in my head.
[3615.44 → 3617.02] Um, it was, it was an absolute idiot.
[3617.38 → 3618.94] He tried to set fire to my trousers.
[3619.64 → 3619.96] Oh dear.
[3620.72 → 3625.50] Do one of you three know the most popular Carl Johnson off the top of your head?
[3626.00 → 3627.22] Is it in the Simpsons?
[3628.14 → 3628.84] That's close.
[3629.14 → 3629.32] Hmm.
[3630.44 → 3630.84] No then.
[3630.84 → 3634.36] It is CJ from Grand Theft Auto 3 San Andreas.
[3634.74 → 3636.52] That's his real full name, is it?
[3636.78 → 3637.82] His name is Carl Johnson.
[3637.94 → 3644.58] So if you search for my name without the M, you get pictures of Carl Johnson, you know,
[3644.66 → 3648.52] posing in front of cars in very low polygon resolution.
[3649.30 → 3654.16] What's funny is if you search Mark Bates, you get the same thing, except me posing in
[3654.16 → 3657.12] front of cars in incredibly low resolution.
[3657.74 → 3660.08] With a tank top on and.
[3660.08 → 3660.78] Well, yeah.
[3660.82 → 3662.52] How else are you going to pose in front of a car?
[3663.02 → 3663.74] Goes with that saying.
[3664.84 → 3665.82] And yet we did.
[3666.54 → 3667.76] And yet we did.
[3668.58 → 3673.30] Well, that's all the time we have for today on Go Time.
[3673.84 → 3676.74] But, uh, thanks for listening.
[3676.96 → 3678.28] And also thanks for being on it.
[3678.54 → 3680.12] Mr. Bates, Mark Bates.
[3680.70 → 3681.78] Thank you very much for coming.
[3682.10 → 3683.60] Carl Johnson, you'll have to come back.
[3683.70 → 3683.86] Thanks.
[3683.88 → 3685.46] And also you, Wayne Ashley Berry.
[3685.88 → 3687.48] Please also come back another time.
[3687.56 → 3688.38] It's been great.
[3688.48 → 3689.06] Very informative.
[3689.06 → 3690.02] Thanks for having me.
[3690.56 → 3690.98] Whoa.
[3691.14 → 3691.78] I'm sorry.
[3692.14 → 3692.48] What?
[3692.92 → 3694.54] They got come back any time.
[3694.74 → 3695.18] Yeah.
[3695.78 → 3696.86] Oh, you noticed.
[3697.18 → 3697.88] You noticed that.
[3697.88 → 3699.86] You just kind of like waved me off.
[3700.40 → 3701.80] You're like, thanks for coming, Mark.
[3702.06 → 3702.42] Bye.
[3702.54 → 3704.76] I think it was the bacon comment that did that.
[3704.86 → 3705.02] Yeah.
[3705.02 → 3706.54] Well, no, Matt's a vegan.
[3706.70 → 3709.50] So he's, he's going to be on board with that one.
[3710.04 → 3710.22] Yeah.
[3711.18 → 3711.50] Don't tell everyone.
[3711.50 → 3712.78] Well, there's the fake bacon.
[3713.24 → 3714.54] Do you like fake bacon or no?
[3715.18 → 3720.90] I don't know why we're spending all this science energy trying to make fake meat.
[3720.90 → 3723.20] Um, so no, I don't.
[3723.28 → 3725.34] I mean, no, I don't get it.
[3725.34 → 3730.00] The times when I've tried vegan diets that, that has mostly been my experience is that like
[3730.00 → 3732.10] all the fake meat is not worth it.
[3732.10 → 3734.44] But I do think that some of the fake bacon is okay.
[3734.96 → 3740.32] To be fair, there's, um, there are now burgers that are, um, very good.
[3740.40 → 3741.26] Impossible burgers.
[3741.42 → 3742.10] And there's another one.
[3742.22 → 3742.64] I forget.
[3742.94 → 3747.74] Um, that are just like, just as I remember eating burgers and actually terrible for you
[3747.74 → 3748.08] as well.
[3748.24 → 3749.28] So bonus.
[3749.44 → 3751.00] We didn't even bother to make them healthy.
[3751.48 → 3751.88] Yeah.
[3752.00 → 3755.44] I don't know what's like all the health benefits of a burger with none of the taste.
[3756.28 → 3757.80] It's actually worse for you.
[3758.02 → 3761.06] It's less healthy than, uh, it's better for the animal.
[3761.06 → 3766.98] You could say, well, but I make up for it by setting an oil refinery on fire every time.
[3767.24 → 3767.74] Yeah, exactly.
[3767.86 → 3768.02] Yeah.
[3769.16 → 3770.06] That's what it tastes like.
[3770.06 → 3770.38] Actually.
[3770.54 → 3772.76] It's like a carbon offset, but in reverse.
[3773.00 → 3775.28] Matt has to drive 200 miles just to get one.
[3775.50 → 3778.04] So yeah, it's a carbon onset.
[3778.40 → 3779.24] Oh, it's a carbon onset.
[3779.38 → 3779.50] Yeah.
[3780.50 → 3781.78] Matt wakes up every day.
[3781.84 → 3784.08] How much more carbon can I bring into the universe today?
[3785.80 → 3786.82] And the answer is none.
[3786.84 → 3788.62] Cause it already all exists.
[3789.72 → 3790.16] Oh.
[3791.06 → 3791.50] Well.
[3791.92 → 3792.22] Yeah.
[3792.40 → 3792.76] Does it?
[3793.28 → 3794.58] No, you can create carbon.
[3795.50 → 3795.90] Can you?
[3796.46 → 3798.34] Inside stars is where things are made.
[3798.70 → 3799.76] Well, let's call Neil deGrasse Tyson.
[3799.76 → 3800.54] I think that's a different podcast.
[3800.56 → 3803.38] Get him on go time next week and let's solve this thing.
[3803.50 → 3803.66] Yeah.
[3803.70 → 3804.28] He won't come on.
[3804.38 → 3807.04] He refuses to cause he's a JavaScript guy.
[3807.40 → 3807.42] So.
[3807.82 → 3810.26] I thought it was because of what happened the last time he was on.
[3811.34 → 3811.78] Yeah.
[3812.58 → 3813.02] Yeah.
[3813.90 → 3814.20] Yeah.
[3814.20 → 3815.24] Talking about black holes.
[3815.72 → 3816.84] That really was embarrassing.
[3816.84 → 3818.94] Okay.
[3818.94 → 3822.44] Well, if that's not baffling enough, join us next time.
[3822.54 → 3825.74] I'm sure we'll be able to equal that or make it worse.
[3826.24 → 3827.06] Thank you very much.
[3827.44 → 3828.38] See you next time.
[3828.38 → 3838.12] You can support our work and help ensure that go time continues into the future with a
[3838.12 → 3839.56] changelog plus membership.
[3840.00 → 3844.82] Ditch the ads, get closer to the metal and directly contribute to all changelog podcasts
[3844.82 → 3847.38] at changelog.com slash plus.
[3847.38 → 3850.88] Once again, that's changelog.com slash plus.
[3851.08 → 3851.56] Check it out.
[3851.56 → 3857.84] This episode was hosted by Matt Refer, produced by Jared Santo with music by Break master Cylinder.
[3858.48 → 3860.70] Go Time is brought to you by our awesome sponsors.
[3861.04 → 3864.14] Special thanks to Vastly, Launch Darkly and Linde.
[3864.84 → 3872.26] Next time on Go Time, Bill Kennedy joins Johnny and Chris for a fascinating discussion on software
[3872.26 → 3875.62] design philosophy and how it applies to Go programs.
[3876.32 → 3877.50] So stay tuned for that one.
[3877.50 → 3879.92] It's coming at you next week.
[3881.56 → 3911.54] Go Time.

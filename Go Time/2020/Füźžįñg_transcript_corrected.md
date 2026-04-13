[0.00 → 1.10] Fuzzy Fuzzy was a bear.
[1.20 → 2.12] Fuzzy Fuzzy had no hair.
[2.60 → 4.10] Fuzzy Fuzzy wasn't very fuzzy, was he?
[4.36 → 4.80] That's impressive.
[4.82 → 6.56] Oh, mate, that's got to be the opening, isn't it?
[7.06 → 7.92] Yeah, it really does.
[9.06 → 9.58] Yeah, deal.
[9.88 → 10.24] Done.
[13.06 → 15.64] Bandwidth for Changelog is provided by Vastly.
[16.00 → 17.88] Learn more at Fastly.com.
[18.14 → 21.22] We move fast and fix things here at Changelog because of Rollbar.
[21.22 → 23.02] Check them out at Rollbar.com.
[23.28 → 25.46] And we're hosted on Linde cloud servers.
[25.80 → 27.80] Head to Linode.com slash Changelog.
[30.00 → 33.06] This episode is brought to you by Digital Ocean.
[33.50 → 34.10] Droplets.
[34.44 → 35.22] Managed Kubernetes.
[35.58 → 36.44] Managed databases.
[36.96 → 37.48] Spaces.
[37.80 → 38.68] Object storage.
[38.96 → 40.20] Volume block storage.
[40.46 → 43.94] Advanced networking like virtual private clouds and cloud firewalls.
[44.14 → 50.38] Developer tooling like the robust API and CLI to make sure you can interact with your infrastructure the way you want to.
[50.38 → 54.32] Digital Ocean is designed for developers and built for businesses.
[54.32 → 61.36] Join over 150,000 businesses that develop, manage, and scale their applications with Digital Ocean.
[61.72 → 65.16] Head to do.co slash Changelog to get started with a $100 credit.
[65.58 → 67.64] Again, do.co slash Changelog.
[80.18 → 81.14] Let's do it.
[81.72 → 82.78] It's go time.
[82.78 → 84.94] Welcome to go time.
[85.12 → 88.24] Your source for diverse discussions from around the go community.
[88.82 → 95.08] We would like to thank each one of you who joined Changelog++ during our soft launch in August.
[95.54 → 97.74] We truly appreciate you supporting the show.
[97.74 → 104.16] If you have no idea what I'm talking about, check it out and learn more at changelog.com slash plus.
[104.74 → 106.48] Okay, it's time to talk fuzzing.
[107.04 → 108.28] Here we go.
[112.78 → 117.50] Hello and welcome to go time.
[117.72 → 118.68] I'm Matt Ryder.
[118.92 → 120.96] Today we're talking about fuzzing.
[121.24 → 126.28] We're going to find out what it is and how we can use it to make our code better.
[126.82 → 134.64] And we're going to take a close look at a new draft design that discusses bringing fuzzing as a first class concern to go.
[135.06 → 135.70] It's very exciting.
[135.82 → 140.32] And we're lucky to be joined by the author of that draft design, Katie Hock man.
[140.42 → 140.92] Hello, Katie.
[141.32 → 141.82] Hi, Matt.
[141.82 → 142.32] How's it going?
[142.86 → 143.18] Good.
[143.28 → 144.04] Welcome to the show.
[144.14 → 144.68] Thanks for coming.
[145.12 → 146.04] Thank you for having me.
[146.64 → 149.72] We're also joined by Filippo Salford.
[149.84 → 150.80] Hello, Filippo.
[151.12 → 151.60] Hey, Matt.
[151.66 → 152.26] Good to be back.
[152.60 → 154.96] Always a pleasure to have you here, sir.
[155.38 → 156.20] Same, same, same.
[156.50 → 157.40] Looking forward to it.
[157.68 → 158.20] Very formal.
[158.78 → 159.00] Yeah.
[159.14 → 159.56] Thank you.
[160.24 → 163.52] And we're also joined by Roberto Claps.
[163.76 → 164.62] Hello, Roberto.
[165.98 → 166.30] 748.
[167.80 → 168.24] Okay.
[168.24 → 170.72] Is that a fuzzed response?
[170.72 → 170.96] Yeah.
[171.38 → 173.26] I wanted to see if you crashed with Integer.
[174.30 → 176.34] I've not crashed, though, nor am I panicking.
[176.68 → 177.46] I've continued.
[178.46 → 180.90] In fact, that was in my unit test earlier.
[181.22 → 183.18] So I was ready for it.
[183.66 → 184.50] But thank you very much.
[184.56 → 185.30] Welcome to the show.
[185.52 → 185.82] Thanks.
[185.82 → 190.88] Can we take a second to acknowledge how Matt rolled the R's for both the Italian names?
[191.60 → 191.72] Yeah.
[191.78 → 192.52] Oh, it's my pleasure.
[192.62 → 192.96] That was good.
[195.34 → 196.46] It's a lovely accent.
[196.70 → 200.36] So I always like to listen to it and have you on for that purpose, really.
[200.74 → 204.88] So if that's all you contribute to this show, then that's fine by me.
[205.36 → 206.26] That's our intention.
[206.26 → 209.86] Well, so maybe we should start at the beginning then.
[209.94 → 214.08] For anybody not familiar, what is fuzzing, and what's it for?
[214.42 → 216.62] Yeah, I can give a quick summary of that.
[216.80 → 223.44] So basically, fuzzing is a form of automated testing that can manipulate inputs in a way
[223.44 → 228.04] that can find bugs that maybe you wouldn't otherwise be able to find on your own.
[228.04 → 233.24] So in my mind, it's kind of a supplement to some of the existing testing that people already do.
[233.52 → 237.12] That's pretty common, like unit testing or integration testing.
[237.34 → 244.04] But what sets it apart is it actually does things on its own and runs and can run continuously.
[244.34 → 246.02] So it's kind of smart in a way.
[246.16 → 251.26] So if it has some interesting inputs, it can actually use some intelligence to go in and
[251.26 → 256.62] mutate those inputs in interesting and meaningful ways to find crashes and panics
[256.62 → 262.44] that wouldn't easily be otherwise found if the developer had to try to identify them themselves.
[262.88 → 265.02] So that's interesting then you talk about this intelligence.
[265.32 → 267.64] It isn't just random then.
[267.80 → 269.62] There's something else going on.
[270.02 → 276.26] Yeah, and I think it's really tricky because there's no industry standard on how these kinds
[276.26 → 277.16] of things work.
[277.16 → 281.26] I mean, there are definitely tons of different ways that you can mutate things randomly.
[281.76 → 285.96] And there's also a lot of interesting discussion around how do you prioritize
[285.96 → 288.12] which corpus entries?
[288.76 → 292.60] And I'll talk a little bit more about what corpuses are later, but basically which inputs
[292.60 → 297.56] to modify and how to modify them and how smart it should really be.
[297.94 → 303.02] And all those things are kind of up in the air and a lot of different buzzers work differently,
[303.60 → 305.22] which is actually kind of cool in my mind.
[305.88 → 306.66] Yeah, that's interesting.
[306.66 → 310.32] So what situations are it good for helping out in then?
[310.32 → 315.92] So let's say the string. Split example from the standard library, you pass in a string
[315.92 → 321.12] and you pass in a separator, and it basically just splits that string wherever it finds that
[321.12 → 325.46] separator and returns a slice of the components, the segments that it found.
[325.72 → 327.62] Would that be a good candidate for fuzzing?
[328.18 → 329.32] Yeah, I think it could be.
[329.52 → 334.10] And I think it'd also be, I think Filippo and Rob will have a lot of perfect things
[334.10 → 339.02] add to in terms of who's used buzzers in the past and how they've usually had a security
[339.02 → 340.24] context around them.
[340.80 → 345.46] And what this proposal has been trying to do is actually get fuzzing into the hands of
[345.46 → 349.38] non-security experts and non-security developers and have other people use them.
[349.52 → 354.02] So in the string split example, you know, if there's an off by one error somewhere or maybe
[354.02 → 359.84] some issue that can cause a panic or some input that doesn't meet some specific property,
[359.84 → 361.62] it might be easy to find with fuzzing.
[361.62 → 366.14] And I think it would be a perfect package to test or a good function to test in that
[366.14 → 366.50] package.
[366.70 → 366.72] Yeah.
[367.10 → 367.30] Yeah.
[367.32 → 372.38] Because you hear a common use cases are things like parsers and things that are doing decoding
[372.38 → 378.68] because, you know, they are dealing with usually unknown in advance kind of structures that
[378.68 → 380.78] maybe they have to sort of infer along the way.
[381.02 → 386.68] So there is a lot of room in that kind of operation for things to go wrong or unexpected input,
[386.78 → 390.28] just things that you would never imagine anyone would pass in.
[390.28 → 395.20] And so, yeah, that's what separates it out from unit tests, I guess, really, because
[395.20 → 397.12] unit tests are very deliberate, aren't they?
[397.42 → 397.58] Yeah.
[397.90 → 398.40] Yeah, they are.
[398.50 → 404.64] I mean, you give a set of inputs, and you run something, and then you look at the output and
[404.64 → 405.34] it's very clear.
[405.48 → 409.90] And you have to say, these are the inputs that I think are important that should test
[409.90 → 410.52] it well enough.
[410.52 → 412.20] And then it should have this output.
[412.90 → 417.40] And fuzzing, I think, can apply to a lot of context beyond parsers and things like that,
[417.40 → 420.58] because there's a reason that we have unit tests everywhere.
[420.58 → 426.16] And there's a reason we don't just test parsers or difficult cryptography or things like that.
[426.22 → 427.42] There's a reason we test everything.
[427.50 → 430.92] And it's because we don't always know where the bugs in our code are.
[430.92 → 433.54] You know, we have default assumptions that our code works.
[433.66 → 439.44] And so we just kind of test it kind of just in good faith sometimes just, you know, to
[439.44 → 440.32] prove that it works.
[440.80 → 445.24] And I think fuzzing, a fuzzing engine should be pretty agnostic in the sense that it doesn't
[445.24 → 449.36] assume that it's going to work, and it's going to go and maybe find things that you didn't
[449.36 → 453.54] really realize could actually break or something that you had overlooked that you didn't realize
[453.54 → 455.44] is a dependency somewhere else that might break.
[455.44 → 456.36] Right.
[456.52 → 463.20] I would also add that since when you write the fun test target, kind of, you want to
[463.20 → 466.44] expect on properties of the stuff that you work on.
[466.44 → 470.32] Instead, when you work on unit tests, you expect some output.
[470.74 → 474.76] For example, in the string split case, you can say, I'm going to call a string split with
[474.76 → 475.32] two parameters.
[475.84 → 481.78] And I'm going to check that the second one never appears in the return slices because the
[481.78 → 482.96] separator should never appear.
[482.96 → 483.44] Right.
[483.68 → 487.38] And that is something you would generally not test in a unit test.
[487.46 → 492.94] Or like you're going to check that the returned slices are less than the characters of the
[492.94 → 493.20] string.
[494.12 → 498.50] So like if you return more than characters there are, there must be a problem.
[498.98 → 501.78] And this is stuff that normally doesn't get tested.
[502.32 → 503.50] I'm pretty bad at writing tests.
[503.66 → 506.94] But when I write unit tests, I don't test for this kind of condition.
[506.94 → 507.54] Yeah.
[507.70 → 512.76] In another example of something that would be good to check in a fuzz test of the split
[512.76 → 518.32] function is that if you put it back together, putting the separators between the things you
[518.32 → 520.78] split, do you get back the regional string?
[521.26 → 523.52] If you do, it probably did its job right.
[523.94 → 528.10] And that's the kind of stuff that buzzers are pretty good at finding because they can just
[528.10 → 533.42] go and find some input where, I don't know, the separator is at the end, and it's missing
[533.42 → 538.28] one character, or I don't know where the thing doesn't round trip.
[538.72 → 543.00] That gives you even more because then you now are testing for an additional property,
[543.18 → 547.46] which is if you string split, and then you string join, you must get the same thing out,
[547.62 → 548.86] which is a normal expectation.
[549.06 → 551.94] I mean, when I use the strings package, I expect that to be true.
[552.32 → 555.76] But I don't know if there is anyone that has been fuzzing that to make sure that
[555.76 → 561.76] is actually true, especially on edge cases like nil slices or slices of empty strings.
[561.76 → 564.40] What happens would be interesting to see.
[565.30 → 565.44] Yeah.
[565.58 → 568.08] So there is an element then of design here.
[568.22 → 573.82] You have to think of that kind of thing, that property to then model it in a fuzz test,
[573.90 → 574.12] right?
[574.66 → 579.86] It's not just you just point it to a method, and it just fills the method up with nonsense.
[580.42 → 581.32] I think yes and no.
[581.38 → 582.04] I think it can.
[582.12 → 584.02] I think it depends on what you're using it for.
[584.42 → 588.84] I mean, you could just throw random input at a function and just see if it panics.
[588.84 → 592.96] Like that is a property that can be tested, and you don't have to know anything about
[592.96 → 593.14] it.
[593.54 → 597.94] I think it can also be used for things like differential testing or property testing or
[597.94 → 601.18] a lot of different things that can be a supplement to your unit test, but it can also just go
[601.18 → 601.80] find a crash.
[602.18 → 604.30] And you could probably do that in a couple of lines with a little thought.
[604.90 → 609.44] Differential testing is something that honestly works a little too well.
[610.00 → 613.70] The idea is that there are multiple implementations of the same thing, right?
[613.70 → 618.00] For example, big number implementations.
[618.36 → 619.78] It doesn't matter what library you use.
[619.80 → 625.94] If you multiply two arbitrary precision decimals, you should get the same arbitrary precision
[625.94 → 626.88] decimal out.
[627.46 → 628.40] Sounds right, right?
[629.24 → 633.82] Oh, my friend, how many bugs buzzers have found just by telling them.
[634.22 → 634.40] Yep.
[634.54 → 635.46] So here are two functions.
[635.58 → 636.62] They need to return the same thing.
[636.84 → 637.02] Cool.
[637.18 → 637.34] Go.
[637.34 → 642.74] I get emails because one of them, the one that are tested is the Go one.
[643.20 → 648.66] And I get emails when there's a mismatch between the Go one and some other implementation.
[649.12 → 650.02] And oh, boy.
[651.86 → 652.34] Yep.
[652.62 → 653.56] Multi-precision is hard.
[654.08 → 655.58] So yeah, that's an excellent example.
[656.18 → 662.54] One thing that I did with differential testing was at one point in Go, a bug was fixed with a
[662.54 → 664.00] problem with header parsing.
[664.00 → 668.70] And I thought, this looks easy to find with a buzzer.
[668.94 → 675.50] So I just imported fast HTTP and the standard HTTP libraries, both in Go, run Go Fuzz for
[675.50 → 676.20] 25 minutes.
[676.34 → 677.00] And I found the bug.
[677.62 → 680.70] The bug that was just fixed and has been there for 12 years.
[681.46 → 687.00] So yeah, if you want to assert for a property, and the case was, I want the header set to
[687.00 → 687.54] be identical.
[687.96 → 690.14] It's quite easy to find problems.
[690.14 → 696.88] And if I recall correctly, at one point, the JSON package was optimized, heavily optimized,
[697.34 → 702.00] and there was a differential buzzer in place that checked that the old version and a new
[702.00 → 704.28] version would parse the JSON the same way.
[704.66 → 710.94] And it found a bug before it hit a stable release, which would have been kind of bad.
[710.94 → 718.06] So that was another kind of success story of fuzzing, not for security reasons.
[718.42 → 720.06] That would just get another test.
[720.66 → 723.06] So how can you do fuzzing in Go today then?
[723.32 → 725.12] What are the choices that we have?
[725.34 → 725.98] There are a few.
[726.20 → 728.94] I mean, I can speak to at least one or two.
[729.06 → 731.20] I mean, I think the common one is Go Fuzz.
[731.40 → 733.34] That's the one that everyone knows about.
[733.44 → 734.94] That's Go-Fuzz.
[734.94 → 735.46] Fuzz.
[735.92 → 738.66] And that was written primarily by Dmitry Tycho.
[739.36 → 742.58] And yeah, I mean, it's really, really amazing.
[742.84 → 744.86] And I've spoken to him about it.
[744.90 → 750.28] And he's actually given a lot of really, perfect feedback into the proposal that's out
[750.28 → 750.66] there now.
[751.08 → 755.50] So it's been nice to partner with him a little bit on that, too, and have him get some feedback
[755.50 → 756.02] on that.
[756.60 → 758.24] And yeah, I mean, it's really neat.
[758.32 → 760.34] And if you haven't used it, you should definitely check it out.
[760.34 → 764.20] And then another tool that somebody wrote was Fuzz Go.
[764.44 → 765.72] It was F-Z-G-O.
[766.24 → 770.84] And I think that was kind of a proof of concept written mostly by the pods, it sounded like,
[771.20 → 775.34] to try to integrate it a little bit more kind of with the Go command and making it look
[775.34 → 780.36] more like kind of an end-to-end tool that wouldn't have to have, so many build steps like
[780.36 → 781.20] Go Fuzz has.
[781.58 → 785.04] And add a little bit of support for modules, I think, was part of that.
[785.10 → 786.56] Or maybe that was a part of Go Fuzz.
[786.56 → 790.70] But there's been different features that both of them have tried to basically model
[790.70 → 791.72] and see how they would work.
[792.10 → 796.68] And I think Fuzz Go was meant to be kind of a prototype or an experiment of what it might
[796.68 → 797.90] look like as a final approach.
[799.12 → 801.24] And you mentioned build steps there then.
[801.42 → 804.56] So it isn't just something at all that runs at runtime.
[804.86 → 806.26] There are other things that happen.
[806.36 → 810.90] Is there some kind of introspection that happens or reflection on the types and things?
[810.96 → 812.58] Is it kind of generic in some way?
[812.58 → 817.72] Well, when I say build steps, I don't remember all the exact details of how Go Fuzz works.
[817.74 → 820.78] But I do know that it has kind of like a Go Fuzz build.
[820.88 → 823.98] And you have to kind of build the binary that will be fuzzed.
[824.10 → 827.34] And then you have to run it separately and kind of manage your own corpus.
[827.48 → 828.82] And so there are a lot of different steps.
[828.90 → 832.86] You can't just run one command with the Go tool chain as it is today.
[832.94 → 836.78] You kind of have to learn a different workflow, which was a bit of a...
[836.78 → 841.08] Just like an impediment for some people to try to start it.
[841.84 → 843.38] Because they didn't want to learn a new tool.
[843.84 → 847.98] I would say that that is one of the main reasons why people are not using it.
[848.06 → 850.82] It's because it's external kind and feels different.
[851.06 → 854.12] Also, one thing that it does, it does a source to source transformation.
[854.32 → 857.58] So it takes your source code and implements some sort of checkpoints.
[857.58 → 862.48] So basically, when your code runs, it can check at which point it got.
[863.06 → 867.08] So basically, while your code executes, it can check how much of the code was covered.
[867.18 → 868.56] More or less like the cover tool.
[869.24 → 873.20] But it needs to do it more heavily than the cover tool and in a more efficient way.
[873.82 → 877.72] And this is one of the reasons why it was quite hard to make it support modules.
[878.10 → 880.04] Because it actually rewrites the sources.
[880.04 → 887.04] Yes, some context here is that part of what makes Buzzer's magic is that...
[887.04 → 891.48] Well, the recent generation of Buzzer's magic since, I think, AFL.
[891.86 → 898.80] Is that they use coverage to figure out what mutations are the ones that are interesting to look at.
[899.12 → 902.64] Katie was talking about how there are different strategies for these.
[903.00 → 909.02] But in general, the common denominator is that they all look at the cover of your code.
[909.02 → 913.18] If you ever run go test-cover profile.
[913.54 → 915.30] Oh boy, I don't remember the flag.
[915.40 → 919.52] But anyway, if you ever generated the coverage report, you know, with the green and the red.
[919.92 → 920.98] That's what Buzzer's do.
[921.08 → 924.72] They run the input and check which parts light up.
[925.14 → 929.64] And if they change the input and some new code lights up, the Buzzer goes like,
[929.70 → 929.98] Aha!
[930.30 → 931.34] Okay, this is useful.
[931.44 → 936.08] I can keep changing this, and maybe I'll hit another path that takes from there.
[936.08 → 941.18] Or maybe I'll be able to combine two paths in a way that we're not tested together.
[941.18 → 946.62] And that's what makes them honestly kind of freakishly effective.
[947.26 → 954.32] There's this demo of AFL slowly building a valid JPG out of nothing.
[954.32 → 962.36] And it slowly makes a picture, and it figures out the letters to put in the tags and everything.
[962.66 → 963.36] It's very good.
[963.68 → 969.42] One thing that really scared me was when I run Gomez against the HTTP library.
[969.72 → 975.02] And after a while, I saw that in the corpus, something that looked like random started appearing.
[975.28 → 976.30] And I was like, oh, cool.
[976.30 → 983.24] So the Go package, the Go standard package started accepting something that is not HTTP because it was HTTP2.
[983.66 → 988.38] Basically, I started constructing valid HTTP2 requests from nothing.
[989.14 → 990.56] And that was scary.
[990.94 → 993.36] And also, I was ashamed because I didn't recognize it.
[993.42 → 996.92] And I had to manually write to decompress it and see what was going on.
[997.28 → 1002.66] Rob, if you can ever read HTTP2 to the naked eye, you need to tell me.
[1002.66 → 1006.62] Yeah, because that is a strange superpower.
[1007.06 → 1011.46] I don't know what has had to bite you for that to be the power that then manifests.
[1011.94 → 1013.00] There are support groups.
[1013.48 → 1014.44] We've all been there.
[1014.72 → 1015.74] Mine is TLS.
[1016.60 → 1017.84] Used to be DNS.
[1018.28 → 1019.20] It's okay.
[1020.36 → 1020.92] There's help.
[1022.18 → 1022.78] Thanks.
[1023.06 → 1024.22] Thanks for keeping them in mind.
[1024.84 → 1032.28] So that is fascinating then that it's not just shifting the inputs like by some external means.
[1032.28 → 1039.34] It actually has an insight into the code that's running inside in your own code, in your own binary.
[1039.56 → 1043.42] And it uses that information to also influence what it's doing.
[1043.60 → 1045.92] So that is kind of like spooky.
[1046.16 → 1047.26] I could definitely imagine.
[1047.50 → 1053.28] It's a little bit like adversarial training in machine learning where you have a model, and you have another model.
[1053.42 → 1055.06] And they sort of compete with each other.
[1055.06 → 1058.52] And then they both just keep getting better, you know, together.
[1058.70 → 1060.06] And that's kind of a great way to...
[1060.58 → 1062.38] It's almost like feels like cheating in some way.
[1062.38 → 1067.94] But you can end up with a mirror of something else, you know, by this technique.
[1068.02 → 1069.48] So it is kind of amazing.
[1069.60 → 1072.38] And yeah, to see it, it really will start to feel intelligent.
[1073.14 → 1075.48] And a few of you have said it's kind of spooky, this thing.
[1076.44 → 1083.38] Another, just a note of another spooky thing is you can also kind of like reverse engineer your code such that it can figure out...
[1083.38 → 1090.40] There are certain tools that can figure out what the input is actually supposed to be and then kind of do that for you.
[1090.44 → 1095.54] So it can actually basically tell the fuzzing engine, like this is what input will make this if statement pass.
[1095.80 → 1102.42] And then it'll just do that to kind of get unstuck from wherever you're at with the fuzzing engine.
[1103.00 → 1104.56] And that's something maybe you do...
[1104.56 → 1110.86] Like I think Go Fuzz does this once every thousand mutations just to try to unstick it, but not every time because it's too expensive.
[1110.86 → 1114.22] And so it's a lot of trade-offs of like how random do you want this to be?
[1114.62 → 1118.90] How much do you want to use prioritization of certain inputs?
[1119.04 → 1123.92] How much coverage is coverage a metric in terms of what is that in terms of feedback loop?
[1124.02 → 1126.78] Like how much do you care about it in terms of other things?
[1126.82 → 1130.82] And so it's kind of creepy, and it's a judgment call from the developer on how they want to design that too.
[1131.36 → 1134.40] Yeah, it does sound like a kind of hacker's tool, doesn't it?
[1134.44 → 1137.92] And in fact, did it have its origins in the security world?
[1137.92 → 1143.70] Yeah, but I like what Katie just said that it's a trade-off that the developer has to make.
[1144.18 → 1148.38] And I think she meant the developer of the fuzzing tool, correct me if I'm wrong?
[1148.38 → 1149.04] Yes, yeah.
[1149.38 → 1150.78] Because that's the thing.
[1151.10 → 1163.82] The thing I like about the proposal is that it does not leave all these decisions and the necessity to learn about all this stuff to the end users, to the Go developers that are just trying to test their code.
[1163.82 → 1171.44] Yeah, and also if you look at the proposal, it tries to make fuzz test targets as close as possible to what a test looks like nowadays.
[1172.42 → 1179.46] So basically the friction to adopt fuzzing if you're used to writing unit tests, and if you're not, you should, is going to be very low.
[1180.30 → 1187.02] Because it's going to basically slightly change the pattern, but it's going to be as close as possible.
[1187.02 → 1190.82] Yeah, we should talk more about that proposal.
[1191.04 → 1194.18] But before we do, I just want to get a few other concepts kind of clear.
[1194.70 → 1196.96] There's this concept of seeding the corpus.
[1197.10 → 1201.38] There's this concept of kind of giving the fuzzing tool some kind of head start.
[1201.88 → 1207.40] A bit like with unit tests where you say, you know, we know these are the inputs and these are the expected outputs.
[1207.88 → 1211.96] You also kind of seed the fuzzing tool similarly, don't you?
[1211.96 → 1227.24] Yes, and I think it's also kind of a goal of the proposal to try to make it such that the unit tests that people have now and the use cases that they've already come up with can basically just be directly used as seed corpus.
[1227.24 → 1234.42] And so the seed corpus is kind of filling two needs, at least in terms of this goal proposal.
[1235.52 → 1238.08] It's first seeding the mutation engine.
[1238.24 → 1242.26] It's seeding that the corpus trying to tell it this is a good starting point for you.
[1242.84 → 1251.00] Build on this, and then it can manage its own corpus on its own as it wants to and build it up as it finds new coverage and new interesting things.
[1251.20 → 1255.24] But it's also can serve as a regression test of sorts.
[1255.24 → 1259.74] The seed corpus is either checked into basically your test data directory.
[1259.88 → 1265.40] It's basically checked in directly into your module or into your package, or it's in there programmatically.
[1265.58 → 1266.90] It's in your test in code.
[1267.86 → 1270.98] And so that's run every single time go test is run.
[1271.80 → 1273.70] And so it's also meant to act as a regression test.
[1273.84 → 1275.80] So you can use existing things.
[1275.88 → 1282.82] You can use new crashes, and you can build out that seed corpus as you find new regressions that you want to make sure you're testing.
[1282.82 → 1293.50] Yeah, so that's a really cool feature that if something fails, that automatically gets contributed to the testing so that next time that will explicitly get tested.
[1293.72 → 1295.22] Is that how it works?
[1295.22 → 1306.80] Yeah, so that is very cool because, of course, the value of unit testing, if in the case where you find a bug, and then you write a test to prove that bug, which you do if you follow TDD tightly.
[1307.34 → 1315.12] And in some cases, I find that to be a kind of great way to work because you get a kind of to-do list for free from the tool chain.
[1315.12 → 1322.80] You know, as you write your test, if things aren't working, they fail, you get kind of errors that you then have to unblock.
[1322.98 → 1327.88] And it's a kind of nice way to decide what you have to do to get something to pass.
[1328.46 → 1336.32] And yes, it has that same kind of idea is if you find a bug, and you've written a test to prove it, you then save that test.
[1336.44 → 1339.94] And next time you run all your test suite, it'll check for that bug again.
[1339.94 → 1342.36] So this is what we mean by protecting from regression.
[1342.64 → 1348.00] You can never have that same bug again if you've fixed it, and you keep the unit test.
[1348.66 → 1350.66] What do we do with that corpus, though?
[1351.02 → 1355.80] Dominic Roos on Twitter asked, what are the best practices for the corpus?
[1356.14 → 1357.56] Should you put it into Git?
[1357.74 → 1359.12] Should it go into some other repo?
[1359.26 → 1360.66] Do you share it amongst the team?
[1361.14 → 1363.76] Is it just something you run on your own dev machine?
[1364.30 → 1365.54] Where does this go in practice?
[1366.04 → 1367.16] I think it's going to depend.
[1367.16 → 1372.28] I also think this is kind of a bit of an open question in terms of what kind of practices do we want?
[1372.36 → 1374.54] Like best practices do we want to lay out for this?
[1374.62 → 1378.58] But also, that part is also kind of up to the developer, too.
[1378.94 → 1380.16] It could be programmatic.
[1380.36 → 1387.96] Like, let's say, like I mentioned before, you have existing unit tests, and you just want to move it into basically change your t.run into an f.fuzz.
[1388.36 → 1390.44] Something like that should be basically possible.
[1390.64 → 1393.06] So if it's already programmatic, keep it programmatic.
[1393.46 → 1394.74] And if it fails, it fails.
[1394.80 → 1395.40] And that's great.
[1395.40 → 1405.62] If you have a bunch of test data, like let's say you have a bunch of big HTTP requests or binary files or something like that you already have somewhere, you can just use those, too.
[1406.02 → 1408.44] And the fuzzing engine will look at that.
[1408.50 → 1413.44] Or not the fuzzing engine, but Go Test will look at test data as part of the seed corpus, too.
[1413.44 → 1417.44] And so I think it also depends on what the seed corpus is.
[1417.50 → 1418.94] Is it a huge binary?
[1419.62 → 1421.36] Is it a small thing?
[1421.48 → 1423.36] Is it something that's best built programmatically?
[1423.36 → 1427.32] And what the best practices for that will be, I think, are still kind of an open question.
[1427.44 → 1428.18] At least it is to me.
[1428.58 → 1433.50] I think there's also an angle of maturity of the ecosystem in there, of maturity of the technique.
[1433.50 → 1444.90] Because when fuzzing is just this tool that some security researchers use to smash against a program once, try to get something out of it, and then move on.
[1444.90 → 1449.48] Of course, they just run the corpus wherever they're keeping it.
[1449.90 → 1458.08] But I feel like just like with testing, we set up continuous integration, and we trust machines to do the heavy lifting for us.
[1458.46 → 1463.60] I expect that fuzzing also take that path once it's built into developer workflows.
[1464.16 → 1470.32] So you would have a small corpus locally on your machine, and Katie's proposal puts it automatically in a cache folder.
[1470.32 → 1476.86] And that will, you know, do a very quick pass, but you're not going to run the buzzer mostly on your laptop.
[1477.20 → 1483.54] Part of what makes buzzers work is that computers are fast, but also you can keep throwing more cores at it.
[1484.02 → 1491.94] And then you upload it, and some CI or OSS fuzz or some continuous integration system can just run the buzzer.
[1491.94 → 1499.46] And it should persist the corpus, so it will keep running the same corpus against it so that you make changes.
[1499.46 → 1505.08] And the corpus is already hot and large, but it's not checked into your repository.
[1505.54 → 1509.94] Because most people don't want megabytes and megabytes of corpus checked in.
[1510.36 → 1514.84] Right. One thing that I also like about buzzers is that there is usually a way to tell them,
[1515.22 → 1519.28] don't feed me input that is bigger than this amount, either directly or indirectly.
[1519.40 → 1525.52] The indirect way is you take whatever the buzzer passes you, and if it is bigger than a certain size, you just return,
[1525.82 → 1526.94] no, I don't want this.
[1526.94 → 1531.70] And after a while, the buzzer will stop seeding the corpus with anything bigger than the size you want.
[1531.82 → 1539.24] So if you're testing string split, yes, you can get up to a megabyte, but it doesn't make sense to split a gigabyte of string.
[1539.36 → 1547.42] Because, I mean, you know the code that you're fuzzing, and you shouldn't be too exaggerating on how liberal you are in the input you feed it to.
[1547.68 → 1550.88] It's like, yes, you're fuzzing, but you know what you're fuzzing.
[1550.88 → 1554.32] It's like, if you're fuzzing a JPEG parser, yes, feed it big stuff.
[1554.50 → 1560.90] If you're fuzzing a string splitter, it's very hard that there is a bug at the three gigabytes mark.
[1561.54 → 1566.68] Yeah, that's a good point, though, because you do get the sense that this is just, you'd switch it on,
[1566.82 → 1569.70] and it just points to your methods, and it's just going to go and do it.
[1570.06 → 1573.94] That is interesting, though, that this is a continuous thing.
[1573.94 → 1577.92] It's not something that you would do like a benchmark, where you just run that on your laptop.
[1579.14 → 1583.26] But there is, in the proposal, there is like a new flag to run the fuzz,
[1583.34 → 1590.06] but is the expectation that that would run in some kind of continuous integration or some other place?
[1590.72 → 1591.86] I think it probably depends.
[1592.02 → 1596.16] I think, yeah, I think it kind of depends on how long someone wants to run a buzzer.
[1596.46 → 1600.86] If they are willing to just let it run on their machine for a while, maybe that's okay.
[1600.86 → 1604.04] If they want to just run it for the weekend, that's totally fine.
[1604.48 → 1606.96] If it's a company, and they have a ton, or just an individual,
[1607.10 → 1609.32] and they have a ton of different things they want to try to fuzz at once,
[1609.82 → 1611.72] I'm not really sure if that's even going to be supported,
[1612.08 → 1615.12] to be able to run multiple buzzers at once.
[1615.20 → 1617.40] I don't know what would happen, like if there's a race condition.
[1618.38 → 1620.68] There are a lot of different things that I'm not totally sure would be supported.
[1620.80 → 1623.26] If it crashes something somewhere, it's hard to know where it's coming from.
[1623.42 → 1627.96] And so it may make more sense in situations like that to have it on some kind of continuous integration.
[1627.96 → 1632.22] I wonder if we're going to end up in a situation where, like with Bitcoin miners,
[1632.38 → 1637.54] we've just got all these machines that are just spending all their time crunching through fuzzing stuff.
[1638.04 → 1639.16] When we've got fuzz coin.
[1639.66 → 1641.08] OSS Fuzz already exists.
[1641.20 → 1647.74] It's this project by Google that basically provides what internally we call cluster fuzz,
[1648.48 → 1651.72] which I don't know if I was allowed to say, but yeah, we're rolling.
[1651.72 → 1658.54] For open source projects where any open source project can submit.
[1658.86 → 1659.32] I don't know.
[1659.50 → 1660.76] There are criteria, of course.
[1660.88 → 1664.72] I don't know what they are exactly, but they will just run your buzzers for you.
[1664.84 → 1667.78] And if we make it standard how to do that with Go,
[1667.88 → 1670.24] it would be extremely easy to submit Go projects.
[1671.08 → 1673.34] Yeah, that gets very exciting, actually.
[1673.48 → 1674.46] That's really cool.
[1674.72 → 1676.22] I think cluster fuzz is open source.
[1676.60 → 1676.90] Cool.
[1677.38 → 1677.60] Okay.
[1677.86 → 1679.22] I'm not getting fired today.
[1679.22 → 1681.88] Yeah, don't get fired, please.
[1682.14 → 1685.02] But if you do want to get fired, please do it this way.
[1685.14 → 1687.70] Come on the show and reveal something that you shouldn't reveal.
[1688.20 → 1689.62] So cool for us.
[1689.82 → 1690.50] Such a scoop.
[1690.72 → 1693.86] I've got a history with that and let's leave it at that and move on.
[1694.38 → 1695.52] Yeah, don't encourage him.
[1696.10 → 1696.26] Yeah.
[1696.72 → 1701.80] Last time Filippo was on the show, he stopped me from admitting to a crime before I said it,
[1701.80 → 1702.96] which was brilliant.
[1703.66 → 1705.08] Really useful service.
[1705.08 → 1711.02] We can take a short break if anyone needs to.
[1711.90 → 1714.58] And people at home can take a break anytime they want to, really.
[1714.96 → 1720.42] Probably just carrying us around on their portable devices so they can just do what they like.
[1720.94 → 1721.94] I don't know why I'm explaining that.
[1722.88 → 1724.96] I was just going to say some bits will get cut out.
[1725.04 → 1726.98] If you need anything cut out, let us know.
[1727.70 → 1728.36] We'll do that.
[1728.36 → 1734.30] Oh, Matt, I've listened to so many episodes of this in which you say this will be cut out and that never happens.
[1734.94 → 1735.32] I know.
[1735.52 → 1738.30] They don't do it for me, but they will do it for you three.
[1738.94 → 1739.26] Okay.
[1741.80 → 1742.32] Thank you.
[1742.36 → 1745.38] They add bits for me from other times I've embarrassed myself.
[1745.82 → 1748.44] I find them in extra shows.
[1748.68 → 1750.56] I didn't embarrass myself then.
[1750.56 → 1752.66] That was a different time when I embarrassed myself.
[1752.66 → 1753.98] It's directly on the soundboard.
[1753.98 → 1755.98] Yeah, exactly, yeah.
[1756.68 → 1756.92] Yeah.
[1757.22 → 1758.74] It's just got me embarrassing myself.
[1758.84 → 1759.48] This is one of them.
[1759.92 → 1760.80] This is one of the clips.
[1763.80 → 1768.82] How much time does your team spend building and maintaining internal tooling?
[1769.08 → 1771.08] I'm talking about those behind-the-scenes apps.
[1771.32 → 1773.10] The ones no one else sees.
[1773.36 → 1775.86] The S3 uploader you built last year for the marketing team.
[1775.86 → 1779.60] That quick Firebase admin panel that lets you monitor key KPIs.
[1779.94 → 1782.70] Maybe even the tool your data science team hacked together
[1782.70 → 1784.88] so they can provide custom ad spend analytics.
[1785.46 → 1787.38] Now, these are tools you need so you build them.
[1787.58 → 1788.54] And that makes sense.
[1789.08 → 1792.40] But the question is, could you have built them in less time,
[1792.54 → 1795.58] with less effort, and less overhead and maintenance required?
[1795.92 → 1798.10] And the answer to that question is, yes.
[1798.58 → 1799.84] That's where Retool comes in.
[1800.22 → 1803.70] Rohan Copra, engineering director at DoorDash, has this to say about Retool.
[1803.70 → 1808.02] Quote, the tools we've been able to quickly build with Retool have allowed us to empower
[1808.02 → 1812.54] and scale our local operators, all while reducing the dependency on engineering.
[1813.00 → 1813.34] End quote.
[1813.82 → 1817.60] Now, the internal tooling process at DoorDash was bogged down with manual data entry,
[1818.02 → 1820.08] missed handoffs, and long turnaround times.
[1820.30 → 1824.08] And after integrating Retool, DoorDash was able to cut the engineering time required
[1824.08 → 1828.68] to build tools by a factor of 10x and eliminate the error-prone manual processes
[1828.68 → 1829.60] that plagued their workflows.
[1829.60 → 1833.42] They were able to empower backend engineers who wouldn't otherwise be able to build front
[1833.42 → 1834.12] ends from scratch.
[1834.52 → 1838.32] And these engineers were able to build fully functional apps in Retool in hours,
[1838.50 → 1839.50] not days or weeks.
[1839.92 → 1843.66] Your next step is to try it free at retool.com slash changelog.
[1843.82 → 1846.24] Again, retool.com slash changelog.
[1859.60 → 1872.82] So the new proposal, which we'll post a link to in the show notes,
[1873.54 → 1878.74] it kind of has a very nice Go feel to it, like the design of it.
[1878.74 → 1883.74] So in the same way that we're used to testing functions, being how we describe unit tests,
[1883.74 → 1889.20] there are fuzz functions now which take a different argument, the testing.f.
[1889.86 → 1892.26] And is that like an interface then?
[1892.48 → 1893.98] What is that testing.f type?
[1894.82 → 1899.02] That testing.f type is very similar to a testing’t or testing.b.
[1899.58 → 1903.12] So it'll implement the testing.TB interface.
[1903.52 → 1905.36] Will there be a testing.f interface then?
[1905.50 → 1907.30] Or is that like a strong type?
[1907.54 → 1908.38] It's a strong type.
[1908.38 → 1908.98] Right.
[1909.30 → 1916.80] And that has methods on it that lets you then interact with the fuzzing stuff.
[1916.98 → 1920.18] But it's a relatively simple API, isn't it?
[1920.48 → 1922.08] Just two methods.
[1922.18 → 1922.58] Is that right?
[1923.24 → 1928.86] Well, I didn't include in that proposal all the other methods that are in the testing.TB interface,
[1928.94 → 1930.54] which it will support.
[1930.74 → 1933.24] Like, for example, if you have some pre-work that you need to do
[1933.24 → 1935.34] and you want to fatal the test or something like that,
[1935.34 → 1937.44] because something failed, you can do that.
[1937.54 → 1938.08] Things like that.
[1938.58 → 1944.76] Originally, some earlier designs had the testing.f function accepted testing.f
[1944.76 → 1948.48] or the f.fuzz function accepted testing.f.
[1948.64 → 1952.40] And then it ended up kind of being not as clear, I think.
[1952.56 → 1954.54] And it was going to complicate things quite a bit.
[1954.96 → 1957.14] And that was some discussions that Filippo and I had.
[1957.16 → 1961.68] And we ended up basically keeping it as a testing’t within that function.
[1961.68 → 1965.12] So it basically should look almost exactly like a t.run.
[1965.12 → 1968.20] And if you have a t.run, you can kind of copy it over directly.
[1968.38 → 1974.14] So it really, it should look and feel exactly like a unit test within that f.fuzz function,
[1974.32 → 1975.78] which just runs kind of as a unit test.
[1975.90 → 1980.28] And then anything you need to do before that, like set things up, add to the corpus,
[1980.76 → 1983.96] whatever you need to do, you can use the testing.f for that part.
[1985.04 → 1991.24] Unlike the run function, where the only argument you can pass into that function is a testing’t,
[1991.24 → 1994.58] you can have additional arguments in these functions.
[1994.58 → 1997.80] And they seem somewhat dynamic.
[1998.40 → 1999.90] Can you explain how they work?
[2000.30 → 2000.46] Yeah.
[2000.58 → 2004.90] So inside this f.fuzz function, those first parameters,
[2005.48 → 2009.74] what you're basically telling it is it's going to take a testing.t.
[2009.88 → 2011.84] Basically, it's scoped to this t.
[2011.84 → 2018.42] And then you're just telling it what things you want the fuzzing engine to be generating for you.
[2018.64 → 2022.14] What is the structure, basically, of each input in your corpus?
[2022.64 → 2028.44] So in the proposal, the example is it takes a testing’t, an a which is a string,
[2028.68 → 2030.28] and then a big INT, which is sum.
[2030.78 → 2034.40] And what that's telling it is, okay, we have an f.fuzz function.
[2034.60 → 2036.76] That's what's going to be run with the fuzzing engine.
[2037.18 → 2040.74] That function is going to be run for every input.
[2041.10 → 2042.32] It's bound by that t.
[2042.74 → 2046.54] And then the corpus is an with a string and a big INT.
[2046.68 → 2050.04] And those are those, that's basically the structure of the corpus.
[2050.04 → 2054.68] And so every time it runs, it should be running with a new string and big INT.
[2054.68 → 2062.32] Does it dynamically look at the arguments that you've passed there and change the code?
[2062.42 → 2064.70] Does it like respond to the arguments?
[2064.90 → 2066.58] Or do you have to define them somewhere?
[2066.84 → 2068.32] Or are there patterns you have to follow?
[2068.76 → 2071.54] I'm not sure exactly that I want to make sure I'm explaining it right.
[2071.64 → 2074.52] But basically, that string and that big INT,
[2074.52 → 2076.80] if you look up a little bit higher in the proposal,
[2077.04 → 2079.78] and you're looking at this f.add function,
[2080.00 → 2082.68] what that's doing is it's adding to the corpus.
[2082.68 → 2084.86] And it's adding a string and a big INT,
[2085.50 → 2092.60] which must look exactly the same as the a and the string and the big INT in that order,
[2093.06 → 2094.80] in that f.add fuzz function.
[2094.92 → 2100.12] So what's that basically defining is this is the definition of the corpus entries
[2100.12 → 2103.74] that will be added manually, and it will be generated by the fuzzing engine.
[2104.52 → 2107.00] And it works with a slice of empty interface.
[2107.24 → 2109.22] So it's kind of generic code in a way.
[2109.66 → 2112.30] If you Go got generics, would that change?
[2112.30 → 2114.40] Would that affect this design in any way?
[2114.52 → 2117.94] Or do you think you'd still probably use it similarly?
[2118.44 → 2121.22] I'm not actually sure that it would impact the design.
[2121.38 → 2123.70] It might impact the implementation a little bit,
[2123.98 → 2125.54] but I haven't really thought too much about it.
[2125.60 → 2127.52] But I also like just thinking about it now,
[2127.68 → 2129.70] I'm not actually sure that it would change much.
[2129.80 → 2131.64] I think what this function is supposed to do,
[2131.78 → 2134.54] this f.fuzz is just kind of like a
[2135.14 → 2136.28] it's a little bit magic-y,
[2136.28 → 2139.34] but it's basically just trying to tell the fuzzing engine,
[2139.46 → 2143.12] the structure that it should be aware of and be using.
[2143.32 → 2146.94] It's a nice API to be able to just define the function
[2146.94 → 2150.94] and have it kind of notice that or work at least.
[2151.32 → 2154.62] But what happens if you've added different kind of data
[2154.62 → 2155.58] or you change the structure?
[2155.76 → 2156.92] What happens in that case?
[2156.92 → 2158.98] Like if, for example, you added,
[2159.22 → 2162.32] you did an f.add with two into or something like that?
[2162.48 → 2163.14] Yeah, exactly, yeah.
[2163.60 → 2164.92] I expect it would probably panic.
[2166.52 → 2168.74] Because what you're doing is you're basically telling it,
[2168.82 → 2172.58] here's two into, and it's expecting a string and a big INT.
[2172.66 → 2174.12] And maybe that can work with static check
[2174.12 → 2176.60] and things like that to find those things at build time.
[2176.60 → 2179.06] For anybody who hasn't read the proposal,
[2179.56 → 2182.78] f.add is the function you use to seed the corpus.
[2183.26 → 2185.36] So it's the function that you use to say,
[2185.58 → 2187.38] here's the starting points,
[2187.76 → 2190.60] which by the way is one of my favourite things of the proposal
[2190.60 → 2193.96] because usually you have to just create a bunch of files,
[2194.22 → 2196.68] one for each input, then put them in a full.
[2196.98 → 2198.32] Actually, I'm going to do something else.
[2198.86 → 2200.80] And instead here, you just write f.add
[2200.80 → 2202.74] and here's my CTSA certificate,
[2202.92 → 2204.48] here's my RSA certificate.
[2204.66 → 2206.12] These are examples, go for it.
[2206.46 → 2209.72] Well, so f.add is the function that adds to the corpus,
[2209.94 → 2211.92] while f.fuzz is the function
[2211.92 → 2214.44] that actually runs the buzzer
[2214.44 → 2218.16] and it runs a function that takes the same types of arguments.
[2218.34 → 2219.02] Yeah, thanks for the problem.
[2219.04 → 2220.34] Just mentioning it because
[2220.34 → 2222.92] in case people haven't read the proposal yet.
[2223.44 → 2224.14] Thank you, brilliant.
[2224.38 → 2226.74] And I love the fact that it kind of still,
[2226.90 → 2229.96] I mean, it's designed to fit into what we already have.
[2229.96 → 2231.66] So it knows about Go Test
[2231.66 → 2234.58] and it kind of cooperates with Go Test as well, doesn't it?
[2235.06 → 2238.10] Yeah, and actually that was my main goal with all of this.
[2238.10 → 2240.48] I wasn't going to be okay with the design
[2240.48 → 2244.48] that didn't feel like testing that we have now.
[2244.80 → 2246.00] Someone should be able to look at this
[2246.00 → 2247.68] and hopefully understand it pretty quickly.
[2248.04 → 2250.32] And the goal is that if you know how to write a unit test,
[2250.46 → 2251.72] you know how to write a fuzz target.
[2252.04 → 2254.06] And it should be approximately as easy.
[2254.50 → 2258.28] I wanted it to be able to work with the Go command as it is now.
[2258.28 → 2263.06] And if people run Go Test, it should just run the same way.
[2263.28 → 2265.68] And it shouldn't have to use anything terribly special.
[2265.82 → 2266.88] It shouldn't have to do anything.
[2267.18 → 2268.48] Learn that much new.
[2268.86 → 2270.36] I wanted kind of the barrier to entry
[2270.36 → 2272.64] to be as low as humanly possible.
[2272.94 → 2274.98] And so if it looks like Go code, that's the goal.
[2275.82 → 2276.62] And I'm glad to hear it.
[2277.08 → 2278.14] I love that about the design
[2278.14 → 2279.94] because I've done some research
[2279.94 → 2281.78] and I've seen people using,
[2282.02 → 2285.06] creating fuzz targets in the wild for parsers.
[2285.06 → 2291.08] And what usually happens is that they take whatever the buzzer engine passes them
[2291.08 → 2293.98] and put it in the parser and that's it.
[2294.42 → 2295.76] So they just basically check.
[2295.96 → 2298.96] The only property they check for is if it panics.
[2299.76 → 2301.26] So that is kind of sad
[2301.26 → 2304.38] because it's so much easier to feed something into your parser
[2304.38 → 2306.48] and then maybe serialize it where I can parse it again
[2306.48 → 2307.46] and check if it is the same.
[2307.90 → 2311.76] So it's kind of easier to write fuzz targets than people assume.
[2311.76 → 2314.96] But since fuzz seems to be such an alien concept,
[2315.58 → 2318.12] I've seen most fuzz targets to assert nothing.
[2318.32 → 2320.66] They just feed the input to the function they want to test.
[2320.74 → 2325.64] It's like if testing strings. Join would just join.
[2326.04 → 2326.46] That's it.
[2326.58 → 2327.48] And then you don't check.
[2327.90 → 2329.46] You even get the string back.
[2330.00 → 2332.68] So there is a type system for that, but that's what you get.
[2332.86 → 2336.26] So I'm really looking forward for this to be first class
[2336.26 → 2341.12] and to be so close to the original test target
[2341.12 → 2344.44] to see what people actually start asserting as a property.
[2344.44 → 2347.30] Because doesn't panic seems to be a little bit too weak.
[2347.50 → 2347.72] Yeah.
[2348.60 → 2351.86] If people get one thing away from this conversation,
[2352.22 → 2356.00] it should really be that fuzzing is going to be built in Go.
[2356.24 → 2358.44] It's not just about finding panics.
[2358.88 → 2362.12] It's not just feed some input and wait for it to crash.
[2362.68 → 2365.96] It's about writing as many invariants as you can think of
[2365.96 → 2367.72] and as many checks as you can think of
[2367.72 → 2371.32] and then letting the buzzer find the inputs
[2371.32 → 2374.10] for which the thing doesn't do what you want it to do.
[2374.46 → 2376.80] So would you say that fuzzing makes a lot of sense
[2376.80 → 2379.82] if you're working with multiple methods?
[2379.94 → 2381.98] I mean, in that example that Roberto gave,
[2382.14 → 2383.90] where you're encoding and decoding,
[2384.24 → 2387.02] because you can say something about the way
[2387.02 → 2388.78] that those two things should interoperate.
[2388.96 → 2391.14] But how can you make assertions on something
[2391.90 → 2393.74] if the input is completely random?
[2393.74 → 2395.68] What kind of assertion are you going to make?
[2395.88 → 2396.68] One thing that I did,
[2396.88 → 2398.90] I was fuzz testing a cache that I implemented.
[2399.30 → 2401.24] Caches are harder than people would normally assume.
[2401.68 → 2402.86] So I wanted to make sure that,
[2403.10 → 2405.14] for example, what I put in, I got back.
[2405.84 → 2407.38] So to test my cache,
[2407.54 → 2409.64] I did differential fuzzing with a hash map.
[2410.86 → 2413.14] So a hash map is a perfect cache, right?
[2413.22 → 2414.32] I mean, it grows indefinitely,
[2414.54 → 2415.98] but that was not, I didn't care.
[2416.06 → 2416.84] It was just fuzz testing.
[2417.18 → 2419.58] So I just fed stuff to my cache
[2419.58 → 2420.60] and when I retrieved it,
[2420.66 → 2422.56] if it wasn't there, meh, it was evicted.
[2422.56 → 2423.50] But if it was there,
[2423.62 → 2426.04] it should be identical to whatever was in that map.
[2426.92 → 2429.56] So you can have simpler number implementation
[2430.24 → 2432.38] of the algorithm you want to implement,
[2432.48 → 2433.54] or maybe a slower one.
[2434.24 → 2435.66] Like if you optimize your code,
[2435.80 → 2436.78] you can keep the old code,
[2436.84 → 2438.42] the slow one to test against.
[2438.92 → 2440.66] And usually slow code is easier to debug
[2440.66 → 2441.96] and it's more reliable
[2441.96 → 2443.22] and it's easier to write.
[2443.22 → 2444.84] It's slower, and you can see what's happening.
[2445.14 → 2445.54] Yeah, exactly.
[2445.98 → 2447.04] Not that slower.
[2448.78 → 2451.70] But yeah, that's kind of the point.
[2451.70 → 2454.48] Another example that I had written up
[2454.48 → 2458.32] for the Cloud4Blog is that I had this parser.
[2458.80 → 2460.14] No, sorry, not this parser, actually,
[2460.22 → 2461.00] this serialized.
[2461.64 → 2464.80] And you're like, how do you test the serialized?
[2465.00 → 2466.80] Like, how do you know if the thing it generated is good?
[2467.16 → 2468.54] Well, the thing I wanted to know
[2468.54 → 2471.76] was whether it would work reusing buffers
[2471.76 → 2473.20] for performance reasons.
[2473.20 → 2475.08] I didn't want to allocate a new buffer
[2475.08 → 2476.54] or zero the buffer every time.
[2476.64 → 2478.70] I just wanted to give it the old packet
[2478.70 → 2481.10] packet and say, just serialize over this one.
[2481.84 → 2483.96] So what I did was write a buzzer
[2483.96 → 2485.96] that would parse a packet.
[2486.32 → 2488.10] And then, but in this case,
[2488.26 → 2489.52] with the Go proposal,
[2489.76 → 2492.04] I would not even maybe do the parse step.
[2492.10 → 2492.90] I would just tell it,
[2493.28 → 2496.08] give me a random packet structure
[2496.08 → 2499.64] and then serialize it on both empty buffer
[2499.64 → 2500.70] of all zeros
[2500.70 → 2504.50] and on a full buffers of all one bit.
[2504.50 → 2506.42] And if they come out different,
[2506.94 → 2509.76] it means that it's not setting the zeros
[2509.76 → 2511.26] in some of the fields.
[2511.40 → 2511.88] And it did.
[2512.22 → 2514.44] And that might or might not have been
[2514.44 → 2517.30] why some stuff in the cloud for DNS server
[2517.30 → 2517.84] wasn't working.
[2518.44 → 2519.38] And that's the kind of stuff
[2519.38 → 2520.68] you can find with buzzers.
[2521.08 → 2523.88] In general, testing should really be about
[2523.88 → 2526.76] defining expected behaviours.
[2527.28 → 2529.10] And that's true of all kinds of testing.
[2529.38 → 2532.02] It's not just about defining expected inputs
[2532.02 → 2532.52] and outputs.
[2532.72 → 2535.24] It's about locking in expectations.
[2536.02 → 2537.62] Any expectation that you can define
[2537.62 → 2540.58] not strictly in terms of this input
[2540.58 → 2542.30] needs to have this output,
[2542.78 → 2544.80] but just the output needs to be longer
[2544.80 → 2545.48] than the input.
[2545.62 → 2546.78] The output needs to be shorter
[2546.78 → 2547.52] than the input.
[2548.06 → 2548.86] Anything like that,
[2548.96 → 2550.60] you can put in a buzzer in a fast target.
[2552.30 → 2554.42] It's kind of like meta testing
[2554.42 → 2556.76] or some kind of abstract testing
[2556.76 → 2557.64] in a sense.
[2557.82 → 2559.52] You're not dealing with the specific values,
[2559.52 → 2562.00] but you still deal with the ideas,
[2562.16 → 2562.66] the variables.
[2562.92 → 2564.70] Yes, which is kind of takes away
[2564.70 → 2566.70] one big risk that there is
[2566.70 → 2567.76] when you write unit tests.
[2567.98 → 2568.88] When you write unit tests,
[2568.94 → 2570.56] you have those assumptions in mind.
[2570.80 → 2572.60] Like what you're trying to test is like,
[2572.96 → 2575.10] I want string split to actually split the string.
[2575.88 → 2577.94] And then you go and test your stuff
[2577.94 → 2578.90] and you put the input
[2578.90 → 2579.62] and you put the output,
[2579.92 → 2581.38] but you're just giving examples.
[2581.96 → 2583.74] You're not testing the actual property
[2583.74 → 2584.32] that you want.
[2584.68 → 2587.28] So I think that writing a property assertion
[2587.28 → 2589.46] for a fuzz target is actually closer
[2589.46 → 2591.10] to what you want to do usually in tests.
[2591.86 → 2593.92] Now, unit tests are always going to be needed.
[2594.56 → 2596.14] But if you put on top something
[2596.14 → 2597.46] that asserts the actual property
[2597.46 → 2598.10] that you meant,
[2598.44 → 2599.98] I think you're adding a lot of value.
[2600.50 → 2601.46] One opinion I heard
[2601.46 → 2603.26] that I'm not supporting,
[2603.40 → 2605.50] you know, retweets are not endorsements,
[2605.96 → 2606.94] but was that,
[2607.30 → 2608.70] why would you write unit tests
[2608.70 → 2610.02] if you already know
[2610.02 → 2612.18] what your program is going to break on?
[2612.58 → 2614.08] Just don't write the bug.
[2614.08 → 2616.02] And I mean,
[2616.12 → 2618.22] yes, yes, yes.
[2619.02 → 2619.74] I know.
[2620.14 → 2624.18] But there is a degree of truth to that.
[2624.80 → 2627.04] The things you can write unit tests,
[2627.28 → 2629.16] unit tests are actually kind of more useful
[2629.16 → 2630.96] for refactoring later
[2630.96 → 2633.08] and for regressions.
[2633.62 → 2634.40] But that's the thing.
[2635.06 → 2637.52] It's unlikely you will think of inputs
[2637.52 → 2640.62] that break on the program you just wrote
[2640.62 → 2642.70] because you thought about those edge cases.
[2642.70 → 2643.14] Yeah.
[2643.60 → 2647.36] And fuzzing will just not care
[2647.36 → 2648.48] about what you thought about.
[2648.78 → 2650.80] Fuzzing will find where it hurts.
[2651.58 → 2652.00] Right.
[2652.44 → 2653.98] And one thing that I like to say
[2653.98 → 2656.10] is that I write test targets
[2656.10 → 2658.72] for my future interaction with the code
[2658.72 → 2662.86] because I also used to do TDD most of the time.
[2662.96 → 2664.12] So I write the tests
[2664.12 → 2665.54] and then I write the code that implements
[2665.54 → 2667.22] whatever I'm testing for.
[2667.62 → 2668.16] And in the future,
[2668.22 → 2668.78] when I refactor,
[2668.90 → 2669.84] I want the tests to pass.
[2669.84 → 2672.40] When I said that I write fuzzes
[2672.40 → 2674.30] for the tests I wrote in the past,
[2674.38 → 2675.60] for the code I wrote in the past.
[2676.18 → 2676.74] So basically,
[2676.90 → 2677.66] the buzzer makes sure
[2677.66 → 2678.42] that whatever is there
[2678.42 → 2680.02] is actually what it's meant to do
[2680.02 → 2681.98] and the tests are there
[2681.98 → 2683.98] so that the future code will keep doing it.
[2684.42 → 2687.66] I really like what Filippo said about
[2687.66 → 2689.88] kind of like the fuzzing engine
[2689.88 → 2692.12] doesn't care what the developer thought about.
[2692.28 → 2692.40] I mean,
[2692.44 → 2695.60] I think that's kind of the benefit of having,
[2696.24 → 2697.30] that's why, for example,
[2697.30 → 2698.26] well, code reviews exist
[2698.26 → 2699.80] because you need another person
[2699.80 → 2702.52] who's kind of more objective to look at it.
[2702.58 → 2704.38] And I think that a fuzzing engine
[2704.38 → 2707.18] can kind of be this third-party objective,
[2707.70 → 2708.58] you know,
[2708.64 → 2710.10] being that just goes in
[2710.10 → 2711.44] and does everything it can
[2711.44 → 2712.28] to try to break it.
[2712.58 → 2713.46] And it has no idea
[2713.46 → 2714.38] what you thought about it.
[2714.62 → 2715.58] It doesn't care about that.
[2715.64 → 2716.44] It just cares about
[2716.44 → 2719.30] trying to find as much coverage as it can
[2719.30 → 2720.20] and try to find bugs.
[2720.68 → 2722.30] And that kind of like third-party entity
[2722.30 → 2723.80] is kind of a cool concept to me.
[2724.42 → 2724.60] Katie,
[2724.68 → 2726.20] aren't you worried about the fuzzing thing
[2726.20 → 2727.24] becoming self-aware
[2727.24 → 2728.36] and then just going around
[2728.36 → 2729.66] doing loads of random crime?
[2730.12 → 2732.04] That's like actually my goal with this.
[2732.28 → 2734.74] I'm actually trying to build a
[2734.74 → 2735.22] yeah,
[2735.68 → 2736.54] self-learning robot
[2736.54 → 2738.12] that'll just take over the language.
[2738.20 → 2738.98] How do you know?
[2739.38 → 2740.16] Based on fuzzing.
[2740.36 → 2740.70] Exactly.
[2741.02 → 2741.90] How do you know
[2741.90 → 2743.54] that's not already what happened
[2743.54 → 2745.46] and we're here pitching fuzzing
[2745.46 → 2749.26] to just make our buzzer overlords happy?
[2750.18 → 2751.52] I'm actually a fuzzing engine.
[2751.84 → 2752.42] All this time,
[2752.48 → 2753.22] it's been a simulation.
[2753.96 → 2754.84] Well, it is a good one.
[2754.84 → 2755.58] Yeah, you're right.
[2755.64 → 2756.44] It does a good job.
[2758.04 → 2758.40] Yeah.
[2759.20 → 2759.82] But the thing is,
[2759.84 → 2760.06] yeah,
[2760.26 → 2761.60] I'd love that though.
[2761.88 → 2762.36] Not really.
[2764.50 → 2766.08] Doesn't know how to interact with you
[2766.08 → 2767.32] now that he knows you're a robot.
[2767.32 → 2771.86] I love it when the machines
[2771.86 → 2774.38] do kind of get this emergent intelligence.
[2774.60 → 2776.50] I find that to be really quite amazing,
[2776.64 → 2778.04] especially when there's so much chaos
[2778.04 → 2780.10] in what's actually going on.
[2780.10 → 2780.90] So yeah,
[2781.00 → 2782.64] the fact that I think the thing
[2782.64 → 2783.34] that I've learned
[2783.34 → 2785.48] and I'll take away is
[2785.48 → 2787.78] it's less about random input
[2787.78 → 2790.02] and it's more about kind of variations
[2790.02 → 2792.82] of the realistic kind of input
[2792.82 → 2794.76] that you're going to pass in, right?
[2794.94 → 2795.10] Right.
[2795.18 → 2796.72] Or that didn't resonate
[2796.72 → 2797.92] because I can tell on my screen
[2797.92 → 2799.10] that there's no...
[2799.90 → 2800.24] Go on.
[2800.46 → 2801.56] Correct me if that's...
[2801.56 → 2802.28] No, it's just...
[2802.28 → 2803.18] I wanted to say that
[2803.18 → 2805.74] I was putting stuff on top of this,
[2805.88 → 2806.36] which is
[2806.36 → 2808.00] the buzzer doesn't care
[2808.00 → 2809.66] about what the code does.
[2809.70 → 2810.32] And that's important
[2810.32 → 2811.64] because if we had like
[2811.64 → 2812.76] machine learning algorithm
[2812.76 → 2813.82] fuzzing our code,
[2814.34 → 2815.14] just, you know,
[2815.18 → 2816.62] trying to learn how the code behaves,
[2816.86 → 2817.80] at one point they would do it
[2817.80 → 2818.48] as humans would.
[2818.74 → 2819.84] They would understand
[2819.84 → 2821.14] what the code is supposed to do
[2821.14 → 2822.14] and kind of, you know,
[2822.86 → 2824.24] accept the code works.
[2824.78 → 2826.26] And instead,
[2826.42 → 2827.60] if you just use an algorithm
[2827.60 → 2829.22] that just tries to bash
[2829.22 → 2830.10] with random stuff,
[2830.16 → 2831.14] at one point you find
[2831.14 → 2832.98] like after two years
[2832.98 → 2834.42] you have been fuzzing a target,
[2834.96 → 2836.48] a new edge case that crashes.
[2837.28 → 2838.36] And this is something that I love
[2838.36 → 2839.30] because a human
[2839.30 → 2840.16] or an intelligent
[2840.16 → 2841.56] like kind of design
[2841.56 → 2844.16] in our way of defining intelligence
[2844.16 → 2845.34] would not find it.
[2845.82 → 2847.08] Because why would you keep doing
[2847.08 → 2847.68] for two years
[2847.68 → 2848.20] the same thing
[2848.20 → 2849.34] expecting a different result?
[2849.58 → 2850.66] Isn't that the definition of madness?
[2851.74 → 2853.00] Yeah, but we are going to end up
[2853.00 → 2854.18] with fuzzing Terminators
[2854.18 → 2855.68] literally just running around
[2855.68 → 2857.16] trying all kinds of different things
[2857.16 → 2857.70] to get you
[2857.70 → 2859.54] and just like goes and hacks something,
[2859.70 → 2860.20] smashes it,
[2860.28 → 2860.82] kicks a puppy,
[2860.82 → 2861.94] throws a baby in the sea.
[2862.28 → 2862.64] Do you know what I mean?
[2862.70 → 2864.10] Just doing all kinds of...
[2864.10 → 2865.40] Just to see what works.
[2865.90 → 2866.22] Do you know what I mean?
[2866.30 → 2866.54] It's not...
[2866.54 → 2867.72] It's a risk we're willing to accept.
[2867.84 → 2868.32] It's a risk.
[2868.96 → 2869.24] Okay.
[2869.50 → 2870.02] You are, are you?
[2870.58 → 2871.14] You really are
[2871.14 → 2872.62] chocolate factory boffins over there.
[2872.68 → 2873.38] It's a sacrifice
[2873.38 → 2874.42] we're willing to make.
[2874.60 → 2874.78] Really.
[2874.78 → 2875.78] Okay.
[2875.78 → 2891.74] What's up, gophers?
[2891.74 → 2892.76] Are you looking for a way
[2892.76 → 2894.08] to instantly debug
[2894.08 → 2895.50] and troubleshoot your applications
[2895.50 → 2896.76] and services running
[2896.76 → 2897.30] in production
[2897.30 → 2898.72] on Kubernetes?
[2898.92 → 2899.60] That's a mouthful.
[2899.90 → 2901.06] Well, Pixie gives you
[2901.06 → 2902.20] a magical API
[2902.20 → 2903.76] to get instant debug data.
[2903.76 → 2904.98] And the best part
[2904.98 → 2906.30] is this doesn't involve
[2906.30 → 2907.14] changing code.
[2907.48 → 2908.72] There are no manual UIs
[2908.72 → 2909.98] and all this lives
[2909.98 → 2911.14] inside Kubernetes.
[2911.82 → 2913.18] Pixie is an API
[2913.18 → 2915.00] which lives inside your platform,
[2915.38 → 2916.40] harvests all of your data
[2916.40 → 2917.04] that you need
[2917.04 → 2919.18] and exposes a bunch of interfaces
[2919.18 → 2920.06] that you can ping
[2920.06 → 2921.34] to get data you need.
[2921.70 → 2922.94] Pixie is essentially
[2922.94 → 2924.58] like a decentralized Splunk.
[2924.78 → 2925.80] It's a programmable
[2925.80 → 2927.16] edge intelligence platform
[2927.16 → 2928.50] which captures metrics,
[2928.70 → 2929.04] traces,
[2929.26 → 2929.58] logs,
[2929.58 → 2930.30] and events
[2930.30 → 2931.62] without any code changes.
[2932.22 → 2933.32] And the team behind Pixie
[2933.32 → 2934.10] is working hard
[2934.10 → 2934.88] to bring it to market
[2934.88 → 2935.72] for broad use
[2935.72 → 2936.94] by the end of 2020.
[2937.46 → 2938.62] But I'm here to tell you
[2938.62 → 2939.24] how you can get your hands
[2939.24 → 2939.98] on the beta today.
[2940.46 → 2941.58] Links are in the show notes
[2941.58 → 2942.38] so check them out
[2942.38 → 2943.30] so you can click through
[2943.30 → 2943.82] to the beta
[2943.82 → 2944.98] and their Slack community.
[2945.30 → 2945.72] Once again,
[2945.82 → 2946.54] links are in the show notes.
[2946.60 → 2947.24] Check them out
[2947.24 → 2948.48] and look forward to Pixie Day
[2948.48 → 2949.06] coming soon.
[2949.06 → 2969.20] I actually think
[2969.20 → 2970.20] you should probably leave.
[2970.20 → 2975.06] I'm talking to the region.
[2979.06 → 2979.98] So,
[2980.56 → 2981.78] does anybody have
[2981.78 → 2983.00] an unpopular opinion
[2983.00 → 2983.96] for us today?
[2984.72 → 2985.90] It can be fuzzing related
[2985.90 → 2987.04] but it doesn't have to be.
[2987.30 → 2988.00] It can be anything.
[2988.38 → 2988.82] Yeah,
[2988.88 → 2989.40] I've got one.
[2990.24 → 2991.34] I can throw in the ring.
[2991.62 → 2992.16] Throw it in.
[2992.48 → 2992.82] So,
[2993.14 → 2994.16] I think that
[2994.16 → 2995.64] it's kind of more like a
[2996.12 → 2996.92] I don't know if it's an opinion
[2996.92 → 2998.50] so much as a personal experience
[2998.50 → 2999.82] but I actually got into
[2999.82 → 3000.42] computer science
[3000.42 → 3001.48] because math wasn't
[3001.48 → 3002.48] social enough for me.
[3003.42 → 3003.86] So,
[3003.96 → 3004.62] I think that
[3004.62 → 3006.52] the thing that I like the most
[3006.52 → 3007.54] I think is the best part
[3007.54 → 3008.46] about computer science
[3008.46 → 3009.46] is actually building
[3009.46 → 3011.08] things with other people
[3011.08 → 3011.98] and I think like
[3011.98 → 3012.86] having social skills
[3012.86 → 3014.10] can take you a really long way
[3014.10 → 3015.60] and is kind of
[3015.60 → 3016.36] undervalued
[3016.36 → 3017.24] in tech.
[3017.40 → 3017.54] So,
[3017.66 → 3018.36] you're telling me
[3018.36 → 3020.26] that you got into CS
[3020.26 → 3022.50] because of the social aspect.
[3023.34 → 3023.74] Exactly.
[3023.88 → 3024.70] I didn't want to sit alone
[3024.70 → 3025.56] in a corner all day
[3025.56 → 3026.98] and just solve math problems
[3026.98 → 3027.50] but I was like,
[3027.56 → 3027.68] oh,
[3027.70 → 3029.14] I can build stuff with people.
[3029.60 → 3030.56] That sounds more fun
[3030.56 → 3031.36] so I'm going to do that
[3031.36 → 3032.60] which I realize
[3032.60 → 3033.18] is the opposite
[3033.18 → 3033.78] of a lot of people.
[3034.36 → 3035.02] And then you ended up
[3035.02 → 3035.74] in security
[3035.74 → 3037.54] because the Infosec community
[3037.54 → 3038.36] is,
[3038.36 → 3039.50] you know,
[3039.78 → 3040.86] shining example
[3040.86 → 3041.92] of excellent
[3041.92 → 3043.06] community support.
[3043.58 → 3044.28] That's a highly
[3044.28 → 3045.26] socialist field though
[3045.26 → 3046.38] because you need to be able
[3046.38 → 3048.08] to talk to people
[3048.08 → 3049.26] and understand
[3049.26 → 3050.80] like if they disclose
[3050.80 → 3051.30] a report
[3051.30 → 3051.80] you need to be able
[3051.80 → 3052.86] to communicate with them
[3052.86 → 3053.84] and understand them
[3053.84 → 3054.56] and be able to
[3054.56 → 3055.40] communicate back
[3055.40 → 3056.14] and you need to be able
[3056.14 → 3056.84] to communicate
[3056.84 → 3058.52] really complicated things
[3058.52 → 3059.62] in a really simple way
[3059.62 → 3060.26] that other people
[3060.26 → 3060.86] can understand
[3060.86 → 3061.68] which is really hard.
[3062.28 → 3062.86] And I think this is,
[3063.04 → 3063.48] that's a field
[3063.48 → 3064.60] where it's even more important
[3064.60 → 3065.12] that you have
[3065.12 → 3065.88] good social skills
[3065.88 → 3066.58] because it's so,
[3067.22 → 3068.36] the stakes are so high.
[3068.92 → 3069.20] Yeah,
[3069.30 → 3069.94] to be fair,
[3070.24 → 3071.26] I should point out
[3071.26 → 3072.72] that the Go security
[3072.72 → 3073.24] community
[3073.24 → 3074.40] is extremely nice.
[3074.54 → 3075.20] The kind of people
[3075.20 → 3076.68] that email us reports
[3076.68 → 3077.46] are usually
[3077.46 → 3078.38] a delight
[3078.38 → 3079.42] to work with.
[3079.76 → 3080.30] I was just
[3080.30 → 3081.40] making a cheap shot
[3081.40 → 3082.22] at the
[3083.44 → 3084.20] right,
[3084.46 → 3085.16] let's say
[3085.16 → 3086.64] traditional
[3086.64 → 3088.82] security community.
[3089.20 → 3089.46] Traditional.
[3089.56 → 3090.64] What can they do
[3090.64 → 3090.98] to get you?
[3090.98 → 3091.42] That's one way
[3091.42 → 3091.86] to put it.
[3091.98 → 3092.42] You're safe,
[3092.48 → 3092.72] aren't you,
[3092.78 → 3093.28] from that lot?
[3093.28 → 3094.26] What can they ever do?
[3094.66 → 3095.00] Right.
[3095.22 → 3095.54] Yeah!
[3097.76 → 3098.80] Now that you say that,
[3098.88 → 3099.02] Katie,
[3099.36 → 3099.90] I think that one
[3099.90 → 3101.16] of the important things
[3101.16 → 3102.18] about the human aspect
[3102.18 → 3102.84] of software
[3102.84 → 3103.48] is like,
[3103.70 → 3104.58] when you design an API,
[3105.14 → 3105.94] you have to design it
[3105.94 → 3106.52] in a way that people
[3106.52 → 3107.06] will understand.
[3107.56 → 3107.72] Like,
[3108.10 → 3109.22] I hate when people say,
[3109.56 → 3109.76] like,
[3109.96 → 3110.86] users of this API
[3110.86 → 3111.44] are stupid
[3111.44 → 3112.24] because they can't
[3112.24 → 3112.96] use it right.
[3114.06 → 3114.18] No,
[3114.36 → 3115.84] when you're designing
[3115.84 → 3116.28] something,
[3116.38 → 3117.08] you're communicating
[3117.08 → 3117.82] to the user.
[3118.52 → 3119.64] People keep forgetting
[3119.64 → 3120.78] that issue.
[3121.70 → 3122.10] Yeah,
[3122.18 → 3122.70] that is true,
[3122.76 → 3123.06] actually,
[3123.06 → 3124.06] because you do think,
[3124.36 → 3124.94] in the beginning,
[3125.20 → 3126.30] I thought APIs
[3126.30 → 3127.14] were for machines
[3127.14 → 3128.12] to talk to each other,
[3128.28 → 3128.92] but they aren't.
[3129.00 → 3129.72] They're for humans
[3129.72 → 3131.04] to build the thing
[3131.04 → 3131.92] that allows the machines
[3131.92 → 3132.76] to talk to each other.
[3133.30 → 3133.46] Yeah,
[3133.52 → 3134.56] so that is true.
[3134.92 → 3135.50] But I don't know,
[3135.60 → 3136.42] Pythagoras could have been
[3136.42 → 3137.64] a laugh at a party,
[3137.76 → 3139.42] might have had a great time
[3139.42 → 3139.64] with him.
[3140.60 → 3141.66] He's probably measuring
[3141.66 → 3142.36] all the stuff
[3142.36 → 3142.66] and you're like,
[3142.74 → 3143.20] Pythagoras,
[3143.32 → 3144.42] just put your ruler down
[3144.42 → 3145.24] for five minutes,
[3145.38 → 3145.60] mate.
[3145.92 → 3146.80] Have a sandwich,
[3146.98 → 3147.82] I've cut them into triangles
[3147.82 → 3148.58] while you like them.
[3148.92 → 3149.08] You know,
[3149.10 → 3149.68] that kind of thing.
[3151.22 → 3151.50] Okay,
[3151.58 → 3152.88] any other populists?
[3152.88 → 3154.28] I have a whole list
[3154.28 → 3155.56] of photography
[3155.56 → 3156.42] and popular opinions,
[3156.42 → 3158.04] but the thing is,
[3158.70 → 3159.80] I don't think anybody
[3159.80 → 3161.68] actually has an opinion
[3161.68 → 3162.38] on these things
[3162.38 → 3163.96] and it's just these 10 people
[3163.96 → 3164.66] and we're all
[3164.66 → 3165.60] on the same slack
[3165.60 → 3166.34] and we just,
[3166.50 → 3166.94] you know,
[3166.98 → 3167.88] discuss these things
[3167.88 → 3168.42] between us.
[3168.54 → 3169.48] So I'm not going to go there.
[3169.48 → 3170.62] Instead,
[3170.94 → 3172.18] my unpopular opinion
[3172.18 → 3173.28] is that,
[3173.74 → 3175.20] and Katie will,
[3176.06 → 3177.00] I know she understands,
[3177.20 → 3179.04] but dogs in the office
[3179.04 → 3179.92] are bad.
[3181.22 → 3181.96] Just bad.
[3182.46 → 3183.44] Dogs in the office.
[3183.50 → 3184.90] There should be no dogs
[3184.90 → 3185.62] in the office.
[3186.12 → 3186.34] Yeah,
[3186.44 → 3186.68] go on,
[3186.72 → 3187.02] elaborate.
[3187.22 → 3188.10] Are you allergic to them,
[3188.24 → 3188.56] Filippo?
[3188.70 → 3189.68] I'm allergic to them.
[3189.76 → 3190.54] I know a bunch of people
[3190.54 → 3191.42] who are allergic to them.
[3191.50 → 3192.16] I know a bunch of people
[3192.16 → 3193.30] who are scared of them
[3193.30 → 3194.90] and don't feel like
[3194.90 → 3195.56] they can say,
[3195.92 → 3196.16] hey,
[3196.38 → 3197.96] so beautiful dog.
[3198.24 → 3198.98] I'm scared of it
[3198.98 → 3200.16] so you don't get to bring it
[3200.16 → 3201.34] to the office anymore
[3201.34 → 3202.50] because I'm scared of dogs.
[3202.62 → 3204.48] No one wants to be that guy.
[3205.00 → 3205.12] Yeah,
[3205.16 → 3206.00] I know you love it
[3206.00 → 3206.50] but to me,
[3206.58 → 3208.32] that's basically a little monster
[3208.32 → 3209.82] from a nightmare.
[3209.82 → 3211.04] somebody might have gotten bitten,
[3211.36 → 3211.98] you know,
[3212.12 → 3213.32] and they're just like,
[3213.40 → 3213.60] yep,
[3213.64 → 3215.06] that makes me extremely uncomfortable
[3215.06 → 3216.32] but I just joined
[3216.32 → 3217.98] and I don't want to be that guy.
[3218.38 → 3219.78] So they're not going to tell you
[3219.78 → 3221.84] and they're just going to walk around
[3221.84 → 3222.22] and be like,
[3222.48 → 3222.74] yep,
[3222.94 → 3223.12] yep,
[3223.30 → 3223.54] cute,
[3223.66 → 3223.84] cute,
[3223.94 → 3224.16] cute,
[3224.16 → 3225.86] walks along the border.
[3226.16 → 3227.92] And to be clear,
[3228.02 → 3229.56] I think Filippo said that about me
[3229.56 → 3230.66] because I love dogs
[3230.66 → 3231.48] like more than,
[3231.76 → 3232.86] anybody who's ever talked to me
[3232.86 → 3233.78] for more than five minutes
[3233.78 → 3235.18] knows that I love dogs
[3235.18 → 3237.46] more than pretty much anything,
[3237.54 → 3238.04] I would say.
[3238.30 → 3238.56] Whoa.
[3238.86 → 3239.04] Yeah.
[3239.60 → 3239.90] I mean,
[3239.92 → 3242.36] I do actually agree with you
[3242.36 → 3244.64] that it makes things complicated.
[3244.78 → 3244.98] I mean,
[3245.02 → 3245.18] like,
[3245.24 → 3245.38] yeah,
[3245.42 → 3246.72] it can bring a source of joy
[3246.72 → 3247.96] for people like me
[3247.96 → 3249.14] who aren't allergic
[3249.14 → 3249.86] and that love them
[3249.86 → 3250.44] but also
[3250.44 → 3252.74] if it's a source of conflict
[3252.74 → 3253.82] and discomfort
[3253.82 → 3254.70] or worse
[3254.70 → 3256.06] for people that I work with
[3256.06 → 3257.32] or people around me
[3257.32 → 3259.70] then that isn't ideal either
[3259.70 → 3260.66] and,
[3260.66 → 3261.76] you know,
[3261.76 → 3262.42] aside from the case
[3262.42 → 3263.20] of like a service dog
[3263.20 → 3264.42] which I know that Filippo
[3264.42 → 3266.60] agrees that's totally fine.
[3267.00 → 3267.32] Honestly,
[3267.44 → 3269.24] I think it's a really reasonable opinion.
[3269.68 → 3271.32] Service dogs are well-trained
[3271.32 → 3272.70] and in general,
[3273.26 → 3273.52] you know,
[3273.62 → 3275.90] if accommodations have to be made,
[3276.12 → 3276.70] you know,
[3276.86 → 3279.56] one can work case by case
[3279.56 → 3280.44] but honestly,
[3280.52 → 3282.24] I never had the problem of,
[3282.24 → 3282.66] oh no,
[3282.74 → 3283.40] I'm really allergic
[3283.40 → 3284.46] to the service dog
[3284.46 → 3286.84] that I can't be around
[3286.84 → 3288.54] but I did have the problem
[3288.54 → 3289.52] with pets a bunch
[3289.52 → 3290.80] because there's just
[3290.80 → 3291.74] many more pets.
[3292.00 → 3293.20] It's just a numbers' problem.
[3293.76 → 3294.68] But how will the management
[3294.68 → 3295.74] show how cool they are
[3295.74 → 3296.80] if they don't allow dogs
[3296.80 → 3297.54] in the office?
[3298.16 → 3298.56] Right.
[3298.76 → 3299.72] What are you going to ban next,
[3299.84 → 3300.12] Filippo?
[3300.18 → 3300.40] Right.
[3300.58 → 3301.48] Foosball tables.
[3301.66 → 3302.40] Pom-pom tables
[3302.40 → 3303.44] have gotten old.
[3304.50 → 3304.76] Yeah.
[3305.02 → 3305.38] There you go.
[3306.78 → 3306.98] Yeah.
[3307.96 → 3308.36] Roberto,
[3308.80 → 3309.52] what do you think?
[3309.58 → 3310.44] How do you feel about dogs
[3310.44 → 3310.98] in the office?
[3312.54 → 3314.72] I'm kind of scared of big dogs
[3314.72 → 3316.50] so I'm on Filippo's side
[3316.50 → 3317.56] but also I have friends
[3317.56 → 3319.32] that are allergic to dogs
[3319.32 → 3320.66] so yeah,
[3320.90 → 3321.68] I agree.
[3322.28 → 3323.28] Unless they are needed
[3323.28 → 3324.62] like they are service dogs,
[3325.12 → 3326.52] I'm not in favour of that.
[3327.66 → 3327.86] Well,
[3328.12 → 3328.58] folks,
[3328.78 → 3329.68] your unpopular opinions
[3329.68 → 3330.92] have so much to discuss
[3330.92 → 3331.06] on.
[3331.10 → 3332.00] My unpopular opinion
[3332.00 → 3332.60] was going to be
[3332.60 → 3333.70] I like yellow
[3333.70 → 3335.00] so wow,
[3335.18 → 3335.68] this is just
[3335.68 → 3336.90] important topics
[3336.90 → 3337.36] that you brought
[3337.36 → 3338.50] to the conversation there.
[3338.80 → 3340.04] Mine was completely useless.
[3341.72 → 3342.96] That's a terrible opinion,
[3343.12 → 3343.28] Rob.
[3343.36 → 3343.94] Take it back.
[3344.50 → 3345.68] Is it the colour you like
[3345.68 → 3346.52] or you just love
[3346.52 → 3347.44] that Coldplay song?
[3347.68 → 3348.04] No,
[3348.10 → 3348.50] the colour.
[3348.76 → 3349.44] Just the colour
[3349.44 → 3350.46] and the effect
[3350.46 → 3351.50] it has on people.
[3352.04 → 3352.88] There are so many
[3352.88 → 3353.60] better colours.
[3354.82 → 3355.26] Right.
[3355.58 → 3356.02] Yeah,
[3356.02 → 3356.96] beautiful colours.
[3357.46 → 3358.24] Yellow is one of them.
[3358.54 → 3358.80] I mean,
[3358.82 → 3359.68] your headphones are yellow.
[3360.26 → 3360.64] That's true.
[3360.70 → 3361.18] Now I was looking
[3361.18 → 3362.04] for clues of yellow
[3362.04 → 3362.92] to verify.
[3363.24 → 3363.72] For some reason
[3363.72 → 3364.38] I'm skeptical
[3364.38 → 3365.62] when Roberto says
[3365.62 → 3366.26] he likes yellow.
[3366.26 → 3366.56] I think,
[3366.64 → 3366.78] well,
[3366.84 → 3367.66] this is a trick.
[3367.78 → 3367.98] Well,
[3368.12 → 3369.34] I have something else
[3369.34 → 3370.04] to prove it.
[3370.62 → 3370.82] Oh,
[3370.88 → 3371.74] a yellow gopher.
[3372.16 → 3372.60] Oh,
[3373.10 → 3374.22] I don't have one.
[3374.22 → 3374.98] It's a podcast.
[3375.44 → 3376.42] This is a podcast.
[3376.82 → 3376.98] Yeah.
[3377.38 → 3377.78] So,
[3377.86 → 3378.92] I already tweeted
[3378.92 → 3379.88] this picture today
[3379.88 → 3381.16] so people just need
[3381.16 → 3381.88] to go back.
[3382.02 → 3382.82] I'll tweet it again.
[3382.84 → 3383.98] I'm scared of those gophers
[3383.98 → 3384.42] by the way.
[3385.04 → 3386.12] That's my unpopular opinion.
[3386.32 → 3387.10] Those little things.
[3387.32 → 3388.36] I have nightmares about them.
[3388.70 → 3389.92] They do look a little weird,
[3390.06 → 3390.20] huh?
[3390.60 → 3391.42] That one in particular,
[3391.54 → 3392.52] that yellow one.
[3392.52 → 3393.28] Well,
[3393.34 → 3393.82] it's a podcast.
[3394.06 → 3394.80] So this really is.
[3394.80 → 3395.52] It's still a podcast.
[3396.00 → 3396.30] Basically,
[3396.56 → 3397.72] I'm getting the gopher
[3397.72 → 3398.42] closer and closer
[3398.42 → 3398.96] to the webcam
[3398.96 → 3400.10] until Matt screams.
[3400.46 → 3401.04] He didn't scream.
[3401.28 → 3402.06] You passed the test.
[3402.18 → 3402.34] Sorry,
[3402.40 → 3403.62] I wasn't suggesting
[3403.62 → 3404.78] do an audio commentary
[3404.78 → 3405.16] of it.
[3405.20 → 3405.78] I was suggesting
[3405.78 → 3406.86] let's not do that
[3406.86 → 3407.74] in the first place
[3407.74 → 3408.90] and focus on the audio.
[3409.22 → 3409.66] Right.
[3410.80 → 3411.12] Okay,
[3411.20 → 3411.40] well,
[3411.58 → 3412.10] unfortunately,
[3412.30 → 3413.42] that's all the time
[3413.42 → 3414.54] we have today.
[3414.90 → 3416.16] Thank you so much
[3416.16 → 3417.12] for joining us,
[3417.26 → 3417.62] Katie,
[3418.12 → 3418.62] Filippo,
[3418.70 → 3419.22] and Roberto.
[3419.22 → 3421.16] And we'll see you next time.
[3424.86 → 3426.14] If you're not following
[3426.14 → 3427.00] Go Time on Twitter,
[3427.26 → 3428.32] let's fix that bug.
[3428.76 → 3430.30] We tweet live show notifications,
[3430.82 → 3431.24] clips,
[3431.52 → 3432.16] and highlights
[3432.16 → 3433.28] from past episodes.
[3433.50 → 3434.32] We take polls
[3434.32 → 3435.54] about unpopular opinions
[3435.54 → 3436.66] and have a lot of fun.
[3437.08 → 3437.90] Join the conversation.
[3438.16 → 3439.64] We're at Go Time FM.
[3440.40 → 3441.82] This episode was hosted
[3441.82 → 3442.78] by Matt Refer
[3442.78 → 3443.72] with special guests
[3443.72 → 3444.46] Katie Hock man,
[3444.64 → 3445.48] Roberto Claps,
[3445.70 → 3446.86] and Filippo Salford.
[3447.02 → 3447.64] It was produced
[3447.64 → 3448.50] by Jared Santo.
[3448.50 → 3449.32] That's me.
[3449.54 → 3450.68] And we get our music
[3450.68 → 3451.64] from the Beat Freak
[3451.64 → 3452.84] Break master Cylinder.
[3453.34 → 3454.50] Thanks to this episode's
[3454.50 → 3454.92] sponsors,
[3455.06 → 3455.66] Digital Ocean,
[3455.86 → 3456.28] Retool,
[3456.46 → 3457.00] and Pixie.
[3457.16 → 3457.68] And of course,
[3457.78 → 3458.80] our long-time partners
[3458.80 → 3459.34] Vastly,
[3459.58 → 3459.94] Linde,
[3460.14 → 3460.80] and Rollbar.
[3461.32 → 3462.18] That's all for now.
[3462.48 → 3463.30] We'll talk to you again
[3463.30 → 3463.80] next week.
[3463.80 → 3475.98] We'll see you again next week.
[3476.14 → 3477.34] Yeah.
[3477.34 → 3507.32] Thank you.
[3507.34 → 3537.32] Thank you.

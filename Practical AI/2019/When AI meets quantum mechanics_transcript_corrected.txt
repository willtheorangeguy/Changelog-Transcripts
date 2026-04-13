[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.40] And we're hosted on Linde cloud servers.
[12.76 → 14.74] Head to linode.com slash Changelog.
[15.72 → 20.34] This episode is brought to you by DigitalOcean, the simplest cloud platform out there.
[20.46 → 25.10] And we're excited to share they now offer dedicated virtual droplets.
[25.10 → 29.02] And unlike standard droplets, which use shared virtual CPU threads,
[29.02 → 32.86] their two performance plans, general purpose and CPU optimized,
[33.40 → 36.08] they have dedicated virtual CPU threads.
[36.40 → 40.86] This translates to higher performance and increased consistency during CPU intensive processes.
[41.36 → 45.20] So if you have build boxes, CCD, video encoding, machine learning, ad serving,
[45.50 → 49.98] game servers, databases, batch processing, data mining, application servers,
[50.20 → 54.92] or active front end web servers that need to be full duty CPU all day every day,
[55.14 → 57.92] then check out DigitalOcean's dedicated virtual CPU droplets.
[57.92 → 61.26] Pricing is very competitive starting at 40 bucks a month.
[61.66 → 66.38] Learn more and get started for free with a $100 credit at do.co slash Changelog.
[66.64 → 69.02] Again, do.co slash Changelog.
[69.02 → 86.38] Welcome to Practical AI, a weekly podcast about making artificial intelligence practical,
[86.78 → 88.56] productive, and accessible to everyone.
[88.94 → 93.44] This is where conversations around AI, machine learning, and data science happen.
[93.92 → 98.20] Join the community and Slack with us around various topics of the show at changelog.com slash community.
[98.20 → 99.38] Follow us on Twitter.
[99.48 → 100.96] We're at Practical AI FM.
[101.46 → 102.28] And now onto the show.
[106.54 → 108.50] Welcome to Practical AI.
[108.88 → 110.44] This is Daniel Whiten ack.
[110.68 → 113.34] I'm a data scientist with SIL International,
[113.72 → 116.22] and I'm joined here by Chris Benson,
[116.48 → 120.06] who is a chief AI strategist at Lockheed Martin.
[120.22 → 120.98] How are you doing, Chris?
[121.32 → 122.08] Doing great, Daniel.
[122.14 → 122.82] How's it going today?
[122.82 → 124.90] It's going good.
[125.04 → 127.34] It's allergy and mowing season,
[127.62 → 131.88] and I finally got peer pressured enough into mowing my lawn last night.
[132.08 → 135.08] So, you know, feeling that a little bit,
[135.30 → 136.80] but all around good.
[137.04 → 141.20] Otherwise, models are training and having fun.
[141.40 → 141.96] There you go.
[142.16 → 142.26] What about you?
[142.26 → 143.44] I'm doing fine.
[143.98 → 145.20] Also, mowing the lawn.
[145.32 → 148.52] You just take a giant Ziploc bag and jump into it and zip it up,
[148.60 → 150.62] you know, and go out there and push it around and, you know,
[150.70 → 153.88] try to avoid the pollen that way.
[155.34 → 156.28] Yeah, exactly.
[156.78 → 158.94] So, I'm really excited today.
[159.96 → 161.92] So, as our listeners know,
[162.04 → 165.32] my background is originally in computational physics,
[165.32 → 171.00] and so I always love when we have guests that kind of overlap with that area.
[171.42 → 173.84] It kind of brings me back to my grad school days.
[174.36 → 179.10] And today, the topic that we're going to talk about is pretty exciting.
[179.30 → 181.08] So, we're going to talk about quantum computing
[181.08 → 184.26] and how that overlaps with machine learning and AI,
[184.44 → 187.08] how machine learning and AI are impacting quantum computing,
[187.56 → 190.16] and then some related things.
[190.16 → 192.50] So, today we're joined by Marcus Edwards,
[192.50 → 196.46] who is a graduate student at the Institute for Quantum Computing
[196.46 → 197.86] at the University of Waterloo,
[198.34 → 200.32] and Dr. Showing Ghost,
[200.54 → 204.38] who is a professor at the Wilfrid Laurier University.
[204.94 → 205.46] Welcome.
[205.68 → 206.76] Thank you guys for joining us.
[207.36 → 208.38] Thank you for having us.
[208.92 → 214.78] Yeah, it would be great to hear just a little bit of a background
[214.78 → 215.86] from each of you,
[215.94 → 219.24] how you got into physics and quantum computing,
[219.24 → 223.58] how you got interested maybe in related things like AI
[223.58 → 224.56] and those sorts of things.
[224.80 → 228.14] So, maybe Dr. Ghost, if you want to start us out with that.
[228.80 → 233.20] So, I've been interested in physics and more generally science for a long time.
[233.46 → 236.70] And yes, I was one of those nerdy kids who loved Star Trek
[236.70 → 238.28] back when I was a kid.
[238.66 → 239.88] There's nothing wrong with that.
[239.88 → 241.08] I was also right.
[242.08 → 244.40] But other than the sci-fi kind of astronauts,
[244.40 → 246.90] I was also inspired by real astronauts.
[246.96 → 248.58] When I was a kid in India,
[248.90 → 251.52] one of my heroes was Rakesh Sharma,
[251.64 → 253.80] who was the first Indian to go to space.
[254.46 → 257.00] So, I always dreamed of following him into space,
[257.02 → 259.32] and that's not something that's happened as yet,
[259.46 → 260.60] but hopefully he's happy, right?
[260.60 → 261.30] You never know.
[261.38 → 262.44] You have time left.
[262.74 → 263.00] Exactly.
[263.66 → 265.24] So, in the meantime,
[265.48 → 267.88] I thought I'd do something that's almost as exciting,
[268.48 → 269.90] which is physics, of course.
[270.36 → 272.68] So, that's what brought me into physics.
[272.68 → 274.38] And then, when I was an undergrad,
[275.06 → 278.56] I was lucky because I got to do a summer research project
[278.56 → 279.68] on quantum physics.
[280.24 → 284.00] So, that was my first real taste of this very bizarre world.
[284.68 → 286.42] And I kind of liked it.
[287.04 → 291.18] And from there, I went to grad school in the U.S.
[291.18 → 292.64] at the University of New Mexico.
[293.28 → 295.72] And back then, that was one of the first research groups
[295.72 → 299.58] in this brand-new area called quantum information science,
[299.58 → 302.86] which is basically the broad area that includes quantum computing,
[303.18 → 304.06] quantum communication,
[304.40 → 305.96] and everything else we hear about today.
[306.58 → 308.48] So, I feel like I got in on the ground floor.
[308.58 → 309.70] It was exciting times,
[309.70 → 312.44] and I've seen the whole field grow and evolve
[312.44 → 313.74] to what it is today.
[313.92 → 316.14] So, it's been a great, wonderful journey,
[316.28 → 319.12] kind of like a Star Trek exploration journey.
[319.64 → 322.68] So, I think it's going well so far.
[322.68 → 326.86] I got to say, any bio that can bring Star Trek into it
[326.86 → 328.78] as part of your bio, that works for me.
[329.18 → 331.06] Marcus, can you tell us a little bit about yourself?
[331.68 → 332.48] I certainly can.
[333.44 → 336.36] Yeah, actually, my link to quantum physics
[336.36 → 338.84] and quantum computing really is Dr. Gone.
[339.56 → 342.38] I attended Wilfrid Laurier University in my undergrad
[342.38 → 344.62] in a double major in computer science and physics.
[345.58 → 347.18] Yeah, so I originally joined that program
[347.18 → 350.42] just because of the interest in sort of the fundamental problem
[350.42 → 352.32] of information science and computing
[352.32 → 354.24] and wanting to get into the physics of it.
[354.80 → 356.06] In that sort of exploration,
[356.54 → 359.20] quantum mechanics was sort of the most interesting facet
[359.20 → 361.78] and sort of felt like that's where people were asking
[361.78 → 365.50] the most fundamental and sort of groundbreaking questions.
[366.22 → 368.12] And so, yeah, so I started working with Dr. Gone
[368.12 → 371.04] in my undergrad doing a directed research study
[371.04 → 372.86] and getting involved that way.
[373.48 → 375.24] And, yeah, it was actually Dr. Gone
[375.24 → 377.26] who encouraged me to continue on with it,
[377.36 → 379.90] and that's why largely I'm at the Institute
[379.90 → 382.66] for Quantum Computing now doing my grad studies.
[383.56 → 387.10] And, yeah, I guess I also am a bit of a technologist,
[387.38 → 390.74] so I'm currently a front-end team lead
[390.74 → 393.16] at Delphox Capital Markets, Inc.,
[393.16 → 395.58] where I'm doing full-stack software development.
[396.46 → 399.76] And so having some of that more practical,
[399.76 → 402.34] like, technology experience
[402.34 → 404.96] and bringing that together with the quantum physics
[404.96 → 406.38] is really exciting to me,
[406.44 → 407.96] and that's sort of where quantum machine learning
[407.96 → 410.32] comes into it, and we'll go from there.
[411.20 → 413.10] Awesome. Yeah, that's super exciting,
[413.26 → 415.08] and I'm definitely, I'm really excited
[415.08 → 417.30] to hear about your passion for kind of merging
[417.30 → 419.52] that practical side of software engineering
[419.52 → 422.16] with the quantum physics.
[422.16 → 426.90] I've really appreciated that in our previous conversations.
[427.62 → 429.58] So maybe if one of you could just,
[429.76 → 431.90] I mean, we're all the time on Practical AI,
[432.00 → 434.70] we're talking about a lot of times,
[434.74 → 437.82] like, GPUs and other ways to accelerate computing.
[438.82 → 441.08] And a lot of our listeners might not be,
[441.24 → 443.00] they might have heard of quantum computing,
[443.00 → 445.24] but not really understand how it fits
[445.24 → 447.72] into the wider scheme of, you know,
[447.72 → 451.32] is it a way to accelerate, you know, regular computers?
[451.76 → 453.10] Is it something different?
[453.26 → 455.78] So if one of you could just kind of describe in general
[455.78 → 457.96] what quantum computing is
[457.96 → 459.96] and how it fits into that scheme
[459.96 → 462.36] of accelerating computing,
[462.54 → 463.38] that would be awesome.
[463.92 → 466.16] Sure, Dr. Ghost, why don't you take a shot at this first,
[466.22 → 466.90] and I'll add anything.
[467.46 → 469.38] So quantum computing, yes,
[469.46 → 472.00] does offer the promise of,
[472.00 → 474.30] you know, superfast speed up
[474.30 → 476.26] for certain types of problems.
[476.70 → 480.28] But this is not just yet another faster computer.
[480.54 → 481.84] So it's not just about how you,
[481.94 → 483.24] you know, you read in the news all the time,
[483.30 → 485.82] oh, now we have yet another faster processor
[485.82 → 487.80] from Intel or AMD or whatever.
[488.28 → 489.46] That's not what we're talking about.
[489.50 → 491.70] We're talking about an entirely different technology.
[492.52 → 494.04] So it's kind of the difference between,
[494.18 → 495.46] for example, you know,
[495.48 → 497.38] transportation by horse and carriage
[497.38 → 498.44] versus transformation,
[498.64 → 499.98] transportation by cars.
[500.24 → 501.90] It's not like you can just build better
[501.90 → 503.42] and better horses and make a car.
[503.42 → 504.42] You can't.
[504.54 → 505.84] So in that sense,
[505.88 → 507.66] it's a completely different technology
[507.66 → 511.32] because it's harnessing different laws of physics
[511.32 → 513.82] than what we use to build current computers.
[514.48 → 515.98] And the laws that we're talking about
[515.98 → 517.88] are the laws of physics
[517.88 → 521.02] that govern the behaviour of individual particles
[521.02 → 523.92] like electrons and photons and so on.
[524.30 → 526.24] And those tend to be rather peculiar laws.
[526.36 → 527.60] So one of the things probably
[527.60 → 528.90] a lot of people have heard of
[528.90 → 531.02] is this idea of quantum uncertainty,
[531.02 → 533.16] or they may have heard about
[533.16 → 535.04] the idea of superposition
[535.04 → 537.18] where a particular particle
[537.18 → 539.06] can have two different properties
[539.06 → 540.00] at the same time.
[540.18 → 541.58] So in the language of computing,
[542.08 → 545.72] that translates into a bit
[545.72 → 547.58] or some piece of information.
[547.70 → 549.72] A quantum bit doesn't have to be just zero or one,
[549.80 → 551.90] but to have a superposition of zero and one,
[552.32 → 554.60] which means it has a probability of being zero
[554.60 → 555.76] and a probability of one.
[555.76 → 558.06] So that may seem like that would lead
[558.06 → 559.66] to more uncertainty in computing,
[559.92 → 561.24] which is true, sure.
[561.34 → 562.68] But if you're smart about it,
[563.00 → 564.74] then you can actually harness this uncertainty
[564.74 → 567.20] to do actually better computing
[567.20 → 569.94] and build new types of applications.
[570.70 → 573.22] So one of the very first such applications
[573.22 → 575.00] was to realize that uncertainty
[575.00 → 578.70] can lead to information security
[578.70 → 580.02] in the sense of encryption
[580.02 → 581.20] and hiding information.
[581.20 → 586.18] And from there, we explored new types of algorithms
[586.18 → 587.86] for other kinds of applications,
[587.98 → 589.40] such as encryption,
[589.92 → 590.72] and not just encryption,
[590.86 → 594.22] but cryptography and mathematical tasks,
[594.32 → 596.22] such as factoring large numbers
[596.22 → 597.54] is another big example,
[598.20 → 599.86] doing searches more efficiently.
[600.34 → 602.50] And all of these come from realizing
[602.50 → 605.20] that all these strange quantum properties
[605.20 → 608.46] essentially give us new math to work with.
[608.46 → 612.88] And when we have more laws of more rules to work with,
[612.94 → 615.64] then we can combine the rules in more clever ways.
[616.10 → 617.90] It's like taking chess, for example,
[618.04 → 618.78] the rules of chess,
[618.82 → 619.38] and then saying,
[619.50 → 622.68] hey, what if we could play 3D chess like in Star Trek?
[623.32 → 625.42] And then you can make a lot more moves
[625.42 → 627.40] and you can play a much more interesting game.
[627.88 → 629.48] So that's really broadly
[629.48 → 631.66] what quantum computing is all about.
[632.10 → 633.30] Yeah, thank you so much.
[633.42 → 635.44] So if I'm understanding right,
[635.44 → 640.40] I mean, there's kind of a basic set of operations
[640.40 → 643.20] and hardware that have powered,
[643.80 → 646.58] even if they're faster computers over time,
[646.64 → 648.84] have powered classical,
[649.34 → 650.62] normal sort of computers
[650.62 → 652.20] that people think of overtime
[652.20 → 653.38] that are really built around
[653.38 → 655.26] maybe things like transistors
[655.26 → 657.74] or other things that have a certain state
[657.74 → 659.12] like one or zero.
[659.40 → 660.80] So am I right in saying
[660.80 → 662.62] that in a quantum computer,
[662.62 → 667.38] there's not necessarily the idea of a transistor,
[667.38 → 669.42] but something that has,
[669.62 → 671.92] you know, maybe not just one or zero,
[672.06 → 673.64] but a certain number of states.
[673.90 → 675.98] And because you have more possibilities,
[676.66 → 679.94] there's sort of fundamentally new things
[679.94 → 681.10] that you can do
[681.10 → 685.04] that are a different kind of space of operations
[685.04 → 687.46] than what was enabled on the other hardware.
[687.58 → 688.24] Is that right?
[688.62 → 689.74] That's exactly right.
[689.74 → 692.50] So a quantum processor would involve gates
[692.50 → 695.76] that are not just flipping off a bit from zero to one,
[696.26 → 697.80] you know, or just multiplying,
[697.96 → 699.18] you know, or and gates,
[699.28 → 700.44] which we are very familiar with
[700.44 → 703.10] in regular classical hardware processors.
[703.70 → 704.66] For quantum processors,
[704.66 → 707.36] we are allowed to build even more gates
[707.36 → 708.58] that we couldn't do before
[708.58 → 710.04] because as you correctly said,
[710.42 → 712.08] there are many more different types
[712.08 → 714.66] of potential manipulations you can do
[714.66 → 715.68] because you're not just restricted
[715.68 → 717.14] to two things, zero and one.
[717.14 → 718.14] Yes.
[718.36 → 720.32] Can I just say that I think it's awesome
[720.32 → 722.16] that quantum information science
[722.16 → 724.04] is a field that lets you sort of go back
[724.04 → 726.04] and design at the level
[726.04 → 728.48] of the comparative transistor.
[728.86 → 730.30] Like who's going to let you redesign
[730.30 → 731.84] the transistor in any other field, right?
[732.84 → 734.40] Yeah, it's kind of like going back
[734.40 → 735.50] to a golden age almost.
[735.96 → 737.50] It is, especially if you're really interested
[737.50 → 739.48] in sort of that technology focused research, right?
[739.48 → 743.24] So, yeah, so I love that comparison
[743.24 → 745.72] to the transistor and designing at that level
[745.72 → 747.88] and thinking about things in different ways.
[747.96 → 750.26] I also really liked that comparison
[750.26 → 751.56] with 3D chess actually
[751.56 → 755.92] because, yeah, there are models
[755.92 → 757.44] of quantum information science
[757.44 → 758.32] that are being developed
[758.32 → 760.80] and some that have been developed
[760.80 → 763.50] to quite a far extent
[763.50 → 764.68] and experimentally tested,
[764.84 → 765.74] experimentally demonstrated.
[765.74 → 769.48] And these models are enabling us
[769.48 → 770.16] to do computation
[770.16 → 771.72] despite not fully understanding
[771.72 → 772.50] the underlying physics
[772.50 → 773.64] of what's going on necessarily.
[774.00 → 775.98] I don't necessarily think anyone
[775.98 → 778.62] truly understands quantum mechanics,
[779.46 → 782.76] but sort of, which is kind of fun
[782.76 → 784.38] how it fits with the 3D chess analogy,
[785.06 → 788.74] we can model quantum mechanical interactions
[789.54 → 790.44] in many-body physics
[790.44 → 792.72] using high-dimensional vector spaces
[792.72 → 796.14] and tensor mathematics, etc.,
[796.14 → 797.78] which ends up leading us
[797.78 → 800.14] to the fact that actually
[800.14 → 801.94] quantum mechanics and quantum computing
[801.94 → 804.54] has a lot of analogs
[804.54 → 805.86] that fit well with machine learning
[805.86 → 806.74] and other fields
[806.74 → 808.64] that deal with high-dimensional mathematics.
[809.18 → 811.40] So, I'm kind of wondering,
[811.70 → 813.34] we're always hearing in the news
[813.34 → 815.98] about quantum computing,
[816.12 → 816.82] quantum computers,
[817.08 → 819.68] but I don't know that in my own mind,
[819.68 → 821.56] I understand what the current state
[821.56 → 823.38] of kind of practical quantum computers,
[824.02 → 825.56] you know, just like I might,
[825.66 → 827.64] you know, work on a traditional computer,
[827.74 → 828.48] a classical computer,
[828.92 → 830.80] where are they at this point?
[830.92 → 832.44] Is this something that we're expecting
[832.44 → 834.58] to be available anytime soon,
[834.64 → 836.16] or are people going to have access to them?
[836.42 → 837.22] And if not,
[837.30 → 838.66] what is the roadmap to get there?
[839.32 → 839.56] Sure.
[839.78 → 843.42] So, I suspect that you may know this,
[843.54 → 845.44] but in 2010,
[845.60 → 846.94] Lockheed Martin actually became
[846.94 → 847.68] the first customer
[847.68 → 850.14] of one of the first companies
[850.14 → 852.16] providing commercially available
[852.16 → 853.72] quantum computing devices.
[854.54 → 855.40] Now, this is,
[855.60 → 856.96] the company I'm talking about is D-Wave,
[857.04 → 857.72] and they don't provide
[857.72 → 858.96] quantum computers per se,
[859.04 → 860.20] not universal quantum computing,
[860.44 → 863.26] but computational devices
[863.26 → 864.74] that make use of quantum physics,
[864.86 → 865.16] for sure.
[866.76 → 867.58] And, you know,
[867.58 → 868.24] that was really exciting
[868.24 → 868.94] because Lockheed Martin
[868.94 → 870.08] was actually able to demonstrate
[870.08 → 871.60] one of the first practical uses
[871.60 → 873.24] of what's called
[873.24 → 874.74] a quantum annealing machine,
[874.86 → 875.96] which is what D-Wave provides,
[876.54 → 878.60] debugging a chunk of 30-year-old code
[878.60 → 879.68] from an F-16 aircraft.
[880.42 → 881.36] It was just a cool story,
[881.92 → 883.78] and I thought it was a cool connection.
[884.44 → 885.26] So that's one example.
[885.44 → 886.88] There are this sort of
[886.88 → 888.24] almost application-specific
[888.24 → 889.00] quantum devices
[889.00 → 890.26] that are actually now available,
[890.92 → 891.92] though there aren't too many
[891.92 → 892.38] in the world.
[894.14 → 895.62] And we also see other companies
[895.62 → 896.54] like IBM,
[896.98 → 897.58] Google,
[898.06 → 898.48] Intel,
[898.48 → 900.16] all working on their own
[900.16 → 902.00] quantum computing projects.
[902.28 → 903.48] Microsoft actually has one too.
[904.14 → 906.24] And these are all sorts of
[906.24 → 907.30] at varying levels
[907.30 → 908.30] and focusing on
[908.30 → 909.08] different technologies
[909.08 → 910.00] because there are many
[910.00 → 910.86] different formulations
[910.86 → 911.80] and approaches
[911.80 → 912.38] to implementing
[912.38 → 913.04] quantum computing.
[913.64 → 915.10] But one of the most notable ones,
[915.18 → 915.42] I think,
[915.48 → 916.70] just because of how far
[916.70 → 917.16] they've come
[917.16 → 917.94] and how well they're doing
[917.94 → 918.40] with marketing
[918.40 → 919.88] and getting researchers on board
[919.88 → 920.34] is IBM.
[921.54 → 923.22] IBM announced this year
[923.22 → 924.26] their system called
[924.26 → 925.38] IBM Quantum One.
[926.32 → 926.94] And what it is
[926.94 → 929.22] is a 20-qubit
[929.22 → 930.50] quantum computer,
[930.68 → 931.82] and it is that sort of
[931.82 → 932.88] universal quantum computer
[932.88 → 935.26] which application-specific devices
[935.26 → 935.90] like D-Waves
[935.90 → 937.12] are not.
[937.60 → 938.48] And that's exciting
[938.48 → 940.20] because it's sort of
[940.20 → 940.92] commercially available.
[941.28 → 942.06] It's also available
[942.06 → 942.96] to research.
[943.78 → 944.74] Researchers like myself
[944.74 → 945.12] use it
[945.12 → 947.60] for just asking
[947.60 → 948.30] interesting questions
[948.30 → 948.74] about physics
[948.74 → 949.84] and seeing what actually happens
[949.84 → 950.46] and if it matches
[950.46 → 951.10] our expectations.
[951.24 → 952.08] It's kind of like a lab
[952.08 → 952.58] that you can access
[952.58 → 953.44] through the cloud.
[953.58 → 953.84] It's cool.
[953.84 → 956.14] And yeah.
[956.38 → 957.74] Now these computers,
[957.86 → 958.04] though,
[958.16 → 959.02] you may suspect
[959.02 → 960.60] aren't changing the world yet.
[961.02 → 962.04] These are sort of,
[962.14 → 962.70] at this point,
[962.86 → 963.80] sort of toy machines
[963.80 → 965.94] and they're really expensive toys.
[966.24 → 967.70] They're several million dollars
[967.70 → 969.44] of sort of parts
[969.44 → 969.90] and work
[969.90 → 970.82] going into each one,
[971.04 → 973.16] but they're still
[973.16 → 973.76] at the point
[973.76 → 975.32] where even if they have
[975.32 → 976.16] many quits
[976.16 → 977.02] like 20,
[977.40 → 978.48] that's not really enough
[978.48 → 979.06] to get us
[979.06 → 980.22] to the point
[980.22 → 980.76] where we're doing
[980.76 → 981.46] any sort of
[981.46 → 982.96] large-scale
[982.96 → 984.30] optimization problems
[984.30 → 985.40] or really enhancing
[985.40 → 986.46] machine learning yet,
[986.98 → 988.00] largely due to
[988.00 → 988.74] just the challenges
[988.74 → 989.30] in engineering
[989.30 → 990.24] that come along with it.
[990.46 → 991.64] Once you're trying
[991.64 → 992.06] to maintain
[992.06 → 992.94] a large quantum system,
[993.02 → 993.88] that becomes very difficult.
[994.30 → 994.78] So,
[995.06 → 996.40] kind of as a follow-up
[996.40 → 996.84] to that,
[997.28 → 998.06] I'm going to ask
[998.06 → 998.68] both of you
[998.68 → 999.32] for an answer.
[999.80 → 1000.90] If you'll put on
[1000.90 → 1003.24] your super prediction hat
[1003.24 → 1004.38] and magically
[1004.38 → 1006.12] look into your crystal ball,
[1006.66 → 1007.82] do you think
[1007.82 → 1008.58] there's a point
[1008.58 → 1010.66] in the future here
[1010.66 → 1011.88] where quantum computers
[1011.88 → 1013.46] become as ubiquitous
[1013.46 → 1015.50] as our classical computers are?
[1016.02 → 1016.94] Or do you think
[1016.94 → 1017.42] they're always going
[1017.42 → 1018.00] to be specialized?
[1018.34 → 1018.80] And if so,
[1019.52 → 1020.68] just pulling a number
[1020.68 → 1021.14] out of the air,
[1021.22 → 1021.84] how long do you think
[1021.84 → 1022.40] we are from that?
[1023.50 → 1023.90] Okay,
[1023.96 → 1024.62] I'll go first.
[1025.04 → 1025.36] Okay.
[1025.72 → 1026.64] And jump in.
[1026.76 → 1027.08] Although,
[1027.28 → 1027.54] of course,
[1027.60 → 1028.46] it's very dangerous
[1028.46 → 1029.58] to ever make predictions
[1029.58 → 1030.50] about technology
[1030.50 → 1031.44] because we never,
[1031.74 → 1032.48] ever get it right.
[1032.60 → 1033.44] That's the only prediction
[1033.44 → 1034.50] I can make for certain
[1034.50 → 1035.20] that I will be wrong.
[1036.10 → 1037.58] But that being said,
[1037.58 → 1038.78] you know,
[1038.86 → 1039.56] I don't,
[1039.64 → 1039.96] currently,
[1040.10 → 1041.56] I don't see any evidence
[1041.56 → 1042.12] that we have,
[1042.44 → 1043.26] we are going to have
[1043.26 → 1044.90] desktops or laptops
[1044.90 → 1046.92] that are quantum computer based
[1046.92 → 1048.20] because for one thing,
[1048.22 → 1048.94] we don't need them.
[1049.06 → 1050.32] So it's a bit of an overkill
[1050.32 → 1050.78] to have,
[1050.90 → 1051.90] to use a quantum computer
[1051.90 → 1053.12] to do emails,
[1053.26 → 1053.72] for example.
[1054.40 → 1055.16] So you're never,
[1055.38 → 1056.48] ever going to need that.
[1056.64 → 1057.28] That's not what
[1057.28 → 1058.72] quantum computing technology
[1058.72 → 1059.32] is all about.
[1059.96 → 1060.36] So I think,
[1060.44 → 1060.82] I don't know.
[1060.92 → 1062.18] I think I might need one
[1062.18 → 1063.54] to run all my Chrome tabs.
[1063.88 → 1064.82] Quantum Chrome.
[1065.00 → 1065.12] Yeah.
[1065.40 → 1065.80] Oh boy.
[1066.10 → 1067.34] I'd say in the near future,
[1067.58 → 1068.42] there's going to be
[1068.42 → 1070.18] definitely specific applications,
[1070.18 → 1071.30] as I said,
[1071.34 → 1072.52] perhaps either in encryption
[1072.52 → 1073.16] or in,
[1073.22 → 1074.30] you know,
[1074.46 → 1075.28] things like
[1075.28 → 1076.30] what we call
[1076.30 → 1077.30] quantum simulation.
[1077.64 → 1079.04] So using a quantum computer
[1079.04 → 1080.12] to try to simulate
[1080.12 → 1081.60] other quantum systems
[1081.60 → 1083.88] like small molecules,
[1084.16 → 1085.60] perhaps that would be used
[1085.60 → 1086.52] for drug development
[1086.52 → 1087.48] and things like this.
[1087.78 → 1088.44] Those will happen
[1088.44 → 1089.46] in the small scale,
[1089.70 → 1092.06] in the relatively near term,
[1092.64 → 1093.52] maybe in,
[1093.72 → 1094.42] we're talking about
[1094.42 → 1095.68] the next decade or so.
[1095.68 → 1097.04] But I think
[1097.04 → 1098.82] in the longer term
[1098.82 → 1099.46] and even now,
[1099.52 → 1100.58] I think what we're doing now
[1100.58 → 1102.30] is envisioning
[1102.30 → 1104.58] more of a hybrid system
[1104.58 → 1105.34] where there'll be
[1105.34 → 1106.50] perhaps a front end
[1106.50 → 1107.22] which is familiar
[1107.22 → 1108.14] to users today
[1108.14 → 1109.04] which looks no different
[1109.04 → 1110.06] than what you're using now.
[1110.16 → 1111.02] And then in the back end,
[1111.10 → 1111.66] maybe there'll be
[1111.66 → 1112.58] some layers of
[1112.58 → 1114.14] either quantum communication
[1114.14 → 1114.62] happening
[1114.62 → 1115.70] or some kind of
[1115.70 → 1116.78] quantum processing
[1116.78 → 1117.26] happening
[1117.26 → 1119.06] that you may not even see.
[1119.40 → 1121.04] And as Marcus described,
[1121.32 → 1122.32] our first access
[1122.32 → 1122.88] right now
[1122.88 → 1123.60] to any kind of
[1123.60 → 1124.24] quantum device,
[1124.24 → 1125.58] which is the IBM device,
[1125.92 → 1126.70] is through the cloud.
[1126.90 → 1127.86] So that might become
[1127.86 → 1129.88] the way forward
[1129.88 → 1130.92] where most of this
[1130.92 → 1131.78] will be cloud-based
[1131.78 → 1132.56] where we don't have it
[1132.56 → 1133.40] in our homes
[1133.40 → 1134.84] all the time necessarily,
[1135.26 → 1136.52] but it'll be there
[1136.52 → 1137.20] in the background.
[1138.14 → 1139.16] So I guess I leave it at that.
[1139.56 → 1141.02] Yeah, not many people
[1141.02 → 1142.56] have like a TPU pod
[1142.56 → 1143.64] from Google
[1143.64 → 1144.98] sitting in their closet
[1144.98 → 1147.02] to run their neural nets either.
[1147.16 → 1147.76] So it seems like
[1147.76 → 1148.54] a similar model.
[1149.06 → 1149.68] I'm just bumming.
[1149.74 → 1150.32] I'm just bumming.
[1150.40 → 1150.64] Apparently,
[1150.78 → 1151.36] I'm not going to have
[1151.36 → 1152.78] a MacBook Pro Quantum
[1152.78 → 1154.56] version anytime soon here.
[1156.38 → 1156.82] Yes.
[1156.96 → 1157.94] Well, it's unlikely.
[1158.46 → 1159.46] I will say, though,
[1159.60 → 1160.26] that one thing
[1160.26 → 1161.24] that really excites me
[1161.24 → 1162.80] is bringing this
[1162.80 → 1163.84] sort of cooperation
[1163.84 → 1165.32] closer together
[1165.32 → 1166.06] between classical
[1166.06 → 1167.68] and quantum computing
[1167.68 → 1169.22] and sort of optimizing
[1169.22 → 1170.20] that as much as possible.
[1170.92 → 1172.16] While it's
[1172.16 → 1173.02] certainly less likely
[1173.02 → 1173.70] that we'll ever have
[1173.70 → 1175.40] a quantum processing unit
[1175.40 → 1175.88] or something
[1175.88 → 1177.12] alongside our CPU
[1177.12 → 1177.86] and our laptops,
[1177.94 → 1178.36] I don't think
[1178.36 → 1179.38] it's impossible.
[1181.34 → 1182.24] My prediction
[1182.24 → 1182.92] would be that,
[1183.00 → 1183.36] of course,
[1183.70 → 1184.68] the first access
[1184.68 → 1186.20] that sort of
[1186.20 → 1187.10] becomes
[1187.10 → 1187.60] quote-unquote
[1187.60 → 1188.36] ubiquitous
[1188.36 → 1189.76] if it gets that far
[1189.76 → 1191.14] to quantum computing
[1191.14 → 1192.08] would be through the cloud.
[1193.60 → 1193.96] And so
[1193.96 → 1195.52] that would be,
[1195.58 → 1195.90] yeah,
[1195.96 → 1197.04] similar to what we have now
[1197.04 → 1198.60] that IBM is providing.
[1200.04 → 1200.86] Other companies
[1200.86 → 1201.68] are starting
[1201.68 → 1202.68] to look at that as well.
[1203.54 → 1204.38] There's Ringette,
[1205.20 → 1205.76] Google,
[1205.76 → 1208.16] and Xanadu
[1208.16 → 1209.06] actually all have
[1209.06 → 1209.92] their own sort of
[1209.92 → 1211.36] software portals now
[1211.36 → 1212.76] that they intend to
[1212.76 → 1214.92] continue to market
[1214.92 → 1215.44] and develop
[1215.44 → 1216.96] and optimize
[1216.96 → 1218.30] for quantum computing
[1218.30 → 1219.50] and enabling
[1219.50 → 1220.70] that communication.
[1221.06 → 1221.22] Now,
[1221.72 → 1222.04] of course,
[1222.12 → 1222.80] communicating with
[1222.80 → 1224.64] a quantum process
[1224.64 → 1225.26] is interesting
[1225.26 → 1226.86] because it becomes
[1226.86 → 1227.44] a bottleneck
[1227.44 → 1229.04] when you sort of
[1229.04 → 1230.12] wrap a quantum process
[1230.12 → 1231.40] in classical processes
[1231.40 → 1232.42] on either end.
[1233.90 → 1234.26] However,
[1234.26 → 1235.70] having a completely
[1235.70 → 1236.34] quantum computer
[1236.34 → 1236.76] to me
[1236.76 → 1237.50] would be
[1237.50 → 1238.58] probably the most
[1238.58 → 1239.20] useless computer
[1239.20 → 1239.80] that exists
[1239.80 → 1240.86] just because
[1240.86 → 1242.54] as sort of humans
[1242.54 → 1243.92] we expect to have
[1243.92 → 1245.60] interpretable information
[1245.60 → 1247.20] coming out at us
[1247.20 → 1247.84] and going into
[1247.84 → 1248.76] the computer from us.
[1249.42 → 1250.08] And so
[1250.08 → 1251.10] I think that
[1251.10 → 1252.24] we will always have
[1252.24 → 1253.76] that sort of
[1253.76 → 1254.96] classical interface
[1254.96 → 1255.46] at least.
[1256.18 → 1256.84] And where quantum
[1256.84 → 1258.38] will actually be useful
[1258.38 → 1259.02] is in,
[1259.62 → 1260.40] as Dr. Go said,
[1260.46 → 1261.22] the back end,
[1261.22 → 1262.88] whether that's a chip
[1262.88 → 1264.74] or a remote database
[1264.74 → 1265.20] somewhere
[1265.20 → 1266.84] that's been implemented
[1266.84 → 1267.98] using quantum physics
[1267.98 → 1270.40] or a remote processor,
[1271.06 → 1273.82] doing particular pieces
[1273.82 → 1274.94] of hybrid algorithms.
[1274.94 → 1276.28] And some of the most
[1276.28 → 1277.42] exciting hybrid algorithms
[1277.42 → 1278.86] are in machine learning.
[1279.38 → 1281.64] And there's work being done
[1281.64 → 1283.14] here in Waterloo
[1283.14 → 1284.54] at IOC
[1284.54 → 1285.62] and at the Perimeter Institute
[1285.62 → 1287.64] on creating
[1287.64 → 1288.60] these hybrid algorithms
[1288.60 → 1289.56] and optimizing them
[1289.56 → 1290.52] for cooperation
[1290.52 → 1291.38] between CPUs
[1291.38 → 1292.04] and CPUs.
[1293.10 → 1294.28] That's really exciting stuff.
[1294.28 → 1303.88] This episode is brought to you
[1303.88 → 1304.88] by Discover. Bot.
[1305.08 → 1306.02] Learn everything there is
[1306.02 → 1306.94] to know about bots
[1306.94 → 1308.08] at Discover. Bot
[1308.08 → 1309.06] slash Practical AI.
[1309.60 → 1310.18] Discover. Bot
[1310.18 → 1310.82] was built by
[1310.82 → 1312.02] Amazon Registry Services
[1312.02 → 1313.44] as an online community
[1313.44 → 1314.04] for bot creators
[1314.04 → 1315.32] and makers of all skill levels
[1315.32 → 1316.36] to learn from one another,
[1316.50 → 1317.48] to share stories,
[1317.64 → 1318.64] and they regularly publish
[1318.64 → 1319.50] guides and resources
[1319.50 → 1320.64] to answer questions like
[1320.64 → 1321.60] how to set up payments
[1321.60 → 1322.12] to your bot,
[1322.22 → 1322.92] how to stop shopping
[1322.92 → 1323.66] card abandonment,
[1323.66 → 1325.14] what KPIs are worth measuring,
[1325.30 → 1326.68] how to write an engaging
[1326.68 → 1327.70] chatbot dialogue.
[1328.14 → 1329.02] You can even register
[1329.02 → 1330.08] .bot domains there.
[1330.36 → 1331.16] Learn more and explore
[1331.16 → 1332.00] this huge library
[1332.00 → 1332.74] of bot resources
[1332.74 → 1334.14] at discover. Bot
[1334.14 → 1334.92] slash Practical AI.
[1335.42 → 1336.72] Again, discover. Bot
[1336.72 → 1337.80] slash Practical AI.
[1349.86 → 1351.38] So I really appreciate
[1351.38 → 1353.12] the explanation
[1353.12 → 1354.94] that both of you gave
[1354.94 → 1355.98] on the front of,
[1356.04 → 1356.24] you know,
[1356.28 → 1358.00] what quantum computing is
[1358.00 → 1359.30] and kind of the current
[1359.30 → 1359.92] state of it,
[1360.00 → 1360.86] maybe some things
[1360.86 → 1361.40] that are coming
[1361.40 → 1362.22] in the future.
[1362.88 → 1363.96] One thing that I,
[1364.18 → 1365.10] one question that I,
[1365.20 → 1366.34] that I have in my mind
[1366.34 → 1367.64] and, you know,
[1367.66 → 1368.66] I played a little bit
[1368.66 → 1370.44] around with like systems
[1370.44 → 1371.06] like Ringette
[1371.06 → 1372.02] and others,
[1372.02 → 1373.88] but I'm wondering,
[1374.06 → 1374.34] you know,
[1374.38 → 1375.66] from your perspective,
[1375.66 → 1376.90] could you just describe
[1376.90 → 1378.58] what does it,
[1378.88 → 1379.86] what does it look like
[1379.86 → 1380.88] to kind of program
[1380.88 → 1382.30] a quantum computer?
[1382.30 → 1382.70] Like,
[1382.76 → 1383.70] do I just pull up,
[1383.98 → 1384.30] you know,
[1384.74 → 1385.54] a Jupyter notebook
[1385.54 → 1387.00] and use Python
[1387.00 → 1388.16] to like,
[1388.74 → 1389.16] say,
[1389.30 → 1389.68] you know,
[1390.34 → 1391.50] pandas read
[1391.50 → 1392.78] from quantum computer
[1392.78 → 1393.38] or, you know,
[1393.44 → 1393.70] something?
[1393.88 → 1394.02] Like,
[1394.08 → 1395.64] what's the interface
[1395.64 → 1396.14] currently
[1396.14 → 1397.40] and how do you,
[1397.40 → 1398.10] how do you envision,
[1398.26 → 1398.40] like,
[1398.46 → 1399.44] what type of different
[1399.44 → 1399.86] thinking
[1399.86 → 1401.02] and different sorts
[1401.02 → 1402.56] of like practical
[1402.56 → 1403.90] operations
[1403.90 → 1404.92] are you dealing with
[1404.92 → 1405.88] when you're programming
[1405.88 → 1407.18] a quantum computer?
[1408.08 → 1408.16] Now,
[1408.20 → 1408.68] this is a very,
[1408.78 → 1409.48] very fun question
[1409.48 → 1411.28] and one that's
[1411.28 → 1411.78] very exciting
[1411.78 → 1412.12] because,
[1412.26 → 1412.52] again,
[1412.72 → 1413.88] when it comes to
[1413.88 → 1415.10] quantum information science,
[1415.38 → 1417.24] you're free to sort of
[1417.24 → 1418.38] reimagine and rethink
[1418.38 → 1419.32] every layer of the stack.
[1419.72 → 1419.98] So,
[1420.58 → 1421.38] for example,
[1422.18 → 1423.14] what sort of language
[1423.14 → 1423.76] do we use
[1423.76 → 1425.18] to program a quantum computer
[1425.18 → 1425.82] at the low level?
[1426.42 → 1427.06] There are a few
[1427.06 → 1427.92] sort of different takes
[1427.92 → 1428.28] at this,
[1428.36 → 1428.92] but it's all
[1428.92 → 1429.96] in the very early stages
[1429.96 → 1432.16] and almost all
[1432.16 → 1432.72] open source
[1432.72 → 1433.36] so that anyone
[1433.36 → 1435.62] who is interested
[1435.62 → 1436.60] can actually start
[1436.60 → 1437.26] learning how
[1437.26 → 1438.78] people are thinking
[1438.78 → 1440.44] about implementing
[1440.44 → 1441.18] assembly languages
[1441.18 → 1442.08] for quantum computers.
[1442.98 → 1444.66] IBM has Opencast,
[1444.72 → 1445.14] they call it.
[1445.22 → 1445.60] It's quantum
[1445.60 → 1446.38] assembly language.
[1447.22 → 1448.20] It's open sourced.
[1448.44 → 1448.46] So,
[1449.10 → 1449.54] for example,
[1449.76 → 1450.50] I have the source
[1450.50 → 1451.26] on my laptop here
[1451.26 → 1451.70] on my Mac
[1451.70 → 1452.98] and I'm able to play
[1452.98 → 1453.78] with that a lot.
[1455.14 → 1455.40] Now,
[1456.24 → 1456.72] sort of
[1456.72 → 1458.34] an interesting question
[1458.34 → 1458.92] is,
[1458.92 → 1460.12] do we want
[1460.12 → 1461.86] our language,
[1462.26 → 1463.12] even our low level
[1463.12 → 1463.56] language,
[1463.96 → 1464.38] our quantum
[1464.38 → 1465.18] assembly language,
[1465.56 → 1467.90] to be opinionated
[1467.90 → 1468.56] and sort of
[1468.56 → 1469.24] limit the scope
[1469.24 → 1469.88] of what a quantum
[1469.88 → 1472.04] physicist can describe?
[1472.18 → 1472.98] Because quantum physics
[1472.98 → 1475.78] is very complex
[1475.78 → 1477.46] and the gate model
[1477.46 → 1478.28] is what's typically
[1478.28 → 1480.16] used to describe
[1480.16 → 1480.82] quantum computing
[1480.82 → 1481.26] processes,
[1481.56 → 1482.30] but it's certainly
[1482.30 → 1483.36] not the only model
[1483.36 → 1484.74] for quantum physics
[1484.74 → 1486.06] and even
[1486.06 → 1486.80] quantum computing.
[1486.80 → 1489.10] There are plenty
[1489.10 → 1489.88] of different types
[1489.88 → 1490.58] of devices even.
[1490.72 → 1490.88] So,
[1491.00 → 1491.66] you might say
[1491.66 → 1493.00] we want to use
[1493.00 → 1493.76] a continuous variable
[1493.76 → 1494.44] quantum computer
[1494.44 → 1495.16] or
[1495.16 → 1497.16] an adiabatic
[1497.16 → 1497.82] quantum computer
[1497.82 → 1498.92] and if we want
[1498.92 → 1499.36] to do that
[1499.36 → 1500.10] because for some
[1500.10 → 1500.40] reason
[1500.40 → 1501.54] there's some
[1501.54 → 1502.66] appeal
[1502.66 → 1503.70] to practically
[1503.70 → 1504.16] implement one
[1504.16 → 1504.42] of those
[1504.42 → 1504.86] in the future,
[1505.56 → 1507.50] maybe IBM's
[1507.50 → 1508.06] ASM
[1508.06 → 1508.76] is no longer
[1508.76 → 1509.34] relevant
[1509.34 → 1510.64] in that case
[1510.64 → 1511.38] because it
[1511.38 → 1512.20] was designed
[1512.20 → 1513.76] to express
[1513.76 → 1514.66] its particular
[1514.66 → 1515.50] type of
[1515.50 → 1516.08] quantum computing.
[1517.66 → 1518.22] So,
[1518.50 → 1518.66] yeah,
[1518.74 → 1519.02] so there's
[1519.02 → 1519.68] sort of bit
[1519.68 → 1521.18] of an emerging
[1521.18 → 1522.04] open source
[1522.04 → 1523.50] community around
[1523.50 → 1524.16] quantum computing
[1524.16 → 1524.92] which is very
[1524.92 → 1525.32] interesting.
[1526.82 → 1527.80] It's largely
[1527.80 → 1528.42] centred around
[1528.42 → 1529.02] IBM and what
[1529.02 → 1529.38] they're doing
[1529.38 → 1530.12] but there's
[1530.12 → 1531.00] alternatives like
[1531.00 → 1531.92] what Xanadu
[1531.92 → 1532.42] is offering
[1532.42 → 1534.12] which is around
[1534.12 → 1534.64] a different type
[1534.64 → 1535.36] of quantum computing
[1535.36 → 1536.46] called continuous
[1536.46 → 1537.56] variable quantum computing
[1537.56 → 1539.16] and I've been
[1539.16 → 1539.58] a contributor
[1539.58 → 1541.38] to Xanadu's
[1541.38 → 1542.56] Strawberry Fields
[1542.56 → 1543.66] library which is
[1543.66 → 1544.40] a Python library
[1544.40 → 1544.98] for about five
[1544.98 → 1545.24] months
[1545.24 → 1547.82] and it's
[1547.82 → 1549.16] trying to define
[1549.16 → 1550.42] basically the
[1550.42 → 1550.96] tensor flow
[1550.96 → 1551.72] of quantum computing
[1551.72 → 1553.04] which is a
[1553.04 → 1553.82] Python library
[1553.82 → 1554.94] that,
[1555.30 → 1555.44] yes,
[1555.48 → 1556.08] allows you to
[1556.08 → 1556.64] define these
[1556.64 → 1557.12] sort of gate
[1557.12 → 1558.76] level operations
[1558.76 → 1560.14] and express
[1560.14 → 1560.90] quantum computing
[1560.90 → 1561.84] processes in that
[1561.84 → 1563.00] way but also
[1563.00 → 1563.86] provide these
[1563.86 → 1564.70] more abstracted
[1564.70 → 1565.94] tools sort of
[1565.94 → 1566.78] like you'd expect
[1566.78 → 1567.88] from a package
[1567.88 → 1568.40] like TensorFlow
[1568.40 → 1569.94] so if you want
[1569.94 → 1570.92] to implement
[1570.92 → 1572.82] a machine learning
[1572.82 → 1576.34] process that uses
[1576.34 → 1577.14] quantum physics
[1577.14 → 1577.86] in the background
[1577.86 → 1579.98] you may use
[1579.98 → 1580.70] their package
[1580.70 → 1581.58] Strawberry Fields
[1581.58 → 1584.12] or Penny Lane
[1584.12 → 1585.62] to actually do
[1585.62 → 1586.46] that in a more
[1586.46 → 1587.30] sort of expressive
[1587.30 → 1589.24] way, and it's
[1589.24 → 1589.78] just really fun
[1589.78 → 1590.28] seeing all this
[1590.28 → 1591.22] stuff sort of
[1591.22 → 1591.84] getting built and
[1591.84 → 1592.46] imagined for the
[1592.46 → 1594.12] first time and
[1594.12 → 1594.92] it's an open area
[1594.92 → 1595.70] of research honestly
[1595.70 → 1597.16] to define
[1597.16 → 1598.62] this sort of
[1598.62 → 1599.76] languages well
[1599.76 → 1601.44] and work is
[1601.44 → 1602.18] going on in
[1602.18 → 1602.68] that area at
[1602.68 → 1604.48] IOC and in
[1604.48 → 1604.98] companies like
[1604.98 → 1605.60] Xanadu, and it's
[1605.60 → 1606.02] really cool.
[1606.70 → 1607.30] I appreciate that
[1607.30 → 1608.00] Marcus, that's a
[1608.00 → 1608.70] great explanation.
[1609.36 → 1610.22] Dr. Ghost,
[1610.92 → 1612.62] how do you see,
[1612.84 → 1613.62] you know, you have
[1613.62 → 1615.22] the existing kind
[1615.22 → 1616.20] of AI and machine
[1616.20 → 1617.10] learning community
[1617.10 → 1617.90] that's out there
[1617.90 → 1618.70] and you have
[1618.70 → 1619.80] these quantum
[1619.80 → 1620.84] communities that
[1620.84 → 1622.18] are in development
[1622.18 → 1624.96] and how are
[1624.96 → 1625.90] those communities
[1625.90 → 1626.64] similar and
[1626.64 → 1627.26] different, how do
[1627.26 → 1628.00] they look at each
[1628.00 → 1628.62] other and how
[1628.62 → 1629.40] might they go
[1629.40 → 1630.26] about collaborating
[1630.26 → 1631.30] to where, you
[1631.30 → 1632.50] know, this idea
[1632.50 → 1633.10] that Marcus
[1633.10 → 1633.70] mentioned [1633.70 → 1634.22] kind of the
[1634.22 → 1635.28] tensor flow of
[1635.28 → 1635.96] quantum computing,
[1636.32 → 1636.72] how does that
[1636.72 → 1637.26] come into being
[1637.26 → 1638.00] where it's actually
[1638.00 → 1639.06] utilized in the
[1639.06 → 1639.38] community?
[1640.24 → 1641.00] Yeah, that's a
[1641.00 → 1641.64] really exciting
[1641.64 → 1642.58] question to explore
[1642.58 → 1643.78] right now and so
[1643.78 → 1644.70] this whole area of
[1644.70 → 1645.48] quantum machine
[1645.48 → 1646.54] learning as we
[1646.54 → 1647.64] call it now is
[1647.64 → 1649.06] rapidly growing
[1649.06 → 1650.26] and as Marcus
[1650.26 → 1652.14] mentioned, Waterloo
[1652.14 → 1653.06] is a big hub for
[1653.06 → 1654.00] this kind of work
[1654.00 → 1655.04] as is Toronto,
[1655.22 → 1656.20] of course, in AI
[1656.20 → 1658.08] in general and so
[1658.08 → 1659.32] I think both
[1659.32 → 1660.62] quantum can benefit
[1660.62 → 1662.16] from AI and
[1662.16 → 1663.22] machine learning and
[1663.22 → 1663.90] machine learning can
[1663.90 → 1664.62] benefit from quantum
[1664.62 → 1664.82] too.
[1664.96 → 1665.72] So what I mean is
[1665.72 → 1667.50] that there's, you
[1667.50 → 1667.88] know if you look
[1667.88 → 1669.20] at the level of the
[1669.20 → 1669.60] mathematical
[1669.60 → 1671.14] structures of
[1671.14 → 1673.02] quantum theory and
[1673.02 → 1673.76] the mathematical
[1673.76 → 1675.16] structures of
[1675.16 → 1675.82] machine learning,
[1676.08 → 1676.98] there's a lot in
[1676.98 → 1677.26] common.
[1677.26 → 1679.06] So one thing
[1679.06 → 1679.88] that people have
[1679.88 → 1681.22] been exploring is
[1681.22 → 1682.52] given that we
[1682.52 → 1683.42] don't actually have
[1683.42 → 1684.50] existing large-scale
[1684.50 → 1685.26] quantum computers
[1685.26 → 1686.48] today, we still
[1686.48 → 1687.76] have to rely on our
[1687.76 → 1688.52] current regular
[1688.52 → 1689.42] computers to be
[1689.42 → 1690.44] modelling and analyzing
[1690.44 → 1691.16] quantum systems,
[1691.54 → 1691.72] right?
[1692.06 → 1693.84] And what happens is
[1693.84 → 1694.50] that it's a very
[1694.50 → 1695.26] challenging problem
[1695.26 → 1696.68] because every time
[1696.68 → 1698.16] you add one more
[1698.16 → 1699.26] quantum bit to
[1699.26 → 1700.18] your system to try
[1700.18 → 1701.12] to model it, you
[1701.12 → 1702.00] double the
[1702.00 → 1703.18] computational space
[1703.18 → 1704.12] that you need to
[1704.12 → 1704.38] simulate.
[1704.84 → 1706.92] So that's a huge
[1706.92 → 1707.94] challenge and
[1707.94 → 1709.04] which prevents us
[1709.04 → 1709.62] from, in fact,
[1709.78 → 1710.58] for example, even
[1710.58 → 1712.04] modelling molecules
[1712.04 → 1713.30] of, you know, a
[1713.30 → 1714.22] few hundred atoms,
[1714.34 → 1715.40] for example, where
[1715.40 → 1716.34] we get stuck.
[1716.40 → 1717.04] Even the world's
[1717.04 → 1717.92] the best supercomputers
[1717.92 → 1718.64] can't handle it.
[1719.08 → 1720.20] However, if you
[1720.20 → 1722.22] look at the best
[1722.22 → 1723.68] ways to map that
[1723.68 → 1724.98] kind of information
[1724.98 → 1725.86] into classical
[1725.86 → 1727.46] computers, turns out
[1727.46 → 1728.60] the sort of
[1728.60 → 1729.86] mathematical
[1729.86 → 1731.14] frameworks like,
[1731.20 → 1731.50] you know, the
[1731.50 → 1732.18] tensor network
[1732.18 → 1733.00] structure and so
[1733.00 → 1733.78] on that you also
[1733.78 → 1735.38] use for the
[1735.38 → 1736.36] machine and the
[1736.36 → 1736.90] neural network,
[1737.00 → 1737.60] the tensor
[1737.60 → 1738.18] network from
[1738.18 → 1739.68] quantum maps
[1739.68 → 1740.56] onto the neural
[1740.56 → 1741.60] network structure
[1741.60 → 1743.02] that's being used
[1743.02 → 1743.56] right now for
[1743.56 → 1744.16] machine learning.
[1744.48 → 1745.32] So there's a lot
[1745.32 → 1746.04] of work in trying
[1746.04 → 1746.90] to explore how
[1746.90 → 1748.74] can we efficiently
[1748.74 → 1751.78] explore quantum
[1751.78 → 1754.04] physics using the
[1754.04 → 1754.90] same kind of
[1754.90 → 1755.72] structures and
[1755.72 → 1756.52] approaches that are
[1756.52 → 1757.12] being used in
[1757.12 → 1757.62] machine learning.
[1758.08 → 1758.84] And there have
[1758.84 → 1759.46] been some initial
[1759.46 → 1761.70] successes for doing
[1761.70 → 1763.14] things like, for
[1763.14 → 1764.08] example, looking at
[1764.08 → 1764.60] the magnetic
[1764.60 → 1765.42] properties of
[1765.42 → 1766.16] different materials
[1766.16 → 1766.74] and so on.
[1767.12 → 1768.34] So those are very
[1768.34 → 1769.26] exciting because it
[1769.26 → 1770.06] means that there are
[1770.06 → 1771.72] actual benefits to be
[1771.72 → 1774.00] had from using the
[1774.00 → 1775.12] mathematics of machine
[1775.12 → 1776.56] learning to also
[1776.56 → 1777.42] analyze quantum
[1777.42 → 1777.74] theory.
[1778.00 → 1778.88] But it can also go the
[1778.88 → 1781.28] other way because we
[1781.28 → 1782.38] can also think about
[1782.38 → 1783.50] what happens when we
[1783.50 → 1785.52] do have working
[1785.52 → 1787.32] quantum computers at a
[1787.32 → 1788.34] scale large enough to
[1788.34 → 1788.78] do something
[1788.78 → 1789.22] interesting.
[1789.68 → 1790.30] The question then
[1790.30 → 1791.28] becomes, can we take
[1791.28 → 1792.78] some of the machine
[1792.78 → 1793.52] learning algorithms
[1793.52 → 1794.64] that are existing
[1794.64 → 1796.42] today and build
[1796.42 → 1797.76] quantum versions of
[1797.76 → 1798.54] those algorithms that
[1798.54 → 1799.10] are much more
[1799.10 → 1799.40] efficient?
[1800.14 → 1801.00] So what I mean by
[1801.00 → 1801.78] that, for example,
[1802.04 → 1802.58] and this is not a
[1802.58 → 1803.02] machine learning
[1803.02 → 1804.86] example, but one of
[1804.86 → 1806.12] the first math
[1806.12 → 1807.28] problems that was
[1807.28 → 1808.24] shown to be much,
[1808.34 → 1809.08] much better if you
[1809.08 → 1809.64] run on a quantum
[1809.64 → 1811.12] computer is this idea
[1811.12 → 1812.10] of factoring a large
[1812.10 → 1812.40] number.
[1813.20 → 1813.82] And this is very
[1813.82 → 1814.36] useful, of course,
[1814.40 → 1815.08] because this is in
[1815.08 → 1815.80] fact what would
[1815.80 → 1817.04] enable us to hack
[1817.04 → 1818.08] into current
[1818.08 → 1819.30] encryption like RSA.
[1819.30 → 1821.82] So what we know is
[1821.82 → 1822.32] that there is a
[1822.32 → 1823.74] quantum version of
[1823.74 → 1825.56] factoring that can
[1825.56 → 1826.84] run much, much
[1826.84 → 1827.94] faster if we had a
[1827.94 → 1828.54] quantum computer.
[1829.44 → 1830.18] So then the question
[1830.18 → 1830.78] is, are there
[1830.78 → 1832.26] quantum versions of
[1832.26 → 1833.06] current machine
[1833.06 → 1833.88] learning algorithms
[1833.88 → 1835.30] that would run much
[1835.30 → 1836.36] faster once we have
[1836.36 → 1837.00] a quantum computer?
[1837.06 → 1837.68] And there's a lot of
[1837.68 → 1838.42] work on that end.
[1838.78 → 1840.32] And as we build more
[1840.32 → 1841.22] of those and have
[1841.22 → 1842.10] them ready to go,
[1842.38 → 1843.32] and at the same time
[1843.32 → 1844.18] develop a good
[1844.18 → 1845.48] software and language
[1845.48 → 1846.58] that we can use to
[1846.58 → 1847.98] program future
[1847.98 → 1848.74] quantum computers,
[1848.74 → 1849.52] then we might be
[1849.52 → 1850.86] able to do all
[1850.86 → 1852.90] these exciting new
[1852.90 → 1853.94] kinds of problems
[1853.94 → 1855.08] that we can't do
[1855.08 → 1855.36] today.
[1855.62 → 1856.14] And that's what we
[1856.14 → 1856.74] call quantum
[1856.74 → 1857.18] advantage.
[1857.78 → 1859.26] So that's where I
[1859.26 → 1859.94] see that field.
[1860.76 → 1861.80] So I guess I'm
[1861.80 → 1862.70] curious from a very
[1862.70 → 1863.60] practical standpoint,
[1863.76 → 1864.22] you know, with
[1864.22 → 1866.28] deep learning now
[1866.28 → 1867.26] being dominated by
[1867.26 → 1868.34] the linear algebra
[1868.34 → 1869.26] and derivatives,
[1869.58 → 1870.02] you know, that we're
[1870.02 → 1871.04] always taking as
[1871.04 → 1872.22] we're training
[1872.22 → 1874.38] models, is that
[1874.38 → 1875.14] going to be
[1875.14 → 1876.36] superseded by
[1876.36 → 1877.10] different quantum
[1877.10 → 1877.60] techniques?
[1877.60 → 1879.08] you know, would
[1879.08 → 1879.74] you, in other
[1879.74 → 1880.22] words, would the
[1880.22 → 1881.38] current math and
[1881.38 → 1882.58] quantum be somehow
[1882.58 → 1883.84] working together or
[1883.84 → 1884.46] are you essentially
[1884.46 → 1887.04] going to replace the
[1887.04 → 1887.64] current mathematics
[1887.64 → 1888.36] with a quantum
[1888.36 → 1889.56] variant of that to
[1889.56 → 1890.56] get, you know,
[1890.60 → 1891.42] better performance
[1891.42 → 1891.86] where you want to
[1891.86 → 1893.30] go on that?
[1893.76 → 1894.54] Quantum mathematics
[1894.54 → 1896.40] is essentially
[1896.40 → 1897.56] linear algebra but
[1897.56 → 1898.24] in a particular
[1898.24 → 1899.62] space, which we
[1899.62 → 1900.42] call Hilbert space,
[1900.60 → 1901.38] which essentially
[1901.38 → 1902.56] means that you have
[1902.56 → 1903.86] complex numbers and
[1903.86 → 1905.12] vectors and there are
[1905.12 → 1905.86] certain properties of
[1905.86 → 1906.20] the space.
[1906.20 → 1907.58] So it's basically a
[1907.58 → 1910.22] yeah, as I said, a
[1910.22 → 1911.14] larger set of
[1911.14 → 1912.34] mathematical rules that
[1912.34 → 1913.04] we can use.
[1913.42 → 1914.36] So as I said, and
[1914.36 → 1915.22] again, if you have
[1915.22 → 1916.32] more rules to a
[1916.32 → 1917.22] game, then you can
[1917.22 → 1919.12] figure out different
[1919.12 → 1920.30] ways to win the
[1920.30 → 1920.52] game.
[1921.48 → 1923.26] So that's really what
[1923.26 → 1924.52] I mean by using
[1924.52 → 1926.74] quantum math to do,
[1927.24 → 1927.88] I mean, the task
[1927.88 → 1929.06] remains the same, but
[1929.06 → 1930.26] the way you solve the
[1930.26 → 1932.14] task changes because
[1932.14 → 1933.38] you're allowed to use
[1933.38 → 1934.16] these different rules.
[1934.16 → 1935.00] Gotcha.
[1935.32 → 1935.52] Yes.
[1935.62 → 1936.22] And one of the
[1936.22 → 1937.02] interesting things that
[1937.02 → 1937.98] we get to do as
[1937.98 → 1939.02] researchers is actually
[1939.02 → 1940.54] recast problems that
[1940.54 → 1941.32] are currently being
[1941.32 → 1942.44] solved by AI and
[1942.44 → 1943.26] solved by classical
[1943.26 → 1945.12] algorithms into sort
[1945.12 → 1946.06] of the Hilbert space
[1946.06 → 1947.10] and into quantum
[1947.10 → 1947.50] problems.
[1947.50 → 1948.36] So if we can do this
[1948.36 → 1949.12] recasting of the
[1949.12 → 1951.08] problem and come up
[1951.08 → 1952.02] with then a quantum
[1952.02 → 1953.82] solution, it's often
[1953.82 → 1954.74] very interesting to see
[1954.74 → 1956.36] what kind of advantage
[1956.36 → 1957.20] that quantum solution
[1957.20 → 1957.92] provides over the
[1957.92 → 1958.50] classical one.
[1958.50 → 1960.14] And so I think we
[1960.14 → 1961.04] already see some
[1961.04 → 1962.34] companies actually
[1962.34 → 1965.06] providing services,
[1965.20 → 1965.96] not too many, but
[1965.96 → 1966.90] there's one quit, for
[1966.90 → 1969.48] example, which does
[1969.48 → 1970.30] actually provide sort
[1970.30 → 1970.76] of a consulting
[1970.76 → 1973.12] service and as a
[1973.12 → 1974.30] part of that, recasts
[1974.30 → 1975.30] problems into quantum
[1975.30 → 1976.94] problems and attempts
[1976.94 → 1977.84] to find solutions to
[1977.84 → 1978.04] that.
[1979.16 → 1981.54] So I imagine if quantum
[1981.54 → 1982.84] computing explodes and
[1982.84 → 1983.78] everything's great, that
[1983.78 → 1984.82] more people would start
[1984.82 → 1985.54] to do that type of
[1985.54 → 1985.78] work.
[1985.78 → 1988.74] And one thing to
[1988.74 → 1989.60] mention too, though, is
[1989.60 → 1991.14] that not only is it
[1991.14 → 1992.38] going to be advantageous
[1992.38 → 1994.50] to recast AI problems
[1994.50 → 1995.64] into quantum AI
[1995.64 → 1997.92] problems, but classical
[1997.92 → 2000.92] AI also is helping us
[2000.92 → 2003.40] to understand sort of
[2003.40 → 2004.92] what's fundamentally
[2004.92 → 2006.28] different and interesting
[2006.28 → 2007.14] about quantum physics.
[2007.32 → 2008.76] Because if we can sort of
[2008.76 → 2009.92] go backwards and take a
[2009.92 → 2011.24] quantum problem and turn
[2011.24 → 2012.24] it into an AI problem,
[2012.76 → 2014.56] and it's sort of solved
[2014.56 → 2015.54] and we can do it,
[2015.54 → 2016.74] today, then maybe that's
[2016.74 → 2017.44] not as interesting a
[2017.44 → 2018.10] problem to physicists
[2018.10 → 2018.78] anymore, right?
[2019.18 → 2020.36] And that does happen.
[2021.34 → 2021.98] And actually one
[2021.98 → 2023.82] interesting phenomena is
[2023.82 → 2025.16] that as sort of quantum
[2025.16 → 2026.04] physicists come up with
[2026.04 → 2027.18] more interesting things
[2027.18 → 2028.00] about quantum computing
[2028.00 → 2028.76] and what could happen,
[2029.32 → 2031.62] classical sort of
[2031.62 → 2033.08] computational scientists
[2033.08 → 2034.66] and data scientists and
[2034.66 → 2036.68] stuff are coming up
[2036.68 → 2038.78] with sort of analogs or
[2038.78 → 2040.36] solutions and getting a
[2040.36 → 2041.38] little bit better in order
[2041.38 → 2042.26] to keep up with quantum
[2042.26 → 2042.88] in some ways.
[2042.88 → 2045.32] And so I think there will
[2045.32 → 2046.20] always be a collaboration
[2046.20 → 2048.76] between the two, and we'll
[2048.76 → 2049.94] have classical and quantum
[2049.94 → 2051.72] computing sort of helping
[2051.72 → 2053.06] each other out as we go
[2053.06 → 2053.32] forward.
[2053.88 → 2055.90] Yeah, it's interesting to kind
[2055.90 → 2057.94] of, I don't know, come
[2057.94 → 2059.66] full circle on this.
[2059.82 → 2061.28] So when I was in grad school,
[2061.42 → 2063.18] I was working on computational
[2063.18 → 2065.26] physics and Dr.
[2065.32 → 2066.48] Ghost, as you said,
[2066.48 → 2071.80] a lot of this kind of just
[2071.80 → 2073.50] brute force techniques will
[2073.50 → 2075.20] get you to maybe modelling,
[2075.36 → 2078.54] you know, a hundred or a few
[2078.54 → 2080.52] hundred atoms or molecules.
[2081.38 → 2083.38] And I remember at the time
[2083.38 → 2085.52] when I was in school, it was
[2085.52 → 2087.68] kind of the first time I had
[2087.68 → 2088.88] seen like kind of at the end
[2088.88 → 2089.98] of my grad school, people
[2089.98 → 2091.20] started to apply machine
[2091.20 → 2093.46] learning techniques to
[2093.46 → 2095.12] figure out like the energy
[2095.12 → 2097.02] functionals and things that
[2097.02 → 2098.28] we were trying to figure out
[2098.28 → 2100.16] kind of just from scratch
[2100.16 → 2101.50] by writing good equations
[2101.50 → 2103.48] and kind of instantly
[2103.48 → 2105.08] outperformed everything that
[2105.08 → 2106.42] we were doing.
[2106.42 → 2107.92] And it was kind of a shock
[2107.92 → 2109.58] to all of us.
[2109.58 → 2111.64] But it just kind of it
[2111.64 → 2112.70] illustrates, as you were
[2112.70 → 2114.26] saying, Marcus, the power
[2114.26 → 2116.56] that you can
[2116.56 → 2117.54] can achieve.
[2117.54 → 2119.12] And in certain cases by
[2119.12 → 2121.16] reimagining a problem as an
[2121.16 → 2122.74] as an AI or as a machine
[2122.74 → 2125.08] learning problem, I'm
[2125.08 → 2125.42] curious.
[2125.68 → 2127.84] So I was kind of just, you
[2127.84 → 2129.20] know, browsing around as you
[2129.20 → 2130.80] were talking on the
[2130.80 → 2132.28] Xanadu website and a couple
[2132.28 → 2132.66] others.
[2132.66 → 2134.60] And I see, you know, certain
[2134.60 → 2135.72] phrases like, you know,
[2135.76 → 2137.12] machine learning toolbox for
[2137.12 → 2138.56] quantum computing powered by
[2138.56 → 2140.32] TensorFlow and other things.
[2140.32 → 2143.28] So is that more on the side
[2143.28 → 2145.40] of, you know, using say using
[2145.40 → 2147.70] TensorFlow, using AI to
[2147.70 → 2151.04] to kind of learn more about
[2151.04 → 2152.22] quantum computing or
[2152.22 → 2153.66] or those things more on the
[2153.66 → 2155.02] side of kind of doing,
[2155.22 → 2157.28] you know, creating a quantum
[2157.28 → 2158.52] computing module for
[2158.52 → 2159.18] for TensorFlow?
[2159.70 → 2160.08] Yes.
[2160.18 → 2162.14] OK, so, yeah, one thing
[2162.14 → 2164.12] that's being done by
[2164.12 → 2165.64] Xanadu and that I'm
[2165.64 → 2166.54] playing around with, too, in
[2166.54 → 2168.30] my research is using
[2168.30 → 2170.26] tools that exist and are
[2170.26 → 2171.32] inherently classical, of
[2171.32 → 2172.22] course, like TensorFlow
[2172.22 → 2174.96] and TPUs and
[2174.96 → 2175.80] GPUs.
[2175.80 → 2177.44] And, you know, looking at
[2177.44 → 2178.46] all the different classical
[2178.46 → 2180.56] technology that exists and
[2181.28 → 2183.26] seeing what can be done to
[2183.26 → 2185.64] sort of emulate, simulate
[2187.02 → 2189.20] or predict the outcomes of
[2189.20 → 2191.32] quantum computations.
[2191.32 → 2191.94] And so, yes.
[2191.94 → 2193.90] So what Xanadu is doing is
[2194.26 → 2195.66] actually using TensorFlow as
[2195.66 → 2196.26] a back end.
[2196.26 → 2199.52] So when you are using
[2199.72 → 2201.56] Penny Lane or strawberry fields
[2201.58 → 2203.68] to sort of express a quantum
[2203.68 → 2205.78] experiment, and you choose
[2205.78 → 2206.96] to use the TensorFlow back
[2206.96 → 2208.12] end, what it's doing is using
[2208.12 → 2209.46] TensorFlow to actually simulate
[2209.46 → 2210.38] that quantum process.
[2211.06 → 2212.74] So it's kind of helping you
[2212.74 → 2214.00] learn about how the experiment
[2214.00 → 2214.54] might go.
[2214.80 → 2216.34] Is that a way to
[2216.34 → 2217.32] to put it or?
[2217.76 → 2217.88] Sure.
[2217.98 → 2218.12] Yeah.
[2218.20 → 2219.88] I mean, it's implementing the
[2219.88 → 2221.76] mathematics of it, right, of
[2221.76 → 2222.12] the model.
[2222.38 → 2224.54] So if you have TensorFlow as
[2224.54 → 2226.38] your back end, then it's
[2226.38 → 2227.22] possible that you could
[2227.22 → 2230.64] actually express gate
[2230.64 → 2232.80] level quantum computations and
[2232.80 → 2234.20] get them sort of compiled down
[2234.20 → 2237.42] to, well, not compiled, but sort
[2237.42 → 2239.76] of interpreted and changed into
[2239.76 → 2241.88] TensorFlow code, which is Python
[2241.88 → 2243.76] that it's that's like creating
[2243.76 → 2245.00] matrices, doing matrix
[2245.00 → 2246.54] multiplication, defining a
[2246.54 → 2247.22] tensor network.
[2247.22 → 2249.68] And then that can get sent off to
[2249.68 → 2251.70] Google, who then implements that
[2251.70 → 2254.40] on a TPU and gives you your
[2254.40 → 2256.08] results through the Google
[2256.08 → 2258.16] cloud, or I think they're calling
[2258.16 → 2259.24] it Athos now or whatever.
[2259.40 → 2261.30] But, you know, yeah.
[2261.38 → 2262.98] So it's using it as a
[2262.98 → 2265.06] simulator back end to sort of help
[2265.06 → 2267.14] physicists learn and inform
[2267.14 → 2268.86] themselves and also demonstrate
[2268.86 → 2271.06] theories like there is certainly
[2271.06 → 2272.64] power in the classical
[2272.64 → 2273.50] infrastructure that exists.
[2274.00 → 2275.48] What's really cool is how the
[2275.48 → 2276.52] machine learning infrastructure is
[2276.52 → 2278.24] getting used now to sort of
[2278.24 → 2279.78] simulate many body physics.
[2280.94 → 2282.20] And TensorFlow is just one
[2282.20 → 2282.48] example.
[2282.48 → 2291.94] This episode is brought to you by
[2291.94 → 2292.62] Strong DM.
[2293.12 → 2295.04] Strong DM makes it easy for DevOps
[2295.04 → 2297.12] to enforce the controls' infosec
[2297.12 → 2299.04] teams require, manage access to
[2299.04 → 2301.02] any database server in any
[2301.02 → 2301.48] environment.
[2302.00 → 2302.96] And in this segment, we're talking
[2302.96 → 2304.90] to Jim Mortco, VP of engineering
[2304.90 → 2305.48] at Hearst.
[2305.56 → 2306.80] He's sharing how they're using
[2306.80 → 2309.02] Strong DM within their team of 90
[2309.02 → 2310.10] plus engineers.
[2310.10 → 2311.10] engineers.
[2311.10 → 2312.56] It now takes them just 60 seconds
[2312.56 → 2314.78] to offboard a team member from a
[2314.78 → 2315.36] data source.
[2315.78 → 2316.86] We have an engineering team of
[2316.86 → 2318.70] somewhere in the area of 80 or 90
[2318.70 → 2319.20] engineers.
[2319.44 → 2321.02] Because we've got so many services
[2321.02 → 2323.54] and many databases and so many
[2323.54 → 2325.30] developers, we need a reasonable way
[2325.30 → 2326.36] to manage access to them.
[2326.78 → 2328.66] It was a somewhat painful and
[2328.66 → 2330.38] you know, labour intensive process.
[2330.78 → 2333.82] Our DevOps team would literally have to
[2333.82 → 2335.22] manage every one of the permissions
[2335.22 → 2336.78] for everybody who wanted access.
[2337.56 → 2339.54] So Strong DM has been a real godsend
[2339.54 → 2340.42] in that area for us.
[2340.78 → 2342.22] Requests for access to specific
[2342.22 → 2344.26] databases were pretty much manual.
[2344.46 → 2345.70] Now we've adopted Strong DM.
[2346.04 → 2347.48] It's something that you don't even
[2347.48 → 2348.04] know is there.
[2348.18 → 2349.62] Once it's installed, it just works.
[2349.70 → 2350.32] It's very simple.
[2350.62 → 2352.28] We've set up a multitude of data
[2352.28 → 2354.02] sources so that when somebody's
[2354.02 → 2355.84] onboarded, we just give them access
[2355.84 → 2356.54] to Strong DM.
[2356.90 → 2357.72] It's pretty simple.
[2358.10 → 2360.38] Our DevOps team, they have a very
[2360.38 → 2361.88] minimal effort required to enable
[2361.88 → 2363.78] each data source to be connected to
[2363.78 → 2365.46] Strong DM and then installing the
[2365.46 → 2367.70] client software is very, very simple
[2367.70 → 2368.22] and straightforward.
[2368.46 → 2369.98] You can use whatever client you want
[2369.98 → 2370.78] to talk to the database.
[2370.96 → 2371.96] So there's really no training
[2371.96 → 2372.40] necessary.
[2372.92 → 2373.20] All right.
[2373.22 → 2374.58] If your team can benefit from nearly
[2374.58 → 2376.88] instant onboarding and offboarding
[2376.88 → 2379.42] that's fully SOC2 compliant, head to
[2379.42 → 2382.04] StrongDM.com to learn more and request
[2382.04 → 2382.76] a free demo.
[2383.12 → 2385.14] Again, StrongDM.com.
[2393.78 → 2401.18] So earlier, I know that you had
[2401.18 → 2403.24] mentioned the quantum emulation
[2403.24 → 2404.64] project that you were working on.
[2404.82 → 2406.34] Could you describe that a bit more?
[2406.82 → 2406.94] Sure.
[2407.10 → 2410.32] So this is one of my research projects
[2410.32 → 2413.34] with Dr. Gone through the IOC.
[2413.50 → 2416.36] So the quantum emulation project is
[2416.36 → 2419.88] sort of the umbrella for all of our
[2419.88 → 2422.12] research into quantum emulation.
[2422.12 → 2426.02] And this is sort of the research that
[2426.02 → 2427.18] has led me to get involved with
[2427.18 → 2429.76] Xanadu contributing to their library
[2429.76 → 2430.50] for Python.
[2431.62 → 2434.98] It's also sort of encapsulate,
[2435.12 → 2438.08] encapsulates my thinking about how
[2438.08 → 2439.60] can hardware potentially emulate
[2439.60 → 2440.30] quantum physics.
[2441.76 → 2444.16] And yeah, so the project itself is
[2444.16 → 2444.88] multifaceted.
[2446.26 → 2448.20] And as you explain that, could you
[2448.20 → 2449.46] also kind of define what quantum
[2449.46 → 2450.50] emulation would be?
[2450.50 → 2451.44] Oh, sure.
[2451.58 → 2451.72] Yeah.
[2452.06 → 2454.70] So this is a yeah, interesting word
[2454.70 → 2456.36] choices, emulation versus simulation,
[2456.50 → 2456.64] right?
[2456.82 → 2458.82] So simulation and emulation.
[2459.16 → 2460.40] I'm thinking of like the Nintendo
[2460.40 → 2462.00] games I play on my Raspberry Pi.
[2462.10 → 2462.26] Right.
[2462.34 → 2462.48] Yeah.
[2462.54 → 2462.68] Okay.
[2463.70 → 2467.26] It's not that, but related.
[2467.58 → 2469.70] So when I say emulation, what I'm
[2469.70 → 2472.34] referring to is a physical system that
[2472.34 → 2475.18] more closely behaves like a quantum
[2475.18 → 2479.48] physical system rather than a software
[2479.48 → 2480.22] simulation.
[2480.22 → 2484.50] So it's very kind of a nitpicky sort
[2484.50 → 2485.66] of difference between simulation and
[2485.66 → 2486.06] emulation.
[2486.06 → 2487.30] But when I'm talking about an emulator,
[2487.30 → 2488.62] it would be something implemented in
[2488.62 → 2490.94] hardware that's designed sort of from
[2490.94 → 2493.10] physics to behave more like quantum
[2493.10 → 2493.46] physics.
[2494.14 → 2495.46] Whereas if I was talking about a
[2495.46 → 2497.32] simulation, I would probably just be
[2497.32 → 2498.24] talking about something I wrote in
[2498.24 → 2498.48] Python.
[2498.48 → 2499.50] Okay.
[2499.50 → 2502.56] And the, the, the, the, the pieces of
[2502.56 → 2504.30] hardware in this sort of emulation,
[2504.30 → 2505.52] what are those?
[2505.58 → 2507.20] Are those pieces of classical hardware
[2507.20 → 2510.34] that are kind of bolted together to
[2510.34 → 2513.30] along with certain software elements to
[2513.30 → 2515.26] do this emulation or what are, what are
[2515.26 → 2515.76] those pieces?
[2515.76 → 2517.58] Are those like, you know, nodes in the
[2517.58 → 2519.66] cloud or what are, what are we talking
[2519.66 → 2520.08] about there?
[2520.42 → 2520.86] Yeah.
[2520.90 → 2521.10] Okay.
[2521.10 → 2522.86] So when I'm talking about a quantum
[2522.86 → 2525.82] emulator, there's sort of actually a
[2525.82 → 2529.82] bunch of research around emulation of
[2530.40 → 2531.20] quantum computing.
[2531.60 → 2533.18] There have been papers about doing this
[2533.18 → 2534.24] with FPGAs.
[2535.66 → 2538.88] There's been a paper about how rough and
[2538.88 → 2541.30] hard it is to do this with analog
[2541.30 → 2545.12] computing elements like op amps and
[2545.12 → 2545.54] such.
[2546.42 → 2547.98] But yeah, I'm, so I'm sort of looking at
[2547.98 → 2550.96] the whole, the whole spread of options
[2550.96 → 2552.86] taking a look at what can be done with
[2552.86 → 2554.44] FPGAs, what can be done with analog,
[2555.10 → 2557.28] how can this be orchestrated efficiently
[2557.28 → 2559.06] to work with sort of the machine
[2559.06 → 2561.22] learning tools that exist, which are
[2561.22 → 2562.62] mostly accessible through the cloud.
[2563.48 → 2566.28] And yeah, so one of the sort of
[2566.28 → 2567.98] questions that I want to answer with
[2567.98 → 2571.06] the research is what can be done to
[2571.06 → 2572.04] take this to the next level.
[2572.04 → 2575.00] We have stuff like what Xanadu is
[2575.00 → 2577.04] producing, which is awesome, expressive
[2577.04 → 2577.52] Python.
[2578.48 → 2580.28] They're also working on a specific
[2580.28 → 2581.66] type of backend hardware, which is
[2581.66 → 2583.16] continuous variable quantum computing.
[2583.46 → 2586.98] We have IBM, and we have all these
[2586.98 → 2587.96] cloud tools as well.
[2588.06 → 2590.08] Can we bring them together and what
[2590.08 → 2592.46] would be missing to make this a
[2592.46 → 2593.02] viable system?
[2593.22 → 2596.22] And is there something I can do to add
[2596.22 → 2597.44] that secret sauce or whatever is
[2597.44 → 2597.68] missing?
[2598.00 → 2601.44] Dr. Ghost, what does success look like
[2601.44 → 2602.42] from your perspective?
[2602.88 → 2605.36] Where should the project be heading and
[2605.36 → 2607.64] what kinds of things are you hoping to
[2607.64 → 2608.66] see come out of the project?
[2609.42 → 2611.62] You mean Marcus's project or process?
[2612.08 → 2613.78] Yeah, I thought I'm sorry.
[2613.88 → 2615.88] I was thinking that both of you were
[2615.88 → 2616.84] participating in that.
[2616.96 → 2618.48] So I can turn it to either one of you all,
[2618.62 → 2620.90] whichever one would like to take a
[2620.90 → 2621.50] stab at it.
[2622.02 → 2623.66] Well, so what Marcus is working on is
[2623.66 → 2625.18] part of a broader research program
[2625.18 → 2627.22] that's in my team, which is why I
[2627.22 → 2629.42] wanted to clarify whether you're talking
[2629.42 → 2632.26] about our research in general.
[2632.64 → 2635.40] So, you know, research success is
[2635.40 → 2636.98] basically exploring something that
[2636.98 → 2639.14] nobody has ever done before and
[2639.14 → 2641.00] figuring out whether you
[2641.00 → 2644.24] actually build something new that is
[2644.24 → 2645.12] useful or not.
[2645.20 → 2645.98] You learn something.
[2646.46 → 2648.40] That's the definition of research.
[2649.08 → 2651.70] So in that sense, you know, this is a
[2651.70 → 2653.34] great area to be in because nobody knows
[2653.34 → 2654.16] anything about anything.
[2654.16 → 2657.80] So that's really how we approach it,
[2657.90 → 2660.40] as in let's, it's almost like playing,
[2660.60 → 2660.80] right?
[2660.90 → 2663.68] Here's this kind of unexplored territory,
[2663.96 → 2666.62] kind of like a new planet in Star Trek.
[2667.66 → 2668.46] And we...
[2668.46 → 2668.80] There you go.
[2668.88 → 2669.56] You did make it.
[2670.94 → 2673.46] And so we, you know, we beamed out to
[2673.46 → 2675.08] this planet, and we start exploring.
[2675.54 → 2677.94] And part of that is to say, well, given
[2677.94 → 2680.78] our current tools, which is that we have
[2680.78 → 2684.00] some access to kind of toy,
[2684.00 → 2685.66] quantum computers as of now,
[2685.80 → 2688.80] and we have this huge, powerful new
[2688.80 → 2691.50] tool set offered through, you know,
[2692.04 → 2693.88] AI and machine learning.
[2694.00 → 2695.92] And we have our current hardware,
[2696.18 → 2698.14] which are, you know, supercomputers and,
[2698.22 → 2699.80] you know, whatever is the latest
[2699.80 → 2700.72] processor today.
[2701.16 → 2702.88] Given what we have today, what's the
[2702.88 → 2703.86] best we can do?
[2704.16 → 2706.58] And what can we learn about, you know,
[2706.76 → 2708.26] what can and cannot be done?
[2708.34 → 2710.40] So, for example, in Marcus's project,
[2710.68 → 2712.72] which, you know, if it comes down to it,
[2712.72 → 2714.74] is going to be limited by the fact that
[2714.74 → 2716.22] we don't have a real quantum computer,
[2716.32 → 2716.50] right?
[2716.52 → 2718.24] So we're going to try to, as you said,
[2718.34 → 2721.98] emulate it using what hardware we can
[2721.98 → 2723.48] build now, for example.
[2723.76 → 2725.42] And the reason to do that is not because
[2725.42 → 2727.48] we expect to somehow replace an actual
[2727.48 → 2728.20] quantum computer,
[2728.60 → 2731.26] but it is to explore what is the actual
[2731.26 → 2732.98] power of a full quantum computer, right?
[2733.02 → 2735.34] Where is that transition happening?
[2735.34 → 2739.42] What is that special fuel that we will
[2739.42 → 2740.82] not be able to emulate, right?
[2740.88 → 2742.76] So in this sense, almost success is not
[2742.76 → 2744.56] succeeding at a certain task, right?
[2744.86 → 2746.98] As in, here is where we would really need
[2746.98 → 2747.68] a quantum computer.
[2747.88 → 2749.66] And so that's what we should focus on.
[2750.10 → 2751.84] So that's kind of how we approach this
[2751.84 → 2753.96] project and research in general.
[2754.30 → 2756.74] I don't know if that is very clear,
[2756.92 → 2758.62] but, you know, research by definition
[2758.62 → 2762.10] is just a lot of going down blind alleys
[2762.10 → 2764.10] and failing a lot and then finding,
[2764.32 → 2767.06] you know, some unexpected discovery
[2767.06 → 2768.76] and then taking it from there.
[2769.46 → 2773.62] Yeah, I have maybe a practical question
[2773.62 → 2777.06] from my perspective as kind of
[2777.06 → 2781.90] being previously in academia
[2781.90 → 2784.46] and also now viewing,
[2784.60 → 2786.70] like you were saying, Dr. Ghost,
[2786.70 → 2790.16] the kind of the powerful tools
[2790.16 → 2791.28] that are available right now
[2791.28 → 2792.76] in TensorFlow and AI.
[2793.54 → 2794.86] And I'm just thinking like back
[2794.86 → 2796.22] to when I was in grad school,
[2796.26 → 2797.42] I think a lot of that
[2797.42 → 2799.46] in some ways would be overwhelming
[2799.46 → 2802.38] for me to like to take in
[2802.38 → 2804.96] in addition to like quantum physics
[2804.96 → 2806.74] and all the other things.
[2806.82 → 2808.62] So I was wondering from
[2808.62 → 2811.56] Marcus, maybe your perspective
[2811.56 → 2813.88] or Dr. Ghost, from your perspective
[2813.88 → 2816.90] as a team and a research group
[2816.90 → 2817.48] in general,
[2817.48 → 2821.48] how have you found the process
[2821.48 → 2824.02] of kind of looking at the problem set
[2824.02 → 2824.78] that's in front of you,
[2824.86 → 2827.80] deciding to use AI and TensorFlow
[2827.80 → 2828.92] and those sorts of things
[2828.92 → 2831.54] and figuring out how to apply TensorFlow
[2831.54 → 2834.26] to your research problem?
[2834.68 → 2836.34] Do you have any tips for those out there
[2836.34 → 2838.80] that are maybe doing some sort of research,
[2838.80 → 2841.28] whether that's an R&D in industry
[2841.28 → 2843.98] or in academia or elsewhere,
[2843.98 → 2845.78] and they see the power
[2845.78 → 2848.28] of what maybe they could achieve with AI,
[2848.78 → 2850.88] but it seems overwhelming for them.
[2850.98 → 2851.76] Do you have any tips
[2851.76 → 2854.82] as far as them getting into this
[2854.82 → 2855.84] and starting to apply
[2855.84 → 2856.80] these sorts of techniques
[2856.80 → 2857.48] in their research?
[2858.12 → 2858.44] Absolutely.
[2858.76 → 2858.92] Yeah.
[2858.92 → 2862.06] I think one of the best things I did
[2862.06 → 2863.46] was just getting involved
[2863.46 → 2865.06] in the open source stuff
[2865.06 → 2865.68] that's out there
[2865.68 → 2867.92] and the Slacks that are available.
[2869.74 → 2871.66] There's a great Slack
[2871.66 → 2872.82] that's hosted by Xanadu
[2872.82 → 2875.24] where people are discussing this stuff.
[2875.96 → 2878.38] And yeah, I think it's awesome
[2878.38 → 2879.14] that these communities
[2879.14 → 2880.04] are starting to emerge
[2880.04 → 2882.56] because there's really smart people
[2882.56 → 2885.12] thinking about fascinating things
[2885.12 → 2887.34] that you can have discussions with,
[2887.34 → 2889.16] whether it's in person or not.
[2890.66 → 2891.56] And the other thing is
[2891.56 → 2892.28] just to read a ton.
[2892.48 → 2894.24] I mean, Dr. Ghost will have more to say too,
[2894.34 → 2895.78] but sort of my strategies have been
[2895.78 → 2897.22] get involved and ask questions
[2897.22 → 2898.50] of people who are experts
[2898.50 → 2900.50] and read a lot.
[2900.68 → 2901.76] So I read a lot of papers
[2901.76 → 2904.20] and that's sort of what I do
[2904.20 → 2905.30] when I'm done working for the day.
[2906.36 → 2908.04] So just to build on that broadly,
[2908.28 → 2910.42] research seems to be
[2911.28 → 2913.80] not so well-defined when you start.
[2913.88 → 2914.74] And I think a lot of,
[2915.20 → 2916.34] especially for students,
[2916.34 → 2918.14] that's hard to get into.
[2918.44 → 2919.78] But there's actually a method
[2919.78 → 2921.38] to all of what we do.
[2921.92 → 2923.54] And as Marcus alluded to it,
[2923.82 → 2925.14] we have to get up to speed.
[2925.26 → 2926.32] So we have to, you know,
[2926.52 → 2928.90] do the background sort of legwork
[2928.90 → 2930.64] and try to understand
[2930.64 → 2932.76] where the field is currently.
[2933.02 → 2933.82] So, you know,
[2933.88 → 2935.32] pick a particular topic
[2935.32 → 2936.16] and then, yeah,
[2936.22 → 2937.34] try to read up on it
[2937.34 → 2938.34] to whatever level
[2939.18 → 2940.18] you're comfortable with.
[2940.28 → 2942.28] And as you read something
[2942.28 → 2944.16] and try to learn a field,
[2944.16 → 2945.80] you will automatically find
[2945.80 → 2946.60] that there are some pieces
[2946.60 → 2947.42] you don't understand.
[2947.72 → 2948.84] And sometimes that's about
[2948.84 → 2949.90] you just being confused.
[2950.02 → 2950.62] So then you have to go
[2950.62 → 2952.42] and read up a little more on that.
[2952.80 → 2954.00] But sometimes it's because
[2954.00 → 2955.02] that just happens to be
[2955.02 → 2956.36] an open question in the field.
[2956.64 → 2958.06] And that's how you can identify
[2958.06 → 2959.02] new questions
[2959.02 → 2960.62] that you can go and do research in.
[2961.38 → 2962.70] And so that's kind of a technique
[2962.70 → 2963.14] that, you know,
[2963.14 → 2963.88] you have to sort of,
[2963.96 → 2964.88] just like everything else,
[2964.88 → 2966.14] you have to, you know,
[2966.54 → 2967.32] practice it
[2967.32 → 2968.70] and get used to it.
[2968.90 → 2970.08] And that then it becomes
[2970.08 → 2970.78] more natural
[2970.78 → 2971.72] to the point where
[2971.72 → 2972.30] you don't even know
[2972.30 → 2972.80] you're doing it.
[2972.86 → 2973.48] But every time
[2973.48 → 2975.00] you look at a new area,
[2975.18 → 2976.76] you sort of scan the field,
[2976.82 → 2978.40] you do like almost a survey
[2978.40 → 2980.66] and then you identify parts
[2980.66 → 2982.14] that have been unexplored.
[2982.52 → 2983.52] And then you try to think,
[2983.60 → 2983.84] okay,
[2984.24 → 2985.22] if this has not been explored,
[2985.30 → 2986.12] let me go and find out
[2986.12 → 2987.56] who else is working on it.
[2987.62 → 2988.78] Maybe I can work with them.
[2988.86 → 2989.88] And if nobody else
[2989.88 → 2990.66] is working on it,
[2990.70 → 2992.54] then either it's really hard
[2992.54 → 2994.62] or it's, you know,
[2994.64 → 2995.50] you found something
[2995.50 → 2996.54] interesting to work on
[2996.54 → 2997.36] and you should go ahead
[2997.36 → 2998.58] and try to, you know,
[2998.62 → 2999.60] find an approach
[2999.60 → 3001.08] to attack that problem
[3001.08 → 3001.72] if that's something
[3001.72 → 3002.28] you're interested in.
[3002.30 → 3003.88] So that's broadly the method.
[3005.02 → 3006.66] Yeah, I appreciate that.
[3006.76 → 3008.30] And I think that there's,
[3009.08 → 3010.06] I don't know,
[3010.18 → 3012.48] that over time,
[3012.48 → 3013.82] I've learned that the people
[3013.82 → 3015.62] that I feel like
[3015.62 → 3017.32] are able to adapt
[3017.32 → 3018.10] very quickly
[3018.10 → 3019.46] and, you know,
[3019.52 → 3020.96] really advance quickly
[3020.96 → 3022.08] are those that are willing
[3022.08 → 3024.44] to just ask a lot of questions
[3024.44 → 3026.02] and be willing to
[3026.02 → 3027.86] not be prideful
[3027.86 → 3028.58] and say like,
[3028.68 → 3029.74] oh, I feel like
[3029.74 → 3030.92] I should know this.
[3030.92 → 3031.40] but really,
[3031.50 → 3032.22] if you don't know,
[3032.34 → 3032.56] you know,
[3032.56 → 3033.56] be willing to ask,
[3033.64 → 3035.36] be willing to research.
[3035.78 → 3036.86] I think, you know,
[3036.92 → 3038.10] I've learned over time
[3038.10 → 3039.60] that people's spheres
[3039.60 → 3040.22] of knowledge,
[3040.36 → 3041.10] individual spheres
[3041.10 → 3041.56] of knowledge
[3041.56 → 3042.34] are much smaller
[3042.34 → 3044.76] than I originally envisioned,
[3044.76 → 3045.42] that no one
[3045.42 → 3046.70] has all the pieces
[3046.70 → 3047.36] of information
[3047.36 → 3048.70] to do a lot
[3048.70 → 3049.74] of these sorts of problems.
[3049.74 → 3050.56] and so it involves
[3050.56 → 3051.50] a lot of being willing
[3051.50 → 3052.62] to discuss
[3052.62 → 3053.84] and ask questions.
[3054.16 → 3054.88] So appreciate
[3054.88 → 3056.40] that perspective.
[3056.96 → 3058.66] Maybe to kind of bring us
[3058.66 → 3060.02] to a little bit
[3060.02 → 3061.00] of a close here,
[3061.16 → 3063.78] regarding quantum computing
[3063.78 → 3064.92] in general,
[3065.52 → 3066.68] and I know that,
[3066.92 → 3067.70] Marcus,
[3067.80 → 3068.22] you've mentioned
[3068.22 → 3069.38] quite a few things
[3069.38 → 3070.28] and open source things
[3070.28 → 3070.92] to start with.
[3071.08 → 3073.76] If people want to start
[3073.76 → 3075.16] and get exposed
[3075.16 → 3077.28] to quantum computing,
[3077.50 → 3078.16] maybe they're
[3078.16 → 3079.12] software engineers,
[3079.44 → 3080.46] but they're really
[3080.46 → 3082.34] interested in quantum computing,
[3082.76 → 3083.88] maybe even contributing
[3083.88 → 3085.32] to open source projects,
[3085.56 → 3086.80] where might be
[3086.80 → 3087.58] a good place
[3087.58 → 3088.56] for them to start
[3088.56 → 3089.18] to learn
[3089.18 → 3090.38] kind of the basics
[3090.38 → 3091.46] of quantum computing
[3091.46 → 3092.28] and then maybe
[3092.28 → 3094.32] start building something?
[3094.76 → 3094.98] Sure.
[3094.98 → 3096.16] So there are
[3096.16 → 3097.10] a few places to go.
[3097.38 → 3098.56] There's something called
[3098.56 → 3100.08] the Quantum Open Source Foundation,
[3100.98 → 3102.76] and they sort of have
[3102.76 → 3103.24] a collection
[3103.24 → 3104.18] of great projects.
[3105.76 → 3107.14] But in terms of
[3107.14 → 3108.48] getting involved
[3108.48 → 3109.74] sort of from the ground up,
[3109.96 → 3111.10] I think the best place
[3111.10 → 3112.00] for software developers
[3112.00 → 3113.04] to start
[3113.04 → 3113.90] is with IBM
[3113.90 → 3114.64] just because
[3114.64 → 3115.88] their focus
[3115.88 → 3116.80] is really on
[3116.80 → 3118.62] sort of introducing
[3118.62 → 3119.56] quantum computing
[3119.56 → 3121.10] to the world
[3121.10 → 3121.84] and especially
[3121.84 → 3122.92] from a software perspective.
[3123.08 → 3123.40] So they have
[3123.40 → 3124.68] really great tutorials,
[3124.98 → 3126.50] they have
[3126.50 → 3127.42] a fantastic
[3127.42 → 3128.22] Python library
[3128.22 → 3129.54] called Ki skit,
[3130.04 → 3131.18] which enables you
[3131.18 → 3131.86] to sort of
[3131.86 → 3132.96] learn through
[3132.96 → 3133.72] tutorials
[3133.72 → 3134.36] and through
[3134.36 → 3135.28] expressive programming
[3135.28 → 3136.44] how quantum computing
[3136.44 → 3137.24] might work.
[3138.64 → 3139.54] And as I mentioned,
[3139.62 → 3139.92] they have lots
[3139.92 → 3140.76] of open source stuff too.
[3140.86 → 3141.70] So I think
[3141.70 → 3142.26] that's a great
[3142.26 → 3142.92] starting point.
[3143.30 → 3143.90] And once you've
[3143.90 → 3144.56] sort of mastered
[3144.56 → 3145.48] what you're doing there,
[3145.62 → 3146.68] I think then you can
[3146.68 → 3147.50] branch off to more
[3147.50 → 3148.90] sort of exotic flavours
[3148.90 → 3150.02] of quantum computing
[3150.02 → 3151.56] like continuous variable,
[3151.70 → 3152.42] which is Xanadu's,
[3152.48 → 3152.74] and they have
[3152.74 → 3153.78] fantastic documentation,
[3153.90 → 3154.24] by the way.
[3154.98 → 3156.30] But I think
[3156.30 → 3157.78] sort of the world
[3157.78 → 3158.66] opens up once you've
[3158.66 → 3159.92] learned it in one place
[3159.92 → 3161.22] and IBM is really great
[3161.22 → 3162.44] at sort of onboarding,
[3162.50 → 3162.74] I think.
[3163.24 → 3163.42] Awesome.
[3163.96 → 3164.30] Well,
[3164.48 → 3166.24] thank you both
[3166.24 → 3167.50] for taking time
[3167.50 → 3168.08] out of your
[3168.08 → 3170.38] busy schedules
[3170.38 → 3171.88] and out of your
[3171.88 → 3173.36] attempts to,
[3173.36 → 3174.08] you know,
[3174.28 → 3176.50] kind of explore
[3176.50 → 3177.64] this whole new world
[3177.64 → 3178.90] of computing.
[3179.40 → 3180.70] Really appreciate you
[3180.70 → 3181.54] taking time
[3181.54 → 3182.86] to chat with us.
[3182.86 → 3183.52] It's been a great
[3183.52 → 3184.18] conversation
[3184.18 → 3186.16] and just
[3186.16 → 3187.56] we'll definitely
[3187.56 → 3188.62] put links
[3188.62 → 3189.48] in our show notes
[3189.48 → 3190.38] to all of those
[3190.38 → 3191.12] things that we've
[3191.12 → 3191.68] talked about
[3191.68 → 3193.30] and I'm really
[3193.30 → 3194.44] excited for
[3194.44 → 3195.42] our listeners
[3195.42 → 3196.26] to explore those
[3196.26 → 3196.74] and for me
[3196.74 → 3197.50] to explore them
[3197.50 → 3198.56] myself as well.
[3198.66 → 3199.14] So thank you
[3199.14 → 3199.58] so much
[3199.58 → 3200.40] for taking time.
[3200.88 → 3201.32] Thank you.
[3201.38 → 3201.50] Awesome.
[3201.54 → 3202.20] Thank you very much.
[3202.32 → 3202.80] Thank you.
[3202.80 → 3205.54] All right.
[3205.60 → 3206.00] Thank you for
[3206.00 → 3206.68] tuning into this
[3206.68 → 3207.60] episode of
[3207.60 → 3208.22] Practical AI.
[3208.48 → 3208.88] If you enjoyed
[3208.88 → 3209.24] the show,
[3209.30 → 3209.94] do us a favour,
[3210.04 → 3210.64] go on iTunes,
[3210.76 → 3211.42] give us a rating,
[3211.70 → 3212.58] go in your podcast
[3212.58 → 3213.58] app and favourite it.
[3213.70 → 3214.22] If you are on
[3214.22 → 3214.96] Twitter or social
[3214.96 → 3215.38] network,
[3215.50 → 3215.90] share a link
[3215.90 → 3216.40] with a friend,
[3216.48 → 3216.90] whatever you got to
[3216.90 → 3217.14] do,
[3217.38 → 3217.78] share the show
[3217.78 → 3218.12] with a friend
[3218.12 → 3218.84] if you enjoyed it.
[3219.14 → 3219.54] And bandwidth
[3219.54 → 3220.28] for Changelog
[3220.28 → 3221.24] is provided by
[3221.24 → 3221.78] Vastly.
[3221.92 → 3222.32] Learn more
[3222.32 → 3223.34] at Fastly.com
[3223.34 → 3224.08] and we catch
[3224.08 → 3224.48] our errors
[3224.48 → 3225.10] before our users
[3225.10 → 3225.58] do here at
[3225.58 → 3225.92] Changelog
[3225.92 → 3226.34] because of
[3226.34 → 3226.74] Rollbar.
[3226.94 → 3227.60] Check them out
[3227.60 → 3227.84] at
[3227.84 → 3228.40] Rollbar.com
[3228.40 → 3228.66] slash
[3228.66 → 3229.34] Changelog.
[3229.64 → 3230.12] And we're
[3230.12 → 3230.88] hosted on
[3230.88 → 3231.50] Linde Cloud
[3232.80 → 3233.30] dot com
[3233.30 → 3233.60] slash
[3233.60 → 3234.14] Changelog.
[3234.22 → 3234.68] Check them out.
[3234.76 → 3235.58] Support this show.
[3235.76 → 3237.02] This episode is
[3237.02 → 3237.52] hosted by
[3237.52 → 3238.44] Daniel Whiten ack
[3238.44 → 3239.16] and Chris Benson.
[3239.60 → 3240.44] The music is
[3240.44 → 3241.24] by Break master
[3241.24 → 3241.68] Cylinder.
[3242.04 → 3242.46] And you can
[3242.46 → 3243.16] find more shows
[3243.16 → 3244.00] just like this
[3244.00 → 3245.50] at ChangeLog.com
[3245.50 → 3246.36] when you go there,
[3246.44 → 3246.90] pop in your
[3246.90 → 3247.64] email address,
[3247.94 → 3248.46] get our weekly
[3248.46 → 3249.18] email keeping
[3249.18 → 3249.72] you up to date
[3249.72 → 3250.46] with the news
[3250.46 → 3251.22] and podcasts
[3251.22 → 3251.78] for developers
[3251.78 → 3252.96] in your inbox
[3252.96 → 3253.96] every single week.
[3254.34 → 3255.14] Thanks for tuning in.
[3255.28 → 3256.06] We'll see you next week.
[3262.80 → 3266.42] All right,
[3266.42 → 3266.88] because you've
[3266.88 → 3267.40] stuck in
[3267.40 → 3268.20] to the end
[3268.20 → 3269.00] of the show,
[3269.28 → 3269.94] here's a preview
[3269.94 → 3270.72] of Brain Science,
[3270.82 → 3271.68] our upcoming podcast
[3271.68 → 3272.88] coming out very soon.
[3273.16 → 3274.00] The easiest way
[3274.00 → 3274.62] to subscribe
[3274.62 → 3275.60] is to subscribe
[3275.60 → 3276.92] to our master feed
[3276.92 → 3277.42] at the
[3277.42 → 3278.84] ChangeLog.com
[3278.84 → 3279.68] slash master.
[3280.04 → 3280.72] Get all of our
[3280.72 → 3281.38] podcasts
[3281.38 → 3282.84] in one single feed
[3282.84 → 3283.98] plus some extras
[3283.98 → 3284.82] that only hit
[3284.82 → 3285.66] the master feed
[3285.66 → 3287.32] including Brain Science.
[3287.72 → 3288.26] Brain Science
[3288.26 → 3289.44] is a podcast
[3289.44 → 3290.14] for the curious.
[3290.36 → 3290.68] We're exploring
[3290.68 → 3291.60] the inner workings
[3291.60 → 3292.46] of the human brain
[3292.46 → 3293.08] so we can understand
[3293.08 → 3294.48] things like behaviour change,
[3294.94 → 3295.80] habit formation,
[3296.38 → 3297.12] mental health,
[3297.32 → 3297.92] and this thing
[3297.92 → 3299.04] we call the human condition.
[3299.34 → 3300.36] It's hosted by myself,
[3300.50 → 3301.46] Adam Stachowiak,
[3301.68 → 3302.56] and Meryl Reese,
[3302.82 → 3304.48] a doctor in clinical psychology.
[3304.96 → 3305.76] It's Brain Science
[3305.76 → 3306.60] applied not just
[3306.60 → 3307.58] how does the brain work,
[3307.80 → 3308.70] but how do we apply
[3308.70 → 3309.44] what we know
[3309.44 → 3310.12] about the brain
[3310.12 → 3311.40] to better our lives.
[3311.96 → 3312.36] Here we go.
[3314.02 → 3314.44] I think that's
[3314.44 → 3315.18] the most interesting
[3315.18 → 3316.14] thing I find
[3316.14 → 3317.94] with this subject
[3317.94 → 3319.40] is I've lived
[3319.40 → 3320.34] most of my life,
[3320.76 → 3320.86] well,
[3320.90 → 3321.58] I've lived all my life,
[3321.60 → 3322.58] the brain for one,
[3322.92 → 3323.64] but I've lived
[3323.64 → 3324.54] most of my life
[3324.54 → 3325.58] not even knowing
[3325.58 → 3326.30] or thinking
[3326.30 → 3328.82] about how it operates.
[3329.52 → 3330.44] And so my curiosity
[3330.44 → 3331.12] comes from,
[3331.28 → 3331.36] okay,
[3331.40 → 3333.14] now that I'm aware
[3333.14 → 3333.78] that the brain
[3333.78 → 3335.12] is the most important organ
[3335.12 → 3335.90] in my body,
[3335.96 → 3336.44] without it,
[3336.54 → 3337.52] nothing else exists
[3337.52 → 3338.74] in terms of being able
[3338.74 → 3339.14] to operate.
[3339.26 → 3340.06] It's the primary
[3340.06 → 3341.52] source of all things
[3341.52 → 3342.44] that makes our body
[3342.44 → 3343.10] our body.
[3343.50 → 3344.64] I begin to think,
[3344.74 → 3344.86] okay,
[3344.94 → 3345.06] well,
[3345.12 → 3345.66] now how does it
[3345.66 → 3346.46] actually work
[3346.46 → 3348.62] so that I can
[3348.62 → 3349.30] understand
[3349.30 → 3350.14] different things
[3350.14 → 3350.64] about my life,
[3350.64 → 3351.56] my personality,
[3351.96 → 3353.14] why I love,
[3353.30 → 3354.08] why I hate,
[3354.58 → 3355.30] why I like,
[3355.38 → 3356.04] why I dislike,
[3356.32 → 3356.46] you know,
[3356.46 → 3357.02] all these different
[3357.02 → 3357.68] things,
[3358.12 → 3358.78] habits,
[3359.56 → 3360.94] drive,
[3361.38 → 3362.38] you know,
[3362.44 → 3362.98] willpower,
[3363.08 → 3363.64] all these different
[3363.64 → 3364.68] things play into that.
[3364.68 → 3366.04] when I begin to think,
[3366.18 → 3366.22] like,
[3366.26 → 3366.44] okay,
[3366.44 → 3367.26] how can I know
[3367.26 → 3369.08] more about my brain?
[3369.18 → 3369.92] And when you mention
[3369.92 → 3370.96] these worn paths
[3370.96 → 3371.76] and these grooves,
[3371.76 → 3372.42] that means,
[3372.46 → 3372.68] like,
[3372.72 → 3373.52] whenever I'm mulling
[3373.52 → 3374.16] over a thought
[3374.16 → 3375.40] or having anxiety,
[3376.00 → 3377.48] the thing that I'm
[3377.48 → 3378.56] mulling over
[3378.56 → 3379.32] or having anxiety
[3379.32 → 3379.90] about becomes
[3379.90 → 3380.86] more and more true
[3380.86 → 3383.02] or more and more real
[3383.02 → 3385.18] as my neurons
[3385.18 → 3385.90] fire together
[3385.90 → 3387.14] based on what you said
[3387.14 → 3387.70] here with the power
[3387.70 → 3388.16] of thoughts
[3388.16 → 3388.58] is that,
[3388.68 → 3390.54] is that if I keep
[3390.54 → 3391.94] thinking that way,
[3391.94 → 3393.78] it becomes more true
[3393.78 → 3394.50] to me than maybe
[3394.50 → 3395.08] somebody else
[3395.08 → 3396.12] because I've worn
[3396.12 → 3396.70] the path.
[3396.82 → 3397.76] Is that accurate to say?
[3398.34 → 3399.08] You're spot on.
[3399.50 → 3400.96] If I'm to draw an analogy,
[3401.08 → 3402.04] it would really be
[3402.04 → 3403.12] that our thoughts
[3403.12 → 3405.06] are the lens
[3405.06 → 3405.92] through which we see
[3405.92 → 3406.40] our world
[3406.40 → 3407.80] and make sense of it,
[3407.84 → 3408.52] which is how
[3408.52 → 3409.66] people can have
[3409.66 → 3411.18] such varied perspectives.
[3412.10 → 3413.06] The thoughts we have
[3413.06 → 3414.26] are really that powerful.
[3414.40 → 3415.32] If you can imagine them
[3415.32 → 3416.24] creating the fabric
[3416.24 → 3418.24] of so much
[3418.24 → 3418.84] of your world
[3418.84 → 3419.76] and like I mentioned
[3419.76 → 3420.64] earlier about,
[3421.02 → 3421.30] you know,
[3421.34 → 3421.76] sort of finalizing
[3421.94 → 3422.74] things according
[3422.74 → 3423.60] to our feelings
[3423.60 → 3424.74] because we're more
[3424.74 → 3425.50] apt to remember
[3425.50 → 3426.44] things according
[3426.44 → 3427.06] to feelings
[3427.06 → 3429.68] and so we want
[3429.68 → 3430.44] to be aware
[3430.44 → 3431.68] of the sort of
[3431.68 → 3432.92] circular nature
[3432.92 → 3434.54] of my thoughts
[3434.54 → 3435.18] and my feelings
[3435.18 → 3435.92] and that like
[3435.92 → 3436.68] how I feel
[3436.68 → 3438.18] creates certain thoughts
[3438.18 → 3439.32] and certain thoughts
[3439.32 → 3440.40] create certain feelings
[3440.40 → 3441.94] and so if I want
[3441.94 → 3442.76] to feel different,
[3442.86 → 3443.38] I really need
[3443.38 → 3444.14] to do different
[3444.14 → 3444.66] and I need
[3444.66 → 3445.58] to think different
[3445.58 → 3447.64] because all of this
[3447.64 → 3449.34] is energy, right?
[3449.40 → 3449.58] I mean,
[3449.60 → 3450.16] you ever walk
[3450.16 → 3451.76] into a room
[3451.76 → 3453.26] or an interaction
[3453.26 → 3454.46] with an individual
[3454.46 → 3455.16] and it just sorts
[3455.16 → 3455.96] of feels off
[3455.96 → 3456.60] and you're thinking
[3456.60 → 3456.86] like,
[3456.96 → 3457.80] what did I miss?
[3457.94 → 3458.36] Or like,
[3458.64 → 3459.38] I couldn't put
[3459.38 → 3460.14] my finger on it
[3460.14 → 3461.76] but something was off
[3461.76 → 3463.96] because there are feelings
[3463.96 → 3466.38] and you catch vibes
[3466.38 → 3467.68] because emotions
[3467.68 → 3468.50] are energy
[3468.50 → 3469.42] and thoughts
[3469.42 → 3471.38] just like the neurons
[3471.38 → 3472.04] that fire together,
[3472.16 → 3473.08] that's, you know,
[3473.16 → 3473.66] electricity
[3473.66 → 3474.78] in our brain.
[3475.52 → 3476.54] It's certainly
[3476.54 → 3477.06] a deep subject
[3477.06 → 3478.36] which I'm just
[3478.36 → 3479.42] barely familiar with
[3479.42 → 3480.36] but basically
[3480.36 → 3481.42] our brain is,
[3481.86 → 3482.06] you know,
[3482.12 → 3482.92] everything is electricity
[3482.92 → 3483.48] as you're saying.
[3483.62 → 3483.72] You know,
[3483.84 → 3484.30] there's,
[3484.58 → 3487.22] it's our brain
[3487.22 → 3487.88] being able to
[3487.88 → 3488.70] somehow miraculously
[3488.70 → 3489.68] be able to process
[3489.68 → 3490.48] this electricity
[3490.48 → 3491.26] into thoughts,
[3491.80 → 3492.26] memories,
[3492.56 → 3493.10] recall,
[3493.96 → 3495.22] autobiographical,
[3495.54 → 3496.48] understanding time,
[3496.72 → 3496.86] you know,
[3496.92 → 3497.70] past, present, future,
[3497.80 → 3498.62] all this different stuff
[3498.62 → 3499.24] and somehow
[3499.24 → 3501.14] these electrical charges
[3501.14 → 3502.04] throughout our entire body
[3502.04 → 3502.96] at the cellular level
[3502.96 → 3504.02] as well as the brain level
[3504.02 → 3505.32] power us
[3505.32 → 3506.62] and like you're saying
[3506.62 → 3507.96] it truly is
[3507.96 → 3509.72] literally energy.
[3510.34 → 3510.56] It is.
[3510.68 → 3510.84] I mean,
[3510.88 → 3512.06] so one of the things
[3512.06 → 3512.88] that is important
[3512.88 → 3514.26] to know
[3514.26 → 3515.16] when it comes to neurons
[3515.16 → 3516.30] is they abide
[3516.30 → 3517.58] by the all or nothing rule
[3517.58 → 3519.48] and what I mean by that
[3519.48 → 3520.60] is that they either fire
[3520.60 → 3521.18] or they don't.
[3521.86 → 3522.52] So sort of like
[3522.52 → 3523.10] that thing
[3523.10 → 3524.18] at the carnival
[3524.18 → 3525.02] with the hammer
[3525.02 → 3526.14] and you smack
[3526.14 → 3527.66] the weighted plate
[3527.66 → 3528.58] and it either goes
[3528.58 → 3529.52] to the top to ding
[3529.52 → 3530.30] or it doesn't,
[3531.10 → 3532.36] that's how neurons are.
[3532.48 → 3533.80] They get to a sort of
[3533.80 → 3535.78] threshold of excitement
[3535.78 → 3537.22] and then they fire
[3537.22 → 3538.36] or they don't
[3538.36 → 3539.46] and so
[3539.46 → 3541.20] being able
[3541.20 → 3542.08] to be aware
[3542.08 → 3543.52] of the thoughts
[3543.52 → 3543.98] I think,
[3544.06 → 3544.52] for example,
[3544.68 → 3544.94] if I'm,
[3545.44 → 3546.16] if I am having
[3546.16 → 3547.04] a really rough day,
[3547.14 → 3548.34] like maybe I pay attention
[3548.34 → 3550.58] to what I'm thinking about,
[3550.68 → 3551.44] like am I thinking
[3551.44 → 3552.46] about a loss
[3552.46 → 3553.24] that I went through?
[3553.36 → 3554.16] Am I thinking about
[3554.16 → 3555.48] a really challenging problem
[3555.48 → 3556.06] that I don't know
[3556.06 → 3556.80] how to overcome
[3556.80 → 3558.98] or maybe it's a relationship
[3558.98 → 3559.62] that I wanted
[3559.62 → 3560.34] to go differently
[3560.34 → 3561.92] and then I don't
[3561.92 → 3562.88] feel very good
[3562.88 → 3563.70] and maybe my stomach
[3563.70 → 3564.52] starts to hurt
[3564.52 → 3565.92] and then I maybe
[3565.92 → 3566.94] start to get a headache,
[3567.44 → 3567.84] you know,
[3568.06 → 3569.90] all of our thoughts
[3569.90 → 3571.38] contribute to
[3571.38 → 3573.60] our own internal systems.
[3574.30 → 3574.80] And they shape
[3574.80 → 3576.00] who we are too,
[3576.30 → 3576.54] you know,
[3576.58 → 3576.82] like,
[3576.94 → 3577.84] like I said earlier,
[3578.44 → 3580.08] if I'm mulling over something
[3580.08 → 3581.20] or if I'm anxious
[3581.20 → 3581.72] about something,
[3581.76 → 3582.54] I just can't stop
[3582.54 → 3583.68] thinking about it.
[3584.12 → 3584.38] It,
[3584.74 → 3585.38] to some degree,
[3585.48 → 3587.18] can even reshape
[3587.18 → 3588.22] my personality
[3588.22 → 3589.54] because I think
[3589.54 → 3590.40] that's what we,
[3590.52 → 3592.06] what we might call moods.
[3592.06 → 3592.78] right,
[3592.80 → 3594.50] if I'm in a bad mood,
[3594.78 → 3596.18] it might be because
[3596.18 → 3597.42] I have an experience
[3597.42 → 3598.62] going on in my brain
[3598.62 → 3599.74] or my thoughts
[3599.74 → 3600.58] that I can't seem
[3600.58 → 3601.28] to shake away
[3601.28 → 3602.30] that's bringing me
[3602.30 → 3603.72] into a negative state.
[3604.22 → 3604.36] You know,
[3604.40 → 3604.96] my perspective
[3604.96 → 3605.54] in that scenario
[3605.54 → 3606.04] is that
[3606.04 → 3607.14] I can't get these
[3607.14 → 3607.64] bad thoughts
[3607.64 → 3608.24] out of my brain
[3608.24 → 3608.82] or I can't stop
[3608.82 → 3609.42] being anxious
[3609.42 → 3610.62] or having anxiety
[3610.62 → 3611.52] about something
[3611.52 → 3612.62] and therefore
[3612.62 → 3614.28] I yell at my wife
[3614.28 → 3615.22] or I'm not so nice
[3615.22 → 3615.80] to my son
[3615.80 → 3617.30] because my mood
[3617.30 → 3617.68] is,
[3617.78 → 3618.90] is changed
[3618.90 → 3620.00] by my thought patterns.
[3620.00 → 3621.04] Yeah,
[3621.12 → 3621.84] you're spot on
[3621.84 → 3623.76] and this is what
[3623.76 → 3624.52] I,
[3624.56 → 3625.78] I think it's so important
[3625.78 → 3627.28] that we can understand
[3627.28 → 3629.18] that it's really possible
[3629.18 → 3630.10] to change these
[3630.10 → 3632.34] because if you can recognize
[3632.34 → 3632.68] like,
[3632.92 → 3633.18] oh,
[3633.32 → 3634.38] I'm not really upset
[3634.38 → 3634.92] with my wife
[3634.92 → 3635.44] or my son,
[3635.54 → 3637.32] I'm feeling bad,
[3637.76 → 3638.36] then again,
[3638.36 → 3639.74] I can put my lid on
[3639.74 → 3640.70] and go,
[3640.92 → 3641.80] what other options
[3641.80 → 3642.90] do I have available to me?
[3643.00 → 3643.26] Like,
[3643.60 → 3644.58] maybe I need to go
[3644.58 → 3645.32] work out,
[3645.72 → 3646.80] maybe I need to
[3646.80 → 3647.72] go write down
[3647.72 → 3648.30] some of what
[3648.30 → 3649.28] is in my mind
[3649.28 → 3650.60] so that I can change
[3650.60 → 3651.56] some of those thoughts
[3651.56 → 3653.24] or maybe I need to
[3653.24 → 3654.52] do some meditation
[3654.52 → 3657.12] or talk to a friend.
[3657.68 → 3659.02] This is how we cope
[3659.02 → 3660.62] with some of those
[3660.62 → 3661.98] negative thoughts
[3661.98 → 3662.74] and negative feelings
[3662.74 → 3663.14] as well.
[3665.34 → 3666.18] That's a preview
[3666.18 → 3667.34] of Brain Science.
[3667.46 → 3668.02] If you love
[3668.02 → 3668.44] where we're going
[3668.44 → 3669.00] with this,
[3669.34 → 3670.12] email us
[3670.12 → 3671.50] to get on the list
[3671.50 → 3672.52] to be notified
[3672.52 → 3673.84] the very moment
[3673.84 → 3674.90] this show gets released.
[3675.26 → 3676.00] Email us
[3676.00 → 3676.78] at editors
[3676.78 → 3678.38] at changelaw.com
[3678.38 → 3679.26] in the subject line
[3679.26 → 3680.50] put in all caps
[3680.50 → 3681.68] BRAIN SCIENCE
[3681.68 → 3683.06] with a couple bangs
[3683.06 → 3683.92] if you're really excited.
[3684.44 → 3685.34] You can also subscribe
[3685.34 → 3686.26] to our master feed
[3686.26 → 3687.26] to get all of our shows
[3687.26 → 3688.68] in one single feed.
[3689.02 → 3690.32] Head to changelaw.com
[3690.32 → 3691.14] slash master
[3691.14 → 3692.38] or search
[3692.38 → 3693.74] in your podcast app
[3693.74 → 3694.60] for change law master.
[3694.74 → 3695.36] You'll find it.
[3695.70 → 3695.90] Subscribe,
[3696.10 → 3696.98] get all of our shows
[3696.98 → 3698.12] and even those
[3698.12 → 3698.90] that only hit
[3698.90 → 3699.78] the master feed.
[3700.04 → 3700.40] Again,
[3700.54 → 3701.28] changelaw.com
[3701.28 → 3701.92] slash master.
[3701.92 → 3731.90] We'll be right back.

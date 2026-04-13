[0.00 → 2.58] Bandwidth for Changelog is provided by Vastly.
[2.96 → 4.86] Learn more at Fastly.com.
[5.08 → 8.16] We move fast and fix things here at Changelog because of Rollbar.
[8.30 → 9.98] Check them out at Rollbar.com.
[10.22 → 12.24] And we're hosted on Linde cloud servers.
[12.74 → 14.74] Head to linode.com slash changelog.
[15.74 → 19.02] This episode is brought to you by Linde, our cloud server of choice.
[19.20 → 21.16] It is so easy to get started with Linde.
[21.48 → 23.34] Servers start at just $5 a month.
[23.58 → 26.60] We host Changelog on Linde cloud servers, and we love it.
[26.66 → 28.38] We get great 24-7 support.
[28.38 → 31.38] Zeus-like powers with native SSDs.
[31.54 → 34.58] A superfast 40 gigabits per second network.
[34.86 → 36.76] And incredibly fast CPUs for processing.
[37.20 → 39.32] And we trust Linde because they keep it fast.
[39.48 → 40.42] They keep it simple.
[40.78 → 43.18] Check them out at linode.com slash changelog.
[43.18 → 66.98] Welcome to Go Time, a podcast featuring a diverse panel and special guests discussing cloud infrastructure, distributed systems, microservices, Kubernetes, Docker.
[67.42 → 68.52] Oh, and also Go.
[68.72 → 72.30] We record live every Tuesday at 3 p.m. Eastern, noon Pacific.
[72.30 → 77.68] Join the community of Slack with us in real time during the show in the Go Time FM channel and go for Slack.
[77.88 → 78.56] Follow us on Twitter.
[78.66 → 79.70] We're at Go Time FM.
[80.24 → 85.46] Listen live at changelog.com slash live or subscribe at changelog.com slash Go Time.
[85.58 → 86.92] And now on to the show.
[86.92 → 89.60] All right.
[89.70 → 90.24] Hey, everybody.
[90.62 → 91.72] Welcome to Go Time.
[91.92 → 95.68] So this is our podcast where we talk about anything really related to Go.
[95.96 → 105.14] Today with Gopher Con coming up, what we wanted to do was talk a little bit about what sort of to expect at Gopher Con, how to get the most out of it.
[105.52 → 110.44] And in order to do that, I have two people here who have been to many, many Gopher Cons.
[110.66 → 111.92] All the Gopher Cons.
[112.24 → 112.46] Okay.
[112.56 → 113.06] All of them.
[114.54 → 115.52] So there's Mark Bates.
[115.58 → 116.08] How are you doing, Mark?
[116.26 → 116.84] All right, John.
[116.86 → 117.24] How are you doing?
[117.60 → 118.08] Pretty good.
[118.40 → 120.42] And Johnny Corsica, did I say that right?
[120.88 → 121.56] No, you didn't.
[122.90 → 124.46] I don't know how to pronounce names.
[125.20 → 125.94] We're starting out well.
[126.30 → 126.84] It's Portico.
[127.56 → 127.76] Portico.
[128.02 → 128.20] Okay.
[128.28 → 128.78] I apologize.
[129.14 → 130.76] Try emceeing conferences.
[131.08 → 132.04] It would not be fun.
[133.04 → 133.36] Again.
[134.02 → 136.60] I got into the stage where I just ask everybody their name.
[136.86 → 140.54] Like, I don't care who I, like, John, I've asked you, like, how do you pronounce your name?
[140.62 → 141.24] John Calhoun?
[141.34 → 142.12] Yes, John Calhoun.
[142.34 → 143.76] I did it to Brad Fitzpatrick.
[143.84 → 148.52] I have done it to everybody in the Go community I've introduced, whether I know them or not.
[148.62 → 148.88] All right.
[148.98 → 149.96] So, Johnny, how are you?
[150.42 → 151.26] I'm doing well.
[151.34 → 155.26] I'm quite excited about next week, actually, but we'll get into that, aren't we?
[155.50 → 155.82] Okay.
[156.00 → 158.24] And then we also have Jamal Youssef.
[158.46 → 158.66] Did I?
[159.00 → 159.36] Yes.
[159.50 → 160.04] You got it right.
[160.04 → 160.44] I did it beforehand.
[160.44 → 161.40] I want to make sure I did it right.
[162.12 → 162.44] Okay.
[163.12 → 168.14] So, Jamal is going to be at his first Gopher Con, so he's going to be here with me asking questions,
[168.34 → 172.08] trying to get the scoop, and trying to make it a little bit easier for you guys to get
[172.08 → 173.04] an idea of what to expect.
[173.26 → 173.56] Okay.
[173.76 → 177.98] So, I guess just to get started, Jamal, do you have any questions for them?
[178.20 → 178.42] Like, any?
[178.80 → 179.78] Or do you want me to start?
[179.84 → 180.30] I don't mind.
[180.56 → 180.76] No.
[180.86 → 182.72] Like, I want to know what the band is, you know?
[182.80 → 185.34] Everybody has guitars in their background, right?
[185.44 → 186.62] That's the first question.
[186.68 → 187.26] What's the band?
[187.26 → 189.38] I'm missing a part of the Go community, man.
[189.38 → 191.06] Everybody seems to play instruments, right?
[191.40 → 193.38] I got to get a guitar, a harmonica, something.
[193.86 → 196.94] Oh, if you're going to play harmonica, you're going to have to fight it out with Ron Evans,
[197.14 → 199.76] who's one of the most amazing harmonica players I've ever played.
[199.82 → 203.62] Matter of fact, I got my box of harmonicas out, bringing to San Diego, so he can teach
[203.62 → 205.46] me a few things on it.
[205.58 → 209.36] But yeah, the band, it started, this will be the third year of the band.
[209.44 → 211.08] It started a couple of years ago in Denver.
[211.08 → 216.02] And what we do is we get a full backline, a full band that comes in, and they kind of
[216.02 → 218.76] usually start the night, like a cover band, kind of fun stuff, whatever.
[219.00 → 221.46] And then basically, Gophers sign up.
[221.52 → 224.68] We choose all these songs, and we start, we learn them, and we show up, and we're like,
[224.72 → 228.28] hey, I want to play drums on this song, and I'm going to sing on this song, and I'm going
[228.28 → 229.28] to play guitar, and whatever.
[229.46 → 233.48] And we kind of pull the pieces of the band out and slot in our own.
[233.80 → 235.72] But yeah, it's a perfect time.
[236.06 → 236.74] Like I said, we've done it.
[236.96 → 238.04] They throw a huge party.
[238.14 → 238.98] I know where the party's going.
[238.98 → 240.28] Has the party been announced, Johnny?
[240.48 → 241.20] I don't know.
[241.58 → 243.58] Has the location of the party been announced?
[243.78 → 245.18] If it's not already, it's got to be soon.
[245.34 → 245.70] Yeah.
[245.90 → 248.66] I don't want to say where it is for fear of Heather.
[249.68 → 250.78] She'll chase you down, really.
[251.20 → 251.48] Yeah.
[251.64 → 255.44] So Heather is the event planner for Gopher Con.
[255.70 → 258.12] Like, she is what makes Gopher Con run.
[258.12 → 258.66] She's awesome.
[258.96 → 259.54] She's awesome.
[259.64 → 260.50] She is amazing.
[260.86 → 262.28] Jamal, do you play an instrument?
[262.60 → 267.94] You know, I got some harmonicas in a drawer that I've been meaning to learn, but I have not
[267.94 → 268.60] done that yet.
[268.60 → 274.00] But now that I see how many musicians are secretly in the Go community, I need to, you
[274.00 → 274.84] know, start practicing.
[277.26 → 282.08] I think Go, like most communities, you know, half the community's developers, right?
[282.14 → 283.68] I mean, I don't know.
[283.74 → 286.60] I know everybody, every developer, sorry, half the community's developers.
[286.72 → 287.66] Half the developer's musician.
[289.04 → 292.10] Half the development community is musicians, I would say.
[292.16 → 294.00] Like, it kind of goes together, right?
[294.00 → 295.04] So bring your harmonicas.
[295.32 → 296.50] And, you know, hey, who knows?
[296.56 → 298.92] Maybe Ron can teach you a few things when he's teaching me a few things.
[299.44 → 300.14] But it's fun.
[300.20 → 302.08] There's a Gopher Con band channel in Slack.
[302.16 → 303.12] You can drop in there.
[303.20 → 305.28] And Brian Downs does most of the organizing.
[305.46 → 307.18] And he does a really amazing job.
[307.26 → 308.40] And it's at the welcome party.
[308.70 → 310.58] So if you, I guess that's first tip, right?
[310.66 → 311.70] Go to the welcome party.
[311.70 → 314.22] Don't miss it.
[314.34 → 317.38] Like, even if you don't like parties, do not skip the welcome party.
[317.46 → 318.10] Yeah, the welcome party.
[318.18 → 319.22] It's more than just a party.
[319.28 → 321.78] Like I said, I mean, we have a band made up of fellow Gophers.
[321.90 → 327.52] Like, last year, they rented an entire park in Denver to set up the stage.
[327.60 → 330.32] And they had, what, but a dozen food trucks there.
[330.48 → 332.56] And it was just, like, it was just amazing.
[332.80 → 334.52] It's really, first year, we smashed guitars.
[334.92 → 335.42] It was a good time.
[335.82 → 336.44] Yeah, yeah.
[336.56 → 336.98] What happened?
[337.06 → 338.96] There was no guitar smashing last year?
[339.58 → 340.30] There was no guitar.
[340.30 → 344.06] I almost smashed the I had bought a guitar for the conference.
[344.06 → 345.08] And I ended up returning.
[345.18 → 346.44] And I almost smashed it on stage.
[346.44 → 349.66] Because it wouldn't even, I got halfway through one song.
[349.70 → 351.34] And it wouldn't even keep in tune anymore.
[352.52 → 354.30] But yeah, the band, the band is a hoot.
[354.42 → 355.34] And so is in the party.
[355.44 → 357.42] Like I said, it's usually good fun for everybody.
[357.58 → 360.24] And this year's location is stunning.
[360.24 → 360.90] San Diego, right?
[361.02 → 361.28] Yeah.
[362.22 → 362.54] Yeah.
[363.10 → 365.72] But where they're having the party, it's pretty awesome.
[365.84 → 366.84] You'll definitely want to attend.
[366.94 → 367.40] Let's put it that way.
[367.40 → 369.76] So I guess, like, some questions I have, right?
[369.76 → 372.86] Like, so just general going to a conference, right?
[373.16 → 375.88] It's nice to go see everybody in person for the first time.
[375.88 → 381.20] But in terms of, like, networking, I know that the conference is set up in a way to allow,
[381.20 → 384.88] like, downtime in between workshops and talks and all that.
[385.14 → 388.92] But one of the things I'm kind of struggling with is kind of planning out the entire day.
[389.12 → 394.12] It's a little overwhelming with all the talks happening at the same time, workshops and all that.
[394.12 → 397.52] Is there a preferred time to network other than, like, the welcome party?
[397.68 → 404.08] Is there, like, an unofficial, off-the-schedule, like, hey, go to this Starbucks near the hotel, right?
[404.24 → 406.36] That's where all the real gophers are going to be, right?
[407.94 → 409.92] I don't think there's any secret society.
[410.06 → 410.58] Is there, Johnny?
[410.68 → 411.96] If there is, I don't know about it.
[411.98 → 412.90] There's no speakeasy.
[413.32 → 414.26] Yeah, exactly.
[416.02 → 417.40] You know, that wouldn't be uncommon.
[417.40 → 425.30] Well, first, Jamal, I always recommend, as Johnny will tell you, dinners and lunches are a fantastic networking experience.
[425.64 → 428.40] So find me one of the days and come to lunch with me.
[428.48 → 429.58] I usually try to grab some people.
[429.68 → 430.92] So just find me and come with me.
[431.20 → 432.18] I'll introduce you around.
[432.24 → 432.96] We'll have a fun lunch.
[433.06 → 433.78] And same with Johnny.
[433.90 → 434.88] I'm sure he'll take you, too.
[435.94 → 438.34] So lunches, dinners, the events.
[438.48 → 440.08] But during the day is important, too.
[440.20 → 441.94] And there are all sorts of great breaks.
[442.12 → 445.96] They do a great job of scheduling, like, afternoon breaks and morning breaks.
[445.96 → 450.28] And, again, Heather brings out all the stops, like, snacks and whatever.
[450.74 → 452.98] And that's a great time to interact with people.
[453.14 → 454.90] So everybody's going to be in the hotel.
[455.50 → 457.00] The conference is in the Marriott.
[457.42 → 460.50] I think there's 1,200 gophers staying in that one hotel.
[462.72 → 463.40] Yeah, I know.
[463.46 → 465.92] And the rest across the street, I feel bad for everybody else in that hotel.
[466.46 → 467.84] Don't feel bad.
[467.94 → 470.42] They can just, you know, cross the street and get in there.
[471.00 → 471.48] No, no, no.
[471.54 → 472.92] I meant for the people in our hotel.
[472.92 → 476.24] So you're going to see the people.
[476.30 → 477.42] You're going to see people all the time.
[477.88 → 478.24] Right?
[478.34 → 479.00] So that's obviously a bit.
[479.06 → 482.28] But the schedule, and I'm sure Johnny has some tips in a second here.
[482.40 → 484.26] I'm just going to finish up my tip.
[484.36 → 486.12] Like, the schedule is always a tough one.
[486.16 → 487.94] Like, how do you watch the talks and network?
[488.08 → 491.32] And how do you watch three talks simultaneously and network?
[491.32 → 494.04] So my advice is always go for con.
[494.20 → 495.00] And most conferences do.
[495.10 → 498.92] But go for con in particular does an amazing job of recording the talks.
[499.34 → 501.04] Just first class.
[501.20 → 502.12] And they're all available.
[502.18 → 505.06] And they're always up within about two or three weeks after the conference.
[505.38 → 506.64] It's, like, ridiculously quick.
[506.70 → 511.56] So when you're looking at a schedule, right, and you see, say, two talks that you're really interested in.
[511.56 → 516.70] Like, my advice, it's just me, is I would go to the one that's less crowded.
[517.16 → 519.44] I'd go to the less, quote, unquote, less popular one, right?
[520.08 → 520.96] You'll find better.
[521.02 → 521.78] You'll get better seats.
[522.66 → 526.42] The speaker will really appreciate it if the room fills up with other people.
[526.54 → 527.34] You won't be standing.
[527.46 → 533.24] And a lot of times, like, the fire marshals will come out, and they'll kick people out if they're standing in the row or sitting down or stuff like that.
[533.24 → 535.64] So if you go to that one and then two weeks later, you know what you do?
[535.66 → 539.16] You sit in your living room, grab a drink, pull it up on the TV.
[539.26 → 543.94] Now you have the best seat in the house for that really, that big talk, that overcrowded talk you couldn't see.
[544.10 → 550.16] And then if nothing appeals to you, or you don't feel like, you know, I don't want to watch any of these right now, then go into the hallway.
[550.30 → 553.20] And you'll always find gophers out there, always in the hallway.
[553.26 → 553.98] And just talk to them.
[554.02 → 556.20] And, again, you can pick up those talks later.
[556.30 → 560.12] Like I said, maybe they didn't grab you at the conference where you wanted to spend 40 minutes watching it.
[560.20 → 561.42] But maybe at home you do.
[561.56 → 562.88] So that's always my advice.
[562.88 → 563.92] And don't bring your laptop.
[564.40 → 566.38] Well, if you must, bring it.
[566.60 → 567.26] But, you know, keep it.
[567.28 → 567.86] Keep it at the hotel.
[567.96 → 570.12] Where else am I going to put all the stickers I get, right?
[571.38 → 571.64] Yeah.
[571.74 → 574.46] You'll have time to decorate afterwards.
[574.74 → 576.24] But, yeah, you're going to want a shopping bag.
[576.38 → 577.92] Actually, they're giving out shopping bags.
[578.12 → 579.60] They're not doing swag bags.
[579.62 → 580.92] They're giving out bags, I believe.
[581.40 → 583.74] And then you can kind of use that bag to go shopping all week.
[583.74 → 584.08] Yep.
[584.16 → 584.36] Yep.
[584.44 → 584.86] Pretty much.
[584.96 → 585.32] Pretty much.
[585.46 → 591.38] But, yeah, I mean, to echo part of what Mark is saying is that personally, like at this point, when I go to conferences,
[591.38 → 603.28] there is my main objective is to network, is to meet people, especially those that I know of online or friends that I've met at past conferences that I want to catch up with.
[603.64 → 604.96] And meeting new people.
[604.96 → 608.78] I always make it a point to always basically set up some time, right?
[609.26 → 612.02] Or put in an extra effort to actually meet new people, right?
[612.10 → 613.02] That way it's not always.
[613.40 → 615.54] I mean, I hang out with Mark every year, right?
[615.62 → 615.72] Yeah.
[615.96 → 616.90] That's a given, right?
[616.90 → 617.52] We're going to hang out.
[617.62 → 619.60] But I don't want to spend all of my time with Mark, right?
[619.60 → 619.96] No, exactly.
[620.32 → 622.98] However, you know, the greatest personality is, right?
[622.98 → 630.82] But, you know, you want to spend time with, you know, other people as well and sort of broaden your perspective, if you will, right?
[630.82 → 633.84] So, people are going to come from all parts of the world, right?
[633.98 → 639.44] That gives you an opportunity to sort of see, okay, well, how's the girl community in your, you know, part of the world?
[639.50 → 642.80] Or how's the, you know, how have you seen girl grow, right?
[642.84 → 643.92] In your part of the world?
[643.92 → 648.16] Or what are some things that, you know, maybe you were doing well that, you know, we could learn from?
[648.16 → 653.04] So, there are a lot of these kinds of exchanges that you're going to be a part of if you try to meet as many people as you can.
[653.16 → 658.14] So, again, the talks and the keynotes, all these things are sort of recorded.
[658.28 → 659.82] You can always go back and watch them.
[660.94 → 669.40] And for some of us, you know, who are like, you know, actually Mark, both Mark and I are teaching workshops the day before the whole sort of sessions and whatnot start.
[669.80 → 672.64] So, you know, a lot of us are going to be sort of tied up, if you will.
[672.64 → 677.90] But that basically, you're still going to have a lot of opportunity to meet a lot of people, you know, you know of online.
[678.16 → 685.32] And, you know, again, this is kind of leads into my other point is that if there are people that you know of online, and you're like, oh, man, this person's always talking about how to go.
[685.42 → 686.78] You know, I'd love to meet them, whatever it is.
[687.00 → 688.72] Like, actually go talk to them, right?
[688.76 → 699.30] There's this sort of sort of this fear that if you go talk to somebody who you consider to be, you know, popular in the Go community, whatever it is that they're, you know, they're unapproachable.
[699.40 → 700.76] That couldn't be further from the truth, right?
[701.10 → 702.62] The Go community is absolutely very welcoming.
[702.82 → 707.66] And the people you know of that are part of that community, they're also very, very nice people, right?
[707.66 → 711.38] They're welcoming, and they enjoy actually talking to people and getting to know other people.
[711.48 → 714.50] So don't be afraid to actually talk to your heroes.
[714.62 → 717.98] I hate using that term, but don't be afraid to actually go talk to these people because they're people, too.
[718.06 → 718.26] Right.
[718.58 → 720.48] So absolutely take advantage of the networking time.
[720.56 → 727.52] And anytime you step out of the hallway, out of a session or the main ballroom where they usually have the keynotes and whatnot, you're going to find people out there.
[727.58 → 729.24] You're going to find sponsor booths as well.
[729.34 → 731.02] There's always people hanging out there trying to get swag.
[731.02 → 731.96] Bring a bag.
[732.02 → 732.80] Bring a shopping bag.
[733.30 → 734.54] Bring a shopping bag.
[734.92 → 735.92] Because there is...
[735.92 → 736.36] I wasn't kidding.
[736.90 → 737.08] Yeah.
[737.34 → 738.70] I mean, you will be...
[738.70 → 743.48] I mean, like every year I always joke to my family, like, look, I don't buy t-shirts, right?
[743.50 → 744.98] I just go to conference, right?
[744.98 → 745.80] Especially at Gopher Con.
[746.00 → 748.50] And basically, I replenish my wardrobe for the year, right?
[748.56 → 749.92] I'm like good on t-shirts, right?
[749.92 → 753.98] So like bring a shopping bag and walk around and there are tons of sponsors.
[754.46 → 756.48] And a lot of the stuff that they're showing is pretty cool.
[756.88 → 758.72] And a lot of it is, you know, most of it is built on go.
[759.20 → 762.78] So, you know, and obviously they're trying to recruit as well, which is another thing we can talk about in a little bit.
[763.10 → 764.62] But there's like tons of opportunities to network.
[764.80 → 766.84] And again, you network because...
[766.84 → 768.32] Like you network when you don't need it, right?
[768.36 → 769.68] That's the other piece of advice I'll give you.
[770.02 → 771.26] Network when you don't need it, right?
[771.26 → 774.94] So not when you actually need to be in touch with somebody, right?
[774.98 → 778.16] So take advantage of the situation, of the environment, right?
[778.36 → 778.72] Network.
[778.92 → 779.36] Talk to people.
[779.46 → 779.84] Meet people.
[779.92 → 780.40] And make friends.
[780.76 → 783.32] You know, I can't agree with that anymore.
[783.66 → 785.16] Like it's super important.
[785.44 → 790.76] My motto, and Johnny's probably heard me say this a hundred times, does I don't go to conferences necessarily for the talk.
[791.14 → 797.90] I go to see the people who I don't get to see every day and talk about shop and talk about things that, you know,
[797.90 → 801.48] that I can have deeper, longer conversations with in person.
[802.16 → 803.98] And that's what, you know, Johnny's saying.
[804.08 → 808.56] It's like, and by the way, Heather would kill me if it sounds like we're telling everybody not to go watch the talks.
[808.56 → 809.92] The talks are amazing.
[810.04 → 813.22] We absolutely recommend you go and watch the talks.
[813.22 → 815.66] I just, I can't stress that enough.
[815.66 → 821.30] But I'm saying you've got to also kind of don't feel obligated to fill your day watching every talk, right?
[821.30 → 823.84] Like understand that it's okay to say, you know what?
[823.84 → 827.58] There's nothing in this block that truly grabs my interest right now.
[827.98 → 830.88] So I'm going to go and find some people to talk to instead.
[831.04 → 835.22] Like that's also, you know, I think Heather would agree that is also a part of the conference too.
[835.22 → 837.38] And like I said, you know, grab some people.
[837.56 → 840.04] Just find some random people and say, hey, you want to go to lunch?
[840.34 → 842.12] You know, I kind of like a Pied Piper.
[842.24 → 843.28] I start with one or two.
[843.42 → 845.66] And as I'm walking out the door, I slow, right, Johnny?
[845.78 → 846.12] Yep, yep.
[846.12 → 847.88] I just kind of slowly pull in people.
[847.96 → 850.46] Then it's like 12 people trailing behind me off to lunch.
[850.60 → 850.72] Yep.
[851.16 → 851.84] So do it.
[851.88 → 852.46] It's worth it.
[852.56 → 854.56] The networking is 100%.
[854.56 → 855.28] And Johnny's right.
[855.58 → 857.52] Everybody in the community is super approachable.
[857.62 → 859.74] No one will yell at you or brush you off.
[859.92 → 860.54] Absolutely not.
[860.88 → 862.20] They might brush me off, but not you.
[862.20 → 878.56] This episode is brought to you by X-Team.
[878.94 → 881.82] X-Team is the world's most energizing community for developers.
[882.32 → 884.46] Work from anywhere in the world with leading brands.
[884.64 → 887.34] Experience belonging unlike any other community.
[887.94 → 890.88] And stay energized by doing more of what you love.
[890.88 → 896.12] In this segment, I talk with Ryan Chart rand, X-Team CEO, about their global community and
[896.12 → 898.36] the work they're doing to enable the supportive community.
[898.74 → 902.96] Yeah, it's interesting because there is this perception that, you know, working remotely
[902.96 → 905.04] is this digital nomad lifestyle.
[905.04 → 908.10] And it's only for, you know, people 20 to maybe 25.
[908.38 → 914.62] But the fascinating thing about X-Team is not only are we in 35 plus countries, we are across
[914.62 → 919.30] all age groups up to, I think, 55 years old, maybe even older than we have in X-Team.
[919.30 → 923.12] And, you know, it's people with families, it's people who are single, it's people of
[923.12 → 924.20] various genders.
[924.32 → 925.82] I mean, it's so diverse.
[926.12 → 928.58] It's really a magical thing to be a part of every day.
[928.70 → 934.48] But it shows you that when you are surrounded by that kind of diversity and knowledge and
[934.48 → 938.00] people with so many different experiences, this is the kind of community that you get into
[938.00 → 940.02] and you have no other option but to grow.
[940.42 → 944.10] So as the CEO of X-Team, what is it that gets you up in the morning?
[944.20 → 945.06] What motivates you?
[945.06 → 950.74] My main motivation when I get up every day is to jump into the community and make connections
[950.74 → 955.22] with people and learn about them, learn about their stories and see how we can make their
[955.22 → 955.80] lives better.
[956.00 → 958.84] And that is one of the most rewarding jobs you can have.
[958.92 → 960.82] So I'm very happy to be a part of it.
[961.32 → 964.66] If you're looking to join one of the most energizing communities for developers out there, do more
[964.66 → 969.36] of what you love to get energized, to find where you belong and to grow, then head to
[969.36 → 971.04] X-Team.com to learn more.
[971.48 → 972.98] Again, X-Team.com.
[985.30 → 989.38] So for those of us who have never gone to a training session, you know, can you guys talk
[989.38 → 993.44] a little bit more about, you know, why like this year might be too late, obviously, but
[993.44 → 997.50] you know, in the future, why they should consider them versus, you know, like there's all these
[997.50 → 1000.96] different training options, you can hire people to come into your company and buy courses
[1000.96 → 1001.34] online.
[1001.44 → 1004.70] Like there's a million different options, but training sessions always seem to sell out
[1004.70 → 1006.60] pretty quickly, or they seem to do very well.
[1006.72 → 1010.52] So like what, what makes that in-person training session at like a gopher con or something like
[1010.52 → 1010.76] that?
[1011.20 → 1012.32] You know who would you pitch that to?
[1012.46 → 1013.32] Johnny, you can take that.
[1014.28 → 1014.62] Yeah.
[1014.66 → 1019.76] I mean, I think we both have, have opinions on that because we know we both teach and whatnot.
[1019.76 → 1024.90] So, um, sort of the real value for me in, in having a live sort of instructor, like in
[1024.90 → 1029.30] the room is really the ability, like, and when you get a perfect instructor, right?
[1029.34 → 1032.36] If you've ever been in a room with say like Bill Kennedy, right?
[1032.36 → 1036.22] Who's going to be teaching at the workshop or people like that, that really have a passion
[1036.22 → 1037.08] for teaching, right?
[1037.12 → 1040.54] They have a certain uncanny ability to read a room, right?
[1040.54 → 1044.72] And know where people are struggling to understand something, where they need to spend a bit more
[1044.72 → 1047.58] time, where maybe they need to slow down a little bit or speed up, right?
[1047.58 → 1051.18] So they have, they have an uncanny ability to sort of read people's faces in the room
[1051.18 → 1054.06] and sort of, you know, and sort of provide the best value, right?
[1054.08 → 1055.18] For the money you're paying, right?
[1055.50 → 1060.38] So to me, that's one of the biggest things you can get out of a out of a live sort of
[1060.38 → 1065.60] a person training, because the questions you get the chance to ask are perhaps things that
[1065.60 → 1067.58] you might not get from a video or from reading a book.
[1067.58 → 1072.12] And I can tell you in terms of pretty much my choice, my preference for training material.
[1072.12 → 1073.64] And I mean, I'm a developer.
[1073.76 → 1075.52] I learn like everybody else, even though I'm teaching, right?
[1075.54 → 1076.88] I learn by teaching.
[1076.88 → 1083.16] But for me, in terms of sort of the learning value, I think videos offer the best value
[1083.16 → 1084.46] over reading for me, right?
[1084.54 → 1089.00] I consume a ton of YouTube videos, training material and whatnot, because that offers me,
[1089.36 → 1090.66] I can speed up, I can slow down.
[1090.72 → 1093.78] I can do a lot of things that I can't do with a book or like written training material.
[1094.02 → 1098.62] But the next best thing, the very, at the top of that sort of hierarchy is the live person
[1098.62 → 1099.48] training, right?
[1099.52 → 1102.20] They're going to offer you, they're going to be able to answer your specific questions.
[1102.20 → 1104.76] They're going to be able to sort of navigate the room, right?
[1104.76 → 1107.64] And kind of deliver the value that most people are looking for.
[1108.04 → 1112.72] So the for a teacher, like, you know, I can speak for me and definitely Mark will have
[1112.72 → 1113.66] his own views on that too.
[1113.92 → 1116.60] Like I mentioned before that I learn by teaching.
[1116.82 → 1121.90] I enjoy the process of teaching because in preparation for, you know, delivering a course
[1121.90 → 1126.38] or training, like I get to find out about nooks and crannies of a particular piece of technology,
[1126.48 → 1126.62] right?
[1126.62 → 1130.20] So I get to like, helps me master my craft before I didn't have to go teach it, right?
[1130.20 → 1133.14] So if, you know, you've heard people say before, like, if you want to learn something
[1133.14 → 1135.32] really, really well, try and teach it to somebody else, right?
[1135.34 → 1138.06] This is, for me, this is sort of the height of that, right?
[1138.10 → 1140.30] And I enjoy the process, right?
[1140.30 → 1146.28] For me personally, the biggest sort of satisfaction I derive from teaching is actually seeing that
[1146.28 → 1146.98] moment, right?
[1147.02 → 1149.24] There's a particular moment and Mark will probably notice too.
[1149.28 → 1151.94] There's a particular moment where somebody like gets it, right?
[1152.08 → 1152.92] It's a fleeting moment.
[1153.04 → 1154.34] If you don't look, right?
[1154.38 → 1155.32] If you don't look, you'll miss it.
[1155.38 → 1156.12] If you'll miss it.
[1156.12 → 1159.14] But that moment when they get it, oh man, I live for that moment.
[1159.28 → 1163.16] I love when people like, some people bounce up and down in their seats and clap loudly.
[1163.28 → 1163.98] It's really great.
[1164.38 → 1164.62] Yep.
[1164.80 → 1165.00] Yep.
[1165.26 → 1165.46] Yeah.
[1165.46 → 1169.72] I have to echo everything Johnny just said, you know, and so I won't kind of go into that.
[1169.78 → 1173.14] But from the student's perspective, if, you know, you're going, you're already going
[1173.14 → 1176.14] to say a gopher con and spending a bit of money.
[1176.20 → 1178.76] Why would you want to spend an additional three or four or five?
[1178.80 → 1182.70] I don't know what the tickets are, but you know, every conference offers workshops.
[1182.82 → 1184.48] Most conferences do, and they're all different prices anyway.
[1184.48 → 1187.00] So why would you pay for the extra add-on?
[1187.08 → 1190.96] And I think Johnny is definitely correct when he says, you know, having a person there in
[1190.96 → 1193.68] front of you, like you can't beat that value.
[1193.74 → 1194.68] Like you can't beat that.
[1194.82 → 1198.70] That's hands down the best way is to interact with another human being.
[1199.04 → 1203.52] You know, and as somebody who runs a training company, that's what I do for a living, right?
[1203.52 → 1207.16] I go around, and I train developers all around the world with gopher guides.
[1207.40 → 1211.92] And, you know, we go into these corporate environments, and they pay a lot of money to
[1211.92 → 1215.26] bring trainers on site and to do that, right?
[1215.34 → 1217.34] I'm, you know, not, it's just what it is.
[1217.38 → 1219.26] That's just the way training and teaching work.
[1219.68 → 1221.28] Not every company can afford to do it.
[1221.52 → 1226.42] Not every company can bring in dedicated people for three days, fly them to their office and
[1226.42 → 1226.72] do it.
[1226.72 → 1231.84] Like that's kind of Fortune 500 level companies, right?
[1231.84 → 1234.90] You know, but your startups, you know, if you can get people to the conference, then
[1234.90 → 1241.56] that extra two, three or $400 add-on can actually be quite valuable and be really worth it where
[1241.56 → 1247.84] they can get the training for the three or four developers on their team at basically bargain
[1247.84 → 1248.48] rates.
[1248.68 → 1252.76] Because they really are, I mean, it's eight hours, but usually the conference workshops are pretty
[1252.76 → 1257.22] cheap in terms of, you know, the actual value you're getting per head, you know?
[1257.46 → 1259.92] So yeah, I, I always think it's a it's worth it.
[1259.94 → 1264.16] And there's every conference I've seen has wonderful instructors and, you know, I know
[1264.16 → 1265.58] gopher con does it and other ones.
[1265.58 → 1271.50] They, they, they find the people they think are the best people to teach the workshops, you
[1271.50 → 1271.74] know?
[1271.82 → 1277.68] And you got Johnny, you got people like Bill and me and Dave Chaney and Frances, Campos,
[1277.68 → 1283.34] and like just all of these awesome people teaching and, you know, Carolyn and Natalie
[1283.34 → 1285.28] and just, just all sorts of amazing people.
[1285.64 → 1290.38] So yeah, you're not gonna, you're not going to waste your money if you spend it on a workshop
[1290.38 → 1291.62] at gopher con, that's for sure.
[1292.06 → 1295.70] So, I mean, that, that all makes a lot of sense, especially like the startup scene, it
[1295.70 → 1296.76] definitely makes a ton of sense.
[1296.76 → 1300.66] Because I know the bigger companies, you know, like you said, it's easy for them to not easy,
[1300.72 → 1302.74] but they can afford the training a little bit more easily.
[1303.06 → 1306.50] But you know if you have a 10-man startup, it's really hard to justify the cost of bringing
[1306.50 → 1308.06] in trainers and that sort of stuff.
[1308.54 → 1312.88] So aside from like training sessions, so that I guess the first day is, you know, getting
[1312.88 → 1315.96] to go for con, what should people sort of expect that day?
[1316.08 → 1318.80] You know, when they're first getting there the first day, you know, what, what would you
[1318.80 → 1319.58] prep them with?
[1319.82 → 1321.32] Get there early for registration.
[1322.28 → 1325.08] Sometimes they do registration on the workshop day.
[1325.28 → 1330.78] And if they do that, you should absolutely try to get there and get your badge and all that
[1330.78 → 1332.74] sort of stuff as early as possible.
[1332.74 → 1337.68] And I can't stress that there are like 1800 people going to this conference.
[1338.00 → 1339.16] They all need badges.
[1339.34 → 1341.20] That's almost 2000 people need badges.
[1341.42 → 1347.08] So arrive really early or the day before if they have hours.
[1347.28 → 1348.56] I can't remember if they do or not.
[1348.78 → 1348.80] Yeah.
[1348.82 → 1351.72] Typically every year they do like the day before.
[1352.16 → 1352.22] Yeah.
[1352.38 → 1355.58] Well, because we're, a lot of us are already in the building anyway for the workshop.
[1355.66 → 1355.86] Exactly.
[1355.86 → 1356.76] So they will often do that.
[1356.82 → 1361.50] So if you, if you're in on the was it Wednesday, the workshop day, if you're around, come in
[1361.50 → 1362.68] and well, read your email.
[1362.76 → 1363.60] Don't, I don't want to get there.
[1365.86 → 1366.14] Yeah.
[1366.18 → 1370.24] And I'd say, I mean, I'd say honestly, in my experience, you kind of get in a groove
[1370.24 → 1371.00] of things.
[1371.18 → 1374.10] I like, I'd like end of day one, right?
[1374.18 → 1377.40] You, you kind of really know, okay, I know, I know what the routine is.
[1377.44 → 1379.62] I know, you know, when I'm supposed to be aware.
[1379.68 → 1382.54] I know how much time to allocate to actually get into the rooms and other rooms.
[1382.54 → 1385.08] Because I mean, you've got a lot of people, you know, bumping into each other and trying
[1385.08 → 1386.18] to get from one place to the other.
[1386.18 → 1389.80] So there's, you know, obviously there's some built-in time for, for, you know, the hallway
[1389.80 → 1390.62] track as we call it.
[1390.94 → 1394.60] But, you know, obviously you get a sense of, okay, this is, this is what it's going to take
[1394.60 → 1397.16] for me to sort of get through, right?
[1397.26 → 1399.14] The these, these few days, right?
[1399.52 → 1402.86] Because I mean, honestly, I mean, most of us are introverts, right?
[1402.90 → 1403.54] Most of us.
[1403.64 → 1407.76] So, and a few of us fall in the ambivert, I kind of fall in that ambivert category, but
[1407.76 → 1412.04] even then sort of the introvert part of me after I've basically spent an entire day talking
[1412.04 → 1414.52] to people, I just want to crawl into a hole somewhere.
[1414.68 → 1417.50] I mean, don't bother me for the next two hours because I need to recoup.
[1417.56 → 1417.74] Right.
[1417.98 → 1421.58] So you, and you kind of have to sort of pace yourself, right?
[1421.58 → 1425.90] If, if you fall in that category, you know, if you kind of have to sort of manage your energy
[1425.90 → 1426.84] level a little bit.
[1426.84 → 1430.60] And I think you really get a good sense of what that looks like, you know, towards the
[1430.60 → 1431.72] end of day one kind of thing.
[1431.72 → 1433.50] So definitely like pace yourself.
[1433.72 → 1434.90] It's hard to say, don't be overwhelmed.
[1434.90 → 1438.98] Cause that sometimes that's out of your control, but basically sort of take it in and strides
[1438.98 → 1442.92] a little bit and sort of, you know, give yourself permission to be overwhelmed, but then take
[1442.92 → 1443.46] a step back.
[1443.52 → 1447.78] And if you need to, you know, step outside the confidence venue to, you know, catch your
[1447.78 → 1449.68] breath or whatever it is, please do it.
[1449.68 → 1449.90] Right.
[1449.94 → 1453.94] I'd rather you get the most out of it, you know, keep your energy levels up and get the
[1453.94 → 1456.96] most out of the experience than, than sort of, you know, burning out cause you actually
[1456.96 → 1459.84] could burn out in those, like those two or three days if you're not careful.
[1460.40 → 1460.56] Oh yeah.
[1460.60 → 1461.08] It's tough.
[1461.20 → 1463.24] I, you know, again, agree with Johnny.
[1463.34 → 1468.38] I often go back to my hotel room in the afternoon, usually in the afternoon break for a couple of hours
[1468.38 → 1475.70] and just sit in the dark watching like something on Netflix for an hour, just like trying to
[1475.70 → 1481.70] like re-enter and refocus my energy again before I go back out and do it all over again.
[1481.82 → 1484.06] You know, uh, it's, it's, it's, it's a lot.
[1484.14 → 1484.28] Yeah.
[1484.44 → 1486.86] It takes, have you ever been to any conferences before Jamal?
[1486.88 → 1491.10] I have, but, uh, I'm completely new to the entire gopher community.
[1491.10 → 1496.54] So it's not my first conference, but I never thought I'd be attending a gopher con conference
[1496.54 → 1501.34] and maybe just to speak on the perspective of somebody who's like just coming into the
[1501.34 → 1504.94] community and seeing it, like all the hard work you guys have put in.
[1505.10 → 1510.60] But the first thing is like, I'm coming from a C++ background and C++ conferences are not
[1510.60 → 1514.40] as fun and there aren't as many opportunities, you know, like there's a there's almost a
[1514.40 → 1515.84] rigid stance on things.
[1515.84 → 1519.78] And it's, it's, it's very hard to kind of integrate and fall into that.
[1519.78 → 1524.84] I didn't even know there was a possibility of getting scholarships to come to gopher con
[1524.84 → 1526.48] like that, or even partial scholarships.
[1527.32 → 1533.68] But, uh, Carmen was the one who probably taught me the most, you know, like, uh, I, I did go
[1533.68 → 1538.52] as a hobby for a few years and just follow the community, read a lot of the stuff that
[1538.52 → 1539.26] you guys write.
[1539.58 → 1541.42] And like, it was my fun language, man.
[1541.44 → 1542.92] It was what I programmed in for fun.
[1543.06 → 1544.80] I wasn't what I did for a living.
[1544.80 → 1551.48] And I got on Twitter, and I was completely new, and it was a talk that Carmen made in
[1551.48 → 1556.80] 2017, the keynote speech at, uh, Gotham Go where it was the legacy of Go.
[1557.00 → 1557.36] Yeah.
[1557.36 → 1560.96] That one was the one that kind of, cause like, it's one thing to know how amazing a technology
[1560.96 → 1565.88] is, but until you know of the community or, you know, some people in there, you don't feel
[1565.88 → 1566.72] like you're a part of it.
[1566.72 → 1571.04] You're always on the exterior and never think that there's a pathway to get into it.
[1571.04 → 1573.38] But Carmen's talk really just was amazing.
[1573.38 → 1577.92] And I, I remember writing a comment under it, and it was like when it was first uploaded,
[1577.92 → 1580.30] like, thank you, Carmen, this is so important and et cetera.
[1580.58 → 1584.16] And then a year goes by, and I'm like, you know what, I'm going to see what's up when we
[1584.16 → 1584.68] get on Twitter.
[1584.94 → 1590.12] And one of the first people I connected with was Carmen, and she really made me feel welcome
[1590.12 → 1593.92] in the community and kind of gave me a perspective that I needed.
[1594.44 → 1597.08] And that is probably the reason why I'm still doing Go.
[1597.18 → 1600.44] So like, I actually have a job now where I was a Go developer, which I still don't believe
[1600.44 → 1604.38] like I get to use the language that I love and get paid for it.
[1604.46 → 1609.32] So it feels good to be like in the community and to be working in the community and to feel
[1609.32 → 1609.94] a part of it.
[1610.12 → 1612.34] And I didn't even know there's a diversity of scholarship.
[1612.46 → 1615.68] I didn't know if there were any scholarships at all, but like through Twitter and you guys
[1615.68 → 1617.52] retweeting and all that, I was like, what?
[1617.66 → 1618.78] Like I can apply?
[1618.94 → 1619.48] I'm like, sure.
[1619.60 → 1621.32] And it's been Christmas since, man.
[1621.34 → 1622.06] I'm excited to come.
[1622.06 → 1627.36] So as someone new coming into all of this, the one thing I keep seeing in this community
[1627.36 → 1633.00] is that like the more known someone is, or I guess the more famous they are within the
[1633.00 → 1634.42] community, the more accessible.
[1634.56 → 1636.92] It's like almost like an inverted pyramid, right?
[1636.94 → 1640.28] Like people you think that are inaccessible, you can't communicate with.
[1640.34 → 1643.86] Like I'll send them a DM and like I get a response back, and I'm not used to that.
[1644.00 → 1645.64] Like this person is pretty busy.
[1646.68 → 1649.92] You know, like I've talked to Bill a few times via Twitter.
[1650.04 → 1650.80] He's been amazing.
[1650.80 → 1652.00] Brian's been amazing.
[1652.36 → 1656.54] You know, it's just been a lot of amazing people who just have answered really silly
[1656.54 → 1660.34] questions, you know, and I've been allowed to ask them, and it's been amazing.
[1660.34 → 1661.52] So I appreciate that.
[1661.76 → 1662.72] But I'm excited.
[1662.88 → 1663.40] I'm excited.
[1663.58 → 1667.38] And there are probably a lot of other questions I have, you know, like one of the things I
[1667.38 → 1670.30] guess was like, man, I thought I was going to, I forgot that it's going to be recorded.
[1670.40 → 1671.58] You know, it's like now I'm attending it.
[1671.60 → 1674.62] I'm like, man, if I miss it, if I don't pick it up, like it's different.
[1674.66 → 1676.28] But then I forget it's going to be uploaded.
[1676.48 → 1676.62] What?
[1676.92 → 1677.78] Two weeks later.
[1677.88 → 1680.10] And it's not the end of the world.
[1680.10 → 1680.28] Yeah.
[1680.28 → 1680.64] Something like that.
[1680.70 → 1680.88] Yeah.
[1681.02 → 1684.40] So let me ask you, are you going to, are you going to be around on the last day, the
[1684.40 → 1685.06] community day?
[1685.18 → 1685.80] I am.
[1686.10 → 1689.20] I have not signed up for any workshops yet.
[1689.34 → 1691.02] So I got a partial scholarship.
[1691.34 → 1694.80] So I'm still thinking about like the benefits of attending.
[1694.90 → 1699.54] I know there are benefits, but cost benefit, cost for the ticket to attend and all that.
[1699.78 → 1699.80] But.
[1699.80 → 1702.48] Well, the last day is called community day.
[1703.02 → 1705.54] And that's not, that's part of the conference.
[1705.62 → 1706.02] Ah.
[1706.38 → 1710.08] And there's no, it's not where Bill happens to have an extra workshop that day, but that's
[1710.08 → 1710.74] an exception.
[1710.74 → 1713.86] So community day has a lot going on.
[1713.86 → 1719.00] I can talk about a few bits of it, but I actually get shanghaied.
[1719.08 → 1721.16] I don't get to actually see much of community day.
[1721.16 → 1723.70] Um, so I run the lightning talks every year.
[1724.10 → 1725.52] Um, and those are on community day.
[1725.52 → 1730.30] And we have about three dozen talks throughout the day, seven minutes of talk.
[1730.30 → 1731.84] So you can imagine three dozen speakers.
[1732.04 → 1733.56] It's quite the, uh, quite the event.
[1733.72 → 1738.92] And they also all get professionally recorded just like full stage conference talks.
[1738.96 → 1740.92] And those are also up a few weeks later.
[1741.26 → 1742.64] So that's an all day thing.
[1742.66 → 1744.28] And there's some really amazing talks this year.
[1744.30 → 1746.52] And I always recommend, uh, the lightning talks.
[1746.58 → 1749.06] What's awesome about them is people go from there to the main stage.
[1749.06 → 1750.84] Like, and it's just really nice to see that.
[1751.10 → 1752.46] It really is a mini conference.
[1752.46 → 1755.30] Um, so I obviously would recommend checking that out.
[1755.30 → 1759.90] Uh, Ron Evans does a hardware hack thing all day.
[1759.90 → 1764.44] Like, so if you don't see Ron at the conference, that's because he's probably in a room somewhere
[1764.44 → 1767.56] assembling Mark Bates, killing drones of some sort.
[1768.90 → 1769.72] It's true.
[1770.72 → 1775.16] But he spends the whole day doing, he gets like, you know, companies like Intel and whatever,
[1775.26 → 1779.98] give him all sorts of hardware to bring with them, you know, processors and all sorts of
[1779.98 → 1780.18] stuff.
[1780.22 → 1783.46] And he spends all day teaching people how to program hardware.
[1783.68 → 1787.32] He gives out tons of hardware to everybody who attends.
[1787.32 → 1792.94] I've never met anybody who said they had a bad time at Ron's hardware hack fest.
[1793.08 → 1794.64] I don't think it's possible either.
[1794.82 → 1797.38] And he's just, he's just, he's just a hoot.
[1798.12 → 1799.10] He really is.
[1799.18 → 1801.12] He's, he is an awesome human being.
[1801.20 → 1803.88] Uh, and then I guess I only learned about this on Monday.
[1804.38 → 1808.82] Um, but I guess there's a, a table, like a round table hack area.
[1808.82 → 1813.74] And they're going to have 56 round tables set up with kind of sign up.
[1813.82 → 1818.02] So you can go and either sign up and say, I'm going to run a little table on my project,
[1818.26 → 1821.30] you know, or I'm going to run a table where I want to, I'm going to teach people how to
[1821.30 → 1822.40] use Go modules, right.
[1822.44 → 1822.92] And drink.
[1823.26 → 1824.32] Um, I'm just kidding.
[1825.48 → 1825.80] Right.
[1825.88 → 1827.42] We'll have like a little table, you know, whatever.
[1827.66 → 1831.96] Um, or you can, you can come in and be like, oh, there's a table on, you know, Go modules.
[1832.02 → 1833.72] Let me go and find out more about that.
[1833.74 → 1835.62] And you can kind of sit down and kind of join that group.
[1835.62 → 1838.40] So that also happens on the community day, I guess.
[1838.78 → 1841.48] Um, Johnny, what else happens on community day?
[1841.70 → 1845.70] It's also worth noting that a lot of people who actually work on Go itself, the language
[1845.70 → 1846.70] itself are going to be there.
[1846.70 → 1846.90] Right.
[1846.92 → 1850.60] So this is an opportunity to sort of talk to them and ask them some sort of, some of
[1850.60 → 1851.90] the behind the scenes, right.
[1851.98 → 1853.64] Um, sort of discussions that goes on.
[1853.68 → 1856.24] I mean, they may not be able to tell you a lot, but you know, you will get some
[1856.24 → 1861.12] insight into sort of, uh, the, the process of, of sort of, um, deciding, right.
[1861.16 → 1863.00] Uh, from somebody who's on the team, right.
[1863.00 → 1865.24] Of, of what makes it in, how do they make decisions, that kind of thing.
[1865.24 → 1868.24] So if this is something that's interesting to you, if you're a language geek and this
[1868.24 → 1871.52] is something that's interesting to you, this is a perfect opportunity to sort of, uh, get
[1871.52 → 1872.70] to meet these people and talk to them.
[1872.94 → 1877.98] There's, there are opportunities for, to contribute to, to, um, last year there was, uh, actually
[1877.98 → 1880.96] a workshop for actually getting you to commit, right.
[1880.96 → 1883.00] Something to the Go project itself.
[1883.00 → 1883.22] Right.
[1883.22 → 1886.78] So if you wanted to be a Go contributor, this would be the perfect way of actually, you
[1886.78 → 1889.56] know, um, going through the process of, you know, setting up, getting everything ready
[1889.56 → 1890.32] to go kind of thing.
[1890.32 → 1892.44] And then basically being able to sort of commit something.
[1892.44 → 1895.68] And we actually had somebody from the core team approving PRs, right.
[1895.74 → 1898.72] Brad Fitzpatrick was one of the people like approving PRs, right.
[1898.76 → 1899.68] You approve one of my PRs.
[1899.72 → 1902.16] I'm like, what, you know, I'm, so I was ecstatic.
[1902.30 → 1905.88] So, you know, things like that, you know, basically, again, making the community more approachable
[1905.88 → 1907.48] and not, are they doing that again next year?
[1907.60 → 1908.60] I don't know if they are.
[1908.82 → 1910.08] It's listed on the agenda.
[1910.26 → 1910.54] Is it?
[1910.72 → 1912.18] Oh, we should probably look at the agenda.
[1912.18 → 1916.64] We probably think we already know it all.
[1916.82 → 1916.92] Yeah.
[1917.16 → 1917.42] Yeah.
[1917.42 → 1917.62] Right.
[1917.90 → 1918.06] Yeah.
[1918.12 → 1921.46] So it says from a 10 AM to 12 PM, they're doing the contributor workshop.
[1921.74 → 1922.02] Okay.
[1922.34 → 1926.16] And then later on in the days when they're doing the like sort of fireside chat slash
[1926.16 → 1929.96] panel where they take questions and talk to the community about Go and that sort of stuff.
[1930.04 → 1930.22] Right.
[1930.40 → 1930.76] Okay.
[1930.96 → 1931.12] Yeah.
[1931.16 → 1931.46] Yeah.
[1931.56 → 1932.08] Let's definitely look at that.
[1932.14 → 1933.16] These are the awesome opportunities.
[1933.28 → 1933.42] Yeah.
[1933.52 → 1938.70] And again, Jamal, what you're saying, the, the, I can't sort of thank you enough for actually
[1938.70 → 1942.06] saying that on air, because this is something that I think the Go community goes out
[1942.06 → 1943.14] of its way, right.
[1943.20 → 1945.56] To, to actually do, to be approachable, right.
[1945.56 → 1950.36] To be welcoming, to, to, to say, Hey, like we know you're a newbie, you know, on the outside
[1950.36 → 1954.52] looking in perhaps, and you're wondering, okay, well, when's a good time to, to come
[1954.52 → 1957.88] in when, you know, when should I try, you know, maybe you've been sort of lurking a little
[1957.88 → 1961.32] bit and, and, and sort of wondering, okay, well, like, am I going to have an opportunity?
[1961.40 → 1964.90] Like, when's my chance to sort of make a connection and sort of join the community to be part
[1964.90 → 1965.30] of the community.
[1965.30 → 1965.56] Right.
[1965.60 → 1969.88] Like this is, you know, we go out of our way as a community to make you feel welcome.
[1969.88 → 1970.20] Right.
[1970.20 → 1972.32] We welcome newcomers, we welcome newbies.
[1972.70 → 1976.90] So this is, this is something that I think everybody needs to hear that the Go community,
[1976.90 → 1977.24] right.
[1977.24 → 1979.42] Is a safe place for beginners, it's a safe place for newbies.
[1979.62 → 1981.16] If you, if you don't know Go, right.
[1981.16 → 1984.18] You're going to hang out with gophers and, and start to pick up, right.
[1984.18 → 1987.70] Some, some knowledge, some tidbits, you know, about what it's like to do Go, what it looks
[1987.70 → 1988.80] like to be part of this community.
[1989.08 → 1991.24] Like it's, this is not just about the language.
[1991.24 → 1993.20] This is not just about the technology.
[1993.20 → 1997.02] I mean, if you, if that was it, then you could go do any other tech you want.
[1997.02 → 2000.28] I mean, it's the, the community plays a central role, right.
[2000.28 → 2002.72] And the language and, and it's life.
[2002.72 → 2002.98] Right.
[2002.98 → 2006.76] So we, we value community tremendously here.
[2006.76 → 2010.88] So please, like if, if, you know, if you're like Jamal, and you're thinking, Hey, like how,
[2011.24 → 2012.18] like, when's my opening?
[2012.18 → 2012.96] You don't need an opening.
[2013.02 → 2014.40] Just, just go meet somebody.
[2014.40 → 2014.72] Right.
[2015.44 → 2016.00] Trust me.
[2016.00 → 2017.30] Like you go and say hi.
[2017.30 → 2018.14] And then that's it.
[2018.22 → 2019.50] That's, that's really all you need to do.
[2019.50 → 2020.40] Just go and say hi.
[2021.14 → 2021.36] Yeah.
[2021.36 → 2022.66] And most of us have stickers.
[2023.46 → 2028.16] What really blew my mind was when I first got on Twitter, I was reading some blog posts
[2028.16 → 2029.32] and some books and all that.
[2029.38 → 2032.16] And I kept on seeing Brad's name just come up.
[2032.16 → 2032.42] Right.
[2032.80 → 2035.12] Thank you, Brad, for all the help, blah, blah, blah, blah.
[2035.18 → 2036.10] I was like, who's this guy?
[2036.14 → 2037.30] And I looked him up, found him on Twitter.
[2037.38 → 2040.60] I was like, and I think I sent him a message like three in the morning.
[2040.60 → 2040.84] Right.
[2040.84 → 2043.80] Like, Hey, I saw that you keep needing to mention all these books.
[2043.80 → 2045.40] Thanks for what you've done for the Go community.
[2045.40 → 2045.76] Right.
[2045.76 → 2050.64] And then like two seconds later, he, he sent me a few sentences back, you know, like blew
[2050.64 → 2052.74] my mind that he was awake that time.
[2052.94 → 2054.06] And he replied.
[2054.90 → 2057.46] He's got like two very small children.
[2057.52 → 2057.76] Yeah.
[2057.88 → 2060.52] So he's probably up anywhere.
[2061.30 → 2065.58] But you know, first time when I first met Brad was the very first Gopher Con.
[2065.78 → 2069.24] I was taking a taxi from the airport to the hotel.
[2069.40 → 2073.16] And while I was waiting for the taxi at the airport, I was talking to another guy up and
[2073.16 → 2074.48] we were in like an HTML shirt.
[2074.48 → 2075.68] We started chatting.
[2075.80 → 2076.88] We realized we were going to the conference.
[2076.88 → 2080.46] So we shared a cab, and we're like, we're in the cab, and he's saying, you know, like,
[2080.54 → 2081.58] so, you know, do you use Go?
[2081.68 → 2084.20] I said, well, a little bit, you know, here and there, whatever, you know.
[2084.24 → 2085.12] And what about you?
[2085.22 → 2086.34] He goes, yeah, I use it daily.
[2086.46 → 2087.16] Oh, okay.
[2087.32 → 2088.88] And anyway, we were talking.
[2088.96 → 2089.36] So what's your name?
[2089.44 → 2090.06] Oh, Brad, whatever.
[2090.36 → 2091.22] And we keep talking.
[2091.22 → 2093.00] Then later on, we were still talking, whatever.
[2093.22 → 2095.10] And I said, you know, so where do you work?
[2095.12 → 2095.60] He goes, Google.
[2096.16 → 2097.44] Are you Brad Fitzpatrick?
[2097.56 → 2097.78] Yeah.
[2100.16 → 2104.24] So I spent like 30 minutes in a car with him, like asking him if he writes Go,
[2104.24 → 2104.70] two.
[2106.50 → 2107.76] What's your favourite part?
[2109.12 → 2110.24] But he's super cool.
[2110.32 → 2111.26] He's such a great guy.
[2111.64 → 2112.24] They all are.
[2112.50 → 2113.74] Everybody really is very nice.
[2113.84 → 2114.40] Johnny does.
[2114.58 → 2114.72] Right.
[2114.76 → 2117.88] I think this is a community that rewards nice people.
[2117.88 → 2122.38] I think it also says a lot that pretty much the entire Go team is at Go4Con, or it feels
[2122.38 → 2126.30] like the entire Go team is there and like they want to get feedback from people.
[2126.68 → 2129.74] And, you know, you hear people say like, oh, Go is Google's language or something like
[2129.74 → 2129.96] that.
[2130.16 → 2131.08] They don't have to be there.
[2131.14 → 2134.10] They don't have to go out of their way to be accessible and, you know, to make all that
[2134.10 → 2134.40] happen.
[2134.44 → 2135.02] But they do.
[2135.46 → 2139.56] And I think that speaks volumes as to why the language itself is as open as it is and
[2139.56 → 2142.44] inclusive and everything is that they're sort of setting that example.
[2142.44 → 2146.98] Yeah, there will definitely be a lot of people in looking at the Go team community room on
[2146.98 → 2147.76] the last day.
[2148.20 → 2152.04] Like I said, there is a contributor workshop from 10 to 12 where you can learn how to contribute
[2152.04 → 2153.24] to Go directly.
[2153.74 → 2159.14] And then at 1.30 to 3, there's Growing Go, which is kind of like a fireside chat panel
[2159.14 → 2161.66] with the Go leadership and team and then kind of closing.
[2161.76 → 2165.24] So it looks like there's a whole day when you can hang out with the team, talk to the
[2165.24 → 2166.28] team, get to know them.
[2166.28 → 2171.44] Again, like Johnny said, most of the team is going to be there, plus a large contingent
[2171.44 → 2174.18] of community contributors to go as well.
[2174.40 → 2178.04] So there's usually a contributor summit that happens at the conference as well.
[2178.24 → 2183.80] So there will be a lot of both core team and contributors just wandering the halls all
[2183.80 → 2184.32] week.
[2184.82 → 2187.38] And you can absolutely chat to any of them.
[2187.64 → 2188.90] They will love to chat with you.
[2189.32 → 2191.02] I'm just volunteering everybody.
[2191.02 → 2196.40] I will definitely go to that day and bug everybody and introduce myself again.
[2196.80 → 2196.90] Yes.
[2196.98 → 2200.04] And you should absolutely, if everybody's listening, they should absolutely introduce
[2200.04 → 2201.58] themselves to Matt Refer as well.
[2201.86 → 2202.06] Yes.
[2202.08 → 2206.78] You absolutely have to meet Matt Refer and meet him like daily because he has, I found
[2206.78 → 2211.24] at conferences, especially like Denver, California, he tends to forget things sometimes.
[2211.24 → 2215.52] So let's just hammer Matt with hellos the entire time.
[2217.22 → 2218.52] He's going to thank you for this, Mark.
[2218.72 → 2219.50] Yeah, I know, right?
[2219.50 → 2222.50] It's also Tim Raymond's birthday next week while we're out there.
[2222.62 → 2223.66] So everybody say hi to him.
[2224.00 → 2224.44] Nice.
[2224.66 → 2225.06] Nice.
[2225.16 → 2226.04] Looking forward to seeing Tim.
[2236.04 → 2238.86] This episode is brought to you by Strong DM.
[2239.20 → 2245.38] Manage and secure remote access to any database, any server, on-prem or in the cloud, and environments.
[2245.38 → 2251.06] They make it easy for DevOps teams to enforce the security and controls Infosec teams require.
[2251.54 → 2254.20] So if your engineers need access, you need Strong DM.
[2254.56 → 2256.32] So what can Strong DM do for your team?
[2256.64 → 2258.40] First off, more control, less hassle.
[2258.88 → 2262.70] Grant or revoke access to any database or server in one command.
[2263.12 → 2267.44] Use your SSO to manage access to every database, every server and environment.
[2267.44 → 2269.32] Second, total visibility.
[2269.78 → 2278.38] Strong DM upgrades your audit logs, log every permission change, every query, every SSH, and every RDP command and know who issued those changes.
[2278.88 → 2285.54] And of course, faster Stock 2 compliance, easily enforce access controls, and instantly answer auditors' questions.
[2286.04 → 2290.06] Head to strongdm.com slash go time to learn more and request a free demo.
[2290.40 → 2292.92] Again, strongdm.com slash go time.
[2297.44 → 2309.12] So you were talking about Community Day with the Lightning Talks.
[2309.32 → 2317.00] I guess for anybody who's unfamiliar, can you sort of tell them what's the difference between regular talks, Lightning Talks, like why they should care about one over the other?
[2317.72 → 2318.56] Oh, that's an interesting...
[2318.56 → 2319.68] Not necessarily over the other, but you know.
[2320.22 → 2324.68] Well, thankfully, we don't have any sort of collision in terms of that.
[2324.68 → 2330.12] But so it really is why would you come to the Lightning Talks and not go to a play with hardware with Ron, right?
[2330.24 → 2334.50] Like, that's the thing I'm always competing against, right?
[2335.10 → 2335.72] That's fun.
[2335.84 → 2339.36] So the Lightning Talks, like, again, for those of you who don't know it, they're seven minutes long.
[2339.86 → 2343.82] We have, like I said, between 30 and, you know, three dozen speakers.
[2344.24 → 2347.84] The variety of people talking is just insane.
[2347.98 → 2350.52] And they cover all these different topics.
[2350.52 → 2351.98] And they're fun.
[2352.10 → 2354.30] A lot of times they're fun and sometimes they're silly.
[2354.64 → 2360.78] You know, for example, one year Sharon Alsop gave a talk on roasting her own coffee beans.
[2361.02 → 2361.68] It was really fun.
[2361.88 → 2370.16] One year someone did a talk about a dead man switch using their iPod or their iPhone as a dead man switch on their computer.
[2370.34 → 2376.74] And they hacked it all, and they did it all and go and like 659, right before I pulled him off the stage, he yanked the cord.
[2376.74 → 2380.16] And the whole screen went dead and, like, that was the end of his demo and it was awesome.
[2381.10 → 2382.98] So there's all these great things that happen.
[2383.24 → 2385.74] You usually get, like, Rama Rao.
[2386.52 → 2387.64] I'm sorry, Rama.
[2388.34 → 2391.72] She writes the Go plugin for VS Code.
[2391.94 → 2393.70] She usually gives a Lightning Talk every year.
[2393.76 → 2395.24] She's giving one this year, kind of, you know.
[2395.32 → 2399.12] And so that's always a great place to hear what's upcoming for things like VS Code.
[2399.12 → 2404.34] I know Florin from JetBrains who works on Poland IDE.
[2404.62 → 2406.38] He's also giving a talk.
[2406.52 → 2412.88] Like, so there's all these just fascinating talks from people from all around the world with all just interesting perspectives.
[2413.02 → 2415.48] And some of them are, hey, I wrote this cool thing.
[2415.76 → 2416.84] I just want to show it.
[2417.46 → 2419.86] Some are, you know, this is my company.
[2420.40 → 2421.36] I just want to show it.
[2421.80 → 2423.12] Those are a little less interesting.
[2423.12 → 2432.26] And then some are just, like, I found this weird issue, this weird bug, this hack, like, watch me do something terrible with Go that you should never do, right?
[2432.32 → 2433.90] So there's always fun stuff there.
[2433.98 → 2435.22] And it's just a fun day.
[2435.26 → 2441.20] And if you don't like the talk, there's a great chance that seven minutes later you might like the next one, right?
[2441.26 → 2447.60] So you're not sitting there for 45 minutes or a half hour just being like, oh, my God, will this person stop talking?
[2447.72 → 2449.42] You're there for, like, six or seven minutes.
[2450.08 → 2452.24] So, you know, they're not all winners.
[2452.24 → 2453.68] They can't be statistically.
[2455.04 → 2459.60] But there's plenty of diversity and interest there, I think, for everybody who wants to attend.
[2460.30 → 2462.64] And seven minutes is a very short amount of time.
[2462.94 → 2463.90] It really is.
[2463.90 → 2464.84] I did one last year.
[2465.02 → 2468.06] And boy, I didn't see the time coming.
[2468.54 → 2470.12] It was, but it was fun, though.
[2470.14 → 2470.68] It was really fun.
[2470.92 → 2471.60] Most people don't.
[2471.74 → 2471.84] Yeah.
[2473.56 → 2474.46] That's always weird.
[2474.50 → 2480.26] We're like in high school when you have to talk about a subject you don't care about, filling three minutes is, like, awful.
[2480.26 → 2482.52] And then, like, you get to talk about something you care about.
[2482.60 → 2483.92] And you're like, wait, seven minutes are up?
[2484.00 → 2485.14] Like, I need way more time.
[2485.36 → 2486.24] Yeah, it's true.
[2486.40 → 2486.76] It's true.
[2486.84 → 2489.44] So the lightning, like I said, I absolutely love the lightning talks.
[2489.54 → 2491.52] I wouldn't keep running them every year if I didn't.
[2492.46 → 2494.76] We just get some really great people come through.
[2494.86 → 2496.92] And like I said, it's lovely to see them start.
[2496.92 → 2502.70] A lot of people start on that stage now and are migrating to the bigger stages in the main conference.
[2503.06 → 2504.46] And that's just awesome to see.
[2504.86 → 2506.04] And I love that we get to do that.
[2506.08 → 2513.00] So if you want to see the next Brad Fitzpatrick or the next Johnny or the next Carmen, the lightning talks may be for you.
[2514.72 → 2515.96] How's that sales pitch?
[2516.30 → 2517.02] Very nice.
[2517.18 → 2524.28] Actually, Heather Sullivan, you know, the person we've been referencing as being sort of the primary organizer for the conference.
[2524.28 → 2524.92] She's pretty awesome.
[2525.22 → 2532.94] She's mentioned that there'll be whiteboards, right, throughout, basically spread throughout the community day, right, around the tables, at the edges and whatnot.
[2533.34 → 2535.04] That roundtable section we were talking about.
[2535.04 → 2535.54] Right, exactly.
[2535.90 → 2536.06] Yeah.
[2536.12 → 2542.30] So if you've got a topic that you want to go up there and put on the board, you can find other people who are also interested in that.
[2542.68 → 2547.66] And you can sit at a roundtable or two, right, and hack on whatever that thing is together, right?
[2547.66 → 2551.74] So it's a way of identifying your tribe, if you will, right?
[2551.74 → 2554.38] Say, hey, yeah, I'm into, you know, dependency management.
[2554.52 → 2556.78] Maybe you go, you know, to the modules table, right?
[2556.78 → 2557.42] Because who isn't?
[2557.54 → 2558.34] Who isn't, right?
[2559.66 → 2561.44] Who wouldn't want to hang out there all day?
[2562.76 → 2563.08] Right.
[2563.20 → 2564.86] So it's tons of opportunities for that stuff.
[2565.00 → 2570.76] I'd also probably mention that even if you don't, like, if you feel like your skills aren't up to snuff or whatever, like, don't worry about that.
[2570.86 → 2572.98] You can learn so much just by sitting with other people.
[2572.98 → 2578.20] And, like, I've been fascinated by, like, you know, people who feel like they aren't very good at Go.
[2578.28 → 2579.26] I've learned things from them.
[2579.74 → 2582.90] Stuff like that happens all the time when you just see other people's approaches.
[2583.22 → 2587.76] So don't worry about, you know, being an imposter or something crazy like that.
[2587.82 → 2589.06] Like, people are all very welcoming.
[2589.20 → 2590.02] Just have a good time.
[2590.86 → 2593.16] At least I feel like the Go community has always been that way.
[2593.42 → 2594.34] They absolutely are.
[2594.48 → 2596.68] That's why I love going to these things.
[2597.34 → 2598.72] I don't know at all.
[2599.30 → 2600.22] None of us do.
[2600.22 → 2609.42] So, like, I have fun about packages and libraries and tools and just, like, endless, you know, just I don't have a CS degree.
[2609.56 → 2619.60] So whenever I'm in big brain land with all these CS people, like, I just try to suck in as much as I possibly can from them and just, you know, learn what I don't know.
[2619.80 → 2621.90] We all have our areas of specialty.
[2622.38 → 2624.54] You know, Jamal, I'm sure you could tell us some stuff.
[2624.60 → 2627.26] For example, I have never done C++ a day in my life.
[2627.70 → 2628.88] I would be all thumbs.
[2628.88 → 2631.32] Couldn't even tell you how to compile it, right?
[2631.46 → 2639.24] So just because you're, you know, a newbie in Go doesn't mean you don't have anything to offer anybody else, right?
[2639.30 → 2641.88] And that's not obviously just for you, Jamal, but that's for everybody, right?
[2641.96 → 2649.20] Like, just because you're new to the conference or the community doesn't mean you're not useful or welcome or have knowledge to offer.
[2649.70 → 2653.80] Thankfully, the lightning talks, like I said, are a great way of helping people show that they can do that.
[2653.80 → 2658.82] But you should know that you can and know that not all of us, no one does, right?
[2658.88 → 2663.40] But even those of us have been there since day one of the conferences, for example, we don't know.
[2663.66 → 2665.50] I, you know, ask me how the garbage collector works.
[2665.56 → 2666.00] I have no idea.
[2666.00 → 2669.36] Yeah, we value, we value outside perspective.
[2670.02 → 2673.86] You know, it's like personally, I enjoy hearing about those stories.
[2673.94 → 2680.22] People who are coming to Go, usually like if sometimes they're coming to programming in general and Go happens to be their first language.
[2680.58 → 2684.60] Absolutely love these people because I really get to sort of shape and mould them, if you will.
[2684.60 → 2689.94] But, you know, you have people who are sort of coming from other programming languages, right?
[2689.98 → 2693.12] So they bring their own ideas and how they're used to dealing with certain things.
[2693.72 → 2696.94] And sometimes it's so you kind of engage a little debate with them.
[2697.04 → 2698.24] Well, I'm used to doing things that way.
[2698.34 → 2702.00] Well, this is why we don't do this very thing that way, you know, and Go kind of thing.
[2702.06 → 2705.86] So you get a chance to sort of get some outside perspective, right?
[2705.90 → 2709.46] And a lot of times, you know, we're like, hey, you know what, that would be kind of cool and Go, right?
[2709.46 → 2715.12] So and this kind of conversations actually do end up sort of bubbling up into, you know, possible proposals, right?
[2715.12 → 2719.50] That the Go core team sort of ends up evaluating and deciding whether that's something they should consider or not.
[2719.82 → 2721.72] I mean, generics is a prime example of that, right?
[2721.78 → 2725.18] So, you know, a lot of people were saying, hey, we need generics in Go, we need generics in Go, right?
[2725.26 → 2726.78] And a lot of people made a case for it.
[2727.06 → 2728.46] And it's something that's being evaluated, right?
[2728.50 → 2736.92] So, again, Missy, the perspective that somebody's going to bring that is from outside the Go community, right, is tremendously valued.
[2737.26 → 2737.68] And it's welcome.
[2737.68 → 2742.34] So even, like, I've come to learn that most of my development is done by myself.
[2742.74 → 2746.10] And as a result, like, the type of development I do is very different.
[2746.10 → 2750.66] Or, like, what works in my code doesn't necessarily work in a company that has, you know, a thousand engineers.
[2750.92 → 2752.20] Like, it's vastly different.
[2752.32 → 2756.30] So just getting that perspective and seeing how they do stuff and learning from them and vice versa.
[2756.38 → 2759.50] They might say, like, oh, you know, you can prototype stuff way quicker than me.
[2759.56 → 2761.96] Let me see how you're doing that and learn some stuff there.
[2762.20 → 2766.02] So just, you know, knowing that everybody comes from a different background, and that's a good thing.
[2766.02 → 2768.60] And, like, conferences are an awesome spot to learn all that stuff.
[2769.14 → 2769.52] Agreed.
[2769.62 → 2772.46] So I don't know if we ever mentioned this, but the scholarships, I guess.
[2772.66 → 2774.00] It's a little bit too late for this year.
[2774.10 → 2779.80] But I do think that's something worth mentioning for the future is that, you know, Gopher Con does offer scholarships.
[2779.80 → 2786.12] So, you know, if you're considering going and, you know, for some reason it's not something you can do, definitely check that out.
[2786.32 → 2789.12] Get in touch and, you know, ask about it.
[2789.12 → 2792.16] Because the goal of the conferences isn't to exclude people.
[2792.24 → 2794.26] It's to, you know, get anybody and everybody there.
[2794.64 → 2799.08] And Heather, last week, she had a story that I don't think got recorded, unfortunately.
[2799.08 → 2803.46] But we got to talk about how there were some people that, like, literally went to a Go conference.
[2803.46 → 2807.46] And, like, now they're, you know, it made a huge difference in their career and in their life.
[2807.92 → 2809.96] And, you know, that's what we're looking for.
[2810.04 → 2811.08] I think that's what they're looking to.
[2811.14 → 2813.18] I guess I'm not technically doing that because I'm not there.
[2813.24 → 2818.52] But, you know, like, it's one of those really positive things that I think a lot of people just see conference and think, I can't go.
[2818.60 → 2820.36] I don't have the money, or I don't have the means to make it there.
[2820.42 → 2822.30] And that shouldn't be what holds you back.
[2822.30 → 2829.24] Yeah, I mean, you can really, you could look at going to a conference and hopefully, you know, an employer pays for you to be there.
[2829.48 → 2836.80] And if you have any other ways of actually getting there, and you're privileged enough to actually be in that room, I highly encourage it.
[2836.82 → 2840.72] Because consider it as an investment, right, in your own career, in your own future.
[2841.04 → 2843.64] You know, I remember going to my very first Gopher Con.
[2843.78 → 2846.14] Actually, you know, Mark was right there sitting next to me.
[2846.14 → 2852.74] And we were like, you know, look up on stage and seeing Bill, amongst a bunch of others, like, you know, well-known speakers do their thing.
[2852.98 → 2856.66] So we were like, hey, this is this go thing is is is for us.
[2856.72 → 2859.10] Like we enjoy the language.
[2859.28 → 2861.32] It's, you know, seems like the community is growing around it.
[2861.36 → 2864.42] So right then and there, we decided, hey, this was worth time.
[2864.42 → 2866.84] Right. And investing energy into it.
[2867.08 → 2868.64] So, you know, fast-forward a few years later.
[2869.00 → 2870.34] I mean, pretty much that's what we do now.
[2870.40 → 2873.30] We do go full-time, and we are part of the go community.
[2873.30 → 2878.20] And, you know, a lot of us basically have businesses that have sprouted out of being involved in a go community.
[2878.42 → 2882.12] I mean, it's really an investment in, you know, possibly in your future.
[2882.70 → 2889.32] So this is why I say, hey, like when you go to the conference, right, don't forget to actually network.
[2889.48 → 2891.26] This is you're not just going for the content.
[2891.38 → 2892.88] You're going to watch the content later anyway.
[2892.88 → 2895.98] Right. So don't forget to actually network.
[2896.10 → 2897.16] We'll get to know people.
[2897.42 → 2897.90] Right. Yeah.
[2899.26 → 2902.14] Yeah. I mean, there were all sorts of like we talked about earlier.
[2902.14 → 2908.16] There are all sorts of events for that kind of built-in, like the welcome party and community day and all sorts of other stuff.
[2908.20 → 2910.74] But there are other events as well, aren't there, Johnny?
[2911.06 → 2911.34] Yes.
[2911.76 → 2917.80] They're actually one of my favourites that's actually going to happen this year is the Go Bridge reception.
[2918.04 → 2921.54] I think that's happening on Thursday, Thursday night, Thursday evening.
[2921.54 → 2936.14] So if you are a person who is considered underrepresented in the Go community and or have helped put together a Go Bridge event or workshop or scholarship of some kind, we absolutely encourage you to come and participate.
[2936.14 → 2949.56] This is sort of our way of saying, hey, we're part of this sort of subgroup, if you will, like within the Go community that basically cares deeply about diversity and inclusion and really making it well, making the Go community welcome for people from underrepresented groups.
[2949.56 → 2953.42] Like we would love to get together and sort of and talk shop.
[2953.52 → 2955.60] Right. Talk about this is the impact we're having.
[2955.68 → 2956.62] This is how we can make things better.
[2957.10 → 2958.92] Ideas come out and come out of such events.
[2959.06 → 2960.56] So absolutely encourage folks.
[2961.14 → 2969.78] Basically, even if you if you like never heard of Go Bridge and want to understand what it is and what it's about, and you think you can help.
[2970.06 → 2971.44] We absolutely would love to have you.
[2971.44 → 2974.80] So it's absolutely something that I had highly recommended.
[2974.96 → 2988.18] Yeah. And there if you're looking for ways to help with the scholarship fund as well at the conference themselves, go for con and kind of sells their old swag from previous years as well as the current year.
[2988.50 → 2993.96] So any money you go, you can go there, and you can buy old go for con swag, T-shirts and the like.
[2994.02 → 2999.10] And they usually have tons of toys and stuff left over because they have to buy them at like 5000 units.
[2999.10 → 3007.58] All right. So there's always toys kicking about, and you can buy all those and all that money goes to the go for con scholarship fund as well.
[3007.76 → 3010.26] And then, you know, Go Bridge and Women Who Go.
[3010.46 → 3012.00] Heather says so many toys.
[3012.12 → 3012.66] There really are.
[3013.22 → 3017.26] And Go Bridge and Women Who Go also offer ways to help as well.
[3017.34 → 3024.06] I know next week you'll see me wearing all Women Who Go T-shirts all next week.
[3024.14 → 3026.36] I bought six from the Women Who Go Threadless store.
[3026.36 → 3028.96] All beautiful Ashley McInnerny designs.
[3029.28 → 3034.78] So you'll see me in a different woman Who Go t-shirt kind of every day next week as well at the conference.
[3035.06 → 3039.18] So and then that money, again, just goes to help the Go Bridge scholarship in that particular case.
[3039.64 → 3046.46] So there's a lot, you know, and last year, I guess they go for con raised $17,000 for scholarships.
[3047.08 → 3049.22] So it'd be awesome if we can raise more.
[3049.88 → 3050.50] That would be pretty cool.
[3050.72 → 3051.74] That would be pretty cool.
[3051.74 → 3052.14] Yeah.
[3052.44 → 3054.26] This is why Mark has to bring a second bag.
[3054.84 → 3055.34] For cash.
[3055.34 → 3057.54] He has to bring an empty luggage bag just to bring back.
[3057.60 → 3058.30] No, not for cash.
[3058.78 → 3060.30] For all the stuff he buys.
[3060.54 → 3061.96] What do you think I'm doing, Johnny?
[3064.10 → 3064.86] Yeah, everybody.
[3065.02 → 3065.98] Give to the Go Bridge fund.
[3066.02 → 3067.50] It all goes in this special bag I brought.
[3069.08 → 3073.14] Mark's like telling everybody, yeah, live on air, I'm going to bring in a big case full of cash.
[3073.20 → 3075.68] All of a sudden, Mark Bates turned into a grifter on the air.
[3075.74 → 3077.00] I'm not quite sure how that happens.
[3077.00 → 3079.86] But seriously, yeah, there's so many.
[3080.16 → 3084.70] And apparently, yeah, and Bill is giving a post-con workshop, which we've kind of talked about a few times.
[3085.52 → 3089.60] And 20K of those proceedings has gone to the Go Bridge Foundation already.
[3089.60 → 3093.90] So the Go for Con team really wants to help in any way they can.
[3094.20 → 3098.00] And, you know, obviously they need your help to help as well.
[3098.10 → 3099.06] So buy that swag.
[3099.74 → 3104.38] You know, support any of these community efforts, whether it be through Go Bridge or through Go for Con itself,
[3104.38 → 3107.62] because they care, and we care, and we should all care.
[3108.76 → 3109.12] Right?
[3109.26 → 3112.52] Sorry, that's my little shy off to the corner now.
[3113.62 → 3118.76] So somebody had mentioned in Slack that I believe there's a pre-party meetup, but I don't know.
[3118.84 → 3120.32] Is that before Go for Con entirely?
[3120.58 → 3126.12] I know that a lot of conferences, like different local meetups will tend to try to have a meetup like the day before the conference.
[3126.12 → 3128.42] So if you happen to be in the area early, look around for those.
[3128.42 → 3131.84] I think that's the San Diego Gophers, it looks like, on Tuesday the 23rd.
[3131.92 → 3134.68] So that's the day before the workshops.
[3135.46 → 3142.24] And I guess Cosmos is also hosting a sort of mixer party thing as well.
[3142.46 → 3142.76] Let's see.
[3142.80 → 3145.14] There are a couple sponsors that are hosting, one Tuesday and Wednesday.
[3145.24 → 3146.16] Wednesday is Cosmos.
[3146.42 → 3150.38] They're going to be holding some sort of mixer kind of singly thing here.
[3150.38 → 3155.88] And then, yeah, a meetup on Wednesday, and I don't know what the other one is because Heather hasn't finished typing it to me yet.
[3157.42 → 3159.00] I was going to say, yeah, just check those out, though.
[3159.14 → 3166.36] If you ever go to a conference, especially Go for Con, I feel like it's pretty common for people to do some sort of meetup, and it's another chance to meet people.
[3166.36 → 3169.64] And WeWork is hosting something on their place that she thinks on Friday.
[3170.02 → 3173.88] So when you show up next week, just keep your evenings free.
[3174.94 → 3175.90] Let's just put it that way.
[3175.90 → 3176.70] Seriously, seriously.
[3176.70 → 3183.40] Just, like, they're all tweeting, like, just look at everybody and just make a decision and say I'm going to all these things.
[3183.48 → 3186.54] But try to go to – it's overwhelming to go to everyone.
[3186.96 → 3193.78] But if you really want to make the most out of your conference, like meeting people and networking – I feel like we've been harping on this for an hour now, right?
[3194.30 → 3194.98] It's important.
[3195.58 → 3196.30] But it's important.
[3196.54 → 3198.22] It's why you go to a conference.
[3198.88 → 3201.38] And those events are great places to do it.
[3201.52 → 3204.34] So, you know, try to get to as many as you can.
[3204.34 → 3211.24] You know if it means taking a small nap after the conference before you go out, then take a small nap and get yourself geared up and go back out.
[3211.30 → 3212.74] Grab a coffee and do it.
[3212.78 → 3213.56] It's worth it.
[3213.92 → 3214.60] Oh, there are also groups.
[3214.66 → 3214.88] That's right.
[3214.92 → 3218.30] Yeah, there's, like, running – there's usually a running group at Go for Con every year.
[3218.50 → 3218.52] That's right.
[3218.52 → 3219.14] Yeah, yeah.
[3219.34 → 3220.18] Early morning run.
[3220.28 → 3224.84] Yeah, and I guess there are other groups in the Go for Con channel, like photography and stuff like that.
[3224.84 → 3228.42] And people are already starting to organize dinners together and stuff like that.
[3228.42 → 3235.66] So if you really, you know, follow the Slack channel, the Go for Con Slack channel, if you're looking to already start making some of those connections.
[3236.00 → 3238.78] I feel like I'd have to go and make the anything but early morning run group.
[3239.22 → 3239.60] Yeah, right.
[3239.72 → 3240.72] I don't mind running.
[3240.82 → 3242.12] I just don't like early morning runs.
[3242.24 → 3245.44] My wife has been running a half-marathon in every state.
[3245.56 → 3248.80] And she's up to, I think, 20, including Washington, D.C.
[3248.80 → 3253.02] And I'll go with her sometimes, and I'll still be sound asleep when she gets back.
[3253.74 → 3258.40] She'll go run 13.1 miles somewhere, come back.
[3258.44 → 3259.42] I'll still be sleeping.
[3260.36 → 3262.10] So, yeah, not for me.
[3262.44 → 3263.80] Oh, we forgot one thing.
[3264.04 → 3265.52] The Go for Guides program.
[3265.86 → 3266.66] I can't believe we forgot that.
[3266.88 → 3268.92] So I think it's just called the Guides.
[3269.42 → 3270.66] Oh, is it the Guides program?
[3270.80 → 3270.98] Okay.
[3271.24 → 3274.78] There's a name collision with Go for Guides, and that was more our fault than Andy's.
[3274.98 → 3275.94] Right, right, right.
[3276.02 → 3277.36] Yeah, actually, I never thought about that.
[3277.36 → 3278.82] That's, yeah, good thing.
[3279.04 → 3279.82] Yeah, thank you for bringing that up.
[3279.90 → 3286.78] Yeah, so the Guides program, Andy Walker, another known community member, basically runs this
[3286.78 → 3289.96] program for first-time attendees.
[3290.54 → 3294.48] Yeah, so basically, if you're really, like, shy, or even if you're not, right, even if
[3294.48 → 3298.18] you just want somebody that, basically, an anchor, you can always go back to and say,
[3298.24 → 3300.36] hey, so I've attended these talks.
[3300.50 → 3305.46] I'm not quite sure which other talks to go to next, or I'm not quite sure what I should
[3305.46 → 3306.00] do now.
[3306.00 → 3307.62] Oh, should I go to this event or that event?
[3308.30 → 3311.54] Usually, the Guides are sort of tethered into the community, right?
[3311.54 → 3315.98] They know sort of what's going to be more suitable for you when you compare a couple
[3315.98 → 3316.48] of things, right?
[3316.48 → 3317.24] Say, hey, oh, you know what?
[3317.32 → 3322.24] If you, I know you value X, Y, and Z, so this event or this talk is going to be more
[3322.24 → 3323.66] suitable for you than this other one, right?
[3323.66 → 3328.42] So somebody who actually knows, right, sort of what would be more appropriate for you
[3328.42 → 3332.54] based on your needs, right, for attending the conference, basically, these people can
[3332.54 → 3334.52] be, like, your guides, basically.
[3334.64 → 3336.40] They can provide some of that insight, right?
[3336.44 → 3340.32] That's going to sort of make sure you get the most out of the conference as possible.
[3340.78 → 3344.02] So definitely, that should be available, I think.
[3344.12 → 3344.78] I have some details.
[3345.04 → 3345.98] You have some details, please.
[3346.02 → 3346.74] I have details.
[3346.74 → 3350.98] So again, like previous years, the Guides program is hosted by Andy, who's just an
[3350.98 → 3352.24] awesome, awesome person.
[3352.38 → 3354.54] You should really get to know Andy because he's a lovely guy.
[3354.84 → 3357.30] Yeah, he's my co-organizer for Baltimore Go, so I know him quite well.
[3357.46 → 3358.46] Oh, there you go then, yeah.
[3359.10 → 3360.78] I wasn't saying you should meet him.
[3363.12 → 3363.98] Don't start with me.
[3365.64 → 3367.46] You know, have you ever met Victoria Portico?
[3367.60 → 3368.10] She's lovely.
[3369.00 → 3375.66] Anyway, so the gathering for the Guides program is at the hallway tracks table, which is on the
[3375.66 → 3378.98] lower level of the space, and there'll be signage when you get there.
[3379.24 → 3383.36] But so since this is going to air, what, on Tuesday, which is when everybody's in the
[3383.36 → 3387.38] air going to Gopher Con, so we're going to air while we're in the air, just a few things
[3387.38 → 3387.62] to know.
[3387.68 → 3391.96] I guess all the conference activities are going to be in the North Tower on the Grand and
[3391.96 → 3396.80] Pacific levels, according to Heather, in the Gopher, not the Gopher Guides program.
[3397.54 → 3401.32] Gopher Guides is an amazing training company who would love to help you with your Go learning
[3401.32 → 3401.64] needs.
[3402.56 → 3403.18] Shameless plug.
[3403.56 → 3404.14] You like that?
[3404.14 → 3408.06] The Guides program, however, I guess is beating on the Pacific level.
[3408.34 → 3410.48] Yeah, I think, are we out of time?
[3410.78 → 3411.58] We're pretty much there.
[3411.82 → 3412.36] Oh, boo.
[3413.14 → 3414.88] I know, we could go on for this, you know.
[3415.10 → 3419.44] Oh, and Heather's promising, I just want to say, the best Wi-Fi ever this year.
[3419.56 → 3420.36] She promises.
[3420.60 → 3420.94] What?
[3421.56 → 3423.08] That's a tall order, Heather.
[3423.54 → 3423.78] I know.
[3424.14 → 3427.38] It's brave, because I know how technology works.
[3427.60 → 3427.96] Yeah.
[3428.40 → 3429.52] There'll be like, no Wi-Fi at all.
[3429.54 → 3429.70] And here you go.
[3429.70 → 3432.44] This will really help the Wi-Fi sing in the hotel.
[3432.44 → 3434.94] Apparently, it's complimentary Wi-Fi in the guest rooms.
[3435.56 → 3437.02] So, yeah.
[3437.46 → 3437.76] Yeah.
[3437.76 → 3440.16] I would do your downloads before you end up there.
[3440.80 → 3442.24] I don't think they know what's coming.
[3442.48 → 3442.72] Yeah.
[3442.72 → 3447.82] I would definitely download anything you want before you end up.
[3449.22 → 3454.26] Because if you have 1,200 gophers in one hotel sharing free Wi-Fi, it's over.
[3454.44 → 3454.90] Game over.
[3455.00 → 3455.66] It's going to be a crawl.
[3456.04 → 3457.04] You think?
[3457.86 → 3458.18] No.
[3458.40 → 3458.56] Yeah.
[3458.74 → 3459.14] Okay.
[3459.76 → 3460.28] Well, awesome.
[3460.32 → 3460.88] I'm excited.
[3461.36 → 3462.66] I'm very excited about this year.
[3462.70 → 3463.42] It's going to be a good time.
[3463.66 → 3464.02] Yes.
[3464.32 → 3464.70] Best ever.
[3464.86 → 3465.30] It always is.
[3465.50 → 3466.18] It really is.
[3466.66 → 3466.86] Yeah.
[3466.92 → 3467.12] Yeah.
[3467.12 → 3467.98] It gets better every year.
[3468.30 → 3468.80] That's what I say.
[3469.70 → 3470.50] Honestly, you're right.
[3470.60 → 3473.26] Having, you know, Johnny, you can say it with me.
[3473.30 → 3474.80] I mean, we've both been to every one.
[3475.40 → 3477.68] It truly has gotten better every single year.
[3478.20 → 3484.62] And, you know, Heather and the team at Convention Designs really listen and care.
[3485.08 → 3488.74] And, you know, when the community speaks up about something, they jump in.
[3488.74 → 3494.68] I mean, just we didn't even get a chance to talk about the food, for example, at Go4Con, which is usually outstanding.
[3495.44 → 3497.66] Like, they just bring in some of the best.
[3497.76 → 3501.70] Like, I do believe you should always go out at least once for lunch.
[3501.72 → 3502.62] Just get out of the space.
[3502.96 → 3506.66] But, you know, if you're there, the food is truly spectacular.
[3506.76 → 3510.20] It's not brown bag conference box lunches.
[3510.34 → 3511.88] Like, it is proper food.
[3511.88 → 3515.10] They also have vegan, kosher, allele stations.
[3515.56 → 3521.36] Like, they really try to cater to everybody and really try to make it, you know, a special time for everybody.
[3521.56 → 3523.72] So, they do amazing work.
[3524.02 → 3526.06] And Heather, if you see Heather, you'll see her.
[3526.16 → 3530.04] She'll be rolling around on her scooter, probably yelling at me.
[3530.78 → 3536.56] If you see her, like, just say hi and say thank you for all the hard work she does because she does so much.
[3536.60 → 3537.20] She really does.
[3537.20 → 3544.22] If you can't recognize her, she'll probably be the boss-looking lady, you know, running around and making sure everything, you know, is going up without a hitch.
[3544.98 → 3545.92] Oh, not allowed.
[3546.06 → 3548.70] Oh, apparently they don't have the segues this year.
[3548.98 → 3551.74] Normally, in Denver, they had segues.
[3552.70 → 3554.38] So, you'd always see her zipping around.
[3555.62 → 3556.98] Red hair behind.
[3557.08 → 3558.90] She said she'll be riding her broom this year.
[3561.24 → 3562.72] Oh, Heather, we love you.
[3563.46 → 3566.26] Okay, I think that's all we've got time for, isn't it?
[3566.26 → 3568.30] We'll have to do this in person next week.
[3568.56 → 3568.90] All right.
[3568.98 → 3570.24] Thank you for joining us.
[3570.50 → 3571.46] That's it for Go Time.
[3575.54 → 3576.16] All right.
[3576.22 → 3578.74] Thank you for tuning in to this week's episode of Go Time.
[3578.84 → 3581.30] If you're not yet, hang with us and go for slack.
[3581.38 → 3583.12] We have a channel called Go Time FM.
[3583.78 → 3584.30] Look it up.
[3584.34 → 3585.08] You'll find us.
[3585.52 → 3587.04] Hang with us during the live shows.
[3587.18 → 3588.42] Connect with other members of the community.
[3588.98 → 3589.68] Share stories.
[3590.26 → 3590.84] Share codes.
[3591.00 → 3591.76] Share coffee recipes.
[3591.92 → 3592.16] Whatever.
[3592.54 → 3593.48] It's a lot of fun.
[3593.48 → 3597.48] Also, we have discussions at changelaw.com on every episode.
[3597.90 → 3600.00] Head to changelaw.com slash go time.
[3600.12 → 3602.66] Find this episode and discuss it with the community.
[3603.10 → 3608.06] Also, thanks to Vastly, our bandwidth partner, Rollbar, for helping us move fast and fix things.
[3608.34 → 3610.18] And Linde for hosting the Change Law platform.
[3610.76 → 3613.58] Our music is produced by the mysterious Break master Cylinder.
[3614.00 → 3618.06] And if you want to hear more awesome podcasts like this, subscribe to our master feed.
[3618.06 → 3622.42] It's one feed to rule them all, plus some extras that only hit the master feed.
[3622.62 → 3627.62] Head to changelaw.com slash master or search for Change Law Master in your podcast client.
[3627.70 → 3628.36] You'll find us.
[3628.70 → 3629.54] Thanks for tuning in.
[3629.74 → 3630.60] We'll see you next week.
[3648.06 → 3678.04] We'll see you next week.
[3678.06 → 3708.04] We'll see you next week.
[3708.06 → 3738.04] We'll see you next week.
[3738.06 → 3745.86] What researchers have found is that attachment, which that's what we label how we relate and connect with others.
[3746.26 → 3755.00] Attachment is 100% learned, which means our genetics don't actually contribute to how we learn to stay in proximity with other people.
[3755.00 → 3762.80] And with that, that we all develop ways to manage the threat of the loss of a relationship.
[3762.80 → 3768.34] But nobody gets to opt out of going, I need to be in relationship with others.
[3768.34 → 3772.38] I mean, think about it within the context of the prison system.
[3772.38 → 3778.86] Like, why is it that the punishment for prisoners when they don't fall in line is isolation?
[3779.42 → 3780.40] Yeah, that's true.
[3781.04 → 3781.26] Right?
[3781.32 → 3785.22] That wouldn't be significant if in some way that doesn't actually harm our brain.
[3785.22 → 3794.28] It's almost like we need to have that echo from another human being to let us know that we're there, or we're alive or just some sort of feedback loop.
[3794.34 → 3795.70] I'm not really sure how to describe that.
[3795.70 → 3799.16] Well, it really is this sense of being with, right?
[3799.26 → 3805.20] Like, I can't fight battles on my friends' behalf or on my kids' behalf, right?
[3805.30 → 3809.98] But the simple fact that I know of what's going on makes a difference.
[3809.98 → 3815.16] Because I would contend it sort of like I help them hold that weight emotionally.
[3815.16 → 3818.36] And so that actually leads me into the third thing.
[3818.74 → 3825.48] And the third thing that I would say in regard to the fundamentals of being human is that we all struggle.
[3825.74 → 3826.58] Oh, yes.
[3827.16 → 3827.64] Right?
[3828.16 → 3828.80] Big time.
[3829.28 → 3834.76] And that, you know, we don't always get to pick the way in which we struggle, but we all struggle.
[3835.44 → 3839.76] Well, if you like what you hear, you should go to changelog.com slash brain science.
[3839.86 → 3842.42] The show is not out yet, so don't get too excited.
[3842.42 → 3847.46] But you can subscribe and be notified as soon as the show launches.
[3847.98 → 3851.04] Once again, changelog.com slash brain science.

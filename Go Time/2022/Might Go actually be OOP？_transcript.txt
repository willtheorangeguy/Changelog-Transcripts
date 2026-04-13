[0.00 --> 4.06]  The answer is I don't know, but I am leaning towards yes.
[4.26 --> 6.66]  It is an object-oriented programming language,
[6.98 --> 10.58]  and it's because of multiple features that it has.
[11.00 --> 13.46]  And to explain why I think it's an object-oriented language,
[13.58 --> 18.02]  I should probably explain why I think it's definitely more object-oriented,
[18.40 --> 22.98]  for instance, than other languages that are considered object-oriented.
[22.98 --> 24.98]  And I'm looking at you, Java.
[30.00 --> 35.66]  This episode is brought to you by our friends at Square.
[35.94 --> 37.98]  Square is the platform that sellers trust.
[38.46 --> 42.72]  There is a massive opportunity for developers to support Square sellers
[42.72 --> 45.30]  by building apps for today's business needs.
[45.66 --> 48.48]  And I'm here with Shannon Skipper, Head of Developer Relations at Square.
[48.88 --> 51.54]  Shannon, can you share some details about the opportunity for developers
[51.54 --> 52.88]  on the Square platform?
[52.88 --> 53.62]  Yeah, absolutely.
[53.86 --> 56.52]  So we have millions of sellers who have unique needs,
[56.84 --> 59.92]  and Square has apps like our point-of-sale app, like our restaurants app,
[60.00 --> 63.72]  but there are so many different sellers, tuxedo shops, florists,
[63.86 --> 66.28]  who need specific solutions for their domain.
[66.54 --> 69.96]  And so we have a Node SDK written in TypeScript
[69.96 --> 73.72]  that allows you to access all of the backend APIs and SDKs
[73.72 --> 77.62]  that we use to power the billions of transactions that we do annually.
[77.84 --> 82.20]  And so there's this massive market of sellers who need help from developers.
[82.28 --> 86.94]  They either need a bespoke solution built for themselves on their own Node stack,
[86.94 --> 90.80]  where they are working with Square dashboard, working with Square hardware,
[90.80 --> 93.62]  or with the e-com, you know, what you see is what you get builder.
[93.86 --> 94.90]  And they need one more thing.
[94.96 --> 96.28]  They need an additional build.
[96.54 --> 99.06]  And then finally, we have the app marketplace where you can make a Node app
[99.06 --> 102.68]  and then distribute it so it can get in front of millions of sellers
[102.68 --> 104.58]  and be an option for them to adopt.
[104.58 --> 105.40]  Very cool.
[105.48 --> 105.74]  All right.
[105.76 --> 108.46]  If you want to learn more, head to developer.squareup.com
[108.46 --> 113.52]  to dive into the docs, APIs, SDKs, and to create your Square Developer account.
[113.82 --> 115.62]  Start developing on the platform seller's trust.
[116.06 --> 118.32]  Again, that's developer.squareup.com.
[118.32 --> 133.54]  Let's do it.
[134.12 --> 135.16]  It's go time.
[135.82 --> 137.14]  Welcome to go time.
[137.60 --> 141.02]  Your source for diverse discussions from all around the go community.
[141.34 --> 143.70]  GopherCon Europe is right around the corner,
[143.90 --> 146.06]  and you know we'll be there doing that go time thing.
[146.06 --> 149.36]  It's just two weeks away, and tickets are still on sale.
[149.52 --> 152.34]  Get yours now, and we'll see you in person or online.
[152.60 --> 154.84]  Special thanks to our partners at Fastly.
[155.04 --> 156.94]  Everything we ship here at Changelog is fast
[156.94 --> 160.92]  because Fastly serves it up super fast everywhere on Earth.
[161.26 --> 163.10]  Check them out at Fastly.com.
[163.38 --> 165.04]  Okay, here we go.
[167.16 --> 170.00]  Good evening, afternoon, morning, or night,
[170.30 --> 173.74]  everyone who's joining us live or listening to this later.
[173.74 --> 178.52]  This episode, Ian and me are being joined by Rona
[178.52 --> 183.08]  to talk about object-oriented programming.
[184.04 --> 187.28]  And we'll start by introducing Rona, I guess.
[187.80 --> 190.24]  Rona, you are an engineering manager at Delivery Hero,
[190.94 --> 192.40]  a Google developer expert for Go,
[192.88 --> 195.04]  a woman who Go organizer in Berlin,
[195.86 --> 198.74]  Go Times Unpopular Opinion Hall of Fame-er,
[198.74 --> 200.94]  and after 20 years in tech,
[201.32 --> 204.04]  you know that the sum of the opportunities
[204.04 --> 206.04]  that were given to you,
[206.54 --> 209.18]  this is why you're basically giving opportunity to others.
[209.54 --> 212.14]  So this is an interesting thing about your bio.
[212.26 --> 213.86]  We'll definitely ask you more about this.
[214.34 --> 216.20]  Now we're here to talk about this workshop
[216.20 --> 220.38]  that you've been crafting since 2017
[220.38 --> 221.78]  that you've been giving to your meetup
[221.78 --> 223.66]  at Women Who Go Berlin,
[223.66 --> 226.02]  the most recent one that you happened to give
[226.02 --> 228.94]  at GopherCon Europe later this month
[228.94 --> 232.44]  on the topic of actually object-oriented design in Go.
[232.82 --> 235.32]  So as a preparation for this episode,
[235.56 --> 240.14]  we were figuring out how each of us pronounces
[240.14 --> 243.94]  the short term for object-oriented programming.
[244.66 --> 245.50]  Rona, how do you say that?
[245.78 --> 247.08]  The three letters acronym.
[247.56 --> 248.56]  You mean OOP?
[248.90 --> 249.34]  OOP?
[250.04 --> 252.26]  Well, I guess it's two versus one, Ian.
[252.26 --> 253.40]  You pronounce this the same.
[253.68 --> 254.62]  Yeah, OOP, yeah.
[254.90 --> 255.86]  I have to say,
[256.20 --> 258.36]  for the past like a month or so,
[258.42 --> 259.60]  I've been writing OO,
[260.16 --> 260.96]  like a lot,
[261.64 --> 263.30]  and it looks like OO,
[263.52 --> 265.14]  like the emoji,
[265.60 --> 267.82]  and it feels very symbolic
[267.82 --> 270.84]  to the state of object-oriented.
[271.16 --> 273.08]  I somehow always thought it's OOP.
[273.30 --> 274.02]  You thought it was OOP?
[274.26 --> 276.96]  I guess it's because last time I used this term
[276.96 --> 277.82]  was in university,
[278.12 --> 279.24]  and it's been a while since.
[279.38 --> 280.44]  And you used to say OOP?
[280.92 --> 281.96]  Yeah, we used to say OOP.
[281.96 --> 283.10]  Ian, what do you say?
[283.50 --> 284.56]  I'd definitely say OOP.
[284.78 --> 287.42]  I don't think I've ever heard someone call it OOP before,
[287.56 --> 287.86]  actually,
[287.94 --> 289.68]  until 10 minutes ago.
[290.00 --> 292.90]  This is definitely a debate worth telling.
[293.34 --> 294.96]  Yeah, that can be a poll.
[295.04 --> 298.00]  Maybe this can even be my unpopular opinion in there.
[298.16 --> 298.92]  I thought I have none.
[299.40 --> 301.36]  So we can say this episode is sort of
[301.36 --> 303.12]  one big unpopular opinion
[303.12 --> 305.08]  coming with a claim, Rona,
[305.34 --> 309.16]  that Go can be an object-oriented programming language.
[309.16 --> 310.38]  Well, I mean,
[310.62 --> 312.38]  I definitely don't think it's not.
[313.38 --> 315.62]  So what happened was that
[315.62 --> 317.30]  I wanted to share with my team
[317.30 --> 319.76]  how to do object-oriented programming with Go.
[320.20 --> 322.38]  And then I kind of realized
[322.38 --> 325.44]  by looking at actual interview questions,
[325.68 --> 326.06]  answers,
[326.36 --> 327.54]  how people like feedback,
[328.20 --> 330.50]  how things are happening in my organization,
[330.50 --> 332.32]  what people think Go is
[332.32 --> 333.54]  and what people think Go isn't,
[333.64 --> 335.32]  they definitely think that Go is not
[335.32 --> 338.20]  an object-oriented programming language.
[338.34 --> 338.96]  So I decided,
[339.14 --> 339.50]  okay,
[339.70 --> 341.68]  I'm going to give a workshop about this,
[341.76 --> 342.14]  sort of like,
[342.40 --> 343.94]  try to sort the mess.
[344.02 --> 344.12]  Like,
[344.16 --> 345.16]  if you want to do it,
[345.20 --> 345.34]  like,
[345.40 --> 346.24]  how you should do it.
[346.62 --> 348.38]  And this has always been,
[348.42 --> 348.60]  like,
[348.62 --> 349.52]  how I do things.
[349.72 --> 350.42]  I try,
[350.52 --> 351.22]  when I teach Go,
[351.28 --> 352.58]  I try to teach people,
[352.88 --> 353.04]  like,
[353.06 --> 354.10]  if they want to do something,
[354.16 --> 355.46]  I try to teach them how to do it,
[355.50 --> 357.24]  not whether they're right or wrong
[357.24 --> 360.40]  to think or do things in a certain way.
[360.40 --> 363.90]  So it's more about how to use the tools
[363.90 --> 366.28]  that you have with the language properly.
[366.44 --> 367.86]  And especially now with generics
[367.86 --> 368.98]  going into the language,
[369.50 --> 373.10]  solving a kind of like a last kind of edge case
[373.10 --> 374.42]  that we didn't have.
[375.14 --> 375.62]  So,
[375.96 --> 376.26]  yeah,
[376.60 --> 377.24]  I posted,
[377.42 --> 379.42]  I was going to do that internally
[379.42 --> 380.60]  in the organization.
[380.78 --> 381.22]  And immediately,
[381.60 --> 383.26]  a lot of people that I've never met
[383.26 --> 385.10]  reached out to,
[385.16 --> 387.00]  to give me honest feedback
[387.00 --> 388.50]  about the workshop
[388.50 --> 390.38]  that I have never given yet.
[390.40 --> 391.20]  And then,
[391.36 --> 392.84]  then I kind of knew that,
[392.96 --> 393.12]  okay,
[393.16 --> 393.32]  like,
[393.38 --> 394.18]  I have a topic
[394.18 --> 396.22]  that is definitely worth exploring.
[397.06 --> 397.32]  So,
[397.84 --> 398.08]  yeah,
[398.38 --> 400.52]  I guess it is my unpopular opinion.
[401.18 --> 401.28]  So,
[401.60 --> 403.26]  tell us about some of that feedback
[403.26 --> 404.36]  or opinion.
[405.70 --> 406.18]  So,
[406.68 --> 407.78]  it's quite amazing.
[408.08 --> 408.22]  So,
[408.28 --> 409.62]  everybody has an opinion.
[410.38 --> 411.76]  Some people were with me
[411.76 --> 412.60]  and wanted to share
[412.60 --> 413.14]  that they are,
[413.34 --> 413.52]  you know,
[413.56 --> 414.26]  that they agree
[414.26 --> 416.30]  that Go can be object-oriented,
[416.62 --> 417.68]  which was really nice.
[417.82 --> 419.04]  What was really nice about it
[419.04 --> 420.32]  was that everybody can find
[420.32 --> 421.82]  a resource to support their claim,
[422.32 --> 424.54]  which I found amazing.
[425.58 --> 426.70]  It's brilliant.
[426.94 --> 427.10]  Like,
[427.40 --> 428.52]  I can't even begin.
[428.80 --> 429.00]  Now,
[429.06 --> 429.86]  I'm not an academic,
[430.08 --> 430.40]  obviously.
[430.80 --> 431.16]  And,
[431.28 --> 432.22]  what I do,
[432.22 --> 432.66]  I do,
[432.74 --> 434.16]  I do by trial and error.
[434.62 --> 434.82]  But,
[434.92 --> 436.06]  I did read a lot about it
[436.06 --> 437.26]  for the past few months
[437.26 --> 439.36]  since we kind of decided
[439.36 --> 440.62]  that I was going to do this.
[440.62 --> 441.12]  and,
[441.12 --> 442.26]  the answer is,
[442.30 --> 442.96]  I don't know.
[443.66 --> 444.02]  But,
[444.44 --> 446.12]  I am leaning towards yes.
[446.70 --> 448.00]  It is an object-oriented
[448.00 --> 449.36]  programming language.
[449.68 --> 450.22]  And,
[450.22 --> 451.44]  it's because of
[451.44 --> 452.44]  multiple features
[452.44 --> 453.28]  that it has.
[454.18 --> 454.28]  And,
[454.38 --> 455.12]  to explain why
[455.12 --> 456.20]  I think it's object-oriented
[456.20 --> 456.70]  languages,
[457.00 --> 458.22]  object-oriented language,
[458.34 --> 459.80]  I should probably explain
[459.80 --> 461.24]  why I think it's
[461.24 --> 463.20]  definitely more object-oriented,
[463.58 --> 464.18]  for instance,
[464.32 --> 465.84]  than other languages
[465.84 --> 466.70]  that are considered
[466.70 --> 468.14]  object-oriented.
[468.14 --> 468.86]  And,
[468.98 --> 469.74]  I'm looking at you,
[469.86 --> 470.16]  Java.
[470.88 --> 471.12]  And,
[471.18 --> 471.96]  here is my case.
[472.02 --> 472.50]  Listen up.
[473.42 --> 473.90]  Java,
[474.48 --> 474.72]  yes,
[474.82 --> 475.00]  sure,
[475.06 --> 475.86]  it has inheritance.
[476.52 --> 476.90]  But,
[477.34 --> 479.00]  you can only inherit once.
[479.48 --> 479.68]  So,
[479.76 --> 480.52]  that means that
[480.52 --> 481.96]  if class A,
[482.08 --> 483.08]  you want to express
[483.08 --> 483.98]  the idea that
[483.98 --> 484.70]  class A,
[484.86 --> 486.18]  or an object of type A,
[486.26 --> 488.42]  is also an object of type B,
[488.54 --> 489.38]  or class B,
[489.98 --> 491.34]  you can only do that once.
[491.40 --> 491.48]  And,
[491.56 --> 493.06]  if you have a case C,
[493.82 --> 495.32]  that A is also C,
[495.78 --> 497.48]  you cannot express that in Java.
[497.48 --> 498.16]  Now,
[498.24 --> 499.44]  I came from C++,
[499.76 --> 500.54]  so I kind of,
[500.58 --> 500.90]  you know,
[500.98 --> 502.30]  had this multiple inheritance.
[502.74 --> 504.22]  I used to be very expressive
[504.22 --> 505.10]  with inheritance.
[505.64 --> 505.72]  And,
[505.82 --> 506.60]  when I look at Java,
[506.78 --> 507.62]  when I look at Ruby,
[508.28 --> 508.74]  Pythonistas,
[508.92 --> 509.28]  I'm sorry,
[509.42 --> 510.96]  I'm not familiar enough
[510.96 --> 511.52]  with your language
[511.52 --> 512.00]  to know,
[512.26 --> 513.00]  to make a case.
[513.60 --> 513.82]  But,
[513.92 --> 514.70]  when I look at Java,
[514.80 --> 515.58]  when I look at Ruby,
[516.14 --> 517.50]  I see that
[517.50 --> 519.06]  you can't really express
[519.06 --> 520.52]  A is C,
[520.62 --> 521.66]  if you already express
[521.66 --> 522.62]  that A is B,
[523.12 --> 524.60]  unless you use interfaces
[524.60 --> 525.54]  or generics.
[525.54 --> 526.58]  Now,
[526.88 --> 529.02]  interfaces are,
[529.46 --> 531.58]  the Go has this dramatic effect
[531.58 --> 532.96]  that interfaces are implicit.
[533.74 --> 534.78]  In Java,
[535.52 --> 537.26]  a class has to be aware,
[537.54 --> 538.50]  to be able to instantiate
[539.18 --> 541.52]  A as type interface I,
[542.36 --> 543.92]  A has to be aware of I
[543.92 --> 545.02]  at the time of writing.
[545.58 --> 546.06]  So,
[546.16 --> 548.46]  that means that to plug A as I,
[548.68 --> 549.96]  you have to do something.
[549.96 --> 551.86]  It could be generics,
[552.24 --> 553.26]  it could be
[553.26 --> 555.70]  some sort of a proxy class
[555.70 --> 556.96]  that we'll implement
[556.96 --> 558.30]  and derive from.
[559.08 --> 559.34]  So,
[559.40 --> 560.20]  there are some ways.
[560.76 --> 560.88]  And,
[560.96 --> 561.32]  in Ruby,
[561.42 --> 562.44]  we also see
[562.44 --> 563.64]  how modules
[563.64 --> 565.04]  are kind of replacing
[565.04 --> 565.94]  generics
[565.94 --> 567.50]  and what people used to do
[567.50 --> 568.72]  in other languages
[568.72 --> 570.18]  to sort of be able
[570.18 --> 571.40]  to be very expressive
[571.40 --> 572.24]  that something
[572.24 --> 573.56]  is also something else.
[574.38 --> 574.70]  So,
[575.14 --> 576.32]  the answer is that
[576.32 --> 577.16]  I think that Go
[577.16 --> 579.74]  is object-oriented.
[580.46 --> 581.96]  I'm leaning towards yes.
[582.30 --> 583.38]  I do see why people
[583.38 --> 584.28]  don't think so.
[585.18 --> 585.66]  But,
[585.74 --> 585.88]  yeah,
[585.96 --> 586.86]  that's where I am
[586.86 --> 588.08]  as a person
[588.08 --> 590.28]  who works with Go.
[590.54 --> 591.06]  Can we go through
[591.06 --> 591.68]  some of the reasons
[591.68 --> 592.80]  people said it wasn't?
[592.90 --> 593.04]  Like,
[593.42 --> 594.48]  because it lacks inheritance?
[594.68 --> 594.80]  Like,
[594.84 --> 595.86]  what features are missing
[595.86 --> 596.72]  that people are like,
[596.76 --> 597.88]  it's not object-oriented?
[598.20 --> 599.44]  I think it's about
[599.44 --> 600.12]  the styling.
[600.12 --> 600.52]  So,
[600.62 --> 600.88]  yes,
[601.02 --> 602.50]  most people talk about
[602.50 --> 603.48]  the lack of hierarchy,
[604.24 --> 606.46]  the composition over,
[607.08 --> 607.42]  what's the word
[607.42 --> 607.98]  I'm looking for?
[608.54 --> 608.98]  Inheritance?
[609.52 --> 610.10]  I guess.
[610.36 --> 610.70]  I mean,
[610.86 --> 611.82]  I think there is a,
[611.84 --> 612.20]  like,
[612.28 --> 613.50]  general term for inheritance,
[613.64 --> 613.92]  but yeah.
[614.40 --> 614.66]  Okay.
[614.82 --> 616.10]  I think it's about,
[617.06 --> 618.12]  I think people do a lot
[618.12 --> 619.60]  of procedural coding with Go.
[619.90 --> 621.06]  You don't have constructors,
[621.16 --> 621.64]  for instance,
[621.72 --> 621.96]  right?
[622.44 --> 624.12]  And why do you not have constructors?
[624.16 --> 625.54]  Because anything can be a type.
[625.88 --> 627.32]  An integer can be a new type.
[627.40 --> 628.64]  You can define a new type
[628.64 --> 629.34]  with pretty much
[629.34 --> 630.74]  in any way that you want.
[631.30 --> 631.50]  So,
[631.56 --> 632.64]  you don't really have constructors
[632.64 --> 633.66]  because you don't have classes
[633.66 --> 635.22]  and anything can be a type.
[635.58 --> 636.96]  And then everything can have
[636.96 --> 637.78]  also methods.
[638.54 --> 638.98]  But,
[639.06 --> 640.10]  the truth is that
[640.10 --> 641.62]  without constructors,
[642.00 --> 642.64]  without a sort of
[642.64 --> 643.70]  a formal way
[643.70 --> 645.08]  of working,
[645.20 --> 645.44]  I think,
[645.50 --> 646.24]  with objects,
[646.94 --> 647.82]  people get lost.
[648.52 --> 649.02]  And then,
[649.10 --> 649.42]  you know,
[649.56 --> 650.62]  they look down at people
[650.62 --> 652.02]  who come in from other languages
[652.02 --> 654.98]  who need these things.
[655.58 --> 656.54]  It is very difficult
[656.54 --> 658.22]  to define a type
[658.22 --> 659.62]  and allow anybody
[659.62 --> 660.60]  to make any changes.
[660.60 --> 660.80]  So,
[660.88 --> 662.02]  you cannot really tell.
[662.50 --> 663.22]  How do you tell
[663.22 --> 664.44]  if it's corrupt or not?
[664.72 --> 665.28]  How do you write
[665.28 --> 666.80]  any kind of defensive code
[666.80 --> 667.70]  in that situation?
[668.34 --> 669.54]  We also have these,
[669.58 --> 669.78]  you know,
[669.88 --> 670.38]  best practices.
[670.50 --> 670.66]  I mean,
[670.98 --> 671.92]  I don't like the word
[671.92 --> 672.66]  best practices
[672.66 --> 674.18]  because I think that
[674.18 --> 675.74]  I usually use the word
[675.74 --> 676.62]  common practice
[676.62 --> 677.46]  to explain
[677.46 --> 679.38]  because it's not always best,
[679.46 --> 679.62]  right?
[679.66 --> 680.20]  There's a case
[680.20 --> 681.24]  for pretty much anything.
[681.74 --> 683.00]  But the common practices
[683.00 --> 684.40]  are everything is public.
[684.64 --> 685.74]  Anyone can do anything
[685.74 --> 686.38]  with the guy
[686.38 --> 687.16]  and if they don't read
[687.16 --> 687.88]  the documentation,
[688.06 --> 688.36]  tough.
[688.96 --> 689.40]  So,
[690.20 --> 691.32]  it is a bit tricky
[691.32 --> 692.24]  for people coming
[692.24 --> 692.96]  into the language
[692.96 --> 693.96]  to know exactly
[693.96 --> 694.66]  what they're supposed
[694.66 --> 695.46]  to do and how.
[696.18 --> 696.84]  And in that sense,
[696.88 --> 697.54]  we're not making
[697.54 --> 698.34]  their lives easier.
[698.76 --> 699.78]  We're just making it harder
[699.78 --> 700.54]  instead of doing
[700.54 --> 701.20]  this gatekeeping.
[701.30 --> 701.66]  Oh, no,
[701.70 --> 702.52]  you come from Java.
[702.66 --> 703.46]  You probably don't know
[703.46 --> 703.92]  how to go.
[704.66 --> 705.38]  Never mind.
[705.66 --> 706.64]  Forget about it.
[707.08 --> 708.52]  This will take some time
[708.52 --> 709.76]  and it doesn't matter.
[709.92 --> 710.96]  They could have 20 years
[710.96 --> 711.76]  of experience
[711.76 --> 713.92]  and still look at them
[713.92 --> 714.14]  like,
[714.54 --> 715.36]  but do you know Go?
[715.90 --> 716.32]  Do you?
[717.00 --> 717.44]  So,
[717.60 --> 718.48]  that's where I am.
[718.62 --> 719.68]  I am curious though
[719.68 --> 720.64]  if we're getting any
[720.64 --> 721.84]  remarks from our listeners.
[722.32 --> 722.54]  So,
[722.88 --> 723.58]  maybe they have
[723.58 --> 724.40]  some opinions.
[724.68 --> 725.58]  Not just yet.
[725.68 --> 726.32]  Not just yet.
[726.36 --> 727.70]  But maybe any minute now.
[727.90 --> 728.28]  Hopefully.
[728.74 --> 729.74]  One can only hope.
[730.78 --> 731.64]  I'll be curious to hear
[731.64 --> 732.94]  what are some of the
[732.94 --> 734.60]  feedbacks that you got
[734.60 --> 735.58]  over the email.
[735.76 --> 735.80]  Like,
[735.84 --> 736.70]  what are the
[736.70 --> 738.38]  pros
[738.38 --> 739.20]  or the people
[739.20 --> 740.26]  who agreed or disagreed?
[740.36 --> 741.18]  You said that they were
[741.18 --> 742.60]  all backing their claims
[742.60 --> 743.34]  which is wonderful.
[743.52 --> 744.42]  It means you have
[744.42 --> 745.34]  generally a great
[745.34 --> 746.44]  discussion.
[746.70 --> 746.98]  Well,
[747.10 --> 747.42]  I mean,
[747.60 --> 748.46]  so there is
[748.46 --> 749.50]  expected practices.
[749.64 --> 750.42]  What was the term you used?
[750.58 --> 751.16]  Common practices.
[751.86 --> 752.80]  And that's great.
[752.92 --> 753.02]  So,
[753.26 --> 753.78]  tell us about them.
[754.08 --> 754.22]  Well,
[754.26 --> 755.04]  the first comment
[755.04 --> 755.96]  that I got was,
[756.42 --> 757.50]  that was really funny,
[758.00 --> 758.22]  was,
[758.38 --> 759.28]  aren't generics enough?
[759.54 --> 760.34]  OOP now?
[760.52 --> 760.70]  Really?
[761.36 --> 762.28]  Something like that.
[763.32 --> 764.64]  I thought that was hilarious.
[765.40 --> 765.68]  So,
[765.90 --> 767.70]  people do refer me a lot.
[768.38 --> 770.04]  to the Go FAQs
[770.04 --> 771.38]  that specifically say
[771.38 --> 772.12]  that the answer
[772.12 --> 773.12]  to whether Go
[773.12 --> 774.30]  is object-oriented
[774.30 --> 774.90]  or not
[774.90 --> 776.66]  is yes and no.
[778.02 --> 778.92]  And then,
[779.28 --> 779.62]  no,
[779.70 --> 779.98]  actually,
[780.14 --> 781.28]  is it a yes and no?
[781.52 --> 781.76]  Or,
[781.92 --> 782.48]  I don't remember.
[782.82 --> 784.08]  I actually prepared it for you.
[784.16 --> 785.04]  Let me read this out.
[785.18 --> 785.72]  Oh, amazing.
[786.28 --> 786.94]  Yes and no.
[787.24 --> 788.36]  Although Go has
[788.36 --> 789.24]  types and methods
[789.24 --> 790.82]  and allows an object-oriented
[790.82 --> 791.78]  style of programming,
[792.06 --> 793.34]  there is no type hierarchy.
[793.92 --> 795.72]  The concept of interface
[795.72 --> 796.58]  in Go provides
[796.58 --> 797.62]  a different approach
[797.62 --> 798.40]  that we believe
[798.40 --> 799.42]  is easy to use
[799.42 --> 800.12]  and in some ways
[800.12 --> 800.72]  more general.
[801.48 --> 802.68]  There are also ways
[802.68 --> 803.68]  to embed types
[803.68 --> 804.48]  in other types
[804.48 --> 805.38]  to provide something
[805.38 --> 806.14]  analogous
[806.14 --> 807.08]  but not identical
[807.08 --> 808.56]  to subclassic.
[808.98 --> 809.54]  Moreover,
[810.06 --> 810.76]  methods in Go
[810.76 --> 812.04]  are more general
[812.04 --> 812.72]  than C++
[812.72 --> 813.50]  or in Java.
[814.16 --> 815.14]  They can be defined
[815.14 --> 816.94]  for any sort of data,
[817.18 --> 818.04]  even built-in types
[818.04 --> 818.70]  such as plain
[818.70 --> 819.62]  and boxed integers,
[819.62 --> 820.58]  and they're not
[820.58 --> 821.26]  restricted to
[821.26 --> 822.40]  classes
[822.40 --> 823.52]  slash structs.
[824.36 --> 824.72]  Also,
[825.10 --> 826.50]  the lack of type hierarchy
[826.50 --> 827.40]  makes objects
[827.40 --> 828.08]  in Go feel
[828.08 --> 828.90]  much more lightweight
[828.90 --> 830.12]  than in languages
[830.12 --> 831.14]  like C++
[831.14 --> 831.78]  or Java.
[832.16 --> 832.40]  Well,
[832.44 --> 833.30]  I kind of agree.
[834.44 --> 835.18]  I mean,
[835.64 --> 836.18]  but then,
[836.26 --> 836.48]  you know,
[836.56 --> 837.96]  I went into the rabbit hole
[837.96 --> 839.02]  because what I remembered,
[839.28 --> 840.12]  what I remembered,
[840.28 --> 840.54]  you know,
[840.60 --> 842.12]  from my university
[842.12 --> 843.86]  was my professor,
[844.12 --> 845.12]  Jeff Rosenstein,
[845.70 --> 846.36]  explaining
[846.36 --> 848.16]  that object-oriented
[848.16 --> 849.18]  is about being able
[849.18 --> 849.94]  to send messages
[849.94 --> 850.76]  to objects.
[851.28 --> 852.40]  And I checked,
[852.58 --> 853.26]  played the origin
[853.26 --> 854.14]  of the idea
[854.14 --> 855.50]  and it appears
[855.50 --> 856.56]  to be the case
[856.56 --> 858.18]  that that is what
[858.18 --> 861.24]  they were going for.
[861.58 --> 862.42]  It wasn't so much
[862.42 --> 863.18]  about hierarchy.
[863.42 --> 864.60]  Hierarchy came in later.
[865.46 --> 865.62]  So,
[866.34 --> 867.14]  if we go back
[867.14 --> 867.74]  to basics,
[867.94 --> 868.40]  maybe Go
[868.40 --> 870.20]  is fully object-oriented.
[871.08 --> 871.54]  And I think
[871.54 --> 872.34]  to answer that,
[872.86 --> 873.78]  you probably need
[873.78 --> 874.28]  to know more
[874.28 --> 874.96]  than I do
[874.96 --> 876.80]  about language design.
[877.40 --> 878.14]  But again,
[878.14 --> 879.46]  from practice,
[879.72 --> 881.02]  I'm leaning towards yes.
[881.72 --> 882.64]  And in the workshop,
[882.96 --> 884.54]  we do things
[884.54 --> 885.62]  very Java-like.
[886.42 --> 887.42]  Exactly the kinds
[887.42 --> 887.82]  of things
[887.82 --> 888.38]  that you're not
[888.38 --> 889.18]  supposed to do
[889.18 --> 889.98]  or it's not really
[889.98 --> 890.44]  that you're not
[890.44 --> 891.04]  supposed to do.
[891.16 --> 892.20]  But we really
[892.20 --> 893.18]  try to express
[893.18 --> 894.50]  the same types
[894.50 --> 895.16]  of ideas
[895.16 --> 896.54]  that keeping
[896.54 --> 898.82]  loyal to,
[898.96 --> 899.32]  I guess,
[899.38 --> 900.02]  the go-way
[900.02 --> 901.02]  of doing things still.
[901.94 --> 902.14]  So,
[902.78 --> 902.98]  yeah,
[903.10 --> 903.48]  I mean,
[903.56 --> 904.18]  at the very least,
[904.24 --> 904.64]  it's going to be
[904.64 --> 905.16]  a lot of fun.
[905.16 --> 907.30]  I try to at least
[907.30 --> 908.24]  add some value
[908.24 --> 909.42]  in that regard.
[909.64 --> 910.42]  I give people
[910.42 --> 911.22]  a good taste
[911.22 --> 913.18]  of how they can
[913.18 --> 913.72]  do things
[913.72 --> 914.50]  and how they can
[914.50 --> 915.26]  get creative.
[915.78 --> 916.58]  But I also think
[916.58 --> 917.48]  that there is
[917.48 --> 918.40]  a lot of room
[918.40 --> 919.00]  for people
[919.00 --> 920.20]  to decide
[920.20 --> 921.38]  within their teams
[921.38 --> 922.84]  their own
[922.84 --> 923.82]  best practices,
[924.00 --> 924.80]  their own practices,
[925.06 --> 926.60]  how they want
[926.60 --> 927.32]  to do things.
[927.84 --> 928.68]  I do think
[928.68 --> 929.34]  there should be
[929.34 --> 930.78]  a discussion.
[930.98 --> 931.68]  I also think
[931.68 --> 932.30]  that it should be
[932.30 --> 932.88]  a little bit
[932.88 --> 934.42]  more lively
[934.42 --> 935.66]  than it is now
[935.66 --> 936.64]  where I think
[936.64 --> 937.20]  the veterans
[937.20 --> 938.22]  sort of dictate
[938.22 --> 939.02]  how people
[939.02 --> 939.46]  are going to
[939.46 --> 940.00]  use the language.
[940.42 --> 940.92]  The users
[940.92 --> 941.72]  of the language
[941.72 --> 942.44]  that are coming
[942.44 --> 943.78]  in are in the future.
[943.90 --> 944.34]  They are going
[944.34 --> 945.60]  to also decide
[945.60 --> 946.68]  for themselves
[946.68 --> 947.40]  how they want
[947.40 --> 947.94]  to do things,
[948.00 --> 948.40]  how they want
[948.40 --> 948.92]  to program.
[949.08 --> 949.52]  They should have
[949.52 --> 950.56]  a space to do that.
[951.32 --> 951.74]  And if they're
[951.74 --> 952.22]  coming from
[952.22 --> 952.74]  other languages
[952.74 --> 953.72]  and they work
[953.72 --> 954.82]  in a similar way,
[954.88 --> 955.34]  that's fine.
[955.74 --> 956.52]  You asked me
[956.52 --> 957.22]  about quotes
[957.22 --> 957.84]  that I got.
[958.14 --> 959.12]  Somebody quoted
[959.12 --> 960.10]  Rob Pike to me.
[960.10 --> 961.44]  I tried.
[961.56 --> 962.10]  I couldn't find
[962.10 --> 962.48]  a quote.
[962.86 --> 963.28]  But somebody
[963.28 --> 964.14]  quoted Rob Pike
[964.14 --> 964.46]  to me.
[964.54 --> 965.02]  So apparently
[965.02 --> 965.74]  Rob Pike
[965.74 --> 966.86]  did say something
[966.86 --> 968.16]  about object-oriented
[968.16 --> 970.32]  look like this,
[970.68 --> 971.40]  I guess,
[971.78 --> 972.40]  object-oriented
[972.40 --> 973.60]  or something
[973.60 --> 974.28]  of the sort.
[974.80 --> 975.22]  But yeah,
[975.28 --> 976.00]  I didn't get
[976.00 --> 976.72]  the source.
[977.44 --> 978.36]  What I do see
[978.36 --> 979.42]  is a lot of people,
[979.62 --> 979.78]  you know,
[979.82 --> 980.24]  sort of,
[980.78 --> 981.26]  this is where
[981.26 --> 981.86]  I think this is
[981.86 --> 982.36]  coming from.
[982.96 --> 983.76]  How people write
[983.76 --> 984.26]  APIs,
[984.60 --> 985.50]  how people write
[985.50 --> 986.52]  their handlers,
[986.88 --> 987.86]  it's all pretty much
[987.86 --> 988.80]  functional programming.
[988.80 --> 989.72]  The way that this
[989.72 --> 990.26]  is designed,
[990.78 --> 991.36]  most people
[991.36 --> 992.22]  don't actually
[992.22 --> 993.26]  use an interface
[993.26 --> 994.48]  in these situations
[994.48 --> 995.62]  and even if they do,
[996.16 --> 996.70]  they kind of
[996.70 --> 997.88]  don't use object,
[998.00 --> 998.82]  they use the functions
[998.82 --> 999.90]  as an interface,
[1000.36 --> 1001.46]  which you can do,
[1001.62 --> 1002.32]  you can infer,
[1002.88 --> 1004.02]  so they're not used
[1004.02 --> 1006.16]  to actually working
[1006.16 --> 1007.64]  with objects
[1007.64 --> 1009.46]  or not objects,
[1009.62 --> 1010.18]  objects is not,
[1010.36 --> 1010.58]  like,
[1010.66 --> 1011.52]  let's say struts.
[1011.68 --> 1012.76]  Let's just use
[1012.76 --> 1013.52]  the word struts
[1013.52 --> 1014.22]  with fields
[1014.22 --> 1014.90]  and actual,
[1015.12 --> 1015.40]  you know,
[1015.70 --> 1016.90]  the classic sort of way
[1016.90 --> 1017.80]  of doing things.
[1017.80 --> 1019.38]  And I think
[1019.38 --> 1019.76]  this is,
[1019.90 --> 1020.50]  I think that's
[1020.50 --> 1021.30]  where it's coming from
[1021.30 --> 1022.00]  because we came
[1022.00 --> 1022.70]  with a language
[1022.70 --> 1023.70]  that was so strong
[1023.70 --> 1024.58]  in that space
[1024.58 --> 1025.72]  and in that space
[1025.72 --> 1026.84]  you really don't need,
[1026.98 --> 1027.44]  you know,
[1027.48 --> 1028.60]  a lot of running objects
[1028.60 --> 1029.40]  and whatever objects
[1029.40 --> 1029.92]  you have
[1029.92 --> 1031.16]  are probably going
[1031.16 --> 1032.46]  to die soon anyways.
[1033.04 --> 1033.64]  And if we think
[1033.64 --> 1035.02]  also like those APIs,
[1035.74 --> 1035.98]  you know,
[1036.02 --> 1036.68]  it sounds funny,
[1036.78 --> 1037.22]  but I mean,
[1037.26 --> 1038.40]  objects don't live long
[1038.40 --> 1038.96]  in APIs
[1038.96 --> 1040.78]  unless they live
[1040.78 --> 1041.96]  the entire lifetime
[1041.96 --> 1042.92]  of the application.
[1042.92 --> 1045.06]  and like the server,
[1045.24 --> 1045.62]  for instance,
[1045.72 --> 1046.48]  that could be
[1046.48 --> 1048.16]  an object.
[1048.56 --> 1049.22]  Their struts
[1049.22 --> 1050.32]  are limited to fields
[1050.32 --> 1051.38]  like configurations
[1051.38 --> 1052.76]  and they don't have
[1052.76 --> 1053.44]  many methods,
[1053.52 --> 1053.72]  right?
[1054.22 --> 1055.12]  But then if you look,
[1055.24 --> 1055.54]  for instance,
[1055.66 --> 1056.68]  at how they set up
[1056.68 --> 1057.66]  their repositories
[1057.66 --> 1059.10]  or how they set up
[1059.10 --> 1059.76]  their models,
[1059.92 --> 1060.46]  how they set up
[1060.46 --> 1061.04]  these things,
[1061.44 --> 1062.80]  because we didn't
[1062.80 --> 1063.60]  have generics
[1063.60 --> 1065.08]  up until very recently,
[1065.74 --> 1066.34]  they don't really
[1066.34 --> 1067.44]  use objects for that
[1067.44 --> 1068.16]  or they generate
[1068.16 --> 1069.12]  a lot of code,
[1069.12 --> 1069.74]  but they don't
[1069.74 --> 1070.84]  actually know
[1070.84 --> 1071.56]  what's in it
[1071.56 --> 1072.70]  or care so much
[1072.70 --> 1073.30]  about it
[1073.30 --> 1075.04]  just to save,
[1075.22 --> 1075.40]  store,
[1075.52 --> 1075.80]  whatever.
[1075.96 --> 1076.66]  But with generics,
[1076.70 --> 1077.18]  you can actually
[1077.18 --> 1078.64]  store any kind
[1078.64 --> 1079.26]  of model
[1079.26 --> 1080.62]  into any kind
[1080.62 --> 1081.90]  of database
[1081.90 --> 1083.44]  or repository.
[1084.18 --> 1085.26]  So we are
[1085.26 --> 1086.18]  that much stronger
[1086.18 --> 1088.02]  in that sense.
[1088.20 --> 1088.40]  Now,
[1088.72 --> 1090.42]  maybe that's going
[1090.42 --> 1090.58]  to,
[1090.78 --> 1091.92]  maybe now the people
[1091.92 --> 1092.64]  are actually going
[1092.64 --> 1093.42]  to write code
[1093.42 --> 1094.10]  for themselves.
[1094.10 --> 1094.64]  They're actually
[1094.64 --> 1096.52]  going to spend
[1096.52 --> 1097.26]  more time thinking
[1097.26 --> 1098.10]  about what they
[1098.10 --> 1099.10]  want to express.
[1099.12 --> 1099.68]  and how,
[1100.18 --> 1100.56]  hopefully.
[1113.16 --> 1114.30]  This episode
[1114.30 --> 1115.38]  is brought to you
[1115.38 --> 1116.06]  by Honeycomb.
[1116.20 --> 1116.96]  Find your most
[1116.96 --> 1117.80]  perplexing application
[1117.80 --> 1118.56]  issues.
[1118.86 --> 1119.70]  Honeycomb is
[1119.70 --> 1121.24]  a fast analysis
[1121.24 --> 1122.22]  tool that reveals
[1122.22 --> 1122.80]  the truth about
[1122.80 --> 1123.90]  every aspect
[1123.90 --> 1125.02]  of your application
[1125.02 --> 1125.78]  in production.
[1126.24 --> 1126.88]  Find out how users
[1126.88 --> 1127.66]  experience your code
[1127.66 --> 1128.36]  in complex
[1128.36 --> 1129.48]  and unpredictable
[1129.48 --> 1130.24]  environments.
[1130.58 --> 1131.26]  Find patterns
[1131.26 --> 1132.28]  and outliers
[1132.28 --> 1133.12]  across billions
[1133.12 --> 1133.88]  of rows of data
[1133.88 --> 1134.64]  and definitively
[1134.64 --> 1135.44]  solve your problems.
[1135.88 --> 1136.62]  And we use Honeycomb
[1136.62 --> 1137.36]  here at Change.
[1137.40 --> 1138.02]  That's why we welcome
[1138.02 --> 1138.44]  the opportunity
[1138.44 --> 1139.40]  to add them
[1139.40 --> 1140.18]  as one of our
[1140.18 --> 1141.20]  infrastructure partners.
[1141.70 --> 1142.22]  In particular,
[1142.22 --> 1143.12]  we use Honeycomb
[1143.12 --> 1143.88]  to track down
[1143.88 --> 1144.86]  CDN issues recently,
[1145.18 --> 1145.68]  which we talked
[1145.68 --> 1146.60]  about at length
[1146.60 --> 1147.84]  on the Kaizen edition
[1147.84 --> 1149.06]  of the Ship It podcast.
[1149.30 --> 1149.98]  So check that out.
[1150.20 --> 1150.70]  Here's the thing.
[1150.92 --> 1151.78]  Teams who don't use
[1151.78 --> 1152.18]  Honeycomb
[1152.18 --> 1153.32]  are forced to find
[1153.32 --> 1154.20]  the needle in the haystack.
[1154.20 --> 1155.34]  They scroll through
[1155.34 --> 1156.44]  endless dashboards
[1156.44 --> 1157.48]  playing whack-a-mole.
[1157.72 --> 1158.88]  They deal with alert floods,
[1159.08 --> 1159.70]  trying to guess
[1159.70 --> 1160.74]  which one matters,
[1161.08 --> 1162.06]  and they go from tool
[1162.06 --> 1162.92]  to tool to tool
[1162.92 --> 1163.76]  playing sleuth,
[1163.98 --> 1164.60]  trying to figure out
[1164.60 --> 1165.72]  how all the puzzle pieces
[1165.72 --> 1166.34]  fit together.
[1166.68 --> 1167.94]  It's this context switching
[1167.94 --> 1169.04]  and tool sprawl
[1169.04 --> 1169.96]  that are slowly killing
[1169.96 --> 1171.00]  teams' effectiveness
[1171.00 --> 1172.36]  and ultimately hindering
[1172.36 --> 1173.00]  their business.
[1173.40 --> 1173.92]  With Honeycomb,
[1174.00 --> 1174.98]  you get a fast,
[1175.28 --> 1175.84]  unified,
[1176.12 --> 1177.62]  and clear understanding
[1177.62 --> 1179.02]  of the one thing
[1179.02 --> 1180.16]  driving your business.
[1180.42 --> 1180.84]  Production.
[1181.36 --> 1181.94]  With Honeycomb,
[1181.94 --> 1182.88]  you guess less
[1182.88 --> 1183.84]  and you know more.
[1184.30 --> 1184.90]  Join the swarm
[1184.90 --> 1186.70]  and try Honeycomb free today
[1186.70 --> 1188.30]  at honeycomb.io
[1188.30 --> 1189.42]  slash changelog.
[1189.58 --> 1190.14]  Again,
[1190.28 --> 1191.40]  honeycomb.io
[1191.40 --> 1193.06]  slash changelog.
[1210.02 --> 1210.54]  So,
[1210.74 --> 1211.62]  you're going through that,
[1211.62 --> 1212.76]  like what you just said,
[1212.82 --> 1213.28]  made me think
[1213.28 --> 1214.30]  maybe my idea
[1214.30 --> 1216.42]  of what OOP is
[1216.42 --> 1218.02]  is pretty heavily influenced
[1218.02 --> 1218.56]  and biased
[1218.56 --> 1219.54]  by writing Go.
[1219.76 --> 1219.98]  Like,
[1220.02 --> 1220.88]  I haven't written anything
[1220.88 --> 1223.08]  but Go in a long time.
[1223.44 --> 1223.62]  Right?
[1223.76 --> 1224.02]  So,
[1224.50 --> 1224.70]  like,
[1224.86 --> 1225.74]  probably two or three years
[1225.74 --> 1226.28]  at this point.
[1226.80 --> 1227.02]  So,
[1227.10 --> 1227.70]  going through that,
[1227.84 --> 1228.20]  you're right.
[1228.30 --> 1228.46]  Like,
[1228.86 --> 1230.00]  I think a lot of the,
[1230.00 --> 1230.22]  like,
[1230.32 --> 1231.42]  OOP stuff that was taught
[1231.42 --> 1231.88]  in school,
[1232.46 --> 1233.40]  I don't use anymore,
[1233.40 --> 1234.36]  but I still think of what
[1234.36 --> 1235.76]  I'm doing as object-oriented.
[1236.06 --> 1236.94]  And maybe I'm wrong.
[1237.14 --> 1237.30]  Like,
[1237.98 --> 1238.18]  like,
[1238.24 --> 1238.80]  in my mind,
[1239.20 --> 1239.90]  object-oriented
[1239.90 --> 1241.28]  is just like encapsulating
[1241.28 --> 1242.58]  a set of data
[1242.58 --> 1243.96]  and having methods on it
[1243.96 --> 1245.68]  that is like self-contained,
[1245.74 --> 1245.92]  right?
[1245.92 --> 1246.84]  And maybe that's not
[1246.84 --> 1247.48]  what it actually is.
[1247.54 --> 1248.04]  Maybe I'm totally
[1248.04 --> 1249.58]  misunderstanding the concept.
[1250.10 --> 1250.26]  So,
[1250.54 --> 1251.22]  that's interesting.
[1251.44 --> 1252.00]  You said it.
[1252.06 --> 1252.92]  You actually said it.
[1253.58 --> 1254.86]  Said encapsulation.
[1254.86 --> 1255.66]  So,
[1255.70 --> 1256.80]  it's about encapsulation,
[1256.92 --> 1257.40]  abstraction,
[1258.00 --> 1259.48]  and later came in
[1259.48 --> 1260.24]  generalization.
[1261.12 --> 1261.52]  So,
[1261.88 --> 1263.00]  to encapsulate,
[1263.10 --> 1263.92]  you don't need hierarchy.
[1265.00 --> 1265.38]  Or,
[1265.74 --> 1266.16]  I mean,
[1266.36 --> 1267.64]  you can have a composition,
[1267.96 --> 1268.36]  essentially,
[1268.64 --> 1269.76]  and that would work
[1269.76 --> 1270.66]  pretty well,
[1270.76 --> 1270.96]  too,
[1271.20 --> 1272.00]  to encapsulate.
[1272.70 --> 1272.94]  But,
[1273.10 --> 1273.60]  essentially,
[1273.72 --> 1273.86]  like,
[1273.90 --> 1274.96]  you don't even need to have
[1274.96 --> 1275.94]  any kind of composition,
[1276.22 --> 1276.72]  I think,
[1277.14 --> 1278.36]  to be able to encapsulate
[1278.36 --> 1278.98]  information.
[1279.10 --> 1280.06]  It is useful,
[1280.30 --> 1281.34]  but the combination
[1281.34 --> 1282.58]  of information
[1282.58 --> 1283.20]  can be,
[1283.26 --> 1283.56]  you know,
[1283.62 --> 1284.64]  across a lot of things.
[1284.96 --> 1285.88]  We know this because
[1285.88 --> 1287.22]  we have distributed systems.
[1287.84 --> 1288.62]  I feel like
[1288.62 --> 1289.66]  we live in a world
[1289.66 --> 1290.82]  where everything is distributed,
[1290.96 --> 1291.06]  like,
[1291.14 --> 1291.80]  all of our data
[1291.80 --> 1291.98]  is,
[1292.06 --> 1292.14]  like,
[1292.16 --> 1292.52]  everywhere.
[1293.02 --> 1294.02]  And we kind of need
[1294.02 --> 1294.90]  to aggregate it.
[1295.16 --> 1295.50]  So,
[1295.70 --> 1296.46]  even a composition
[1296.46 --> 1297.78]  is sort of nice to have,
[1297.88 --> 1298.54]  something that we're
[1298.54 --> 1299.58]  very used to when we do,
[1300.10 --> 1301.42]  but we don't actually
[1301.42 --> 1302.56]  need to have it.
[1302.88 --> 1303.12]  So,
[1303.28 --> 1304.60]  if we have encapsulation,
[1304.92 --> 1306.54]  which I think we do in Go,
[1307.12 --> 1308.58]  and we are able to
[1308.58 --> 1309.82]  define abstractions,
[1310.00 --> 1311.04]  which we have
[1311.04 --> 1311.94]  interfaces for.
[1312.48 --> 1312.66]  And,
[1312.66 --> 1313.26]  by the way,
[1313.34 --> 1314.32]  there is a case,
[1314.32 --> 1314.92]  so,
[1315.58 --> 1316.34]  it's kind of interesting
[1316.34 --> 1317.84]  as I found a code snippet
[1317.84 --> 1318.84]  that was exactly
[1318.84 --> 1319.46]  what I needed
[1319.46 --> 1321.12]  for this workshop
[1321.12 --> 1322.38]  at the time,
[1322.54 --> 1323.86]  it was the C++ code.
[1324.00 --> 1324.64]  I really loved
[1324.64 --> 1326.34]  because it starts
[1326.34 --> 1327.22]  with a license
[1327.22 --> 1328.12]  that do whatever
[1328.12 --> 1328.92]  the hell you want
[1328.92 --> 1329.56]  with this code
[1329.56 --> 1331.04]  as long as you don't blame me.
[1331.04 --> 1333.62]  And then this code,
[1333.62 --> 1335.26]  that it's an event
[1335.26 --> 1336.34]  that you can register
[1336.34 --> 1337.22]  listeners to,
[1337.70 --> 1339.18]  regardless of the type.
[1339.40 --> 1339.96]  So, essentially,
[1340.22 --> 1341.62]  it works with templates
[1341.62 --> 1342.58]  or generics.
[1342.90 --> 1343.38]  So,
[1343.46 --> 1344.24]  that code
[1344.24 --> 1345.64]  uses generics
[1345.64 --> 1346.84]  for a case
[1346.84 --> 1347.80]  that we don't need.
[1348.36 --> 1349.40]  When we write
[1349.40 --> 1350.00]  this code
[1350.00 --> 1351.56]  in C++,
[1351.82 --> 1352.60]  we have to have,
[1352.70 --> 1353.52]  we have to use
[1353.52 --> 1354.68]  this kind of code
[1354.68 --> 1355.38]  with templates
[1355.38 --> 1356.82]  to plug in something
[1356.82 --> 1357.78]  into something else,
[1357.78 --> 1359.08]  to even be able
[1359.08 --> 1359.76]  to do that,
[1359.82 --> 1360.64]  to just plug in
[1360.64 --> 1361.38]  some functionality
[1361.38 --> 1362.32]  into something else
[1362.32 --> 1363.34]  that it's not aware of.
[1363.44 --> 1363.62]  Again,
[1363.72 --> 1364.64]  because interfaces,
[1365.24 --> 1365.38]  well,
[1365.50 --> 1367.00]  C++ doesn't have interfaces.
[1367.22 --> 1368.06]  It has classes
[1368.06 --> 1369.52]  where you can define
[1369.52 --> 1370.84]  functions as pure virtual,
[1371.44 --> 1372.20]  so it doesn't have
[1372.20 --> 1373.48]  to have all the implementation.
[1374.36 --> 1374.84]  But,
[1375.08 --> 1376.80]  whatever object you have,
[1376.84 --> 1377.76]  you cannot pass in
[1377.76 --> 1378.30]  as another
[1378.30 --> 1379.62]  unless it implements,
[1380.08 --> 1381.40]  it extends
[1381.40 --> 1382.72]  or is essentially
[1382.72 --> 1384.04]  a class.
[1384.62 --> 1385.62]  But in this case,
[1385.62 --> 1387.18]  you define your own
[1387.18 --> 1388.84]  event handler,
[1389.08 --> 1389.52]  obviously,
[1389.66 --> 1390.54]  nobody knows,
[1390.98 --> 1391.54]  you can't really
[1391.54 --> 1392.42]  pass in
[1392.42 --> 1393.66]  or use in this code
[1393.66 --> 1394.40]  any class
[1394.40 --> 1394.74]  that you didn't
[1394.74 --> 1395.44]  write yourself.
[1395.96 --> 1396.38]  So,
[1396.46 --> 1397.16]  you get stuck
[1397.16 --> 1398.18]  and this is why
[1398.18 --> 1399.34]  you use generics
[1399.34 --> 1400.42]  in many,
[1400.52 --> 1401.08]  many languages.
[1401.42 --> 1402.24]  It's for this case
[1402.24 --> 1403.46]  and that was why
[1403.46 --> 1404.36]  for many,
[1404.50 --> 1405.04]  many years
[1405.04 --> 1405.96]  people would say,
[1406.08 --> 1406.12]  well,
[1406.16 --> 1406.66]  why do you need
[1406.66 --> 1407.26]  interfaces?
[1407.74 --> 1408.30]  Why do you need
[1408.30 --> 1409.06]  generics when you
[1409.06 --> 1409.78]  have interfaces?
[1410.26 --> 1411.14]  But the truth is
[1411.14 --> 1411.84]  that you do need
[1411.84 --> 1413.08]  generics for the cases
[1413.08 --> 1414.84]  where the behavior
[1414.84 --> 1416.26]  of the class
[1416.26 --> 1417.00]  is derived
[1417.00 --> 1419.04]  by the type.
[1419.70 --> 1419.88]  So,
[1420.10 --> 1420.70]  for instance,
[1421.20 --> 1422.68]  next node
[1422.68 --> 1424.12]  in a linked list.
[1424.76 --> 1424.92]  So,
[1425.42 --> 1426.22]  the next is going
[1426.22 --> 1426.76]  to return
[1426.76 --> 1427.58]  the same type
[1427.58 --> 1428.00]  of node
[1428.00 --> 1428.74]  and if your node
[1428.74 --> 1429.20]  is holding
[1429.20 --> 1429.72]  an integer
[1429.72 --> 1430.46]  or a float
[1430.46 --> 1431.04]  or whatever
[1431.04 --> 1432.08]  type of value,
[1432.32 --> 1432.92]  it's going
[1432.92 --> 1433.90]  to be different.
[1434.42 --> 1435.20]  A repository
[1435.20 --> 1436.00]  that stores
[1436.00 --> 1437.16]  any kind of model.
[1437.70 --> 1438.22]  A map
[1438.22 --> 1439.18]  with a key
[1439.18 --> 1440.26]  value.
[1440.38 --> 1440.98]  By the way,
[1441.48 --> 1442.42]  go always
[1442.42 --> 1443.28]  hot generics.
[1443.28 --> 1443.88]  Actually,
[1443.98 --> 1444.56]  that would be
[1444.56 --> 1445.90]  my unpopular
[1445.90 --> 1446.34]  opinion.
[1446.80 --> 1447.24]  Go always
[1447.24 --> 1447.94]  hot generics
[1447.94 --> 1448.94]  because map
[1448.94 --> 1449.82]  is a generic
[1449.82 --> 1450.20]  type.
[1450.86 --> 1451.26]  It maps
[1451.26 --> 1452.20]  from a key
[1452.20 --> 1453.56]  that is a generic
[1453.56 --> 1455.30]  type to a value
[1455.30 --> 1456.06]  that is a generic
[1456.06 --> 1456.46]  type.
[1456.88 --> 1457.40]  I see you're
[1457.40 --> 1458.38]  sipping your drink
[1458.38 --> 1458.62]  again,
[1458.70 --> 1459.06]  so I know
[1459.06 --> 1459.66]  that you disagree.
[1460.70 --> 1460.96]  No,
[1461.08 --> 1462.18]  I 100% agree.
[1462.68 --> 1462.84]  Oh,
[1462.86 --> 1463.18]  you do?
[1463.36 --> 1463.52]  Okay.
[1464.12 --> 1464.82]  The slices
[1464.82 --> 1465.92]  were always
[1465.92 --> 1466.36]  generic.
[1466.72 --> 1467.44]  We just couldn't
[1467.44 --> 1468.40]  define our own,
[1468.54 --> 1469.28]  so it was like
[1469.28 --> 1470.52]  good for the 80%
[1470.52 --> 1471.22]  of the use
[1471.22 --> 1471.58]  cases,
[1471.68 --> 1472.22]  but then we
[1472.22 --> 1472.94]  had our own
[1472.94 --> 1473.70]  cases that we
[1473.70 --> 1474.18]  needed it,
[1474.50 --> 1474.92]  and we just
[1474.92 --> 1475.32]  didn't have
[1475.32 --> 1475.68]  anything.
[1476.14 --> 1476.86]  So you will
[1476.86 --> 1477.40]  talk now,
[1477.46 --> 1477.86]  and I will
[1477.86 --> 1478.46]  sip a drink.
[1480.10 --> 1480.50]  No,
[1480.58 --> 1481.12]  I definitely
[1481.12 --> 1481.58]  agree with you
[1481.58 --> 1482.54]  that the maps
[1482.54 --> 1483.10]  and the slices
[1483.10 --> 1484.62]  are generic.
[1484.74 --> 1485.42]  They've literally
[1485.42 --> 1486.14]  since day one,
[1486.86 --> 1487.26]  and like you
[1487.26 --> 1487.38]  said,
[1487.40 --> 1487.94]  it is like that
[1487.94 --> 1488.90]  80% use case,
[1488.96 --> 1489.12]  right?
[1489.50 --> 1489.80]  I don't know
[1489.80 --> 1490.28]  how to tie this
[1490.28 --> 1491.70]  back to OOP
[1491.70 --> 1492.38]  stuff now.
[1492.62 --> 1492.74]  No,
[1492.80 --> 1494.24]  because why I
[1494.24 --> 1495.02]  think it plays
[1495.02 --> 1496.00]  a role in this
[1496.00 --> 1497.30]  is because what
[1497.30 --> 1498.90]  people did in
[1498.90 --> 1499.66]  those cases
[1499.66 --> 1500.52]  is they would
[1500.52 --> 1501.88]  write a lot
[1501.88 --> 1502.36]  of functional
[1502.36 --> 1503.06]  code,
[1503.76 --> 1505.02]  procedural code,
[1505.34 --> 1505.74]  et cetera,
[1506.22 --> 1507.64]  and did not
[1507.64 --> 1508.92]  use necessarily
[1508.92 --> 1510.92]  generic types.
[1511.54 --> 1512.56]  I think we've
[1512.56 --> 1513.26]  had a lot of
[1513.26 --> 1514.02]  workarounds.
[1515.08 --> 1515.66]  I think now
[1515.66 --> 1516.88]  we can eliminate
[1516.88 --> 1517.14]  them.
[1517.24 --> 1517.70]  I think the
[1517.70 --> 1518.76]  language is very
[1518.76 --> 1519.84]  mature to be
[1519.84 --> 1520.54]  object-oriented.
[1521.00 --> 1521.20]  No,
[1521.26 --> 1521.70]  that makes sense
[1521.70 --> 1522.00]  to me.
[1522.26 --> 1522.74]  Natalie,
[1523.22 --> 1524.00]  can you hear me?
[1524.14 --> 1524.46]  No.
[1524.86 --> 1525.58]  One thing is on
[1525.58 --> 1525.94]  Zoom call,
[1526.04 --> 1526.56]  another thing is
[1526.56 --> 1527.26]  on a podcast.
[1528.00 --> 1528.34]  It's a whole
[1528.34 --> 1528.72]  new level.
[1528.90 --> 1530.10]  I found a
[1530.10 --> 1530.66]  quote from
[1530.66 --> 1531.20]  Rob Pike
[1531.20 --> 1532.50]  about Go
[1532.50 --> 1534.24]  being yes
[1534.24 --> 1534.76]  or no
[1534.76 --> 1536.22]  object-oriented.
[1536.70 --> 1537.60]  So it's a
[1537.60 --> 1538.22]  bit of a
[1538.22 --> 1538.88]  thread.
[1539.36 --> 1539.94]  So it starts
[1539.94 --> 1540.46]  with whenever
[1540.46 --> 1541.08]  someone from
[1541.08 --> 1541.52]  Java or
[1541.52 --> 1542.20]  C++ or
[1542.20 --> 1542.68]  C Sharp
[1542.68 --> 1544.82]  comes to
[1544.82 --> 1545.02]  Go,
[1545.16 --> 1545.58]  they look for
[1545.58 --> 1545.94]  class,
[1546.06 --> 1546.54]  find struct
[1546.54 --> 1547.00]  and stop
[1547.00 --> 1547.44]  looking.
[1547.84 --> 1548.26]  But this
[1548.26 --> 1548.78]  misses two
[1548.78 --> 1549.38]  fundamental
[1549.38 --> 1549.92]  differences
[1549.92 --> 1550.54]  between Go
[1550.54 --> 1551.54]  and traditional
[1551.54 --> 1552.50]  object-oriented
[1552.50 --> 1552.98]  languages.
[1553.58 --> 1554.18]  The first
[1554.18 --> 1554.70]  one is that
[1554.70 --> 1555.04]  it's not
[1555.04 --> 1555.84]  only structs.
[1556.06 --> 1556.74]  Any concrete
[1556.74 --> 1557.66]  type can have
[1557.66 --> 1558.24]  methods.
[1558.24 --> 1558.88]  integers,
[1559.18 --> 1559.48]  balls,
[1559.74 --> 1560.06]  slices,
[1560.28 --> 1560.88]  even funks.
[1561.32 --> 1561.94]  But the
[1561.94 --> 1562.64]  more important
[1562.64 --> 1563.86]  idea is the
[1563.86 --> 1564.42]  separation of
[1564.42 --> 1564.84]  concepts.
[1564.98 --> 1565.40]  Data and
[1565.40 --> 1566.00]  behavior are
[1566.00 --> 1566.84]  two distinct
[1566.84 --> 1567.42]  concepts of
[1567.42 --> 1567.64]  Go,
[1568.14 --> 1568.84]  not conflated
[1568.84 --> 1569.44]  into a single
[1569.44 --> 1569.98]  notion of
[1569.98 --> 1570.42]  class.
[1570.82 --> 1571.88]  This is the
[1571.88 --> 1572.58]  insight which
[1572.58 --> 1573.18]  goes all the
[1573.18 --> 1573.70]  way back to
[1573.70 --> 1574.70]  small talk on
[1574.70 --> 1575.50]  which the
[1575.50 --> 1576.32]  object-oriented
[1576.32 --> 1577.10]  type system,
[1577.24 --> 1577.76]  including the
[1577.76 --> 1578.46]  interface model,
[1578.58 --> 1578.98]  is built.
[1579.40 --> 1579.70]  So stopping
[1579.70 --> 1580.30]  at struct
[1580.30 --> 1581.52]  equals equals
[1581.52 --> 1582.58]  class misses
[1582.58 --> 1583.86]  much of what
[1583.86 --> 1584.50]  makes Go
[1584.50 --> 1584.94]  work.
[1584.94 --> 1585.66]  So what
[1585.66 --> 1585.88]  are your
[1585.88 --> 1586.20]  thoughts?
[1586.60 --> 1587.18]  I agree.
[1587.78 --> 1588.38]  It sort of
[1588.38 --> 1589.00]  works very
[1589.00 --> 1589.46]  well with
[1589.46 --> 1590.10]  everything that
[1590.10 --> 1591.02]  I learned
[1591.02 --> 1592.14]  recently about
[1592.14 --> 1592.52]  this.
[1592.74 --> 1593.12]  Honestly,
[1593.58 --> 1594.80]  it feels like
[1594.80 --> 1595.72]  Go is more
[1595.72 --> 1597.24]  naturally object-oriented
[1597.24 --> 1599.16]  than languages
[1599.16 --> 1600.00]  that I worked
[1600.00 --> 1601.38]  with before.
[1601.96 --> 1602.42]  I had this
[1602.42 --> 1603.06]  discussion with
[1603.06 --> 1603.66]  my boyfriend
[1603.66 --> 1604.52]  because of the
[1604.52 --> 1605.42]  workshop and the
[1605.42 --> 1605.76]  amount of
[1605.76 --> 1606.64]  resistance that I
[1606.64 --> 1607.12]  was getting.
[1607.50 --> 1608.14]  Does he think
[1608.14 --> 1610.00]  Go is object-oriented?
[1610.36 --> 1610.66]  Yes.
[1611.04 --> 1611.86]  So his answer
[1611.86 --> 1612.64]  was, of course
[1612.64 --> 1613.06]  it is.
[1613.62 --> 1614.88]  It wasn't even a
[1614.88 --> 1615.58]  question in his
[1615.58 --> 1615.78]  mind.
[1616.24 --> 1616.76]  And then he
[1616.76 --> 1617.42]  told me, well,
[1617.48 --> 1618.18]  you know how the
[1618.18 --> 1618.94]  JavaScript people
[1618.94 --> 1620.00]  say that a
[1620.00 --> 1621.30]  prototype is the
[1621.30 --> 1622.04]  best way to
[1622.04 --> 1623.58]  define object-oriented.
[1623.94 --> 1624.88]  And my takeaway
[1624.88 --> 1625.98]  from this is that
[1625.98 --> 1627.12]  every night I go
[1627.12 --> 1628.08]  to sleep next to
[1628.08 --> 1628.84]  a man who
[1628.84 --> 1629.48]  quotes the
[1629.48 --> 1630.32]  JavaScript people.
[1632.32 --> 1633.04]  That's it.
[1633.84 --> 1634.84]  I thought it was
[1634.84 --> 1635.58]  a pretty cool
[1635.58 --> 1636.48]  observation, to be
[1636.48 --> 1637.18]  honest, but
[1637.18 --> 1638.76]  still concerning.
[1638.76 --> 1640.38]  I'll keep you
[1640.38 --> 1640.78]  posted.
[1642.48 --> 1643.70]  The quote
[1643.70 --> 1644.30]  there where it
[1644.30 --> 1645.48]  says it
[1645.48 --> 1646.66]  separates the
[1646.66 --> 1647.58]  idea of data
[1647.58 --> 1648.36]  and behavior, I
[1648.36 --> 1648.68]  think that's
[1648.68 --> 1649.34]  the important
[1649.34 --> 1649.92]  part of that
[1649.92 --> 1650.30]  area.
[1650.74 --> 1651.24]  But I'm having
[1651.24 --> 1652.08]  a hard time
[1652.08 --> 1652.72]  articulating
[1652.72 --> 1654.74]  exactly why in
[1654.74 --> 1655.16]  my head.
[1655.50 --> 1656.06]  You think that
[1656.06 --> 1656.72]  that is a good
[1656.72 --> 1657.84]  way to express
[1657.84 --> 1658.90]  object-oriented?
[1659.42 --> 1660.18]  Yeah, I do.
[1660.36 --> 1661.12]  Extracting away
[1661.12 --> 1662.36]  the data from
[1662.36 --> 1663.38]  the functionality?
[1663.80 --> 1664.46]  Yeah, I think
[1664.46 --> 1665.42]  going to what
[1665.42 --> 1665.84]  you're saying
[1665.84 --> 1666.66]  where Go is
[1666.66 --> 1667.50]  almost a more
[1667.50 --> 1668.70]  pure version of
[1668.70 --> 1669.56]  object-orientation.
[1669.64 --> 1670.22]  I think that's
[1670.22 --> 1671.24]  what leads to
[1671.24 --> 1671.56]  it, right?
[1671.62 --> 1672.42]  The idea that,
[1672.92 --> 1673.26]  I don't know,
[1673.32 --> 1673.70]  I'd have to
[1673.70 --> 1674.16]  really sit down
[1674.16 --> 1674.64]  and think about
[1674.64 --> 1675.68]  it, but that's
[1675.68 --> 1676.36]  where my mind
[1676.36 --> 1676.80]  is going.
[1677.08 --> 1678.12]  I think that I
[1678.12 --> 1680.10]  found something
[1680.10 --> 1681.80]  that the person
[1681.80 --> 1683.46]  that wrote me
[1683.46 --> 1684.68]  about Go not
[1684.68 --> 1685.62]  being object-oriented
[1685.62 --> 1687.42]  language might be
[1687.42 --> 1688.48]  related to.
[1689.04 --> 1689.98]  So I searched
[1689.98 --> 1690.72]  for Ron Pike
[1690.72 --> 1691.42]  in object-oriented
[1691.42 --> 1692.22]  and I found
[1692.22 --> 1692.74]  Wikipedia.
[1693.96 --> 1695.02]  And Wikipedia,
[1695.52 --> 1696.50]  he is
[1696.50 --> 1697.26]  criticizing
[1697.26 --> 1698.56]  object-oriented.
[1699.12 --> 1700.18]  So it's
[1700.18 --> 1700.86]  possible that
[1700.86 --> 1701.76]  that was what
[1701.76 --> 1702.78]  that quote
[1702.78 --> 1703.50]  was about.
[1703.84 --> 1704.30]  If you want to
[1704.30 --> 1704.86]  read this out
[1704.86 --> 1705.96]  and share this
[1705.96 --> 1706.64]  later in our
[1706.64 --> 1707.32]  show notes,
[1707.40 --> 1708.18]  everybody can go
[1708.18 --> 1708.86]  back to this
[1708.86 --> 1709.06]  too.
[1709.48 --> 1710.34]  Yeah, I think
[1710.34 --> 1710.84]  it's funny.
[1711.98 --> 1712.80]  I mean,
[1712.94 --> 1713.46]  clearly,
[1714.06 --> 1714.90]  yes, I will
[1714.90 --> 1715.70]  send it to you
[1715.70 --> 1716.94]  and we can
[1716.94 --> 1717.58]  include that.
[1718.06 --> 1719.56]  So he criticized
[1719.56 --> 1720.54]  object-oriented
[1720.54 --> 1721.24]  for being
[1721.24 --> 1722.30]  incredibly heavy,
[1722.92 --> 1723.38]  I guess.
[1723.38 --> 1724.08]  and that
[1724.08 --> 1724.80]  sort of
[1724.80 --> 1725.60]  works pretty
[1725.60 --> 1726.08]  well with
[1726.08 --> 1726.78]  those quotes
[1726.78 --> 1727.94]  about objects
[1727.94 --> 1728.84]  being lightweight
[1728.84 --> 1729.58]  and go,
[1730.02 --> 1730.96]  I think I agree.
[1731.46 --> 1731.98]  I think it
[1731.98 --> 1732.60]  feels very,
[1732.70 --> 1733.30]  very natural.
[1733.72 --> 1734.14]  By the way,
[1734.20 --> 1734.76]  something that
[1734.76 --> 1735.72]  I really love
[1735.72 --> 1737.42]  is we don't
[1737.42 --> 1738.92]  have enumerators,
[1739.12 --> 1739.62]  but we do
[1739.62 --> 1740.12]  have,
[1740.46 --> 1740.72]  like,
[1741.18 --> 1742.36]  it's very
[1742.36 --> 1743.40]  easy for me
[1743.40 --> 1743.90]  to,
[1744.36 --> 1744.82]  when I look
[1744.82 --> 1745.70]  at pseudocode
[1745.70 --> 1746.16]  with those
[1746.16 --> 1746.84]  red-black
[1746.84 --> 1748.72]  trees and,
[1748.78 --> 1749.24]  you know,
[1749.38 --> 1751.48]  coloring nodes
[1751.48 --> 1752.06]  in a graph
[1752.06 --> 1752.46]  and stuff
[1752.46 --> 1752.94]  like that.
[1753.28 --> 1753.76]  This is
[1753.76 --> 1754.44]  kind of stuff
[1754.44 --> 1755.12]  that I teach
[1755.12 --> 1755.62]  to people
[1755.62 --> 1756.24]  who don't
[1756.24 --> 1756.90]  have the,
[1757.80 --> 1758.18]  let's say,
[1758.22 --> 1758.70]  the classical
[1758.70 --> 1759.24]  background
[1759.24 --> 1760.14]  in the university
[1760.14 --> 1761.90]  and I teach
[1761.90 --> 1762.52]  that stuff
[1762.52 --> 1763.84]  to people
[1763.84 --> 1764.46]  because
[1764.46 --> 1766.14]  they need
[1766.14 --> 1767.36]  to pass
[1767.36 --> 1768.58]  interviews.
[1769.30 --> 1769.48]  So,
[1769.76 --> 1770.84]  unfortunately,
[1771.46 --> 1773.04]  this is where
[1773.04 --> 1773.60]  this is coming
[1773.60 --> 1773.92]  from.
[1774.28 --> 1774.76]  But what I
[1774.76 --> 1775.58]  really like
[1775.58 --> 1776.02]  to do,
[1776.12 --> 1776.56]  because I
[1776.56 --> 1777.30]  don't,
[1777.74 --> 1778.30]  I can't
[1778.30 --> 1778.88]  code those,
[1779.20 --> 1779.86]  so I take
[1779.86 --> 1780.56]  pseudocode
[1780.56 --> 1781.54]  with white,
[1781.76 --> 1782.20]  black,
[1782.44 --> 1782.76]  gray,
[1782.92 --> 1783.30]  whatever,
[1783.58 --> 1784.40]  red colors.
[1784.94 --> 1785.76]  I define a
[1785.76 --> 1786.78]  color that is,
[1787.24 --> 1787.48]  that,
[1787.68 --> 1788.36]  I don't define
[1788.36 --> 1788.90]  a new type
[1788.90 --> 1789.46]  of alias
[1789.46 --> 1789.98]  integers
[1789.98 --> 1791.40]  to do that
[1791.40 --> 1791.84]  and I get
[1791.84 --> 1792.16]  very,
[1792.30 --> 1793.06]  very expressive
[1793.06 --> 1794.52]  and basically
[1794.52 --> 1795.62]  write pseudocode
[1795.62 --> 1795.98]  and go.
[1796.76 --> 1797.76]  And I don't
[1797.76 --> 1798.28]  think that you
[1798.28 --> 1798.96]  could do that
[1798.96 --> 1801.04]  with a non-object
[1801.04 --> 1801.80]  oriented language.
[1801.96 --> 1802.84]  I can pretty
[1802.84 --> 1803.52]  much express
[1803.52 --> 1804.44]  any pseudocode
[1804.44 --> 1805.16]  that I see
[1805.16 --> 1806.24]  without actually
[1806.24 --> 1806.84]  giving much
[1806.84 --> 1807.56]  thought to
[1807.56 --> 1808.16]  what is written
[1808.16 --> 1808.44]  there.
[1808.58 --> 1808.86]  I just
[1808.86 --> 1810.14]  essentially copy
[1810.14 --> 1810.70]  and paste it
[1810.70 --> 1811.00]  and make
[1811.00 --> 1811.36]  the code
[1811.36 --> 1811.72]  work.
[1812.48 --> 1812.72]  Like,
[1812.80 --> 1813.14]  I just
[1813.14 --> 1813.54]  make the
[1813.54 --> 1814.32]  types work
[1814.32 --> 1814.82]  and the
[1814.82 --> 1815.20]  functions
[1815.20 --> 1815.96]  work and
[1815.96 --> 1816.42]  if the
[1816.42 --> 1816.74]  function
[1816.74 --> 1817.32]  happens to
[1817.32 --> 1817.84]  be a method,
[1818.02 --> 1818.50]  that's what's
[1818.50 --> 1819.10]  going to be.
[1819.68 --> 1820.48]  And if the
[1820.48 --> 1821.28]  function happens
[1821.28 --> 1821.78]  to be a
[1821.78 --> 1822.08]  procedural
[1822.08 --> 1822.62]  function,
[1822.80 --> 1823.18]  that's what
[1823.18 --> 1823.48]  it's going
[1823.48 --> 1824.02]  to be and
[1824.02 --> 1824.34]  just,
[1824.48 --> 1824.64]  you know,
[1824.68 --> 1825.08]  make it
[1825.08 --> 1825.40]  work,
[1825.88 --> 1827.00]  whatever is
[1827.00 --> 1827.82]  necessary.
[1827.96 --> 1828.22]  I don't
[1828.22 --> 1828.54]  think I
[1828.54 --> 1828.80]  would have
[1828.80 --> 1829.26]  been able
[1829.26 --> 1829.68]  to do
[1829.68 --> 1830.44]  that if
[1830.44 --> 1830.86]  Go was
[1830.86 --> 1831.54]  not object
[1831.54 --> 1831.94]  oriented.
[1832.46 --> 1832.86]  Also,
[1833.14 --> 1833.58]  you should
[1833.58 --> 1834.06]  not be
[1834.06 --> 1834.88]  testing people
[1834.88 --> 1835.36]  in red,
[1835.44 --> 1836.22]  black trees.
[1836.22 --> 1839.14]  I definitely
[1839.14 --> 1839.76]  could not
[1839.76 --> 1840.34]  code up a
[1840.34 --> 1840.46]  red,
[1840.52 --> 1840.88]  black tree
[1840.88 --> 1841.68]  without
[1841.68 --> 1842.56]  Googling
[1842.56 --> 1842.84]  something
[1842.84 --> 1843.24]  right now.
[1843.36 --> 1843.54]  Yeah,
[1843.58 --> 1844.06]  obviously.
[1844.60 --> 1844.74]  No,
[1844.84 --> 1845.54]  I still do
[1845.54 --> 1846.36]  these exercises
[1846.36 --> 1846.92]  with people
[1846.92 --> 1847.44]  so they get
[1847.44 --> 1847.94]  used to the
[1847.94 --> 1848.52]  idea and
[1848.52 --> 1848.80]  then if
[1848.80 --> 1849.08]  they can
[1849.08 --> 1849.54]  do this,
[1849.60 --> 1849.82]  they can
[1849.82 --> 1850.44]  do anything,
[1850.62 --> 1851.00]  stuff like
[1851.00 --> 1851.30]  that,
[1851.42 --> 1851.80]  essentially.
[1852.46 --> 1852.76]  But yeah,
[1852.80 --> 1853.24]  there are way
[1853.24 --> 1853.68]  too many
[1853.68 --> 1854.22]  edge cases
[1854.22 --> 1854.56]  in the
[1854.56 --> 1854.70]  red,
[1854.78 --> 1855.20]  black tree.
[1855.96 --> 1856.40]  Okay.
[1857.98 --> 1858.70]  Somebody should
[1858.70 --> 1859.72]  simplify this.
[1859.92 --> 1860.42]  Someone should
[1860.42 --> 1860.72]  write a
[1860.72 --> 1861.18]  library,
[1861.54 --> 1862.06]  generic library
[1862.06 --> 1862.62]  for it once
[1862.62 --> 1863.14]  and then never
[1863.14 --> 1863.72]  touch it again.
[1863.72 --> 1865.46]  That sounds
[1865.46 --> 1865.90]  very good.
[1866.00 --> 1866.72]  So let's rant
[1866.72 --> 1867.42]  about people
[1867.42 --> 1868.44]  who give
[1868.44 --> 1869.62]  impossible tests
[1869.62 --> 1871.52]  to complete
[1871.52 --> 1872.14]  beginners in
[1872.14 --> 1872.42]  coding.
[1872.94 --> 1873.78]  Or tell us
[1873.78 --> 1874.24]  how you do
[1874.24 --> 1874.70]  this right
[1874.70 --> 1875.30]  when you're
[1875.30 --> 1875.78]  hiring for
[1875.78 --> 1876.16]  your team.
[1876.66 --> 1877.68]  So I don't
[1877.68 --> 1878.16]  know that I
[1878.16 --> 1878.70]  do this right.
[1878.92 --> 1879.38]  Let's start
[1879.38 --> 1879.76]  with that.
[1880.04 --> 1880.74]  But I try
[1880.74 --> 1881.32]  to decide
[1881.32 --> 1882.06]  what I want
[1882.06 --> 1883.28]  and then I
[1883.28 --> 1883.82]  don't test
[1883.82 --> 1884.38]  people and
[1884.38 --> 1884.90]  stuff that I
[1884.90 --> 1885.28]  don't want.
[1885.40 --> 1885.96]  So what I
[1885.96 --> 1886.62]  will do,
[1886.78 --> 1887.24]  for instance,
[1887.34 --> 1887.88]  like if I
[1887.88 --> 1888.34]  care,
[1889.02 --> 1889.46]  if I want
[1889.46 --> 1890.06]  to know how
[1890.06 --> 1891.00]  thorough somebody
[1891.00 --> 1891.54]  is going to
[1891.54 --> 1891.82]  be,
[1891.98 --> 1892.80]  that I
[1892.80 --> 1893.70]  will dive
[1893.70 --> 1894.58]  with them
[1894.58 --> 1895.02]  on something
[1895.02 --> 1895.34]  that they
[1895.34 --> 1895.82]  do know
[1895.82 --> 1896.34]  and check
[1896.34 --> 1896.96]  how familiar
[1896.96 --> 1897.46]  they are
[1897.46 --> 1897.82]  with all
[1897.82 --> 1898.30]  the details.
[1899.38 --> 1900.56]  So if
[1900.56 --> 1901.46]  somebody tells
[1901.46 --> 1901.88]  me, I
[1901.88 --> 1902.12]  don't know,
[1902.14 --> 1902.50]  let's start
[1902.50 --> 1902.78]  with the
[1902.78 --> 1903.44]  very basics.
[1903.64 --> 1904.04]  If somebody
[1904.04 --> 1904.76]  tells me
[1904.76 --> 1905.92]  that they
[1905.92 --> 1906.82]  have worked
[1906.82 --> 1907.38]  with my
[1907.38 --> 1907.90]  SQL,
[1908.22 --> 1908.96]  then I
[1908.96 --> 1910.14]  will test
[1910.14 --> 1911.12]  them heavily
[1911.12 --> 1911.86]  on my
[1911.86 --> 1912.56]  SQL until
[1912.56 --> 1912.86]  I reach
[1912.86 --> 1913.54]  something that
[1913.54 --> 1914.42]  either they
[1914.42 --> 1914.94]  don't know
[1914.94 --> 1916.24]  or to get
[1916.24 --> 1917.04]  a sense of
[1917.04 --> 1917.76]  how far
[1917.76 --> 1918.46]  into the
[1918.46 --> 1918.96]  rabbit hole
[1918.96 --> 1919.52]  they went.
[1920.28 --> 1921.26]  Or any
[1921.26 --> 1921.66]  topic,
[1921.76 --> 1922.10]  any other
[1922.10 --> 1922.46]  topic.
[1922.46 --> 1923.22]  this one
[1923.22 --> 1923.72]  is kind
[1923.72 --> 1924.78]  of normal.
[1925.18 --> 1925.52]  But it
[1925.52 --> 1926.00]  all depends
[1926.00 --> 1926.28]  on the
[1926.28 --> 1926.78]  profile.
[1927.12 --> 1927.38]  It really
[1927.38 --> 1927.84]  all depends
[1927.84 --> 1928.10]  on the
[1928.10 --> 1928.38]  profile.
[1929.22 --> 1930.06]  So we
[1930.06 --> 1930.70]  said earlier
[1930.70 --> 1931.18]  that I
[1931.18 --> 1931.54]  am the
[1931.54 --> 1931.86]  sum of
[1931.86 --> 1931.96]  the
[1931.96 --> 1932.48]  opportunities
[1932.48 --> 1932.86]  that were
[1932.86 --> 1933.32]  given to
[1933.32 --> 1933.60]  me.
[1934.34 --> 1935.04]  And I
[1935.04 --> 1935.40]  don't think
[1935.40 --> 1935.80]  I'm a
[1935.80 --> 1936.50]  bad developer.
[1937.08 --> 1937.54]  We all
[1937.54 --> 1938.12]  want to
[1938.12 --> 1939.02]  hire somebody
[1939.02 --> 1939.56]  who cannot
[1939.56 --> 1940.08]  do what
[1940.08 --> 1940.72]  we can't
[1940.72 --> 1940.90]  do.
[1941.46 --> 1941.90]  Essentially,
[1942.24 --> 1942.72]  like I feel
[1942.72 --> 1943.08]  like we are
[1943.08 --> 1943.62]  raising the
[1943.62 --> 1944.50]  bar constantly
[1944.50 --> 1945.20]  to a level
[1945.20 --> 1945.58]  that people
[1945.58 --> 1946.36]  cannot actually
[1946.36 --> 1946.82]  meet.
[1947.28 --> 1948.04]  Not because
[1948.04 --> 1948.84]  they're not
[1948.84 --> 1949.44]  good enough.
[1949.44 --> 1950.58]  So for
[1950.58 --> 1950.86]  instance,
[1950.86 --> 1951.32]  if I
[1951.32 --> 1951.80]  can't do
[1951.80 --> 1952.50]  something and
[1952.50 --> 1952.92]  I am going
[1952.92 --> 1953.50]  to search for
[1953.50 --> 1954.08]  somebody who
[1954.08 --> 1954.46]  is going
[1954.46 --> 1956.24]  to be able
[1956.24 --> 1956.86]  to do it,
[1956.92 --> 1957.76]  that's a little
[1957.76 --> 1958.34]  bit unfair.
[1959.06 --> 1960.00]  And I feel
[1960.00 --> 1960.48]  like we are
[1960.48 --> 1961.00]  doing this
[1961.00 --> 1961.54]  all the time.
[1961.62 --> 1961.92]  We're sort
[1961.92 --> 1962.50]  of like raising
[1962.50 --> 1962.90]  the bar,
[1963.00 --> 1963.30]  raising the
[1963.30 --> 1963.46]  bar,
[1963.52 --> 1963.84]  raising the
[1963.84 --> 1964.16]  bar to
[1964.16 --> 1964.70]  essentially
[1964.70 --> 1966.22]  think maybe
[1966.22 --> 1967.12]  make up for
[1967.12 --> 1967.96]  our own
[1967.96 --> 1969.04]  disadvantages.
[1969.92 --> 1970.86]  So I
[1970.86 --> 1971.76]  try to
[1971.76 --> 1972.30]  not be
[1972.30 --> 1972.78]  unreasonable.
[1973.50 --> 1973.92]  When I
[1973.92 --> 1974.22]  interview
[1974.22 --> 1974.60]  somebody,
[1974.70 --> 1975.24]  I do think
[1975.24 --> 1975.64]  about,
[1976.28 --> 1977.02]  I do try
[1977.02 --> 1977.92]  to see if
[1977.92 --> 1978.32]  they can
[1978.32 --> 1979.80]  learn during
[1979.80 --> 1980.86]  the interview
[1980.86 --> 1981.60]  process,
[1981.70 --> 1982.04]  for instance.
[1982.22 --> 1983.16]  So I
[1983.16 --> 1983.82]  will present
[1983.82 --> 1984.22]  them with
[1984.22 --> 1985.66]  something that
[1985.66 --> 1985.96]  they will
[1985.96 --> 1986.60]  have to
[1986.60 --> 1987.60]  think about
[1987.60 --> 1988.74]  and sort
[1988.74 --> 1989.92]  of internalize
[1989.92 --> 1990.92]  and then
[1990.92 --> 1991.68]  spit out some
[1991.68 --> 1992.98]  information that
[1992.98 --> 1993.78]  could be wrong,
[1993.84 --> 1994.40]  could be right,
[1994.48 --> 1994.92]  but you know,
[1995.38 --> 1995.98]  it could be
[1995.98 --> 1996.70]  very small
[1996.70 --> 1997.34]  things that
[1997.34 --> 1998.22]  tell me if
[1998.22 --> 1998.86]  they get it.
[1999.50 --> 2000.20]  For instance,
[2000.74 --> 2001.46]  I work with
[2001.46 --> 2001.98]  billing.
[2002.42 --> 2003.02]  People are not
[2003.02 --> 2004.04]  necessarily familiar
[2004.04 --> 2004.80]  with those
[2004.80 --> 2005.36]  concepts,
[2005.36 --> 2006.60]  so I will
[2006.60 --> 2007.06]  introduce
[2007.06 --> 2008.02]  something that
[2008.02 --> 2008.80]  has something
[2008.80 --> 2009.36]  to do with
[2009.36 --> 2010.00]  what we do
[2010.00 --> 2010.54]  in the domain
[2010.54 --> 2011.80]  and it's
[2011.80 --> 2012.80]  fine that
[2012.80 --> 2013.16]  they don't
[2013.16 --> 2013.62]  know this
[2013.62 --> 2014.06]  and then I
[2014.06 --> 2014.68]  won't ask
[2014.68 --> 2014.86]  them,
[2014.98 --> 2015.38]  so how
[2015.38 --> 2016.12]  would you
[2016.12 --> 2016.58]  do it?
[2016.68 --> 2016.86]  Like,
[2016.94 --> 2017.50]  given those
[2017.50 --> 2018.18]  constraints,
[2018.82 --> 2019.20]  what would
[2019.20 --> 2019.56]  you do?
[2019.92 --> 2020.60]  So I taught
[2020.60 --> 2021.30]  them something
[2021.30 --> 2022.62]  and now I
[2022.62 --> 2023.34]  can see
[2023.34 --> 2024.20]  how they
[2024.20 --> 2024.94]  actually learn
[2024.94 --> 2025.92]  and what
[2025.92 --> 2026.42]  they actually
[2026.42 --> 2026.86]  do with
[2026.86 --> 2027.58]  this information
[2027.58 --> 2028.76]  and it's
[2028.76 --> 2029.22]  not really
[2029.22 --> 2030.04]  just problem
[2030.04 --> 2030.44]  solving,
[2030.76 --> 2031.20]  it's more
[2031.20 --> 2031.78]  of trying
[2031.78 --> 2032.28]  not to
[2032.28 --> 2032.64]  introduce
[2032.64 --> 2032.98]  them to
[2032.98 --> 2033.32]  problems
[2033.32 --> 2033.56]  that they
[2033.56 --> 2034.10]  already know,
[2034.54 --> 2034.92]  essentially.
[2034.92 --> 2036.74]  So it
[2036.74 --> 2037.00]  could be
[2037.00 --> 2037.28]  very,
[2037.38 --> 2037.90]  very small
[2037.90 --> 2038.34]  things.
[2039.34 --> 2039.48]  Yeah,
[2039.60 --> 2040.12]  so I am
[2040.12 --> 2040.56]  the sum of
[2040.56 --> 2041.08]  the opportunities
[2041.08 --> 2041.38]  that were
[2041.38 --> 2041.80]  given to
[2041.80 --> 2042.12]  me and
[2042.12 --> 2043.16]  I'm a
[2043.16 --> 2044.10]  huge believer
[2044.10 --> 2044.78]  that if you
[2044.78 --> 2045.20]  give people
[2045.20 --> 2045.80]  an opportunity
[2045.80 --> 2046.32]  they're not
[2046.32 --> 2046.72]  going to let
[2046.72 --> 2047.14]  you down,
[2047.54 --> 2048.36]  especially if
[2048.36 --> 2048.98]  they've been
[2048.98 --> 2049.90]  begging for
[2049.90 --> 2051.16]  work since
[2051.16 --> 2051.60]  forever.
[2052.34 --> 2053.12]  And I do
[2053.12 --> 2054.12]  think that you
[2054.12 --> 2054.80]  can bank on
[2054.80 --> 2055.56]  people's loyalty
[2055.56 --> 2056.86]  in those cases.
[2056.86 --> 2057.98]  I think for a lot
[2057.98 --> 2058.38]  of people,
[2059.18 --> 2060.00]  just having
[2060.00 --> 2061.24]  their foot in
[2061.24 --> 2062.50]  the door is
[2062.50 --> 2063.02]  such a big
[2063.02 --> 2063.54]  deal for
[2063.54 --> 2063.86]  them,
[2064.22 --> 2064.56]  that they
[2064.56 --> 2065.94]  will pay
[2065.94 --> 2066.64]  space.
[2067.22 --> 2068.38]  So I do
[2068.38 --> 2069.22]  see a lot
[2069.22 --> 2069.80]  of value
[2069.80 --> 2070.92]  in these
[2070.92 --> 2071.20]  people.
[2071.70 --> 2072.76]  And even
[2072.76 --> 2073.50]  now, if I
[2073.50 --> 2074.12]  go for a
[2074.12 --> 2074.76]  job interview,
[2075.12 --> 2076.56]  I am never
[2076.56 --> 2077.32]  going to apply
[2077.32 --> 2077.80]  for something
[2077.80 --> 2078.34]  that I already
[2078.34 --> 2078.62]  know.
[2078.72 --> 2079.24]  I want to
[2079.24 --> 2079.96]  grow just as
[2079.96 --> 2080.28]  much as
[2080.28 --> 2080.90]  everyone else.
[2080.98 --> 2081.30]  So I'm
[2081.30 --> 2081.86]  always going
[2081.86 --> 2083.54]  to go and
[2083.54 --> 2084.38]  try to
[2084.38 --> 2085.00]  convince somebody
[2085.00 --> 2085.58]  that they
[2085.58 --> 2086.00]  need to
[2086.00 --> 2086.48]  invest in
[2086.48 --> 2087.46]  my potential.
[2087.46 --> 2088.82]  I am
[2088.82 --> 2090.80]  very, very
[2090.80 --> 2093.50]  similar to
[2093.50 --> 2093.84]  a complete
[2093.84 --> 2095.24]  beginner because
[2095.24 --> 2096.06]  we all have
[2096.06 --> 2097.34]  to go around
[2097.34 --> 2098.32]  and essentially
[2098.32 --> 2099.12]  convince people
[2099.12 --> 2099.86]  to give us
[2099.86 --> 2101.34]  a chance to
[2101.34 --> 2102.00]  prove that we
[2102.00 --> 2102.36]  can do
[2102.36 --> 2103.16]  something that
[2103.16 --> 2104.40]  we have not
[2104.40 --> 2105.16]  shown before
[2105.16 --> 2105.72]  that we can
[2105.72 --> 2105.92]  do.
[2106.68 --> 2107.14]  It's so
[2107.14 --> 2107.68]  obvious to
[2107.68 --> 2108.16]  people that
[2108.16 --> 2108.48]  okay,
[2108.76 --> 2109.16]  Rona after
[2109.16 --> 2109.88]  20 years is
[2109.88 --> 2110.32]  going to be
[2110.32 --> 2110.80]  able to do
[2110.80 --> 2111.14]  this.
[2111.68 --> 2112.10]  But it
[2112.10 --> 2112.62]  shouldn't be,
[2112.92 --> 2113.18]  right?
[2113.44 --> 2113.84]  I mean, at
[2113.84 --> 2114.20]  the end of
[2114.20 --> 2114.68]  the day,
[2115.28 --> 2115.98]  it really
[2115.98 --> 2116.60]  shouldn't be.
[2116.60 --> 2117.60]  I fail just
[2117.60 --> 2118.06]  as much as
[2118.06 --> 2118.72]  everyone else.
[2119.10 --> 2119.52]  So that's
[2119.52 --> 2119.90]  why I go
[2119.90 --> 2120.34]  with it.
[2120.34 --> 2120.70]  It's a very
[2120.70 --> 2121.40]  long answer
[2121.40 --> 2121.70]  to your
[2121.70 --> 2121.98]  question,
[2122.10 --> 2122.30]  Loli.
[2133.56 --> 2134.54]  This episode
[2134.54 --> 2135.38]  is brought
[2135.38 --> 2135.74]  to you by
[2135.74 --> 2136.34]  our friends
[2136.34 --> 2136.98]  at Acuity,
[2137.26 --> 2137.76]  a new
[2137.76 --> 2138.38]  platform that
[2138.38 --> 2138.90]  brings fully
[2138.90 --> 2139.70]  managed Argo
[2139.70 --> 2140.60]  CD and
[2140.60 --> 2141.00]  enterprise
[2141.00 --> 2141.86]  services to
[2141.86 --> 2142.22]  the cloud
[2142.22 --> 2142.64]  or on
[2142.64 --> 2143.02]  premise.
[2143.58 --> 2143.80]  And I'm
[2143.80 --> 2144.02]  here with
[2144.02 --> 2144.34]  two of the
[2144.34 --> 2144.88]  co-founders
[2144.88 --> 2145.38]  from Acuity,
[2145.68 --> 2146.32]  Jesse Suin,
[2146.32 --> 2146.64]  and
[2146.64 --> 2147.24]  Alexander
[2147.24 --> 2148.24]  Matusenchev.
[2148.50 --> 2148.74]  So the
[2148.74 --> 2149.32]  Acuity platform
[2149.32 --> 2150.24]  is in
[2150.24 --> 2150.72]  beta right
[2150.72 --> 2151.06]  now.
[2151.32 --> 2151.58]  You guys
[2151.58 --> 2151.94]  have some
[2151.94 --> 2152.60]  big ideas
[2152.60 --> 2153.00]  you're executing
[2153.00 --> 2153.60]  on around
[2153.60 --> 2154.20]  Argo CD,
[2154.58 --> 2155.20]  managed Argo
[2155.20 --> 2155.56]  CD,
[2155.84 --> 2156.02]  Kubernetes
[2156.02 --> 2156.78]  native application
[2156.78 --> 2157.20]  delivery,
[2157.54 --> 2157.74]  and the
[2157.74 --> 2158.30]  power of
[2158.30 --> 2158.68]  GitOps.
[2158.74 --> 2158.96]  Help me
[2158.96 --> 2159.54]  understand the
[2159.54 --> 2159.96]  what and
[2159.96 --> 2160.52]  the why
[2160.52 --> 2161.00]  of what
[2161.00 --> 2161.20]  you're doing
[2161.20 --> 2161.62]  right now.
[2161.88 --> 2162.44]  So we
[2162.44 --> 2163.20]  started Acuity
[2163.20 --> 2164.28]  because we
[2164.28 --> 2165.10]  saw what was
[2165.10 --> 2165.88]  happening in
[2165.88 --> 2166.50]  the Kubernetes
[2166.50 --> 2167.02]  community,
[2167.26 --> 2167.84]  the challenges
[2167.84 --> 2168.32]  that people
[2168.32 --> 2168.90]  were facing
[2168.90 --> 2170.22]  about developer
[2170.22 --> 2170.96]  experience.
[2171.36 --> 2171.82]  And having
[2171.82 --> 2172.72]  run Argo
[2172.72 --> 2173.48]  CD for
[2173.48 --> 2174.18]  Intuit for
[2174.18 --> 2174.46]  a couple
[2174.46 --> 2174.78]  of years,
[2174.78 --> 2175.36]  we knew it
[2175.36 --> 2175.68]  took a
[2175.68 --> 2176.44]  small team
[2176.44 --> 2177.00]  to build
[2177.00 --> 2177.46]  this and
[2177.46 --> 2177.88]  scale it
[2177.88 --> 2178.36]  and provide
[2178.36 --> 2179.12]  a performance
[2179.12 --> 2180.16]  solution for
[2180.16 --> 2181.06]  the developers.
[2181.58 --> 2181.90]  And so
[2181.90 --> 2182.80]  at Acuity,
[2182.94 --> 2183.14]  in the
[2183.14 --> 2183.74]  Acuity platform,
[2183.92 --> 2184.14]  what we're
[2184.14 --> 2184.84]  trying to do
[2184.84 --> 2185.22]  is,
[2185.34 --> 2185.80]  the first thing
[2185.80 --> 2186.08]  we're trying
[2186.08 --> 2186.44]  to do is
[2186.44 --> 2187.48]  actually provide
[2187.48 --> 2188.22]  Argo CD
[2188.22 --> 2189.38]  as a fully
[2189.38 --> 2190.36]  managed solution
[2190.36 --> 2191.30]  to our users.
[2191.30 --> 2191.36]  developers.
[2191.66 --> 2192.36]  But that is
[2192.36 --> 2192.90]  just actually
[2192.90 --> 2193.42]  the start
[2193.42 --> 2193.82]  of things.
[2193.94 --> 2194.12]  And we
[2194.12 --> 2195.06]  actually want
[2195.06 --> 2195.88]  to take
[2195.88 --> 2196.34]  the next
[2196.34 --> 2197.36]  steps on
[2197.36 --> 2198.12]  improving
[2198.12 --> 2198.82]  the whole
[2198.82 --> 2199.42]  GitOps and
[2199.42 --> 2199.74]  developer
[2199.74 --> 2200.56]  experience and
[2200.56 --> 2201.48]  providing new
[2201.48 --> 2201.96]  tools and
[2201.96 --> 2203.32]  ecosystems around
[2203.32 --> 2204.10]  Argo and
[2204.10 --> 2204.34]  the Argo
[2204.34 --> 2204.76]  project.
[2205.10 --> 2205.28]  Yeah,
[2205.38 --> 2205.70]  that's right,
[2205.76 --> 2205.90]  JC.
[2206.08 --> 2206.80]  So Argo CD
[2206.80 --> 2207.34]  is just
[2207.34 --> 2207.74]  the beginning,
[2208.12 --> 2208.86]  but every
[2208.86 --> 2210.06]  company eventually
[2210.06 --> 2211.20]  needs way more
[2211.20 --> 2212.16]  tools integrated
[2212.16 --> 2212.78]  into the
[2212.78 --> 2213.50]  DevOps platform.
[2213.96 --> 2214.42]  And that's
[2214.42 --> 2214.78]  what we're
[2214.78 --> 2215.18]  hoping to
[2215.18 --> 2215.86]  deliver with
[2215.86 --> 2216.26]  Acuity
[2216.26 --> 2216.64]  platform.
[2217.14 --> 2217.50]  So we're
[2217.50 --> 2217.92]  hoping to
[2217.92 --> 2218.70]  provide a
[2218.70 --> 2219.14]  great user
[2219.14 --> 2219.96]  interface that
[2219.96 --> 2220.82]  enable developers
[2220.82 --> 2221.96]  to achieve
[2221.96 --> 2222.38]  what they
[2222.38 --> 2223.12]  need in a
[2223.12 --> 2223.46]  matter of
[2223.46 --> 2223.82]  just a few
[2223.82 --> 2224.12]  clicks.
[2224.58 --> 2224.94]  But we
[2224.94 --> 2225.42]  also want
[2225.42 --> 2225.88]  to make
[2225.88 --> 2226.42]  Argo CD
[2226.42 --> 2227.18]  enterprise
[2227.18 --> 2227.44]  ready.
[2227.92 --> 2228.24]  What that
[2228.24 --> 2228.98]  means is
[2228.98 --> 2229.94]  our customers
[2229.94 --> 2230.54]  will get
[2230.54 --> 2232.18]  audits and
[2232.18 --> 2232.90]  insightful
[2232.90 --> 2234.04]  analytics out
[2234.04 --> 2234.54]  of the box
[2234.54 --> 2235.14]  without
[2235.14 --> 2236.04]  configuring
[2236.04 --> 2236.46]  anything.
[2236.94 --> 2237.36]  That's what
[2237.36 --> 2238.26]  we did at
[2238.26 --> 2238.80]  Intuit and
[2238.80 --> 2239.16]  we learned
[2239.16 --> 2239.64]  that it was
[2239.64 --> 2240.16]  not so easy
[2240.16 --> 2240.52]  to do.
[2240.88 --> 2241.20]  And that's
[2241.20 --> 2241.50]  what we're
[2241.50 --> 2241.96]  hoping to
[2241.96 --> 2242.46]  solve for
[2242.46 --> 2242.86]  multiple
[2242.86 --> 2243.70]  organizations.
[2244.22 --> 2244.48]  Very cool.
[2244.56 --> 2244.84]  Thank you,
[2244.88 --> 2245.08]  Jesse.
[2245.24 --> 2245.60]  Thank you,
[2245.66 --> 2245.96]  Alex.
[2246.06 --> 2246.46]  Again,
[2246.54 --> 2246.84]  listeners,
[2247.10 --> 2248.34]  this is a
[2248.34 --> 2249.08]  closed beta.
[2249.42 --> 2249.72]  Check it
[2249.72 --> 2250.04]  out.
[2250.20 --> 2250.62]  Acuity
[2250.62 --> 2251.62]  dot IO
[2251.62 --> 2252.10]  slash
[2252.10 --> 2252.86]  changelog.
[2252.92 --> 2253.44]  Head there
[2253.44 --> 2253.88]  and see
[2253.88 --> 2254.14]  what this
[2254.14 --> 2255.08]  platform is
[2255.08 --> 2255.80]  all about.
[2256.14 --> 2256.42]  Again,
[2256.58 --> 2257.52]  acuity dot IO
[2257.52 --> 2257.90]  slash
[2257.90 --> 2258.48]  changelog.
[2258.54 --> 2259.30]  Links are
[2259.30 --> 2259.72]  in the
[2259.72 --> 2260.20]  show notes.
[2260.76 --> 2260.96]  And by
[2260.96 --> 2261.52]  our friends
[2261.52 --> 2262.06]  at Launch
[2262.06 --> 2262.48]  Darkly,
[2262.76 --> 2263.18]  fundamentally
[2263.18 --> 2263.92]  change how
[2263.92 --> 2264.26]  you deliver
[2264.26 --> 2264.86]  software,
[2265.32 --> 2265.52]  innovate
[2265.52 --> 2266.20]  faster,
[2266.54 --> 2266.76]  deploy
[2266.76 --> 2267.16]  fearlessly,
[2267.66 --> 2267.92]  and take
[2267.92 --> 2268.30]  control of
[2268.30 --> 2268.78]  your software
[2268.78 --> 2269.12]  so you can
[2269.12 --> 2269.56]  ship value
[2269.56 --> 2269.98]  to customers
[2269.98 --> 2270.90]  faster and
[2270.90 --> 2271.56]  get feedback
[2271.56 --> 2272.00]  sooner.
[2272.46 --> 2272.60]  Launch
[2272.60 --> 2273.06]  Darkly is
[2273.06 --> 2273.38]  built for
[2273.38 --> 2274.04]  developers but
[2274.04 --> 2274.50]  empowers the
[2274.50 --> 2274.90]  entire
[2274.90 --> 2275.50]  organization.
[2276.00 --> 2276.28]  Get started
[2276.28 --> 2276.80]  for free and
[2276.80 --> 2277.36]  get a demo
[2277.36 --> 2277.78]  at
[2277.78 --> 2278.78]  launchdarkly.com.
[2278.78 --> 2279.62]  Again,
[2279.96 --> 2280.94]  launchdarkly.com.
[2280.94 --> 2301.52]  You mentioned
[2301.52 --> 2302.42]  briefly about
[2302.42 --> 2303.42]  your background,
[2303.60 --> 2304.10]  starting with
[2304.10 --> 2305.28]  C++ and also
[2305.28 --> 2306.06]  on a little bit
[2306.06 --> 2306.96]  on how you
[2306.96 --> 2307.64]  come to the idea
[2307.64 --> 2308.16]  of doing this
[2308.16 --> 2308.56]  workshop.
[2308.56 --> 2308.98]  Do you want
[2308.98 --> 2310.10]  to elaborate
[2310.10 --> 2310.68]  a little bit
[2310.68 --> 2311.66]  on kind of
[2311.66 --> 2312.36]  giving the
[2312.36 --> 2312.98]  context of
[2312.98 --> 2314.06]  what brought
[2314.06 --> 2315.62]  you on the
[2315.62 --> 2316.26]  shorter time
[2316.26 --> 2316.70]  and on the
[2316.70 --> 2317.24]  longer term
[2317.24 --> 2317.72]  to this
[2317.72 --> 2318.18]  idea?
[2318.56 --> 2319.22]  I don't
[2319.22 --> 2319.48]  know.
[2319.90 --> 2320.26]  There was
[2320.26 --> 2321.42]  this jobs
[2321.42 --> 2322.78]  fair in
[2322.78 --> 2323.74]  April where
[2323.74 --> 2324.48]  I sat down
[2324.48 --> 2324.88]  with the
[2324.88 --> 2325.92]  organizer of
[2325.92 --> 2326.34]  Graphicon
[2326.34 --> 2327.34]  Europe and
[2327.34 --> 2328.02]  I asked
[2328.02 --> 2329.30]  her point
[2329.30 --> 2329.66]  blank,
[2330.04 --> 2331.04]  so why
[2331.04 --> 2331.34]  have you
[2331.34 --> 2331.98]  never asked
[2331.98 --> 2333.02]  me to
[2333.02 --> 2333.72]  do a
[2333.72 --> 2334.16]  workshop?
[2334.92 --> 2335.58]  You know,
[2335.66 --> 2336.34]  I do this.
[2336.34 --> 2337.78]  And then
[2337.78 --> 2338.30]  she told
[2338.30 --> 2338.54]  me,
[2338.62 --> 2338.76]  well,
[2338.78 --> 2339.20]  it's a lot
[2339.20 --> 2339.62]  of work
[2339.62 --> 2339.96]  and I
[2339.96 --> 2340.18]  said,
[2340.28 --> 2340.56]  yeah,
[2340.74 --> 2341.22]  I mean,
[2341.26 --> 2341.64]  this is
[2341.64 --> 2342.26]  something that
[2342.26 --> 2342.78]  I do.
[2343.80 --> 2344.12]  But the
[2344.12 --> 2344.74]  topic itself
[2344.74 --> 2345.26]  is really
[2345.26 --> 2345.84]  something that
[2345.84 --> 2346.18]  I didn't
[2346.18 --> 2346.62]  want to
[2346.62 --> 2347.10]  teach my
[2347.10 --> 2347.32]  team.
[2347.40 --> 2347.74]  My team
[2347.74 --> 2348.90]  works mostly
[2348.90 --> 2349.74]  procedural code,
[2349.80 --> 2349.98]  right?
[2350.08 --> 2350.34]  Mostly
[2350.34 --> 2351.34]  procedural code
[2351.34 --> 2352.06]  with Go.
[2352.52 --> 2352.74]  Why?
[2352.82 --> 2353.22]  Why did you
[2353.22 --> 2353.62]  want to do
[2353.62 --> 2353.76]  it?
[2353.80 --> 2354.08]  How did
[2354.08 --> 2354.38]  you even
[2354.38 --> 2354.72]  come to
[2354.72 --> 2355.02]  think of
[2355.02 --> 2355.18]  it?
[2355.28 --> 2355.58]  Because
[2355.58 --> 2355.90]  that's
[2355.90 --> 2356.20]  what they
[2356.20 --> 2356.84]  do and
[2356.84 --> 2357.54]  I actually
[2357.54 --> 2358.12]  don't think
[2358.12 --> 2358.52]  that those
[2358.52 --> 2359.14]  patterns that
[2359.14 --> 2359.66]  they're using
[2359.66 --> 2360.62]  serve my
[2360.62 --> 2361.08]  team very
[2361.08 --> 2361.38]  well.
[2361.56 --> 2361.90]  Actually,
[2362.06 --> 2362.46]  it's not
[2362.46 --> 2362.86]  really my
[2362.86 --> 2363.06]  team,
[2366.34 --> 2366.82]  months ago
[2366.82 --> 2367.50]  we
[2367.50 --> 2368.20]  reorganized.
[2368.56 --> 2369.12]  We used
[2369.12 --> 2369.62]  middleware
[2369.62 --> 2370.98]  patterns in
[2370.98 --> 2371.76]  a way that
[2371.76 --> 2372.56]  was not
[2372.56 --> 2373.22]  really working
[2373.22 --> 2373.70]  well for
[2373.70 --> 2373.96]  us.
[2374.62 --> 2374.98]  I mean,
[2375.02 --> 2375.30]  I'm not
[2375.30 --> 2375.64]  saying that
[2375.64 --> 2375.96]  there is
[2375.96 --> 2376.58]  no way to
[2376.58 --> 2377.10]  make it
[2377.10 --> 2377.82]  not work.
[2378.20 --> 2378.72]  There is
[2378.72 --> 2379.28]  no way to
[2379.28 --> 2379.60]  make it
[2379.60 --> 2379.86]  work,
[2380.24 --> 2381.04]  but the
[2381.04 --> 2381.40]  way that
[2381.40 --> 2381.76]  we did
[2381.76 --> 2382.22]  this was
[2382.22 --> 2382.70]  not really
[2382.70 --> 2383.28]  working well
[2383.28 --> 2383.72]  for us.
[2384.40 --> 2385.34]  And I
[2385.34 --> 2385.86]  was trying
[2385.86 --> 2386.32]  to show
[2386.32 --> 2386.66]  the team
[2386.66 --> 2387.14]  different
[2387.14 --> 2387.68]  approaches
[2387.68 --> 2388.64]  to maybe
[2388.64 --> 2389.74]  redesign
[2389.74 --> 2391.32]  really a
[2391.32 --> 2391.98]  portion of
[2391.98 --> 2392.48]  the code
[2392.48 --> 2393.44]  that I
[2393.44 --> 2394.08]  felt would
[2394.08 --> 2394.88]  just be
[2394.88 --> 2395.84]  easier to
[2395.84 --> 2396.60]  understand
[2396.60 --> 2397.46]  with classic
[2397.46 --> 2398.16]  object oriented
[2398.16 --> 2399.30]  because that
[2399.30 --> 2400.06]  is how we
[2400.06 --> 2400.62]  used to see
[2400.62 --> 2401.10]  the world.
[2401.56 --> 2402.18]  We understand
[2402.18 --> 2402.78]  the legation.
[2402.92 --> 2403.30]  For instance,
[2403.38 --> 2404.12]  if I tell
[2404.12 --> 2404.94]  you not only
[2404.94 --> 2405.58]  to breathe
[2405.58 --> 2405.86]  in,
[2405.96 --> 2406.30]  you don't
[2406.30 --> 2406.68]  have to
[2406.68 --> 2408.42]  think about
[2408.42 --> 2409.62]  operating your
[2409.62 --> 2409.88]  lungs.
[2409.98 --> 2410.24]  You just
[2410.24 --> 2410.74]  breathe in.
[2411.66 --> 2412.58]  And if I
[2412.58 --> 2413.06]  tell you to
[2413.06 --> 2413.74]  breathe deeply,
[2413.96 --> 2414.32]  then you
[2414.32 --> 2414.92]  will breathe
[2414.92 --> 2415.30]  deeply.
[2415.40 --> 2415.72]  And if I
[2415.72 --> 2416.16]  tell you to
[2416.16 --> 2416.88]  stop breathing,
[2417.18 --> 2417.60]  you will
[2417.60 --> 2418.02]  until you
[2418.02 --> 2418.40]  panic.
[2420.58 --> 2420.98]  Defer.
[2421.32 --> 2421.82]  Breathe out.
[2424.74 --> 2425.34]  You will
[2425.34 --> 2425.78]  the first
[2425.78 --> 2426.20]  sun breath,
[2426.38 --> 2426.76]  hopefully.
[2428.40 --> 2428.92]  Unless
[2428.92 --> 2429.52]  something is
[2429.52 --> 2429.94]  broken.
[2432.22 --> 2432.98]  I do
[2432.98 --> 2433.70]  feel that
[2433.70 --> 2434.44]  when the
[2434.44 --> 2435.04]  code gets
[2435.04 --> 2436.24]  too complex
[2436.24 --> 2436.72]  and you
[2436.72 --> 2437.38]  don't understand
[2437.38 --> 2438.04]  it anymore,
[2438.26 --> 2438.92]  you really,
[2439.18 --> 2439.66]  really need to
[2439.66 --> 2440.44]  start thinking
[2440.44 --> 2442.16]  in terms
[2442.16 --> 2443.66]  of objects.
[2443.92 --> 2444.72]  It makes
[2444.72 --> 2445.68]  things so
[2445.68 --> 2446.36]  much easier.
[2446.56 --> 2447.10]  People do
[2447.10 --> 2447.80]  understand
[2447.80 --> 2448.98]  those concepts
[2448.98 --> 2449.66]  very well
[2449.66 --> 2450.46]  because they
[2450.46 --> 2451.72]  mimic the
[2451.72 --> 2452.20]  way that we
[2452.20 --> 2452.62]  think, the
[2452.62 --> 2453.06]  way that we
[2453.06 --> 2453.54]  work, the
[2453.54 --> 2453.88]  way the
[2453.88 --> 2454.66]  world works.
[2455.62 --> 2456.00]  So that's
[2456.00 --> 2456.28]  where it
[2456.28 --> 2456.62]  came from.
[2456.66 --> 2456.90]  It came
[2456.90 --> 2457.22]  from a
[2457.22 --> 2457.82]  real problem
[2457.82 --> 2458.36]  in our
[2458.36 --> 2458.96]  code base.
[2459.32 --> 2459.78]  And then
[2459.78 --> 2460.70]  kind of
[2460.70 --> 2461.62]  realized that
[2461.62 --> 2462.30]  if people
[2462.30 --> 2462.94]  don't agree
[2462.94 --> 2463.36]  that it's
[2463.36 --> 2463.74]  an object
[2463.74 --> 2464.08]  oriented
[2464.08 --> 2464.66]  language,
[2464.78 --> 2465.64]  then one,
[2466.02 --> 2466.48]  I want
[2466.48 --> 2466.84]  them to
[2466.84 --> 2467.38]  see why
[2467.38 --> 2467.70]  I think
[2467.70 --> 2468.16]  it is
[2468.16 --> 2469.32]  and at
[2469.32 --> 2469.64]  least give
[2469.64 --> 2469.94]  them the
[2469.94 --> 2470.28]  option.
[2470.92 --> 2471.40]  And also,
[2471.54 --> 2472.02]  I feel like
[2472.02 --> 2472.42]  we failed
[2472.42 --> 2472.76]  them in
[2472.76 --> 2473.12]  some way.
[2473.24 --> 2473.82]  If people
[2473.82 --> 2474.46]  work with
[2474.46 --> 2474.90]  Go and
[2474.90 --> 2475.46]  they don't
[2475.46 --> 2476.26]  see it
[2476.26 --> 2476.96]  and they
[2476.96 --> 2477.50]  don't see
[2477.50 --> 2478.14]  the benefits
[2478.14 --> 2478.70]  at all
[2478.70 --> 2479.80]  and they
[2479.80 --> 2480.30]  don't think
[2480.30 --> 2480.70]  it even
[2480.70 --> 2481.26]  exists,
[2481.26 --> 2482.52]  it's a
[2482.52 --> 2483.26]  massive part
[2483.26 --> 2483.54]  of the
[2483.54 --> 2484.56]  language that
[2484.56 --> 2485.00]  they're not
[2485.00 --> 2485.54]  utilizing.
[2486.54 --> 2487.20]  Go is very
[2487.20 --> 2488.16]  simple, like
[2488.16 --> 2488.78]  in the sense
[2488.78 --> 2489.20]  that, for
[2489.20 --> 2490.18]  instance, if
[2490.18 --> 2490.96]  we compare it
[2490.96 --> 2491.62]  to my first
[2491.62 --> 2492.22]  language, it's
[2492.22 --> 2492.76]  not really my
[2492.76 --> 2493.30]  first language,
[2493.40 --> 2494.18]  let's say my
[2494.18 --> 2495.36]  somewhat first
[2495.36 --> 2495.80]  language.
[2496.12 --> 2496.58]  My first
[2496.58 --> 2497.10]  language is
[2497.10 --> 2497.98]  Pascal, but
[2497.98 --> 2499.00]  if you point a
[2499.00 --> 2499.38]  gun to my
[2499.38 --> 2499.78]  head, I won't
[2499.78 --> 2500.36]  be able to.
[2500.52 --> 2501.08]  Same here.
[2501.54 --> 2501.80]  Yeah.
[2502.46 --> 2502.86]  They're the
[2502.86 --> 2503.62]  products of the
[2503.62 --> 2505.04]  same education
[2505.04 --> 2505.88]  system.
[2506.28 --> 2506.90]  Some people
[2506.90 --> 2508.48]  had Java,
[2508.48 --> 2510.26]  which is
[2510.26 --> 2510.76]  not really
[2510.76 --> 2511.90]  the uncle
[2511.90 --> 2513.88]  of Go,
[2514.08 --> 2514.82]  unlike Pascal,
[2514.94 --> 2515.36]  which is.
[2515.64 --> 2516.20]  Yeah, that's
[2516.20 --> 2516.46]  true.
[2516.74 --> 2517.22]  It's actually
[2517.22 --> 2517.60]  true.
[2517.90 --> 2518.28]  Although I
[2518.28 --> 2518.68]  did start
[2518.68 --> 2519.16]  with doctor
[2519.16 --> 2519.76]  scheme to
[2519.76 --> 2520.22]  be very,
[2520.36 --> 2521.02]  very accurate.
[2521.58 --> 2522.14]  Well, I
[2522.14 --> 2523.10]  mean, the
[2523.10 --> 2523.64]  only reason
[2523.64 --> 2524.10]  that I know
[2524.10 --> 2524.38]  that is
[2524.38 --> 2524.86]  because of
[2524.86 --> 2525.48]  Carmenando,
[2525.72 --> 2526.36]  who went
[2526.36 --> 2526.94]  around telling
[2526.94 --> 2527.90]  everybody that
[2527.90 --> 2529.34]  Go is like
[2529.34 --> 2530.46]  a child of
[2530.46 --> 2531.16]  the branches
[2531.16 --> 2531.90]  of Pascal.
[2532.18 --> 2532.34]  Yeah.
[2532.98 --> 2533.58]  And then I
[2533.58 --> 2534.12]  learned also
[2534.12 --> 2534.90]  that Ruby is
[2534.90 --> 2535.96]  also somewhat
[2535.96 --> 2536.60]  a child of
[2536.60 --> 2537.10]  Pascal, which
[2537.10 --> 2537.70]  explains why I
[2537.70 --> 2538.14]  like Ruby.
[2538.14 --> 2538.76]  Although I
[2538.76 --> 2539.28]  don't remember
[2539.28 --> 2540.12]  Pascal at all
[2540.12 --> 2540.80]  and I can't
[2540.80 --> 2541.50]  really feel like
[2541.50 --> 2541.88]  there are
[2541.88 --> 2542.66]  similarities or
[2542.66 --> 2542.94]  not.
[2543.06 --> 2543.62]  I have no
[2543.62 --> 2543.90]  idea.
[2544.50 --> 2545.30]  Try to take
[2545.30 --> 2545.66]  it with a
[2545.66 --> 2546.00]  piece of
[2546.00 --> 2546.28]  paper.
[2546.46 --> 2546.76]  Maybe it
[2546.76 --> 2547.20]  will refresh
[2547.20 --> 2547.58]  your memory
[2547.58 --> 2548.02]  more than
[2548.02 --> 2548.28]  with a
[2548.28 --> 2548.56]  screen.
[2550.04 --> 2550.54]  That's how
[2550.54 --> 2551.02]  it was for
[2551.02 --> 2551.34]  me, at
[2551.34 --> 2551.72]  least, writing
[2551.72 --> 2552.42]  Pascal code.
[2552.76 --> 2553.04]  I thought you
[2553.04 --> 2553.58]  ever actually
[2553.58 --> 2554.48]  executed any.
[2554.82 --> 2555.06]  Did you
[2555.06 --> 2555.26]  get to
[2555.26 --> 2555.62]  write it?
[2556.08 --> 2556.46]  I don't
[2556.46 --> 2556.86]  remember.
[2557.34 --> 2557.96]  For better
[2557.96 --> 2558.36]  and worse,
[2558.58 --> 2559.24]  education
[2559.24 --> 2559.70]  system.
[2560.56 --> 2561.10]  It's the
[2561.10 --> 2561.76]  whiteboard of
[2561.76 --> 2562.52]  the early
[2562.52 --> 2562.92]  times.
[2563.54 --> 2564.32]  Anyway, yes,
[2564.46 --> 2564.76]  it's like
[2564.76 --> 2565.30]  uncle of
[2565.30 --> 2565.54]  Ruby.
[2565.62 --> 2565.94]  I did not
[2565.94 --> 2566.40]  know that.
[2566.62 --> 2567.18]  Yeah, things
[2567.18 --> 2567.66]  that you
[2567.66 --> 2568.90]  learn when
[2568.90 --> 2569.24]  you go to
[2569.24 --> 2569.68]  conferences.
[2571.12 --> 2571.56]  Random
[2571.56 --> 2572.74]  bits of
[2572.74 --> 2573.48]  information,
[2573.90 --> 2574.64]  of trivia
[2574.64 --> 2575.22]  that could
[2575.22 --> 2575.66]  be useful
[2575.66 --> 2575.92]  in the
[2575.92 --> 2576.36]  future or
[2576.36 --> 2576.54]  not.
[2577.26 --> 2578.10]  So, back
[2578.10 --> 2578.58]  to C++,
[2578.74 --> 2579.26]  it has a
[2579.26 --> 2579.98]  million features
[2579.98 --> 2580.36]  that you're
[2580.36 --> 2580.70]  never going
[2580.70 --> 2581.06]  to use.
[2581.56 --> 2582.24]  JavaScript as
[2582.24 --> 2582.78]  well, nobody
[2582.78 --> 2584.20]  uses, let's
[2584.20 --> 2584.88]  say, what it
[2584.88 --> 2585.08]  is.
[2585.12 --> 2585.58]  It's not a
[2585.58 --> 2586.28]  common practice.
[2586.36 --> 2586.88]  In that case,
[2586.90 --> 2587.46]  it's the best
[2587.46 --> 2588.38]  practice not to
[2588.38 --> 2589.84]  utilize all the
[2589.84 --> 2590.90]  features in
[2590.90 --> 2591.58]  those languages
[2591.58 --> 2592.54]  because that
[2592.54 --> 2594.52]  is not
[2594.52 --> 2595.50]  maintainable code.
[2596.18 --> 2596.56]  So,
[2596.78 --> 2597.32]  letting go,
[2597.32 --> 2598.08]  Go has
[2598.08 --> 2598.52]  been written
[2598.52 --> 2599.08]  in a way
[2599.08 --> 2599.60]  that should
[2599.60 --> 2600.18]  allow us
[2600.18 --> 2601.00]  to utilize
[2601.00 --> 2601.80]  all the
[2601.80 --> 2602.20]  features.
[2603.14 --> 2603.76]  So, the
[2603.76 --> 2604.32]  idea that
[2604.32 --> 2604.96]  people don't
[2604.96 --> 2606.38]  do it is,
[2606.94 --> 2607.26]  well, she
[2607.26 --> 2608.06]  said, I
[2608.06 --> 2608.42]  don't know
[2608.42 --> 2608.72]  what to
[2608.72 --> 2610.30]  say else
[2610.30 --> 2610.82]  about it.
[2610.82 --> 2611.42]  What are
[2611.42 --> 2611.88]  some good
[2611.88 --> 2612.94]  or bad
[2612.94 --> 2613.80]  use cases
[2613.80 --> 2614.64]  for using
[2614.64 --> 2615.00]  that?
[2615.34 --> 2615.86]  Like, you
[2615.86 --> 2616.26]  mentioned,
[2616.52 --> 2617.02]  billing is
[2617.02 --> 2617.80]  your close
[2617.80 --> 2618.10]  to home
[2618.10 --> 2618.60]  example.
[2619.06 --> 2619.24]  Do you
[2619.24 --> 2619.66]  have some
[2619.66 --> 2621.50]  other use
[2621.50 --> 2621.94]  cases you
[2621.94 --> 2622.18]  would say
[2622.18 --> 2622.90]  definitely use
[2622.90 --> 2623.12]  it or
[2623.12 --> 2623.48]  definitely
[2623.48 --> 2623.94]  don't?
[2623.94 --> 2625.24]  So, the
[2625.24 --> 2625.84]  quote that
[2625.84 --> 2627.18]  Rob Pike,
[2627.50 --> 2627.80]  that I
[2627.80 --> 2628.08]  think
[2628.08 --> 2628.70]  whatever,
[2629.00 --> 2629.34]  whomever
[2629.34 --> 2630.10]  sent me
[2630.10 --> 2631.08]  the message
[2631.08 --> 2631.80]  was basing
[2631.80 --> 2632.34]  it on,
[2632.58 --> 2633.08]  he said
[2633.08 --> 2633.60]  that, I
[2633.60 --> 2633.88]  don't know,
[2633.96 --> 2634.40]  there were
[2634.40 --> 2635.26]  multiple,
[2635.76 --> 2636.56]  a professor
[2636.56 --> 2637.30]  used multiple
[2637.30 --> 2638.18]  classes to
[2638.18 --> 2638.82]  perform something
[2638.82 --> 2639.24]  that was a
[2639.24 --> 2639.96]  simple lookup.
[2640.50 --> 2641.26]  And I think
[2641.26 --> 2641.90]  this is it.
[2641.98 --> 2642.50]  And I also
[2642.50 --> 2643.36]  understand why
[2643.36 --> 2643.96]  it happened.
[2644.84 --> 2645.30]  But again,
[2645.38 --> 2645.92]  it's not
[2645.92 --> 2646.24]  Go,
[2646.40 --> 2646.86]  actually.
[2647.68 --> 2648.70]  So, again,
[2648.76 --> 2649.22]  when we go
[2649.22 --> 2649.98]  back to
[2649.98 --> 2651.52]  Java,
[2652.34 --> 2652.82]  you are not
[2652.82 --> 2653.56]  able to
[2653.56 --> 2654.30]  say that
[2654.30 --> 2655.14]  A is B
[2655.14 --> 2655.88]  unless A is
[2655.88 --> 2656.54]  aware of B
[2656.54 --> 2657.42]  and knows
[2657.42 --> 2657.66]  that it
[2657.66 --> 2658.32]  implements B.
[2658.82 --> 2659.22]  So, you
[2659.22 --> 2659.78]  can't really
[2659.78 --> 2660.36]  say that A
[2660.36 --> 2660.76]  is B.
[2661.36 --> 2661.82]  And then in
[2661.82 --> 2662.32]  those languages,
[2662.32 --> 2662.74]  you really
[2662.74 --> 2663.54]  have to work
[2663.54 --> 2664.98]  extra hard
[2664.98 --> 2666.70]  to express
[2666.70 --> 2667.24]  the idea
[2667.24 --> 2667.66]  that A
[2667.66 --> 2668.00]  is B.
[2668.66 --> 2669.08]  And that
[2669.08 --> 2669.70]  could create
[2669.70 --> 2670.18]  those, you
[2670.18 --> 2670.88]  know, those
[2670.88 --> 2672.02]  intermediate layers
[2672.02 --> 2673.08]  between code
[2673.08 --> 2673.64]  that is just
[2673.64 --> 2674.56]  a proxy,
[2674.80 --> 2675.16]  which just
[2675.16 --> 2675.78]  invokes more
[2675.78 --> 2676.14]  code and
[2676.14 --> 2676.66]  invokes more
[2676.66 --> 2676.98]  code.
[2677.40 --> 2678.02]  And then at
[2678.02 --> 2678.36]  the end of
[2678.36 --> 2678.66]  the day,
[2678.74 --> 2679.08]  if you want
[2679.08 --> 2679.70]  to perform
[2679.70 --> 2680.52]  a simple
[2680.52 --> 2680.92]  lookup,
[2681.26 --> 2682.00]  it can look
[2682.00 --> 2683.02]  like something
[2683.02 --> 2683.46]  that will
[2683.46 --> 2684.12]  create this
[2684.12 --> 2684.98]  very chaotic
[2684.98 --> 2686.02]  code base
[2686.02 --> 2687.44]  for something
[2687.44 --> 2687.96]  very, very
[2687.96 --> 2688.36]  simple.
[2689.18 --> 2689.66]  But then
[2689.66 --> 2690.78]  in Go,
[2691.06 --> 2691.72]  I always say
[2691.72 --> 2692.12]  that everything
[2692.12 --> 2692.80]  is explicit
[2692.80 --> 2693.50]  in Go
[2693.50 --> 2693.96]  except for
[2693.96 --> 2694.32]  the things
[2694.32 --> 2694.78]  that aren't.
[2695.46 --> 2695.90]  And what I
[2695.90 --> 2696.40]  mean by the
[2696.40 --> 2696.82]  things that
[2696.82 --> 2697.30]  aren't are
[2697.30 --> 2698.04]  like stringers,
[2698.16 --> 2698.60]  for instance,
[2698.74 --> 2699.86]  where we
[2699.86 --> 2700.88]  invoke some
[2700.88 --> 2702.24]  functionality by
[2702.24 --> 2703.26]  performing some
[2703.26 --> 2704.42]  type assertion
[2704.42 --> 2706.22]  that nobody
[2706.22 --> 2706.90]  is aware of
[2706.90 --> 2707.18]  somewhere.
[2708.12 --> 2708.34]  But yeah,
[2708.42 --> 2708.84]  but generally
[2708.84 --> 2709.34]  speaking,
[2709.44 --> 2709.80]  Go is
[2709.80 --> 2710.24]  explicit.
[2710.90 --> 2711.62]  If you have
[2711.62 --> 2712.46]  a package and
[2712.46 --> 2712.88]  it's well
[2712.88 --> 2713.28]  written,
[2714.00 --> 2715.16]  then it
[2715.16 --> 2716.18]  should meet
[2716.18 --> 2716.90]  the open
[2716.90 --> 2718.12]  close principles
[2718.12 --> 2719.98]  and then you
[2719.98 --> 2720.98]  should be able
[2720.98 --> 2722.34]  to wrap this
[2722.34 --> 2722.78]  type with
[2722.78 --> 2723.16]  whatever,
[2723.68 --> 2723.98]  you know,
[2724.02 --> 2724.94]  or extend
[2724.94 --> 2725.76]  the functionality
[2725.76 --> 2726.68]  of whatever it
[2726.68 --> 2727.10]  is that you
[2727.10 --> 2727.30]  want.
[2727.86 --> 2728.46]  I understand
[2728.46 --> 2728.94]  why people
[2728.94 --> 2729.56]  struggle with
[2729.56 --> 2729.76]  that.
[2730.08 --> 2730.62]  I think that
[2730.62 --> 2731.26]  is the biggest
[2731.26 --> 2732.54]  issue is
[2732.54 --> 2734.08]  how we
[2734.08 --> 2734.54]  don't write
[2734.54 --> 2735.30]  packages very
[2735.30 --> 2735.58]  well.
[2735.64 --> 2735.98]  By the way,
[2736.06 --> 2736.38]  for the
[2736.38 --> 2736.74]  workshop,
[2737.04 --> 2738.08]  I had to
[2738.08 --> 2739.44]  revise my
[2739.44 --> 2740.10]  code multiple
[2740.10 --> 2741.06]  times because
[2741.06 --> 2741.76]  I realized that
[2741.76 --> 2742.40]  my design
[2742.40 --> 2743.02]  choices were
[2743.02 --> 2744.38]  so far,
[2744.84 --> 2745.30]  let's say.
[2745.52 --> 2746.08]  Less common
[2746.08 --> 2746.56]  practices.
[2748.14 --> 2749.14]  For instance,
[2749.30 --> 2749.90]  it's really
[2749.90 --> 2750.32]  funny.
[2751.30 --> 2752.10]  So I
[2752.10 --> 2752.78]  actually wanted
[2752.78 --> 2753.38]  to show
[2753.38 --> 2754.28]  that the
[2754.28 --> 2754.72]  code was
[2754.72 --> 2755.44]  extendable.
[2755.78 --> 2756.68]  So by
[2756.68 --> 2757.66]  actually creating
[2757.66 --> 2758.08]  an extra
[2758.08 --> 2759.02]  package that
[2759.02 --> 2759.66]  will use that
[2759.66 --> 2760.08]  package.
[2760.08 --> 2760.94]  and then I
[2760.94 --> 2761.58]  realized that
[2761.58 --> 2761.74]  no,
[2761.82 --> 2762.26]  that package
[2762.26 --> 2762.62]  should take
[2762.62 --> 2762.84]  in an
[2762.84 --> 2763.26]  interface,
[2763.38 --> 2763.64]  for instance.
[2763.80 --> 2763.86]  Like,
[2763.90 --> 2764.12]  I mean,
[2764.50 --> 2764.84]  you should
[2764.84 --> 2765.56]  extend that
[2765.56 --> 2765.94]  through an
[2765.94 --> 2766.40]  interface,
[2766.52 --> 2767.12]  not direct.
[2767.82 --> 2768.62]  And as I
[2768.62 --> 2769.16]  was doing
[2769.16 --> 2769.60]  that,
[2769.94 --> 2770.38]  the reason
[2770.38 --> 2770.94]  that I
[2770.94 --> 2771.84]  realized that
[2771.84 --> 2772.44]  was because
[2772.44 --> 2773.00]  I had a
[2773.00 --> 2773.84]  third package
[2773.84 --> 2774.42]  that actually
[2774.42 --> 2775.54]  did need
[2775.54 --> 2776.58]  that interface
[2776.58 --> 2777.54]  and it needed
[2777.54 --> 2778.24]  that interface
[2778.24 --> 2778.70]  to be in
[2778.70 --> 2779.34]  the in-between
[2779.34 --> 2779.78]  layer.
[2780.34 --> 2780.80]  And then I
[2780.80 --> 2781.46]  started thinking,
[2781.64 --> 2782.12]  so how do
[2782.12 --> 2782.58]  I make,
[2782.72 --> 2782.84]  like,
[2782.88 --> 2783.42]  if I wanted
[2783.42 --> 2784.02]  to teach
[2784.02 --> 2784.84]  somebody that,
[2785.02 --> 2785.64]  how would I
[2785.64 --> 2786.70]  actually do it?
[2786.96 --> 2787.22]  And I'm
[2787.22 --> 2787.94]  still struggling
[2787.94 --> 2788.26]  with,
[2788.38 --> 2788.46]  like,
[2788.52 --> 2789.08]  figuring out,
[2789.16 --> 2789.26]  like,
[2789.28 --> 2789.84]  what is the
[2789.84 --> 2791.60]  exact problem
[2791.60 --> 2792.00]  with that
[2792.00 --> 2792.84]  code that
[2792.84 --> 2793.36]  I could tell
[2793.36 --> 2793.66]  somebody,
[2793.76 --> 2793.86]  like,
[2793.88 --> 2794.36]  if you see
[2794.36 --> 2794.70]  this,
[2794.76 --> 2795.28]  then that is
[2795.28 --> 2795.78]  your problem
[2795.78 --> 2796.14]  and that's
[2796.14 --> 2796.36]  what you
[2796.36 --> 2796.66]  need to
[2796.66 --> 2797.20]  change.
[2797.92 --> 2798.54]  But it's
[2798.54 --> 2798.98]  really funny
[2798.98 --> 2799.34]  because I
[2799.34 --> 2799.84]  was actually
[2799.84 --> 2800.66]  writing something
[2800.66 --> 2801.66]  to show
[2801.66 --> 2802.58]  that it's
[2802.58 --> 2803.10]  going to be
[2803.10 --> 2803.64]  extendable
[2803.64 --> 2804.10]  and then it
[2804.10 --> 2804.70]  wasn't.
[2804.78 --> 2805.16]  And then at
[2805.16 --> 2805.58]  some point,
[2805.64 --> 2805.76]  like,
[2805.82 --> 2807.08]  I hit an end.
[2807.40 --> 2807.96]  So obviously,
[2808.08 --> 2808.26]  you know,
[2808.32 --> 2809.10]  I fixed it.
[2809.66 --> 2810.96]  But generally,
[2811.46 --> 2812.70]  it's a different
[2812.70 --> 2813.60]  type of language.
[2813.60 --> 2814.70]  So a package
[2814.70 --> 2815.50]  doesn't have
[2815.50 --> 2816.44]  to expose
[2816.44 --> 2817.26]  the interfaces
[2817.26 --> 2817.88]  that,
[2818.16 --> 2818.34]  like,
[2818.38 --> 2818.94]  an interface.
[2819.10 --> 2819.24]  Like,
[2819.30 --> 2819.90]  if you write
[2819.90 --> 2821.22]  code in Java,
[2821.32 --> 2821.62]  if you write
[2821.62 --> 2822.44]  code in C++,
[2822.98 --> 2823.80]  you don't want
[2823.80 --> 2824.48]  to express it
[2824.48 --> 2824.80]  easy.
[2825.46 --> 2826.26]  But at the time
[2826.26 --> 2826.86]  that you write
[2826.86 --> 2827.36]  the package
[2827.36 --> 2827.92]  or you write
[2827.92 --> 2828.40]  the class
[2828.40 --> 2828.86]  or you write
[2828.86 --> 2829.24]  anything,
[2829.24 --> 2830.26]  you have to
[2830.26 --> 2831.58]  know how
[2831.58 --> 2832.28]  the user is
[2832.28 --> 2832.90]  going to use
[2832.90 --> 2833.08]  it.
[2833.52 --> 2834.28]  You have to
[2834.28 --> 2834.56]  know.
[2834.88 --> 2835.46]  And then you
[2835.46 --> 2836.26]  have to
[2836.26 --> 2836.92]  extend
[2836.92 --> 2838.40]  or implement
[2838.40 --> 2839.10]  or,
[2839.18 --> 2839.48]  you know,
[2840.00 --> 2841.42]  do something
[2841.42 --> 2842.92]  so that
[2842.92 --> 2843.54]  a user
[2843.54 --> 2844.18]  who is
[2844.18 --> 2844.74]  using your
[2844.74 --> 2845.10]  package
[2845.10 --> 2845.48]  is going
[2845.48 --> 2846.10]  to be able
[2846.10 --> 2846.72]  to plug
[2846.72 --> 2847.56]  in your
[2847.56 --> 2848.50]  A as B,
[2848.78 --> 2850.04]  your A as I,
[2850.16 --> 2850.68]  your A as
[2850.68 --> 2850.96]  whatever.
[2851.86 --> 2852.46]  So you have
[2852.46 --> 2853.36]  to think
[2853.36 --> 2854.04]  about how
[2854.04 --> 2854.58]  people are
[2854.58 --> 2855.34]  going to
[2855.34 --> 2856.70]  use your
[2856.70 --> 2857.16]  class.
[2857.62 --> 2858.26]  And then in
[2858.26 --> 2858.42]  Go,
[2858.48 --> 2858.78]  you don't
[2858.78 --> 2859.36]  have to do
[2859.36 --> 2859.54]  it,
[2859.66 --> 2859.98]  but then
[2859.98 --> 2860.30]  you can
[2860.30 --> 2860.90]  write very
[2860.90 --> 2861.34]  easily
[2861.34 --> 2862.08]  a usable
[2862.08 --> 2862.62]  package
[2862.62 --> 2863.14]  or
[2863.14 --> 2863.38]  an
[2863.38 --> 2863.88]  extendable
[2863.88 --> 2864.46]  package.
[2865.28 --> 2865.60]  So how
[2865.60 --> 2866.00]  to write
[2866.00 --> 2866.46]  it well,
[2866.56 --> 2866.94]  by the way,
[2867.02 --> 2867.28]  is something
[2867.28 --> 2867.62]  that I'm
[2867.62 --> 2867.98]  still,
[2868.12 --> 2868.56]  I still
[2868.56 --> 2869.20]  don't know
[2869.20 --> 2869.82]  that we
[2869.82 --> 2870.24]  are very
[2870.24 --> 2870.62]  good at
[2870.62 --> 2871.18]  teaching.
[2871.42 --> 2871.94]  I'm
[2871.94 --> 2872.44]  trying to
[2872.44 --> 2872.82]  sort of
[2872.82 --> 2873.34]  figure that
[2873.34 --> 2873.78]  out as
[2873.78 --> 2874.38]  well as
[2874.38 --> 2874.76]  I go.
[2875.22 --> 2875.68]  How do
[2875.68 --> 2876.40]  I define
[2876.40 --> 2877.42]  that a
[2877.42 --> 2878.46]  package is
[2878.46 --> 2878.90]  good?
[2879.28 --> 2879.66]  And I
[2879.66 --> 2880.54]  love when
[2880.54 --> 2881.32]  people explain
[2881.32 --> 2881.72]  the open
[2881.72 --> 2882.12]  clause,
[2882.22 --> 2882.70]  they always
[2882.70 --> 2883.82]  talk about
[2883.82 --> 2885.08]  CRL or
[2885.08 --> 2885.56]  curl or
[2885.56 --> 2886.08]  whatever the
[2886.08 --> 2886.50]  command.
[2886.84 --> 2887.24]  Nobody's
[2887.24 --> 2887.60]  going to
[2887.60 --> 2888.66]  rewrite curl.
[2889.22 --> 2889.62]  It doesn't
[2889.62 --> 2890.92]  require redesigning.
[2891.12 --> 2891.56]  Why?
[2891.72 --> 2892.24]  Why is it
[2892.24 --> 2892.82]  so good?
[2892.90 --> 2893.44]  What makes
[2893.44 --> 2894.52]  it so good?
[2894.90 --> 2895.54]  And what
[2895.54 --> 2895.94]  makes a
[2895.94 --> 2896.76]  good package?
[2897.14 --> 2897.64]  It's a
[2897.64 --> 2897.90]  very,
[2898.06 --> 2898.64]  very difficult
[2898.64 --> 2899.34]  question.
[2900.12 --> 2900.62]  Regardless,
[2900.84 --> 2901.24]  by the way,
[2901.24 --> 2902.50]  if you have
[2902.50 --> 2903.14]  object-oriented
[2903.14 --> 2903.54]  or not,
[2903.62 --> 2904.22]  even if it's
[2904.22 --> 2905.08]  just a bunch
[2905.08 --> 2905.70]  of functions,
[2906.22 --> 2906.74]  it is very
[2906.74 --> 2907.36]  difficult to
[2907.36 --> 2908.66]  define when
[2908.66 --> 2909.22]  you're done,
[2909.36 --> 2910.16]  to know exactly
[2910.16 --> 2910.52]  when you're
[2910.52 --> 2910.76]  done.
[2911.14 --> 2912.36]  One last
[2912.36 --> 2913.26]  question before
[2913.26 --> 2914.22]  we switch to
[2914.22 --> 2914.98]  the fun and
[2914.98 --> 2915.78]  popular opinion,
[2916.08 --> 2917.24]  which we were
[2917.24 --> 2918.06]  missing so much
[2918.06 --> 2918.54]  throughout this
[2918.54 --> 2919.22]  entire episode.
[2919.66 --> 2920.34]  You've been
[2920.34 --> 2920.98]  kind of giving
[2920.98 --> 2921.88]  sprinkles of
[2921.88 --> 2922.72]  information on
[2922.72 --> 2923.60]  the workshop.
[2924.04 --> 2924.94]  So other than
[2924.94 --> 2925.66]  this as being
[2925.66 --> 2926.56]  an object-oriented
[2926.56 --> 2927.60]  programming in Go,
[2927.94 --> 2928.68]  what else can you
[2928.68 --> 2929.22]  tell us about
[2929.22 --> 2929.38]  it?
[2930.12 --> 2930.56]  Well,
[2930.68 --> 2931.34]  I can tell
[2931.34 --> 2931.82]  you that I
[2931.82 --> 2932.46]  will take the
[2932.46 --> 2933.38]  learners through
[2933.38 --> 2935.28]  a maze of
[2935.28 --> 2937.26]  object-oriented.
[2937.94 --> 2938.66]  And when I
[2938.66 --> 2939.66]  say a maze,
[2939.80 --> 2940.80]  I mean quite
[2940.80 --> 2941.24]  literally.
[2942.12 --> 2943.12]  We are going
[2943.12 --> 2943.66]  to navigate
[2943.66 --> 2944.68]  through a maze.
[2945.18 --> 2945.88]  I mentioned
[2945.88 --> 2946.72]  Jeff Rosenstein
[2946.72 --> 2947.70]  earlier,
[2948.00 --> 2948.98]  who is my
[2948.98 --> 2950.02]  professor to
[2950.02 --> 2951.00]  intro to CS.
[2951.00 --> 2953.10]  and our
[2953.10 --> 2954.66]  first exercise
[2954.66 --> 2955.96]  way back
[2955.96 --> 2957.34]  when in
[2957.34 --> 2959.00]  2003,
[2959.54 --> 2960.40]  that's what
[2960.40 --> 2960.94]  I'm taking
[2960.94 --> 2961.74]  people through.
[2962.08 --> 2962.52]  So it's
[2962.52 --> 2963.86]  heavily inspired
[2963.86 --> 2964.94]  by his work.
[2965.38 --> 2965.96]  So credit
[2965.96 --> 2966.44]  to him.
[2967.30 --> 2968.26]  I thought it
[2968.26 --> 2968.94]  was a very
[2968.94 --> 2970.56]  good way of
[2970.56 --> 2972.30]  exploring object-oriented.
[2972.70 --> 2973.60]  And I like to
[2973.60 --> 2974.38]  take people through
[2974.38 --> 2975.42]  journeys that I
[2975.42 --> 2976.28]  found very good
[2976.28 --> 2976.94]  for myself.
[2977.08 --> 2977.72]  Like if I had
[2977.72 --> 2978.54]  a moment,
[2978.80 --> 2979.46]  I try to share
[2979.46 --> 2979.92]  it with other
[2979.92 --> 2980.70]  people as well.
[2981.00 --> 2982.00]  And Natalie,
[2982.18 --> 2982.66]  you know this.
[2982.80 --> 2983.36]  Ian, actually,
[2983.42 --> 2984.14]  I can ask you,
[2984.48 --> 2985.14]  what is your
[2985.14 --> 2986.26]  aha moment in
[2986.26 --> 2986.84]  your career?
[2987.08 --> 2988.30]  Like situations
[2988.30 --> 2989.00]  when you said,
[2989.12 --> 2990.20]  wow, and now
[2990.20 --> 2990.70]  I get it.
[2990.80 --> 2991.42]  Now I know.
[2991.90 --> 2992.44]  That's a real
[2992.44 --> 2993.22]  on-the-spot
[2993.22 --> 2993.62]  question.
[2993.68 --> 2994.08]  I know.
[2994.18 --> 2994.74]  It's a difficult
[2994.74 --> 2995.14]  one.
[2996.24 --> 2996.94]  When did you
[2996.94 --> 2997.66]  realize that you
[2997.66 --> 2998.38]  can do this?
[2998.50 --> 2999.22]  You can code.
[2999.46 --> 3000.10]  You know what
[3000.10 --> 3000.48]  to do.
[3000.72 --> 3001.62]  You've got this.
[3001.98 --> 3002.82]  I mean, that
[3002.82 --> 3004.42]  moment was, you
[3004.42 --> 3004.84]  know, so I was
[3004.84 --> 3005.62]  in school and I
[3005.62 --> 3006.22]  went to interview
[3006.22 --> 3006.98]  for an internship,
[3007.54 --> 3007.94]  you know, and
[3007.94 --> 3009.28]  going, doing
[3009.28 --> 3009.80]  that interview.
[3009.94 --> 3010.48]  And they did
[3010.48 --> 3010.90]  like the whole
[3010.90 --> 3011.62]  whiteboard thing,
[3011.66 --> 3012.08]  you know, it was
[3012.08 --> 3013.00]  eight hours of
[3013.00 --> 3013.46]  interviews.
[3013.88 --> 3014.62]  Leaving that was
[3014.62 --> 3015.24]  that like aha
[3015.24 --> 3015.96]  moment was like,
[3016.04 --> 3016.70]  I felt good at
[3016.70 --> 3017.12]  the end of that
[3017.12 --> 3017.56]  and that made
[3017.56 --> 3018.86]  me feel like I
[3018.86 --> 3019.26]  was like, oh
[3019.26 --> 3019.78]  yeah, I can do
[3019.78 --> 3019.94]  this.
[3020.00 --> 3020.52]  I can do this,
[3020.58 --> 3020.78]  you know.
[3021.16 --> 3021.92]  So for you.
[3022.18 --> 3023.04]  But before that,
[3023.08 --> 3023.72]  I had no
[3023.72 --> 3024.26]  confidence.
[3024.94 --> 3025.52]  That's the thing.
[3025.52 --> 3026.38]  So for you, it was
[3026.38 --> 3027.24]  trial by fire.
[3027.62 --> 3027.94]  Exactly.
[3028.12 --> 3028.28]  Yeah.
[3028.46 --> 3028.90]  That's very
[3028.90 --> 3029.28]  interesting.
[3029.44 --> 3030.14]  I think for a lot
[3030.14 --> 3031.10]  of people, it is
[3031.10 --> 3032.58]  just like succeeding
[3032.58 --> 3033.50]  in something that I
[3033.50 --> 3034.14]  didn't think they
[3034.14 --> 3034.74]  could before.
[3035.20 --> 3035.90]  I didn't think I
[3035.90 --> 3036.66]  was ready for like
[3036.66 --> 3037.78]  that kind of set of
[3037.78 --> 3038.52]  interviews, you know,
[3038.54 --> 3040.80]  but that's a reason
[3040.80 --> 3041.44]  why I tell people
[3041.44 --> 3042.58]  just you see a lot
[3042.58 --> 3043.22]  of those posts where
[3043.22 --> 3044.40]  it's like, oh, you
[3044.40 --> 3044.98]  know, I'm trying to
[3044.98 --> 3045.94]  get do these things
[3045.94 --> 3046.98]  before I apply for
[3046.98 --> 3047.78]  jobs in an interview.
[3047.78 --> 3048.60]  And my advice is
[3048.60 --> 3049.30]  always just like, just
[3049.30 --> 3049.72]  go interview.
[3049.86 --> 3050.82]  Like if you do
[3050.82 --> 3052.20]  poorly, like you've
[3052.20 --> 3052.98]  learned something and
[3052.98 --> 3054.00]  you can go do the
[3054.00 --> 3054.46]  next one a little
[3054.46 --> 3054.82]  bit better.
[3054.98 --> 3056.12]  Like, don't wait,
[3056.24 --> 3056.66]  just go.
[3056.94 --> 3057.92]  I think Natalie, the
[3057.92 --> 3058.86]  next time we need to
[3058.86 --> 3059.60]  bring somebody who
[3059.60 --> 3060.30]  doesn't agree.
[3062.92 --> 3063.86]  Because we are all
[3063.86 --> 3064.90]  so on the same page.
[3064.96 --> 3065.54]  It's a problem.
[3066.20 --> 3066.56]  100%.
[3066.56 --> 3067.50]  Yeah.
[3067.94 --> 3068.64]  Yeah, we'll pull
[3068.64 --> 3069.30]  some from your
[3069.30 --> 3069.70]  emails.
[3070.36 --> 3071.60]  A thought that came
[3071.60 --> 3073.08]  to mind throughout
[3073.08 --> 3073.82]  this episode.
[3074.68 --> 3075.64]  See if I can make
[3075.64 --> 3076.98]  this into sort of an
[3076.98 --> 3077.96]  unpopular opinion.
[3078.64 --> 3079.24]  Probably not.
[3079.32 --> 3079.84]  So I'm not going to
[3079.84 --> 3080.56]  make the tune just
[3080.56 --> 3080.84]  yet.
[3081.40 --> 3082.66]  But thinking of an
[3082.66 --> 3083.98]  AI-generated tool,
[3084.00 --> 3085.82]  they get inspired
[3085.82 --> 3086.82]  from existing code,
[3086.88 --> 3087.08]  right?
[3087.48 --> 3089.78]  And we can have
[3089.78 --> 3091.04]  this conversation if
[3091.04 --> 3091.94]  there's features of
[3091.94 --> 3094.72]  Go, of OOP in
[3094.72 --> 3095.62]  Go or not.
[3095.86 --> 3096.80]  But if there's not a
[3096.80 --> 3097.82]  lot of examples out
[3097.82 --> 3099.96]  there, the different
[3099.96 --> 3101.98]  models that generate
[3101.98 --> 3103.78]  code will not be
[3103.78 --> 3105.26]  creating this a lot.
[3105.56 --> 3107.34]  So assuming that the
[3107.34 --> 3108.42]  trend of code is not
[3108.42 --> 3109.48]  just human writing it,
[3109.52 --> 3110.44]  but more like human
[3110.44 --> 3112.64]  guiding it, it means
[3112.64 --> 3113.44]  means that it will,
[3113.90 --> 3114.46]  at least the way I
[3114.46 --> 3115.22]  see it, it means
[3115.22 --> 3116.40]  that a lot of the
[3116.40 --> 3117.70]  code or the
[3117.70 --> 3118.60]  languages will kind
[3118.60 --> 3119.68]  of fall deeper
[3119.68 --> 3121.74]  into their template
[3121.74 --> 3122.96]  or into their
[3122.96 --> 3124.86]  niche or little box
[3124.86 --> 3126.14]  rather than spreading
[3126.14 --> 3127.42]  out of it like you
[3127.42 --> 3127.64]  did.
[3127.88 --> 3129.24]  So this can be a fun
[3129.24 --> 3130.46]  thing to think
[3131.28 --> 3132.78]  about as a person
[3132.78 --> 3133.84]  who's researching AI
[3133.84 --> 3134.30]  and code.
[3134.80 --> 3135.12]  Wow.
[3135.12 --> 3136.00]  I love it.
[3136.12 --> 3136.98]  So, you know, a
[3136.98 --> 3139.24]  few days ago I had
[3139.24 --> 3140.46]  that thought, AI is
[3140.46 --> 3141.32]  not going to write
[3141.32 --> 3142.90]  code or OOP maybe
[3142.90 --> 3143.92]  because they don't
[3143.92 --> 3144.74]  really understand the
[3144.74 --> 3145.44]  world like we do.
[3145.52 --> 3146.16]  They don't have that
[3146.16 --> 3146.64]  restriction.
[3147.36 --> 3148.10]  You know, a bot
[3148.10 --> 3149.00]  doesn't tell a person
[3149.00 --> 3149.60]  to breathe.
[3149.82 --> 3150.32]  You know what I mean?
[3150.98 --> 3151.88]  They don't need to.
[3152.02 --> 3153.38]  They can go as
[3153.38 --> 3154.96]  deeply into the
[3154.96 --> 3156.30]  mechanics of how to
[3156.30 --> 3157.68]  breathe so that
[3157.68 --> 3158.88]  their understanding is
[3158.88 --> 3160.04]  going to be very
[3160.04 --> 3161.44]  different of those
[3161.44 --> 3161.86]  models.
[3161.86 --> 3162.74]  Yeah.
[3163.12 --> 3164.22]  Maybe there will be
[3164.22 --> 3164.92]  some way of doing
[3164.92 --> 3166.60]  this guided and then
[3166.60 --> 3167.78]  we're saved from
[3167.78 --> 3168.42]  those boxes.
[3168.62 --> 3169.04]  Exactly.
[3169.32 --> 3170.24]  So that is very
[3170.24 --> 3172.32]  interesting is what
[3172.32 --> 3173.88]  what you have there
[3173.88 --> 3175.36]  because, you know,
[3175.42 --> 3176.36]  like something that I
[3176.36 --> 3177.58]  said earlier about how
[3177.58 --> 3178.66]  how do you know that
[3178.66 --> 3179.94]  a package is complete?
[3180.08 --> 3181.18]  Maybe a bot can do
[3181.18 --> 3181.90]  that for you.
[3182.16 --> 3183.60]  Static analysis or
[3183.60 --> 3184.04]  dynamic.
[3184.32 --> 3185.58]  Maybe a bot can
[3185.58 --> 3187.36]  analyze if something
[3187.36 --> 3188.16]  is open closed.
[3188.70 --> 3188.88]  Yeah.
[3189.00 --> 3189.18]  Yeah.
[3189.30 --> 3190.50]  That definitely is a
[3190.50 --> 3191.64]  fun conversation to
[3191.64 --> 3191.96]  have.
[3192.60 --> 3193.64]  And if anybody wants
[3193.64 --> 3194.54]  to chat about this,
[3194.64 --> 3195.46]  we are on the go
[3195.46 --> 3197.14]  time Slack channel
[3197.14 --> 3197.70]  and the go for
[3197.70 --> 3198.02]  Slack.
[3198.26 --> 3198.96]  So reach out and
[3198.96 --> 3199.86]  maybe this will be
[3199.86 --> 3201.18]  our some future
[3201.18 --> 3201.70]  episode.
[3202.06 --> 3202.70]  But until then,
[3202.82 --> 3203.60]  let's do the tune
[3203.60 --> 3204.54]  for the unpopular
[3204.54 --> 3204.94]  opinion.
[3210.94 --> 3212.24]  I actually think
[3212.24 --> 3213.18]  she'd probably leave.
[3216.32 --> 3217.00]  Unpopular
[3217.00 --> 3218.10]  opinion.
[3221.64 --> 3223.66]  And now it's time
[3223.66 --> 3224.32]  for the unpopular
[3224.32 --> 3224.80]  opinion.
[3224.98 --> 3225.60]  Rona, what do you
[3225.60 --> 3226.14]  have for us?
[3226.58 --> 3227.58]  I mean, I felt like
[3227.58 --> 3229.08]  the entire show
[3229.08 --> 3230.50]  was about, I have
[3230.50 --> 3232.06]  an arsenal of, you
[3232.06 --> 3234.44]  know, of things that
[3234.44 --> 3235.34]  I need to convince
[3235.34 --> 3236.84]  people about.
[3237.64 --> 3240.64]  So I feel that we're
[3240.64 --> 3242.00]  going to be much
[3242.00 --> 3243.76]  stronger if we
[3243.76 --> 3245.26]  collected opinions
[3245.26 --> 3246.78]  about go from people
[3246.78 --> 3247.30]  who are not
[3247.30 --> 3248.44]  professional gophers.
[3248.44 --> 3250.38]  And instead of
[3250.38 --> 3251.34]  teaching them,
[3251.92 --> 3252.90]  learn from them a
[3252.90 --> 3254.08]  little bit, I do
[3254.08 --> 3255.36]  see other languages
[3255.36 --> 3256.68]  evolve, you know,
[3256.70 --> 3257.40]  in many different
[3257.40 --> 3258.02]  directions.
[3258.26 --> 3260.32]  I think people
[3260.32 --> 3261.98]  understand today
[3261.98 --> 3263.44]  how to work with
[3263.44 --> 3265.36]  languages in a very
[3265.36 --> 3266.50]  different way than
[3266.50 --> 3268.02]  what we used to do.
[3268.56 --> 3269.40]  The evolution of
[3269.40 --> 3270.58]  best practices, all
[3270.58 --> 3271.38]  of those things,
[3271.80 --> 3272.54]  it's just, it's
[3272.54 --> 3272.86]  tremendous.
[3273.06 --> 3273.82]  And also I think
[3273.82 --> 3275.52]  that go added a lot
[3275.52 --> 3276.46]  of value to other
[3276.46 --> 3277.68]  languages just by
[3277.68 --> 3278.62]  existing, just
[3278.62 --> 3279.56]  because, you know,
[3279.84 --> 3281.42]  go introduced these
[3281.42 --> 3282.14]  features that we
[3282.14 --> 3282.70]  discussed.
[3283.12 --> 3283.76]  I think we
[3283.76 --> 3285.08]  influenced the
[3285.08 --> 3286.62]  industry, but I
[3286.62 --> 3287.10]  think that we
[3287.10 --> 3287.78]  should be open
[3287.78 --> 3288.48]  also to be
[3288.48 --> 3289.36]  influenced back.
[3289.48 --> 3290.34]  So your unpopular
[3290.34 --> 3291.36]  opinion is that we
[3291.36 --> 3292.30]  go should be open
[3292.30 --> 3293.18]  to be influenced
[3293.18 --> 3294.76]  by non-gophers.
[3295.14 --> 3295.56]  Yes.
[3296.02 --> 3296.48]  All right.
[3296.60 --> 3297.28]  Let's see how that
[3297.28 --> 3297.84]  poll works.
[3298.22 --> 3299.06]  This will be a poll
[3299.06 --> 3299.86]  and then let's see
[3299.86 --> 3301.08]  if that brings you
[3301.08 --> 3302.68]  further into the
[3302.68 --> 3304.02]  hall of fame of
[3304.02 --> 3304.46]  the unpopular
[3304.46 --> 3304.96]  opinions.
[3305.26 --> 3305.92]  Well, I mean,
[3306.12 --> 3307.28]  Matt said after he
[3307.28 --> 3307.96]  put me in the
[3307.96 --> 3309.04]  hall of fame, he
[3309.04 --> 3309.88]  then said that it
[3309.88 --> 3310.70]  doesn't exist
[3310.70 --> 3311.24]  everywhere.
[3311.72 --> 3312.58]  I think so that
[3312.58 --> 3314.84]  the other people
[3314.84 --> 3315.62]  with unpopular
[3315.62 --> 3316.72]  opinions are not
[3316.72 --> 3316.94]  jealous.
[3317.60 --> 3318.66]  But I mean, as
[3318.66 --> 3319.22]  far as I'm
[3319.22 --> 3321.22]  concerned, it's
[3321.22 --> 3324.80]  I won that title
[3324.80 --> 3325.56]  fair and square.
[3328.06 --> 3329.10]  But let's see.
[3329.18 --> 3329.56]  Let's see.
[3329.66 --> 3330.60]  I mean, it might
[3330.60 --> 3331.82]  not be as
[3331.82 --> 3333.22]  unorthodox as the
[3333.22 --> 3334.22]  old one.
[3334.22 --> 3336.48]  Oh, all right.
[3336.62 --> 3337.80]  Well, that was
[3337.80 --> 3339.08]  fun and interesting
[3339.08 --> 3340.78]  and I hope this
[3340.78 --> 3341.48]  will bring to the
[3341.48 --> 3342.16]  workshop that will
[3342.16 --> 3342.92]  generate enough
[3342.92 --> 3343.50]  code that will
[3343.50 --> 3344.38]  train the AI to
[3344.38 --> 3344.90]  do some
[3344.90 --> 3346.28]  OOPI Go.
[3347.10 --> 3347.78]  Thanks, Rona.
[3347.98 --> 3348.42]  Thanks, Ian.
[3348.52 --> 3348.96]  Thanks, everyone
[3348.96 --> 3349.38]  who joined.
[3349.70 --> 3350.26]  Thank you.
[3354.70 --> 3355.60]  What do you think
[3355.60 --> 3357.22]  about Go and OOP?
[3357.58 --> 3358.84]  Let us know in the
[3358.84 --> 3359.36]  comments.
[3359.72 --> 3360.48]  Links to the
[3360.48 --> 3361.48]  discussion in the
[3361.48 --> 3361.94]  show notes.
[3361.94 --> 3363.40]  I also want to
[3363.40 --> 3364.14]  share with you an
[3364.14 --> 3364.92]  awesome conversation
[3364.92 --> 3365.64]  we had on the
[3365.64 --> 3366.44]  changelog recently.
[3366.72 --> 3367.58]  Ken Konser wrote
[3367.58 --> 3369.60]  up 16 lessons he
[3369.60 --> 3370.44]  learned doing
[3370.44 --> 3371.46]  security audits for
[3371.46 --> 3372.54]  tech startups and
[3372.54 --> 3373.28]  we sat down with
[3373.28 --> 3374.06]  him for a thorough
[3374.06 --> 3374.88]  discussion of his
[3374.88 --> 3375.26]  findings.
[3375.78 --> 3376.78]  Here's one moment
[3376.78 --> 3377.76]  from that episode
[3377.76 --> 3379.10]  where Ken shares
[3379.10 --> 3380.72]  some pro tips for
[3380.72 --> 3381.72]  pen testing teams.
[3382.34 --> 3383.84]  And honestly, we
[3383.84 --> 3384.78]  would also ask the
[3384.78 --> 3385.92]  devs, we would
[3385.92 --> 3386.44]  say like what
[3386.44 --> 3387.24]  keeps you up, like
[3387.24 --> 3388.02]  where in the code
[3388.02 --> 3388.66]  keeps you up at
[3388.66 --> 3388.86]  night?
[3389.12 --> 3389.68]  We wouldn't treat
[3389.68 --> 3390.40]  that as God's
[3390.40 --> 3391.72]  truth, but you
[3391.72 --> 3392.56]  know, developers
[3392.56 --> 3393.48]  have a surprisingly
[3393.48 --> 3395.52]  good sense, even
[3395.52 --> 3396.28]  without security
[3396.28 --> 3398.24]  knowledge, of what
[3398.24 --> 3399.14]  parts of the code
[3399.14 --> 3400.82]  are scary and
[3400.82 --> 3401.40]  they're kind of
[3401.40 --> 3401.94]  worried about.
[3402.32 --> 3402.76]  They definitely
[3402.76 --> 3403.74]  have blind spots.
[3404.34 --> 3405.02]  That's definitely
[3405.02 --> 3405.76]  true, but in
[3405.76 --> 3407.08]  terms of like, we
[3407.08 --> 3407.42]  were talking about
[3407.42 --> 3408.30]  business logic, a
[3408.30 --> 3408.70]  lot of times
[3408.70 --> 3409.04]  they'll be like,
[3409.08 --> 3409.62]  yeah, this part
[3409.62 --> 3410.54]  is super gnarly,
[3410.68 --> 3411.94]  like there's a ton
[3411.94 --> 3413.06]  of logic here and
[3413.06 --> 3414.26]  it kind of works,
[3414.38 --> 3414.98]  but like it also
[3414.98 --> 3415.64]  breaks a decent
[3415.64 --> 3416.90]  amount and it's
[3416.90 --> 3417.30]  an important
[3417.30 --> 3418.16]  functionality for the
[3418.16 --> 3418.70]  app, so please
[3418.70 --> 3419.22]  check that out.
[3419.60 --> 3420.06]  So those two
[3420.06 --> 3420.82]  things really helped
[3420.82 --> 3421.26]  prioritize.
[3421.72 --> 3422.56]  That scary
[3422.56 --> 3423.44]  intuition reminds
[3423.44 --> 3424.14]  me of severance,
[3424.28 --> 3424.62]  honestly.
[3424.84 --> 3425.82]  It's like, well, I
[3425.82 --> 3426.70]  can easily spot the
[3426.70 --> 3427.62]  scary numbers here.
[3429.56 --> 3430.54]  Continue listening
[3430.54 --> 3432.32]  at changelog.fm
[3432.32 --> 3433.64]  slash 494.
[3433.80 --> 3434.62]  That's episode
[3434.62 --> 3436.26]  number 494.
[3436.60 --> 3437.26]  Thanks again to
[3437.26 --> 3437.82]  our partners at
[3437.82 --> 3438.62]  Fastly for having
[3438.62 --> 3439.68]  our CDN covered,
[3439.96 --> 3440.82]  to the mysterious
[3440.82 --> 3442.00]  Breakmaster Cylinder for
[3442.00 --> 3442.76]  keeping our beat
[3442.76 --> 3444.36]  supply on swole, and
[3444.36 --> 3445.12]  to you for listening.
[3445.32 --> 3446.12]  We appreciate you.
[3446.34 --> 3447.50]  That is all for now.
[3447.70 --> 3448.34]  We'll talk to you
[3448.34 --> 3449.80]  again next time on
[3449.80 --> 3450.34]  GoTime.
[3450.34 --> 3454.26]  GoTime.
[3454.72 --> 3455.18]  Goigi.
[3455.18 --> 3456.18]  GoTime.
[3461.32 --> 3462.72]  GoTime.
[3462.72 --> 3465.10]  Game on!

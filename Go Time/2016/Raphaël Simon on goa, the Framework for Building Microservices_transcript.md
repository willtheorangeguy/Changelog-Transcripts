[0.00 --> 2.46]  I'm Rafael Simon, and this is Go Time.
[17.46 --> 22.18]  It's Go Time, a weekly podcast where we discuss interesting topics around the Go programming
[22.18 --> 27.06]  language, the community, and everything in between. If you currently write Go or aspire to,
[27.06 --> 28.62]  this is the show for you.
[30.00 --> 35.94]  All right, everybody. Welcome back for another episode of Go Time. It is episode number seven.
[36.68 --> 40.52]  Today, we have Brian Kettleson here with us. Say hello, Brian.
[41.06 --> 41.44]  Hello.
[42.18 --> 44.26]  And Carlisa Campos is also here.
[45.04 --> 46.38]  Glad to be here. Hi, everybody.
[46.88 --> 54.26]  And we also have a special guest here with us, Rafael Simon, who is the creator of a framework
[54.26 --> 60.38]  called Goa for generating APIs, which Brian is particularly excited about.
[60.94 --> 61.20]  Hello.
[61.20 --> 65.36]  You want to give us a little bit of background, Rafael?
[66.28 --> 67.14]  Sure. Yeah.
[67.34 --> 70.66]  So let's start with who am I.
[71.24 --> 74.12]  So I'm a platform architect at RedScale.
[74.64 --> 76.90]  RedScale is a cloud management platform.
[76.90 --> 80.88]  I've been working there for almost eight years.
[81.22 --> 84.84]  And when I started, the whole product was basically a single raise app.
[85.48 --> 87.66]  And the platform has grown a lot since then.
[88.00 --> 92.12]  And last time I counted, there were about 52 different services running in production,
[92.80 --> 94.42]  you know, running on about a thousand VM.
[94.42 --> 99.56]  So I've helped design, develop, and debug a lot of them.
[100.96 --> 106.96]  And part of going from this single raise app to all those distributed services,
[107.54 --> 113.58]  we felt a lot of pain in having to design APIs the right way.
[114.14 --> 120.26]  What I mean by that is being able to come up with APIs that are consistent
[120.26 --> 124.56]  and have standards that are enforceable.
[124.86 --> 127.24]  So, you know, so that we can come up and say,
[127.38 --> 128.90]  yep, that API looks good.
[129.24 --> 130.42]  It follows our standards.
[131.10 --> 135.06]  And we'd be able to integrate that service with the rest of the fleet.
[136.06 --> 139.70]  And as you probably know, once an API is alive,
[139.70 --> 141.96]  it's almost impossible to change it.
[142.28 --> 144.32]  Once you have customers that start using it,
[144.42 --> 147.54]  or once your internal services rely on it,
[147.54 --> 151.52]  then that API is going to be alive forever.
[151.78 --> 155.46]  So it is very important that you spend the time designing it properly.
[157.42 --> 160.84]  And when we looked at what was available to do that,
[161.28 --> 162.34]  there just wasn't much.
[163.24 --> 166.08]  There were a few tools here and there,
[166.24 --> 169.22]  but nothing that we felt would be enough for us.
[169.22 --> 175.66]  So we ended up creating a framework at the time that framework was in Ruby
[175.66 --> 179.26]  called Praxis that basically allowed you to write that design code.
[179.38 --> 183.04]  And then the framework would leverage a design at runtime.
[184.78 --> 186.38]  And fast-forwarding forward,
[187.56 --> 190.06]  RISCALE kind of shifted towards Go.
[190.06 --> 194.68]  And I thought it would be good to see if we could do something in Latin Go.
[195.80 --> 198.80]  And to be honest, I wasn't sure initially that would be possible.
[200.52 --> 203.40]  So I played around with a few things.
[204.94 --> 206.90]  And it took me about a year, really,
[207.04 --> 210.86]  to come up with something that started to look like it may work.
[210.86 --> 219.66]  And so there were two big aha moments in that kind of research phase.
[219.90 --> 224.86]  One was the realization that code generation was the perfect approach
[224.86 --> 228.72]  for achieving the goal of keeping the design and implementation separate
[228.72 --> 231.60]  while making sure that the design is directly enforced.
[232.22 --> 237.40]  And the second realization was that the design should be written in a DSL
[237.40 --> 241.46]  so that the language used to describe the API used the right terms, right?
[241.48 --> 245.14]  You want to talk about resources, actions, responses, requests,
[245.52 --> 249.58]  and you don't want to have to deal with programming language artifacts.
[250.94 --> 254.12]  So that DSL would have to be a Go DSL, obviously,
[254.30 --> 256.30]  so that it could be understood right away
[256.30 --> 261.08]  and also so that it's still possible to use the Go language when it's needed.
[262.36 --> 265.12]  So fast-forward a year and a half,
[265.12 --> 269.60]  and I have to say that the result turned out a lot better than I thought it would be.
[270.46 --> 272.64]  And I think a lot of the credits goes to the Go language.
[273.32 --> 276.24]  The Go language provides very simple and powerful mechanism
[276.24 --> 278.72]  to create that DSL.
[279.14 --> 283.60]  It also has very good code analysis support, which is essential,
[284.12 --> 286.90]  and very good generation packages, code generation packages,
[287.68 --> 289.26]  the template package in particular.
[289.86 --> 291.76]  So all of that put together,
[291.76 --> 294.56]  I think we end up today with something that is actually very interesting,
[295.06 --> 300.08]  and we've started using Goa fairly extensively here at RightScale.
[300.32 --> 301.50]  So that's great.
[301.86 --> 305.06]  So just kind of like a high-level detail.
[305.32 --> 309.98]  So Goa is a framework for using kind of DSL
[309.98 --> 314.44]  that's written in Go to generate HTTP APIs.
[314.44 --> 316.26]  Yep, exactly.
[317.12 --> 318.46]  And it, you know,
[318.60 --> 321.40]  from that design,
[321.56 --> 323.82]  from that DSL,
[324.14 --> 327.22]  which is Go code with basically the DSL,
[327.28 --> 331.78]  you can think of it as a lot of package-level functions
[331.78 --> 334.08]  that you invoke and that are recursive.
[334.08 --> 336.16]  So you call a top-level function,
[336.30 --> 336.68]  let's say,
[336.80 --> 337.38]  called API,
[338.04 --> 342.90]  and you then embed other function cores in it
[342.90 --> 345.68]  where you define every single property of the API,
[345.82 --> 346.36]  like the title,
[346.52 --> 346.92]  the description,
[347.08 --> 347.34]  et cetera.
[347.86 --> 349.80]  So when you look at it,
[349.84 --> 351.18]  it's actually not too ugly.
[351.50 --> 353.40]  You can actually understand it very well
[353.40 --> 355.22]  and follow what it's trying to do.
[355.22 --> 357.32]  And from that design,
[357.58 --> 360.78]  what happens is when you load the design,
[360.88 --> 361.78]  when you start the process
[361.78 --> 363.60]  that has that package linked in,
[364.98 --> 367.78]  because all of that design code
[367.78 --> 370.16]  lives in global viable,
[370.80 --> 373.54]  the Go runtime takes care of running all of that for you
[373.54 --> 378.42]  and you end up with a lot of in-memory data structures
[378.42 --> 380.30]  that describe your API.
[381.58 --> 383.64]  And those are simple,
[383.64 --> 385.58]  nothing special,
[386.02 --> 386.82]  Go data structures
[386.82 --> 388.00]  that you can look at,
[388.16 --> 388.42]  inspect,
[388.68 --> 390.74]  and use to generate pretty much anything.
[391.32 --> 392.54]  So it's quite nice
[392.54 --> 394.24]  because you start from a language
[394.24 --> 395.18]  that is easy to use
[395.18 --> 397.18]  from a human point of view
[397.18 --> 399.70]  and you end up with data structures
[399.70 --> 401.00]  that are very nice to handle
[401.00 --> 402.62]  from a programmatic point of view.
[404.26 --> 406.78]  And so Goa comes with a few built-in
[406.78 --> 410.44]  code generation outputs.
[410.76 --> 412.08]  One is the glue code
[412.08 --> 413.98]  that produces the load of an HTTP server
[413.98 --> 415.96]  with the user-provided handlers.
[416.58 --> 418.52]  And that code takes care of validating
[418.52 --> 419.66]  the incoming requests
[419.66 --> 421.30]  according to the validation rules
[421.30 --> 422.18]  described in language.
[422.76 --> 425.38]  It also builds convenient data structures
[425.38 --> 427.52]  for accessing the request state
[427.52 --> 428.68]  and writing the response.
[428.68 --> 431.48]  So you end up with code
[431.48 --> 432.80]  that you have to write as the user,
[432.96 --> 434.46]  which is fairly small, right?
[434.48 --> 435.58]  You don't have to do
[435.58 --> 436.36]  all the validation
[436.36 --> 437.64]  that you usually have to do
[437.64 --> 439.60]  and you don't have to bind
[439.60 --> 440.32]  the request body
[440.32 --> 441.14]  to some data structure.
[441.30 --> 442.88]  All of that is done already.
[443.62 --> 444.54]  You end up with
[444.54 --> 447.06]  what is called a context data structure
[447.06 --> 448.20]  and that data structure
[448.20 --> 450.06]  has everything laid out
[450.06 --> 451.10]  in a way that's very easy
[451.10 --> 452.52]  for you to access and consume.
[453.18 --> 455.96]  So your code is very terse
[455.96 --> 457.26]  and very clean.
[459.30 --> 461.18]  The GoaGen tool
[461.18 --> 462.38]  that comes with Goa,
[462.80 --> 464.52]  which is the code generation tool,
[465.02 --> 467.58]  also generates a client package
[467.58 --> 468.86]  and a client tool.
[469.52 --> 471.80]  So that's also been very neat
[471.80 --> 474.36]  because one issue is
[474.36 --> 475.82]  when you create an API,
[476.48 --> 478.04]  obviously the point is
[478.04 --> 479.22]  for the API to be consumed.
[479.82 --> 481.10]  And what tends to happen
[481.10 --> 482.34]  is that every team
[482.34 --> 483.78]  consuming the tool
[483.78 --> 485.94]  will develop their own client
[485.94 --> 487.68]  and they will all
[487.68 --> 490.30]  become out of date
[490.30 --> 491.30]  and they will all have
[491.30 --> 492.36]  small discrepancies
[492.36 --> 494.70]  and things start creeping up,
[494.84 --> 496.22]  which make the whole thing
[496.22 --> 497.70]  more difficult to evolve.
[498.72 --> 499.62]  And so having that
[499.62 --> 501.00]  being generated automatically
[501.00 --> 503.02]  means that the team
[503.02 --> 504.46]  that provides the API
[504.46 --> 506.42]  also provides the client
[506.42 --> 507.88]  and everybody uses
[507.88 --> 508.66]  that one client.
[508.84 --> 509.68]  And so it makes
[509.68 --> 510.52]  everything consistent
[510.52 --> 512.92]  and helps other teams
[512.92 --> 514.78]  consume the API.
[515.80 --> 516.36]  And GoaGen also
[516.36 --> 517.34]  generates documentation
[517.34 --> 518.98]  in the form of a Swagger
[518.98 --> 520.30]  and JSON schema
[520.30 --> 522.10]  so that you can,
[522.20 --> 523.06]  at any point in time,
[523.22 --> 524.82]  share the design
[524.82 --> 525.80]  to other people
[525.80 --> 526.90]  that may not be familiar
[526.90 --> 528.22]  with the Goa DSL.
[528.86 --> 530.18]  And you can use it also
[530.18 --> 531.18]  to document the API
[531.18 --> 532.88]  once it's in running production.
[533.62 --> 534.94]  So all of that
[534.94 --> 536.26]  makes for a very nice
[536.26 --> 538.86]  way of developing APIs
[538.86 --> 540.40]  and very efficient
[540.40 --> 541.22]  way of doing it.
[541.86 --> 543.40]  So I have two comments.
[543.72 --> 545.10]  I found Goa
[545.10 --> 547.32]  in October, November,
[547.44 --> 548.20]  I guess, of last year.
[548.54 --> 550.30]  And two things struck me
[550.30 --> 552.14]  immediately when I saw Goa.
[552.20 --> 552.96]  The first was that
[552.96 --> 554.06]  the generated code
[554.06 --> 555.32]  looked handwritten.
[555.86 --> 557.68]  And I have to commend you
[557.68 --> 558.90]  for that because for me
[558.90 --> 559.86]  that was the most impressive
[559.86 --> 560.72]  part of the project
[560.72 --> 562.70]  was that all other
[562.70 --> 564.72]  code generation facilities
[564.72 --> 565.48]  I've seen before,
[565.60 --> 566.32]  it's really clear
[566.32 --> 568.64]  that it's generated code
[568.64 --> 570.84]  and it doesn't feel idiomatic.
[571.00 --> 572.10]  It doesn't feel like Go.
[572.30 --> 573.46]  It feels like somebody
[573.46 --> 574.62]  generated some Go code.
[574.80 --> 577.20]  So having that generated code
[577.20 --> 577.94]  in Goa
[577.94 --> 579.56]  look so handwritten
[579.56 --> 581.26]  was very impressive for me.
[581.96 --> 582.70]  Well, thank you.
[582.86 --> 583.26]  Yeah, I mean,
[583.30 --> 584.00]  that was definitely
[584.00 --> 584.88]  a design goal.
[585.66 --> 585.84]  You know,
[585.92 --> 587.98]  when I started Goa,
[588.10 --> 590.34]  I was a little bit
[590.34 --> 591.88]  not afraid,
[591.98 --> 592.92]  but I was a little bit worried
[592.92 --> 595.04]  about the reception
[595.04 --> 595.88]  that the Go community
[595.88 --> 596.34]  would have
[596.34 --> 597.40]  because I know that
[597.40 --> 598.58]  the Go programmers
[598.58 --> 599.34]  are very,
[599.46 --> 601.24]  not picky,
[601.40 --> 602.46]  but they like
[602.46 --> 603.32]  the Go code
[603.32 --> 604.08]  to be geometric.
[604.46 --> 605.84]  They like a certain way,
[607.56 --> 607.84]  you know,
[607.96 --> 608.64]  they like the code
[608.64 --> 609.50]  to look a certain way
[609.50 --> 610.70]  and behave a certain way.
[611.12 --> 612.78]  And so I wanted,
[613.36 --> 614.58]  I didn't want the generated code
[614.58 --> 615.30]  to be an issue,
[615.54 --> 615.82]  basically.
[615.90 --> 616.70]  I wanted that to be
[616.70 --> 617.32]  a non-issue.
[617.44 --> 618.64]  I wanted people to look at it
[618.64 --> 619.02]  and say,
[619.02 --> 619.54]  yeah, okay,
[619.64 --> 620.26]  it looks good enough.
[620.54 --> 621.00]  I don't have to,
[621.18 --> 621.86]  it's not terrible.
[621.86 --> 624.02]  And so I definitely
[624.02 --> 625.58]  try to put some efforts
[625.58 --> 627.26]  to make that
[627.26 --> 628.16]  a non-issue
[628.16 --> 629.92]  for the adoption
[629.92 --> 630.46]  of Goa.
[631.14 --> 631.66]  Now,
[631.96 --> 633.24]  speaking of the kind of
[633.24 --> 634.74]  idiomatic Go
[634.74 --> 635.94]  and reception
[635.94 --> 636.76]  from the community,
[637.34 --> 638.28]  what's the reception
[638.28 --> 639.40]  like for the actual
[639.40 --> 640.34]  DSL itself?
[640.98 --> 641.80]  Because I've seen
[641.80 --> 642.56]  the generated code,
[642.86 --> 643.34]  which I think
[643.34 --> 644.28]  is highly idiomatic.
[645.40 --> 646.64]  But I don't know
[646.64 --> 647.76]  whether the DSL
[647.76 --> 648.38]  is so much.
[648.46 --> 649.58]  Do you get a lot of
[649.58 --> 650.54]  slack about that
[650.54 --> 651.26]  or are people
[651.26 --> 651.78]  pretty helpful?
[651.86 --> 652.18]  Yeah,
[652.30 --> 653.28]  so there's been
[653.28 --> 654.20]  a few comments
[654.20 --> 655.20]  on the repo
[655.20 --> 655.62]  and GitHub
[655.62 --> 656.40]  of people
[656.40 --> 658.76]  trying to make it
[658.76 --> 660.58]  look more like Go,
[660.76 --> 662.22]  but then I'm always very,
[663.32 --> 664.38]  I kind of have a hard line
[664.38 --> 664.98]  saying,
[665.14 --> 665.84]  this is not Go.
[665.94 --> 666.60]  It's a DSL.
[666.68 --> 667.48]  It's a different language.
[667.64 --> 669.10]  It's implemented in Go,
[669.24 --> 670.28]  but it's not Go.
[670.76 --> 671.46]  So for example,
[671.56 --> 672.44]  one thing that you
[672.44 --> 673.68]  sort of have to do
[673.68 --> 674.56]  when you use DSL
[674.56 --> 675.68]  is use dot imports,
[675.94 --> 676.10]  right?
[676.12 --> 676.72]  And a lot of people
[676.72 --> 677.58]  don't like that.
[677.94 --> 678.68]  And I agree.
[678.68 --> 679.42]  I don't think
[679.42 --> 680.00]  that the ports are good
[680.00 --> 680.34]  either.
[680.76 --> 681.64]  I think if you're at Google,
[681.80 --> 682.46]  you shouldn't use them
[682.46 --> 683.14]  and nothing else
[683.14 --> 684.28]  in Go uses that.
[684.52 --> 686.12]  But for the purpose
[686.12 --> 686.68]  of using,
[687.08 --> 687.80]  of implementing
[687.80 --> 688.64]  the DSL,
[689.12 --> 690.08]  that ends up being,
[690.58 --> 692.30]  making the whole thing
[692.30 --> 693.08]  a lot nicer,
[693.36 --> 694.58]  feel a lot more natural.
[695.46 --> 695.96]  And so,
[696.42 --> 697.90]  there is a little bit
[697.90 --> 699.04]  of that pushback,
[699.16 --> 700.24]  but then my response
[700.24 --> 700.52]  is,
[700.68 --> 700.86]  well,
[701.24 --> 702.08]  this is not Go.
[702.08 --> 703.46]  And I'm not trying
[703.46 --> 705.46]  for DSL
[705.46 --> 706.44]  to be idiomatic Go
[706.44 --> 707.22]  because it's not Go
[707.22 --> 707.88]  in the first place.
[709.38 --> 710.86]  And if you think about it,
[711.04 --> 711.24]  you know,
[711.30 --> 713.00]  some of the target outputs
[713.00 --> 713.74]  for the DSL
[713.74 --> 714.50]  is documentation.
[715.02 --> 716.40]  There's also a JavaScript client
[716.40 --> 717.32]  that you can generate
[717.32 --> 718.68]  from that DSL.
[719.16 --> 720.26]  And in the future,
[720.60 --> 721.60]  there can be plugins
[721.60 --> 722.60]  written to generate
[722.60 --> 723.98]  clients in other languages.
[724.50 --> 724.92]  And so,
[725.92 --> 726.66]  the language
[726.66 --> 728.34]  has to be agnostic,
[728.62 --> 728.74]  right?
[728.76 --> 729.54]  It has to remain
[729.54 --> 731.44]  independent of any target
[731.44 --> 732.30]  that it generates.
[732.58 --> 733.20]  And sure,
[733.30 --> 734.04]  Go is the main target
[734.04 --> 734.48]  for sure,
[734.86 --> 735.68]  but still,
[735.80 --> 736.12]  the language
[736.12 --> 737.10]  should try to remain
[737.10 --> 738.36]  as agnostic as possible.
[739.16 --> 739.62]  Right.
[739.72 --> 739.86]  So,
[739.86 --> 740.98]  people just need
[740.98 --> 741.82]  to disconnect
[741.82 --> 742.54]  a little better,
[742.62 --> 742.80]  right?
[742.88 --> 743.60]  It's kind of like
[743.60 --> 744.30]  GRPC,
[744.60 --> 744.80]  right?
[745.34 --> 746.58]  The DSL
[746.58 --> 747.06]  is essentially
[747.06 --> 747.94]  the protobufs,
[747.98 --> 748.16]  right?
[748.26 --> 749.10]  And then the generator
[749.10 --> 750.12]  generates from that.
[750.66 --> 751.68]  Yours just happens to be.
[752.36 --> 752.76]  So,
[752.92 --> 753.08]  yeah.
[753.48 --> 753.66]  Yeah.
[754.20 --> 754.42]  Yeah,
[754.46 --> 755.06]  it's like,
[755.20 --> 756.10]  if you write Swagger,
[756.30 --> 758.36]  then it's completely
[758.36 --> 759.00]  different from your
[759.00 --> 759.56]  programming language.
[759.66 --> 760.24]  It's the same idea.
[760.44 --> 760.56]  Yeah.
[761.44 --> 761.98]  Well,
[762.02 --> 762.86]  that leads me to the
[762.86 --> 763.86]  second thing that I
[763.86 --> 764.64]  noticed about Goa,
[764.70 --> 765.26]  which was the
[765.26 --> 766.58]  approachability of the DSL.
[767.34 --> 767.90]  And I've seen
[767.90 --> 769.62]  many DSLs in the past,
[769.82 --> 770.06]  you know,
[770.06 --> 771.18]  being a former Ruby
[771.18 --> 771.64]  developer,
[771.88 --> 772.02]  it's,
[772.16 --> 772.28]  you know,
[772.28 --> 773.18]  everything we did in Ruby
[773.18 --> 774.30]  was a DSL in one way
[774.30 --> 774.62]  or another.
[775.08 --> 775.48]  So,
[775.86 --> 776.92]  seeing a DSL in Go
[776.92 --> 777.86]  that was approachable
[777.86 --> 778.50]  and understandable
[778.50 --> 779.38]  was really surprising
[779.38 --> 779.70]  for me.
[779.78 --> 780.94]  I had seen
[780.94 --> 782.64]  the test frameworks,
[782.92 --> 783.68]  which one is it?
[784.38 --> 784.82]  Ginkgo?
[785.02 --> 785.38]  GoMega?
[785.50 --> 785.60]  Yeah.
[785.60 --> 785.94]  One of those?
[786.58 --> 787.74]  That uses a similar
[787.74 --> 788.26]  approach.
[788.26 --> 789.56]  And it still just
[789.56 --> 790.20]  didn't really click
[790.20 --> 791.14]  with me until I
[791.14 --> 791.72]  played with Goa.
[791.78 --> 792.84]  And I really enjoyed
[792.84 --> 796.10]  the readability factor
[796.10 --> 797.86]  of the DSL in Goa.
[798.68 --> 799.34]  Thank you.
[799.44 --> 799.62]  Yeah.
[799.88 --> 800.92]  That took a while
[800.92 --> 801.54]  to get right.
[801.54 --> 802.00]  And actually,
[802.32 --> 803.26]  it's funny you mentioned
[803.26 --> 804.20]  Ginkgo and GoMega
[804.20 --> 805.06]  because they were
[805.06 --> 806.70]  definitely big inspiration
[806.70 --> 808.52]  for the Goa DSL.
[809.32 --> 809.54]  You know,
[809.60 --> 809.86]  I went through
[809.86 --> 810.66]  different iterations.
[811.24 --> 811.98]  One iteration,
[812.14 --> 812.80]  I was using
[812.80 --> 814.58]  literal data structures
[814.58 --> 815.86]  to define a DSL.
[816.02 --> 817.06]  It was ugly.
[817.50 --> 817.84]  I mean,
[817.84 --> 819.12]  it was very ugly.
[820.18 --> 821.78]  And I think
[821.78 --> 822.66]  it clicked
[822.66 --> 823.92]  once I saw
[823.92 --> 824.36]  the trick
[824.36 --> 825.00]  of basically
[825.00 --> 826.76]  having an anonymous
[826.76 --> 827.28]  function
[827.28 --> 828.88]  being an argument,
[829.16 --> 829.30]  right?
[829.34 --> 830.34]  That's really the trick.
[830.34 --> 831.86]  Like, once you see that,
[831.94 --> 832.82]  once you understand that,
[832.88 --> 834.20]  then everything
[834.20 --> 835.16]  kind of falls together.
[835.40 --> 836.28]  Then it's easy
[836.28 --> 837.16]  to sort of
[837.16 --> 838.30]  embed those function
[838.30 --> 838.70]  cores
[838.70 --> 840.90]  and make it look
[840.90 --> 842.22]  like it's just
[842.22 --> 843.12]  a series of
[843.12 --> 844.14]  instructions,
[844.14 --> 846.26]  which is nice.
[846.58 --> 847.38]  But that,
[847.50 --> 847.62]  yeah,
[847.66 --> 848.12]  that took a while.
[848.52 --> 849.32]  So what has surprised
[849.32 --> 850.42]  you most about
[850.42 --> 851.92]  the explosion
[851.92 --> 853.14]  of Goa adoption?
[853.14 --> 855.16]  I was very,
[855.24 --> 856.02]  very impressed
[856.02 --> 857.84]  by how the Goa community
[857.84 --> 858.94]  and you especially
[858.94 --> 862.36]  really embraced Goa.
[863.10 --> 863.98]  I didn't think,
[864.50 --> 864.66]  you know,
[864.70 --> 864.98]  I was,
[865.16 --> 866.10]  it was more of a
[866.10 --> 867.54]  sort of personal
[867.54 --> 868.28]  research,
[868.32 --> 869.20]  interesting project,
[869.48 --> 870.60]  see what could happen.
[871.14 --> 871.70]  Also,
[871.70 --> 872.46]  with the potential
[872.46 --> 873.96]  of maybe being used
[873.96 --> 874.60]  at Ryscale.
[874.60 --> 876.78]  But that was about it.
[876.88 --> 877.20]  And then,
[877.60 --> 878.54]  I guess,
[878.60 --> 879.56]  you stumbled on it
[879.56 --> 880.02]  and started
[880.02 --> 881.30]  tweeting about it.
[881.76 --> 884.18]  And I wrote a blog post.
[884.80 --> 885.28]  Yeah,
[885.40 --> 886.18]  put me into
[886.18 --> 888.04]  the Slack channel.
[888.56 --> 890.02]  And it's been awesome.
[890.24 --> 890.46]  I mean,
[890.52 --> 890.84]  I think
[890.84 --> 892.12]  there's no way
[892.12 --> 892.72]  that Goa
[892.72 --> 893.72]  would be what it is today
[893.72 --> 894.10]  without
[894.10 --> 895.66]  that community,
[895.88 --> 896.88]  without all the input.
[897.42 --> 897.56]  you know,
[898.30 --> 899.56]  that's not just code,
[899.64 --> 900.30]  it's the ideas,
[900.46 --> 901.14]  the requirements,
[901.54 --> 903.40]  the numerous bug fixes.
[903.68 --> 903.86]  I mean,
[904.02 --> 905.06]  that to me was
[905.06 --> 906.74]  like waking up in the morning
[906.74 --> 907.76]  and seeing a PR
[907.76 --> 908.96]  where that fixes a bug
[908.96 --> 909.36]  I wrote.
[909.60 --> 910.48]  That's the best thing.
[910.90 --> 911.28]  I mean,
[911.34 --> 912.48]  there's no better way
[912.48 --> 913.14]  to start a day.
[914.02 --> 915.36]  And so,
[915.48 --> 915.60]  yeah,
[915.60 --> 916.50]  I've been very impressed.
[917.02 --> 918.00]  I'm very grateful.
[918.76 --> 921.08]  And it's been awesome.
[921.58 --> 921.60]  So,
[921.72 --> 922.72]  it's only appropriate
[922.72 --> 923.50]  that we talk about
[923.50 --> 924.40]  that blog post
[924.40 --> 924.86]  that I wrote
[924.86 --> 926.20]  because on this show,
[926.20 --> 927.02]  we have a habit
[927.02 --> 928.18]  at the end of every show
[928.18 --> 929.02]  talking about
[929.02 --> 930.76]  the Free Software Friday
[930.76 --> 931.68]  movement
[931.68 --> 932.62]  that we're trying
[932.62 --> 934.06]  to portray here.
[934.46 --> 935.14]  And that was
[935.14 --> 935.92]  the blog post
[935.92 --> 936.28]  in,
[936.46 --> 937.02]  I want to say
[937.02 --> 937.72]  it was in November
[937.72 --> 939.40]  of last year
[939.40 --> 940.32]  where I mentioned
[940.32 --> 941.10]  that I had stumbled
[941.10 --> 941.78]  across Goa
[941.78 --> 942.12]  and I thought
[942.12 --> 942.48]  it was just
[942.48 --> 943.34]  an amazing thing.
[943.98 --> 945.16]  And I was talking
[945.16 --> 945.68]  about ways
[945.68 --> 946.16]  that you could
[946.16 --> 946.86]  talk to
[946.86 --> 948.36]  open source programmers
[948.36 --> 949.52]  and thank them
[949.52 --> 950.02]  for the work
[950.02 --> 950.54]  that they do
[950.54 --> 951.24]  and tell them
[951.24 --> 952.12]  that you appreciate it.
[952.38 --> 953.14]  I think I actually
[953.14 --> 954.46]  even proposed to you.
[954.76 --> 955.28]  I'm not sure.
[955.68 --> 955.76]  Oh,
[955.80 --> 956.02]  I did.
[956.02 --> 956.24]  Yeah.
[956.46 --> 958.26]  On 17 November 2015,
[958.26 --> 960.04]  I think I want
[960.04 --> 960.68]  to marry the guy
[960.68 --> 961.46]  who wrote Goa.
[962.26 --> 962.70]  So,
[962.86 --> 964.30]  I have to apologize
[964.30 --> 964.96]  if that made you
[964.96 --> 965.36]  uncomfortable
[965.36 --> 966.10]  in any way.
[967.18 --> 967.58]  No,
[967.70 --> 968.64]  that made me laugh.
[968.74 --> 969.28]  That made me
[969.28 --> 970.50]  have to retrieve
[970.50 --> 972.00]  my lost Twitter password.
[974.84 --> 975.28]  Actually,
[975.46 --> 977.06]  I wasn't on Twitter
[977.06 --> 978.06]  at the time
[978.06 --> 979.00]  and it's a colleague
[979.00 --> 979.44]  of mine
[979.44 --> 981.24]  that saw the tweet
[981.24 --> 982.16]  and told me
[982.16 --> 982.68]  about it
[982.68 --> 984.02]  and
[984.02 --> 985.76]  they had a good laugh
[985.76 --> 986.16]  and I think
[986.16 --> 986.60]  it's,
[986.60 --> 987.80]  yeah,
[987.88 --> 988.46]  it's been great.
[988.56 --> 989.08]  I think it's,
[989.24 --> 990.08]  I really appreciate
[990.08 --> 990.72]  all the support
[990.72 --> 992.08]  that you've been giving Goa
[992.08 --> 992.56]  and I think,
[992.92 --> 993.10]  again,
[993.18 --> 993.92]  Goa wouldn't be,
[993.92 --> 994.68]  you know,
[994.88 --> 995.52]  what it is today
[995.52 --> 996.88]  without all of that support
[996.88 --> 997.68]  and all the people
[997.68 --> 998.84]  now participating
[998.84 --> 1000.10]  into the development
[1000.10 --> 1000.46]  of it.
[1000.46 --> 1001.78]  And I know
[1001.78 --> 1003.30]  it was probably
[1003.30 --> 1004.14]  a few months ago
[1004.14 --> 1004.92]  but you went
[1004.92 --> 1005.82]  through a refactoring,
[1005.90 --> 1006.00]  right,
[1006.06 --> 1006.86]  to kind of support
[1006.86 --> 1007.52]  pluggable,
[1008.06 --> 1009.76]  to create kind of
[1009.76 --> 1010.54]  plugins for stuff
[1010.54 --> 1010.92]  because I know
[1010.92 --> 1011.86]  Brian ended up
[1011.86 --> 1012.54]  going through
[1012.54 --> 1012.94]  and creating
[1012.94 --> 1013.42]  a plugin
[1013.42 --> 1015.72]  for ORM integration.
[1016.66 --> 1016.82]  Yeah,
[1016.90 --> 1017.52]  I think Goa
[1017.52 --> 1018.24]  may have caused
[1018.24 --> 1019.50]  Brian to
[1019.50 --> 1021.10]  kind of
[1021.10 --> 1022.68]  rewrite the same thing
[1022.68 --> 1023.92]  seven times in a row
[1023.92 --> 1024.88]  or something like that.
[1027.30 --> 1027.78]  So,
[1027.94 --> 1028.60]  sorry about that.
[1028.60 --> 1030.44]  But yeah,
[1030.54 --> 1030.70]  I mean,
[1030.72 --> 1031.32]  it was basically
[1031.32 --> 1031.92]  an exercise
[1031.92 --> 1033.06]  of trying
[1033.06 --> 1033.94]  to make it possible
[1033.94 --> 1035.66]  for plugins
[1035.66 --> 1036.42]  to be added
[1036.42 --> 1037.04]  to Goa
[1037.04 --> 1038.82]  at the same time
[1038.82 --> 1040.76]  that the big plugin
[1040.76 --> 1041.86]  that Brian was developing
[1041.86 --> 1042.66]  was being developed,
[1042.88 --> 1043.02]  right?
[1043.08 --> 1043.74]  So Brian wrote
[1043.74 --> 1045.70]  this amazing plugin
[1045.70 --> 1046.40]  called Gorma
[1046.40 --> 1047.40]  which allows you
[1047.40 --> 1048.98]  to define models
[1048.98 --> 1049.56]  in DSL.
[1049.64 --> 1050.22]  So now you can
[1050.22 --> 1050.92]  not only define
[1050.92 --> 1052.28]  your API shapes
[1052.28 --> 1053.42]  but you can also define
[1053.42 --> 1055.24]  the database models
[1055.24 --> 1056.64]  and from that,
[1057.34 --> 1058.48]  Gorma generates code
[1058.48 --> 1059.86]  that will instantiate
[1059.86 --> 1060.52]  those models
[1060.52 --> 1062.56]  from request bodies
[1062.56 --> 1063.32]  and then create
[1063.32 --> 1064.40]  response bodies
[1064.40 --> 1065.24]  from the model.
[1065.38 --> 1066.86]  So it makes it very easy
[1066.86 --> 1068.72]  to have a full stack
[1068.72 --> 1070.38]  kind of app
[1070.38 --> 1071.56]  in a few minutes.
[1071.70 --> 1072.38]  So it's awesome.
[1073.60 --> 1074.08]  But yeah,
[1074.22 --> 1075.20]  I was working
[1075.20 --> 1076.24]  on trying
[1076.24 --> 1077.56]  to make plugins
[1077.56 --> 1078.32]  work in Goa
[1078.32 --> 1079.16]  in the same times
[1079.16 --> 1080.88]  that Brian
[1080.88 --> 1081.32]  was working
[1081.32 --> 1081.94]  on Gorma
[1081.94 --> 1082.90]  and so,
[1083.10 --> 1083.24]  you know,
[1083.30 --> 1083.66]  I must have
[1083.66 --> 1084.98]  broken Gorma
[1084.98 --> 1086.62]  maybe 200 times.
[1086.62 --> 1087.26]  I don't know,
[1087.36 --> 1088.32]  something like that.
[1089.82 --> 1090.66]  It was a sure
[1090.66 --> 1091.66]  fun process though.
[1091.70 --> 1092.08]  It's okay.
[1092.88 --> 1093.12]  Yeah,
[1093.12 --> 1093.36]  yeah,
[1093.52 --> 1093.76]  yeah.
[1094.04 --> 1094.68]  And I think,
[1094.72 --> 1094.88]  you know,
[1094.88 --> 1095.44]  the end result
[1095.44 --> 1096.52]  is nice.
[1096.64 --> 1096.94]  I think,
[1097.02 --> 1098.56]  you know,
[1098.56 --> 1099.28]  I think anybody
[1099.28 --> 1100.54]  that now writes
[1100.54 --> 1101.42]  a plugin for Goa
[1101.42 --> 1102.96]  has to thank you.
[1103.46 --> 1105.04]  I think that's the,
[1105.20 --> 1105.38]  yeah,
[1105.50 --> 1106.56]  that should be the rule.
[1107.52 --> 1108.22]  So what's been
[1108.22 --> 1109.00]  the most surprising
[1109.00 --> 1110.04]  plugin that you've seen
[1110.04 --> 1111.08]  or the most surprising
[1111.08 --> 1112.18]  contribution to Goa?
[1112.18 --> 1112.22]  Yeah.
[1112.74 --> 1112.98]  Well,
[1113.06 --> 1113.80]  I think Gorma
[1113.80 --> 1114.88]  is definitely up there.
[1115.60 --> 1115.76]  You know,
[1115.84 --> 1116.92]  it was clearly,
[1117.64 --> 1119.76]  once you think about it,
[1120.00 --> 1121.00]  it's a use case
[1121.00 --> 1123.52]  that's really important.
[1124.10 --> 1124.70]  I just hadn't
[1124.70 --> 1125.34]  thought about it.
[1125.96 --> 1127.38]  And once you think,
[1127.46 --> 1127.68]  oh yeah,
[1127.76 --> 1128.14]  obviously,
[1128.38 --> 1128.78]  the next thing
[1128.78 --> 1129.84]  you need to do
[1129.84 --> 1131.10]  after you get
[1131.10 --> 1131.74]  your request paid
[1131.74 --> 1132.64]  is to store it.
[1132.76 --> 1132.90]  Well,
[1133.12 --> 1133.34]  yeah,
[1133.38 --> 1133.94]  you're going to need
[1133.94 --> 1136.12]  to talk to some database
[1136.12 --> 1137.16]  and yeah,
[1137.22 --> 1137.68]  you could generate
[1137.68 --> 1138.38]  code to do that.
[1139.10 --> 1139.74]  So I think
[1139.74 --> 1141.26]  that has been,
[1141.26 --> 1141.50]  you know,
[1141.50 --> 1142.70]  very interesting
[1142.70 --> 1144.18]  because I hadn't
[1144.18 --> 1144.82]  thought about it
[1144.82 --> 1145.88]  and it just makes
[1145.88 --> 1146.40]  a lot of sense
[1146.40 --> 1146.78]  and I think
[1146.78 --> 1147.30]  it's very useful.
[1147.80 --> 1149.00]  So I guess
[1149.00 --> 1149.60]  it's kind of hard
[1149.60 --> 1150.70]  to go into detail
[1150.70 --> 1153.60]  about the actual DSL itself
[1153.60 --> 1154.94]  because this is
[1154.94 --> 1156.28]  all audio based.
[1157.02 --> 1157.26]  I mean,
[1157.28 --> 1157.90]  we could draw stuff
[1157.90 --> 1158.34]  on our own
[1158.34 --> 1159.22]  individual whiteboards
[1159.22 --> 1159.94]  if we wanted to,
[1160.04 --> 1160.46]  but I don't think
[1160.46 --> 1161.46]  somehow that's going
[1161.46 --> 1162.08]  to help the listeners.
[1162.74 --> 1163.94]  So one thing
[1163.94 --> 1164.72]  I would like to talk
[1164.72 --> 1165.16]  about though
[1165.16 --> 1166.82]  is not everybody's
[1166.82 --> 1167.36]  kind of familiar
[1167.36 --> 1168.36]  with code generation.
[1168.78 --> 1170.14]  So I guess
[1170.14 --> 1171.60]  one thought process
[1171.60 --> 1172.40]  that constantly
[1172.40 --> 1173.20]  comes across people
[1173.20 --> 1173.90]  when they first hear
[1173.90 --> 1174.70]  the idea is
[1174.70 --> 1175.80]  how do you maintain
[1175.80 --> 1176.76]  generated code,
[1176.84 --> 1176.98]  right?
[1177.02 --> 1177.62]  Like if you were
[1177.62 --> 1178.50]  to modify it
[1178.50 --> 1179.20]  and you need
[1179.20 --> 1180.12]  to regenerate,
[1180.28 --> 1180.46]  you know,
[1180.50 --> 1181.12]  are you wiping
[1181.12 --> 1181.92]  over all the top
[1181.92 --> 1182.50]  of your stuff?
[1183.00 --> 1183.98]  So I'd love to kind
[1183.98 --> 1185.16]  of hear you explain
[1185.16 --> 1185.66]  kind of like
[1185.66 --> 1186.34]  what the model
[1186.34 --> 1187.62]  is for maintaining
[1187.62 --> 1188.12]  your code
[1188.12 --> 1188.90]  that's been generated
[1188.90 --> 1190.80]  and if I got
[1190.80 --> 1191.36]  a new version
[1191.36 --> 1191.88]  of Goa
[1191.88 --> 1193.08]  and wanted to
[1193.08 --> 1193.68]  take advantage
[1193.68 --> 1194.52]  of some new features
[1194.52 --> 1195.04]  or plugins,
[1195.54 --> 1196.14]  what does that look
[1196.14 --> 1196.84]  like for the code
[1196.84 --> 1197.80]  that I had to manually
[1197.80 --> 1198.70]  write as part
[1198.70 --> 1199.96]  of that API?
[1201.04 --> 1201.14]  Right.
[1201.26 --> 1202.84]  So the main idea
[1202.84 --> 1203.60]  is you don't.
[1203.88 --> 1205.24]  You do not maintain
[1205.24 --> 1205.86]  generated code.
[1206.44 --> 1206.74]  Basically,
[1206.96 --> 1207.32]  you know,
[1207.38 --> 1208.02]  the generated code
[1208.02 --> 1209.58]  is generated
[1209.58 --> 1210.80]  in its own package
[1210.80 --> 1211.86]  and you,
[1212.66 --> 1213.82]  it's cheap code.
[1214.00 --> 1214.44]  You don't have
[1214.44 --> 1215.02]  to maintain it.
[1215.08 --> 1215.38]  You don't have
[1215.38 --> 1216.04]  to test it.
[1216.20 --> 1216.64]  You don't have
[1216.64 --> 1217.62]  to really know
[1217.62 --> 1218.74]  the internals of it.
[1218.80 --> 1219.32]  You're welcome
[1219.32 --> 1219.96]  to look at them
[1219.96 --> 1220.48]  and hopefully
[1220.48 --> 1220.98]  it's understandable
[1220.98 --> 1221.98]  but you don't have to.
[1223.24 --> 1224.38]  All you care about
[1224.38 --> 1225.38]  is what it provides
[1225.38 --> 1225.80]  to you
[1225.80 --> 1226.84]  and how it interfaces
[1226.84 --> 1227.72]  with your code,
[1228.14 --> 1228.32]  right?
[1228.32 --> 1230.14]  So one of the
[1230.14 --> 1231.38]  kind of
[1231.38 --> 1232.26]  code generation
[1232.26 --> 1233.60]  principle behind Goa
[1233.60 --> 1234.48]  is that
[1234.48 --> 1236.00]  user code
[1236.00 --> 1237.88]  and generated code
[1237.88 --> 1238.60]  never mix
[1238.60 --> 1239.78]  and there is
[1239.78 --> 1241.16]  a very clear interface,
[1241.58 --> 1242.06]  an explicit,
[1242.26 --> 1242.38]  I mean,
[1242.50 --> 1243.66]  a Go interface,
[1243.80 --> 1243.90]  right?
[1243.98 --> 1245.46]  It's a very
[1245.46 --> 1246.28]  explicit interface
[1246.28 --> 1246.92]  between the two.
[1247.58 --> 1248.36]  It's not just one,
[1248.44 --> 1248.80]  it's multiple
[1248.80 --> 1249.80]  but the idea
[1249.80 --> 1250.76]  is that you have
[1250.76 --> 1252.16]  interfaces that are clear
[1252.16 --> 1253.94]  between the generated code
[1253.94 --> 1254.78]  and the user code
[1254.78 --> 1256.36]  and if you regenerate
[1256.36 --> 1256.82]  your code,
[1257.08 --> 1257.88]  you shouldn't care.
[1257.88 --> 1258.56]  I mean,
[1258.60 --> 1259.32]  basically the idea
[1259.32 --> 1260.40]  is if you
[1260.40 --> 1261.68]  change your design
[1261.68 --> 1262.44]  and you add,
[1262.52 --> 1263.02]  let's say you add
[1263.02 --> 1263.70]  a new field
[1263.70 --> 1265.08]  to a request payload,
[1265.70 --> 1266.76]  you regenerate your code,
[1266.90 --> 1267.46]  all that means
[1267.46 --> 1268.46]  is now your context
[1268.46 --> 1269.56]  subject has a new field
[1269.56 --> 1270.54]  and you can use it
[1270.54 --> 1270.98]  and that's it.
[1271.14 --> 1271.70]  You don't have to
[1271.70 --> 1273.62]  worry about anything else.
[1274.90 --> 1275.34]  Obviously,
[1275.56 --> 1276.22]  there are cases
[1276.22 --> 1278.12]  where the interface
[1278.12 --> 1278.70]  may break,
[1278.96 --> 1279.70]  they may change
[1279.70 --> 1281.00]  between different tools
[1281.00 --> 1281.78]  but in that case
[1281.78 --> 1282.58]  it should be clear,
[1282.72 --> 1283.52]  it should be you're moving
[1283.52 --> 1285.00]  from 1.0 to 2.0
[1285.00 --> 1285.76]  and you're doing
[1285.76 --> 1286.50]  that conscientiously.
[1286.64 --> 1287.24]  It shouldn't be something
[1287.24 --> 1288.14]  that is a side effect.
[1289.20 --> 1289.60]  So,
[1289.72 --> 1290.46]  I've been very careful
[1290.46 --> 1290.96]  about that
[1290.96 --> 1292.96]  because in the past
[1292.96 --> 1293.82]  I've had experience
[1293.82 --> 1294.18]  with,
[1294.18 --> 1294.40]  you know,
[1294.48 --> 1294.88]  Core Bar,
[1295.02 --> 1295.74]  IDL,
[1295.92 --> 1296.62]  MIDL
[1296.62 --> 1297.96]  and it was always
[1297.96 --> 1298.66]  very painful
[1298.66 --> 1299.68]  whenever
[1299.68 --> 1301.26]  generated code
[1301.26 --> 1302.90]  mixed with user code
[1302.90 --> 1304.08]  because now
[1304.08 --> 1304.56]  what do you do?
[1304.64 --> 1305.12]  Do you test
[1305.12 --> 1305.68]  the whole thing?
[1306.00 --> 1306.10]  So,
[1306.22 --> 1307.44]  do you now own
[1307.44 --> 1308.08]  the generated code,
[1308.18 --> 1308.32]  right?
[1308.40 --> 1309.60]  Do you need to test it
[1309.60 --> 1310.42]  to maintain it?
[1310.98 --> 1312.12]  And then you run into
[1312.12 --> 1313.58]  the issues of lifecycle
[1313.58 --> 1314.84]  when you change the source
[1314.84 --> 1315.90]  then you need to change
[1315.90 --> 1316.38]  that code.
[1316.82 --> 1316.90]  So,
[1317.00 --> 1317.82]  I know sometimes
[1317.82 --> 1318.50]  some like some
[1318.50 --> 1319.76]  MIDL generators
[1319.76 --> 1320.76]  would put markers
[1320.76 --> 1321.78]  in comments
[1321.78 --> 1322.38]  in your file,
[1322.46 --> 1322.64]  right?
[1322.68 --> 1323.24]  And then they would
[1323.24 --> 1324.34]  find those markers
[1324.34 --> 1325.20]  and change the code
[1325.20 --> 1325.64]  in between
[1325.64 --> 1326.30]  and you're not supposed
[1326.30 --> 1326.92]  to change that.
[1327.74 --> 1328.10]  So,
[1328.64 --> 1330.36]  I really wanted to try
[1330.36 --> 1331.50]  and avoid running
[1331.50 --> 1332.70]  into those issues
[1332.70 --> 1333.54]  and so
[1333.54 --> 1335.54]  all the generated code
[1335.54 --> 1336.80]  goes into a font package
[1336.80 --> 1338.02]  which you do not touch.
[1338.22 --> 1338.50]  Actually,
[1338.60 --> 1339.52]  you cannot touch it
[1339.52 --> 1341.04]  because the generator
[1341.04 --> 1341.84]  or the code generator
[1341.84 --> 1342.64]  will wipe out
[1342.64 --> 1343.44]  the entire directory
[1343.44 --> 1343.98]  every time.
[1344.82 --> 1345.30]  So,
[1345.42 --> 1346.20]  there's no way
[1346.20 --> 1346.88]  that your code
[1346.88 --> 1347.46]  is going to mix
[1347.46 --> 1348.34]  with the generated code
[1348.34 --> 1349.38]  and the interface
[1349.38 --> 1352.68]  is a Go interface,
[1352.78 --> 1353.34]  it's explicit
[1353.34 --> 1354.84]  and that's how
[1354.84 --> 1355.80]  you both
[1355.80 --> 1356.62]  could interact.
[1357.14 --> 1357.16]  So,
[1357.30 --> 1357.86]  when you say
[1357.86 --> 1359.64]  don't worry about testing
[1359.64 --> 1361.08]  the code
[1361.08 --> 1361.70]  that was
[1361.70 --> 1362.56]  auto-generated
[1362.56 --> 1364.52]  part of the code
[1364.52 --> 1366.60]  was the controllers.
[1367.48 --> 1367.98]  Are you saying,
[1368.32 --> 1368.54]  so,
[1368.74 --> 1370.28]  how is your workflow?
[1371.22 --> 1372.44]  Do you test,
[1372.72 --> 1374.24]  do you then go
[1374.24 --> 1374.78]  and manually
[1374.78 --> 1375.52]  write tests
[1375.52 --> 1376.42]  for integration,
[1376.82 --> 1379.36]  for functionality
[1379.36 --> 1381.02]  and not specifically,
[1381.18 --> 1382.30]  I'm not a huge fan
[1382.30 --> 1383.30]  of testing controllers
[1383.30 --> 1383.98]  in specific,
[1384.56 --> 1385.26]  I'm more a fan
[1385.26 --> 1386.24]  of testing integration
[1386.24 --> 1386.72]  but how,
[1387.14 --> 1387.90]  do you then go
[1387.90 --> 1388.90]  and write it manually?
[1390.18 --> 1390.38]  So,
[1390.62 --> 1390.74]  the,
[1390.74 --> 1391.54]  so,
[1391.54 --> 1393.40]  the controllers
[1393.40 --> 1393.84]  that,
[1393.84 --> 1394.44]  that Go agent
[1394.44 --> 1395.82]  generate are,
[1396.72 --> 1397.80]  this is code
[1397.80 --> 1398.40]  that you own.
[1398.82 --> 1399.26]  So,
[1399.26 --> 1399.64]  there's,
[1399.70 --> 1401.06]  there's two kinds
[1401.06 --> 1401.40]  of code
[1401.40 --> 1401.80]  that Go agent
[1401.80 --> 1402.20]  generates.
[1402.32 --> 1403.02]  One is the vast
[1403.02 --> 1404.00]  majority of the code
[1404.00 --> 1405.34]  is things that
[1405.34 --> 1405.60]  are,
[1405.78 --> 1406.18]  live in different
[1406.18 --> 1406.54]  packages
[1406.54 --> 1407.22]  that you don't
[1407.22 --> 1407.82]  worry about.
[1407.82 --> 1409.02]  but then,
[1409.02 --> 1409.68]  there's also
[1409.68 --> 1411.12]  this scaffolding code
[1411.12 --> 1411.66]  which is kind of
[1411.66 --> 1412.64]  just a bootstrap code
[1412.64 --> 1413.68]  to help you get started,
[1413.94 --> 1414.12]  right?
[1414.26 --> 1415.16]  It's not something
[1415.16 --> 1415.94]  that you're going
[1415.94 --> 1416.80]  to regenerate over time,
[1416.86 --> 1417.26]  it's something
[1417.26 --> 1418.16]  to do once
[1418.16 --> 1419.40]  and it helps you
[1419.40 --> 1420.48]  quickly compile
[1420.48 --> 1421.00]  your service
[1421.00 --> 1422.32]  and be able
[1422.32 --> 1423.12]  to test it
[1423.12 --> 1423.44]  and,
[1423.44 --> 1423.76]  and,
[1423.76 --> 1424.94]  and play with it
[1424.94 --> 1425.42]  right away.
[1425.42 --> 1426.82]  And so,
[1426.98 --> 1427.72]  for that code,
[1427.82 --> 1428.44]  that code belongs
[1428.44 --> 1428.76]  to you.
[1429.02 --> 1429.40]  That code,
[1429.50 --> 1430.24]  you test it
[1430.24 --> 1430.82]  and you maintain
[1430.82 --> 1431.22]  it like,
[1431.28 --> 1431.80]  like your code
[1431.80 --> 1432.20]  and actually,
[1432.32 --> 1432.96]  next time you run
[1432.96 --> 1433.28]  Go agent,
[1433.50 --> 1434.42]  it won't override
[1434.42 --> 1434.94]  those files
[1434.94 --> 1437.06]  and those files
[1437.06 --> 1438.30]  live in the main package.
[1439.54 --> 1439.96]  So,
[1440.14 --> 1440.62]  the controller
[1440.62 --> 1441.56]  lives in the main package
[1441.56 --> 1442.40]  and,
[1442.46 --> 1443.04]  and you test
[1443.04 --> 1443.76]  that you own that.
[1444.30 --> 1444.54]  The,
[1444.54 --> 1445.04]  the,
[1445.04 --> 1446.70]  the low level
[1446.70 --> 1447.26]  handlers
[1447.26 --> 1448.56]  that get generated
[1448.56 --> 1449.08]  in,
[1449.46 --> 1449.90]  by default,
[1449.98 --> 1450.44]  in the package
[1450.44 --> 1451.12]  called app,
[1451.44 --> 1452.34]  those,
[1452.56 --> 1452.80]  those,
[1453.06 --> 1453.62]  those are the ones
[1453.62 --> 1454.54]  that I'm saying
[1454.54 --> 1455.46]  you don't have to maintain,
[1455.58 --> 1456.44]  you don't have to worry about.
[1456.74 --> 1457.10]  Got it.
[1457.32 --> 1458.36]  And I wanted to say too,
[1458.50 --> 1458.94]  in prepping
[1458.94 --> 1460.12]  for this episode,
[1460.58 --> 1461.24]  I watched
[1461.24 --> 1462.70]  a talk
[1462.70 --> 1463.84]  that Brian Keltelsen
[1463.84 --> 1464.76]  gave in
[1464.76 --> 1465.18]  Tampa
[1465.18 --> 1467.44]  and it's simply amazing
[1467.44 --> 1468.10]  if you have,
[1468.52 --> 1469.42]  if you don't know Goa
[1469.42 --> 1471.04]  and have any interest
[1471.04 --> 1471.52]  at all,
[1471.96 --> 1472.60]  the talk is
[1472.60 --> 1473.60]  at an hour and 15
[1473.60 --> 1474.80]  but it's so worth it
[1474.80 --> 1475.64]  because he
[1475.64 --> 1477.84]  shows
[1477.84 --> 1479.98]  the functionalities
[1479.98 --> 1481.32]  that Goa provides
[1481.32 --> 1482.06]  in Gorma
[1482.06 --> 1483.54]  and then he shows
[1483.54 --> 1484.06]  codes
[1484.06 --> 1484.96]  and pretty much
[1484.96 --> 1486.24]  I watched the whole talk
[1486.24 --> 1487.36]  and I came away
[1487.36 --> 1488.50]  with a very good sense
[1488.50 --> 1489.18]  that I understood
[1489.18 --> 1490.18]  what Goa does
[1490.18 --> 1491.24]  and I thought
[1491.24 --> 1492.08]  it was very simple
[1492.08 --> 1492.74]  to use.
[1493.38 --> 1493.82]  Another thing
[1493.82 --> 1494.34]  that I thought
[1494.34 --> 1494.60]  was,
[1494.76 --> 1495.20]  I come from
[1495.20 --> 1496.28]  a Rails background
[1496.28 --> 1498.98]  and I saw
[1498.98 --> 1500.04]  a lot of similarities.
[1500.40 --> 1500.76]  To me,
[1500.86 --> 1501.60]  it felt like
[1501.60 --> 1502.58]  this could
[1502.58 --> 1504.06]  very much be
[1504.06 --> 1504.60]  an alternative
[1504.60 --> 1505.24]  to Rails
[1505.24 --> 1506.28]  if I wanted to do
[1506.28 --> 1508.18]  a backend app
[1508.18 --> 1509.24]  or an API app
[1509.24 --> 1510.24]  in Goa
[1510.24 --> 1511.30]  and,
[1511.38 --> 1513.34]  but except that
[1513.34 --> 1514.30]  it didn't abstract
[1514.30 --> 1515.54]  away a lot of the things
[1515.54 --> 1517.20]  I saw right there
[1517.20 --> 1518.30]  what the code
[1518.30 --> 1518.92]  was doing
[1518.92 --> 1519.54]  and it was
[1519.54 --> 1520.14]  very much
[1520.14 --> 1521.02]  under my control
[1521.02 --> 1522.42]  as opposed to
[1522.42 --> 1524.04]  just calling it
[1524.04 --> 1524.62]  abstractions
[1524.62 --> 1525.72]  that maybe
[1525.72 --> 1526.72]  I knew
[1526.72 --> 1527.46]  or maybe
[1527.46 --> 1528.02]  I didn't.
[1528.02 --> 1528.72]  Yeah,
[1528.84 --> 1529.54]  I mean,
[1529.58 --> 1530.16]  there's definitely
[1530.16 --> 1534.06]  some similarities
[1534.06 --> 1534.88]  in the way
[1534.88 --> 1535.28]  that
[1535.28 --> 1537.26]  you have controllers
[1537.26 --> 1538.74]  and you have
[1538.74 --> 1539.16]  resources
[1539.16 --> 1540.14]  and so
[1540.14 --> 1541.20]  that definitely
[1541.20 --> 1543.46]  is similar.
[1543.46 --> 1545.28]  I think also
[1545.28 --> 1547.54]  one other thing
[1547.54 --> 1548.58]  that
[1548.58 --> 1550.82]  Goa is trying
[1550.82 --> 1551.28]  to do
[1551.28 --> 1552.18]  is
[1552.18 --> 1553.12]  stay
[1553.12 --> 1554.06]  simple,
[1554.30 --> 1554.46]  right?
[1554.46 --> 1555.40]  So one other thing
[1555.40 --> 1555.74]  that
[1555.74 --> 1558.84]  we've used
[1558.84 --> 1559.62]  Rails quite a bit
[1559.62 --> 1559.98]  here
[1559.98 --> 1560.70]  and
[1560.70 --> 1562.92]  we've got an
[1562.92 --> 1563.34]  application
[1563.34 --> 1564.66]  probably way too
[1564.66 --> 1565.22]  big for what
[1565.22 --> 1565.88]  Rails was supposed
[1565.88 --> 1566.82]  to be doing
[1566.82 --> 1567.74]  and so
[1567.74 --> 1568.66]  we felt a lot of
[1568.66 --> 1569.38]  pain with
[1569.38 --> 1570.58]  some of the
[1570.58 --> 1570.98]  plugins
[1570.98 --> 1571.82]  and some of
[1571.82 --> 1572.36]  the,
[1572.76 --> 1573.36]  at some point
[1573.36 --> 1574.04]  I think we had
[1574.04 --> 1574.52]  like 100,
[1574.76 --> 1575.38]  more than 100
[1575.38 --> 1576.18]  gems we're using
[1576.18 --> 1576.58]  and so
[1576.58 --> 1577.74]  at this point
[1577.74 --> 1578.88]  it becomes
[1578.88 --> 1580.32]  almost impossible
[1580.32 --> 1581.32]  to understand
[1581.32 --> 1582.88]  the request
[1582.88 --> 1583.68]  flow throughout
[1583.68 --> 1584.44]  and so something
[1584.44 --> 1585.96]  I think Goa
[1585.96 --> 1586.56]  is trying to do
[1586.56 --> 1587.24]  is to keep
[1587.24 --> 1588.60]  things simple
[1588.60 --> 1589.14]  kind of
[1589.14 --> 1590.72]  get the best
[1590.72 --> 1591.20]  of Go,
[1591.40 --> 1591.54]  right?
[1591.58 --> 1592.36]  The Go principles
[1592.36 --> 1593.94]  of doing
[1593.94 --> 1594.76]  simple tools
[1594.76 --> 1595.32]  that do
[1595.32 --> 1596.20]  simple things
[1596.20 --> 1598.48]  and can be
[1598.48 --> 1599.44]  composed together
[1599.44 --> 1599.98]  to achieve
[1599.98 --> 1600.62]  what you want
[1600.62 --> 1601.52]  and try to get
[1601.52 --> 1602.30]  those ideas
[1602.30 --> 1603.02]  and mix them
[1603.02 --> 1604.18]  with at the same
[1604.18 --> 1604.56]  time the
[1604.56 --> 1605.40]  practicality
[1605.40 --> 1606.96]  of doing
[1606.96 --> 1607.80]  something where
[1607.80 --> 1608.94]  you don't have
[1608.94 --> 1609.52]  to rebuild
[1609.52 --> 1610.16]  everything
[1610.16 --> 1610.76]  every time.
[1611.38 --> 1611.56]  So
[1611.56 --> 1613.10]  that's
[1613.10 --> 1613.66]  I think
[1613.66 --> 1614.00]  that's a
[1614.00 --> 1614.68]  nice little
[1614.68 --> 1616.00]  kind of
[1616.00 --> 1616.64]  two goals
[1616.64 --> 1617.02]  that are a
[1617.02 --> 1617.46]  little bit
[1617.46 --> 1619.24]  opposed to
[1619.24 --> 1619.62]  each other
[1619.62 --> 1620.70]  but it's
[1620.70 --> 1620.94]  a good
[1620.94 --> 1621.32]  tension
[1621.32 --> 1622.08]  and I think
[1622.08 --> 1622.56]  Goa is trying
[1622.56 --> 1623.56]  to strike the
[1623.56 --> 1623.86]  balance
[1623.86 --> 1624.30]  between the
[1624.30 --> 1624.48]  two.
[1624.78 --> 1624.92]  Yeah,
[1624.96 --> 1625.62]  my impression
[1625.62 --> 1626.34]  was that
[1626.34 --> 1627.78]  it was very
[1627.78 --> 1629.50]  easy in the
[1629.50 --> 1630.04]  sense that
[1630.04 --> 1630.78]  when you
[1630.78 --> 1631.46]  jump into
[1631.46 --> 1632.24]  a Rails app
[1632.24 --> 1633.74]  it's very easy
[1633.74 --> 1634.40]  to get going.
[1635.08 --> 1635.56]  So it was
[1635.56 --> 1636.24]  easy in that
[1636.24 --> 1637.00]  sense but it
[1637.00 --> 1637.34]  was also
[1637.34 --> 1638.24]  simple and
[1638.24 --> 1638.94]  that's what
[1638.94 --> 1639.72]  I was trying
[1639.72 --> 1640.50]  to say
[1640.50 --> 1642.60]  in Rails
[1642.60 --> 1643.04]  I'm using
[1643.04 --> 1643.44]  a lot of
[1643.44 --> 1644.06]  abstractions
[1644.06 --> 1644.42]  that maybe
[1644.42 --> 1645.02]  I went into
[1645.02 --> 1645.38]  the Rails
[1645.38 --> 1646.20]  source code
[1646.20 --> 1646.72]  and looked
[1646.72 --> 1647.14]  at it
[1647.14 --> 1647.86]  and I know
[1647.86 --> 1648.42]  what it is
[1648.42 --> 1649.66]  but probably
[1649.66 --> 1650.46]  I didn't
[1650.46 --> 1650.86]  and with
[1650.86 --> 1652.24]  using
[1652.24 --> 1653.28]  Goa and
[1653.28 --> 1653.94]  Gorma
[1653.94 --> 1655.20]  I see
[1655.20 --> 1655.92]  everything right
[1655.92 --> 1656.18]  there.
[1656.40 --> 1657.48]  I have direct
[1657.48 --> 1658.10]  control of
[1658.10 --> 1658.62]  what's going
[1658.62 --> 1659.94]  on and
[1659.94 --> 1660.88]  it's simple.
[1661.54 --> 1661.58]  Yeah,
[1661.64 --> 1661.94]  that makes
[1661.94 --> 1662.18]  sense.
[1662.58 --> 1662.90]  I'm happy
[1662.90 --> 1663.18]  you said
[1663.18 --> 1663.38]  that.
[1663.50 --> 1663.62]  I mean
[1663.62 --> 1663.82]  that was
[1663.82 --> 1664.24]  definitely
[1664.24 --> 1665.18]  a goal
[1665.18 --> 1665.64]  too is
[1665.64 --> 1666.54]  trying to
[1666.54 --> 1667.54]  simplify
[1667.54 --> 1668.16]  things
[1668.16 --> 1668.92]  and kind
[1668.92 --> 1669.34]  of hide
[1669.34 --> 1669.58]  a lot
[1669.58 --> 1669.90]  of the
[1669.90 --> 1670.32]  complexity
[1670.32 --> 1670.90]  of hooking
[1670.90 --> 1671.64]  up the
[1671.64 --> 1672.02]  mux
[1672.02 --> 1674.00]  and so
[1674.00 --> 1674.34]  in a
[1674.34 --> 1675.04]  general code
[1675.04 --> 1676.30]  and then
[1676.30 --> 1677.24]  what you
[1677.24 --> 1677.68]  have to
[1677.68 --> 1678.04]  implement
[1678.04 --> 1678.48]  as the
[1678.48 --> 1678.88]  user
[1678.88 --> 1679.94]  should be
[1679.94 --> 1680.20]  fairly
[1680.20 --> 1680.72]  straightforward.
[1681.02 --> 1681.36]  Basically
[1681.36 --> 1681.90]  the data
[1681.90 --> 1682.32]  structures
[1682.32 --> 1682.64]  you have
[1682.64 --> 1682.92]  to deal
[1682.92 --> 1683.22]  with
[1683.22 --> 1683.88]  are the
[1683.88 --> 1684.10]  ones
[1684.10 --> 1684.62]  that you
[1684.62 --> 1685.06]  define
[1685.06 --> 1685.32]  in your
[1685.32 --> 1685.78]  design
[1685.78 --> 1686.80]  so it
[1686.80 --> 1686.94]  should
[1686.94 --> 1687.32]  all be
[1687.32 --> 1687.66]  very
[1687.66 --> 1688.34]  expected
[1688.34 --> 1689.06]  and
[1689.06 --> 1690.82]  fairly
[1690.82 --> 1691.46]  simple
[1691.46 --> 1691.86]  to use.
[1692.44 --> 1693.24]  Now I
[1693.24 --> 1693.58]  have an
[1693.58 --> 1693.88]  anecdote
[1693.88 --> 1694.56]  about that.
[1694.74 --> 1695.18]  In the
[1695.18 --> 1695.86]  Goa
[1695.86 --> 1696.18]  Slack
[1696.18 --> 1696.58]  channel
[1696.58 --> 1697.00]  and the
[1697.00 --> 1697.24]  Gopher
[1697.24 --> 1697.68]  Slack
[1697.68 --> 1698.56]  we call
[1698.56 --> 1699.12]  Raphael
[1699.12 --> 1699.54]  the
[1699.54 --> 1700.08]  godfather
[1700.08 --> 1701.60]  and that's
[1701.60 --> 1702.40]  because of
[1702.40 --> 1703.98]  his extreme
[1703.98 --> 1704.64]  dedication
[1704.64 --> 1705.54]  to the
[1705.54 --> 1705.98]  simplicity
[1705.98 --> 1706.50]  of the
[1706.50 --> 1706.98]  DSL
[1706.98 --> 1707.50]  and the
[1707.50 --> 1707.74]  user
[1707.74 --> 1708.34]  experience.
[1708.70 --> 1709.00]  He will
[1709.00 --> 1709.42]  not let
[1709.42 --> 1709.68]  anything
[1709.68 --> 1710.10]  get by
[1710.10 --> 1710.34]  that
[1710.34 --> 1711.20]  complicates
[1711.20 --> 1711.88]  the
[1711.88 --> 1712.20]  process
[1712.20 --> 1712.76]  and I
[1712.76 --> 1712.96]  really
[1712.96 --> 1713.34]  appreciate
[1713.34 --> 1713.56]  that.
[1713.66 --> 1713.92]  I think
[1713.92 --> 1714.92]  having that
[1714.92 --> 1715.60]  laser sharp
[1715.60 --> 1716.54]  focus on
[1716.54 --> 1717.84]  user experience
[1717.84 --> 1718.36]  and developer
[1718.36 --> 1719.02]  experience is
[1719.02 --> 1719.50]  what makes
[1719.50 --> 1720.06]  Goa a
[1720.06 --> 1720.62]  great tool
[1720.62 --> 1721.44]  versus
[1721.44 --> 1722.66]  many of
[1722.66 --> 1722.94]  the other
[1722.94 --> 1723.24]  code
[1723.24 --> 1723.66]  generators
[1723.66 --> 1724.10]  some of
[1724.10 --> 1724.50]  which I've
[1724.50 --> 1724.74]  written
[1724.74 --> 1725.34]  that suck.
[1725.34 --> 1726.94]  So that's
[1726.94 --> 1727.26]  important.
[1727.36 --> 1727.72]  You have to
[1727.72 --> 1728.04]  have the
[1728.04 --> 1728.50]  godfather
[1728.50 --> 1728.86]  in every
[1728.86 --> 1729.28]  project.
[1730.78 --> 1730.90]  Yeah,
[1731.02 --> 1731.42]  try to
[1731.42 --> 1732.28]  hide all
[1732.28 --> 1732.48]  the,
[1732.66 --> 1733.26]  you know,
[1733.52 --> 1734.04]  keep all
[1734.04 --> 1734.60]  the complexity
[1734.60 --> 1735.14]  below.
[1735.52 --> 1736.12]  You can look
[1736.12 --> 1736.44]  at it if
[1736.44 --> 1736.82]  you want,
[1736.98 --> 1737.82]  but you
[1737.82 --> 1738.14]  don't have
[1738.14 --> 1738.42]  to deal
[1738.42 --> 1738.72]  with it.
[1738.78 --> 1739.00]  I think
[1739.00 --> 1739.24]  it's a
[1739.24 --> 1739.38]  very
[1739.38 --> 1739.80]  interesting
[1739.80 --> 1741.24]  principle.
[1742.62 --> 1743.38]  You get
[1743.38 --> 1744.30]  developers of
[1744.30 --> 1746.04]  like in a
[1746.04 --> 1746.54]  big team,
[1746.62 --> 1746.84]  you get
[1746.84 --> 1747.60]  developers of
[1747.60 --> 1748.18]  every level
[1748.18 --> 1748.82]  that need
[1748.82 --> 1749.08]  to use
[1749.08 --> 1749.50]  your tool.
[1749.62 --> 1750.02]  And so
[1750.02 --> 1751.18]  I think
[1751.18 --> 1751.44]  you need
[1751.44 --> 1751.76]  to make
[1751.76 --> 1751.90]  it
[1751.90 --> 1752.44]  approachable
[1752.44 --> 1752.92]  so anybody
[1752.92 --> 1753.42]  can take
[1753.42 --> 1754.00]  advantage of
[1754.00 --> 1754.34]  it and
[1754.34 --> 1755.04]  leverage it.
[1755.34 --> 1756.88]  as best
[1756.88 --> 1758.00]  as possible,
[1758.10 --> 1758.22]  right?
[1758.28 --> 1758.98]  You shouldn't
[1758.98 --> 1759.48]  have to
[1759.48 --> 1760.78]  know how
[1760.78 --> 1761.26]  the tool
[1761.26 --> 1762.10]  works to
[1762.10 --> 1762.56]  take full
[1762.56 --> 1763.18]  advantage of
[1763.18 --> 1763.40]  it.
[1763.82 --> 1764.28]  I think it
[1764.28 --> 1764.62]  should be,
[1764.74 --> 1765.10]  it's the
[1765.10 --> 1766.00]  tool's job
[1766.00 --> 1767.10]  to make
[1767.10 --> 1767.86]  sure that
[1767.86 --> 1769.12]  you can use
[1769.12 --> 1769.52]  it in a way
[1769.52 --> 1770.14]  that's easy
[1770.14 --> 1770.74]  and all the
[1770.74 --> 1771.36]  complexity is
[1771.36 --> 1771.92]  hidden from
[1771.92 --> 1772.18]  you.
[1772.58 --> 1772.84]  And at the
[1772.84 --> 1773.40]  same time,
[1773.60 --> 1774.38]  if you are
[1774.38 --> 1775.16]  a more
[1775.16 --> 1775.74]  advanced user
[1775.74 --> 1776.18]  or you're
[1776.18 --> 1776.72]  curious and
[1776.72 --> 1777.02]  you can see
[1777.02 --> 1777.24]  how it
[1777.24 --> 1777.60]  works,
[1777.94 --> 1778.26]  it shouldn't
[1778.26 --> 1778.64]  be hidden
[1778.64 --> 1779.00]  either.
[1779.14 --> 1779.52]  And what's
[1779.52 --> 1779.84]  underneath
[1779.84 --> 1780.60]  should also be
[1780.60 --> 1781.18]  fairly nice
[1781.18 --> 1781.74]  design and
[1781.74 --> 1781.94]  program.
[1781.94 --> 1783.34]  But you
[1783.34 --> 1783.52]  shouldn't
[1783.52 --> 1783.88]  have to be
[1783.88 --> 1784.34]  exposed to
[1784.34 --> 1784.56]  the whole
[1784.56 --> 1785.78]  thing from
[1785.78 --> 1786.28]  the get-go.
[1786.86 --> 1787.58]  So another
[1787.58 --> 1788.14]  thing that's
[1788.14 --> 1788.68]  kind of
[1788.68 --> 1790.60]  risen in
[1790.60 --> 1791.50]  extreme popularity
[1791.50 --> 1792.22]  over the past
[1792.22 --> 1792.50]  couple of
[1792.50 --> 1793.12]  years is
[1793.12 --> 1793.60]  Swagger
[1793.60 --> 1794.66]  for doing
[1794.66 --> 1795.12]  API
[1795.12 --> 1795.92]  specifications.
[1796.96 --> 1797.38]  And as I
[1797.38 --> 1798.10]  understand it,
[1798.58 --> 1799.14]  Goa also
[1799.14 --> 1800.16]  generates all
[1800.16 --> 1800.92]  the Swagger
[1800.92 --> 1802.34]  specs so that
[1802.34 --> 1802.92]  you get the
[1802.92 --> 1803.76]  Swagger UI
[1803.76 --> 1804.84]  for free for
[1804.84 --> 1805.28]  anything that
[1805.28 --> 1805.74]  you've defined
[1805.74 --> 1806.48]  in this DSL.
[1806.48 --> 1807.10]  Yeah,
[1807.26 --> 1808.26]  Swagger was
[1808.26 --> 1809.04]  definitely a big
[1809.04 --> 1810.00]  inspiration for
[1810.00 --> 1810.80]  the abstractions
[1810.80 --> 1811.46]  in the design.
[1812.30 --> 1813.40]  So it's no
[1813.40 --> 1814.60]  coincidence that
[1814.60 --> 1815.98]  the Swagger
[1815.98 --> 1817.08]  generation is
[1817.08 --> 1819.04]  fairly complete
[1819.04 --> 1819.74]  in the sense
[1819.74 --> 1820.22]  that you can
[1820.22 --> 1822.06]  express anything
[1822.06 --> 1822.52]  that you can
[1822.52 --> 1822.92]  express in
[1822.92 --> 1823.46]  Swagger in
[1823.46 --> 1824.08]  a DSL.
[1825.26 --> 1825.62]  Actually,
[1825.80 --> 1826.04]  the first
[1826.04 --> 1829.00]  inspiration was
[1829.00 --> 1829.78]  JSON schema.
[1830.28 --> 1830.78]  I don't know
[1830.78 --> 1831.08]  if you're
[1831.08 --> 1831.64]  familiar with
[1831.64 --> 1832.58]  how Heroku
[1832.58 --> 1834.66]  document their
[1834.66 --> 1835.28]  APIs, but
[1835.28 --> 1835.62]  they use
[1835.62 --> 1836.46]  JSON schema
[1836.46 --> 1837.02]  this kind
[1837.02 --> 1837.96]  of recursive
[1837.96 --> 1839.06]  JSON schema
[1839.06 --> 1839.62]  to describe
[1839.62 --> 1840.62]  all of their
[1840.62 --> 1841.18]  APIs.
[1842.48 --> 1842.82]  And so that
[1842.82 --> 1843.20]  was kind of
[1843.20 --> 1843.72]  the initial
[1843.72 --> 1844.88]  inspiration for
[1844.88 --> 1845.94]  the abstractions
[1845.94 --> 1846.44]  in the design
[1846.44 --> 1846.86]  language.
[1847.60 --> 1848.44]  But then it
[1848.44 --> 1848.86]  so happened
[1848.86 --> 1849.68]  that Swagger
[1849.68 --> 1850.64]  is also using
[1850.64 --> 1851.26]  JSON schema
[1851.26 --> 1851.96]  for a lot
[1851.96 --> 1852.50]  of their
[1852.50 --> 1854.48]  representation
[1854.48 --> 1855.78]  of what
[1855.78 --> 1856.14]  they call
[1856.14 --> 1857.22]  the path
[1857.22 --> 1857.64]  object.
[1858.40 --> 1858.82]  And so
[1858.82 --> 1859.96]  that mapping
[1859.96 --> 1860.92]  was very
[1860.92 --> 1861.70]  easy to do
[1861.70 --> 1862.66]  and it
[1862.66 --> 1863.36]  just was
[1863.36 --> 1863.72]  sort of
[1863.72 --> 1864.16]  natural.
[1865.04 --> 1865.60]  So, yeah,
[1865.60 --> 1865.94]  I think
[1865.94 --> 1866.34]  it's great
[1866.34 --> 1867.02]  too because
[1867.02 --> 1867.86]  that means
[1867.86 --> 1868.28]  that people
[1868.28 --> 1868.86]  that already
[1868.86 --> 1869.44]  know Swagger
[1869.44 --> 1870.26]  are already
[1870.26 --> 1870.92]  used to
[1870.92 --> 1871.86]  thinking about
[1871.86 --> 1872.54]  design of
[1872.54 --> 1873.84]  APIs will
[1873.84 --> 1874.62]  feel right at
[1874.62 --> 1874.86]  home.
[1875.10 --> 1876.12]  They will have
[1876.12 --> 1876.60]  to deal with
[1876.60 --> 1876.94]  the same
[1876.94 --> 1877.74]  abstractions that
[1877.74 --> 1878.10]  they already
[1878.10 --> 1878.42]  know.
[1879.42 --> 1880.06]  And actually,
[1880.20 --> 1880.94]  I think an
[1880.94 --> 1881.42]  interesting
[1881.42 --> 1883.82]  project or
[1883.82 --> 1884.36]  add-on that
[1884.36 --> 1885.00]  could be done
[1885.00 --> 1886.30]  with Goa
[1886.30 --> 1887.16]  is a tool
[1887.16 --> 1887.46]  that would
[1887.46 --> 1888.12]  take the
[1888.12 --> 1888.50]  Swagger
[1888.50 --> 1889.14]  definition
[1889.14 --> 1889.76]  specification
[1889.76 --> 1890.60]  and generate
[1890.60 --> 1892.02]  so that the
[1892.02 --> 1892.90]  Goa DSL
[1892.90 --> 1893.30]  kind of go
[1893.30 --> 1893.54]  the other
[1893.54 --> 1894.02]  way around.
[1894.30 --> 1895.68]  So, if you
[1895.68 --> 1896.06]  write the Goa
[1896.06 --> 1896.44]  DSL, you
[1896.44 --> 1896.90]  get Swagger.
[1897.10 --> 1897.40]  It would be
[1897.40 --> 1897.96]  also interesting
[1897.96 --> 1898.58]  if you had
[1898.58 --> 1899.04]  Swagger to
[1899.04 --> 1899.58]  be able to
[1899.58 --> 1900.00]  go to a
[1900.00 --> 1900.66]  Goa DSL
[1900.66 --> 1901.36]  because then
[1901.36 --> 1902.28]  you would be
[1902.28 --> 1902.80]  able to take
[1902.80 --> 1903.40]  advantage of
[1903.40 --> 1903.94]  Goa Gen to
[1903.94 --> 1904.38]  generate all
[1904.38 --> 1904.74]  those other
[1904.74 --> 1905.10]  things.
[1905.88 --> 1906.06]  You know,
[1906.16 --> 1906.72]  if you started
[1906.72 --> 1907.12]  that to your
[1907.12 --> 1907.76]  brain.
[1907.98 --> 1908.46]  Pardon me?
[1909.04 --> 1909.70]  He's assigning
[1909.70 --> 1910.24]  that to you.
[1910.60 --> 1911.70]  I was just
[1911.70 --> 1912.02]  going to say,
[1912.14 --> 1912.74]  if you started
[1912.74 --> 1913.40]  with a Swagger
[1913.40 --> 1914.42]  specification and
[1914.42 --> 1915.14]  you generated
[1915.14 --> 1917.04]  a Goa DSL
[1917.04 --> 1918.16]  and then the
[1918.16 --> 1918.92]  Goa DSL
[1918.92 --> 1919.64]  generated a
[1919.64 --> 1919.90]  Swagger
[1919.90 --> 1920.48]  specification,
[1920.86 --> 1921.46]  you could set
[1921.46 --> 1921.98]  that thing
[1921.98 --> 1922.78]  into an
[1922.78 --> 1923.68]  endless loop
[1923.68 --> 1924.74]  and by the
[1924.74 --> 1925.08]  end of it,
[1925.10 --> 1925.48]  it would be
[1925.48 --> 1926.16]  Turing complete.
[1927.62 --> 1928.06]  Yes,
[1928.24 --> 1928.62]  it would be
[1928.62 --> 1929.10]  actually very
[1929.10 --> 1929.68]  interesting to
[1929.68 --> 1930.80]  see how the
[1930.80 --> 1931.56]  Swagger
[1931.56 --> 1932.86]  evolves over
[1932.86 --> 1933.46]  time when it
[1933.46 --> 1934.14]  degrades or,
[1934.34 --> 1934.52]  you know.
[1935.92 --> 1936.80]  Or whether it
[1936.80 --> 1937.38]  takes over the
[1937.38 --> 1938.00]  world and starts
[1938.00 --> 1938.66]  launching with
[1938.66 --> 1939.40]  your warheads.
[1940.36 --> 1941.14]  I have a
[1941.14 --> 1941.94]  question for
[1941.94 --> 1942.46]  Rafael.
[1943.38 --> 1944.26]  The views
[1944.26 --> 1945.66]  aspect or
[1945.66 --> 1946.78]  feature of
[1946.78 --> 1947.12]  Goa,
[1947.16 --> 1947.54]  I thought it
[1947.54 --> 1948.06]  was super
[1948.06 --> 1948.46]  interesting.
[1948.70 --> 1949.06]  I remember
[1949.06 --> 1949.64]  working with
[1949.64 --> 1950.34]  a Rails app,
[1950.54 --> 1951.02]  an API,
[1951.66 --> 1952.82]  that was
[1952.82 --> 1953.40]  serving
[1953.40 --> 1954.40]  cube data
[1954.40 --> 1957.32]  as restful
[1957.32 --> 1958.30]  resources and
[1958.30 --> 1959.08]  we had to
[1959.08 --> 1959.76]  do some
[1959.76 --> 1962.12]  filters that
[1962.12 --> 1963.34]  were complicated.
[1963.56 --> 1964.08]  Once I figured
[1964.08 --> 1965.16]  out a pattern,
[1965.46 --> 1965.74]  it was,
[1966.66 --> 1967.48]  we just followed
[1967.48 --> 1967.86]  the pattern.
[1967.98 --> 1968.50]  It was sort
[1968.50 --> 1969.00]  of simple.
[1969.30 --> 1969.82]  But then I
[1969.82 --> 1970.42]  ended up running
[1970.42 --> 1971.48]  with problems
[1971.48 --> 1972.16]  because we were
[1972.16 --> 1973.00]  using the
[1973.00 --> 1973.64]  Swagger
[1973.64 --> 1974.88]  documentation
[1974.88 --> 1975.54]  tool.
[1975.96 --> 1976.22]  Swagger
[1976.22 --> 1976.78]  as a
[1976.78 --> 1977.18]  documentation
[1977.18 --> 1977.68]  tool,
[1978.24 --> 1978.80]  not necessarily
[1978.80 --> 1980.42]  to design
[1980.42 --> 1980.84]  the API,
[1980.92 --> 1981.32]  but just to
[1981.32 --> 1981.84]  document the
[1981.84 --> 1982.16]  API.
[1983.02 --> 1983.90]  And so
[1983.90 --> 1984.82]  there was a
[1984.82 --> 1985.46]  mismatch
[1985.46 --> 1986.40]  there between
[1986.40 --> 1986.96]  what we were
[1986.96 --> 1987.58]  doing and
[1987.58 --> 1988.26]  between the
[1988.26 --> 1989.36]  specs that
[1989.36 --> 1989.76]  Swagger,
[1990.00 --> 1990.90]  Swagger spec,
[1991.02 --> 1991.44]  whatever the
[1991.44 --> 1991.94]  spec version
[1991.94 --> 1992.50]  was that we
[1992.50 --> 1992.90]  were using.
[1993.88 --> 1994.38]  Now,
[1995.22 --> 1996.48]  with query
[1996.48 --> 1997.16]  params and
[1997.16 --> 1999.08]  filtering features
[1999.08 --> 1999.68]  of an API,
[2000.06 --> 2000.62]  is that what the
[2000.62 --> 2001.80]  views does?
[2001.80 --> 2002.72]  Is that like
[2002.72 --> 2003.54]  if I have
[2003.54 --> 2003.98]  different
[2003.98 --> 2006.02]  filtering criteria,
[2006.28 --> 2006.70]  I can use
[2006.70 --> 2007.60]  different views
[2007.60 --> 2009.04]  to represent
[2009.04 --> 2009.46]  that?
[2009.56 --> 2009.94]  Is that what
[2009.94 --> 2010.32]  it is?
[2010.88 --> 2011.02]  Yeah.
[2011.16 --> 2011.40]  I mean,
[2011.44 --> 2011.60]  yeah,
[2011.62 --> 2012.18]  that's the
[2012.18 --> 2012.42]  idea.
[2012.64 --> 2012.82]  So,
[2013.10 --> 2013.66]  you know,
[2013.82 --> 2014.30]  the idea is
[2014.30 --> 2015.72]  that a
[2015.72 --> 2016.52]  single resource
[2016.52 --> 2017.40]  may be
[2017.40 --> 2017.88]  represented
[2017.88 --> 2018.26]  in different
[2018.26 --> 2018.62]  ways,
[2018.74 --> 2018.92]  right?
[2018.96 --> 2019.22]  You may
[2019.22 --> 2020.68]  have an
[2020.68 --> 2021.18]  index view,
[2021.26 --> 2021.68]  for example,
[2021.68 --> 2022.38]  that only has
[2022.38 --> 2023.12]  a few fields
[2023.12 --> 2023.82]  and you may
[2023.82 --> 2024.52]  have a detailed
[2024.52 --> 2025.26]  view that has
[2025.26 --> 2025.96]  other fields
[2025.96 --> 2026.42]  and you may
[2026.42 --> 2026.84]  have another
[2026.84 --> 2027.34]  view that is
[2027.34 --> 2027.88]  specialized in
[2027.88 --> 2028.16]  some other
[2028.16 --> 2028.42]  way.
[2028.42 --> 2029.60]  And so,
[2029.70 --> 2030.20]  the idea is
[2030.20 --> 2030.58]  that you
[2030.58 --> 2031.16]  shouldn't have
[2031.16 --> 2032.60]  to kind of
[2032.60 --> 2033.36]  redefine a
[2033.36 --> 2034.06]  different media
[2034.06 --> 2034.52]  type every
[2034.52 --> 2034.84]  time.
[2035.10 --> 2035.36]  So,
[2035.44 --> 2036.00]  you define
[2036.00 --> 2036.46]  your media
[2036.46 --> 2037.18]  type once,
[2037.74 --> 2038.42]  you list all
[2038.42 --> 2038.84]  the fields of
[2038.84 --> 2039.16]  the media
[2039.16 --> 2039.48]  type,
[2039.60 --> 2040.30]  and then you
[2040.30 --> 2041.16]  define views,
[2041.46 --> 2042.54]  different ways
[2042.54 --> 2043.36]  of representing
[2043.36 --> 2043.92]  that media
[2043.92 --> 2044.22]  type.
[2044.48 --> 2044.88]  And each
[2044.88 --> 2046.38]  view can
[2046.38 --> 2048.22]  define arbitrary
[2048.22 --> 2049.94]  fields that
[2049.94 --> 2050.46]  were defined
[2050.46 --> 2050.82]  on the media
[2050.82 --> 2051.08]  type.
[2051.26 --> 2051.44]  And so,
[2051.86 --> 2053.38]  and then how
[2053.38 --> 2054.80]  you produce
[2054.80 --> 2055.40]  those views
[2055.40 --> 2055.92]  from the
[2055.92 --> 2056.68]  request is
[2056.68 --> 2057.24]  really up to
[2057.24 --> 2057.84]  you.
[2058.42 --> 2059.12]  So,
[2059.22 --> 2059.42]  if you
[2059.42 --> 2059.90]  decide that
[2059.90 --> 2060.24]  you want
[2060.24 --> 2060.68]  to use
[2060.68 --> 2061.20]  a query
[2061.20 --> 2061.50]  string
[2061.50 --> 2062.02]  parameter
[2062.02 --> 2062.92]  called
[2062.92 --> 2063.34]  view,
[2063.66 --> 2064.18]  and the
[2064.18 --> 2064.56]  name can
[2064.56 --> 2065.24]  be either
[2065.24 --> 2066.12]  indexed
[2066.12 --> 2067.64]  or expanded,
[2068.44 --> 2069.54]  then great,
[2069.72 --> 2070.18]  do that.
[2070.56 --> 2071.88]  And in
[2071.88 --> 2072.50]  your controller,
[2072.62 --> 2072.84]  in your
[2072.84 --> 2073.16]  code,
[2073.54 --> 2074.48]  you basically
[2074.48 --> 2075.00]  build a
[2075.00 --> 2075.78]  response using
[2075.78 --> 2076.30]  the view
[2076.30 --> 2076.94]  that you
[2076.94 --> 2078.04]  wanted for
[2078.04 --> 2079.46]  that value
[2079.46 --> 2079.74]  of the
[2079.74 --> 2080.18]  query string.
[2081.62 --> 2081.92]  So,
[2082.26 --> 2082.76]  and that
[2082.76 --> 2083.62]  all gets
[2083.62 --> 2084.86]  also translated
[2084.86 --> 2085.46]  into the
[2085.46 --> 2085.92]  swagger
[2085.92 --> 2086.86]  that gets
[2086.86 --> 2087.44]  generated
[2087.44 --> 2088.18]  as
[2088.18 --> 2088.86]  basically
[2088.86 --> 2090.32]  different
[2090.32 --> 2094.78]  responses
[2094.78 --> 2095.84]  for the
[2095.84 --> 2096.18]  action.
[2096.74 --> 2096.84]  So,
[2097.20 --> 2097.84]  it's all
[2097.84 --> 2098.38]  documented
[2098.38 --> 2100.52]  and you
[2100.52 --> 2100.90]  get also
[2100.90 --> 2102.14]  the benefit
[2102.14 --> 2103.10]  of not
[2103.10 --> 2103.66]  having to
[2103.66 --> 2104.34]  redefine all
[2104.34 --> 2104.86]  those different
[2104.86 --> 2105.36]  media types
[2105.36 --> 2105.76]  every time.
[2106.06 --> 2106.18]  Yeah,
[2106.20 --> 2106.54]  that sounds
[2106.54 --> 2106.90]  brilliant.
[2107.18 --> 2107.76]  And I bet
[2107.76 --> 2108.12]  it's a lot
[2108.12 --> 2108.56]  easier to
[2108.56 --> 2109.30]  document as
[2109.30 --> 2109.52]  well.
[2109.86 --> 2110.06]  Yeah,
[2110.18 --> 2110.40]  yeah,
[2110.44 --> 2110.68]  I mean,
[2110.72 --> 2111.20]  it is.
[2111.28 --> 2111.52]  And I
[2111.52 --> 2112.04]  think people
[2112.04 --> 2112.82]  have a
[2112.82 --> 2113.24]  sort of
[2113.24 --> 2114.28]  instinctive
[2114.28 --> 2114.86]  understanding
[2114.86 --> 2115.24]  of it,
[2115.30 --> 2115.50]  right?
[2115.58 --> 2116.68]  It makes
[2116.68 --> 2117.12]  sense.
[2117.40 --> 2118.20]  If I want
[2118.20 --> 2118.56]  to index
[2118.56 --> 2118.74]  you,
[2118.86 --> 2119.40]  then great.
[2119.78 --> 2120.32]  It's the
[2120.32 --> 2121.02]  same backing
[2121.02 --> 2121.44]  resource,
[2121.56 --> 2121.76]  it's just
[2121.76 --> 2122.18]  different ways
[2122.18 --> 2122.70]  of representing
[2122.70 --> 2122.92]  it.
[2122.94 --> 2123.02]  So,
[2123.06 --> 2123.24]  I don't
[2123.24 --> 2123.60]  think it's
[2123.60 --> 2124.20]  a very
[2124.20 --> 2124.80]  complicated
[2124.80 --> 2125.98]  abstraction
[2125.98 --> 2127.08]  and it
[2127.08 --> 2127.58]  does add
[2127.58 --> 2127.96]  a lot
[2127.96 --> 2129.48]  to the
[2129.48 --> 2130.54]  DSL.
[2131.02 --> 2131.24]  So,
[2131.38 --> 2131.78]  I'd like to
[2131.78 --> 2132.16]  make...
[2132.16 --> 2133.12]  What's that?
[2133.50 --> 2133.98]  I'm just
[2133.98 --> 2134.26]  saying I
[2134.26 --> 2134.66]  completely
[2134.66 --> 2135.12]  agree with
[2135.12 --> 2135.22]  that.
[2135.30 --> 2135.52]  I love
[2135.52 --> 2136.44]  the idea
[2136.44 --> 2137.02]  of views
[2137.02 --> 2137.98]  having the
[2137.98 --> 2138.92]  same resource
[2138.92 --> 2139.50]  represented
[2139.50 --> 2140.30]  slightly
[2140.30 --> 2140.70]  differently
[2140.70 --> 2141.52]  for a
[2141.52 --> 2141.72]  different
[2141.72 --> 2142.18]  use case
[2142.18 --> 2142.68]  doesn't mean
[2142.68 --> 2142.98]  you should
[2142.98 --> 2143.30]  have to
[2143.30 --> 2143.58]  write a
[2143.58 --> 2143.80]  ton of
[2143.80 --> 2144.02]  different
[2144.02 --> 2144.38]  code.
[2144.70 --> 2145.20]  You just
[2145.20 --> 2145.64]  ask for
[2145.64 --> 2146.18]  that resource
[2146.18 --> 2146.86]  with a
[2146.86 --> 2147.20]  specific
[2147.20 --> 2147.52]  view.
[2148.90 --> 2149.30]  Yep.
[2149.86 --> 2150.26]  So,
[2150.34 --> 2150.72]  I'd like to
[2150.72 --> 2151.00]  make sure
[2151.00 --> 2151.30]  we have
[2151.30 --> 2151.96]  time to
[2151.96 --> 2152.46]  do a
[2152.46 --> 2153.22]  fireside
[2153.22 --> 2153.66]  chat,
[2153.98 --> 2154.28]  you know,
[2154.50 --> 2155.00]  talking about
[2155.00 --> 2155.90]  news and
[2155.90 --> 2156.72]  projects and
[2156.72 --> 2157.06]  stuff we've
[2157.06 --> 2157.48]  run across
[2157.48 --> 2157.84]  together.
[2158.34 --> 2158.44]  So,
[2158.54 --> 2159.02]  before we
[2159.02 --> 2159.64]  move on
[2159.64 --> 2160.40]  off of
[2160.40 --> 2160.78]  Goa,
[2161.00 --> 2161.66]  I'd just
[2161.66 --> 2161.86]  kind of
[2161.86 --> 2162.08]  like to
[2162.08 --> 2162.30]  hear from
[2162.30 --> 2162.42]  you,
[2162.52 --> 2162.98]  what's
[2162.98 --> 2163.46]  next for
[2163.46 --> 2163.74]  Goa?
[2164.12 --> 2164.70]  What kind
[2164.70 --> 2165.60]  of functionality
[2165.60 --> 2166.02]  are you
[2166.02 --> 2166.40]  looking to
[2166.40 --> 2166.84]  add here
[2166.84 --> 2167.02]  in the
[2167.02 --> 2167.50]  near future?
[2168.32 --> 2168.54]  Yep.
[2169.12 --> 2169.48]  So,
[2169.60 --> 2169.76]  there are
[2169.76 --> 2169.96]  a couple
[2169.96 --> 2170.90]  of things
[2170.90 --> 2171.42]  that...
[2172.68 --> 2173.44]  Goa is
[2173.44 --> 2174.10]  not 1.0
[2174.10 --> 2174.38]  yet,
[2174.58 --> 2175.22]  so I
[2175.22 --> 2175.56]  think the
[2175.56 --> 2176.00]  new future
[2176.00 --> 2176.28]  is going
[2176.28 --> 2176.66]  to be
[2176.66 --> 2177.50]  finishing
[2177.50 --> 2178.12]  1.0.
[2178.18 --> 2178.40]  And we
[2178.40 --> 2178.72]  are very
[2178.72 --> 2179.14]  close.
[2179.88 --> 2180.86]  What I
[2180.86 --> 2181.12]  think would
[2181.12 --> 2181.58]  make sense
[2181.58 --> 2182.12]  is to
[2182.12 --> 2182.82]  finish up
[2182.82 --> 2183.52]  the security
[2183.52 --> 2184.22]  examples
[2184.22 --> 2184.78]  that we've
[2184.78 --> 2185.10]  started,
[2185.36 --> 2186.34]  because that's
[2186.34 --> 2186.74]  an area
[2186.74 --> 2187.18]  that can
[2187.18 --> 2187.66]  get a bit
[2187.66 --> 2188.90]  hairier than
[2188.90 --> 2189.16]  the other
[2189.16 --> 2189.54]  areas,
[2189.62 --> 2189.84]  so having
[2189.84 --> 2190.46]  good examples
[2190.46 --> 2190.86]  around that
[2190.86 --> 2191.42]  makes a lot
[2191.42 --> 2191.80]  of sense.
[2192.68 --> 2192.98]  So,
[2193.34 --> 2193.60]  finishing
[2193.60 --> 2194.28]  those examples,
[2194.90 --> 2195.44]  making sure
[2195.44 --> 2195.88]  everybody is
[2195.88 --> 2196.30]  happy with
[2196.30 --> 2196.58]  those,
[2196.80 --> 2197.58]  and then I
[2197.58 --> 2197.88]  think at
[2197.88 --> 2198.32]  that point
[2198.32 --> 2198.78]  we'll be
[2198.78 --> 2199.40]  ready to
[2199.40 --> 2200.82]  freeze and
[2200.82 --> 2201.38]  kind of
[2201.38 --> 2202.12]  ship 1.0,
[2202.26 --> 2202.48]  whatever
[2202.68 --> 2202.98]  means.
[2203.82 --> 2204.34]  But the
[2204.34 --> 2204.66]  idea is
[2204.66 --> 2205.06]  that then
[2205.06 --> 2205.50]  that is
[2205.50 --> 2205.86]  stable.
[2206.18 --> 2206.66]  So if
[2206.66 --> 2207.04]  you were
[2207.04 --> 2207.72]  waiting for
[2207.72 --> 2208.02]  Goa to
[2208.02 --> 2208.46]  be stable
[2208.46 --> 2208.90]  to use
[2208.90 --> 2209.06]  it,
[2209.16 --> 2209.38]  there you
[2209.38 --> 2209.56]  go,
[2209.70 --> 2209.88]  now you
[2209.88 --> 2210.20]  can start
[2210.20 --> 2210.64]  using it.
[2211.34 --> 2211.94]  And now
[2211.94 --> 2212.76]  for moving
[2212.76 --> 2213.22]  on for
[2213.22 --> 2214.12]  VNEX 2.0,
[2214.56 --> 2215.62]  I think there's
[2215.62 --> 2216.04]  a couple of
[2216.04 --> 2216.94]  interesting areas
[2216.94 --> 2217.44]  I'm looking at
[2217.44 --> 2217.76]  right now.
[2217.86 --> 2218.26]  One is
[2218.26 --> 2220.80]  extending Goa
[2220.80 --> 2221.82]  beyond HTTP.
[2222.62 --> 2223.24]  So in
[2223.24 --> 2223.62]  particular,
[2223.88 --> 2224.12]  I've been
[2224.12 --> 2224.48]  looking at
[2224.48 --> 2225.06]  GRPC.
[2225.06 --> 2226.58]  I think it's
[2226.58 --> 2227.06]  an area
[2227.06 --> 2227.88]  that I've
[2227.88 --> 2228.74]  been asked
[2228.74 --> 2229.16]  a lot,
[2229.52 --> 2229.86]  and it's
[2229.86 --> 2230.36]  also something
[2230.36 --> 2230.76]  we are
[2230.76 --> 2231.24]  looking at
[2231.24 --> 2231.62]  here at
[2231.62 --> 2232.08]  RightScale.
[2232.64 --> 2233.50]  So I'd
[2233.50 --> 2233.92]  like to see
[2233.92 --> 2234.22]  what we
[2234.22 --> 2234.56]  can do
[2234.56 --> 2234.88]  there.
[2235.48 --> 2236.00]  It's going
[2236.00 --> 2236.12]  to be
[2236.12 --> 2236.48]  interesting
[2236.48 --> 2237.90]  because some
[2237.90 --> 2238.14]  of the
[2238.14 --> 2238.86]  abstractions
[2238.86 --> 2240.20]  don't match
[2240.20 --> 2241.06]  exactly the
[2241.06 --> 2242.12]  HTTP rest
[2242.12 --> 2242.70]  abstractions,
[2242.86 --> 2243.14]  so we're
[2243.14 --> 2243.72]  going to have
[2243.72 --> 2245.06]  to come up
[2245.06 --> 2245.54]  with some
[2245.54 --> 2246.72]  interesting
[2246.72 --> 2247.56]  solutions there,
[2247.68 --> 2248.12]  but I think
[2248.12 --> 2248.64]  it makes
[2248.64 --> 2248.94]  sense.
[2249.66 --> 2250.14]  And another
[2250.14 --> 2250.92]  interesting space
[2250.92 --> 2251.42]  is making
[2251.42 --> 2251.94]  the DSL
[2251.94 --> 2252.60]  engine a
[2252.60 --> 2252.96]  bit more
[2252.96 --> 2253.40]  flexible.
[2253.98 --> 2254.54]  So today
[2254.54 --> 2255.28]  we've mentioned
[2255.28 --> 2255.72]  it's possible
[2255.72 --> 2256.10]  to write
[2256.10 --> 2256.58]  plugins,
[2257.14 --> 2257.82]  and you
[2257.82 --> 2258.08]  can,
[2258.44 --> 2258.82]  no plugins
[2258.82 --> 2259.40]  can define
[2259.40 --> 2259.72]  their own
[2259.72 --> 2260.36]  DSL,
[2260.72 --> 2262.04]  and or they
[2262.04 --> 2262.56]  can define
[2262.56 --> 2262.90]  their own
[2262.90 --> 2263.30]  output,
[2263.74 --> 2264.36]  but it's a
[2264.36 --> 2264.62]  bit more
[2264.62 --> 2265.30]  difficult if
[2265.30 --> 2265.96]  you want
[2265.96 --> 2266.48]  an output
[2266.48 --> 2266.90]  from one
[2266.90 --> 2267.42]  plugin to
[2267.42 --> 2267.92]  affect the
[2267.92 --> 2268.34]  output of
[2268.34 --> 2268.66]  another
[2268.66 --> 2269.06]  plugin,
[2269.50 --> 2271.00]  or a
[2271.00 --> 2271.66]  built-in
[2271.66 --> 2272.08]  generator.
[2272.54 --> 2272.86]  So an
[2272.86 --> 2273.34]  example of
[2273.34 --> 2273.72]  that would
[2273.72 --> 2274.14]  be,
[2274.50 --> 2274.64]  you know,
[2274.68 --> 2275.08]  what if you
[2275.08 --> 2275.44]  wanted to
[2275.44 --> 2275.90]  write a
[2275.90 --> 2276.26]  security
[2276.26 --> 2277.34]  plugin,
[2277.68 --> 2277.82]  right,
[2277.88 --> 2278.88]  and there
[2278.88 --> 2279.44]  will be some
[2279.44 --> 2280.22]  DSL that
[2280.22 --> 2280.74]  you can put
[2280.74 --> 2281.02]  in your
[2281.02 --> 2281.30]  API
[2281.30 --> 2282.30]  description
[2282.30 --> 2283.10]  that says,
[2283.24 --> 2283.40]  hey,
[2283.46 --> 2284.14]  if you need
[2284.14 --> 2284.50]  to call
[2284.50 --> 2285.12]  this action,
[2285.30 --> 2285.68]  then this
[2285.68 --> 2285.98]  is the
[2285.98 --> 2286.44]  authorization
[2286.44 --> 2287.04]  middle way
[2287.04 --> 2287.38]  that you
[2287.38 --> 2287.58]  need to
[2287.58 --> 2288.04]  go through.
[2289.14 --> 2289.78]  If you
[2289.78 --> 2290.10]  wanted to
[2290.10 --> 2290.46]  do that
[2290.46 --> 2290.94]  today,
[2291.68 --> 2292.22]  it would
[2292.22 --> 2292.54]  be a bit
[2292.54 --> 2292.84]  difficult
[2292.84 --> 2293.42]  because you
[2293.42 --> 2293.90]  couldn't
[2293.90 --> 2294.58]  modify the
[2294.58 --> 2295.32]  output generated
[2295.32 --> 2295.68]  by the
[2295.68 --> 2296.10]  built-in
[2296.10 --> 2296.94]  generator for
[2296.94 --> 2298.12]  the low-level
[2298.12 --> 2299.32]  HTTP server
[2299.32 --> 2299.66]  glue.
[2301.24 --> 2301.56]  And so I
[2301.56 --> 2301.86]  think that's
[2301.86 --> 2302.46]  another interesting
[2302.46 --> 2303.12]  dimension to
[2303.12 --> 2304.24]  look at in
[2304.24 --> 2304.74]  terms of
[2304.74 --> 2305.30]  trying to
[2305.30 --> 2305.74]  make Go
[2305.74 --> 2306.14]  a bit more
[2306.14 --> 2306.80]  open and
[2306.80 --> 2307.90]  have no
[2307.90 --> 2308.32]  more people
[2308.32 --> 2309.70]  contribute more
[2309.70 --> 2310.36]  plugins to
[2310.36 --> 2310.56]  it.
[2310.74 --> 2312.74]  So this
[2312.74 --> 2313.24]  is also
[2313.24 --> 2314.30]  something I'm
[2314.30 --> 2314.92]  thinking about.
[2315.20 --> 2315.84]  This is great.
[2316.20 --> 2317.60]  If anybody
[2317.60 --> 2318.08]  wants to
[2318.08 --> 2318.66]  keep up
[2318.66 --> 2319.78]  with or
[2319.78 --> 2320.58]  investigate,
[2321.12 --> 2321.34]  Goa.
[2321.34 --> 2321.90]  Goa.
[2322.14 --> 2322.76]  design is
[2322.76 --> 2323.26]  probably the
[2323.26 --> 2323.96]  best place.
[2324.52 --> 2324.90]  I'm going to
[2324.90 --> 2325.24]  get a
[2325.24 --> 2325.86]  link there.
[2326.74 --> 2327.06]  Yes,
[2327.30 --> 2327.76]  and the
[2327.76 --> 2328.30]  Slack channel
[2328.30 --> 2328.94]  I think
[2328.94 --> 2329.32]  would be.
[2329.58 --> 2330.02]  There's a
[2330.02 --> 2330.32]  gopher
[2330.32 --> 2330.76]  academy,
[2331.30 --> 2333.00]  so gopherst.slack.com
[2333.00 --> 2334.20]  and there's
[2334.20 --> 2334.50]  a Goa
[2334.50 --> 2335.14]  channel there.
[2335.74 --> 2336.34]  That's right.
[2336.54 --> 2336.96]  And you'll
[2336.96 --> 2337.48]  be actually
[2337.48 --> 2338.22]  speaking at
[2338.22 --> 2338.72]  GopherCon
[2338.72 --> 2339.26]  this year
[2339.26 --> 2340.24]  and Brian
[2340.24 --> 2340.60]  will be
[2340.60 --> 2341.38]  speaking at
[2341.38 --> 2342.32]  abstractions
[2342.32 --> 2343.48]  about Goa
[2343.48 --> 2344.08]  as well,
[2344.20 --> 2344.56]  if I'm
[2344.56 --> 2344.90]  correct.
[2345.44 --> 2345.88]  That's right.
[2345.94 --> 2346.38]  And we have
[2346.38 --> 2346.68]  a big
[2346.68 --> 2347.04]  announcement
[2347.04 --> 2347.96]  for people
[2347.96 --> 2348.40]  who might
[2348.40 --> 2348.86]  be interested
[2348.86 --> 2349.28]  in learning
[2349.28 --> 2349.90]  about Goa
[2349.90 --> 2350.28]  at either
[2350.28 --> 2350.56]  one of
[2350.56 --> 2350.72]  those
[2350.72 --> 2351.14]  conferences.
[2351.14 --> 2351.56]  I talked
[2351.56 --> 2351.90]  to the
[2351.90 --> 2352.32]  organizer
[2352.32 --> 2352.62]  of
[2352.62 --> 2353.34]  abstractions
[2353.34 --> 2354.38]  and I
[2354.38 --> 2354.56]  talked
[2354.56 --> 2354.94]  with Eric
[2354.94 --> 2355.96]  and we
[2355.96 --> 2356.64]  both agreed
[2356.64 --> 2357.38]  to do
[2357.38 --> 2358.12]  a discount
[2358.12 --> 2358.52]  code
[2358.52 --> 2359.86]  for both
[2359.86 --> 2360.28]  conferences
[2360.28 --> 2360.88]  so you can
[2360.88 --> 2361.34]  get $50
[2361.34 --> 2362.46]  off if you
[2362.46 --> 2363.06]  book at
[2363.06 --> 2363.56]  GopherCon
[2363.56 --> 2364.54]  or abstractions
[2364.54 --> 2365.52]  if you use
[2365.52 --> 2365.96]  the code
[2365.96 --> 2366.90]  GOTIME
[2366.90 --> 2367.70]  all lowercase
[2367.70 --> 2368.58]  with no
[2368.58 --> 2369.04]  space in
[2369.04 --> 2370.04]  G-O-T-I-M-E
[2370.04 --> 2370.70]  so GOTIME
[2370.70 --> 2371.12]  will get you
[2371.12 --> 2371.82]  $50 off
[2371.82 --> 2372.40]  either conference
[2372.40 --> 2372.74]  if you want
[2372.74 --> 2373.32]  to go see
[2373.32 --> 2374.54]  Raphael talk
[2374.54 --> 2375.14]  at GopherCon
[2375.14 --> 2375.64]  or see me
[2375.64 --> 2376.14]  talk at
[2376.14 --> 2376.74]  abstractions
[2376.74 --> 2377.32]  about Goa
[2377.32 --> 2379.10]  abstractions.io
[2379.10 --> 2379.94]  is the website
[2379.94 --> 2380.86]  for abstractions
[2380.86 --> 2381.28]  and
[2381.28 --> 2382.42]  GopherCon.com
[2382.42 --> 2383.52]  for GopherCon.
[2384.12 --> 2384.36]  All right,
[2384.36 --> 2385.38]  so let's
[2385.38 --> 2385.82]  do some
[2385.82 --> 2386.72]  fireside chat
[2386.72 --> 2387.10]  here.
[2387.90 --> 2388.64]  News and
[2388.64 --> 2389.04]  interesting
[2389.04 --> 2389.74]  projects
[2389.74 --> 2390.92]  and we'd
[2390.92 --> 2391.28]  love for you
[2391.28 --> 2391.90]  to participate
[2391.90 --> 2392.36]  Raphael
[2392.36 --> 2393.00]  jump in
[2393.00 --> 2393.58]  wherever
[2393.58 --> 2394.72]  and offer
[2394.72 --> 2395.44]  your own
[2395.44 --> 2395.82]  input
[2395.82 --> 2396.58]  or things
[2396.58 --> 2396.88]  that you've
[2396.88 --> 2397.32]  come across
[2397.32 --> 2397.68]  you find
[2397.68 --> 2398.14]  interesting.
[2399.32 --> 2399.46]  Great,
[2399.70 --> 2399.88]  yep,
[2400.04 --> 2400.54]  sounds good.
[2401.38 --> 2402.06]  Who wants
[2402.06 --> 2402.32]  to kick
[2402.32 --> 2402.70]  this thing
[2402.70 --> 2403.06]  off?
[2403.70 --> 2404.04]  I'll start.
[2404.64 --> 2405.20]  I would
[2405.20 --> 2405.48]  like to
[2405.48 --> 2405.72]  mention
[2405.72 --> 2406.70]  the CLI
[2406.70 --> 2407.00]  tool
[2407.00 --> 2407.34]  that I
[2407.34 --> 2407.76]  found.
[2408.14 --> 2409.56]  The author's
[2409.56 --> 2410.18]  name is not
[2410.18 --> 2410.72]  very clear
[2410.72 --> 2411.06]  but I'm
[2411.06 --> 2411.38]  going to
[2411.38 --> 2412.00]  say that
[2412.00 --> 2412.64]  his repo
[2412.64 --> 2413.78]  is
[2413.78 --> 2414.84]  MK
[2414.84 --> 2415.92]  ideal
[2415.92 --> 2417.28]  in the
[2417.28 --> 2417.64]  project
[2417.64 --> 2417.94]  called
[2417.94 --> 2418.52]  CLI.
[2418.66 --> 2419.26]  I love
[2419.26 --> 2420.02]  it because
[2420.02 --> 2421.90]  the examples
[2421.90 --> 2422.82]  are super
[2422.82 --> 2424.44]  clear and
[2424.44 --> 2424.76]  there are
[2424.76 --> 2425.14]  tons of
[2425.14 --> 2425.60]  examples.
[2426.14 --> 2426.66]  I did a
[2426.66 --> 2427.86]  CLI app
[2427.86 --> 2428.72]  at some
[2428.72 --> 2429.30]  point in
[2429.30 --> 2429.52]  Go.
[2430.04 --> 2430.68]  If I had
[2430.68 --> 2431.28]  seen this,
[2431.36 --> 2431.52]  it would
[2431.52 --> 2431.78]  have been
[2431.78 --> 2432.32]  so much
[2432.32 --> 2432.68]  easier for
[2432.68 --> 2432.96]  me to
[2432.96 --> 2433.44]  understand
[2433.44 --> 2433.86]  how to
[2433.86 --> 2434.28]  do it.
[2434.72 --> 2435.06]  It also
[2435.06 --> 2435.98]  has not
[2435.98 --> 2436.48]  only flags
[2436.48 --> 2437.28]  but commands.
[2437.80 --> 2438.10]  Seems
[2438.10 --> 2439.06]  very clean
[2439.06 --> 2439.74]  and neat.
[2440.88 --> 2442.72]  So that's
[2442.72 --> 2443.24]  my recommendation
[2443.24 --> 2443.68]  today.
[2444.60 --> 2445.32]  How would
[2445.32 --> 2445.86]  you compare
[2445.86 --> 2446.24]  it with
[2446.24 --> 2446.88]  Cobra?
[2447.08 --> 2447.40]  I've been
[2447.40 --> 2448.00]  using Cobra
[2448.00 --> 2448.62]  for Goa
[2448.62 --> 2449.08]  but I'm
[2449.08 --> 2449.60]  curious.
[2450.66 --> 2451.54]  I thought
[2451.54 --> 2451.86]  it was
[2451.86 --> 2452.84]  easier to
[2452.84 --> 2453.48]  understand
[2453.48 --> 2454.40]  and follow
[2454.40 --> 2455.36]  and if
[2455.36 --> 2457.40]  I am
[2457.40 --> 2457.78]  going to
[2457.78 --> 2458.30]  use Cobra
[2458.30 --> 2459.42]  today because
[2459.42 --> 2459.80]  I used
[2459.80 --> 2460.26]  it before
[2460.26 --> 2460.70]  exactly.
[2460.86 --> 2461.22]  My first
[2461.22 --> 2461.48]  time I
[2461.48 --> 2461.92]  used Cobra
[2461.92 --> 2462.42]  and Viper.
[2463.48 --> 2464.16]  Today I
[2464.16 --> 2464.54]  would have
[2464.54 --> 2464.88]  an easy
[2464.88 --> 2465.32]  time.
[2465.46 --> 2465.66]  But if
[2465.66 --> 2466.06]  it was my
[2466.06 --> 2466.76]  first time
[2466.76 --> 2468.06]  this would
[2468.06 --> 2468.44]  be so
[2468.44 --> 2468.78]  easy.
[2469.04 --> 2469.60]  This would
[2469.60 --> 2469.82]  have been
[2469.82 --> 2470.18]  so easy
[2470.18 --> 2470.64]  because the
[2470.64 --> 2471.00]  documentation
[2471.00 --> 2472.86]  is amazing.
[2473.14 --> 2473.56]  Kudos to
[2473.56 --> 2475.06]  the project
[2475.06 --> 2475.52]  container.
[2476.70 --> 2478.34]  I just
[2478.34 --> 2478.98]  quickly looked
[2478.98 --> 2479.40]  at this
[2479.40 --> 2480.78]  but it
[2480.78 --> 2481.22]  seems like
[2481.22 --> 2481.72]  it has
[2481.72 --> 2483.72]  integrations
[2483.72 --> 2484.18]  for other
[2484.18 --> 2484.58]  things.
[2484.88 --> 2486.54]  You can
[2486.54 --> 2487.52]  define a
[2487.52 --> 2487.92]  particular
[2487.92 --> 2489.14]  argument as
[2489.14 --> 2489.76]  a PID
[2489.76 --> 2491.14]  file and
[2491.14 --> 2492.02]  it decodes
[2492.02 --> 2492.48]  that and
[2492.48 --> 2492.90]  gives you
[2492.90 --> 2493.50]  a pointer
[2493.50 --> 2493.84]  to the
[2493.84 --> 2494.36]  file so
[2494.36 --> 2494.60]  you can
[2494.60 --> 2495.14]  interact with
[2495.14 --> 2495.44]  it that
[2495.44 --> 2495.64]  way.
[2495.64 --> 2496.80]  It is an
[2496.80 --> 2497.12]  interesting
[2497.12 --> 2498.00]  approach with
[2498.00 --> 2498.32]  these
[2498.32 --> 2499.66]  decoders.
[2499.86 --> 2500.12]  I'll have
[2500.12 --> 2500.34]  to look
[2500.34 --> 2500.64]  into this
[2500.64 --> 2500.84]  a little
[2500.84 --> 2501.10]  more.
[2501.58 --> 2502.02]  Exactly.
[2502.66 --> 2503.60]  You can
[2503.60 --> 2506.60]  define your
[2506.60 --> 2507.52]  flags as
[2507.52 --> 2508.46]  slice or
[2508.46 --> 2510.02]  map and
[2510.02 --> 2510.46]  there are
[2510.46 --> 2510.92]  the features
[2510.92 --> 2511.26]  there.
[2511.98 --> 2512.26]  That's
[2512.26 --> 2512.58]  interesting.
[2513.30 --> 2513.86]  My
[2513.86 --> 2515.20]  edition for
[2515.20 --> 2515.70]  this week
[2515.70 --> 2516.26]  is the
[2516.26 --> 2516.70]  post by
[2516.70 --> 2517.34]  Scott Mansfield
[2517.34 --> 2517.56]  from
[2517.56 --> 2518.34]  Netflix
[2518.34 --> 2519.36]  about
[2519.36 --> 2520.04]  application
[2520.04 --> 2520.64]  data
[2520.64 --> 2521.08]  caching.
[2521.68 --> 2522.50]  It is
[2522.50 --> 2523.52]  way too
[2523.52 --> 2523.94]  in-depth
[2523.94 --> 2524.40]  and too
[2524.40 --> 2524.86]  long to
[2524.86 --> 2525.20]  discuss
[2525.20 --> 2525.44]  here.
[2525.64 --> 2526.66]  There are
[2526.66 --> 2527.04]  some
[2527.04 --> 2528.10]  interesting
[2528.10 --> 2528.58]  discussions
[2528.58 --> 2529.28]  about
[2529.28 --> 2529.74]  data
[2529.74 --> 2530.12]  storage
[2530.12 --> 2530.28]  and
[2530.28 --> 2530.46]  data
[2530.46 --> 2531.02]  structure.
[2531.74 --> 2532.94]  Go tools
[2532.94 --> 2533.98]  like the
[2533.98 --> 2534.30]  REND
[2534.30 --> 2535.10]  project which
[2535.10 --> 2535.54]  is available
[2535.54 --> 2536.06]  on GitHub
[2536.06 --> 2536.94]  open source.
[2537.68 --> 2538.50]  A very
[2538.50 --> 2539.20]  nice and
[2539.20 --> 2539.94]  technically
[2539.94 --> 2540.54]  in-depth
[2540.54 --> 2541.06]  article.
[2541.28 --> 2541.66]  Just the
[2541.66 --> 2542.40]  sort of
[2542.40 --> 2542.78]  stuff that
[2542.78 --> 2543.38]  I love to
[2543.38 --> 2543.84]  wake up to
[2543.84 --> 2544.16]  with my
[2544.16 --> 2544.50]  coffee.
[2545.26 --> 2546.04]  It even
[2546.04 --> 2546.40]  has some
[2546.40 --> 2547.00]  RocksDB in
[2547.00 --> 2547.28]  there for
[2547.28 --> 2547.44]  you,
[2547.50 --> 2547.64]  Eric.
[2548.44 --> 2549.26]  I love me
[2549.26 --> 2549.92]  some RocksDB.
[2551.36 --> 2552.56]  I read that
[2552.56 --> 2552.98]  post too.
[2552.98 --> 2553.14]  It's
[2553.14 --> 2553.34]  actually
[2553.34 --> 2553.54]  really
[2553.54 --> 2553.92]  interesting.
[2554.30 --> 2554.76]  REND
[2554.76 --> 2556.62]  is kind
[2556.62 --> 2556.94]  of wire
[2556.94 --> 2557.54]  compatible
[2557.54 --> 2558.02]  with
[2558.02 --> 2558.68]  Memcache
[2558.68 --> 2558.98]  D.
[2559.64 --> 2560.04]  Basically,
[2560.40 --> 2560.80]  what they
[2560.80 --> 2562.20]  implemented
[2562.20 --> 2563.20]  was this
[2563.20 --> 2564.22]  proxy
[2564.22 --> 2565.04]  almost in
[2565.04 --> 2565.64]  between their
[2565.64 --> 2566.48]  clients and
[2566.48 --> 2567.08]  Memcache
[2567.08 --> 2567.42]  D.
[2567.72 --> 2568.40]  They implemented
[2568.40 --> 2569.72]  an L1 and
[2569.72 --> 2570.74]  L2 cache
[2570.74 --> 2571.58]  so that
[2571.58 --> 2572.52]  Memcache
[2572.52 --> 2573.32]  D was the
[2573.32 --> 2574.66]  L1, but
[2574.66 --> 2575.22]  obviously they
[2575.22 --> 2575.74]  could swap
[2575.74 --> 2576.30]  that out.
[2576.90 --> 2577.30]  Then they
[2577.30 --> 2577.72]  were using
[2577.72 --> 2578.74]  RocksDB to
[2578.74 --> 2580.08]  communicate with
[2580.08 --> 2581.10]  their SSDs
[2581.10 --> 2581.38]  as kind
[2581.38 --> 2581.62]  of like
[2581.62 --> 2582.16]  an L2
[2582.16 --> 2582.64]  cache.
[2583.28 --> 2583.84]  All of
[2583.84 --> 2584.24]  this was
[2584.24 --> 2585.20]  to reduce
[2585.20 --> 2587.90]  their financial
[2587.90 --> 2589.10]  costs monthly
[2589.10 --> 2589.72]  for their
[2589.72 --> 2590.94]  Amazon instances
[2590.94 --> 2591.76]  for high
[2591.76 --> 2592.36]  memory because
[2592.36 --> 2592.56]  they were
[2592.56 --> 2594.04]  storing lots
[2594.04 --> 2594.62]  of user
[2594.62 --> 2596.04]  data in
[2596.04 --> 2596.44]  memory.
[2596.84 --> 2597.50]  They'd have
[2597.50 --> 2598.54]  the hot
[2598.54 --> 2599.30]  data set
[2599.30 --> 2600.14]  in a given
[2600.14 --> 2600.80]  region, but
[2600.80 --> 2601.18]  they'd also
[2601.18 --> 2601.72]  have a cold
[2601.72 --> 2602.62]  data set so
[2602.62 --> 2603.14]  in case
[2603.14 --> 2604.18]  people
[2604.18 --> 2604.88]  failed over
[2604.88 --> 2606.76]  from another
[2606.76 --> 2608.00]  region and
[2608.00 --> 2608.28]  things like
[2608.28 --> 2608.46]  that.
[2608.66 --> 2609.44]  It's really
[2609.44 --> 2610.44]  interesting how
[2610.44 --> 2610.96]  much they
[2610.96 --> 2611.80]  dropped off.
[2612.00 --> 2612.82]  I love the
[2612.82 --> 2613.16]  fact that
[2613.16 --> 2613.60]  they're using
[2613.60 --> 2614.12]  RocksDB.
[2614.48 --> 2615.08]  There's a lot
[2615.08 --> 2615.38]  of people
[2615.38 --> 2615.80]  using that
[2615.80 --> 2615.98]  now.
[2616.14 --> 2616.40]  There's a
[2616.40 --> 2616.92]  Mongo
[2616.92 --> 2618.82]  Rocks was
[2618.82 --> 2619.22]  out not
[2619.22 --> 2619.54]  too long
[2619.54 --> 2619.96]  ago.
[2622.22 --> 2622.90]  One of our
[2622.90 --> 2623.42]  other favorites,
[2623.56 --> 2624.20]  CockroachDB,
[2624.62 --> 2625.18]  they're using
[2625.18 --> 2626.28]  RocksDB under
[2626.28 --> 2626.78]  the covers,
[2627.02 --> 2627.50]  unless they've
[2627.50 --> 2627.98]  changed by
[2627.98 --> 2628.32]  now, but I
[2628.32 --> 2628.56]  think they're
[2628.56 --> 2629.00]  still using
[2629.00 --> 2629.20]  it.
[2630.32 --> 2630.96]  RocksDB
[2630.96 --> 2631.46]  actually comes
[2631.46 --> 2631.64]  out of
[2631.64 --> 2631.96]  Facebook.
[2633.20 --> 2633.64]  I definitely
[2633.64 --> 2634.08]  just want to
[2634.08 --> 2634.58]  shout out to
[2634.58 --> 2635.06]  Scott and
[2635.06 --> 2635.60]  the team at
[2635.60 --> 2636.38]  Netflix for
[2636.38 --> 2637.16]  such a nice
[2637.16 --> 2637.66]  and thorough
[2637.66 --> 2638.14]  write-up.
[2638.14 --> 2639.08]  I know
[2639.08 --> 2639.76]  Scott's been
[2639.76 --> 2640.58]  dragging the
[2640.58 --> 2640.96]  people who
[2640.96 --> 2641.46]  will listen,
[2641.86 --> 2642.88]  kicking and
[2642.88 --> 2643.42]  screaming into
[2643.42 --> 2644.06]  the Go world.
[2644.58 --> 2645.00]  Even though
[2645.00 --> 2645.62]  they're a
[2645.62 --> 2646.12]  Java-heavy
[2646.12 --> 2647.18]  shop, they
[2647.18 --> 2647.70]  do have a
[2647.70 --> 2648.04]  lot of Go
[2648.04 --> 2648.50]  behind the
[2648.50 --> 2648.98]  scenes there.
[2649.08 --> 2649.34]  They just
[2649.34 --> 2649.76]  don't talk
[2649.76 --> 2650.24]  about it a
[2650.24 --> 2650.40]  lot.
[2651.78 --> 2653.46]  I remember
[2653.46 --> 2653.94]  seeing some
[2653.94 --> 2654.10]  of the
[2654.10 --> 2654.54]  performance
[2654.54 --> 2654.92]  metrics.
[2655.12 --> 2655.54]  There was
[2655.54 --> 2656.12]  something in
[2656.12 --> 2656.44]  the neighborhood
[2656.44 --> 2657.68]  of 2 million
[2657.68 --> 2658.92]  requests per
[2658.92 --> 2659.46]  second, but I
[2659.46 --> 2659.76]  think that
[2659.76 --> 2661.32]  wasn't fully
[2661.32 --> 2661.82]  accurate because
[2661.82 --> 2662.28]  that wasn't
[2662.28 --> 2662.84]  wired up to
[2662.84 --> 2663.42]  back ends.
[2663.58 --> 2663.90]  I know when
[2663.90 --> 2664.84]  it was all
[2664.84 --> 2665.38]  said and done,
[2665.46 --> 2665.72]  the whole
[2665.72 --> 2666.60]  system was
[2666.60 --> 2667.84]  something in
[2667.84 --> 2668.20]  the neighborhood
[2668.20 --> 2669.18]  of 20 or
[2669.18 --> 2671.42]  25,000 inserts
[2671.42 --> 2672.04]  per second.
[2672.22 --> 2673.14]  But still, the
[2673.14 --> 2673.48]  amount of
[2673.48 --> 2674.12]  performance that
[2674.12 --> 2674.42]  we're getting
[2674.42 --> 2675.04]  out of this
[2675.04 --> 2676.78]  Go proxy is
[2676.78 --> 2678.06]  awesome.
[2678.92 --> 2679.66]  We'll link to
[2679.66 --> 2680.22]  that in the
[2680.22 --> 2680.82]  show notes too
[2680.82 --> 2681.26]  because that is
[2681.26 --> 2681.74]  an interesting
[2681.74 --> 2682.16]  read.
[2682.64 --> 2683.24]  Especially if
[2683.24 --> 2683.48]  you're not
[2683.48 --> 2684.02]  familiar with
[2684.02 --> 2685.08]  RocksDB and
[2685.08 --> 2685.50]  some of those
[2685.50 --> 2685.92]  things, that's
[2685.92 --> 2686.42]  fun.
[2686.88 --> 2687.36]  I'm getting to
[2687.36 --> 2687.76]  learn how
[2687.76 --> 2688.62]  log-structured
[2688.62 --> 2689.34]  merge trees
[2689.34 --> 2689.78]  work.
[2690.14 --> 2690.92]  Cassandra uses
[2690.92 --> 2691.82]  the same
[2691.82 --> 2692.60]  approach there.
[2692.60 --> 2695.04]  Another project
[2695.04 --> 2695.72]  that I've been
[2695.72 --> 2696.28]  following for a
[2696.28 --> 2696.92]  long time but
[2696.92 --> 2697.90]  really only
[2697.90 --> 2698.58]  recently has
[2698.58 --> 2699.28]  started to
[2699.28 --> 2701.22]  mature is
[2701.22 --> 2701.98]  Shield from
[2701.98 --> 2702.58]  Stark and
[2702.58 --> 2703.14]  Wayne on
[2703.14 --> 2703.38]  GitHub.
[2704.12 --> 2705.20]  You guys may
[2705.20 --> 2706.50]  remember Dr.
[2706.60 --> 2707.02]  Nick from
[2707.02 --> 2707.38]  the Ruby
[2707.38 --> 2707.82]  world.
[2708.82 --> 2709.36]  He seems to
[2709.36 --> 2710.74]  have endorsed
[2710.74 --> 2711.40]  Go or
[2711.40 --> 2712.26]  embraced Go.
[2713.24 --> 2714.58]  This tool
[2714.58 --> 2715.48]  Shield is
[2715.48 --> 2718.48]  almost a
[2718.48 --> 2719.76]  universal utility
[2719.76 --> 2720.30]  knife for
[2720.30 --> 2720.98]  backing things
[2720.98 --> 2721.22]  up.
[2721.42 --> 2721.90]  You can write
[2721.90 --> 2722.52]  plugins to
[2722.52 --> 2723.54]  back up
[2723.54 --> 2724.62]  Redis.
[2724.78 --> 2725.00]  You can
[2725.00 --> 2726.66]  back up a
[2726.66 --> 2726.96]  database.
[2727.28 --> 2727.44]  You can
[2727.44 --> 2728.10]  back up a
[2728.10 --> 2728.40]  disk.
[2728.54 --> 2728.80]  You can
[2728.80 --> 2729.30]  back up
[2729.30 --> 2730.20]  anything if
[2730.20 --> 2730.74]  you write a
[2730.74 --> 2731.26]  plugin for
[2731.26 --> 2731.52]  it.
[2732.00 --> 2733.30]  Shield, when
[2733.30 --> 2733.88]  it first came
[2733.88 --> 2735.02]  out, I read
[2735.02 --> 2735.62]  the code because
[2735.62 --> 2736.00]  there was no
[2736.00 --> 2736.64]  description in
[2736.64 --> 2737.78]  GitHub and
[2737.78 --> 2738.54]  just tried to
[2738.54 --> 2739.00]  guess what it
[2739.00 --> 2739.48]  was going to
[2739.48 --> 2740.00]  do eventually.
[2740.44 --> 2741.04]  I couldn't
[2741.04 --> 2741.50]  figure it out
[2741.50 --> 2742.08]  for quite a
[2742.08 --> 2742.46]  few months.
[2743.10 --> 2743.84]  Now it's
[2743.84 --> 2744.48]  matured quite a
[2744.48 --> 2745.02]  bit and it
[2745.02 --> 2745.72]  looks to be a
[2745.72 --> 2746.12]  really nice
[2746.12 --> 2746.54]  tool for
[2746.54 --> 2747.24]  backing up all
[2747.24 --> 2747.74]  the things.
[2748.78 --> 2749.62]  I briefly
[2749.62 --> 2750.04]  looked at
[2750.04 --> 2750.18]  that.
[2750.26 --> 2750.50]  I need to
[2750.50 --> 2750.92]  find a use
[2750.92 --> 2751.58]  case for it.
[2751.90 --> 2753.70]  I like the
[2753.70 --> 2754.22]  idea that you
[2754.22 --> 2755.34]  can wire up
[2755.34 --> 2756.84]  where it's
[2756.84 --> 2757.26]  pulling the
[2757.26 --> 2758.04]  data from and
[2758.04 --> 2758.38]  where it's
[2758.38 --> 2758.76]  pushing the
[2758.76 --> 2759.22]  data to.
[2760.16 --> 2760.90]  I need more
[2760.90 --> 2761.30]  time.
[2761.98 --> 2762.72]  Almost like the
[2762.72 --> 2763.36]  concept of
[2763.36 --> 2763.96]  Hekka we were
[2763.96 --> 2764.50]  talking about
[2764.50 --> 2765.04]  last week.
[2765.70 --> 2766.62]  This is Hekka
[2766.62 --> 2767.18]  for backups.
[2767.92 --> 2768.58]  That's actually a
[2768.58 --> 2769.12]  good comparison.
[2769.84 --> 2770.16]  Thanks for
[2770.16 --> 2770.58]  saying so.
[2772.60 --> 2773.38]  I have to make
[2773.38 --> 2773.90]  you feel better.
[2775.52 --> 2776.32]  After the code
[2776.32 --> 2776.96]  reviews I've been
[2776.96 --> 2777.48]  through this week,
[2777.52 --> 2778.10]  I'll take anything
[2778.10 --> 2778.68]  I can get.
[2781.68 --> 2782.36]  Another
[2782.36 --> 2783.42]  interesting project
[2783.42 --> 2785.34]  that I've
[2785.34 --> 2786.12]  seen was
[2786.12 --> 2787.90]  Zap from
[2787.90 --> 2789.12]  Uber, which
[2789.12 --> 2789.82]  was a
[2789.82 --> 2790.36]  structured
[2790.36 --> 2790.94]  logging
[2790.94 --> 2792.80]  framework that
[2792.80 --> 2793.66]  is supposed to
[2793.66 --> 2794.24]  have, I think,
[2794.30 --> 2795.48]  zero allocations.
[2795.98 --> 2796.96]  That was kind
[2796.96 --> 2797.38]  of interesting.
[2798.04 --> 2798.76]  We're down here
[2798.76 --> 2799.44]  in the south, so
[2799.44 --> 2800.02]  we can call that
[2800.02 --> 2800.36]  y'all.
[2800.68 --> 2801.14]  Yet another
[2801.14 --> 2801.92]  leveled logger.
[2801.92 --> 2807.30]  I really
[2807.30 --> 2807.90]  liked the
[2807.90 --> 2809.18]  structured part
[2809.18 --> 2809.82]  of that
[2809.82 --> 2810.76]  system.
[2811.20 --> 2811.72]  I remember
[2811.72 --> 2812.94]  when I worked
[2812.94 --> 2814.16]  again in the
[2814.16 --> 2814.96]  Rails app and
[2814.96 --> 2815.80]  we were using
[2815.80 --> 2816.90]  Splunk to keep
[2816.90 --> 2817.46]  track of our
[2817.46 --> 2819.46]  logs and we
[2819.46 --> 2820.80]  had to agree
[2820.80 --> 2822.26]  upon a specific
[2822.26 --> 2823.24]  way to write
[2823.24 --> 2824.18]  our code so
[2824.18 --> 2825.00]  that it will be
[2825.00 --> 2826.00]  easy to find in
[2826.00 --> 2826.62]  Splunk and we
[2826.62 --> 2827.44]  had to just
[2827.44 --> 2828.96]  like certain
[2828.96 --> 2829.96]  keywords and the
[2829.96 --> 2831.18]  ecosign and the
[2831.18 --> 2832.12]  whatever variable
[2832.12 --> 2833.16]  we wanted to
[2833.16 --> 2833.80]  look at.
[2834.40 --> 2835.40]  And we had to
[2835.40 --> 2835.98]  rely upon
[2835.98 --> 2836.96]  everybody remembering
[2836.96 --> 2837.84]  to do that.
[2838.22 --> 2839.04]  So with this
[2839.04 --> 2840.40]  structure, it
[2840.40 --> 2841.36]  just makes life
[2841.36 --> 2842.42]  so much simpler
[2842.42 --> 2843.62]  for everybody
[2843.62 --> 2845.16]  besides the fact
[2845.16 --> 2845.82]  that it seems to
[2845.82 --> 2846.48]  be very efficient
[2846.48 --> 2848.20]  and about the
[2848.20 --> 2848.78]  features.
[2849.68 --> 2849.96]  All right.
[2850.02 --> 2850.50]  Anybody have
[2850.50 --> 2850.96]  anything else
[2850.96 --> 2851.28]  they want to
[2851.28 --> 2851.92]  talk about before
[2851.92 --> 2853.32]  we kind of go
[2853.32 --> 2853.86]  on our merry
[2853.86 --> 2854.20]  way?
[2854.74 --> 2855.14]  No, it's been
[2855.14 --> 2855.58]  a pretty full
[2855.58 --> 2855.90]  show.
[2856.34 --> 2857.06]  Or not so merry
[2857.06 --> 2857.82]  for Brian who's
[2857.82 --> 2858.70]  going to get a
[2858.70 --> 2859.34]  beat down in his
[2859.34 --> 2859.72]  code review.
[2859.72 --> 2860.12]  Go back to my
[2860.12 --> 2860.60]  code review.
[2861.74 --> 2862.58]  Don't tell
[2862.58 --> 2863.18]  Blake if he's
[2863.18 --> 2863.48]  listening.
[2866.24 --> 2867.48]  So one of the
[2867.48 --> 2868.04]  things we like to
[2868.04 --> 2868.80]  do when we
[2868.80 --> 2869.78]  close the show is
[2869.78 --> 2870.18]  just kind of
[2870.18 --> 2870.98]  briefly go around
[2870.98 --> 2873.06]  and give thanks to
[2873.06 --> 2873.76]  an open source
[2873.76 --> 2875.00]  project kind of as
[2875.00 --> 2875.52]  you spoke to
[2875.52 --> 2876.36]  earlier, Raphael,
[2876.56 --> 2878.04]  to kind of to
[2878.04 --> 2878.90]  get kind of that
[2878.90 --> 2879.72]  feedback from the
[2879.72 --> 2880.44]  community sometimes
[2880.44 --> 2881.20]  makes your day.
[2881.42 --> 2882.32]  So we want to
[2882.32 --> 2882.76]  make sure that
[2882.76 --> 2883.58]  we're regularly
[2883.58 --> 2884.62]  reaching out and
[2884.62 --> 2885.70]  thanking people for
[2885.70 --> 2886.14]  the things that
[2886.14 --> 2886.60]  make our lives
[2886.60 --> 2886.94]  easier.
[2887.52 --> 2888.18]  You want to
[2888.18 --> 2888.76]  kick this off,
[2888.86 --> 2889.02]  Brian?
[2889.36 --> 2889.84]  I'll kick it
[2889.84 --> 2890.26]  off today.
[2890.26 --> 2891.08]  One of my
[2891.08 --> 2891.74]  favorite open
[2891.74 --> 2892.32]  source tools
[2892.32 --> 2893.40]  ever is
[2893.40 --> 2894.36]  NSQ from
[2894.36 --> 2894.70]  Bitly.
[2895.14 --> 2895.90]  I've used
[2895.90 --> 2897.02]  NSQ in
[2897.02 --> 2898.12]  dozens of
[2898.12 --> 2899.16]  projects and
[2899.16 --> 2900.14]  it has never
[2900.14 --> 2900.92]  ever disappointed
[2900.92 --> 2901.12]  me.
[2901.16 --> 2901.78]  It is blazing
[2901.78 --> 2902.26]  fast.
[2902.82 --> 2903.62]  It is 100%
[2903.62 --> 2904.72]  predictable and
[2904.72 --> 2905.94]  reliable and
[2905.94 --> 2906.98]  it's just amazing
[2906.98 --> 2907.94]  how much you can
[2907.94 --> 2909.24]  do with
[2909.24 --> 2910.58]  NSQ in very
[2910.58 --> 2911.94]  little code and
[2911.94 --> 2913.46]  I really appreciate
[2913.46 --> 2914.04]  the fact that they
[2914.04 --> 2914.64]  open source that.
[2914.74 --> 2915.64]  It's a great tool.
[2915.64 --> 2916.80]  What is it?
[2917.30 --> 2918.38]  NSQ is a
[2918.38 --> 2919.12]  distributed
[2919.12 --> 2920.42]  queue that's
[2920.42 --> 2921.14]  incredibly
[2921.14 --> 2921.88]  fault tolerant
[2921.88 --> 2922.88]  and really fast
[2922.88 --> 2923.32]  and it's written
[2923.32 --> 2924.58]  in Go and
[2924.58 --> 2925.60]  it's written
[2925.60 --> 2926.66]  really smartly.
[2927.50 --> 2928.10]  Yeah, and so
[2928.10 --> 2929.64]  actually Matt
[2929.64 --> 2930.44]  Richardson did a
[2930.44 --> 2931.32]  talk in
[2931.32 --> 2932.82]  Go4Con 2014
[2932.82 --> 2933.74]  on it.
[2933.98 --> 2934.34]  I think the
[2934.34 --> 2935.06]  talk was titled
[2935.06 --> 2935.52]  something like
[2935.52 --> 2936.58]  Spray Some NSQ
[2936.58 --> 2937.14]  on it or
[2937.14 --> 2937.56]  something like
[2937.56 --> 2937.78]  that.
[2937.78 --> 2937.80]  That's right,
[2937.86 --> 2937.98]  yeah.
[2938.32 --> 2938.68]  But yeah,
[2938.82 --> 2940.06]  that should be
[2940.06 --> 2940.90]  on GitHub too.
[2941.38 --> 2942.04]  And that video
[2942.04 --> 2942.88]  is up on
[2942.88 --> 2943.42]  YouTube.
[2943.80 --> 2943.90]  Yeah.
[2943.90 --> 2945.04]  How about
[2945.04 --> 2945.18]  you,
[2945.24 --> 2945.56]  Carlicia?
[2946.24 --> 2947.08]  I would like
[2947.08 --> 2947.44]  to mention
[2947.44 --> 2948.76]  today iTerm2,
[2949.14 --> 2950.38]  which I'm
[2950.38 --> 2951.74]  sure most
[2951.74 --> 2952.60]  people already
[2952.60 --> 2953.18]  use.
[2953.50 --> 2954.58]  If you don't,
[2954.68 --> 2955.36]  you definitely
[2955.36 --> 2956.40]  should check it
[2956.40 --> 2956.80]  out because
[2956.80 --> 2957.54]  eventually you
[2957.54 --> 2957.94]  will.
[2959.46 --> 2960.16]  It seems that
[2960.16 --> 2960.70]  everybody makes
[2960.70 --> 2961.56]  a transition from
[2961.56 --> 2962.22]  the normal
[2962.22 --> 2963.76]  terminal that
[2963.76 --> 2964.32]  comes with the
[2964.32 --> 2965.08]  Apple system
[2965.08 --> 2966.32]  to iTerm2.
[2966.98 --> 2968.10]  And especially
[2968.10 --> 2969.74]  the 2.9
[2969.74 --> 2971.04]  beta version,
[2971.74 --> 2972.50]  I had to
[2972.50 --> 2973.12]  download that for
[2973.12 --> 2973.68]  some reason that
[2973.68 --> 2974.10]  I forgot.
[2974.40 --> 2974.76]  And it's been
[2974.76 --> 2975.72]  a couple months
[2975.72 --> 2976.54]  and it's
[2976.54 --> 2977.10]  amazing.
[2978.20 --> 2978.98]  There are a
[2978.98 --> 2979.98]  bunch of new
[2979.98 --> 2980.68]  features that
[2980.68 --> 2981.02]  are very
[2981.02 --> 2981.36]  interesting,
[2981.48 --> 2982.00]  very useful.
[2982.94 --> 2983.60]  I'm just going
[2983.60 --> 2984.16]  to say I
[2984.16 --> 2984.78]  recommend you
[2984.78 --> 2985.28]  leave.
[2986.14 --> 2987.44]  It pops up
[2987.44 --> 2988.18]  a tip of the
[2988.18 --> 2989.06]  day every day
[2989.06 --> 2990.30]  right on the
[2990.30 --> 2990.64]  terminal.
[2990.84 --> 2991.28]  It's very
[2991.28 --> 2992.12]  non-intrusive.
[2992.24 --> 2992.72]  We can just
[2992.72 --> 2993.50]  hitscape and
[2993.50 --> 2994.16]  it'll go away.
[2995.12 --> 2995.64]  Basically,
[2996.38 --> 2997.18]  leave that on
[2997.18 --> 2997.60]  and you're
[2997.60 --> 2998.32]  going to
[2998.32 --> 2999.38]  discover a
[2999.38 --> 3000.36]  treasure trove
[3000.36 --> 3001.60]  of cool
[3001.60 --> 3002.56]  features for
[3002.56 --> 3002.96]  your terminal.
[3003.96 --> 3004.44]  There.
[3004.70 --> 3005.10]  That's it.
[3005.72 --> 3006.42]  For when I
[3006.42 --> 3007.18]  am actually on
[3007.18 --> 3007.62]  my Mac
[3007.62 --> 3008.28]  recently, I
[3008.28 --> 3008.70]  have the
[3008.70 --> 3009.24]  little tips
[3009.24 --> 3009.66]  on there.
[3009.88 --> 3010.46]  It's because
[3010.46 --> 3010.88]  it's been a
[3010.88 --> 3011.28]  while since
[3011.28 --> 3011.80]  I've explored
[3011.80 --> 3012.60]  features added,
[3012.82 --> 3013.06]  so I'm
[3013.06 --> 3013.44]  letting it
[3013.44 --> 3014.44]  annoy me
[3014.44 --> 3015.24]  periodically to
[3015.24 --> 3015.54]  tell me
[3015.54 --> 3016.04]  things that I
[3016.04 --> 3016.34]  should be
[3016.34 --> 3016.56]  doing.
[3017.14 --> 3017.52]  They've added
[3017.52 --> 3018.16]  some really
[3018.16 --> 3018.92]  radical stuff
[3018.92 --> 3019.96]  to iTerm2.
[3020.10 --> 3020.60]  The latest
[3020.60 --> 3021.32]  betas are
[3021.32 --> 3022.26]  pretty crazy in
[3022.26 --> 3022.84]  terms of the
[3022.84 --> 3024.18]  toys that they've
[3024.18 --> 3024.34]  added.
[3024.44 --> 3024.76]  I'm not sure
[3024.76 --> 3025.20]  if I'll ever
[3025.20 --> 3025.78]  use them all,
[3025.90 --> 3026.48]  but they are
[3026.48 --> 3026.88]  impressive.
[3026.88 --> 3028.14]  I get a
[3028.14 --> 3028.64]  little jealous
[3028.64 --> 3029.10]  because most
[3029.10 --> 3029.62]  of the time I
[3029.62 --> 3030.32]  work off of
[3030.32 --> 3031.38]  my Linux
[3031.38 --> 3032.10]  workstation,
[3032.70 --> 3034.48]  so GNOME
[3034.48 --> 3035.02]  Terminal I
[3035.02 --> 3035.36]  think is the
[3035.36 --> 3035.82]  current one I'm
[3035.82 --> 3037.10]  using in
[3037.10 --> 3037.76]  i3, but
[3037.76 --> 3039.74]  it's not the
[3039.74 --> 3039.98]  same.
[3042.34 --> 3043.04]  Raphael, do you
[3043.04 --> 3043.68]  have a project
[3043.68 --> 3044.20]  you'd like to
[3044.20 --> 3044.44]  thank?
[3045.22 --> 3046.44]  Yeah, actually
[3046.44 --> 3047.36]  we started
[3047.36 --> 3048.36]  using Rethink
[3048.36 --> 3050.62]  DB and it
[3050.62 --> 3051.14]  has been very
[3051.14 --> 3051.56]  interesting.
[3051.56 --> 3053.74]  I stumbled
[3053.74 --> 3054.58]  on it kind
[3054.58 --> 3055.42]  of by chance
[3055.42 --> 3055.98]  and was
[3055.98 --> 3056.84]  reading the
[3056.84 --> 3057.34]  description and
[3057.34 --> 3057.98]  the feature set
[3057.98 --> 3058.58]  and it all
[3058.58 --> 3059.10]  sounded good
[3059.10 --> 3059.82]  like it usually
[3059.82 --> 3061.58]  does, but
[3061.58 --> 3061.90]  then what
[3061.90 --> 3064.00]  really struck
[3064.00 --> 3064.60]  me is how
[3064.60 --> 3065.70]  it fit with
[3065.70 --> 3066.38]  the use case
[3066.38 --> 3066.94]  that we were
[3066.94 --> 3067.58]  after, which
[3067.58 --> 3068.90]  was trying
[3068.90 --> 3070.34]  to generate
[3070.34 --> 3071.32]  events whenever
[3071.32 --> 3072.52]  some data was
[3072.52 --> 3072.92]  updated.
[3073.74 --> 3074.02]  And so
[3074.02 --> 3074.92]  RethinkDB has
[3074.92 --> 3075.62]  that built-in,
[3075.72 --> 3076.32]  this idea of
[3076.32 --> 3076.82]  subscriptions
[3076.82 --> 3077.54]  built-in.
[3078.42 --> 3079.90]  And it's
[3079.90 --> 3081.20]  been a very
[3081.20 --> 3081.96]  interesting journey.
[3082.28 --> 3083.22]  It has changed
[3083.22 --> 3083.90]  quite a bit
[3083.90 --> 3085.60]  the way we're
[3085.60 --> 3086.20]  thinking about
[3086.20 --> 3087.02]  the design for
[3087.02 --> 3087.40]  those new
[3087.40 --> 3087.84]  services.
[3088.80 --> 3089.64]  And so I
[3089.64 --> 3090.16]  would definitely
[3090.16 --> 3091.26]  recommend people
[3091.26 --> 3092.12]  take a look at
[3092.12 --> 3092.72]  it if they
[3092.72 --> 3093.24]  haven't yet,
[3093.60 --> 3094.34]  because it
[3094.34 --> 3096.46]  does provide
[3096.46 --> 3097.68]  another dimension
[3097.68 --> 3099.48]  to how you
[3099.48 --> 3100.22]  can design your
[3100.22 --> 3100.80]  systems and
[3100.80 --> 3101.36]  take advantage
[3101.36 --> 3101.92]  of these
[3101.92 --> 3102.98]  subscriptions
[3102.98 --> 3103.72]  capabilities.
[3104.54 --> 3105.12]  So very,
[3105.24 --> 3105.80]  we're glad that
[3105.80 --> 3106.18]  they open
[3106.18 --> 3106.80]  sourced that.
[3107.90 --> 3108.96]  And something
[3108.96 --> 3109.56]  else I wanted
[3109.56 --> 3110.02]  to mention,
[3110.14 --> 3111.18]  it's not a
[3111.18 --> 3111.64]  project,
[3111.86 --> 3113.44]  but I wanted
[3113.44 --> 3113.98]  to give a
[3113.98 --> 3114.58]  shout out to
[3114.58 --> 3114.90]  all the
[3114.90 --> 3115.82]  companies that
[3115.82 --> 3116.32]  let their
[3116.32 --> 3117.04]  employees develop
[3117.04 --> 3117.42]  open source
[3117.42 --> 3118.06]  projects,
[3118.58 --> 3118.78]  right?
[3118.84 --> 3119.72]  Because it
[3119.72 --> 3120.30]  takes time.
[3121.36 --> 3122.68]  It's not that
[3122.68 --> 3123.34]  we all have to
[3123.34 --> 3123.88]  make a living.
[3124.46 --> 3124.90]  And at the end
[3124.90 --> 3125.40]  of the day,
[3125.64 --> 3126.58]  the companies
[3126.58 --> 3127.40]  that allow
[3127.40 --> 3127.94]  their employees
[3127.94 --> 3129.04]  to develop
[3129.04 --> 3129.46]  open source
[3129.46 --> 3131.42]  projects are
[3131.42 --> 3131.70]  already
[3131.70 --> 3132.38]  enablers.
[3132.68 --> 3134.24]  And I think
[3134.24 --> 3135.72]  we need to
[3135.72 --> 3137.26]  thank them
[3137.26 --> 3137.64]  for that.
[3137.64 --> 3138.02]  and I'm
[3138.02 --> 3138.52]  thankful for
[3138.52 --> 3138.80]  rescate,
[3138.86 --> 3139.16]  obviously,
[3139.48 --> 3140.16]  with Goa,
[3140.26 --> 3141.08]  but it's
[3141.08 --> 3141.58]  not just,
[3142.00 --> 3142.80]  I was also
[3142.80 --> 3143.96]  thinking about
[3143.96 --> 3146.34]  JP Robinson
[3146.34 --> 3146.96]  at New York
[3146.96 --> 3148.00]  Times doing
[3148.00 --> 3148.46]  Gizmo.
[3148.70 --> 3148.82]  I mean,
[3148.88 --> 3149.64]  there are many,
[3149.76 --> 3150.20]  many examples
[3150.20 --> 3151.12]  of people that
[3151.12 --> 3152.06]  work in
[3152.06 --> 3154.18]  industry and
[3154.18 --> 3154.96]  where their
[3154.96 --> 3156.06]  company actually
[3156.06 --> 3156.72]  pay them to
[3156.72 --> 3157.20]  develop open
[3157.20 --> 3157.94]  source projects.
[3158.28 --> 3158.78]  So I think
[3158.78 --> 3159.28]  that's awesome.
[3160.12 --> 3160.66]  And I actually
[3160.66 --> 3161.28]  get to cheat
[3161.28 --> 3162.20]  because we got
[3162.20 --> 3162.82]  to just talk
[3162.82 --> 3163.48]  about the
[3163.48 --> 3164.32]  Netflix post
[3164.32 --> 3165.26]  and RocksDB
[3165.26 --> 3166.42]  and I love
[3166.42 --> 3167.08]  RocksDB.
[3167.40 --> 3168.36]  So I'm going
[3168.36 --> 3168.62]  to give a
[3168.62 --> 3169.06]  shout out to
[3169.06 --> 3169.26]  them.
[3170.26 --> 3171.04]  That's cheating.
[3171.44 --> 3171.86]  That shouldn't
[3171.86 --> 3172.30]  even count.
[3173.08 --> 3173.78]  We're taking
[3173.78 --> 3174.26]  this one off
[3174.26 --> 3174.88]  your scoreboard,
[3174.98 --> 3175.10]  Eric.
[3176.20 --> 3176.94]  But I mean,
[3176.94 --> 3177.48]  it's awesome.
[3177.62 --> 3177.74]  I mean,
[3177.74 --> 3178.16]  if anybody
[3178.16 --> 3178.80]  hasn't played
[3178.80 --> 3179.08]  with it,
[3179.12 --> 3179.56]  they should.
[3180.16 --> 3181.04]  And even
[3181.04 --> 3181.78]  just investigating
[3181.78 --> 3182.30]  kind of how
[3182.30 --> 3182.94]  log structured
[3182.94 --> 3183.58]  merge trees
[3183.58 --> 3184.58]  work is
[3184.58 --> 3184.88]  kind of
[3184.88 --> 3185.48]  fascinating.
[3185.92 --> 3186.94]  So I think
[3186.94 --> 3187.42]  with that,
[3187.50 --> 3188.06]  we are,
[3188.10 --> 3188.46]  I think,
[3188.46 --> 3189.06]  just about
[3189.06 --> 3189.78]  out of time.
[3190.20 --> 3191.22]  So I
[3191.22 --> 3191.60]  definitely want
[3191.60 --> 3191.84]  to thank
[3191.84 --> 3192.46]  everybody for
[3192.46 --> 3192.80]  being on
[3192.80 --> 3193.40]  the show
[3193.40 --> 3193.98]  and especially
[3193.98 --> 3194.74]  Rafael for
[3194.74 --> 3195.38]  coming on
[3195.38 --> 3195.84]  and talking
[3195.84 --> 3196.50]  to us about
[3196.50 --> 3196.94]  generating
[3196.94 --> 3197.42]  all the
[3197.42 --> 3197.82]  things.
[3198.62 --> 3199.24]  Thank you.
[3199.34 --> 3199.84]  This has
[3199.84 --> 3200.34]  been great.
[3200.58 --> 3200.96]  Thank you very
[3200.96 --> 3201.18]  much.
[3201.26 --> 3201.62]  We have the
[3201.62 --> 3202.40]  godfather of
[3202.40 --> 3203.06]  code generation
[3203.06 --> 3203.74]  on the show.
[3206.30 --> 3207.32]  This has been
[3207.32 --> 3207.78]  really great.
[3208.16 --> 3208.68]  Thank you for
[3208.68 --> 3209.22]  the opportunity.
[3209.42 --> 3209.62]  I really
[3209.62 --> 3210.20]  appreciate it.
[3210.54 --> 3210.80]  And we'll
[3210.80 --> 3211.82]  have links to
[3211.82 --> 3212.50]  everything we've
[3212.50 --> 3213.04]  talked about
[3213.04 --> 3213.74]  in the show
[3213.74 --> 3215.02]  notes or if
[3215.02 --> 3215.54]  you happen to
[3215.54 --> 3216.26]  be following us
[3216.26 --> 3216.94]  on Twitter
[3216.94 --> 3217.82]  at GoTime
[3217.82 --> 3218.32]  FM.
[3218.98 --> 3219.72]  Most of this
[3219.72 --> 3220.16]  stuff should be
[3220.16 --> 3220.76]  linked there
[3220.76 --> 3221.78]  or the Slack
[3221.78 --> 3222.22]  channel.
[3222.22 --> 3223.16]  The Gopher
[3223.16 --> 3223.72]  Slack.
[3224.26 --> 3224.36]  We're
[3224.36 --> 3225.42]  GoodTime
[3225.42 --> 3226.06]  FM there as
[3226.06 --> 3226.26]  well.
[3228.12 --> 3228.60]  Yeah.
[3228.86 --> 3229.54]  So I think
[3229.54 --> 3230.64]  that is about
[3230.64 --> 3231.08]  it.
[3231.52 --> 3233.26]  I guess we'll
[3233.26 --> 3233.64]  see everybody
[3233.64 --> 3234.08]  next week.
[3234.54 --> 3234.78]  Awesome.
[3235.00 --> 3235.20]  Thanks,
[3235.26 --> 3235.52]  everybody.
[3236.04 --> 3236.46]  Thank you.
[3236.58 --> 3236.80]  Goodbye.
[3237.24 --> 3237.54]  Bye.
[3237.54 --> 3237.60]  Bye.
[3237.60 --> 3237.66]  Bye.
[3237.66 --> 3237.70]  Bye.
[3237.70 --> 3238.60]  Bye.
[3238.60 --> 3238.66]  Bye.
[3238.66 --> 3239.60]  Bye.
[3239.60 --> 3239.66]  Bye.
[3239.66 --> 3240.66]  Bye.
[3240.66 --> 3241.60]  Bye.
[3241.60 --> 3241.66]  Bye.
[3241.66 --> 3242.60]  Bye.
[3242.60 --> 3242.66]  Bye.
[3242.66 --> 3243.60]  Bye.
[3243.60 --> 3244.66]  Bye.
[3244.66 --> 3245.60]  Bye.
[3245.60 --> 3246.66]  Bye.
[3246.66 --> 3247.66]  Bye.
[3247.66 --> 3248.66]  Bye.
[3248.66 --> 3249.66]  Bye.
[3249.66 --> 3249.70]  Bye.
[3249.70 --> 3250.20]  Bye.
[3250.20 --> 3250.66]  Bye.
[3250.66 --> 3250.68]  Bye.
[3250.68 --> 3251.64]  Bye.
[3251.64 --> 3252.20]  Bye.
[3252.22 --> 3253.98]  Bye.
[3253.98 --> 3255.40]  Bye.
[3255.40 --> 3255.60]  Bye.
[3255.68 --> 3256.24]  Bye.
[3256.56 --> 3256.62]  Bye.
[3257.92 --> 3258.64]  Bye.
[3274.76 --> 3275.10]  Bye.
[3275.10 --> 3279.06]  Bye.

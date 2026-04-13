[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.74]  Head to linode.com slash Changelog.
[17.46 --> 20.04]  This episode is brought to you by DigitalOcean.
[20.38 --> 25.14]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[25.14 --> 36.82]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[37.08 --> 42.54]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[42.90 --> 46.34]  Head to do.co slash Changelog to get started with a $100 credit.
[46.64 --> 48.80]  Again, do.co slash Changelog.
[55.14 --> 61.52]  Let's do it.
[62.12 --> 63.12]  It's Go Time.
[63.64 --> 69.38]  Welcome to Go Time, a podcast where we discuss everything under the sun of Go's expanding influence.
[69.72 --> 75.08]  Cloud infrastructure, distributed systems, microservices, Kubernetes, Docker, and yes, the Go language itself.
[75.34 --> 77.10]  We record the show live on Tuesdays.
[77.14 --> 77.84]  It's a lot of fun.
[77.84 --> 82.36]  Join us in the Go Time FM channel of Go for Slack at 3 p.m. Eastern, noon Pacific.
[82.36 --> 85.72]  We also take requests at changelog.com slash request.
[85.94 --> 88.96]  Select Go Time in the dropdown and let us know what you'd like to hear about on the pod.
[89.20 --> 90.98]  Follow us on Twitter at GoTime FM.
[91.40 --> 92.50]  Okay, let's do this.
[92.68 --> 93.18]  Go Time, baby.
[95.86 --> 96.60]  Hello, everybody.
[96.90 --> 98.00]  Welcome to Go Time.
[98.18 --> 100.28]  Today, we are joined with guest Andrew Williams.
[100.54 --> 101.14]  Want to say hi, Andy?
[101.54 --> 102.00]  Hi, everybody.
[102.20 --> 103.86]  Thanks very much for inviting me along.
[103.94 --> 105.22]  It's really cool to be part of the chat.
[106.02 --> 108.92]  And then we have one of our hosts, Johnny Borsico.
[109.46 --> 110.20]  Hello, everybody.
[110.32 --> 110.98]  Good to be back.
[110.98 --> 113.08]  And myself, John Calhoun.
[113.48 --> 116.76]  So today, we're going to be talking about unusual uses for Go.
[117.48 --> 119.38]  You know, just the weird ways developers are using Go.
[119.52 --> 122.68]  Maybe not weird, but just not quite the normal ones.
[123.80 --> 128.72]  So first, we just kind of want to establish what are some of the more common use cases of Go.
[129.08 --> 133.26]  And then we're going to jump into what we consider anything that sort of falls outside of that
[133.26 --> 135.18]  is what we'd say is slightly unusual.
[135.48 --> 138.58]  That isn't to say that all of these are unusual.
[138.58 --> 140.64]  I mean, some of them are more common than others.
[140.84 --> 142.76]  So you'll see that going all different directions.
[143.28 --> 147.08]  And we're not trying to encourage anybody to not use Go for any specific reasons.
[147.30 --> 151.26]  This is more of just exploring some different ways you might use it that you might not have traditionally heard about.
[151.26 --> 155.46]  So who wants to take the common use cases?
[155.58 --> 156.36]  What do you think those are?
[157.04 --> 157.98]  I can take a stab.
[158.52 --> 159.96]  Mind if I take a first stab, Andy?
[160.34 --> 161.02]  Yeah, on you go.
[161.38 --> 161.64]  Okay.
[161.82 --> 162.06]  Okay.
[162.06 --> 173.24]  So my own personal experience is that when I first heard of Go, it was all about sort of back-end systems level kind of work,
[173.62 --> 181.48]  queuing technologies, databases, that kind of thing, like high-throughput networked applications and services.
[181.48 --> 186.86]  Like what was basically being called at the time lower-level kind of back-end things,
[186.86 --> 191.92]  as opposed to your traditional sort of web developer framework stacks, right?
[192.08 --> 194.08]  You know, that was sort of familiar with.
[194.46 --> 197.14]  And really, that's been fairly consistent.
[197.42 --> 204.36]  Up until about, I'd say, three-ish years ago, then I saw an explosion of all kinds of different uses of Go.
[204.68 --> 205.92]  But yeah, we're going to get into that.
[205.92 --> 212.46]  But that's my personal experience of what the common uses of Go have been for me until a few years ago.
[212.78 --> 215.06]  Yeah, I think that sounds about right for me as well.
[215.28 --> 218.42]  I've only really been in the community for not even two years, actually.
[218.72 --> 222.38]  So after all of these new and exciting areas started opening up,
[222.66 --> 227.72]  but the common use cases still seem to be focused around web servers, back-end systems.
[227.90 --> 230.62]  Like you say, it's where the power is at, where the examples are.
[230.62 --> 235.76]  And often, if you ask somebody, what's this language for, they're pretty much going to say,
[235.76 --> 237.26]  you know, what it was designed for.
[237.38 --> 240.02]  And I think, like you said, that's solidly where it started.
[240.50 --> 242.40]  Yeah, I'd say my experience has been pretty similar.
[242.66 --> 245.34]  I've definitely seen, like even on the web side of it,
[245.38 --> 248.86]  you see it a lot more in APIs and things that are returning JSON than with the,
[249.38 --> 253.04]  you know, like you don't see the templating library being used quite as often to generate HTML.
[253.48 --> 255.34]  You know, a lot of times when people think about web frameworks,
[255.42 --> 257.24]  they think about like Rails or something else.
[257.72 --> 259.62]  And that stuff has started to exist in Go,
[259.62 --> 264.66]  but it just wasn't nearly as common until more recently as tools have sort of started to emerge.
[264.66 --> 267.18]  Okay, let me jump into the next question.
[267.80 --> 269.96]  Before we deep dive into any specific areas,
[270.20 --> 272.80]  what is the strangest thing you've seen Go used for?
[274.72 --> 276.44]  Am I going to throw you both off with that one?
[276.94 --> 280.50]  Well, I mean, I'm biased working so much in the GUI space.
[280.58 --> 283.06]  I've seen some pretty crazy things done there.
[283.06 --> 291.84]  And there's some ideas around running user interfaces using native that's then rendered through the web browser
[291.84 --> 293.86]  instead of using the web technologies.
[294.06 --> 295.60]  That feels pretty wacky to me.
[295.82 --> 301.26]  Interesting area, like some cool applications, but not my first choice for how to build something.
[301.26 --> 305.66]  To me, JavaScript is a weird one to have in Go.
[306.10 --> 311.06]  Like specifically, I'm thinking of projects like Go4JS, Vecti.
[311.66 --> 313.40]  There's some we've got listed here.
[313.78 --> 315.18]  GoPlay.space.
[315.50 --> 316.58]  I'm not sure what that's about.
[316.86 --> 319.54]  That's kind of odd.
[320.02 --> 323.14]  And I don't know, perhaps I don't want to say,
[323.24 --> 326.78]  I don't want to sound like I'm anti-JavaScript in Go.
[326.78 --> 333.66]  But typically, the way I see it is that if I need to do JavaScript, I'll just go do JavaScript.
[334.02 --> 337.50]  I wouldn't try to sort of bring it in into my Go world.
[337.82 --> 343.36]  I don't know, like I have this odd sort of desire to use the right tool for the job.
[343.64 --> 346.76]  And to me, like trying to force that in.
[346.92 --> 348.36]  I mean, I'm sure it has its use cases.
[348.58 --> 351.60]  But I mean, for me personally, I haven't come across one where I really like,
[351.68 --> 352.04]  oh, you know what?
[352.46 --> 354.34]  Yeah, let me do some JavaScript through Go.
[354.34 --> 358.22]  So, like, yeah, it just never really felt right to me.
[358.52 --> 360.36]  I think the JavaScript one is the same for me.
[360.48 --> 362.86]  But mostly just because every time I've looked at it and been like,
[362.96 --> 363.96]  you know, I want to try this thing.
[364.00 --> 364.90]  I want to see what it's like.
[365.30 --> 366.82]  And then I look at it and I just think,
[367.14 --> 369.08]  I almost feel like I need to know JavaScript.
[369.72 --> 372.04]  And then I need to know like the Go version on top of it.
[372.42 --> 374.64]  So I'm like, if I've already learned JavaScript at this point,
[374.98 --> 378.10]  I'm not, like, there's probably some benefits in different things.
[378.40 --> 379.98]  And that's not to say that it's not a cool project.
[379.98 --> 383.20]  I definitely like that people are experimenting and trying different stuff.
[383.20 --> 384.66]  Like, I love that.
[384.78 --> 386.16]  It's just, I see it and I'm like,
[386.24 --> 388.50]  I cannot see me using this in a production environment.
[389.34 --> 390.94]  Or like trying to sell it to a manager.
[391.04 --> 392.50]  I'm like, I don't know how I'd make that sale.
[392.92 --> 394.50]  So if somebody has actually made that sale,
[394.62 --> 395.94]  please let me know how you did it.
[396.34 --> 399.06]  Because that's definitely an interesting one to pull off.
[399.58 --> 400.12]  It's a superpower.
[401.24 --> 403.34]  But yeah, like when you see those,
[403.48 --> 406.76]  like GoPlay.Space is an example of something built with Vecti and Go4JS.
[406.76 --> 407.64]  And it's really cool.
[408.16 --> 408.96]  But I'm just like,
[409.14 --> 412.32]  I sometimes wonder if like you might be better off just finding somebody who
[412.32 --> 414.12]  knows the JavaScript stuff really well and just,
[414.22 --> 415.50]  you know, doing it that way.
[415.60 --> 416.52]  But it's hard to say.
[416.66 --> 418.02]  It is cool that people are doing it.
[418.34 --> 419.14]  But on the other side,
[419.72 --> 420.98]  the WebAssembly stuff is,
[421.62 --> 422.96]  I think has a lot of potential,
[423.18 --> 424.82]  like to be really cool in the future.
[425.28 --> 425.60]  So,
[425.86 --> 428.94]  and I'm guessing things like Go4JS sort of help pave the way for that.
[429.04 --> 429.64]  So I'm like,
[429.68 --> 429.88]  all right,
[430.04 --> 430.84]  if it's helping do that,
[430.88 --> 431.72]  that's pretty awesome too.
[431.72 --> 437.10]  So I'm curious what the sort of the impetus is for doing these other things
[437.10 --> 437.52]  through,
[437.64 --> 438.30]  through Go,
[438.40 --> 438.60]  right?
[438.68 --> 439.86]  So I imagine,
[440.32 --> 440.58]  you know,
[440.60 --> 440.78]  if,
[440.86 --> 443.74]  if you're really passionate about Go and you want to use Go for all the
[443.74 --> 444.24]  things,
[444.50 --> 444.62]  right,
[444.66 --> 447.56]  maybe you can generate your JavaScript from Go and that's fine.
[448.06 --> 448.50]  Again,
[448.68 --> 449.40]  I'm,
[449.52 --> 453.50]  I see these things as more of being a sort of a nice fun thought experiments
[453.50 --> 458.40]  and nice sort of projects that are sort of pushing the boundaries of what's
[458.40 --> 458.80]  possible.
[458.80 --> 461.66]  And I think you do need these kinds of projects.
[461.72 --> 462.56]  In any ecosystem,
[462.82 --> 462.98]  right.
[463.04 --> 464.34]  To sort of show,
[464.56 --> 464.76]  Hey,
[464.96 --> 466.90]  like let's think outside of the,
[466.90 --> 469.48]  the box that was defined for the language,
[469.56 --> 469.80]  right.
[469.86 --> 471.34]  And from day one kind of thing.
[471.42 --> 474.32]  And I think those definitely have a place in the community and they will
[474.32 --> 475.08]  always play a role.
[475.58 --> 475.66]  But,
[475.96 --> 476.68]  you know,
[476.70 --> 477.56]  like to your point,
[477.68 --> 480.22]  if I'm trying to build sort of production grade applications,
[480.22 --> 483.56]  not to say that those projects can't produce production grade
[483.56 --> 484.00]  applications,
[484.00 --> 484.86]  it's just,
[484.86 --> 486.40]  I would have a hard time selling,
[486.78 --> 490.66]  not doing JavaScript in JavaScript or in a framework that is tailored for
[490.66 --> 491.10]  doing,
[491.10 --> 491.58]  say,
[491.74 --> 492.04]  you know,
[492.26 --> 494.30]  graphical user interfaces or web interfaces,
[494.30 --> 497.20]  or even mobile interfaces with JavaScript tooling,
[497.46 --> 498.48]  trying to do that through go,
[498.56 --> 499.70]  I'd have a hard time selling that.
[500.42 --> 500.78]  Yeah.
[501.16 --> 504.24]  So it sounds like what we need to do is get somebody who's an expert in these
[504.24 --> 506.52]  areas and have them come on and change our mind,
[506.64 --> 507.52]  which would be pretty awesome.
[507.96 --> 508.12]  Yeah.
[508.14 --> 508.40]  I don't know.
[508.44 --> 509.50]  You think you can find one of those?
[509.96 --> 510.64]  We can look.
[510.78 --> 511.20]  We'll see.
[511.20 --> 511.64]  Okay.
[511.64 --> 516.24]  So we have Andrew here with us and Andrew has a little bit more experience in
[516.24 --> 519.48]  what I'd consider more of the like native graphical user interface area.
[520.12 --> 522.20]  So for those of you who are not familiar with Andrew,
[522.32 --> 523.64]  he created or helped create,
[523.74 --> 525.34]  I'm not sure how that started.
[525.34 --> 526.26]  fine,
[526.42 --> 529.22]  which is something that allows you to sort of build native,
[529.22 --> 529.82]  you know,
[529.82 --> 531.36]  graphical user interfaces or GUIs.
[531.36 --> 537.62]  So I guess the first question I want to ask is why don't we see more people
[537.62 --> 540.82]  doing like graphical user interface type stuff in go or in,
[540.96 --> 541.04]  you know,
[541.04 --> 541.74]  some of these languages,
[541.74 --> 545.24]  like what makes it challenging because surely people want to build,
[545.32 --> 546.08]  you know,
[546.08 --> 548.92]  these applications that work natively on an OS.
[549.96 --> 550.44]  Yeah.
[550.82 --> 552.72]  It's actually a bit of a mystery to me,
[552.80 --> 553.12]  honestly,
[553.30 --> 557.88]  when I was first thinking about how might you reimagine building graphical
[557.88 --> 558.50]  applications,
[558.50 --> 559.18]  which is,
[559.26 --> 559.48]  you know,
[559.52 --> 561.12]  kind of where fine came from.
[561.12 --> 563.60]  I looked at go as a language and compared it with,
[563.76 --> 567.92]  with a few others and it just seemed like such a great fit with the
[567.92 --> 572.26]  concurrency memory management and just the language semantics seem to fit
[572.26 --> 572.92]  really well.
[573.36 --> 573.78]  Partly,
[573.86 --> 577.86]  I think maybe there's not much going on in this space because that's not
[577.86 --> 581.00]  what people originally expected that language would be useful for.
[581.20 --> 582.52]  So it's kind of,
[582.68 --> 582.88]  you know,
[582.90 --> 587.42]  a few years behind that opportunity because it was particularly not worked on
[587.42 --> 587.62]  for,
[587.68 --> 588.52]  for a long time.
[588.52 --> 589.96]  But like Johnny said,
[589.96 --> 594.30]  it's been expanding over the last few years into lots of different areas and
[594.30 --> 596.30]  people are starting to think outside of,
[596.30 --> 597.14]  of that area.
[597.14 --> 602.14]  And so the graphical toolkits along with other things are coming along now.
[602.68 --> 607.38]  And you'll probably look at the awesome goal list and see like 25 different
[607.38 --> 607.98]  toolkits all,
[607.98 --> 612.56]  all trying to do something with graphical user interfaces in go.
[612.56 --> 615.90]  And maybe half of those are on the embedded website.
[615.90 --> 620.24]  And the others would be to some flavor of native.
[620.24 --> 621.50]  That said,
[621.84 --> 625.04]  it is a really hard thing to do well.
[625.80 --> 626.80]  And if I tell somebody,
[626.90 --> 627.08]  Oh yeah,
[627.14 --> 630.40]  we're building a new graphical user interface toolkit from scratch.
[630.60 --> 630.98]  You know,
[630.98 --> 632.16]  they just look at you and go,
[632.54 --> 632.68]  well,
[632.76 --> 633.46]  like why?
[633.56 --> 635.54]  That's just so much work.
[635.94 --> 638.70]  Surely the ones that exist are good enough.
[638.70 --> 640.72]  And so it is,
[640.80 --> 642.22]  I think one of those challenges that,
[642.26 --> 643.16]  that people just go,
[643.50 --> 644.50]  what's the point?
[646.00 --> 647.08]  So like,
[647.10 --> 648.80]  I know one of the big issues I see,
[648.94 --> 652.86]  because people have been trying to make this like a cross platform GUI type
[652.86 --> 653.72]  thing for a while.
[653.86 --> 656.58]  Like you see react native and you see a bunch of others out there.
[656.64 --> 657.56]  And even on mobile,
[657.56 --> 658.74]  there were people who would be like,
[658.78 --> 658.98]  okay,
[659.00 --> 659.96]  come learn our thing.
[659.96 --> 663.12]  And you can develop for both iOS and Android at the same time,
[663.12 --> 664.16]  which was always a big challenge.
[664.54 --> 666.00]  So I guess the first question is,
[666.00 --> 669.76]  do you think it's really possible to make good user interfaces that are
[669.76 --> 671.86]  cross platform at like one time,
[671.86 --> 672.90]  or is this kind of a,
[673.34 --> 676.22]  we're stuck just building it for each different operating system separately
[676.22 --> 677.74]  because they all expect different stuff.
[678.40 --> 678.62]  Well,
[679.14 --> 681.70]  I absolutely think that it can be done.
[681.90 --> 685.48]  That is kind of the purpose behind the projects,
[685.48 --> 690.02]  just to show that one of these considered impossible tasks actually just
[690.02 --> 693.62]  hadn't been tackled with the latest tool set,
[693.76 --> 695.80]  a language that supports these ideas.
[696.00 --> 697.48]  And if I didn't think it was possible,
[697.70 --> 697.88]  you know,
[697.88 --> 700.14]  I'd be doing something else with my time for sure.
[700.76 --> 701.68]  And so that's,
[701.94 --> 704.46]  I think it's a question of,
[704.48 --> 709.06]  of trying to figure out how do you apply current technologies on top of all of
[709.06 --> 712.58]  the learning that we've had over the last 20,
[712.72 --> 716.86]  30 years of building graphical interfaces and the toolkits that support them
[716.86 --> 720.32]  and bring all of that together with a bit of fresh thinking.
[720.32 --> 728.82]  And one of the things that really drove me initially was when the smartphone apps were really taking off and we saw what good usability could really look like.
[729.00 --> 730.72]  And then people looked at desktop and just went,
[730.80 --> 730.86]  Oh,
[730.90 --> 731.04]  these,
[731.16 --> 732.40]  these two are incompatible.
[732.40 --> 733.14]  Well,
[733.30 --> 733.58]  you know,
[733.58 --> 740.36]  maybe that's because actually we needed to take the opportunity to reimagine it and see how this could work across all platforms,
[740.36 --> 740.88]  you know,
[740.88 --> 741.78]  with a fresh look.
[741.78 --> 744.56]  And can we apply the design learnings,
[744.56 --> 748.86]  the usability and take those concepts onto both desktop,
[749.06 --> 753.18]  but also the cross platform with one code base concept.
[753.92 --> 755.00]  And I think there's,
[755.08 --> 758.16]  there's a lot of space there to really come at this with a fresh angle.
[758.22 --> 759.32]  And that's what we're trying to do.
[759.46 --> 760.84]  There's always a trade off,
[760.94 --> 761.08]  right?
[761.12 --> 763.46]  So if you're trying to create something that's cross platform,
[763.96 --> 764.42]  some,
[764.62 --> 765.98]  in some environments you're going to get,
[766.30 --> 766.76]  you might say,
[766.80 --> 766.96]  well,
[767.38 --> 767.80]  for,
[767.94 --> 768.88]  for the Mac environment,
[768.88 --> 769.38]  you know,
[770.02 --> 771.22]  we can take advantage of certain,
[771.40 --> 772.24]  certain things here,
[772.26 --> 773.38]  but for windows environment,
[773.38 --> 775.54]  we can't take advantage of the same things.
[775.54 --> 777.80]  We have to sort of give up some things here in order to get that.
[777.80 --> 778.00]  So,
[778.00 --> 780.02]  so where are the trade offs that you're making?
[780.54 --> 791.74]  Or are you hiding those from the developer from having to create sort of a specific sort of an OS based APIs and things for allowing a developer to do what they want to do with the project?
[792.22 --> 792.30]  Yeah,
[792.36 --> 792.76]  absolutely.
[793.30 --> 797.36]  I guess there's definitely trade offs in anything that you're trying to do cross platform.
[797.36 --> 799.66]  Although as the Go team have showed us,
[799.80 --> 800.00]  you can,
[800.06 --> 805.28]  you can actually find clever ways to work around most of these and still have an elegant API at the end of the day.
[805.62 --> 814.54]  They probably would be worth looking at what native means because there's a lot of different toolkits that are trying to be native and they can take different approaches.
[814.88 --> 816.50]  The and labs UI project,
[816.66 --> 818.64]  which is doing a really fantastic job of,
[818.64 --> 823.04]  of abstracting a standard API across system standard components.
[823.04 --> 827.14]  So you build an application with one code base and when you run it,
[827.14 --> 831.32]  it looks exactly like every other application on the system it's running on.
[831.32 --> 837.66]  And so the trade off that they're going to be taking on board is sort of the,
[837.66 --> 838.12]  I guess,
[838.16 --> 840.10]  the lowest common denominator to element,
[840.48 --> 840.94]  although they're,
[840.94 --> 845.34]  they're managing to build more complex components off the standard items available.
[845.34 --> 847.84]  But so finds in a place where we thought,
[847.92 --> 851.58]  actually let's have a standard user interface across all of these systems.
[852.08 --> 853.56]  And so the trade off there is,
[853.56 --> 859.38]  is probably the immediate recognition that a user might expect when they're loading a new application.
[859.38 --> 861.68]  We're presenting them something that is a little bit different.
[861.96 --> 868.34]  We're going for consistency across the platforms as opposed to specifically consistency with the current system,
[869.00 --> 870.54]  which is a potentially courageous,
[870.54 --> 872.70]  but design choice that we made.
[872.70 --> 874.96]  So there's a bit of trade off there with,
[874.96 --> 876.10]  with user familiarity,
[876.10 --> 878.30]  but the one that we're looking at at the moment is,
[878.34 --> 881.02]  is around system dialogues.
[881.02 --> 881.54]  You know,
[881.60 --> 883.14]  there's if you're running on,
[883.32 --> 883.72]  for example,
[883.82 --> 885.32]  the Apple desktop,
[885.32 --> 888.02]  there's a lot of functionality there,
[888.02 --> 891.64]  like the iCloud document store and things that if you're saving a file,
[891.70 --> 893.40]  you would expect to have presented to you.
[893.60 --> 896.36]  So we're needing to look at a system by system basis,
[896.36 --> 902.68]  how exactly that integration might work so that people can get access to the files that they would expect.
[902.70 --> 907.66]  on their system without a huge variance in the capability of the software running on different platforms.
[908.38 --> 908.78]  So,
[908.88 --> 909.12]  I mean,
[909.16 --> 909.30]  there's,
[909.30 --> 909.54]  there's,
[909.60 --> 910.94]  there's all sorts of ways that it's,
[911.10 --> 911.24]  you know,
[911.26 --> 913.32]  it can have to vary across systems,
[913.32 --> 913.60]  but that,
[913.72 --> 915.52]  that's the one that's certainly on our mind at the moment.
[916.38 --> 917.94]  So when you said that,
[917.96 --> 924.06]  like the go team showed us that we can actually use some clever things to sort of get around the differences between the operating systems,
[924.06 --> 925.64]  just for anybody who's not familiar,
[925.64 --> 931.32]  I'm assuming you're referring to like having build tags and having specific go files that compile depending on the language you're building for.
[931.72 --> 932.20]  Yeah,
[932.28 --> 932.52]  I mean,
[932.56 --> 932.98]  absolutely.
[933.08 --> 934.06]  That's a big part of it,
[934.14 --> 934.46]  but I,
[934.50 --> 940.36]  I guess I was more thinking that from the language and the standard library level,
[940.54 --> 944.12]  you really don't need to worry about it at all for the most part.
[944.34 --> 946.38]  If you're reaching for a build tag,
[946.72 --> 946.88]  you know,
[946.90 --> 955.26]  you're probably wanting to do something specific for a certain platform and you're making that choice to break away from the guaranteed consistency across systems.
[955.26 --> 962.16]  And that is certainly a challenge when you start working in the graphical world where those guarantees don't necessarily go away completely,
[962.32 --> 976.52]  but they certainly introduce a lot more challenges and how you manage to have an API that is as easy to use as the standard go libraries whilst dealing with these more system specific concepts is a challenge as well.
[977.40 --> 977.52]  Yeah.
[977.58 --> 981.32]  So what I meant initially was that you can have multiple go files and each one,
[981.42 --> 983.42]  depending on the language you're building for is the one that's used,
[983.42 --> 990.52]  but the actual API that people are calling is the same functions and they're generally expected to do the same thing as just how they do it might be a little bit different.
[991.20 --> 991.48]  Oh yeah,
[991.68 --> 992.06]  absolutely.
[992.50 --> 996.52]  But then the flip side of that is you kind of get lured into this,
[996.58 --> 998.68]  almost wanting to have two things act different ways.
[998.68 --> 1002.18]  And you don't want developers to call a function and have to mentally think like,
[1002.26 --> 1004.86]  if I call this function and they're running on Mac,
[1004.92 --> 1005.76]  it's going to do this thing.
[1005.82 --> 1006.58]  But if it's on windows,
[1006.64 --> 1008.10]  it's going to do something similar,
[1008.24 --> 1009.36]  but not quite the same.
[1009.68 --> 1010.04]  And,
[1010.12 --> 1010.22]  you know,
[1010.22 --> 1011.78]  like my code needs to sort of,
[1011.78 --> 1012.00]  you know,
[1012.00 --> 1012.94]  adapt for both of those,
[1012.94 --> 1014.00]  which would be very challenging,
[1014.12 --> 1015.52]  especially like you said,
[1015.58 --> 1015.74]  in the,
[1015.74 --> 1016.98]  in the GUI world,
[1017.54 --> 1021.12]  everything from alerts and notifications and just permissions.
[1021.12 --> 1028.42]  Like there's just so many different things that are really challenging to pull off because that's where the differences in the operating systems really start to stick out.
[1028.86 --> 1029.58]  For sure.
[1029.66 --> 1029.84]  Yeah.
[1029.84 --> 1036.64]  I think if anybody's ever trying to design an API that's going to be consumed outside of your team at work,
[1036.76 --> 1041.82]  it's important to consider the path of least surprise for any developer that's going to be using the API.
[1041.82 --> 1044.66]  And if you do want to put platform specifics in there,
[1044.66 --> 1052.50]  the outcome should really be entirely consistent irrespective of the specifics that are happening behind the scenes.
[1052.50 --> 1056.88]  And so there may be a significant difference to how things are functioning,
[1057.08 --> 1060.02]  but really the end result should be consistent.
[1060.38 --> 1060.86]  And I mean,
[1060.88 --> 1063.68]  notifications is a really interesting example there,
[1063.82 --> 1064.44]  but I mean,
[1064.48 --> 1072.74]  there's probably a hugely long list of those sorts of system items that are going to be challenged to do consistently across systems.
[1072.74 --> 1074.92]  But from the developer's point of view,
[1075.10 --> 1075.26]  yeah,
[1075.36 --> 1077.50]  they call a function and a thing happens.
[1077.64 --> 1078.38]  The documentation,
[1078.88 --> 1081.64]  whether it's Godoc or something more elaborate,
[1081.86 --> 1083.70]  is going to describe the functionality,
[1084.00 --> 1086.02]  not the platform specific item.
[1086.26 --> 1087.18]  And I think that's important.
[1100.86 --> 1101.56]  Hi there.
[1101.56 --> 1102.88]  This is John Calhoun,
[1103.04 --> 1104.26]  one of your GoTime panelists.
[1104.96 --> 1106.08]  When I'm not working on GoTime,
[1106.28 --> 1109.54]  I create programming courses that help developers level up their Go skills.
[1110.10 --> 1111.44]  And one of my more recent courses,
[1111.60 --> 1112.42]  Algorithms with Go,
[1112.66 --> 1113.20]  is live,
[1113.34 --> 1114.84]  and I wanted to invite you to check it out.
[1115.30 --> 1116.30]  So it's completely free,
[1116.56 --> 1119.42]  and in it we explore how algorithms and data structures work,
[1119.54 --> 1121.78]  as well as how to actually implement them in GoCode.
[1122.18 --> 1125.42]  So if you've ever had an interest in learning about algorithms or data structures,
[1125.70 --> 1128.30]  or if you felt like you understand them conceptually,
[1128.36 --> 1130.20]  but just couldn't nail down that coding part,
[1130.20 --> 1131.76]  this course is going to be great for you.
[1131.88 --> 1133.58]  We actually dive into coding everything,
[1133.88 --> 1135.10]  we work on practice problems,
[1135.10 --> 1135.98]  and it's a lot of fun.
[1136.48 --> 1140.42]  You can sign up completely free at algorithmswithgo.com slash GoTime.
[1140.90 --> 1143.94]  Again, that's algorithmswithgo.com slash GoTime.
[1144.06 --> 1146.00]  And don't forget that last slash GoTime bit.
[1146.00 --> 1148.52]  It helps me keep track of how you found out about the course,
[1148.74 --> 1150.42]  so that GoTime gets credit for referring you.
[1150.74 --> 1151.46]  Thanks for listening.
[1169.68 --> 1171.80]  So, you're working on Fine,
[1171.94 --> 1174.28]  which does, I believe, mobile and desktop.
[1174.28 --> 1174.88]  Is that correct?
[1175.38 --> 1176.40]  It was desktop initially,
[1176.72 --> 1179.10]  and just in December we added mobile,
[1179.26 --> 1181.54]  so that's iOS, Android,
[1181.70 --> 1183.60]  and also Raspberry Pi fitted in there
[1183.60 --> 1186.16]  because it's running the same chipsets
[1186.16 --> 1188.42]  for the graphics output as the mobile devices are.
[1188.56 --> 1189.84]  So it's not really mobile,
[1190.04 --> 1192.82]  but it was a nice added bonus at the same time.
[1193.50 --> 1195.08]  So when you're thinking about that,
[1195.28 --> 1196.86]  do you think about those,
[1197.10 --> 1198.64]  like when you're exposing an API,
[1198.78 --> 1202.84]  do you guys feel that that API should be the same for mobile and desktop,
[1202.84 --> 1204.70]  or is this something where you've actually drawn a line
[1204.70 --> 1206.56]  and said one's different enough from the other
[1206.56 --> 1208.18]  that we can't just make it universal?
[1209.02 --> 1209.76]  No, absolutely.
[1209.94 --> 1212.96]  These APIs that we're building have to be consistent completely.
[1213.44 --> 1215.86]  We're following Go's design principles on that,
[1216.00 --> 1218.18]  and everything that we do is idiomatic,
[1218.32 --> 1221.12]  or we're aiming to be idiomatic to the language,
[1221.44 --> 1224.10]  and consistent APIs is really important there.
[1224.10 --> 1227.22]  So if somebody's writing an application with Fine,
[1227.56 --> 1229.86]  then they know that it's going to work
[1229.86 --> 1232.32]  across all of these different devices in the same way.
[1232.64 --> 1235.64]  That said, there are sometimes differences between devices
[1235.64 --> 1239.12]  that you want to enable that aren't generic.
[1239.54 --> 1242.50]  The one that springs to mind right now is a virtual keyboard.
[1242.70 --> 1246.36]  That's not typically available on a desktop platform,
[1246.84 --> 1250.48]  and so there are some APIs that are device-specific,
[1250.48 --> 1253.36]  and you can use appropriate calls to say,
[1253.42 --> 1256.00]  you know what, if I'm running in this environment,
[1256.12 --> 1257.14]  then take this action.
[1257.70 --> 1261.26]  So that's available if people want to customize their systems
[1261.26 --> 1262.38]  to the device it's running on,
[1262.42 --> 1264.44]  but it's not really encouraged
[1264.44 --> 1267.18]  because we want to make as much of this
[1267.18 --> 1269.16]  completely transparent as possible.
[1269.60 --> 1271.12]  So I know historically,
[1271.32 --> 1273.96]  one of the big downsides to using something
[1273.96 --> 1277.12]  that sort of does the GUIs across platforms
[1277.12 --> 1278.58]  tends to be performance,
[1278.58 --> 1281.42]  but a lot of times I think that's shown up in JavaScript worlds
[1281.42 --> 1283.42]  where everything's running through JavaScript
[1283.42 --> 1286.28]  rather than running in something that was actually compiled.
[1286.80 --> 1289.18]  So do you think using Go actually helps prevent that issue
[1289.18 --> 1290.88]  and keeps it snappy?
[1291.86 --> 1293.02]  Yes, absolutely.
[1293.18 --> 1294.74]  The performance that we've experienced
[1294.74 --> 1297.10]  has been really phenomenal, actually.
[1297.78 --> 1298.48]  You're quite right.
[1298.52 --> 1302.80]  A lot of the technologies that try to tackle the cross-platform
[1302.80 --> 1307.50]  do suffer in some of their choices and performances
[1307.50 --> 1310.34]  can be challenging to keep up there.
[1310.74 --> 1314.36]  But when the Go code is compiled down to the machine,
[1315.02 --> 1318.74]  apart from some implementation details that we might have,
[1318.94 --> 1322.22]  it's going to be running at the same speed as the native code
[1322.22 --> 1324.94]  if you'd been building with the toolkits
[1324.94 --> 1327.72]  that the platform was designed with.
[1327.72 --> 1330.90]  And partly because the graphics drivers
[1330.90 --> 1332.12]  that we have implemented
[1332.12 --> 1334.62]  are going straight down to the same hardware acceleration
[1334.62 --> 1339.64]  that the Swift or Java codes would be using as well.
[1340.64 --> 1342.98]  So I guess I find that interesting
[1342.98 --> 1345.24]  because if you're getting down to that level,
[1345.80 --> 1347.92]  I know one of the common concerns
[1347.92 --> 1349.00]  that I hear people talk about,
[1349.10 --> 1350.78]  especially, and this isn't specific to GUIs,
[1350.90 --> 1355.08]  but I talk to people in sort of the system administration space
[1355.08 --> 1355.96]  and stuff like that,
[1356.44 --> 1358.36]  and they always make the argument that,
[1358.52 --> 1360.16]  all right, say I'm a Mac sysadmin,
[1360.78 --> 1362.96]  they say that eventually I need to get into Swift
[1362.96 --> 1365.94]  to touch the lower-level things that I need to touch.
[1366.28 --> 1368.28]  I guess, do you ever run into cases where that's the case,
[1368.32 --> 1371.76]  where you really need to touch OS-specific APIs?
[1371.92 --> 1373.34]  Because that's one of the issues, I guess.
[1373.74 --> 1375.24]  A better way of putting this is that
[1375.24 --> 1377.46]  it seems like to write for Mac, you need to know Swift.
[1377.60 --> 1379.02]  To write for Windows, you need to know
[1379.02 --> 1381.16]  one of those .NET languages
[1381.16 --> 1382.84]  that actually can interact with the things
[1382.84 --> 1384.20]  they want you to sort of restrict.
[1384.20 --> 1386.44]  And it seems like they don't care as much
[1386.44 --> 1387.82]  about supporting other languages
[1387.82 --> 1389.88]  with those really specifics.
[1390.62 --> 1392.08]  So has that been a challenge
[1392.08 --> 1393.22]  or is that something you're just,
[1393.74 --> 1395.22]  you know, not doing those things?
[1396.44 --> 1398.12]  It really is a challenge.
[1398.24 --> 1399.00]  Yeah, absolutely.
[1399.44 --> 1401.96]  There's certain things that there's just no way
[1401.96 --> 1404.12]  to address using a language
[1404.12 --> 1405.56]  that's not what was intended.
[1406.12 --> 1408.82]  And it's something that occupies my mind,
[1408.98 --> 1410.28]  you know, when we're working
[1410.28 --> 1413.38]  to do new capabilities on systems.
[1413.96 --> 1417.88]  But our best efforts are to hide all of that complexity
[1417.88 --> 1420.88]  from anybody that would be building their application
[1420.88 --> 1422.46]  with our APIs.
[1422.96 --> 1426.36]  So the project exposes a pure Go API,
[1426.74 --> 1428.58]  which, you know, is great for everybody
[1428.58 --> 1429.36]  who's working on it.
[1429.40 --> 1431.94]  And it makes a lot of sense in all the standard tools.
[1431.94 --> 1434.38]  But if you were to go and look at our source code,
[1434.48 --> 1438.22]  then you'd find Java and Objective-C and some C.
[1438.40 --> 1440.92]  It's all, you know, brought together under the hood,
[1440.98 --> 1443.20]  depending on the target build system.
[1443.70 --> 1445.00]  And there's a couple of tricks in there
[1445.00 --> 1446.96]  to make sure that you don't have to have
[1446.96 --> 1449.22]  all of those variants installed all of the time
[1449.22 --> 1450.48]  just for a build to work.
[1450.56 --> 1452.64]  This is largely going to work out the box
[1452.64 --> 1455.06]  if you have Go and a C compiler.
[1455.06 --> 1458.06]  So there's a lot of complexity under the hood.
[1458.44 --> 1460.20]  But it means that we're able to hook
[1460.20 --> 1462.58]  into the platform-specific APIs,
[1462.74 --> 1464.90]  the types of things that are only available
[1464.90 --> 1467.70]  on an Android machine, an Android device,
[1468.00 --> 1469.96]  if you're accessing the Java APIs
[1469.96 --> 1472.32]  or that might only be exposed through Objective-C
[1472.32 --> 1473.24]  on an Apple computer.
[1473.78 --> 1476.30]  But we want to make sure that that is never anything
[1476.30 --> 1477.76]  that you would need to think about
[1477.76 --> 1480.58]  if you were building on top of our system.
[1481.50 --> 1483.56]  And there's obviously going to be areas
[1483.56 --> 1485.38]  where we haven't completely added
[1485.38 --> 1486.74]  all of the support that we need to.
[1487.34 --> 1488.68]  But we're working on it over time.
[1488.74 --> 1489.90]  And if people find an area
[1489.90 --> 1491.46]  that they're having to reach out
[1491.46 --> 1492.96]  to some other language for,
[1493.16 --> 1494.36]  then, you know, we'd encourage them
[1494.36 --> 1496.46]  to open a ticket and help us work
[1496.46 --> 1498.32]  that support into the main project.
[1499.74 --> 1501.54]  So you say that you build with, like, Java
[1501.54 --> 1502.74]  and C in these things.
[1503.20 --> 1505.14]  I guess, can you talk a little bit more about that?
[1505.24 --> 1507.04]  Like, are you using just, like, C bindings
[1507.04 --> 1508.68]  and connecting to, you know,
[1508.68 --> 1510.04]  things that are going to be on the systems,
[1510.46 --> 1511.06]  you know, every system?
[1511.16 --> 1513.00]  Like, I guess, what does that look like?
[1513.00 --> 1514.20]  Are you talking to, like, OpenGL
[1514.20 --> 1515.30]  or is it something else?
[1515.86 --> 1516.12]  Yeah.
[1516.34 --> 1518.92]  So it is pretty much through C Go, like you say.
[1519.08 --> 1520.94]  And the main dependency issue
[1520.94 --> 1522.70]  is talking to OpenGL,
[1522.82 --> 1525.00]  which gives us access to the graphic subsystems.
[1525.44 --> 1528.80]  In fact, that is the only dependency
[1528.80 --> 1531.34]  for this on most systems.
[1531.60 --> 1533.12]  On desktop, we don't need to do
[1533.12 --> 1535.76]  any clever things for the most part.
[1536.28 --> 1538.80]  And some Apple APIs that might be required
[1538.80 --> 1540.78]  are actually accessible by C
[1540.78 --> 1542.86]  or the objective C that, you know,
[1542.94 --> 1544.94]  compiles down to using the standard tool chain.
[1545.00 --> 1547.88]  So it's not really too much of a problem.
[1548.48 --> 1549.32]  When you're building for mobile,
[1549.44 --> 1551.14]  this becomes a lot more challenging.
[1551.60 --> 1554.52]  But the Go Mobile team have done a fantastic job
[1554.52 --> 1557.58]  of actually solving a lot of the challenges there for us.
[1557.76 --> 1559.36]  And through extending that project,
[1559.36 --> 1561.42]  we've managed to add that support.
[1561.42 --> 1563.96]  I think the craziest thing that I saw
[1563.96 --> 1566.08]  in terms of making that work
[1566.08 --> 1568.78]  was that the Android target
[1568.78 --> 1571.48]  has some Java code in it
[1571.48 --> 1574.06]  that's pre-compiled into a Dex binary
[1574.06 --> 1577.30]  that's then bundled into the Go source code
[1577.30 --> 1578.34]  as a data asset.
[1578.58 --> 1580.26]  And then that's extracted
[1580.26 --> 1581.52]  as part of the build process
[1581.52 --> 1584.00]  to give you your bootstrap into the Go runtime.
[1584.52 --> 1587.10]  Now, I would rather hope that nobody using this
[1587.10 --> 1588.98]  would ever know that that existed under there.
[1588.98 --> 1591.34]  But if you wanted to delve into, you know,
[1591.38 --> 1593.76]  how can I improve this for Android specifically,
[1594.42 --> 1595.94]  you're going to find some really weird stuff.
[1596.52 --> 1598.34]  Yeah, I can imagine that being confusing
[1598.34 --> 1600.00]  at the very least when you're getting started.
[1600.54 --> 1602.70]  So the Go Mobile project
[1602.70 --> 1605.14]  is what was helping you sort of bootstrap into that.
[1605.24 --> 1606.50]  Was there anything that you found
[1606.50 --> 1607.74]  like open source or otherwise
[1607.74 --> 1608.94]  that helped you sort of get started
[1608.94 --> 1610.16]  with the overall project
[1610.16 --> 1611.68]  or getting into like OpenGL
[1611.68 --> 1612.46]  and that sort of space?
[1613.16 --> 1616.36]  Actually, the graphics is a complicated area, I guess.
[1616.46 --> 1618.32]  And it's very, very low level.
[1618.32 --> 1621.12]  So the code reuse between projects
[1621.12 --> 1624.34]  is not exactly shining in that area.
[1624.96 --> 1628.02]  Really, I guess I was just basing on experience
[1628.02 --> 1630.92]  I had with previous projects as much as anything.
[1633.08 --> 1637.40]  They, yeah, I can't think of anything particular
[1637.40 --> 1639.32]  that we really called on.
[1640.28 --> 1642.36]  Although I suppose initially,
[1642.36 --> 1645.94]  the project did use the render pipeline
[1645.94 --> 1648.86]  from the EFL tool chain.
[1648.96 --> 1650.42]  That's the Enlightenment project.
[1650.84 --> 1653.56]  And that gave us some abstraction
[1653.56 --> 1654.62]  for the graphics driver.
[1655.20 --> 1656.78]  But in the end, we realized that
[1656.78 --> 1659.96]  to really build an idiomatic API top to bottom,
[1660.30 --> 1662.50]  we couldn't depend on an abstraction
[1662.50 --> 1663.98]  built in another language.
[1664.06 --> 1667.18]  It just didn't really speak the right language for us.
[1667.18 --> 1668.76]  And we were working a lot
[1668.76 --> 1671.72]  to work around the way it functioned.
[1671.72 --> 1673.32]  And we had duplicated code in there
[1673.32 --> 1675.22]  and thought, actually, this doesn't make sense.
[1675.36 --> 1677.72]  So we took it out and implemented it from scratch
[1677.72 --> 1679.44]  right the way down to the hardware.
[1680.16 --> 1682.00]  I mean, it's probably even more pronounced in your space,
[1682.04 --> 1683.06]  but I think in a lot of spaces,
[1683.06 --> 1685.34]  you'll see that sort of difference
[1685.34 --> 1687.30]  as to whether or not they started with the end user
[1687.30 --> 1689.56]  for like the designing the API for end users
[1689.56 --> 1691.86]  versus starting with like something
[1691.86 --> 1693.66]  they had to work with to touch the backend
[1693.66 --> 1695.40]  and then working their way towards the end user.
[1696.12 --> 1698.76]  Because an API that's designed for end users
[1698.76 --> 1700.32]  will look like very clearly
[1700.32 --> 1701.84]  like they designed this for me to use it.
[1702.08 --> 1702.88]  And then there's other cases
[1702.88 --> 1705.70]  where you get an API where it's like really confusing
[1705.70 --> 1707.70]  or everything's just scattered all over.
[1708.10 --> 1709.10]  I'm trying to think of an example,
[1709.22 --> 1710.34]  but I can't off the top of my head.
[1710.44 --> 1711.78]  But I know that like I've definitely seen
[1711.78 --> 1712.94]  even like just web APIs
[1712.94 --> 1715.40]  where you can tell the web API
[1715.40 --> 1717.02]  is based off of the data models
[1717.02 --> 1717.96]  that they're storing things in
[1717.96 --> 1719.24]  rather than like what end users
[1719.24 --> 1720.30]  are actually going to want to use.
[1720.98 --> 1722.68]  And as a result, it just ends up looking very,
[1722.68 --> 1725.40]  you know, not very user friendly
[1725.40 --> 1727.14]  because they didn't think like
[1727.14 --> 1729.00]  what is a user actually going to want here
[1729.00 --> 1731.22]  versus what's easiest for us to give to them.
[1732.02 --> 1732.74]  Absolutely, yeah.
[1732.90 --> 1735.40]  And I mean, sometimes you want a design
[1735.40 --> 1736.56]  that's close to the hardware
[1736.56 --> 1738.02]  or that's close to the data model.
[1738.22 --> 1739.62]  And there are projects out there
[1739.62 --> 1742.56]  that would, you know, use that design on purpose.
[1742.56 --> 1745.30]  But I think for really for our project,
[1745.30 --> 1747.80]  we're trying to make this as easy to use as possible
[1747.80 --> 1750.74]  for even first time graphical app developer.
[1750.74 --> 1753.02]  So it needs to be built with them in mind
[1753.02 --> 1755.52]  with as few lines of code as possible,
[1755.60 --> 1758.74]  very clear intent in every single line of code
[1758.74 --> 1759.78]  so that nothing there is,
[1759.96 --> 1762.48]  nothing is excess, nothing is confusing.
[1762.90 --> 1764.92]  But there are different approaches
[1764.92 --> 1767.16]  where actually folk love graphics libraries
[1767.16 --> 1771.04]  that expose exactly how a graphics pipeline works
[1771.04 --> 1772.56]  and you're feeding instructions
[1772.56 --> 1774.76]  through into that pipeline.
[1775.42 --> 1778.26]  I mean, if you were, I guess, building a game engine,
[1778.38 --> 1779.78]  that would be really important for you.
[1779.78 --> 1782.82]  But we're pretty sure that really enabling folk
[1782.82 --> 1785.60]  to quickly build applications that are, you know,
[1785.66 --> 1789.18]  user-friendly is what's most significantly lacking
[1789.18 --> 1789.70]  at the moment.
[1789.96 --> 1791.32]  And especially cross-platform,
[1791.42 --> 1793.26]  there's just not really anything there
[1793.26 --> 1795.64]  if you don't want to worry about the fun
[1795.64 --> 1799.14]  of web technologies inside your seemingly native applications.
[1799.70 --> 1800.98]  Yeah, that makes sense.
[1801.60 --> 1804.32]  And I guess one way I kind of view it is,
[1804.94 --> 1806.20]  like you mentioned game engines,
[1806.20 --> 1808.60]  and I think there are some people
[1808.60 --> 1810.50]  who want to definitely access the low-level stuff,
[1810.60 --> 1811.74]  but for the most part,
[1811.82 --> 1813.30]  at least when I'm watching people make games,
[1813.72 --> 1816.48]  it seems like a lot of them want to use engines of some sort,
[1816.80 --> 1818.16]  like they want to use like Unreal Engine
[1818.16 --> 1820.00]  or, you know, some engine of some sort
[1820.00 --> 1822.30]  that abstracts some of that away for them
[1822.30 --> 1824.70]  so that they can kind of speak in a little bit,
[1825.30 --> 1827.32]  you know, not quite like system-level language.
[1827.32 --> 1828.98]  They can actually start talking about things
[1828.98 --> 1831.40]  in a way that makes more sense to them.
[1832.12 --> 1833.32]  So I get what you mean.
[1833.38 --> 1835.10]  There's definitely some people who need that low-level,
[1835.30 --> 1836.84]  but I think there's a lot more people
[1836.84 --> 1838.86]  that tend to talk at that higher level,
[1838.98 --> 1840.52]  a little bit easier to understand language.
[1841.48 --> 1842.22]  Yeah, absolutely.
[1842.70 --> 1846.84]  I mean, you know, every API is built with a design in mind,
[1847.26 --> 1848.48]  and I think you're right,
[1848.54 --> 1850.72]  important to know who you're designing for
[1850.72 --> 1851.74]  when you set out,
[1851.74 --> 1853.62]  because changing that after the fact
[1853.62 --> 1855.22]  is going to be really difficult,
[1855.62 --> 1857.96]  probably make a rather confusing product
[1857.96 --> 1858.64]  at the end of the day.
[1858.64 --> 1861.94]  Okay, so we talked a little bit about gaming stuff.
[1862.42 --> 1864.00]  Do you think a lot of this is why
[1864.00 --> 1867.16]  the gaming space is just not that common in Go as well?
[1867.30 --> 1869.54]  Is it like basically the same type of challenges
[1869.54 --> 1870.96]  where getting that stuff rendering,
[1871.06 --> 1872.42]  or do you think there's different challenges there?
[1873.38 --> 1876.28]  Well, now that there's a lot of projects out there
[1876.28 --> 1878.72]  that can actually get something rendering to the screen,
[1879.28 --> 1881.52]  I'm not entirely sure that that's a challenge now.
[1881.68 --> 1883.08]  Maybe people are still cautious
[1883.08 --> 1885.46]  because it's new or, you know,
[1885.46 --> 1887.08]  not strictly part of the language,
[1887.08 --> 1888.34]  if you'll excuse the phrase,
[1888.42 --> 1889.70]  but I've heard it a fair amount.
[1890.72 --> 1893.02]  I think that it's more around
[1893.02 --> 1895.62]  putting together the libraries and the support,
[1895.70 --> 1897.22]  the type of stuff you described.
[1897.32 --> 1898.66]  I don't want to write a game engine.
[1898.76 --> 1901.00]  I just want to pull together a game.
[1901.48 --> 1903.68]  And that is another huge amount of work.
[1903.76 --> 1906.14]  And I wouldn't be surprised if sooner or later,
[1906.14 --> 1907.46]  we do see something emerge
[1907.46 --> 1909.48]  that is a pretty compelling approach,
[1909.90 --> 1912.74]  maybe close to a cool typed API
[1912.74 --> 1914.24]  that would look really great for Go.
[1914.72 --> 1917.68]  I just imagine that maybe it's going to take a while
[1917.68 --> 1919.80]  before folk are happy to put the effort
[1919.80 --> 1921.86]  into building that sort of an engine.
[1922.60 --> 1924.62]  Binding to an existing engine in Go,
[1924.78 --> 1926.82]  just it wouldn't really make any sense in my mind.
[1927.78 --> 1930.00]  The differences between languages in this space
[1930.00 --> 1933.50]  are so vast that I think you could spend a lot of time
[1933.50 --> 1936.74]  and realize that actually it's just too hard to read.
[1937.78 --> 1938.22]  Yeah.
[1938.38 --> 1940.34]  I think one of the things that might also help there
[1940.34 --> 1942.38]  is that there's a lot of tools out there
[1942.38 --> 1944.76]  that are also very good at cross-platform game stuff.
[1945.26 --> 1946.56]  Like Steam has done a lot of work
[1946.56 --> 1948.90]  to make sure a lot of their games run on every OS.
[1949.34 --> 1951.40]  And as a result, you can kind of use their tools.
[1951.74 --> 1953.04]  So we're not really lacking.
[1953.20 --> 1955.00]  Whereas, like we talked about earlier,
[1955.16 --> 1958.72]  the rendering of graphical user interfaces across systems,
[1958.90 --> 1960.42]  at least every approach I've seen so far
[1960.42 --> 1962.50]  has had issues of some sort
[1962.50 --> 1963.78]  that people typically run into.
[1964.30 --> 1967.04]  And I know the, basically like the really big UI
[1967.04 --> 1969.06]  that would start to lag if you had too much data
[1969.06 --> 1970.26]  or too much of anything in there
[1970.26 --> 1972.76]  was a big one that I saw a lot of companies complaining about.
[1972.84 --> 1974.30]  Because if you're doing like an Airbnb
[1974.30 --> 1975.52]  and you have a bunch of listings,
[1975.98 --> 1978.00]  it would start to like not render correctly
[1978.00 --> 1979.08]  when you're swiping up or something
[1979.08 --> 1980.28]  or it just wouldn't feel natural.
[1980.78 --> 1981.92]  So Go is a good fit for that.
[1982.20 --> 1983.72]  But if you've got games that are kind of working,
[1983.80 --> 1986.74]  I get that maybe it's not as big of an issue
[1986.74 --> 1988.68]  to get something in that space
[1988.68 --> 1990.30]  when there's already somebody who solved that problem
[1990.30 --> 1991.80]  in like another language, another way.
[1992.46 --> 1993.88]  Yeah, I guess that's a good point.
[1993.88 --> 1997.54]  I'm not entirely sure how solved it is.
[1997.98 --> 2001.64]  Just from my experience with the games Christmas sale,
[2001.76 --> 2003.36]  I saw this huge list of great bargains
[2003.36 --> 2005.62]  and thought, oh, fantastic, I'll get a load of them.
[2006.16 --> 2007.64]  And then of course, like only one in 10
[2007.64 --> 2009.48]  actually worked on the platform I was running on.
[2009.62 --> 2011.94]  So it may be technically solved,
[2012.00 --> 2013.36]  but there's clearly challenges there
[2013.36 --> 2016.16]  that mean it's not absolutely consistent.
[2016.86 --> 2020.68]  And I think this is, it's a real problem actually
[2020.68 --> 2025.26]  with any API or platform that tries to do cross-platform.
[2025.56 --> 2027.18]  If there's really any roadblock
[2027.18 --> 2029.40]  to just rolling out across all of them,
[2029.74 --> 2031.00]  then you're going to drop off,
[2031.12 --> 2033.36]  find people drop off really quite substantially.
[2033.82 --> 2036.40]  And if we're seeing new games getting released
[2036.40 --> 2038.50]  only for one platform out of three or four
[2038.50 --> 2040.86]  on a major system like Steam,
[2040.94 --> 2042.80]  then I have to think, you know, there's,
[2043.10 --> 2044.80]  I don't know the APIs,
[2044.96 --> 2047.10]  but I have to feel that there's probably something in there
[2047.10 --> 2049.34]  that makes it a real challenge.
[2049.34 --> 2051.20]  And if you're going to claim cross-platform,
[2052.00 --> 2054.54]  it really needs to truly be cross-platform
[2054.54 --> 2056.48]  without having to jump through hoops
[2056.48 --> 2058.40]  or do special things to make your code work.
[2059.06 --> 2060.06]  So given that that's the case,
[2060.20 --> 2063.54]  do you think that anybody who's making a GUI library in Go
[2063.54 --> 2064.98]  needs to actually keep track
[2064.98 --> 2066.92]  of what languages things are being released in?
[2066.98 --> 2068.12]  Like if somebody is using Fine
[2068.12 --> 2070.26]  and you find that a lot of your users
[2070.26 --> 2072.80]  are only actually releasing to Mac OS,
[2072.92 --> 2074.78]  they're not actually releasing to all three,
[2074.98 --> 2076.50]  you know, or Windows, Linux, Mac,
[2076.64 --> 2078.50]  and, or maybe they're just using two of them.
[2078.50 --> 2080.16]  Do you keep track of things like that
[2080.16 --> 2081.54]  or try to like keep an eye on that
[2081.54 --> 2082.82]  to sort of see if that's a sign
[2082.82 --> 2083.96]  that you're not doing as well
[2083.96 --> 2085.08]  as you could be in one language
[2085.08 --> 2086.32]  or one operating system?
[2086.68 --> 2089.62]  That is probably something that we should do actually
[2089.62 --> 2090.78]  to have a better idea
[2090.78 --> 2093.40]  about where this is working for people
[2093.40 --> 2095.12]  and where it's not working so well.
[2095.58 --> 2097.86]  I imagine that we would get a lot of feedback
[2097.86 --> 2098.92]  from the community,
[2099.08 --> 2100.90]  which like we have an awesome community,
[2101.00 --> 2102.68]  very supportive, very, very active.
[2103.02 --> 2104.56]  But the challenge here is that
[2104.56 --> 2106.78]  actually we're finding more people than I expected
[2106.78 --> 2108.62]  are using this in their workplace
[2108.62 --> 2110.60]  to add a user interface to something
[2110.60 --> 2112.36]  that was maybe a command line tool
[2112.36 --> 2114.50]  or an ugly web form that they wanted to get rid of.
[2114.96 --> 2117.24]  And so these types of projects
[2117.24 --> 2119.42]  are not really going out in the open
[2119.42 --> 2121.26]  to be able to give us that visibility.
[2121.80 --> 2123.90]  And so it's kind of lacking there a little bit.
[2124.12 --> 2125.56]  We're trying to figure this out
[2125.56 --> 2128.44]  by publicizing the applications that are available.
[2128.66 --> 2130.10]  Anything that is open source,
[2130.32 --> 2132.16]  we're putting together a list of
[2132.16 --> 2134.40]  and recommending that people check it out.
[2134.40 --> 2137.14]  But when it comes to what are you distributing for,
[2137.76 --> 2138.98]  you know, we're really trying to emphasize
[2138.98 --> 2140.92]  the cross-platform approach and say,
[2141.04 --> 2143.74]  look, you know, just run the build
[2143.74 --> 2144.90]  for different target platforms.
[2145.12 --> 2146.10]  That's the only step.
[2146.36 --> 2149.14]  It doesn't make sense with the way
[2149.14 --> 2152.08]  that we're designing it to target only one platform.
[2152.52 --> 2154.88]  It may be that you only want to perform one upload
[2154.88 --> 2156.60]  or submit it to one store.
[2157.04 --> 2158.76]  But if the links are available on a website
[2158.76 --> 2160.24]  or an open source repository,
[2160.56 --> 2161.66]  it's there for the taking.
[2161.66 --> 2165.30]  There's no additional complications to just rebuild it
[2165.30 --> 2167.18]  for the, you know, the additional platforms.
[2167.86 --> 2168.60]  In theory.
[2169.46 --> 2173.60]  I'm curious about the design process
[2173.60 --> 2178.20]  and sort of the thinking that goes into deciding
[2178.20 --> 2181.26]  basically which direction the project should go
[2181.26 --> 2182.78]  in terms of its API footprint.
[2183.12 --> 2183.92]  What should it do?
[2184.06 --> 2184.74]  How should it do it?
[2184.78 --> 2186.80]  When should feature X, Y, and Z come?
[2186.94 --> 2189.38]  I mean, you're at version one, two, one right now.
[2189.38 --> 2191.70]  Along those lines, are there design decisions
[2191.70 --> 2193.78]  that you made up to this point
[2193.78 --> 2195.04]  that you wish you could take back?
[2195.34 --> 2198.78]  Or are there some things that you found out later on
[2198.78 --> 2201.08]  that basically you think could have been caught
[2201.08 --> 2201.94]  during the design phase?
[2202.24 --> 2205.72]  I guess I'm asking because I don't know this world
[2205.72 --> 2207.56]  and I don't know how different it is
[2207.56 --> 2209.92]  from the traditional sort of software engineering
[2209.92 --> 2211.38]  sort of practice and design
[2211.38 --> 2213.38]  and all of the thinking and best practices
[2213.38 --> 2214.30]  that goes along with that.
[2214.30 --> 2216.24]  Sure, yeah.
[2216.82 --> 2219.80]  I think, I mean, there's absolutely things
[2219.80 --> 2223.54]  that I would change with a year and a half of hindsight,
[2224.02 --> 2227.88]  but not as much as maybe I'd imagined we would.
[2228.02 --> 2231.10]  We're very careful about our design process,
[2231.36 --> 2234.10]  both from an interface design point of view,
[2234.16 --> 2236.06]  but also from an API design point of view.
[2236.34 --> 2239.80]  And the design of the API came before
[2239.80 --> 2242.04]  really a single line of implementation.
[2242.04 --> 2246.52]  The project started with an ambition to rethink
[2246.52 --> 2248.68]  how you could build graphical user interfaces
[2248.68 --> 2249.50]  across platform.
[2249.96 --> 2252.88]  And then came a broad strokes design outline
[2252.88 --> 2254.82]  as to how that API might function.
[2255.36 --> 2256.56]  And then we started implementing
[2256.56 --> 2260.00]  initially with this other backend component.
[2260.16 --> 2261.70]  So we didn't have to write the graphics drivers,
[2261.84 --> 2263.30]  but then eventually, you know,
[2263.54 --> 2264.50]  coded it all the way down.
[2265.22 --> 2269.20]  And so it is a very considered approach.
[2269.20 --> 2272.16]  This is the way that I would consider
[2272.16 --> 2273.94]  any software engineering project
[2273.94 --> 2275.70]  if I was in a workplace.
[2276.34 --> 2278.70]  So when I started to think about this open source project,
[2278.70 --> 2279.60]  I wanted to make sure
[2279.60 --> 2282.40]  that we didn't compromise at all in that way.
[2282.96 --> 2284.90]  So, you know, obviously there's other ways
[2284.90 --> 2286.58]  to build projects, get the code running,
[2287.14 --> 2287.88]  share it with some people
[2287.88 --> 2289.54]  and start building from there.
[2289.62 --> 2293.42]  But I felt that without a real design backing to this,
[2293.56 --> 2296.42]  it would struggle to keep its consistency over time.
[2296.42 --> 2300.06]  And so when people ask for new features to be added,
[2300.44 --> 2301.54]  not only do we think,
[2301.86 --> 2303.34]  how would that look as an API,
[2303.50 --> 2304.42]  maybe even ask them
[2304.42 --> 2306.04]  how they would like to interact with it.
[2306.30 --> 2307.62]  But we also have to consider,
[2307.88 --> 2309.86]  well, is this something that makes sense
[2309.86 --> 2311.86]  for the majority of our users?
[2312.02 --> 2314.76]  And is it something that can make sense
[2314.76 --> 2316.52]  across the different target platforms
[2316.52 --> 2317.66]  that we want to support
[2317.66 --> 2320.42]  so that we're not just dropping in,
[2320.52 --> 2322.54]  you know, a small feature for one platform
[2322.54 --> 2324.76]  that then doesn't do what you'd expect
[2324.76 --> 2326.02]  on other systems?
[2326.42 --> 2328.86]  That process, I think, has served us very well.
[2329.38 --> 2331.56]  It does mean that sometimes features
[2331.56 --> 2333.24]  take a long time to develop
[2333.24 --> 2335.00]  and, you know, others dropping quickly,
[2335.12 --> 2335.80]  but not always.
[2336.48 --> 2338.16]  So we have a roadmap that,
[2338.30 --> 2339.20]  I mean, I put together
[2339.20 --> 2341.96]  probably initially two years ago
[2341.96 --> 2343.20]  and it evolves all the time.
[2343.38 --> 2344.02]  And first of all,
[2344.02 --> 2346.18]  we wanted to get desktop apps working.
[2346.40 --> 2346.98]  And then we thought,
[2347.08 --> 2347.72]  okay, that's solid.
[2348.10 --> 2350.34]  Let's add some new widgets to it.
[2350.34 --> 2353.10]  And then it came time to look at mobile.
[2353.48 --> 2354.72]  And so we targeted that
[2354.72 --> 2356.48]  for the 1.2 release last year.
[2356.96 --> 2358.92]  Actually, as part of that release,
[2358.92 --> 2361.04]  we wanted to get data binding in there as well
[2361.04 --> 2362.84]  because it's really simple
[2362.84 --> 2364.06]  to build a simple application.
[2364.06 --> 2365.62]  But then if you want to back
[2365.62 --> 2367.52]  a big data model into it
[2367.52 --> 2369.74]  or connect more complex systems,
[2369.86 --> 2370.90]  display lots of items,
[2371.00 --> 2372.64]  that's, even though it's,
[2372.64 --> 2373.94]  you know, pretty slick,
[2374.02 --> 2375.24]  there's still a lot of code to be written.
[2375.24 --> 2375.66]  So we thought,
[2375.76 --> 2377.44]  if we're really going to do this properly,
[2377.44 --> 2380.12]  we need a good data binding system.
[2381.22 --> 2382.86]  And we started designing it.
[2382.98 --> 2384.36]  And there was a lot of discussion.
[2384.36 --> 2385.70]  There was a bit of experimentation
[2385.70 --> 2386.74]  to see what could work.
[2387.20 --> 2389.28]  And it came close to release time
[2389.28 --> 2390.06]  and the mobile stuff
[2390.06 --> 2391.50]  was polishing up quite nicely.
[2392.02 --> 2392.60]  And we had to say,
[2392.64 --> 2393.58]  look, actually,
[2393.72 --> 2395.16]  if we put this in right now,
[2395.26 --> 2397.24]  we don't think that we could commit
[2397.24 --> 2399.26]  to this being the API
[2399.26 --> 2400.30]  going forward forever.
[2400.58 --> 2402.84]  So we took that out of the release
[2402.84 --> 2405.28]  and invented a new 1.3.
[2405.82 --> 2407.26]  We were initially going to go directly
[2407.26 --> 2409.42]  to a big 2.0 drum roll.
[2409.78 --> 2410.16]  But we thought,
[2410.24 --> 2410.64]  no, actually,
[2410.68 --> 2411.66]  to do this properly,
[2411.88 --> 2413.12]  we need to take more time.
[2413.28 --> 2414.56]  We need to engage
[2414.56 --> 2417.12]  with more external developers.
[2417.42 --> 2418.74]  So we're not just building
[2418.74 --> 2420.24]  as a development team
[2420.24 --> 2421.04]  what we think is right,
[2421.12 --> 2422.14]  but actually what makes sense
[2422.14 --> 2423.22]  for everybody else.
[2423.36 --> 2424.24]  And so I'm sure that
[2424.24 --> 2425.96]  the guys who are working on that
[2425.96 --> 2426.74]  could think this has been
[2426.74 --> 2427.80]  a lengthy process
[2427.80 --> 2428.78]  because we've been building
[2428.78 --> 2429.96]  that API now for,
[2430.18 --> 2431.90]  well, over three months.
[2431.90 --> 2433.54]  That's quite a long time
[2433.54 --> 2435.16]  in any engineer's lifetime,
[2435.26 --> 2435.66]  I suppose.
[2436.00 --> 2436.54]  We're confident
[2436.54 --> 2437.50]  we're going to get it right.
[2437.64 --> 2438.18]  And actually,
[2438.30 --> 2440.78]  the demos that are coming together now,
[2441.02 --> 2441.98]  they're blowing me away,
[2442.02 --> 2442.28]  actually,
[2442.44 --> 2443.36]  what a bit of time
[2443.36 --> 2445.00]  and consideration has created.
[2445.22 --> 2446.02]  It's really cool.
[2446.28 --> 2447.46]  So we're going to continue
[2447.46 --> 2448.28]  to think really hard
[2448.28 --> 2450.06]  about all of these design elements.
[2450.64 --> 2452.30]  The items that we would change
[2452.30 --> 2452.90]  if we could do,
[2453.06 --> 2454.38]  they're very small details
[2454.38 --> 2455.94]  in the grand scheme of things.
[2456.08 --> 2458.34]  And maybe when 2.0 comes along,
[2458.42 --> 2459.34]  we can change
[2459.34 --> 2460.38]  some deprecated stuff
[2460.38 --> 2462.20]  and do a walkthrough
[2462.20 --> 2462.70]  about how people
[2462.70 --> 2463.48]  might update their code,
[2463.56 --> 2464.66]  but it shouldn't be a big deal.
[2465.70 --> 2466.68]  Sorry, long answer.
[2467.18 --> 2467.70]  No, yeah, no,
[2467.76 --> 2469.18]  it's great insight
[2469.18 --> 2470.16]  into the process.
[2470.60 --> 2471.38]  Yeah, it sounds like
[2471.38 --> 2472.72]  there's just as much
[2472.72 --> 2474.24]  sort of agonizing
[2474.24 --> 2475.96]  over what the API
[2475.96 --> 2476.78]  should look like,
[2476.90 --> 2477.04]  you know,
[2477.08 --> 2478.14]  what the developer experience
[2478.14 --> 2478.82]  should be,
[2478.94 --> 2479.60]  you know,
[2479.64 --> 2480.96]  that goes into any great API.
[2481.60 --> 2482.68]  So along those lines,
[2482.74 --> 2482.88]  I mean,
[2482.92 --> 2483.92]  you've written a book,
[2484.24 --> 2484.48]  you know,
[2484.62 --> 2485.84]  hands-on GUI application
[2485.84 --> 2486.56]  development in Go.
[2486.78 --> 2488.06]  And I'm curious,
[2489.10 --> 2489.62]  basically,
[2489.86 --> 2491.76]  what the process,
[2492.18 --> 2492.42]  right,
[2492.60 --> 2493.82]  having worked with
[2493.82 --> 2494.38]  a lot of different
[2494.38 --> 2496.48]  GUI toolkits,
[2496.68 --> 2496.82]  you know,
[2496.86 --> 2498.16]  from GTK to Qt
[2498.16 --> 2499.32]  to any number
[2499.32 --> 2500.02]  of the ones
[2500.02 --> 2500.46]  you talk about
[2500.46 --> 2500.90]  in your book,
[2501.34 --> 2501.92]  I'm curious
[2501.92 --> 2503.30]  what makes
[2503.30 --> 2504.66]  Go
[2504.66 --> 2506.28]  uniquely suited
[2506.28 --> 2507.10]  for FINE
[2507.10 --> 2507.52]  for the current
[2507.52 --> 2508.26]  project of work now.
[2508.38 --> 2509.38]  What makes Go
[2509.38 --> 2510.90]  a good fit
[2510.90 --> 2512.02]  or even
[2512.02 --> 2512.70]  what makes it,
[2513.10 --> 2513.34]  you know,
[2513.48 --> 2514.08]  what are some areas
[2514.08 --> 2515.24]  where it struggles
[2515.24 --> 2515.92]  compared to what
[2515.92 --> 2516.66]  you're familiar with
[2516.66 --> 2517.74]  in other frameworks
[2517.74 --> 2518.38]  and other languages?
[2518.64 --> 2518.72]  Like,
[2518.84 --> 2520.32]  where does Go shine
[2520.32 --> 2520.92]  in this project?
[2522.46 --> 2522.82]  Yeah,
[2523.16 --> 2523.50]  wow.
[2523.78 --> 2525.02]  Thinking back to,
[2525.16 --> 2525.36]  you know,
[2525.38 --> 2526.28]  when we picked this
[2526.28 --> 2526.94]  as a language,
[2527.38 --> 2527.76]  really,
[2528.44 --> 2529.76]  I think part of it
[2529.76 --> 2531.52]  was how well thought out
[2531.52 --> 2533.14]  the language is
[2533.14 --> 2535.78]  and the documentation
[2535.78 --> 2536.70]  that goes with it.
[2536.86 --> 2537.88]  If you're going to learn
[2537.88 --> 2538.64]  a new language
[2538.64 --> 2539.70]  and you just want to learn
[2539.70 --> 2540.20]  a new language,
[2540.32 --> 2541.60]  Go would be a fantastic option.
[2542.06 --> 2543.22]  It's so well put together.
[2543.22 --> 2545.16]  The documentation is there.
[2545.28 --> 2546.62]  The community support is there.
[2546.82 --> 2548.56]  And also the broader
[2548.56 --> 2549.78]  open source community
[2549.78 --> 2550.46]  in the way that
[2550.46 --> 2552.24]  all of this complex functionality
[2552.24 --> 2553.30]  is readily available
[2553.30 --> 2554.34]  for any developer
[2554.34 --> 2556.02]  without having to know
[2556.02 --> 2557.08]  additional tooling.
[2557.34 --> 2557.46]  You know,
[2557.50 --> 2558.62]  that was very compelling
[2558.62 --> 2559.86]  from a language design
[2559.86 --> 2560.50]  point of view.
[2560.76 --> 2561.24]  But really,
[2561.50 --> 2562.66]  the process of writing
[2562.66 --> 2563.10]  the book,
[2563.24 --> 2563.94]  thinking about
[2563.94 --> 2564.70]  the challenges
[2564.70 --> 2565.54]  that have existed
[2565.54 --> 2567.24]  in graphical user interfaces
[2567.24 --> 2568.40]  through the ages
[2568.40 --> 2569.96]  and looking at
[2569.96 --> 2571.06]  the challenges
[2571.06 --> 2573.32]  that existing toolkits
[2573.32 --> 2575.14]  push onto their end users,
[2575.48 --> 2576.78]  I just couldn't help
[2576.78 --> 2577.58]  but notice that
[2577.58 --> 2578.28]  concurrency,
[2579.16 --> 2580.02]  memory management
[2580.02 --> 2581.38]  and building across
[2581.38 --> 2582.22]  multiple platforms,
[2582.34 --> 2583.02]  they were just like
[2583.02 --> 2585.12]  the three standout issues
[2585.12 --> 2586.02]  that really
[2586.02 --> 2586.82]  there was an opportunity
[2586.82 --> 2587.46]  to solve.
[2587.98 --> 2589.04]  And if you put a bullet list
[2589.04 --> 2589.84]  together like that
[2589.84 --> 2590.22]  and you say,
[2590.30 --> 2590.80]  which language
[2590.80 --> 2591.84]  is this a good fit for?
[2592.06 --> 2592.82]  You don't have
[2592.82 --> 2593.64]  a very long list
[2593.64 --> 2594.80]  and Go was really
[2594.80 --> 2595.84]  clearly the top of it.
[2602.58 --> 2603.84]  If practical AI
[2603.84 --> 2604.90]  isn't in your regular
[2604.90 --> 2605.88]  podcast rotation,
[2606.04 --> 2606.94]  it's time to fix that.
[2607.18 --> 2607.86]  Daniel Whitenack
[2607.86 --> 2608.48]  and Chris Benson
[2608.48 --> 2609.38]  are on a mission
[2609.38 --> 2610.80]  to help you put AI tools
[2610.80 --> 2612.12]  and techniques in practice.
[2612.54 --> 2613.06]  Here's a sample
[2613.06 --> 2613.80]  of what to expect
[2613.80 --> 2615.04]  is from episode 64
[2615.04 --> 2616.40]  and the guys are discussing
[2616.40 --> 2617.20]  how OpenAI
[2617.20 --> 2618.64]  trained a pair of neural nets
[2618.64 --> 2620.30]  to enable a robot hand
[2620.30 --> 2621.56]  to solve a Rubik's Cube.
[2621.98 --> 2622.52]  Take a listen.
[2623.64 --> 2625.16]  But here they're talking
[2625.16 --> 2626.24]  about emergent
[2626.24 --> 2627.58]  meta learning,
[2627.80 --> 2628.44]  which sounds like
[2628.44 --> 2631.22]  this really weird term to me.
[2632.24 --> 2633.54]  And it's almost like
[2633.54 --> 2635.10]  a term that doesn't mean anything.
[2635.10 --> 2635.94]  It's like emergent
[2635.94 --> 2636.68]  and it's meta.
[2637.14 --> 2638.80]  Very new age sounding there.
[2639.06 --> 2639.28]  Yeah.
[2639.32 --> 2640.48]  What does that even mean?
[2640.54 --> 2641.26]  I'm not sure.
[2641.38 --> 2642.76]  So what do you get,
[2642.90 --> 2643.28]  if anything,
[2643.28 --> 2644.16]  from that?
[2644.58 --> 2646.80]  Well, I actually drew
[2646.80 --> 2648.62]  an analogy between
[2648.62 --> 2649.84]  what they were doing
[2649.84 --> 2650.32]  with that
[2650.32 --> 2651.12]  and kind of
[2651.12 --> 2652.28]  what we as humans do
[2652.28 --> 2653.70]  in the sense of
[2653.70 --> 2654.50]  as they kept
[2654.50 --> 2655.72]  cranking up the difficulty
[2655.72 --> 2657.64]  by changing the parameters
[2657.64 --> 2658.90]  into something more difficult,
[2658.90 --> 2660.30]  it reminded me
[2660.30 --> 2661.08]  as I read that
[2661.08 --> 2662.08]  about, for instance,
[2662.44 --> 2663.20]  teaching my daughter
[2663.20 --> 2663.86]  to ride a bike
[2663.86 --> 2664.28]  and, you know,
[2664.28 --> 2665.16]  first just learning
[2665.16 --> 2666.40]  how to sit on it
[2666.40 --> 2666.80]  and pedal
[2666.80 --> 2667.94]  with training wheels on
[2667.94 --> 2669.40]  and start steering it
[2669.40 --> 2669.98]  and then
[2669.98 --> 2671.14]  as she got comfortable
[2671.14 --> 2671.68]  with that
[2671.68 --> 2672.30]  and, you know,
[2672.38 --> 2673.60]  going over curbs
[2673.60 --> 2674.36]  and then taking
[2674.36 --> 2675.44]  the training wheels off
[2675.44 --> 2676.20]  and, you know,
[2676.24 --> 2676.86]  having to learn
[2676.86 --> 2677.64]  how to do balance
[2677.64 --> 2678.24]  and all that.
[2678.24 --> 2680.44]  Practical AI
[2680.44 --> 2681.66]  is filled with goodness.
[2682.12 --> 2682.56]  Check it out
[2682.56 --> 2683.84]  at changelog.com
[2683.84 --> 2684.94]  slash practical AI
[2684.94 --> 2685.86]  or just search
[2685.86 --> 2686.60]  for Practical AI
[2686.60 --> 2687.96]  in Apple Podcasts,
[2688.06 --> 2688.52]  Spotify,
[2688.86 --> 2689.58]  or your favorite
[2689.58 --> 2690.50]  podcast directory.
[2690.60 --> 2691.16]  You'll find it.
[2691.34 --> 2691.94]  While you're at it,
[2691.98 --> 2693.10]  upgrade to our master feed
[2693.10 --> 2693.96]  at changelog.com
[2693.96 --> 2694.66]  slash master
[2694.66 --> 2695.92]  and let your podcast app
[2695.92 --> 2697.08]  download all of our shows.
[2697.24 --> 2698.20]  Then you can pick and choose
[2698.20 --> 2699.36]  the ones you're interested in
[2699.36 --> 2700.34]  and skip the rest.
[2700.56 --> 2701.28]  What have you got to lose?
[2701.58 --> 2701.88]  All right,
[2702.16 --> 2702.78]  back to the show.
[2702.78 --> 2716.90]  JavaScript really shines
[2716.90 --> 2717.94]  at some of these aspects.
[2718.38 --> 2718.84]  Like they're,
[2719.34 --> 2719.50]  you know,
[2719.52 --> 2720.40]  like the async model
[2720.40 --> 2721.74]  that JavaScript tends to be
[2721.74 --> 2722.30]  and like the fact
[2722.30 --> 2723.30]  they can react to events
[2723.30 --> 2724.30]  makes it great
[2724.30 --> 2725.22]  for graphical stuff.
[2725.54 --> 2726.42]  But I think that
[2726.42 --> 2727.12]  there's other areas
[2727.12 --> 2729.38]  where it doesn't quite shine
[2729.38 --> 2730.02]  the same ways
[2730.02 --> 2730.64]  that Go does,
[2730.76 --> 2731.60]  which could, you know,
[2731.62 --> 2732.56]  make it a little bit different
[2732.56 --> 2733.62]  and there's also the fact
[2733.62 --> 2734.62]  that people have done this
[2734.62 --> 2735.74]  in JavaScript enough times
[2735.74 --> 2737.16]  that clearly that,
[2737.28 --> 2738.28]  I don't think that would have
[2738.28 --> 2739.46]  necessarily solved the problem
[2739.46 --> 2740.26]  to just do another
[2740.26 --> 2741.60]  JavaScript library to do it.
[2742.66 --> 2743.10]  Absolutely.
[2743.44 --> 2744.02]  And I mean,
[2744.06 --> 2744.36]  honestly,
[2744.36 --> 2745.20]  when it came to
[2745.20 --> 2746.30]  pulling together the content
[2746.30 --> 2747.56]  for the book,
[2747.68 --> 2748.84]  it was commissioned
[2748.84 --> 2751.88]  and one of the key items
[2751.88 --> 2753.22]  in what the book
[2753.22 --> 2753.84]  should contain
[2753.84 --> 2754.44]  was that actually
[2754.44 --> 2756.06]  as well as being easy
[2756.06 --> 2756.70]  to build something
[2756.70 --> 2757.34]  that looked great,
[2757.56 --> 2758.48]  it was important
[2758.48 --> 2759.40]  that these applications
[2759.40 --> 2760.68]  would be performant
[2760.68 --> 2761.52]  that, you know,
[2761.58 --> 2762.42]  as well as being
[2762.42 --> 2764.10]  easily built
[2764.10 --> 2764.90]  that they would run
[2764.90 --> 2765.62]  really well.
[2766.50 --> 2767.72]  And so for that reason,
[2767.72 --> 2768.20]  we thought,
[2768.32 --> 2769.18]  well, actually,
[2769.50 --> 2769.74]  you know,
[2769.76 --> 2770.90]  let's not go with
[2770.90 --> 2772.44]  embedded browser engines
[2772.44 --> 2773.80]  and a JavaScript stack.
[2773.94 --> 2774.70]  And that's not to say
[2774.70 --> 2775.70]  that it can't be done
[2775.70 --> 2776.62]  with JavaScript,
[2777.24 --> 2778.94]  but if you were looking
[2778.94 --> 2779.48]  to compare
[2779.48 --> 2780.42]  a lot of technologies,
[2780.42 --> 2781.18]  I don't imagine
[2781.18 --> 2782.22]  that would be
[2782.22 --> 2783.16]  a huge number
[2783.16 --> 2783.92]  that really thought
[2783.92 --> 2784.50]  that performance
[2784.50 --> 2786.08]  was really top of the list
[2786.08 --> 2787.32]  if that was the technology
[2787.32 --> 2788.08]  stack you were using.
[2788.30 --> 2789.38]  And so I took the opportunity
[2789.38 --> 2789.94]  to say,
[2790.02 --> 2790.24]  well,
[2790.24 --> 2790.88]  in that case,
[2790.94 --> 2792.22]  let's not look
[2792.22 --> 2793.16]  at web technologies,
[2793.16 --> 2794.02]  let's just look
[2794.02 --> 2794.32]  at the way
[2794.32 --> 2794.88]  that people are doing
[2794.88 --> 2795.54]  this natively.
[2795.64 --> 2796.56]  And I think it felt
[2796.56 --> 2797.36]  like a much more
[2797.36 --> 2798.42]  clean story
[2798.42 --> 2799.46]  about the history
[2799.46 --> 2800.52]  and future
[2800.52 --> 2801.92]  of graphical user interfaces.
[2802.64 --> 2803.18]  Of course,
[2803.26 --> 2803.52]  we'd go,
[2803.66 --> 2804.18]  but yeah.
[2805.18 --> 2806.72]  So if we're looking
[2806.72 --> 2807.24]  at different ways
[2807.24 --> 2807.96]  to build GUIs
[2807.96 --> 2808.36]  in Go,
[2808.82 --> 2809.66]  I guess first off,
[2809.70 --> 2810.34]  can we talk about
[2810.34 --> 2811.20]  just what options
[2811.20 --> 2811.56]  are there?
[2811.70 --> 2813.00]  So you created Fine,
[2813.50 --> 2814.06]  you mentioned
[2814.06 --> 2814.86]  Anlabs UI,
[2815.06 --> 2815.74]  which is the one
[2815.74 --> 2817.12]  that compiles down
[2817.12 --> 2817.44]  to something
[2817.44 --> 2818.06]  that looks native
[2818.06 --> 2818.72]  to the OS.
[2819.60 --> 2820.38]  What other ones
[2820.38 --> 2820.82]  are out there
[2820.82 --> 2821.88]  and can you talk
[2821.88 --> 2822.22]  a little bit
[2822.22 --> 2823.88]  about how they're
[2823.88 --> 2824.40]  going about
[2824.40 --> 2825.34]  rendering the UI?
[2825.64 --> 2826.26]  Does that make sense?
[2827.18 --> 2827.50]  Yeah,
[2827.56 --> 2828.44]  I can try.
[2828.86 --> 2829.20]  Honestly,
[2829.30 --> 2830.28]  the list is too long.
[2830.38 --> 2831.86]  I'm going to miss people out
[2831.86 --> 2833.16]  if I try to pick through them.
[2833.64 --> 2834.64]  And I hope this list
[2834.64 --> 2835.76]  doesn't show
[2835.76 --> 2837.86]  any of my particular prejudices,
[2838.00 --> 2839.28]  but it's somewhat inevitable.
[2839.76 --> 2840.02]  So yeah,
[2840.08 --> 2841.72]  I mentioned Anlabs.
[2842.20 --> 2843.60]  There are absolutely
[2843.60 --> 2844.30]  great projects
[2844.30 --> 2844.94]  that will bind
[2844.94 --> 2846.06]  to existing technologies
[2846.06 --> 2846.62]  as well.
[2846.90 --> 2847.50]  There's a couple
[2847.50 --> 2848.10]  of different ones
[2848.10 --> 2849.14]  for GTK
[2849.14 --> 2850.12]  and for Qt.
[2850.22 --> 2851.64]  So if that's something
[2851.64 --> 2852.10]  that you would like
[2852.10 --> 2852.64]  to play with,
[2852.84 --> 2853.60]  there's some really
[2853.60 --> 2854.40]  great stuff there.
[2854.88 --> 2855.48]  You might need
[2855.48 --> 2857.00]  a bigger amount
[2857.00 --> 2857.70]  of free space
[2857.70 --> 2859.08]  on your hard drive
[2859.08 --> 2860.02]  to be able to set those up.
[2860.22 --> 2861.50]  But they are established
[2861.50 --> 2862.76]  projects with really
[2862.76 --> 2863.62]  substantial APIs.
[2864.02 --> 2864.96]  If we're looking at
[2864.96 --> 2866.22]  things that are
[2866.22 --> 2867.60]  a little bit different,
[2867.74 --> 2868.08]  I guess,
[2868.36 --> 2869.04]  a few years ago
[2869.04 --> 2869.60]  there was a couple
[2869.60 --> 2871.04]  of famous projects,
[2871.28 --> 2872.24]  the GXUI
[2872.24 --> 2873.94]  and the Shiny projects.
[2873.94 --> 2875.10]  GXUI,
[2875.78 --> 2876.16]  actually,
[2876.38 --> 2877.06]  I don't know
[2877.06 --> 2877.90]  a huge amount about
[2877.90 --> 2879.16]  because that kind of
[2879.16 --> 2880.14]  went dormant
[2880.14 --> 2881.16]  a number of years ago.
[2881.62 --> 2882.36]  And although it was
[2882.36 --> 2883.32]  interesting,
[2883.46 --> 2884.18]  maybe when I started
[2884.18 --> 2885.08]  researching the book,
[2885.28 --> 2886.28]  it seemed like
[2886.28 --> 2887.32]  it wasn't really
[2887.32 --> 2888.68]  going to pick up.
[2889.38 --> 2889.86]  And so I looked
[2889.86 --> 2890.74]  at Shiny instead.
[2891.38 --> 2892.86]  This was a project
[2892.86 --> 2894.06]  that was put together
[2894.06 --> 2894.72]  by some people,
[2895.06 --> 2895.44]  I think,
[2895.54 --> 2896.30]  on the Go team,
[2896.38 --> 2896.90]  although I honestly
[2896.90 --> 2897.46]  can't remember
[2897.46 --> 2898.28]  their names right now.
[2898.78 --> 2899.24]  Apologies.
[2899.24 --> 2900.58]  And this was,
[2900.88 --> 2901.58]  I guess,
[2901.62 --> 2902.84]  a really powerful
[2902.84 --> 2903.68]  technology demo,
[2903.80 --> 2904.02]  I suppose,
[2904.10 --> 2904.68]  of what could be
[2904.68 --> 2905.24]  done with Go.
[2905.52 --> 2906.40]  They implemented
[2906.40 --> 2907.86]  in very,
[2908.10 --> 2908.46]  I think,
[2908.56 --> 2909.22]  similar ways
[2909.22 --> 2910.40]  the OpenGL
[2910.40 --> 2911.92]  drivers
[2911.92 --> 2913.04]  and an abstraction
[2913.04 --> 2913.84]  on how you might
[2913.84 --> 2915.02]  paint using
[2915.02 --> 2915.74]  Go primitives.
[2916.28 --> 2916.84]  And in fact,
[2917.04 --> 2917.76]  it is used,
[2917.84 --> 2918.20]  I believe,
[2918.34 --> 2919.06]  for certain
[2919.06 --> 2920.22]  runtime configurations
[2920.22 --> 2921.30]  in the Go mobile
[2921.30 --> 2921.88]  project.
[2922.28 --> 2922.86]  To this day,
[2922.96 --> 2923.54]  it's a really
[2923.54 --> 2924.46]  solid project.
[2924.62 --> 2925.28]  It just doesn't
[2925.28 --> 2926.40]  really have much
[2926.40 --> 2927.08]  widget toolkit
[2927.08 --> 2928.04]  built on top of it.
[2928.04 --> 2929.40]  It sort of stopped
[2929.40 --> 2930.02]  where it was.
[2930.44 --> 2931.50]  Then there is
[2931.50 --> 2932.98]  the Geo project,
[2933.56 --> 2934.82]  which is being run
[2934.82 --> 2936.26]  by Elias Nure,
[2936.44 --> 2937.32]  if I remember
[2937.32 --> 2937.98]  his name correctly.
[2938.46 --> 2938.76]  Actually,
[2938.86 --> 2939.58]  I think kind of
[2939.58 --> 2941.06]  contemporary with Fine
[2941.06 --> 2941.92]  has been going
[2941.92 --> 2943.30]  for a couple of years
[2943.30 --> 2943.84]  thereabout.
[2944.26 --> 2944.90]  But the approach
[2944.90 --> 2946.62]  that that project
[2946.62 --> 2947.52]  has taken is,
[2948.02 --> 2949.58]  although rendering
[2949.58 --> 2951.30]  a similar low-level
[2951.30 --> 2952.44]  API behind the scenes,
[2952.54 --> 2953.02]  they're using
[2953.02 --> 2954.54]  an immediate mode
[2954.54 --> 2955.96]  API as opposed
[2955.96 --> 2957.20]  to the retain mode
[2957.20 --> 2958.12]  that Fine
[2958.12 --> 2958.74]  has put together.
[2959.08 --> 2959.56]  Basically,
[2959.72 --> 2960.26]  what that means
[2960.26 --> 2961.78]  is that each time
[2961.78 --> 2963.20]  the user interface
[2963.20 --> 2963.84]  wants to render
[2963.84 --> 2964.50]  a refresh,
[2965.00 --> 2966.88]  then the developer's
[2966.88 --> 2967.58]  code is going
[2967.58 --> 2968.10]  to describe
[2968.10 --> 2969.16]  how the system
[2969.16 --> 2969.72]  should look
[2969.72 --> 2970.94]  at that point
[2970.94 --> 2971.40]  in time.
[2972.14 --> 2972.68]  And that's really
[2972.68 --> 2973.56]  powerful for
[2973.56 --> 2974.48]  games development
[2974.48 --> 2976.02]  embedded systems.
[2976.58 --> 2977.10]  And actually,
[2977.56 --> 2978.90]  it's a manner
[2978.90 --> 2979.70]  of putting together
[2979.70 --> 2980.42]  a graphics API
[2980.42 --> 2981.26]  that's gaining
[2981.26 --> 2981.72]  popularity
[2981.72 --> 2983.02]  in many areas.
[2983.02 --> 2985.02]  But the approach
[2985.02 --> 2985.50]  that I wanted
[2985.50 --> 2986.24]  to take with Fine
[2986.24 --> 2987.22]  was to say,
[2987.38 --> 2987.68]  actually,
[2988.18 --> 2988.68]  this is going
[2988.68 --> 2989.66]  to be minimal code
[2989.66 --> 2991.12]  for the end developer.
[2991.64 --> 2992.14]  We're going to make
[2992.14 --> 2992.80]  a lot of assumptions
[2992.80 --> 2993.60]  on their behalf.
[2993.84 --> 2994.56]  And in that regard,
[2995.00 --> 2995.90]  Fine is a very
[2995.90 --> 2997.14]  opinionated toolkit.
[2997.52 --> 2998.58]  It looks a certain way,
[2998.64 --> 2999.58]  it behaves a certain way,
[2999.62 --> 3000.36]  and if you like it,
[3000.40 --> 3000.60]  brilliant.
[3000.72 --> 3001.16]  And if not,
[3001.52 --> 3002.30]  it's maybe not going
[3002.30 --> 3002.88]  to be for you.
[3002.96 --> 3004.26]  Whereas a toolkit
[3004.26 --> 3006.04]  that's got more flexibility
[3006.04 --> 3008.64]  could be very tempting
[3008.64 --> 3010.08]  to folk who actually
[3010.08 --> 3010.66]  want to control
[3010.66 --> 3013.16]  every single aspect
[3013.16 --> 3014.58]  of how their application
[3014.58 --> 3015.24]  is going to work.
[3015.60 --> 3016.92]  I am sure that I have
[3016.92 --> 3017.78]  missed a couple
[3017.78 --> 3019.04]  off that list.
[3019.52 --> 3021.00]  I think that there's
[3021.00 --> 3022.32]  always also bindings
[3022.32 --> 3023.52]  to other systems.
[3023.74 --> 3024.72]  The nuclear project
[3024.72 --> 3026.40]  is quite interesting.
[3026.52 --> 3027.78]  That contains Go bindings
[3027.78 --> 3029.24]  that are pretty easy
[3029.24 --> 3029.66]  to use.
[3030.48 --> 3031.76]  And then you've got
[3031.76 --> 3034.24]  Wales and Walk
[3034.24 --> 3035.76]  for Windows-specific
[3035.76 --> 3036.28]  APIs.
[3037.08 --> 3038.22]  And there are other
[3038.22 --> 3039.54]  platforms out there
[3039.54 --> 3040.66]  for solving
[3040.66 --> 3041.72]  particular problems,
[3041.88 --> 3042.96]  but I've really only
[3042.96 --> 3043.74]  looked into the ones
[3043.74 --> 3044.28]  that we're aiming
[3044.28 --> 3045.80]  to make cross-platform
[3045.80 --> 3046.80]  graphical apps.
[3047.14 --> 3047.76]  I hope I've not missed
[3047.76 --> 3048.58]  anybody out there
[3048.58 --> 3049.12]  that thinks they're
[3049.12 --> 3049.96]  really happening
[3049.96 --> 3050.90]  in this space right now.
[3051.76 --> 3052.88]  I think everybody
[3052.88 --> 3053.98]  understands that that's,
[3054.08 --> 3055.16]  it's hard to list everybody.
[3055.68 --> 3057.16]  So, I've only looked
[3057.16 --> 3058.04]  at Wales very briefly,
[3058.34 --> 3059.20]  but is that one that uses,
[3059.38 --> 3060.18]  does it use Vue.js
[3060.18 --> 3061.14]  or is it use something,
[3062.00 --> 3063.02]  I wasn't sure what it was
[3063.02 --> 3063.84]  using to actually render
[3063.84 --> 3064.66]  stuff, because it seemed
[3064.66 --> 3066.38]  like Fine had this
[3066.38 --> 3067.88]  model of,
[3067.88 --> 3068.64]  like you said,
[3068.72 --> 3069.56]  we kind of have
[3069.56 --> 3070.94]  an idea of what each
[3070.94 --> 3071.74]  component looks like,
[3071.76 --> 3072.36]  and you kind of use
[3072.36 --> 3073.40]  our predefined component
[3073.40 --> 3074.24]  type design.
[3074.78 --> 3075.30]  And Labs was,
[3075.38 --> 3075.82]  like you said,
[3075.90 --> 3076.56]  try to get everything
[3076.56 --> 3077.76]  native, like looking,
[3078.28 --> 3079.32]  and it looked like Wales
[3079.32 --> 3080.28]  was more of a,
[3080.40 --> 3080.72]  you know,
[3080.72 --> 3081.56]  like a wrapper around
[3081.56 --> 3082.64]  like a JavaScript type
[3082.64 --> 3084.24]  view that you had a
[3084.24 --> 3084.90]  little more customization
[3084.90 --> 3086.20]  around, but it wasn't
[3086.20 --> 3087.20]  necessarily native.
[3087.64 --> 3088.34]  Is that correct?
[3088.80 --> 3089.78]  That's my understanding.
[3090.26 --> 3090.96]  Actually, that's probably
[3090.96 --> 3092.24]  about the limit of my
[3092.24 --> 3093.04]  understanding of the
[3093.04 --> 3093.86]  project as well,
[3093.92 --> 3095.16]  because it falls in the
[3095.16 --> 3097.04]  category of hybrid or
[3097.04 --> 3098.64]  using web technologies.
[3098.76 --> 3099.58]  I haven't explored it
[3099.58 --> 3100.88]  anywhere near as much
[3100.88 --> 3101.88]  as the other ones that
[3101.88 --> 3102.98]  I spoke about there.
[3103.48 --> 3104.58]  Yeah, I know that this
[3104.58 --> 3105.38]  is a space that it would
[3105.38 --> 3106.44]  be fun to go build
[3106.44 --> 3107.86]  projects in like every
[3107.86 --> 3108.62]  one of, like, you know,
[3108.62 --> 3109.28]  try to build a small
[3109.28 --> 3110.14]  project in each one of
[3110.14 --> 3111.74]  these, because even like
[3111.74 --> 3112.56]  you'd said, like some of
[3112.56 --> 3113.30]  these are a little bit
[3113.30 --> 3115.52]  more involved, and I've
[3115.52 --> 3117.06]  never dove into those.
[3117.32 --> 3119.04]  So you say it's, is it
[3119.04 --> 3120.56]  cutie, or I don't know
[3120.56 --> 3121.18]  how you pronounce that
[3121.18 --> 3121.36]  one.
[3121.96 --> 3122.92]  Well, I think it's, I
[3122.92 --> 3123.42]  think it's pronounced
[3123.42 --> 3124.08]  cute.
[3124.50 --> 3124.72]  Cute?
[3124.72 --> 3125.04]  Okay.
[3125.18 --> 3125.74]  I was going to say, like,
[3125.74 --> 3126.14]  I don't even know how
[3126.14 --> 3126.58]  to pronounce it.
[3126.66 --> 3127.58]  That's how limited my
[3127.58 --> 3128.40]  exposure is there.
[3128.84 --> 3130.00]  So I'm just like, all
[3130.00 --> 3130.92]  right, I see people doing
[3130.92 --> 3131.96]  this, but I've just never
[3131.96 --> 3132.56]  gotten there.
[3133.00 --> 3135.04]  People tend to pick a
[3135.04 --> 3135.92]  camp, you know, one that
[3135.92 --> 3136.80]  works for them for the
[3136.80 --> 3137.78]  reasons that they need at
[3137.78 --> 3138.80]  that time, and they just
[3138.80 --> 3139.70]  get passionate about it
[3139.70 --> 3141.04]  because it's solving the
[3141.04 --> 3142.02]  problems that they want.
[3142.24 --> 3143.50]  And I think that people
[3143.50 --> 3144.36]  who are picking up
[3144.36 --> 3146.04]  graphical app development
[3146.04 --> 3147.62]  now are looking to
[3147.62 --> 3148.70]  solve different problems.
[3149.12 --> 3150.08]  One of the challenges I
[3150.08 --> 3151.22]  realized when exploring
[3151.22 --> 3152.88]  this is that very few of
[3152.88 --> 3153.74]  them have any web
[3153.74 --> 3154.74]  services integration.
[3154.74 --> 3155.68]  They don't really help
[3155.68 --> 3157.22]  you with persisting state
[3157.22 --> 3158.38]  between user sessions or
[3158.38 --> 3159.76]  even different devices.
[3159.76 --> 3161.30]  And I'm thinking, you know,
[3161.30 --> 3162.22]  if we can solve all of
[3162.22 --> 3163.54]  those things, you don't
[3163.54 --> 3164.86]  have to be on the web to
[3164.86 --> 3166.42]  take advantage of modern
[3166.42 --> 3167.56]  cloud-based technologies.
[3167.56 --> 3170.46]  And so, yeah, the right tool
[3170.46 --> 3171.48]  for building something is
[3171.48 --> 3172.40]  not necessarily the same
[3172.40 --> 3173.24]  tool as you want for
[3173.24 --> 3174.18]  communicating with back
[3174.18 --> 3175.76]  ends, sorry, through the
[3175.76 --> 3176.50]  back end systems.
[3176.76 --> 3179.04]  And so, yeah, native apps,
[3179.12 --> 3180.62]  I think, have got an
[3180.62 --> 3182.24]  opportunity to perhaps gain
[3182.24 --> 3182.82]  a little bit more
[3182.82 --> 3183.88]  popularity if we really
[3183.88 --> 3184.98]  could make the cross-
[3184.98 --> 3185.78]  platform work well.
[3186.58 --> 3188.26]  I also liked, you had
[3188.26 --> 3188.92]  mentioned that a lot of
[3188.92 --> 3190.06]  people are using find to do
[3190.06 --> 3191.10]  things like take something
[3191.10 --> 3192.70]  that's command line and make
[3192.70 --> 3193.74]  it a little bit more user
[3193.74 --> 3196.04]  accessible, which I find
[3196.04 --> 3197.20]  useful because I've found
[3197.20 --> 3198.60]  myself doing random one-off
[3198.60 --> 3199.50]  tasks for my wife.
[3199.76 --> 3200.70]  So my wife's a photographer
[3200.70 --> 3201.66]  and like there have been
[3201.66 --> 3202.52]  times where she's like
[3202.52 --> 3203.86]  imported all the photos
[3203.86 --> 3204.62]  twice in a folder.
[3204.76 --> 3205.60]  So she's got a bunch that
[3205.60 --> 3206.64]  have like the space to at
[3206.64 --> 3206.98]  the end.
[3207.42 --> 3208.56]  And as a programmer, you're
[3208.56 --> 3210.12]  like, it takes no time at
[3210.12 --> 3210.68]  all to write something.
[3210.74 --> 3211.44]  It just goes and deletes
[3211.44 --> 3211.84]  those all.
[3211.86 --> 3212.44]  And she doesn't want to go
[3212.44 --> 3213.24]  through and manually delete
[3213.24 --> 3213.48]  them all.
[3213.54 --> 3214.70]  That's just really tedious
[3214.70 --> 3215.70]  for thousands of photos.
[3216.38 --> 3217.74]  So, you know, I see that
[3217.74 --> 3218.20]  and I'm like, all right,
[3218.20 --> 3218.96]  this would be cool to build
[3218.96 --> 3220.26]  a little, you know, a UI for
[3220.26 --> 3221.50]  her to work with that she's
[3221.50 --> 3222.48]  not going to mess things up.
[3222.64 --> 3223.54]  She can choose the right
[3223.54 --> 3224.62]  folder and sort of do it.
[3225.20 --> 3226.08]  And like, I think there's
[3226.08 --> 3227.44]  a lot of small problems
[3227.44 --> 3228.28]  that could be solved that
[3228.28 --> 3228.50]  way.
[3228.70 --> 3230.90]  So if somebody wants to get
[3230.90 --> 3231.54]  into this, you know,
[3231.58 --> 3232.32]  building something with a
[3232.32 --> 3233.34]  graphical user interface,
[3233.82 --> 3235.50]  do you have suggestions for
[3235.50 --> 3235.66]  them?
[3235.68 --> 3236.52]  Like where would you suggest
[3236.52 --> 3237.12]  they start?
[3237.30 --> 3238.42]  What types of projects
[3238.42 --> 3239.26]  should they keep an eye out
[3239.26 --> 3239.62]  for?
[3240.32 --> 3241.50]  Before you answer, Andy.
[3241.66 --> 3242.06]  Okay.
[3243.04 --> 3244.96]  John, there is nothing wrong
[3244.96 --> 3246.42]  with a command line
[3246.42 --> 3247.14]  interface.
[3247.56 --> 3248.50]  No, there's nothing wrong
[3248.50 --> 3249.66]  with it when we're using it.
[3249.66 --> 3250.60]  But if I'm trying to show
[3250.60 --> 3251.54]  my wife how to use it,
[3251.58 --> 3252.28]  there's a problem.
[3252.28 --> 3255.20]  It sounds like you need to
[3255.20 --> 3256.34]  teach your wife how to use
[3256.34 --> 3257.48]  the command line, my friend.
[3257.62 --> 3258.78]  What happens is she says,
[3258.92 --> 3260.18]  honey, please come do this
[3260.18 --> 3260.78]  for me again.
[3260.92 --> 3262.30]  So I just do it every time.
[3265.46 --> 3267.16]  I think how you get started,
[3267.42 --> 3268.66]  you know, kind of depends on
[3268.66 --> 3270.42]  what you want to do.
[3270.72 --> 3271.72]  At the moment, there's a lot
[3271.72 --> 3273.34]  to explore and somebody who's
[3273.34 --> 3275.00]  curious should definitely check
[3275.00 --> 3278.00]  out the awesome list.
[3278.40 --> 3280.20]  Go to the GUI section in
[3280.20 --> 3281.46]  Awesome Go and see what's
[3281.46 --> 3284.30]  there and just try them
[3284.30 --> 3284.48]  all.
[3284.60 --> 3285.86]  Like really, I mean,
[3285.90 --> 3287.48]  personally, I would think
[3287.48 --> 3288.48]  if somebody wants to get up
[3288.48 --> 3289.52]  and running with something
[3289.52 --> 3292.24]  graphical in Go, then they
[3292.24 --> 3293.90]  should absolutely head to
[3293.90 --> 3296.04]  the find.io homepage and
[3296.04 --> 3296.92]  have a little read.
[3297.06 --> 3299.32]  We put together a tour that
[3299.32 --> 3300.60]  kind of follows the format
[3300.60 --> 3302.60]  that the Go tour used because
[3302.60 --> 3304.12]  it's just like so easy to pick
[3304.12 --> 3304.76]  up really quickly.
[3304.96 --> 3306.38]  And so we step people through
[3306.38 --> 3308.64]  what it means to put together
[3308.64 --> 3310.70]  graphical application, you
[3310.70 --> 3311.92]  know, how applications relate
[3311.92 --> 3313.26]  to Windows and how content
[3313.26 --> 3315.62]  is handled and callbacks,
[3315.68 --> 3316.28]  that kind of thing.
[3316.60 --> 3317.52]  So I'm going to like
[3317.52 --> 3318.82]  absolutely just say that
[3318.82 --> 3320.06]  that's the way you should go.
[3320.48 --> 3321.62]  But given the graphical
[3321.62 --> 3322.72]  nature of it, I would also
[3322.72 --> 3324.24]  say head to YouTube, see
[3324.24 --> 3325.10]  what you can find.
[3325.34 --> 3326.44]  There's such a good selection
[3326.44 --> 3327.90]  of demos out there.
[3328.26 --> 3329.56]  And if you if you put a
[3329.56 --> 3332.06]  couple of key search terms
[3332.06 --> 3333.02]  in there, you're going to
[3333.02 --> 3334.36]  see a huge variety of
[3334.36 --> 3335.00]  different things.
[3335.00 --> 3336.54]  And the code tutorials
[3336.54 --> 3337.70]  often come with them.
[3338.94 --> 3340.90]  Yeah, that's I mean,
[3340.98 --> 3342.56]  that's sort of my my
[3342.56 --> 3343.50]  biased angle on it.
[3343.78 --> 3346.68]  Also, the GopherCon talks.
[3347.16 --> 3348.38]  I know this this this has
[3348.38 --> 3349.68]  come up a couple of times
[3349.68 --> 3351.82]  a go lab and hopefully
[3351.82 --> 3352.74]  you can discover more
[3352.74 --> 3354.38]  upcoming conferences as
[3354.38 --> 3354.66]  well.
[3355.06 --> 3356.82]  Although it's as an unusual
[3356.82 --> 3358.40]  use for go, it's not
[3358.40 --> 3359.92]  something that gets a lot
[3359.92 --> 3361.86]  of airtime on the bigger
[3361.86 --> 3363.52]  conferences because it's not
[3363.52 --> 3364.54]  what people go there for.
[3365.00 --> 3365.14]  Yeah.
[3365.26 --> 3367.34]  So I guess, yeah, a bit of
[3367.34 --> 3368.28]  go code up and running in
[3368.28 --> 3369.44]  your favorite editor and
[3369.44 --> 3370.58]  start typing out some
[3370.58 --> 3372.48]  keywords and it's going to
[3372.48 --> 3373.66]  discover these for you,
[3373.76 --> 3374.48]  suggest how you pull
[3374.48 --> 3375.08]  something together.
[3375.40 --> 3376.62]  A little application is
[3376.62 --> 3377.86]  really only going to take a
[3377.86 --> 3378.78]  couple more lines of code
[3378.78 --> 3379.60]  than the command line
[3379.60 --> 3380.14]  application.
[3381.00 --> 3383.24]  Not everybody's really
[3383.24 --> 3384.94]  thinking quite so so big as
[3384.94 --> 3386.12]  as some of the fine team
[3386.12 --> 3386.72]  who are currently
[3386.72 --> 3388.54]  reinventing the desktop by
[3388.54 --> 3389.78]  building that from scratch
[3389.78 --> 3391.14]  and in go as well.
[3391.58 --> 3393.44]  There's a very big space for
[3393.44 --> 3394.96]  innovative and exciting
[3394.96 --> 3396.74]  applications in between
[3396.74 --> 3398.34]  those two and I think it
[3398.34 --> 3399.18]  doesn't have to be
[3399.18 --> 3399.94]  difficult anymore.
[3400.28 --> 3401.26]  You know, this is something
[3401.26 --> 3404.10]  that really is so much
[3404.10 --> 3405.78]  simpler in a modern,
[3406.20 --> 3407.08]  higher level language.
[3407.08 --> 3410.24]  So I would say that, so don't
[3410.24 --> 3410.96]  say, don't sell yourself
[3410.96 --> 3411.28]  short.
[3411.36 --> 3412.14]  Don't sell this project
[3412.14 --> 3412.76]  short, right?
[3412.76 --> 3414.46]  So at Go conferences
[3414.46 --> 3417.38]  currently, and I can speak
[3417.38 --> 3418.56]  very confidently, at least
[3418.56 --> 3421.06]  for Go4Con, that there are
[3421.06 --> 3422.82]  way more folks that are new
[3422.82 --> 3424.48]  to Go coming into the
[3424.48 --> 3426.06]  community than there are
[3426.06 --> 3426.96]  experienced developers.
[3427.40 --> 3428.70]  That's currently the state of
[3428.70 --> 3429.26]  affairs, right?
[3429.28 --> 3431.68]  We have way more newbies than
[3431.68 --> 3432.54]  any number of experienced
[3432.54 --> 3433.46]  developers, right?
[3433.94 --> 3434.92]  So a lot of folks are going
[3434.92 --> 3436.74]  to be coming to the language
[3436.74 --> 3437.84]  and to the community through
[3437.84 --> 3438.82]  different avenues, right?
[3438.88 --> 3441.20]  The bigger the population,
[3441.50 --> 3441.64]  right?
[3441.70 --> 3442.96]  The more variation you're
[3442.96 --> 3444.26]  going to have and basically
[3444.26 --> 3445.92]  for people to take up the
[3445.92 --> 3446.48]  language, right?
[3446.50 --> 3448.32]  So if somebody wants, who's
[3448.32 --> 3449.98]  familiar with the other
[3449.98 --> 3452.20]  Goie frameworks and they
[3452.20 --> 3454.16]  want to also learn Go, maybe
[3454.16 --> 3456.12]  fine is the gateway, right?
[3456.16 --> 3457.16]  That's the gateway by which
[3457.16 --> 3457.98]  they come into the Go
[3457.98 --> 3458.26]  community.
[3458.42 --> 3459.36]  So I think you're going to
[3459.36 --> 3460.96]  see a lot more of this type
[3460.96 --> 3462.88]  of adoption through non
[3462.88 --> 3464.20]  traditional avenues, right?
[3464.24 --> 3465.88]  For new Go beginners.
[3466.72 --> 3467.72]  That's really good to hear
[3467.72 --> 3468.00]  actually.
[3468.12 --> 3468.90]  I think you're right.
[3468.98 --> 3470.18]  There's so many more people
[3470.18 --> 3471.92]  coming into it now that we
[3471.92 --> 3473.52]  do need to think, you know,
[3473.56 --> 3475.32]  how are you bringing this to
[3475.32 --> 3476.92]  brand new folk, not to
[3476.92 --> 3478.54]  established Go developers?
[3479.38 --> 3481.04]  And I think that we've been
[3481.04 --> 3482.44]  bearing that in mind, you
[3482.44 --> 3483.46]  know, how do you make this
[3483.46 --> 3484.98]  obvious for the first time
[3484.98 --> 3486.54]  developer of which a lot do
[3486.54 --> 3488.24]  fine and then apologize for the
[3488.24 --> 3489.32]  questions and we say, no, no,
[3489.32 --> 3491.48]  we want to know what you're
[3491.48 --> 3492.44]  struggling with so we can make
[3492.44 --> 3492.76]  it better.
[3493.10 --> 3494.52]  I think actually one of the
[3494.52 --> 3496.74]  unexpected challenges is that
[3496.74 --> 3498.18]  sometimes people come across
[3498.18 --> 3499.36]  the fine project and they want
[3499.36 --> 3500.08]  to learn Go and they're
[3500.08 --> 3501.44]  familiar with GUIs and they're
[3501.44 --> 3504.12]  confused about why a thing
[3504.12 --> 3505.32]  that's really difficult for
[3505.32 --> 3506.96]  them isn't even present in the
[3506.96 --> 3508.22]  language or the toolkit.
[3508.54 --> 3509.38]  And there are a couple of
[3509.38 --> 3510.80]  times where folks say, no, no,
[3510.82 --> 3512.66]  you're missing this capability.
[3513.30 --> 3514.16]  And actually we have to say,
[3514.24 --> 3515.60]  well, you know, we've designed
[3515.60 --> 3516.40]  it slightly differently.
[3516.40 --> 3517.18]  That thing that you're
[3517.18 --> 3518.86]  familiar with struggling with,
[3518.86 --> 3520.68]  like, just completely forget it.
[3520.80 --> 3521.80]  And so, you know, the
[3521.80 --> 3523.12]  preconceptions that people can
[3523.12 --> 3524.78]  have is actually, I think,
[3524.84 --> 3527.32]  harder work to help with than
[3527.32 --> 3528.88]  somebody coming in going, oh,
[3528.88 --> 3529.92]  man, I completely don't know
[3529.92 --> 3530.06]  this.
[3530.10 --> 3530.56]  What do I do?
[3530.62 --> 3532.18]  Because in that regard, you
[3532.18 --> 3532.74]  point them at some
[3532.74 --> 3534.28]  documentation or video.
[3535.02 --> 3536.50]  But if somebody knows an old
[3536.50 --> 3537.82]  system and they want to try and,
[3537.82 --> 3539.24]  you know, kind of break free of
[3539.24 --> 3542.00]  it, that's a lot of built in
[3542.00 --> 3544.14]  learning and you don't
[3544.14 --> 3546.70]  necessarily know where it came
[3546.70 --> 3548.78]  from or why they picked up a
[3548.78 --> 3549.50]  previous system.
[3549.70 --> 3551.08]  And so perhaps some re-education
[3551.08 --> 3553.32]  to do, but also perhaps we do
[3553.32 --> 3554.36]  need to make something that
[3554.36 --> 3556.14]  looks more familiar or adapt to
[3556.14 --> 3558.06]  familiar use cases if that
[3558.06 --> 3560.06]  seems like, you know, the right
[3560.06 --> 3560.58]  thing to do.
[3561.58 --> 3562.52]  Matt likes to do the segment
[3562.52 --> 3564.44]  where we ask our guests, what is
[3564.44 --> 3565.58]  their unpopular opinion?
[3565.58 --> 3566.80]  And it can be a tech opinion.
[3566.96 --> 3568.06]  I think he kind of leans towards
[3568.06 --> 3569.30]  that, but it doesn't have to be.
[3587.68 --> 3590.00]  So Andy, what is your unpopular
[3590.00 --> 3591.22]  opinion that you'd like to share?
[3592.40 --> 3595.30]  Well, so I thought about this and I
[3595.30 --> 3596.80]  don't know how unpopular it is.
[3596.80 --> 3599.22]  I think that people might agree
[3599.22 --> 3600.84]  with it, but often don't.
[3601.54 --> 3602.80]  And so I thought I would say that
[3602.80 --> 3606.24]  to me, a quality engineered
[3606.24 --> 3608.10]  approach is more important than
[3608.10 --> 3609.14]  the speed of development.
[3610.42 --> 3613.08]  So this may be completely obvious
[3613.08 --> 3614.78]  to some folk or it may be pretty
[3614.78 --> 3615.26]  challenging.
[3615.80 --> 3617.64]  And if you're, you know, building a
[3617.64 --> 3619.64]  project to a deadline, there's
[3619.64 --> 3620.76]  obviously going to be a time
[3620.76 --> 3623.16]  pressure, but I'd far more like to
[3623.16 --> 3624.88]  be involved in a project where they
[3624.88 --> 3626.44]  took their time, thought it through,
[3626.44 --> 3628.66]  and built something that was pretty
[3628.66 --> 3629.06]  solid.
[3629.76 --> 3631.52]  And, you know, maybe it was later,
[3631.62 --> 3632.48]  maybe it didn't have the
[3632.48 --> 3634.40]  functionality that was expected, but
[3634.40 --> 3635.76]  it's something to build on.
[3636.00 --> 3638.20]  And looking project to project, it's
[3638.20 --> 3639.36]  perhaps a little bit different,
[3639.48 --> 3641.76]  some difficult to think which is
[3641.76 --> 3642.34]  more important.
[3642.64 --> 3645.48]  But I look at the overall ecosystem
[3645.48 --> 3647.42]  of applications that we build our
[3647.42 --> 3648.18]  lives on now.
[3648.62 --> 3650.22]  And I think, goodness, you know, if
[3650.22 --> 3651.64]  actually somebody had taken a little
[3651.64 --> 3653.68]  bit longer, thought this through,
[3653.68 --> 3656.08]  then maybe, you know, maybe it would
[3656.08 --> 3657.44]  work a little bit better or maybe it
[3657.44 --> 3660.04]  could be easier maintained.
[3660.50 --> 3662.48]  And so although the fine project is
[3662.48 --> 3664.22]  about helping people get up and
[3664.22 --> 3665.44]  running with graphical apps really
[3665.44 --> 3667.42]  quickly, actually what's more
[3667.42 --> 3669.68]  important to us is helping people do
[3669.68 --> 3670.32]  it well.
[3670.56 --> 3672.40]  Build a code base that is easy to
[3672.40 --> 3674.66]  understand three, four, ten years
[3674.66 --> 3676.44]  down the road rather than having to
[3676.44 --> 3678.04]  replatform or reinvent things.
[3678.04 --> 3680.90]  I don't know if it's too right there
[3680.90 --> 3683.12]  or not, but it's something that I'm
[3683.12 --> 3684.56]  surprised that not everybody agrees
[3684.56 --> 3684.84]  with.
[3685.18 --> 3687.40]  So I thought I would just say it.
[3687.92 --> 3691.02]  I will see your unpopular opinion and
[3691.02 --> 3696.42]  raise you that the level of quality of
[3696.42 --> 3700.70]  a project should match its urgency to
[3700.70 --> 3701.36]  get to market.
[3703.50 --> 3705.20]  Yeah, I like that.
[3705.86 --> 3707.42]  It's a challenging thing sometimes,
[3707.42 --> 3709.30]  though, you know, it's obviously
[3709.30 --> 3711.08]  important to get somewhere fast, but if
[3711.08 --> 3712.94]  you get there fast and then have to
[3712.94 --> 3715.56]  backtrack or, I don't know, need a
[3715.56 --> 3717.00]  whole bunch more time to fix the
[3717.00 --> 3718.80]  things that got you there, it's
[3718.80 --> 3720.10]  difficult to see that it was worth the
[3720.10 --> 3720.36]  effort.
[3723.08 --> 3724.20]  Anyway, I mean, yeah.
[3724.62 --> 3726.54]  A lot of this strongly comes down to
[3726.54 --> 3729.12]  like, we've talked about this a million
[3729.12 --> 3730.48]  times, but like the size of your team
[3730.48 --> 3731.24]  and everything else.
[3731.50 --> 3734.10]  Because I know, like if I'm working on
[3734.10 --> 3735.80]  a project completely by myself, what I
[3735.80 --> 3737.42]  can get away with is drastically
[3737.42 --> 3738.94]  different, especially if I'm not open
[3738.94 --> 3739.64]  sourcing something.
[3740.14 --> 3741.62]  Because it's like, I'm the only person
[3741.62 --> 3743.20]  that sees this and if I need to rip this
[3743.20 --> 3745.04]  all out, nobody's going to give me any
[3745.04 --> 3745.62]  grief for it.
[3745.70 --> 3747.04]  And I already understand how it all
[3747.04 --> 3747.28]  works.
[3747.30 --> 3749.26]  So it's not like I have to figure out
[3749.26 --> 3750.68]  like, what does this hodgepodge of code
[3750.68 --> 3751.00]  do?
[3751.00 --> 3753.12]  But I definitely agree that if you're
[3753.12 --> 3754.82]  working with teams on projects, especially
[3754.82 --> 3757.06]  like with you guys, releasing a graphical
[3757.06 --> 3758.64]  user interface and like having other
[3758.64 --> 3761.80]  people use it, that is a very, very
[3761.80 --> 3763.06]  different beast to tackle.
[3763.46 --> 3765.52]  And when you're doing that, you can't
[3765.52 --> 3766.66]  have people using it and then all of a
[3766.66 --> 3768.52]  sudden say, all these APIs we had, we're
[3768.52 --> 3769.16]  ripping them all out.
[3769.22 --> 3769.54]  Good luck.
[3769.88 --> 3771.32]  Like if you want to migrate to version two,
[3771.40 --> 3772.64]  you basically just throw all your code
[3772.64 --> 3772.82]  out.
[3772.88 --> 3774.46]  Like that's not a realistic migration
[3774.46 --> 3774.96]  strategy.
[3775.84 --> 3777.34]  No, no, that's painful.
[3777.44 --> 3778.86]  And I mean, there's been a couple of
[3778.86 --> 3781.14]  famous situations, I suppose, with that
[3781.14 --> 3782.32]  over the last few years.
[3782.66 --> 3783.98]  It's difficult to say that it could have
[3783.98 --> 3785.38]  been done better, but you just have to
[3785.38 --> 3788.76]  think, well, you know, maybe a little bit
[3788.76 --> 3791.54]  less speed, a lot more thought and design
[3791.54 --> 3794.14]  into this could have been beneficial.
[3794.74 --> 3797.20]  It just occurred to me that the thing about
[3797.20 --> 3798.38]  team size is really interesting.
[3798.52 --> 3801.04]  One is maybe easy to not think about it so
[3801.04 --> 3803.94]  carefully when it's just you, but I find
[3803.94 --> 3808.70]  it to be helpful to think or actually do
[3808.70 --> 3812.04]  any new projects out in the open and
[3812.04 --> 3814.94]  think, would anybody who saw my code think
[3814.94 --> 3817.78]  I was doing a good job and imagine that
[3817.78 --> 3820.58]  the rest of the community is your code
[3820.58 --> 3821.50]  review peers.
[3822.16 --> 3823.48]  You know, they're probably never going to
[3823.48 --> 3826.04]  look at it, but I think it helps keep me
[3826.04 --> 3828.60]  honest, especially early days and a project
[3828.60 --> 3831.40]  like this one, it had huge ambitions and
[3831.40 --> 3833.58]  had to start somewhere and without the
[3833.58 --> 3836.06]  community as it started, it was helpful to
[3836.06 --> 3837.88]  think, wow, you know, if I was looking at
[3837.88 --> 3840.04]  this, I had no idea, would it make sense?
[3840.54 --> 3843.00]  So, yeah, I just pretended that the rest
[3843.00 --> 3844.36]  of the internet was reviewing my code.
[3845.74 --> 3847.08]  That's a lot of pressure to put yourself.
[3848.80 --> 3850.36]  I was going to say, I think you could write
[3850.36 --> 3851.66]  perfect code and the internet would still
[3851.66 --> 3855.08]  be brutal, but maybe I'm just too
[3855.08 --> 3855.64]  pessimistic.
[3855.90 --> 3856.34]  I don't know.
[3858.42 --> 3859.76]  Somebody somewhere is always going to have
[3859.76 --> 3860.12]  an issue.
[3860.12 --> 3861.16]  All right.
[3861.24 --> 3861.40]  Yeah.
[3861.56 --> 3863.12]  Andrew, thank you for joining us.
[3863.42 --> 3865.08]  Everybody, thanks for joining us for GoTime.
[3865.38 --> 3866.80]  Hopefully we'll get to cover the subject
[3866.80 --> 3868.38]  again in the future and we'll cover some
[3868.38 --> 3870.02]  other unusual use cases for Go.
[3870.40 --> 3872.24]  If you have any ideas or suggestions for,
[3872.30 --> 3873.84]  you know, weird ways that people are using
[3873.84 --> 3875.48]  Go, definitely reach out, get in touch with
[3875.48 --> 3875.70]  us.
[3876.22 --> 3877.20]  We'd love to hear about them.
[3877.20 --> 3883.24]  Thank you for listening to GoTime.
[3883.70 --> 3885.68]  Is there a gopher or aspiring gopher in
[3885.68 --> 3887.06]  your life who would benefit from listening
[3887.06 --> 3887.60]  to the show?
[3887.96 --> 3889.96]  We would truly appreciate a recommendation.
[3890.62 --> 3892.46]  Shoot them a quick email or a Slack message,
[3892.72 --> 3893.68]  put out a tweet, whatever.
[3894.20 --> 3896.14]  Get crazy, get up from your desk, walk
[3896.14 --> 3897.98]  across the room and tell them in Mead Space.
[3898.40 --> 3898.88]  Who knows?
[3898.98 --> 3900.34]  It might be a good conversation starter.
[3900.88 --> 3902.82]  This episode was hosted by John Calhoun and
[3902.82 --> 3903.42]  Johnny Borsico.
[3903.68 --> 3905.56]  Thanks to our special guest, Andy Williams.
[3905.56 --> 3907.78]  It was produced by me, Jared Santo, with
[3907.78 --> 3909.32]  music by the one and only Breakmaster
[3909.32 --> 3910.54]  Cylinder, What a Beat Freak.
[3910.76 --> 3911.94]  And we're brought to you by awesome
[3911.94 --> 3912.46]  sponsors.
[3912.60 --> 3913.16]  Support them.
[3913.28 --> 3913.98]  They support the show.
[3914.40 --> 3916.20]  You know Fastly, Linode, and Rolbar have
[3916.20 --> 3916.56]  our back.
[3916.86 --> 3918.84]  If you haven't yet, hit up our master feed
[3918.84 --> 3920.68]  because, hey, monoliths are back in
[3920.68 --> 3920.96]  style.
[3921.34 --> 3923.76]  It's all Changedog podcasts in one easy
[3923.76 --> 3924.24]  subscription.
[3924.72 --> 3926.24]  Get it for the price of a free donut.
[3926.84 --> 3927.72]  Thanks again for listening.
[3927.90 --> 3928.80]  We'll talk to you next week.
[3935.56 --> 3965.54]  We'll be right back.
[3965.56 --> 3995.54]  We'll be right back.

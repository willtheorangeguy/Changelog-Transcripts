[0.00 --> 3.00]  I am José Valim and you're listening to The Changelog.
[12.08 --> 15.64]  Welcome back everyone, this is The Changelog and I'm your host Adam Stachowiak.
[15.76 --> 17.46]  This is episode 194.
[18.06 --> 21.06]  It's a big show today, we got José Valim on the show.
[21.42 --> 24.50]  We learned about the early days of José's start as a programmer.
[24.94 --> 29.72]  José took us back to the beginning of Elixir and shared why Erling got him so excited.
[30.00 --> 33.54]  We broke down the features of the language, we talked about functional programming,
[33.68 --> 36.80]  we talked about concurrency, developing for multi-core systems,
[37.42 --> 43.52]  we talked about the Elixir community, the future of Phoenix, Ecto, and so much more.
[44.12 --> 50.68]  We had four awesome sponsors, TopTal, Rollbar, Linode, and Truesight Pulse.
[50.96 --> 54.96]  Our first sponsor of the show is our friends at TopTal,
[55.36 --> 59.12]  an exclusive network of top freelance software developers and designers.
[59.12 --> 64.98]  Top companies rely on TopTal freelancers every single day for their most mission-critical projects.
[65.54 --> 69.08]  At TopTal, you'll be part of a worldwide community of engineers and designers
[69.08 --> 73.40]  with the flexibility to travel, blog on the TopTal engineering blog,
[73.80 --> 78.56]  apply for open source grants, or for scholarship options for our fellow women developers out there.
[79.02 --> 81.94]  Lots of opportunity inside of TopTal for you.
[81.94 --> 86.60]  Head to TopTal.com, that's T-O-P-T-A-L.com to learn more,
[86.92 --> 93.32]  or email me at adam at changelaw.com if you'd prefer a personal introduction to our friends at TopTal.
[93.64 --> 94.96]  And now, on to the show.
[94.96 --> 104.40]  All right, everyone, we're here today talking about Elixir.
[104.72 --> 108.88]  And Jared, you know, we've wanted to have Jose on the show for so long.
[108.96 --> 110.56]  We had several issues come up.
[111.32 --> 117.00]  And Jose, I think you and I might have exchanged some sort of GitHub message way, way back in the day,
[117.08 --> 120.34]  trying to get you on the show when you were still working more so on Ruby.
[120.34 --> 120.82]  Yes, indeed.
[120.82 --> 122.60]  But it's been a long time coming, my friend.
[122.68 --> 124.34]  A lot happened in those...
[125.20 --> 130.42]  I don't remember when we talked, but when I look back,
[130.70 --> 135.40]  there are so many things that happened in the last five years, which is just crazy.
[136.94 --> 139.60]  And Jared, like any good show, it begins with an issue.
[139.68 --> 140.68]  So how did this one come about?
[141.26 --> 143.50]  Yeah, multiple issues, like you said, over the years.
[143.58 --> 146.48]  I think the last time around was like the end of 2014,
[146.48 --> 150.32]  and we couldn't quite schedule it out or line it up with Jose.
[150.48 --> 153.40]  But we had Chris McCord on the show to talk about Phoenix specifically,
[153.98 --> 155.00]  which was a great episode.
[155.16 --> 159.00]  If you're interested in that, check out 147, which was like last March.
[159.80 --> 162.06]  And that kind of counted for our Elixir show for a while.
[162.06 --> 167.76]  And then recently, in December, Jose, one of your counterparts there at Platformatech,
[167.90 --> 170.64]  George, help me with the name, Jose.
[171.26 --> 172.42]  George Guimaraes.
[172.42 --> 172.86]  Yes.
[173.32 --> 176.36]  So shout out to George for hollering again and saying,
[176.48 --> 179.92]  you know, we've had some big milestones in Elixir 1.2,
[180.72 --> 183.28]  or is it Ecto 1.2 and Elixir 1.1?
[183.34 --> 184.72]  I can't remember the exact version numbers.
[185.42 --> 187.04]  And it's time to get him on.
[187.56 --> 190.72]  And yeah, Elixir 1.2, Ecto 1.1.
[191.28 --> 192.54]  So thanks, George.
[192.68 --> 194.86]  And Jose, we're really happy to have you on the show.
[195.44 --> 195.72]  Thank you.
[195.76 --> 196.84]  I'm glad to be here as well.
[197.38 --> 199.92]  You had Chris back in March last year?
[200.46 --> 200.84]  Yes.
[201.28 --> 201.58]  Yes.
[201.58 --> 203.78]  Oh, so we have a lot to talk about.
[204.14 --> 206.50]  Yeah, a lot's changed in Phoenix as well, right?
[207.18 --> 207.64]  Yes.
[207.98 --> 211.62]  I think March, it was not even 1.0 yet.
[211.62 --> 217.60]  And I think March was when I was actually starting to contribute to Phoenix,
[218.04 --> 219.36]  or I had just started.
[220.40 --> 228.54]  And then we had like this great, let's say, sprint where Chris and I were working
[228.54 --> 229.84]  and we're improving things.
[230.44 --> 237.24]  And I think we got like the 1.0 about July, something like this, kind of middle of last
[237.24 --> 237.50]  year.
[238.00 --> 238.32]  Yeah.
[238.42 --> 239.80]  So we have a ton to catch up on.
[240.58 --> 243.18]  Adam and I are quite excited about both Elixir and Phoenix.
[243.28 --> 244.48]  So we have tons of questions for you.
[244.88 --> 249.30]  Jose, one thing we like to do kind of as an intro to the show is to get to know the people
[249.30 --> 253.66]  behind open source because we find that's super interesting and enlightening.
[253.66 --> 259.12]  So from the internet, you know, and from following you and your work, we know a little bit about
[259.12 --> 262.02]  you, which is that you're a Brazilian and you live in Poland.
[262.74 --> 264.98]  We know that you crank out a ton of open source stuff.
[265.94 --> 272.52]  You also seem to be, just from my experience online, like a super nice and a positive person.
[272.52 --> 277.66]  But we don't know very much about beyond that, really, of your background and how you came
[277.66 --> 279.40]  to be where you are.
[279.56 --> 282.68]  So we love to hear developer origin stories on the show.
[283.42 --> 287.92]  And so if you're willing, we'd like to hear kind of your origin story, where things began
[287.92 --> 291.74]  for you in software, and then how did you get where you are today?
[292.92 --> 293.78]  Oh, okay.
[293.78 --> 293.82]  Okay.
[294.60 --> 302.94]  So I would say things like my first real contact with software was at university.
[303.82 --> 310.58]  I went to do, so I grew up in the center of Brazil in a small city called Inunas, and
[310.58 --> 316.06]  I moved to Sao Paulo, which is, you know, big city and everything for studies to do my
[316.06 --> 321.62]  university in, which ended up being automation and control engineering, which I don't use for
[321.62 --> 322.54]  anything, but anyway.
[324.06 --> 329.32]  And the first year I had C programming, and that's how I started with programming.
[329.58 --> 336.96]  And I have very good, and I have very good memories from those classes, because I remember,
[337.20 --> 341.58]  you know, you would, the professor would program in the whiteboard, which is a little bit weird,
[341.58 --> 347.46]  but he would say, now you need to declare this variable, like int, the variable name.
[348.02 --> 349.84]  And he would say, you need to do this.
[349.84 --> 356.94]  And then every time he said, like, you need to, or you must do this, I would ask, why?
[357.40 --> 359.62]  What would happen if you don't?
[360.12 --> 367.76]  And, and he, he, he was like very, he was a little bit peculiar with the professor, but
[367.76 --> 370.30]  he would always like entertain my questions.
[370.48 --> 374.12]  But at some point he got like, he couldn't take it anymore.
[374.28 --> 376.46]  And then he like, why do you want to do it?
[376.50 --> 377.06]  You're softer.
[377.06 --> 379.16]  Like you need to follow those rules.
[379.70 --> 379.86]  Yeah.
[380.62 --> 382.08]  Why are the rules in place, man?
[382.14 --> 382.54]  Tell me.
[383.06 --> 383.70]  Yeah, exactly.
[383.80 --> 384.02]  Right.
[384.08 --> 386.56]  I just, I just wanted to know what was going to happen.
[386.72 --> 391.12]  And, and, and, you know, and, but he, he said that like, it was also interesting because
[391.12 --> 395.04]  you would say like, oh, the, the variables would need to be initialized.
[395.12 --> 395.46]  Right.
[395.46 --> 401.34]  But you see, if you don't initialize, something is going to happen.
[401.38 --> 403.00]  It's just going to have whatever is in memory.
[403.00 --> 409.82]  And those weird questions actually made his, made him like tell this stuff as well.
[410.12 --> 410.36]  Right.
[410.36 --> 412.98]  Like what are, what are the consequences if you don't do something?
[412.98 --> 414.78]  So I think we could learn.
[415.04 --> 422.02]  And hopefully I was not just the annoying person in the classroom getting in the way of teaching.
[422.66 --> 426.86]  But that was, that was pretty much like my, my first contact with it.
[426.86 --> 432.14]  And, um, then it's still in the first year of university.
[432.54 --> 435.48]  I've, I, me and a couple of friends, we, we had a band.
[435.58 --> 436.86]  It was an acoustic band.
[437.58 --> 445.14]  And one of the, the, the players of the band with me, uh, is Hugo Barahuna, which is a co-founder
[445.14 --> 446.76]  of Platform Attack with me.
[446.76 --> 451.30]  So we, we had like a lot of story together that started exactly in the first year of university
[451.30 --> 458.42]  and we had a band and I decided to make the website, uh, for our band using flash and
[458.42 --> 459.22]  action script.
[459.46 --> 459.60]  Nice.
[459.68 --> 464.28]  So this is like the first time I was like, Hey, I'm going to learn things for myself and
[464.28 --> 465.88]  I'm going to try to make this work.
[466.30 --> 471.54]  And I was doing it out of, you know, it was not because I had classes, even before I enjoyed
[471.54 --> 476.32]  like the, the, the C classes, I was actually doing this because I wanted and I wanted to
[476.32 --> 476.60]  learn.
[476.60 --> 481.64]  And, um, and that went pretty much, uh, like that.
[481.80 --> 487.38]  I also remember that at some point I went from, I started learning more about databases,
[487.90 --> 491.60]  uh, you know, MySQL probably at the time.
[491.60 --> 498.28]  And then I ended up going to do PHP and, and MySQL.
[498.60 --> 500.78]  It was a very short period of time.
[500.88 --> 502.80]  I did a couple of projects as a freelancer.
[502.80 --> 508.60]  Um, I remember like a couple, a couple of interesting stories as well, because we were
[508.60 --> 509.24]  still in the band.
[509.30 --> 511.64]  I was always very passionate with music.
[511.84 --> 518.00]  I remember that at some point when I was to university, I went looking for like a music
[518.00 --> 522.78]  school, like, uh, I don't know if it's conservatorium in English or how you say that.
[523.42 --> 528.56]  And, uh, I remember that I was checking on the internet, which ones had really horrible
[528.56 --> 534.46]  websites and I called them and I was saying like, Hey, if you give me like, uh, classes
[534.46 --> 539.46]  on singing or guitar, I'm going to do a new website for you.
[539.52 --> 542.84]  Like if you give me six months of classes, I'm going to do a new website for you.
[542.90 --> 544.88]  So that's something that happened at the time.
[545.08 --> 545.34]  That work?
[545.98 --> 546.40]  Worked.
[546.42 --> 546.82]  It worked.
[546.90 --> 549.34]  I got, I got my six months of singing classes.
[549.54 --> 549.82]  Yes.
[549.82 --> 553.38]  So you're, you're basically trading websites for educations.
[554.10 --> 554.54]  Oh, sorry.
[555.32 --> 559.32]  So you're basically trading website work for an education and, and singing.
[560.14 --> 561.14]  Yes, exactly.
[561.50 --> 563.98]  Uh, I couldn't afford to sing classes at a conservator.
[564.10 --> 565.28]  Those are usually really good.
[565.80 --> 570.50]  Uh, but so, you know, that was a plan that worked and they're like, well, we would really
[570.50 --> 571.50]  appreciate a new website.
[571.78 --> 574.40]  So, um, yeah.
[574.64 --> 579.40]  So, you know, so it was pretty much that nothing serious, just doing things on the side, even
[579.40 --> 583.54]  because the engineering university was, you know, required a lot of time.
[584.08 --> 586.48]  And it was at the end of 2006.
[586.94 --> 593.04]  I had, uh, we were a couple of friends and, uh, and that was when I actually met George
[593.04 --> 594.60]  that got us here on the show.
[594.66 --> 596.98]  It was about 2006 that we got closer.
[597.30 --> 603.14]  And then we had some ideas for startups and, uh, rails was already, you know, a lot of people
[603.14 --> 605.26]  were talking about trails and I decided to try it out.
[605.40 --> 607.82]  And that's when I got started with rails.
[607.82 --> 610.42]  And, uh, yeah.
[610.50 --> 614.28]  And then a lot more happened, uh, regarding that.
[614.34 --> 616.82]  I was, I was doing rails for quite some time.
[617.60 --> 624.28]  And, uh, at the end of my university, they have a, an agreement between, um, so at that
[624.28 --> 629.80]  point I was still in Brazil, but, uh, the university had an engineering, the engineering school had
[629.80 --> 635.52]  an agreement where I could go on and do my last year university in another country.
[635.98 --> 637.76]  And that's when I moved to Italy.
[637.86 --> 639.92]  And that's when I left Brazil.
[640.14 --> 644.48]  And it was really funny because when I left, I was like, the whole course was like, uh,
[644.48 --> 648.06]  two years, uh, that I, what I had to finish.
[648.06 --> 650.12]  And then I was thinking, well, you know what?
[650.12 --> 653.24]  I'm just going to go stay there six months and then come back.
[653.36 --> 655.20]  I'm not even going to do the whole two years.
[655.42 --> 657.14]  And then I never came back.
[657.78 --> 658.50]  I'm still here.
[659.28 --> 662.00]  Um, yeah, but that's how I went abroad.
[662.30 --> 667.42]  And that's kind of what explains how someone from Brazil is living in Poland.
[667.42 --> 669.20]  I met my wife, my wife's Polish.
[669.42 --> 670.50]  And now I live here.
[670.58 --> 672.42]  I'm living here in Poland for five years.
[673.10 --> 676.66]  I was going to, I was going to ask what kept you in Poland, but then you told us you,
[676.66 --> 678.72]  you found a wife and, uh, settled down.
[678.92 --> 678.94]  So.
[679.02 --> 679.38]  Good reasons.
[679.88 --> 680.74]  Congrats on that.
[681.32 --> 681.90]  Yes, exactly.
[682.12 --> 682.54]  Thank you.
[683.40 --> 688.80]  So you mentioned you were doing rails work and, uh, many people, I think probably in our
[688.80 --> 694.04]  audience who know you and may not yet know you, uh, uh, with regard to Elixir probably
[694.04 --> 701.04]  know you with regard to the, the rails work that you did, which started off as, um, device,
[701.32 --> 701.54]  right?
[701.54 --> 706.40]  Or maybe that's not the starting point, but that was the, the, the gem that you and your
[706.40 --> 711.08]  team at platform tech built that became kind of one of the de facto, you know, authentication
[711.08 --> 714.48]  tools that people use on rails, even to this day.
[715.30 --> 720.10]  Um, can you tell us about that, you know, kind of that section in your, in your software
[720.10 --> 724.74]  career with regard to devise and working with Ruby and then eventually on the rails
[724.74 --> 725.18]  core team?
[726.64 --> 726.78]  Sure.
[727.00 --> 731.42]  So, uh, yeah, it was a little bit before that and it's, there is a very nice
[731.42 --> 738.80]  story here because, uh, I remember my first open source contribution, which we had, this
[738.80 --> 740.28]  was probably back 2006, 2007.
[740.28 --> 748.38]  And, uh, I sent, we had a, uh, plugin, uh, called, uh, upload column, if I remember correctly,
[749.14 --> 750.32]  uh, for Aos.
[750.32 --> 757.38]  And, uh, and I remember sending a patch, uh, by email to the altar, like, Hey, what if we
[757.38 --> 758.14]  did those changes?
[758.70 --> 765.04]  And, uh, it's really nice because I, I later, you know, uh, the outer, uh, the, the owner
[765.04 --> 767.38]  of that package, uh, is Jonas Nicholas.
[767.76 --> 769.68]  And, you know, he went to write Capybara.
[769.68 --> 775.16]  He, he wrote, uh, Carrowave and the new refile, uh, plugin for Rails.
[775.70 --> 782.82]  And, uh, and this was goes like way back and probably 2006, 2007, like we were exchanging
[782.82 --> 784.16]  these emails, we were exchanging patches.
[784.44 --> 788.50]  And it's nice because, uh, recently he started coding with Elixir as well.
[788.94 --> 792.12]  So, uh, that's a fun side story.
[792.12 --> 798.16]  But that's, that's like what I remember as like my, my first, my first like dabbling
[798.16 --> 798.82]  at open source.
[799.68 --> 805.14]  And, um, a couple of years later, I think it was like 2008, 2009, I actually created something
[805.14 --> 810.04]  called inherited resources, which was, I don't know if you ever got to use it.
[810.14 --> 816.72]  Uh, but it was the first thing that, uh, started that I, that I've, that I've written myself
[816.72 --> 819.18]  and started to gain some like attention.
[819.18 --> 825.36]  Um, I also, I don't remember for those who are doing, uh, Rails for a long time as well.
[825.40 --> 829.60]  I don't remember the time, but we also had something called Rails footnotes, which was
[829.60 --> 834.10]  a plugin that you had to, you could install in Rails application and it would add a bunch
[834.10 --> 839.12]  of footnotes at, uh, at the bottom saying, showing like what was the request parameters,
[839.32 --> 840.32]  what was in the logs.
[840.52 --> 842.44]  So it gave access to a lot of information.
[842.60 --> 846.10]  It would show like which queries ran and how, how much time it took.
[846.28 --> 847.86]  And I also contributed to that.
[847.86 --> 854.94]  But the first one was, uh, exactly inherited resources and we've inherited resources.
[854.94 --> 862.08]  So this, if I remember correctly, it was 2009 and we had, uh, the Google storm of code happening.
[862.84 --> 868.40]  And, and this was when a Rails tool was starting to become Rails 3, right?
[868.46 --> 870.76]  The work towards Rails 3 had already started.
[870.76 --> 877.88]  And, um, and Google storm of code was happening and I was still a student at the time.
[878.12 --> 882.62]  So I wrote a proposal for the new generator system, which I still think is the generator
[882.62 --> 884.26]  system using today in Rails.
[884.46 --> 889.18]  And the whole idea of the proposal was, you know, Rails 3 is meant to be agnostic and everything,
[889.32 --> 889.44]  right?
[889.44 --> 892.16]  Like you can bring your own RIM layer.
[892.16 --> 895.62]  You can bring your own, your own like, uh, test framework.
[896.38 --> 900.72]  But then I said, like, we cannot really say that Rails is going to be agnostic.
[900.92 --> 906.22]  If the generators, they are still going to generate only active record stuff, right?
[906.26 --> 912.80]  Like, uh, at Rails 2, if you're using RSpec, you need to use like RSpec scaffold, RSpec model.
[912.80 --> 914.98]  They, they could not play together.
[915.32 --> 922.18]  So I wrote this Google storm of code proposal, um, and for the new generator system.
[922.18 --> 923.06]  And it was accepted.
[923.58 --> 925.78]  Uh, I worked with YehudaCat on that.
[925.84 --> 926.54]  He was my mentor.
[926.84 --> 932.62]  And that's how I started to, it was a really great opportunity because, um, you know,
[932.92 --> 936.12]  contributions on GitHub was not that easy at the time.
[936.16 --> 938.26]  Like how the, it was new still.
[938.26 --> 943.98]  So it was hard for you to be really in touch, you know, like with the people actually building
[943.98 --> 944.74]  the software.
[945.04 --> 947.24]  And it was really hard because I got really close to Yehuda.
[947.36 --> 948.34]  We became good friends.
[949.18 --> 952.84]  And, uh, and that's how I got like my first big contributions to Rails.
[953.84 --> 959.86]  And, and then, you know, uh, I started contributing more and more, eventually became part of the,
[959.86 --> 960.74]  the Rails core team.
[961.00 --> 966.62]  It was also at the time that we started Devise and Devise, uh, it, it was started as part of
[966.62 --> 967.38]  Plot and Formatech.
[967.38 --> 973.40]  We hired at the time, our first person we were, uh, in 2009, the company had just started.
[973.52 --> 977.04]  So we were four, the four founders and we hired Carlos Antonio.
[977.80 --> 982.44]  And, and the, one of the reasons we hired him was exactly because of his other contributions
[982.44 --> 984.24]  to other open source projects.
[984.38 --> 987.08]  And he started working on Devise and working together.
[987.38 --> 994.28]  I was kind of more of doing a mentorship role and those initial days, but then Devise grew
[994.28 --> 994.50]  up.
[994.50 --> 1002.30]  A lot of people started using it and, uh, it's, it's our biggest, um, you know, open source
[1002.30 --> 1005.86]  project for, for, for the Rails community in particular.
[1005.96 --> 1008.50]  And we have other ones like Simple Form and so on.
[1009.22 --> 1009.30]  Yeah.
[1009.34 --> 1011.30]  I actually had forgotten about inherited resources.
[1011.64 --> 1012.56]  I recall it now.
[1012.56 --> 1017.42]  Uh, and, and, and, and as you spoke about it, it kind of reminded me of what you were mentioning,
[1017.42 --> 1022.86]  um, back with your professor in college asking why, because correct me if I'm wrong, wasn't
[1022.86 --> 1028.58]  the purpose of inherited resources was to really dry up the controllers quite a bit inside Rails
[1028.58 --> 1034.34]  and remove a lot of the, the kind of the boilerplate, which is scaffolded out, um, in a typical
[1034.34 --> 1035.20]  Rails controller.
[1035.20 --> 1040.60]  And it just seems like that was you basically asking why with regards to how we do controllers
[1040.60 --> 1043.64]  in Rails and kind of your answer to a different way of doing that.
[1043.64 --> 1044.86]  Yeah.
[1044.86 --> 1049.00]  So the, the whole idea is that you would inherit from inherited resource space or something
[1049.00 --> 1049.54]  like that.
[1049.54 --> 1049.98]  Right.
[1049.98 --> 1056.10]  And it would bring the whole, the whole, you know, it would have a default implementation
[1056.10 --> 1058.48]  that does everything the Rails couple is supposed to do.
[1058.48 --> 1065.06]  And this is usually too, like what your controller typically does is that, you know, you need
[1065.06 --> 1070.24]  to have like the, the query part where you need to say, you know, if I want to get the,
[1070.24 --> 1076.70]  the current, the current manager for this project inside this company, you need to build the
[1076.70 --> 1077.36]  query, right.
[1077.54 --> 1079.32]  And often using things from session.
[1079.42 --> 1080.34]  So that was one thing.
[1080.42 --> 1082.70]  The other one is how to render those resources.
[1083.56 --> 1086.70]  And that's kind of what was in there together.
[1086.70 --> 1091.08]  And eventually, you know, at this point, if you go to the inherited resource project,
[1091.18 --> 1093.00]  they're going to say, Hey, don't use this.
[1093.08 --> 1094.04]  We don't montate this anymore.
[1094.14 --> 1095.58]  We don't recommend people to use it.
[1095.66 --> 1096.06]  Exactly.
[1096.14 --> 1097.72]  Because it just hides too much.
[1098.68 --> 1103.74]  We, we, you know, we, we, if, if at some point you say like, ah, there's scaffolding
[1103.74 --> 1104.00]  rails.
[1104.10 --> 1105.10]  There's a lot of baller plate.
[1105.48 --> 1106.88]  And the inherited resources has none.
[1107.16 --> 1109.06]  We had to find a balance somewhere.
[1109.42 --> 1113.64]  And inherited resource was too much to the extreme, to the point you would look at our controller
[1113.64 --> 1115.36]  and you're not really sure what it is doing.
[1115.36 --> 1121.08]  Or you would have to, or you would surmise like one of, of 20 callbacks.
[1121.08 --> 1125.16]  And then you actually have not a lot of confidence of how that works.
[1126.42 --> 1128.08]  Yeah, that's, that's actually my exact experience.
[1128.36 --> 1130.06]  I had one situation with it.
[1130.14 --> 1132.94]  I actually inherited a project that used it, used it.
[1133.36 --> 1137.76]  And it took me a really long time just to figure out what was going on because, you
[1137.76 --> 1139.64]  know, like where was all this activity coming from?
[1139.64 --> 1142.70]  And then once I, once I realized it, it started to make more sense.
[1142.82 --> 1145.16]  But again, like you said, it's funny.
[1145.24 --> 1147.60]  Like the question is why, why are we doing this boilerplate?
[1147.70 --> 1152.76]  And it's a super useful experiment to like, let's, let's see if we can just dry this up
[1152.76 --> 1153.64]  and not have to do it.
[1154.14 --> 1158.18]  And then over time you learn, well, it's also helpful for it to be obvious what's going
[1158.18 --> 1158.46]  on.
[1158.46 --> 1160.96]  And so you're, you're hiding a lot under the covers there.
[1162.30 --> 1164.12]  So yeah, interesting stuff.
[1164.30 --> 1167.82]  And so Devise came later and was, like you said, part of Plataforma Tech.
[1168.20 --> 1172.72]  We're going to go to a break here real quick, but can you just give us a real quick synopsis
[1172.72 --> 1174.66]  of, of your company, Plataforma Tech?
[1174.76 --> 1178.58]  You said you founded it with four other people and its purpose and kind of how it plays into
[1178.58 --> 1179.12]  open source.
[1179.92 --> 1180.06]  Sure.
[1180.24 --> 1183.60]  So Plataforma Tech, we are a consultancy based in Brazil.
[1183.60 --> 1192.22]  I said like 2009, we were, we were four, but now we are about 40 developers and we, we
[1192.22 --> 1199.36]  work with both, you know, well-established startups and big companies, Fortune 500, for
[1199.36 --> 1199.70]  example.
[1199.90 --> 1203.74]  And what we're really good at is to go there.
[1203.74 --> 1209.36]  And if you're having hard problems to solve, right, we come in and you're trying to make
[1209.36 --> 1213.16]  your whole process around the software development more efficient.
[1213.60 --> 1223.72]  And, uh, the relation with open source was exactly when we started, um, was, I was, I
[1223.72 --> 1224.56]  was doing open source.
[1224.76 --> 1228.74]  So, you know, we started us four and for a while we didn't have any clients.
[1228.74 --> 1233.04]  So I had a lot of free time and that's when I wrote Inherited Resources.
[1233.04 --> 1239.08]  And we, what happened at the time is that we started to get a lot of clients because of
[1239.08 --> 1240.50]  our open source work.
[1241.04 --> 1246.56]  So we knew it, we knew at that point, like, Hey, investing in open source besides, you know,
[1246.60 --> 1248.40]  it also helps us to grow the company.
[1248.40 --> 1252.74]  And as I said, the first person we hired was also because of the open source contribution.
[1252.74 --> 1255.16]  So it's not, we can get clients, right?
[1255.16 --> 1259.24]  We can also, it helped us to attract a good talent.
[1260.12 --> 1265.16]  And, uh, that's how it, you know, was our relationship with open source.
[1265.48 --> 1269.58]  But, and it changed a lot with Elixir.
[1269.72 --> 1274.72]  I would, I would think because with Elixir, it was when we decided to make a huge bet, right?
[1274.72 --> 1276.58]  When you say like, Hey, I want to invest in the language.
[1276.74 --> 1281.32]  We are no longer talking about, you know, making a small project, uh, for the community.
[1281.32 --> 1287.20]  You're, you're talking about, you know, investing on something for a long period of time that
[1287.20 --> 1292.60]  has also a higher risks because you can invest for like three years and nobody uses it.
[1292.60 --> 1292.86]  Right.
[1293.00 --> 1295.88]  So what, what's going to become of that?
[1296.46 --> 1299.52]  We did a great job there, teeing up the next segment of the show, Jose.
[1299.52 --> 1304.12]  We, uh, and we obviously want to dive deep into that, uh, that big bet you mentioned,
[1304.20 --> 1304.76]  which is Elixir.
[1304.92 --> 1310.10]  So we're going to take a break, uh, you know, great learning about your origin and all that.
[1310.10 --> 1315.96]  I guess it will definitely dovetail quite deeply into your passion for multi-core and Elixir.
[1316.08 --> 1316.82]  So let's take that break.
[1317.08 --> 1318.44]  We'll dive deep when we come back.
[1319.40 --> 1322.50]  I'm excited to tell you about a new sponsor of ours, Rollbar.
[1322.84 --> 1327.70]  One of the most frustrating things about being a software developer is dealing with errors,
[1328.10 --> 1332.96]  relying on users to report your errors, digging through log files, trying to debug issues,
[1333.12 --> 1337.24]  or a million alerts, flooding your inbox and ruining your day.
[1337.24 --> 1343.90]  With Rollbar's full stack error monitoring, you get the context, the insights and control
[1343.90 --> 1347.66]  you need to find and fix bugs faster with a lot less noise.
[1348.48 --> 1349.96]  Rollbar is easy to install.
[1350.08 --> 1354.06]  You can start tracking your production errors and deployments in eight minutes or less.
[1354.58 --> 1360.42]  And Rollbar works with all major languages and frameworks, including Ruby, Python, JavaScript,
[1360.42 --> 1364.76]  PHP, Node, iOS, Android, Elixir, and more.
[1365.42 --> 1367.68]  Integrate Rollbar into your existing workflow.
[1368.20 --> 1373.60]  Send error alerts to Slack or HipChat or automatically create new issues in GitHub,
[1374.00 --> 1376.62]  Jira, Asana, Pivotal Tracker.
[1377.26 --> 1379.82]  And we have a special offer just for you, our listeners.
[1380.38 --> 1382.56]  Go to rollbar.com slash changelog.
[1382.96 --> 1385.84]  Sign up and get the bootstrap plan free for 90 days.
[1385.84 --> 1389.56]  That's basically 300,000 errors tracked for you.
[1389.98 --> 1390.66]  Totally free.
[1391.58 --> 1397.78]  Rollbar is loved by developers at awesome companies like Heroku, Twilio, Kayak, Instacart,
[1397.94 --> 1400.14]  Zendesk, Twitch, and more.
[1400.62 --> 1402.18]  Give Rollbar a try today.
[1402.68 --> 1406.04]  Head over to rollbar.com slash changelog.
[1409.58 --> 1411.36]  All right, we're back from our break.
[1411.36 --> 1416.52]  We got Jose Valim here, long time in the making this show, as many shows, Jared.
[1416.96 --> 1417.08]  Yep.
[1417.18 --> 1420.38]  It came from an issue, but it goes much deeper for you, Jose.
[1420.58 --> 1426.92]  You came from Ruby Roots and you came from roots where you kind of got, I don't want to
[1426.92 --> 1430.70]  put words in your mouth, but it seemed like you kind of got bummed about the lack of multi-core
[1430.70 --> 1434.90]  systems and concurrency and all these other things that other languages bring.
[1435.22 --> 1437.48]  And obviously we've got Elixir now.
[1437.72 --> 1439.60]  So maybe let's begin with that.
[1439.60 --> 1443.72]  Tell us a story about how it began for you and Elixir.
[1443.86 --> 1444.74]  Where were you at with Rails?
[1444.82 --> 1445.64]  Where were you at with Ruby?
[1446.18 --> 1452.14]  And what kind of sparked this interest of multi-core concurrency and ultimately Elixir?
[1452.96 --> 1460.36]  Yeah, that's a great question because I was working with Rails and I was one of the ones
[1460.36 --> 1464.66]  responsible, not responsible, but working with making Rails thread safe.
[1464.66 --> 1468.94]  And it was really, really hard, you know.
[1468.94 --> 1474.36]  And we worked a lot on making or improving Rails.
[1474.36 --> 1482.02]  So if you go back in time, like Rails 2.3 said that Rails was finally thread safe, but it
[1482.02 --> 1485.44]  was thread safe by putting a huge lock around your application, right?
[1485.48 --> 1489.20]  Which is not what you want because you're not going to leverage concurrency.
[1489.36 --> 1492.12]  And then we wanted to improve this more and more of time.
[1492.22 --> 1493.10]  It was a lot of work.
[1493.10 --> 1497.88]  And then when you thought like, hey, I can finally make this work, then you realize that
[1497.88 --> 1503.52]  it doesn't work on JRuby or Rubinus because they give you different guarantees regarding
[1503.52 --> 1505.16]  thread safety.
[1505.94 --> 1509.74]  So, you know, it was really frustrating work.
[1509.86 --> 1510.08]  It was.
[1510.08 --> 1516.10]  And as you know, like if you're using threads and motaxes and so on, and you have a lot
[1516.10 --> 1521.78]  of state around, which is what we have in our regular Rails applications, sometimes you
[1521.78 --> 1524.70]  don't know that there is a race condition or there is a concurrency bug in there.
[1524.94 --> 1529.64]  It's just when you're running in production under certain scenarios or in particular some
[1529.64 --> 1533.54]  high loads, right, that those issues, they are going to show up.
[1533.68 --> 1538.34]  And then they are even harder to debug and try to give a guarantee to say for sure, hey,
[1538.40 --> 1539.22]  this is thread safe.
[1539.22 --> 1541.04]  So I was working with that.
[1541.18 --> 1546.48]  And then what came to my mind was that, you know, I was already hearing this was, I think,
[1546.58 --> 1547.80]  2010.
[1548.66 --> 1552.38]  I was already hearing like, you know, concurrency is becoming even more important.
[1552.50 --> 1554.32]  That's why we want to try to save in the first place, right?
[1554.32 --> 1557.90]  So we could get our Rails application, put it in a server in production.
[1558.12 --> 1563.08]  And if it had like four cores, it would use all the four cores efficiently without needing
[1563.08 --> 1565.88]  to restart four instances, for example.
[1566.24 --> 1567.32]  So I knew that.
[1567.32 --> 1568.50]  I knew it was becoming important.
[1568.64 --> 1572.52]  But I said, you know, like, if this is going to be the future, right, if the future is going
[1572.52 --> 1585.52]  to have like eight cores, 32 cores or 128 cores, we needed to have better abstractions because
[1585.52 --> 1589.22]  the ones I had working with Ruby and Rails, they are not going to cut it.
[1589.22 --> 1594.48]  So I decided to study other languages and see what they are doing.
[1594.60 --> 1599.20]  And the idea was exactly to kind of see what is happening there and try to bring it into
[1599.20 --> 1602.10]  Ruby and into Rails.
[1602.10 --> 1608.88]  And I did, I spent a good period of time studying other languages and so on.
[1609.18 --> 1611.70]  But the one I really, really loved was Erlang.
[1612.72 --> 1620.38]  And the reason why I really liked Erlang, as not only the language, but also the whole
[1620.38 --> 1625.94]  virtual machine was exactly because to me, they were no longer, they were not doing the
[1625.94 --> 1626.54]  concurrency.
[1626.54 --> 1628.06]  They're not worried about concurrency.
[1628.38 --> 1631.14]  They're actually worried about distribution, right?
[1631.18 --> 1634.34]  You're not writing software and they're saying, oh, I want to make this software concurrent.
[1634.50 --> 1638.06]  You're saying, hey, I'm writing this software and this software can be distributed, which
[1638.06 --> 1640.76]  means it can run on multiple machines, right?
[1640.92 --> 1647.40]  It just happens that, you know, our model, when you're running on multiple machines, it
[1647.40 --> 1650.54]  can also happen that you can run everything in the same machine and you get concurrency for
[1650.54 --> 1650.78]  free.
[1650.78 --> 1656.66]  So I'll expand a little bit on that, which is, so when you're writing software in Erlang
[1656.66 --> 1662.20]  and now today in Elixir, all of our code, it runs inside the processes.
[1663.54 --> 1666.72]  And the Erlang virtual machine is like, it's 30 years old.
[1666.88 --> 1669.22]  It has been there for a while.
[1669.50 --> 1674.40]  And when they were writing it, they were not worried about concurrency, the multi-core
[1674.40 --> 1677.58]  concurrency at the time, because you didn't have multi-cores at the time.
[1677.58 --> 1682.84]  But so when you're writing Elixir code, you have your code running in processes, right?
[1682.92 --> 1685.14]  And those processes, they're not operating system processes.
[1685.68 --> 1688.24]  They are very lightweight threads of execution.
[1688.36 --> 1689.06]  They are very cheap.
[1689.14 --> 1691.62]  You can create literally millions of those.
[1692.50 --> 1699.10]  And it was everything done in a way where, you know, I can have a process running this
[1699.10 --> 1699.40]  machine.
[1699.50 --> 1701.62]  I can have a process running on another machine.
[1701.62 --> 1705.78]  And as long as those machines are connected as part of our closer, they can exchange messages
[1705.78 --> 1708.94]  between them and all those processes they're running at the same time.
[1709.28 --> 1710.84]  And that's what they built at the time.
[1710.96 --> 1716.14]  And then when they needed concurrency, they just realized that concurrency is the special
[1716.14 --> 1721.24]  case where you have all those processes, but instead of them running in different machines,
[1721.44 --> 1722.92]  they're only running the same machine.
[1723.04 --> 1727.24]  So you just, you can get a little bit extra guarantees for that, but it's really a special
[1727.24 --> 1728.68]  case for the model.
[1728.80 --> 1729.42]  They have that.
[1729.42 --> 1732.12]  And when I saw that, I found it beautiful, right?
[1732.22 --> 1738.40]  Because if you think like we as a software, you know, the industry is changing, right?
[1739.28 --> 1743.96]  Now we are hearing more and more languages oriented towards concurrency.
[1744.36 --> 1748.28]  It may get at some point that we're going to hear more and more languages that are oriented
[1748.28 --> 1749.28]  towards distribution.
[1750.02 --> 1751.28]  And Erlang is already there.
[1751.36 --> 1753.28]  It has been there for 30 years, right?
[1753.60 --> 1755.50]  So that was really fascinating to me.
[1755.50 --> 1760.02]  And I was like, you know, if I want to write software in the future, I want to write software
[1760.02 --> 1762.02]  that's going to run on this virtual machine.
[1763.04 --> 1768.16]  And that's what got me excited and led me down this path.
[1769.12 --> 1773.84]  So just to give us some context, what year was this when you were formulating, you were
[1773.84 --> 1775.52]  conceiving the idea of Elixir?
[1775.78 --> 1776.68]  Give us a time period.
[1777.10 --> 1781.88]  This was 2010 and the beginning of 2011.
[1781.88 --> 1788.10]  So the first commit to Elixir was like January of 2011.
[1789.16 --> 1791.32]  And it was the time I started.
[1791.48 --> 1793.72]  So after that, I started writing more and more Erlang.
[1794.36 --> 1798.56]  But there were a couple of things that I really feel like it was missing the language.
[1798.74 --> 1803.36]  The way I like to sum it up is that I liked everything I saw, but I hated the things I
[1803.36 --> 1803.74]  didn't see.
[1803.86 --> 1807.16]  I wanted, for example, really good Unicode support.
[1807.16 --> 1814.58]  I wanted good abstractions for working with collection, things that I was used to, right?
[1814.76 --> 1817.20]  And I could not really give up on them.
[1818.16 --> 1820.22]  So after, yeah, go ahead.
[1820.54 --> 1825.98]  I was just going to say, it sounds like, you know, the programmer happiness angle that Matt
[1825.98 --> 1829.58]  took with Ruby, you know, it spoils you when you get used to it.
[1829.58 --> 1831.80]  I know I'm spoiled in many ways by it.
[1832.12 --> 1834.50]  And I look for those features everywhere else I go.
[1835.16 --> 1840.80]  And I judge other languages in terms of semantics and syntax with regard to how I can express
[1840.80 --> 1841.38]  myself.
[1842.14 --> 1844.92]  And it sounds like you're hitting that same thing where like everything you saw about
[1844.92 --> 1850.60]  Erlang, the foundations, the distribution model, all these things were great and you
[1850.60 --> 1851.08]  loved it.
[1851.18 --> 1855.36]  But there was just missing pieces that you just didn't feel like you could live without.
[1855.88 --> 1858.38]  Because if you could have lived without them, you could have just kept writing more Erlang,
[1858.38 --> 1858.68]  right?
[1859.14 --> 1863.40]  But you decided, no, I'm going to actually start something new that's going to be kind
[1863.40 --> 1864.66]  of a melding of these two worlds.
[1864.72 --> 1865.34]  Is that fair to say?
[1866.18 --> 1866.48]  Yes.
[1866.70 --> 1873.56]  That was kind of the, it was not the idea at the time, but it's what it came to be.
[1873.88 --> 1877.96]  So at the beginning, so like I see the first commit was January of 2011.
[1878.88 --> 1888.26]  And so I knew what I was missing, but I was not sure what I wanted, if that makes sense.
[1888.26 --> 1895.18]  So for example, I was like, oh, I want better support for collections or I wanted a way
[1895.18 --> 1896.28]  to do polymorphies.
[1896.78 --> 1901.90]  So the first, if you go like to the early commits of Alexer, to the early history, it
[1901.90 --> 1903.48]  was actually an object-oriented language.
[1903.98 --> 1906.42]  It had a prototype-based model.
[1906.42 --> 1910.14]  And, but everything in Erlang virtual machine is immutable.
[1910.14 --> 1911.90]  So I was trying those things.
[1912.14 --> 1917.10]  So I know I had a problem and I wanted to solve it, but the answers I had at the time,
[1917.46 --> 1920.90]  they were very Ruby-centric, let's say.
[1920.90 --> 1924.96]  So it was more guided, biased towards object-orientation.
[1925.22 --> 1927.74]  And however, Ruby was solving those particular problems.
[1928.54 --> 1934.88]  So for example, metaprogramming, it was still, it was a metaprogramming similar to Ruby where,
[1935.04 --> 1939.34]  you know, when you need to do faster things, you need to be doing classic volume strings
[1939.34 --> 1940.16]  and things like that.
[1940.56 --> 1943.80]  So I knew I had like those problems and I was trying to solve them.
[1943.80 --> 1949.06]  And then I played with it for three or four months and the end result was really, really
[1949.06 --> 1953.06]  bad because, you know, I was like, I know I had those problems.
[1953.22 --> 1954.44]  Those are the solutions I know.
[1954.66 --> 1957.56]  And they didn't map really, really well, right?
[1957.64 --> 1961.98]  In the sense that the things I was trying to bring, it was not going to fit in this new
[1961.98 --> 1964.12]  ecosystem, this new way of doing things.
[1964.52 --> 1970.42]  So I stopped working on Alexer at the time and I said, okay, I know those are the problems.
[1970.42 --> 1975.46]  And I know that some of the solutions I'm looking right now, they are not going to fit.
[1975.56 --> 1977.88]  So I need to, I need to study more.
[1978.02 --> 1983.96]  I need to see how other languages, they are solving those problems and how they can fit
[1983.96 --> 1986.36]  into this new, into this virtual machine.
[1987.44 --> 1993.32]  And so that's why, that's when I started to say, okay, so I want, I don't want like Ruby
[1993.32 --> 1994.14]  in Erlang.
[1994.56 --> 1997.64]  I actually want, you know, I want to solve those particular problems.
[1997.64 --> 2001.50]  And if I need to take some ideas from Ruby, I'll take some ideas from Ruby.
[2001.64 --> 2005.98]  But if the best ideas, they are from Python, that will fit here.
[2006.08 --> 2007.08]  They are going to be from Python.
[2007.18 --> 2010.06]  They're going to be from Haskell or they're going to be from Clojure and so on.
[2011.54 --> 2012.92]  And yeah, go ahead.
[2013.62 --> 2015.60]  Yeah, I was just going to say, I mean, that's, that's very interesting.
[2015.74 --> 2019.50]  It kind of reminds me of what, you know, Jeremy Ashkenis did, you know, with CoffeeScript
[2019.50 --> 2024.30]  back in the day, which was, I'm not just going to do, you know, a nicer syntax, right?
[2024.30 --> 2028.84]  A Ruby version of JavaScript, I'm actually going to pull in what he considered and what
[2028.84 --> 2031.94]  the community considered best ideas from all these different camps specifically.
[2032.18 --> 2035.62]  But that, you know, Python plus Ruby was major influencers.
[2037.10 --> 2038.88]  So, I mean, that's definitely a winning strategy.
[2038.98 --> 2042.58]  It's like, you're not just, let's just not take Ruby ideas and move it over here to Erlang
[2042.58 --> 2042.92]  world.
[2043.10 --> 2048.58]  Let's actually like come up with the best thing we can for each given circumstance.
[2048.58 --> 2054.48]  But that seems like a really big green field and there's so many decisions to make.
[2054.60 --> 2055.22]  Was it daunting?
[2055.60 --> 2058.82]  Were you intimidated by this task that you had just taken on?
[2059.72 --> 2061.98]  That's a great question because I think a lot about it.
[2062.14 --> 2067.30]  And one of the things that makes it really easy is that, you know, if you're building
[2067.30 --> 2071.02]  software, if you're building a language on top of the Erlang virtual machine, there are
[2071.02 --> 2075.10]  a bunch of decisions that they are going to be taking for you.
[2075.10 --> 2075.98]  Okay.
[2075.98 --> 2083.76]  So that narrows a lot the scope of what you can do, which is, you know, it helps you.
[2084.70 --> 2086.68]  It helps keep you sane, right?
[2086.72 --> 2088.54]  Otherwise, it would be too much.
[2088.74 --> 2095.64]  I already feel like, you know, being a engineer, being a software developer, I want to build the
[2095.64 --> 2097.58]  best software I can possibly build.
[2097.98 --> 2098.42]  Right.
[2098.42 --> 2105.00]  And sometimes I have like those things that, you know, I see something different.
[2105.10 --> 2105.80]  I see something new.
[2105.98 --> 2109.54]  And I ask, should Elixir be using that instead?
[2110.18 --> 2110.44]  Right.
[2110.58 --> 2116.88]  How, how, how could, you know, how would that affect the language if I had made this other
[2116.88 --> 2117.40]  decision?
[2117.74 --> 2125.46]  And those things, they can be quite consuming because also if the answer was yes, life was
[2125.46 --> 2128.38]  going to be much easier because say, okay, I know how to make this better.
[2128.74 --> 2130.76]  But the answer is not yes.
[2130.88 --> 2137.74]  It's maybe you need to consider how it interacts with the other, you know, all the other things
[2137.74 --> 2138.70]  that you have in the language.
[2138.70 --> 2139.02]  Right.
[2139.12 --> 2141.30]  I say like, it's like a Jenga game.
[2141.36 --> 2143.36]  You need to have like the pieces well together.
[2143.46 --> 2148.16]  And sometimes you can, you know, take a piece out and put a better one in place.
[2148.16 --> 2153.36]  But, you know, maybe you do that and you're going to continue building on top until you
[2153.36 --> 2156.28]  find out that, oops, that piece was a bad piece.
[2157.66 --> 2159.94]  So, yeah.
[2160.08 --> 2162.78]  So I, I get that a lot.
[2162.84 --> 2167.56]  And I say joking that it's something I would never do again, create another programming language
[2167.56 --> 2172.00]  because of all those questions that you can have, it's just such a wild scope.
[2172.00 --> 2178.78]  And you, you cannot really, you know, choose how like this is a hundred percent better than
[2178.78 --> 2179.16]  the other.
[2180.04 --> 2181.90]  But the early virtual machine helped a lot.
[2182.04 --> 2188.06]  So I could get a lot of concerns, a lot of things like, okay, even if this is cool, I
[2188.06 --> 2189.16]  know I can have it here.
[2189.30 --> 2190.24]  So, and that's fine.
[2190.42 --> 2190.76]  Right.
[2190.78 --> 2191.44]  That's life.
[2191.76 --> 2197.88]  And I also, when I decided, so after I studied and I, I decided to give Alex here another try,
[2198.16 --> 2200.26]  I had a better foundation of what I wanted.
[2200.26 --> 2204.62]  So I said, for example, okay, if I'm building for the Erlang virtual machine, one of the
[2204.62 --> 2210.28]  things I want to do is to leverage this virtual machine as efficiently as I can.
[2210.72 --> 2213.02]  So I made a decision to, you know, I want to stay.
[2213.96 --> 2218.28]  So when you're compiling a code, you have like many compiler steps.
[2218.50 --> 2224.26]  And I decided to target a compiler step that was semantically very close to Erlang.
[2224.26 --> 2229.68]  And that would give me, that would add even more constraints, right?
[2229.70 --> 2230.48]  In language development.
[2230.64 --> 2231.62]  So that helped a lot.
[2232.02 --> 2236.34]  I also had already made decisions on what I wanted the syntax to be and that I wanted
[2236.34 --> 2239.50]  to have a macro system based on the STs and so on.
[2239.60 --> 2244.64]  So all those things that were like initial decisions, like this is what I want to be on
[2244.64 --> 2248.64]  top of, helped make it a little bit less daunting.
[2248.64 --> 2248.76]  Hmm.
[2251.46 --> 2257.20]  So did you just go into a, into a cave for two or three years and write code?
[2257.30 --> 2260.48]  Or I mean, you obviously were taking influence from other places.
[2260.62 --> 2261.48]  Were there any books?
[2261.56 --> 2264.22]  Was there any influence when it's like, I'm going to write a programming language?
[2264.30 --> 2268.20]  Sounds like you had a, at least a second start there, which is always nice to throw away
[2268.20 --> 2272.14]  those first efforts and start over when you have a little bit solid foundation.
[2272.14 --> 2279.44]  But what was the process like from, from maybe not to 1.0, but here's, here's a new guidepost.
[2279.56 --> 2287.02]  So in, in 2013, there's a post by Joe Armstrong, who I'm sure, Jose, you know, but to the audience,
[2287.18 --> 2288.70]  he's one of the designers of Erlang.
[2289.56 --> 2292.00]  And he published a post about Elixir.
[2292.08 --> 2296.26]  I think it was called One Week with Elixir in which he said, and I quote, this is good shit.
[2296.26 --> 2299.32]  So that's, I think that's a mile.
[2299.44 --> 2305.34]  I think that feels like a milestone to me from conception in 2010 and a false start to
[2305.34 --> 2308.92]  a certain degree or a restart in 2011 to 2013.
[2309.38 --> 2312.16]  You know, one of the inventors of Erlang is impressed with what you've done here.
[2312.70 --> 2317.22]  Can you, can you walk us through that time period and the process you went through to,
[2317.34 --> 2318.70]  to create it?
[2319.54 --> 2319.68]  Sure.
[2319.86 --> 2323.94]  So, uh, so at the beginning of 2011 was when I made the prototype.
[2323.94 --> 2326.70]  It sucked and I threw it all away.
[2327.28 --> 2333.06]  And then it was the end of 2011, the ending of 2011, beginning of 2012, where I had like,
[2333.36 --> 2338.48]  I've built a, a, a conceptual model that I said, okay, I think this can work.
[2338.66 --> 2345.10]  And this was also the period where I went to platform attack and say, okay, I think we
[2345.10 --> 2346.20]  can build this thing.
[2346.24 --> 2352.10]  And I think it can be useful because at the time we were looking at, uh, what I said was
[2352.10 --> 2355.94]  something like, you know, concurrency is becoming that thing.
[2355.94 --> 2357.70]  I just said concurrency has become more and more important.
[2358.28 --> 2365.06]  And today, if you, if you want to use a language that, uh, for better or worse is, um, it's a
[2365.06 --> 2371.36]  dynamic language and it focused on concurrency and it focused on productivity and being expressive.
[2371.36 --> 2375.60]  The, the option we had at the time, the main ones was, uh, closure.
[2376.16 --> 2376.56]  Right.
[2376.62 --> 2380.42]  So, you know, if you get something like you have Ruby and Python, but they are still not
[2380.42 --> 2382.34]  concurrency oriented as those other languages.
[2382.34 --> 2382.68]  Right.
[2382.98 --> 2385.58]  Uh, you have goal, but it has a static type system.
[2385.70 --> 2388.78]  They are not very focused on being expressive as a developer.
[2389.14 --> 2389.50]  Right.
[2389.50 --> 2395.40]  So I said like the only language that has everything that I could think of us using, uh, at the
[2395.40 --> 2396.32]  time was closure.
[2396.32 --> 2399.10]  And I said, you know, we, we need to have more options.
[2399.10 --> 2399.44]  Right.
[2399.72 --> 2403.66]  And it would be really nice to have an option that runs on the Erling virtual machine.
[2403.94 --> 2405.82]  And that was January 2012.
[2405.98 --> 2412.92]  And it was when the company made the commitment to, okay, we are going to like to invest, uh,
[2413.12 --> 2418.42]  part-time of, you know, uh, half of your time, uh, into developing this.
[2418.42 --> 2419.54]  So that helped a lot, right.
[2419.60 --> 2425.26]  Because it was not me being, you know, coding at night or something like that.
[2425.26 --> 2428.36]  I had, uh, it was part of my job from that moment.
[2429.20 --> 2432.38]  And so I had this idea of what I wanted the language to be.
[2432.52 --> 2437.80]  So as I said, I wanted to be closer to Erling and I knew I wanted a macro system.
[2437.80 --> 2442.42]  I knew I wanted, uh, for polymorphies, for example, I had completely ditched the idea of
[2442.42 --> 2443.54]  objects at this point.
[2443.98 --> 2448.56]  I, I ended up implementing something that's very close to closure protocols.
[2448.78 --> 2453.68]  And it's similar a little bit to type classes in Haskell and a little bit of interfaces in
[2453.68 --> 2454.76]  it's kind of the same idea.
[2455.42 --> 2458.04]  So that was like, okay, that's what I wanted to build.
[2458.18 --> 2459.64]  And then I started working on it.
[2459.94 --> 2464.18]  And I don't remember how much time it took me, maybe six months to have something like,
[2464.34 --> 2470.14]  Hey, I, I kind of feel comfortable now for releasing Elixir, uh, uh, what I would say
[2470.14 --> 2474.68]  like the 0.5, which is what people use when they say like, okay, this is probably usable
[2475.20 --> 2476.60]  up to some extent.
[2476.60 --> 2478.66]  And I also made the plan.
[2479.12 --> 2482.86]  I think it was even the beginning of the year to speak at Strangelove.
[2482.98 --> 2486.08]  They had at the time an emerging languages track.
[2486.90 --> 2490.20]  And, uh, I was, I went there, I was able to speak about Elixir.
[2490.32 --> 2494.04]  It's probably one of my first public talks about Elixir.
[2494.70 --> 2499.02]  And at that moment, some people already started to, to, to find it.
[2499.10 --> 2502.96]  So, uh, I always had access to a good part of the community.
[2502.96 --> 2505.30]  Like a lot of people follow me on Twitter and stuff like that.
[2505.60 --> 2507.48]  So I was always talking a little bit about it.
[2507.76 --> 2512.58]  And some people, they decided to try it out and they decided to explore, uh, the language.
[2512.62 --> 2514.32]  And some people started contributing back.
[2514.52 --> 2519.86]  So we see a little bit of a community forming and, uh, important contributions to the language.
[2519.98 --> 2521.84]  They came about that time.
[2522.02 --> 2526.62]  So for example, one of my favorite features we have today is the idea of doc tests.
[2526.62 --> 2533.00]  So the here doc syntax we have, like if we want to do a very long, uh, tax, right.
[2533.14 --> 2538.54]  We got it from Python and then someone said, you know, uh, Python has this doc test thing.
[2538.62 --> 2539.62]  It's already got the here docs.
[2539.70 --> 2545.16]  Look at the doc test, which allows you to write documentation of tasks inside your documentation.
[2545.32 --> 2548.28]  Then you can guarantee that the documentation is up to date.
[2548.56 --> 2549.00]  Right.
[2549.10 --> 2551.24]  And, uh, that's something we got at the time.
[2551.32 --> 2552.18]  It was a contribution.
[2552.18 --> 2557.06]  So the language was growing a little bit, you know, I was pouring my time.
[2557.14 --> 2561.08]  The community already started to, to help it grow and, and, and help it move forward.
[2561.42 --> 2564.50]  And it was, I think so.
[2564.60 --> 2567.98]  And, and then it was, that was 2012, right?
[2568.00 --> 2569.06]  I was working on it.
[2569.14 --> 2572.92]  The company was investing it, but I was always a little bit uncertain, right?
[2573.12 --> 2577.24]  Because, you know, like I know the company was investing in it, but for how long are we
[2577.24 --> 2578.56]  going to actually invest in it?
[2578.56 --> 2583.72]  Like if we spend two years working on this and nobody's using it, does it make sense?
[2583.92 --> 2588.68]  So I always had like the feeling that, you know, maybe next year it's going to be my
[2588.68 --> 2590.90]  final year working on this.
[2592.40 --> 2597.46]  And yeah, it was, but it was like, you know, if that happened, it was like, oh, the ride
[2597.46 --> 2598.00]  was fun.
[2598.12 --> 2598.44]  Right.
[2598.52 --> 2603.80]  Like, uh, I learned a lot and, uh, people, you know, use it and enjoy it.
[2603.80 --> 2611.02]  So, so that was worthwhile, but it was in 2013 that, uh, we had like two very good news,
[2611.02 --> 2618.90]  uh, you know, in a row, which was, um, Dave Thomas, he sent me an email asking if he could
[2618.90 --> 2620.52]  publish a book about elixir.
[2621.28 --> 2627.40]  And, uh, a little bit actually before that, also, uh, Simon St. Laurent, uh, from O'Reilly,
[2627.40 --> 2632.38]  he wrote Introducing Erlang and he said, I want to make this Introducing Elixir 2, which
[2632.38 --> 2635.70]  is, um, probably the first Elixir book announced.
[2635.80 --> 2637.50]  I don't remember which one of those two they came.
[2638.26 --> 2639.86]  And, and it was just fantastic, right?
[2639.88 --> 2646.08]  Because now it's like, there are other people, uh, you know, effectively investing on the
[2646.08 --> 2646.84]  language as well.
[2647.04 --> 2647.38]  Right.
[2647.38 --> 2653.04]  And, you know, like if one of the things I had in my mind is that I didn't want to write
[2653.04 --> 2654.54]  a book on Elixir.
[2654.90 --> 2659.46]  I felt like, well, maybe this is something that it's probably going to be necessary in
[2659.46 --> 2661.88]  the long run, but I don't want it to be me.
[2661.96 --> 2667.22]  But if nobody does that, uh, I, I, I would probably do it, let's say.
[2667.54 --> 2670.46]  And, you know, and then Dave Thomas come and say like, Hey, I want to write the book.
[2670.48 --> 2671.28]  Like, that's great.
[2671.30 --> 2671.46]  Right.
[2671.46 --> 2672.42]  Like it's Dave Thomas.
[2672.76 --> 2674.36]  He's, he wants to write the book.
[2674.36 --> 2676.60]  So that was very exciting.
[2676.96 --> 2677.86]  And that was a big deal.
[2678.54 --> 2678.78]  Yes.
[2678.90 --> 2683.72]  And, and, and that was what led, I think it was Dave Thomas that led, uh, Joe to, to
[2683.72 --> 2688.72]  do that because, uh, Joe, he got to know that Dave Thomas was writing a book on Elixir.
[2688.78 --> 2690.64]  And I was like, okay, I need to try this.
[2690.70 --> 2697.10]  And, um, and we started growing more and more from that, uh, from that moment on.
[2697.68 --> 2701.94]  So surely you read Joe's post and you, you know, you saw the quote, you saw his take
[2701.94 --> 2702.34]  on it.
[2702.34 --> 2706.96]  You're, can you recall your thoughts and feelings, uh, with regard to Elixir when you
[2706.96 --> 2709.70]  see, you know, one of the designers of Erlang saying that it's good?
[2710.36 --> 2712.38]  Oh, it was, uh, it was really great.
[2712.58 --> 2719.58]  Uh, I don't remember exactly, but, um, Joe and, uh, which Joe and Robert, they're both
[2719.58 --> 2720.12]  creators of Erlang.
[2720.24 --> 2723.08]  They were always very open and we could always have conversations.
[2723.58 --> 2728.92]  Also the OTP team at Ericsson at Montaigne's Erlang, they're always, uh, they were always
[2728.92 --> 2729.46]  very open.
[2729.46 --> 2735.22]  And so I remember when I first announced at Elixir, uh, the, the tagline was, uh, Elixir,
[2735.48 --> 2739.52]  uh, a modern approach for, to the Erlang virtual machine.
[2740.02 --> 2746.78]  And it was a horrible tagline, but the modern, uh, word like, uh, made some people mad.
[2746.78 --> 2752.50]  And, and I remember getting email from, from someone that, you know, at Ericsson say, you
[2752.50 --> 2756.02]  know, like, it's fine, you know, ignore that.
[2756.10 --> 2758.12]  Just continuing, just continue building with stuff.
[2758.34 --> 2758.78]  Right.
[2758.78 --> 2764.52]  So that was very encouraging and getting Joe's feedback and later Robert feedback and so
[2764.52 --> 2764.70]  on.
[2764.76 --> 2769.66]  It was also very encouraging to continue, um, doing the work.
[2769.74 --> 2769.98]  Right.
[2769.98 --> 2774.54]  I just want to point something out here for the, for the listening audience, just in case
[2774.54 --> 2780.18]  they didn't kind of hear what I think I heard, which was, here's you, uh, and everyone sees
[2780.18 --> 2783.04]  you as this really great software developer.
[2783.42 --> 2789.44]  Um, especially with all the success with Elixir and they see you to what you just said, basically
[2789.44 --> 2792.90]  was that you got a couple of years into this and you thought it might not work out.
[2792.90 --> 2798.38]  And then you sort of hit this stride where I'm sure one of your heroes, Dave Thomas, who
[2798.38 --> 2802.98]  wrote the Ruby programming book, which is the, the most bought Ruby book ever.
[2802.98 --> 2803.40]  I'm sure.
[2804.00 --> 2808.14]  Uh, like, so here's one of your heroes bless basically what you're doing and then want to
[2808.14 --> 2808.84]  write a book about it.
[2808.84 --> 2814.36]  Like how that all worked out was to me, it's just like a, a really triumphant moment for
[2814.36 --> 2814.52]  you.
[2815.06 --> 2815.42]  Yes.
[2815.54 --> 2815.90]  Yes.
[2815.90 --> 2819.54]  It was, it was like those things that give you a lot of confidence, right.
[2819.54 --> 2820.72]  To continue moving forward.
[2820.90 --> 2821.02]  Right.
[2821.16 --> 2822.06]  You're going the right way.
[2822.06 --> 2822.10]  Yeah.
[2822.52 --> 2822.92]  Yes.
[2822.92 --> 2828.20]  It takes the, it takes the, you know, the uncertainty, which helps a lot.
[2828.24 --> 2828.64]  Right.
[2828.68 --> 2831.72]  Removing that uncertainty that I may not be working on this next month.
[2831.88 --> 2832.16]  Right.
[2832.42 --> 2834.72]  Uh, so that was really nice.
[2835.26 --> 2841.22]  And, and, you know, I, and the, the, the benefit is that I, I became closer to Dave Thomas
[2841.22 --> 2841.56]  as well.
[2841.66 --> 2848.40]  So when we had the first Elixir conference, uh, it was in Austin and my flight was, uh, in,
[2848.40 --> 2849.96]  from Dallas where he lives.
[2849.96 --> 2853.00]  So we took a car ride and we're able to talk a lot there.
[2853.28 --> 2855.20]  Sometimes I'm like wondering things.
[2855.42 --> 2859.66]  I know I have like the perk of being able to send like Dave Thomas and the main and say
[2859.66 --> 2861.10]  like, Hey, what do you think about this?
[2861.50 --> 2861.84]  Right.
[2861.84 --> 2869.00]  So, uh, those are very nice perks that came as consequence of the book as well.
[2869.66 --> 2872.98]  Well, I'm going to tease something out for you, Jose, before we head to this break, I'd
[2872.98 --> 2878.54]  like to hear from you what some of the overarching features of Elixir are.
[2878.98 --> 2883.46]  When we come back from the break, uh, we'll dive a little deeper into some of them if we
[2883.46 --> 2883.90]  can.
[2883.90 --> 2888.82]  Uh, but do us a favor, share kind of an overarching feature set for Elixir.
[2890.06 --> 2890.46]  Okay.
[2890.58 --> 2890.76]  Yeah.
[2890.76 --> 2892.44]  So that's really hard.
[2892.82 --> 2895.80]  So I like, I like, so yeah.
[2895.80 --> 2902.04]  So Elixir, so the main thing is that you're going to use it to build, uh, maintainable and
[2902.04 --> 2902.96]  scalable applications.
[2902.96 --> 2908.02]  But we, I, we also, Elixir is also an expressive language.
[2908.02 --> 2912.68]  So we want to, you know, allow that thing that developers, they can get the language.
[2913.02 --> 2914.36]  Actually, I'm not going to say expressive.
[2914.64 --> 2916.22]  It can be expressive as well, but extensible.
[2916.38 --> 2920.42]  They can get the language that's always on the ideas language to be able to get it and
[2920.42 --> 2927.34]  extend it to whatever domain, uh, you're working on and the focus on, on productivity as well.
[2927.46 --> 2928.64]  So we have very good tooling.
[2928.64 --> 2934.92]  So I would say like the, so that's like the macro overview, uh, of what you can build
[2934.92 --> 2936.70]  with the language and then features.
[2936.84 --> 2940.62]  There are so many, but I think like the tooling is, it's really fantastic.
[2940.98 --> 2947.46]  I like features like focus on documentation and, um, and what else?
[2947.50 --> 2953.62]  I like our, uh, the way we can do polymorphism, which is a language specific trait in this case
[2953.62 --> 2955.44]  and so on.
[2955.60 --> 2958.42]  I, yeah, I'm not sure if I, if I give it to the answer.
[2958.64 --> 2961.32]  But yeah, that, that's what we're looking for.
[2961.38 --> 2962.84]  I mean, we're getting ready to go into this break.
[2962.84 --> 2967.58]  So we wanted to kind of get a breakdown to leave the listeners hanging, so to speak, a
[2967.58 --> 2971.34]  little cliffhanger, so to speak on what, uh, Elixir is built upon.
[2971.34 --> 2975.48]  Like, I think the, the plain language in which you put it in wasn't like, here's the feature
[2975.48 --> 2976.94]  list of, of, uh, Elixir.
[2976.94 --> 2980.28]  It's, it's more like, you know, from your, from your mouth.
[2980.28 --> 2984.00]  So from in your own words, it wasn't like this scripted list.
[2984.38 --> 2984.74]  Cool.
[2985.00 --> 2986.90]  Uh, Jared, anything you want to add before we go to the break?
[2986.90 --> 2988.12]  No, that's good.
[2988.20 --> 2991.74]  I've, I've been writing those down and we have a list of things that we can definitely
[2991.74 --> 2995.38]  use as jumping off points to talk about, uh, on the other side.
[2995.58 --> 2995.94]  Cool.
[2996.04 --> 2996.80]  Let's take that break.
[2996.82 --> 2997.68]  We'll be right back.
[2997.68 --> 3003.76]  Our friends, Linode are huge fans of the show and many of the developers that work at Linode.
[3004.18 --> 3005.46]  Listen to the show.
[3005.46 --> 3006.88]  They're huge fans of what we're doing here.
[3006.92 --> 3008.06]  They want to support what we're doing.
[3008.60 --> 3011.30]  And we want to invite you to try out Linode.
[3011.54 --> 3015.30]  One of the most fastest efficient SSD cloud servers on the market.
[3015.84 --> 3019.30]  Use our code change log 20 to get $20 in credit.
[3019.80 --> 3021.16]  Basically two free months.
[3021.36 --> 3023.32]  Plan started just 10 bucks a month.
[3023.32 --> 3029.24]  They have eight data centers spread across the entire world, North America, Europe, Asia
[3029.24 --> 3029.78]  Pacific.
[3030.32 --> 3033.62]  I got hourly billing with a monthly cap on all plans and add on services.
[3033.62 --> 3036.54]  You get full root access for more control.
[3037.04 --> 3040.42]  Run VMs, run containers, or even your own private Git server.
[3040.88 --> 3046.56]  You can enjoy native SSD storage, 40 gigabit network, Intel E5 processors.
[3046.56 --> 3051.46]  Again, use the code change log 20 to get a $20 credit with unlimited uses.
[3051.66 --> 3052.30]  Tell your friends.
[3052.74 --> 3054.68]  It doesn't expire until the end of this year.
[3054.86 --> 3056.62]  So use it as many times as you want.
[3056.74 --> 3058.40]  Share it to everyone you know.
[3058.82 --> 3061.50]  Head to Linode.com slash change log to get started.
[3065.96 --> 3067.36]  All right, we're back from the break.
[3067.62 --> 3071.26]  And we got this feature list and we're looking at it.
[3071.34 --> 3073.74]  And one of them stands out more than the others.
[3073.74 --> 3076.20]  And it's maintainable and scalable applications.
[3076.20 --> 3077.28]  How do we quantify that?
[3077.34 --> 3078.34]  What exactly does that mean?
[3078.96 --> 3079.90]  How do we break that down, Jose?
[3081.16 --> 3083.34]  So that's a very good point.
[3083.74 --> 3087.30]  I don't like to say, oh, what is the language feature?
[3087.36 --> 3091.22]  I like to say pattern matching because unless you use the functional programming language,
[3091.28 --> 3092.64]  you don't know what it is.
[3093.10 --> 3096.62]  So I started with things like, what is the focus?
[3096.70 --> 3099.48]  And the focus is maintainability and scalability.
[3099.48 --> 3114.66]  And one of the things about maintainability in my experience with Alex here so far and why I think it's a maintainable language is all behind the idea of processes we were talking about.
[3115.12 --> 3115.30]  Right?
[3115.30 --> 3120.30]  So for example, if you're thinking about maintaining an application, there are two aspects of it.
[3120.44 --> 3122.14]  It's like it's running production.
[3122.72 --> 3129.10]  And part of maintaining it is to ensure it actually runs properly in production.
[3129.10 --> 3134.42]  So if you never, I know you're already playing with Alex here.
[3134.42 --> 3144.76]  But if you never run with it, use it before, we have a tool called Observer that you can install your node or connect to a node and run this tool.
[3145.16 --> 3147.48]  And it kind of shows the whole tree of our system.
[3148.24 --> 3156.70]  So Alexier applications, sorry, your Alexier software, your Alexier system is built into a bunch of tiny applications.
[3156.70 --> 3165.00]  And you can go one by one and introspect those processes, those lightweight threads of computation we were talking about earlier.
[3165.34 --> 3169.56]  So you have really a great amount of introspection of how your system works.
[3169.74 --> 3176.00]  And this matters a lot to ensure the software is running properly in production, which is one of the aspects.
[3176.00 --> 3191.22]  Just to give an idea of how this is useful is, so one of the things that we did with Phoenix and the whole channels idea and WebSocket idea is to make sure we got a very powerful machine for our Rackspace.
[3192.04 --> 3196.02]  And we wanted to, and we're able to have two million connections on that same machine.
[3196.12 --> 3200.04]  So we had like two million clients connect to the same machine, connect to Phoenix channels.
[3200.04 --> 3207.42]  And we broadcast, for example, a Wikipedia article to those two million clients in like two or three seconds, right?
[3207.88 --> 3212.74]  And in order to make it go that fast, we had to improve it.
[3213.08 --> 3216.14]  So what we did is that we connected the clients.
[3216.72 --> 3225.58]  And then when we, for example, at the first try were what, 300,000 clients where we reached our first bottleneck or even 30,000.
[3225.64 --> 3226.28]  I don't remember exactly.
[3226.28 --> 3233.02]  But what we did is that we connected the observer and because it gives you this whole idea of the system, right?
[3233.10 --> 3244.12]  We could say, and because all the code run into processes, those lightweight threads of computation, when things started to go slow, we went to a pain and say, wait, which process is the one that is slow?
[3244.22 --> 3245.58]  The one that's doing a lot of work?
[3245.62 --> 3247.62]  Because that's the one that's going to be my bottleneck.
[3247.92 --> 3250.08]  And I say, oh, that's the one that's being slow.
[3250.34 --> 3251.34]  Let's optimize it.
[3251.34 --> 3256.10]  And then we optimized, we moved the bottleneck elsewhere, and we did this a couple times.
[3256.24 --> 3262.24]  And I think over the period of two days, we were able to go like to two million connections just by relying on this tool.
[3262.50 --> 3267.54]  And these we used as an optimization job, which is also part of maintainability, right?
[3267.58 --> 3271.98]  If things are slow, you need to go and try to understand your system and try to make it fast.
[3271.98 --> 3274.16]  So that's one aspect that we have to eat.
[3274.50 --> 3279.24]  The other aspect that we have of maintainability is also related to code.
[3280.02 --> 3282.56]  So we were talking about this during the break.
[3282.86 --> 3289.96]  So, for example, I think the whole idea regarding immutability helps a lot with that.
[3290.24 --> 3291.64]  And the whole idea of functional programming.
[3292.12 --> 3297.98]  So, okay, let me just do a statement and then we're going to explore a little bit.
[3297.98 --> 3306.84]  I think a lot of the reason why this software is more maintainable, it's because of ideas that we have that come from functional programming.
[3307.72 --> 3311.70]  And functional programming, you know, if we ask someone like, what is functional programming?
[3312.74 --> 3315.46]  You're going to get a bunch of different answers.
[3316.16 --> 3322.40]  So one of the things that's usually associated with functional programming is the whole idea of immutability.
[3322.72 --> 3325.40]  And I'm going to expand this soon.
[3325.40 --> 3337.06]  But to me, the big thing about functional programming is that it pushes part, it tries to make the complex parts of your system explicit.
[3337.66 --> 3339.56]  And that's why it's so helpful.
[3340.10 --> 3342.76]  So, for example, mutation, right?
[3342.82 --> 3344.36]  Like changing things in place.
[3344.40 --> 3350.06]  It's a source of complexity because Rich Hickey has great talks on the topic, right?
[3350.10 --> 3354.12]  Because now you need to think of how that thing is changing over time.
[3354.12 --> 3358.58]  And if you remove the mutability aspect, right?
[3358.62 --> 3365.98]  If you make things immutable by default, you remove that whole time question of understanding your system, right?
[3366.14 --> 3369.22]  So mutability is a source of complexity.
[3369.48 --> 3370.92]  So it needs to be more explicit.
[3371.12 --> 3372.10]  It cannot be the default.
[3372.20 --> 3375.40]  It cannot be something that you do automatically.
[3375.40 --> 3388.40]  And for example, another way this shows up in functional programming for using more strict languages like Haskell is the whole idea that any side effect that you have in your system, right?
[3388.42 --> 3397.38]  If your system is changing the word around you, like talking to the database or someone, in Haskell, you need to be explicit and use a monad.
[3397.38 --> 3400.02]  But here we don't have monads, right?
[3400.12 --> 3410.74]  But we go with this idea, you know, if you want to do something that's changing the word around you, we want you to be explicit and put it somewhere more explicit in your code.
[3410.94 --> 3415.68]  And we want you to put it apart from the code that does not change the word around you.
[3415.68 --> 3424.40]  And so what you have at the end of the day, you're like writing functions that receive data and transform this data instead of mutating it.
[3424.52 --> 3429.28]  Which means like every time you call a function with the same input, you're going to get the same output.
[3429.44 --> 3433.58]  It's easier to understand what is happening with it.
[3433.66 --> 3436.90]  The state that it receives, it's always explicit.
[3437.10 --> 3439.40]  There is nothing happening behind the scenes.
[3439.40 --> 3444.88]  One example to try, like people listening, to try to visualize that.
[3445.62 --> 3452.40]  And for example, like when you're writing tasks for object-oriented languages, sometimes we always had to write that task.
[3452.52 --> 3452.84]  I don't know.
[3452.96 --> 3461.56]  We had to set up a bunch of our mocks or relationships or set up the state you need to get to before you can write the task, right?
[3461.56 --> 3469.96]  And that's because, you know, it has a bunch of states, a bunch of things related to it that it can mutate, that it depends on implicitly, right?
[3470.22 --> 3472.34]  It's like inside the object.
[3472.66 --> 3474.22]  But here we don't have that, right?
[3474.26 --> 3481.48]  Like you have functions and everything, there is an object state that is a consequence of calling something, right?
[3481.70 --> 3486.60]  Everything that you receive is explicit and you need to return everything explicitly as well.
[3486.60 --> 3499.02]  And I think that makes wonder to, you know, make your software more maintainable because now you can look at it and say, hey, I see what this is doing because I can look at a function and see everything it needs to work on.
[3499.34 --> 3502.64]  There are no inner state, right?
[3502.84 --> 3508.46]  There are a bunch of relationships that can change and affect the whole system.
[3509.02 --> 3512.64]  So those are some of the points for maintainability.
[3512.64 --> 3518.64]  I'll just expand on that and maybe bring up a specific point when it comes to functional programming.
[3519.72 --> 3524.38]  One thing that you often find is you have this, like you said, you're just transforming data, right?
[3524.48 --> 3530.90]  So you pass the data to this function, then this function, then this function, and they all change it in some way, return a new thing.
[3531.14 --> 3532.86]  That's a mutation of that previous form.
[3532.86 --> 3543.02]  And so you end up oftentimes passing around the same, like I've called previously, just a bag of data and doing things to it.
[3543.26 --> 3546.64]  And so my question is always like, well, why don't you just make that bag of data smarter?
[3547.00 --> 3552.50]  And then it's an object and now it has its own internal, you know, things going on and you get back to object-oriented programming.
[3552.50 --> 3573.40]  One thing that Elixir does, which I think is really cool, when it comes to like passing that same thing into as the first argument to all these different functions that are going to mutate it, is you've introduced a way of just alleviating that little syntax pain, which is your pipeline operator, which is kind of like the pipe symbol and the greater than symbol.
[3573.40 --> 3578.70]  Can you explain us? I think that's one of the, if we talk about just language features, I think that's a big one.
[3579.22 --> 3581.10]  And maybe it's just syntax sugar, maybe not.
[3581.34 --> 3588.00]  But can you talk about the pipeline operator and what it does and then why it seems to resonate so well with so many programmers?
[3589.22 --> 3601.68]  Right. So the whole idea of the pipeline operator is actually to help you and to express like the whole, like I have the data and I want it to go through this step, this step, this step.
[3601.68 --> 3606.36]  Like the pipe in your terminal. Right. And I added it.
[3606.44 --> 3611.92]  I think it was, I added because I saw it in F sharp or ML or something like that.
[3612.62 --> 3616.80]  But who really took it like to the next level was Dave Thomas.
[3617.00 --> 3620.68]  So if you buy like programming Elixir book, the pipeline operator is right down in the cover.
[3620.92 --> 3626.04]  And he was the one who saw like, hey, this is the thing that's going to make Elixir click to a lot of people.
[3626.04 --> 3632.00]  Right. And, but yeah, the idea is very simple.
[3632.30 --> 3639.40]  And Elixir kind of said, okay, the subject is always going to be the first argument, which makes everything easier to pipe.
[3639.40 --> 3643.86]  Right. And yeah, and that's it.
[3643.96 --> 3649.86]  And I, I, I agree with you that it kind of gives the idea, well, this is kind of object oriented, right?
[3649.88 --> 3656.52]  Because I could think of, I had like this bag of data and then I could be calling functions on it and the pipeline is going to resemble that.
[3656.52 --> 3676.84]  And that's why I think it resonates to a lot with a lot of people, but there is one very big importance difference, which is if you, if you have like, if we made it objects and the thing about objects is that you are putting the data with the things that act on it together.
[3676.84 --> 3679.66]  Right. You are, you are mixing data plus code.
[3680.24 --> 3680.32]  Right.
[3680.40 --> 3690.20]  Yes. And one of the things that I ended up with realized, I ended up realizing later is that it brings a bunch of awkwardness into, into our software.
[3690.20 --> 3700.78]  And then it kind of becomes a problem and we end up trying to solve it, solve it and, and ends up creating more problems in object oriented languages.
[3700.78 --> 3706.38]  Uh, I hope that I do not sound like a, what is a snob saying those things.
[3707.04 --> 3708.94]  Um, I don't think so.
[3709.30 --> 3709.66]  Yeah.
[3709.88 --> 3710.58]  Truth is truth.
[3711.60 --> 3714.60]  Yeah. It's just like things that I built with time, right?
[3714.60 --> 3719.90]  Like those, those perceptions, because for example, after you put those things together, right?
[3719.96 --> 3727.48]  You say, okay, now if I want to add something new that works on this data, I want to couple it together as well.
[3727.48 --> 3732.30]  So imagine that you have like your object that has a couple, a couple of methods that work on this data.
[3732.40 --> 3733.20]  We just couple them.
[3733.36 --> 3736.94]  And then you have an idea for a new method that you want to add to it.
[3737.24 --> 3747.32]  You, if you call it differently as different from the other methods, if you cannot simply say object.foo, if you cannot say object my new method, it's awkward, right?
[3747.36 --> 3750.88]  So we want to put it in there with the rest of the things.
[3751.24 --> 3753.60]  And for example, Java does not allow you to do it.
[3753.60 --> 3755.24]  After you define, you cannot extend it.
[3755.52 --> 3758.78]  And then people are like, oh, now you need to sublux and so on.
[3759.32 --> 3768.90]  And, uh, Ruby is much more flexible on, on these matters that we can extend things later, but it generates all kind of weird coupling now, right?
[3768.90 --> 3775.74]  Because I have now external code that may be, uh, monkey patching an existing class and that adds issues.
[3775.74 --> 3780.54]  And that's all because we try to couple those two things in the first place, right?
[3780.72 --> 3793.48]  In Alexeer, it doesn't, we, we, we don't, when you're using the pipeline, there is, there isn't this awkwardness because we are saying, I have my data and I'm going to call, uh, the function bar from the module full.
[3793.48 --> 3799.24]  And then if you want to add your own module with your own functions, you just call it next in the pipeline, right?
[3799.28 --> 3803.82]  I'm going to call my new, my new function in this other module, right?
[3803.88 --> 3806.72]  And it's natural because that's how you're calling everything.
[3807.12 --> 3810.74]  And you can swap easily, you know, change things.
[3810.78 --> 3812.94]  You can compose, you can replace the function calls.
[3812.94 --> 3820.52]  And you never feel that need to couple it together with the data, which to me, it's the, it's the big win, right?
[3820.82 --> 3827.90]  It also has the big win that, uh, for example, if you're, if you have an object, you're saying object.full, where is that full defined?
[3828.20 --> 3830.20]  For example, in Ruby, where you can define things everywhere.
[3830.36 --> 3831.66]  It's really hard, right?
[3831.92 --> 3838.52]  And you can even think it's defined somewhere, but some other, uh, file kind of replaced it by something else.
[3838.52 --> 3842.74]  But here you have modules and after the module is compiled, it's done.
[3842.86 --> 3843.86]  It's a, it's a sealed deal.
[3844.18 --> 3845.74]  And I know it's in that place.
[3845.80 --> 3848.54]  And if I'm going to look at there, it's going to be there for sure.
[3848.86 --> 3851.48]  So it's going to, to move somewhere else under my feet.
[3851.74 --> 3857.02]  So I think those things, they, they, they, they, they matter a lot.
[3857.14 --> 3860.58]  And it's going to help us write more maintainable code.
[3862.08 --> 3865.66]  Let's talk about another aspect, which you bring up around productivity.
[3865.66 --> 3868.98]  And you say it's because the tooling is good.
[3869.78 --> 3875.56]  And, uh, recently we've had a lot of fans of Elm talking to us, especially after our show recently with Richard Feldman.
[3876.06 --> 3890.86]  Um, one thing he said on that show, which was that the most exciting thing about Elm to him, which again, that's the best functional programming in their browser as their pitch, is that the compiler itself is a huge benefit of using Elm.
[3890.86 --> 3907.78]  And, um, I'm not sure if it was him or somebody else who said this idea of humane compilers, where they're like there to help you and to, uh, be useful and not just like segfault or just throw it like a, you know, syntax error, not, not give you any information about what's going on.
[3907.78 --> 3910.34]  Um, is huge for productivity.
[3910.74 --> 3912.50]  And that's something that Elixir seems to support.
[3913.22 --> 3921.50]  Um, as I said, I've been doing a little bit of Elixir and I'll find that sometimes it tells me not just what went wrong, but like gives me a code snippet.
[3921.58 --> 3925.54]  I'm like, if you would just replace your code with this code, everything would be all right.
[3925.54 --> 3927.54]  That seems like a pretty big feature.
[3928.16 --> 3931.70]  Was that a, um, a focus for the language early on?
[3932.28 --> 3938.34]  And, and can you talk about, um, why that's such an important aspect of why, um, Elixir is the way it is?
[3939.04 --> 3941.38]  Yeah, that's, yeah, that's a great question.
[3941.66 --> 3951.82]  Uh, so I always said, uh, like if you see a bad error message in Elixir, uh, you should open up a bug report.
[3951.82 --> 3956.34]  Like if you, if you get an error and say like, I don't know how to fix this, I don't know what is the next step.
[3956.60 --> 3957.92]  I don't know what is wrong with my code.
[3958.22 --> 3961.64]  Open up a bug report and I'm going to try to, to make it, uh, it better.
[3962.44 --> 3970.90]  Um, and I, I don't think our compiler is as good as the Elms compiler in terms of like telling you what to do next.
[3970.90 --> 3981.50]  Uh, Evan did really a great job with Elm and having this static type system in that case, uh, uh, helps a lot to, you know, provide the proper information.
[3981.82 --> 3984.44]  But it's something that we really try to do, right?
[3984.50 --> 3988.08]  Like, Hey, you know, I, I don't want to make you clueless, right?
[3988.10 --> 3988.82]  Something's wrong.
[3988.90 --> 3992.98]  I'm going to try to tell you as much as possible why that happened.
[3993.32 --> 4002.54]  And the, and that, and it was there since the beginning because, uh, what happened is that I want people to use Elixir, right?
[4002.98 --> 4006.94]  And if they're using Elixir, they need to learn a lot of things, right?
[4006.96 --> 4011.48]  They need to learn about pattern matching as we're talking about, you know, immutability.
[4011.66 --> 4014.40]  And you no longer have objects and things are immutable.
[4014.76 --> 4017.06]  So you need to think in terms of immutability.
[4017.06 --> 4018.18]  There is recursion.
[4018.48 --> 4021.16]  There are a lot of things that you need to learn, right?
[4021.24 --> 4025.98]  So those small things that can get in your way, uh, the silly things, right?
[4026.00 --> 4027.04]  They are not the important ones.
[4027.04 --> 4036.60]  Like when I do a type or when I do a small mistake, we need to get them out of our way, or if they happen, I need to tell you, you know, how to solve that problem and how to think in the proper way.
[4037.06 --> 4040.38]  So, um, that's the reasoning for this.
[4040.46 --> 4041.72]  And it was kind of always there.
[4041.72 --> 4047.76]  It was something that we always were to, you know, let's, let's make this learning process easy.
[4047.92 --> 4054.04]  So you can focus on the things that matter and not on those small details on those hiccups that everyone have, right?
[4054.04 --> 4059.80]  When they are, they are, um, learning how to program on a new language.
[4059.80 --> 4071.62]  I remember, I don't know, I don't remember who said this, but they said that their first Alex's code, they would just type whatever they think what it should be.
[4072.14 --> 4075.30]  And then the compiler would tell them, Hey, that's not the proper thing.
[4075.40 --> 4076.68]  And they would fix it.
[4076.82 --> 4079.94]  And, you know, they got it working only with those steps.
[4079.94 --> 4094.68]  And he didn't have like to, to, to search on the internet, go and stack overflow because the compiler, every time he did something that was not like the, the, the thing that was supposed to be done, it was able to guide him towards the proper direction, which is really nice.
[4095.54 --> 4096.34]  Yeah, absolutely.
[4096.74 --> 4102.40]  Getting stuck on those little things is always a burden and can really turn you off to a language when you just can't get it to work, you know?
[4102.40 --> 4106.74]  So having it hold your hand as much as possible, um, is huge.
[4106.98 --> 4115.50]  I think another aspect, we talk about features, um, a huge feature in any language is the community, the ecosystem around it.
[4115.68 --> 4119.60]  We've been mentioning offhand Phoenix, which is the web framework.
[4119.60 --> 4138.32]  Um, there's also, um, there's also Ecto, which is a database layer, um, and other projects that aren't Elixir proper, but they are things that you appear to be personally invested in with regards to time and effort, um, and decision making and stuff.
[4138.32 --> 4146.72]  When we had Chris McCord on back in episode 147, I asked him kind of about, I asked him about you and I was kind of wondering aloud.
[4147.44 --> 4159.40]  Um, and I, I said, I wonder if the reason why you've been so highly involved specifically in Phoenix at that time is because you, you see it as a, as a chance to give Elixir a greater success.
[4159.40 --> 4168.68]  So if it has a killer web framework, you know, Rails put Ruby on the map in America at least, um, and made it something that was more mainstream.
[4169.42 --> 4181.06]  And so maybe if Elixir had a Rails-esque type of a project or, uh, let's just say a really viable web framework that people could build web apps with, that would increase the chance of success of the language.
[4181.06 --> 4183.20]  I asked Chris if that's why you did it.
[4183.58 --> 4185.70]  And he said, well, I can't really answer that.
[4185.78 --> 4187.68]  I can't tell you why Jose does what he does.
[4188.30 --> 4190.38]  Um, but you might ask him sometime.
[4190.64 --> 4196.46]  So I say all that to say this, um, here we are.
[4196.56 --> 4197.64]  I can finally ask you.
[4198.20 --> 4201.90]  Um, you've been highly invested in the web framework and in these web tools.
[4202.22 --> 4204.16]  And I just wonder the reasoning behind that.
[4204.16 --> 4210.54]  And if I was right on in the sense of, you know, you, you see this as a path of giving Elixir its greatest chance for success.
[4211.06 --> 4212.10]  Right.
[4212.24 --> 4220.16]  So I, I try to not vinculate whatever I'm doing with the chance of success, you know, like directly.
[4220.38 --> 4222.06]  I obviously wanted to succeed.
[4222.18 --> 4222.44]  Right.
[4222.50 --> 4229.14]  But, uh, I try not to do things like directly because of that.
[4229.14 --> 4229.44]  Right.
[4229.44 --> 4235.00]  So for example, for the web in particular case, um, I, I said at the beginning, right.
[4235.00 --> 4236.28]  About platform attack, right.
[4236.28 --> 4239.08]  That we are a consultancy and then we are working with projects.
[4239.08 --> 4241.28]  And most of our projects, they were web projects.
[4241.98 --> 4250.90]  So when, when I, I, back in 2012, when I asked them to fund the idea is that eventually we would have, uh, Elixir 1.0.
[4250.90 --> 4254.00]  And eventually we would have the good web tooling.
[4254.74 --> 4257.46]  Uh, so we can use it for ourselves.
[4257.46 --> 4265.48]  The company could use it and can start using, uh, Elixir in production and use with our clients, which is our, one, one of our goals.
[4265.90 --> 4268.14]  So that was pretty much the idea.
[4268.24 --> 4273.48]  So when I was working with Elixir, I had like, I don't want this to be a web centric language.
[4273.48 --> 4276.78]  So I'm not putting like things that make sense only for the web here.
[4276.98 --> 4278.22]  That's not what I want.
[4278.88 --> 4286.44]  Um, but after we got Elixir 1.0 out of the way, I said, okay, I'm going to step two, right?
[4286.56 --> 4289.86]  Like this is the second milestone, which is to focus on the web tool.
[4289.90 --> 4295.64]  And that's why I started to work more with Phoenix and work more with Vecto and, and so on.
[4295.64 --> 4309.86]  And other than that, for example, before Elixir 1.0 came out, I kind of built my own web framework that was not supposed to be used for anything, but just to give an idea like how, uh, where the language was and what could I do with it and what could be improved.
[4310.00 --> 4314.06]  So that's something that happened, but I always try to keep this stuff apart.
[4314.16 --> 4315.30]  It was never the focus.
[4315.92 --> 4324.02]  So the main reason was really, you know, if we want to use, if Plataform Attack want to use this with clients, we need to have a very good, uh, web story.
[4324.02 --> 4327.02]  And that was actually the goal for last year.
[4328.00 --> 4336.86]  And, uh, I am like, and we, I think we achieved it with, with a lot of success because, uh, Phoenix 1.0 came out and it's not me, right?
[4336.86 --> 4340.62]  It's like the, the nice thing about Phoenix is actually that I didn't have to solve that problem.
[4340.76 --> 4343.10]  Chris did like most of the work.
[4343.18 --> 4344.26]  I'm just helping.
[4344.84 --> 4346.44]  And, uh, this is great.
[4346.44 --> 4352.12]  And then, uh, I think we were able to get really far with, uh, Phoenix 1.0, Acton 1.0 came out.
[4352.22 --> 4353.42]  Now the community is starting to grow.
[4353.42 --> 4355.96]  We can see more and more companies using Phoenix.
[4356.16 --> 4357.32]  And I'm in the last steps.
[4357.40 --> 4359.60]  I'm working on Acton 2.0 right now.
[4359.72 --> 4363.28]  That's going to, uh, improve based on some of the feedback.
[4363.76 --> 4372.66]  Uh, I'm also working with Chris and Bruce State, uh, on the, uh, programming Phoenix book, which is also going to help with all of those things.
[4372.66 --> 4372.94]  Right.
[4372.94 --> 4377.82]  But the main reason was exactly, you know, I, I, it's just something that we need to use.
[4377.86 --> 4379.46]  And that's what I want to focus on.
[4379.46 --> 4391.48]  And yes, I, I, I kind of knew that if we have that, it's going to, it's going to help with adoption because when you have just the language, you don't have, let's say, a tool to use it with.
[4391.48 --> 4402.32]  And this was actually very interesting because when Phoenix started to become more popular, it started to attract different, let's say, kind of developers that were, they aimed on different things.
[4402.32 --> 4407.48]  Because when you're learning only, only the language, your folks, oh, I want to learn the language and I want to master it.
[4407.48 --> 4413.72]  And when it comes to Phoenix, I will start to, to see more developers that are like, hey, I want to build something.
[4414.48 --> 4422.04]  And, uh, of course, learning the language is part of the process of building something, but it's not my goal on its own, right?
[4422.10 --> 4426.90]  Per se, which is completely fine, but it's just interesting how the dynamics change.
[4427.78 --> 4429.74]  So, yeah, so that's kind of the reason.
[4429.74 --> 4432.74]  I think I maybe possibly answered your question.
[4434.64 --> 4435.52]  No, you did.
[4435.62 --> 4446.24]  I find it somewhat interesting that you say you don't necessarily like to think about it in terms of what you do directly leading or increasing the chances of Elixir's success.
[4446.72 --> 4449.20]  I would expect it to be the exact opposite.
[4449.62 --> 4455.22]  Like, you would, you would want all your efforts to specifically try to advance the chance of Elixir's success.
[4455.32 --> 4457.12]  Maybe it's just not that deliberate.
[4457.12 --> 4461.48]  Um, but that led me to this thought is what does success look like?
[4461.54 --> 4462.16]  I'll tee this up.
[4462.28 --> 4463.26]  We need to take our final break.
[4463.40 --> 4471.70]  And this will give you a chance, Jose, to, to think about the answer is, um, if Elixir is as successful as possible, like, what does that even mean?
[4471.78 --> 4479.90]  What would a success story be five years down the road, 10 years down the road that would make you sit back and say, yes, this was worth it.
[4479.90 --> 4482.28]  This was all that it could possibly have been.
[4482.36 --> 4483.16]  What would success look like?
[4483.24 --> 4484.74]  So we'll talk about that.
[4484.78 --> 4490.34]  And then we'll go back into more of the community stuff after that existential question right after this break.
[4490.34 --> 4505.48]  We're excited to be working with BMC to spread the word about TruSight Pulse, their SaaS-based monitoring service for cloud and server infrastructure that lets you monitor, visualize, and alert with one-second resolution.
[4506.10 --> 4511.96]  I had a chance to talk to Mike Moran, the senior architect, about what real-time monitoring is.
[4512.04 --> 4512.58]  Take a listen.
[4513.28 --> 4515.74]  Real-time obviously means different things to different people.
[4515.74 --> 4517.46]  Well, to us, real-time is one second.
[4517.66 --> 4521.14]  So for us, we have one-second metrics on everything that we collect.
[4521.30 --> 4529.40]  We'll pull all of that, push it to our servers, and you can see it roughly in about four to eight seconds, depending on where that falls in the interval.
[4529.58 --> 4533.72]  So we'll pull one-second data, and within eight seconds, you can see it streaming live on your dashboard.
[4534.06 --> 4538.44]  So during this conversation with Mike, I was trying to figure out what real-time monitoring means to them.
[4538.44 --> 4546.68]  And I was also trying to figure out who might use it and why they would care about one-second resolution timing when it comes to monitoring their infrastructure.
[4547.20 --> 4548.78]  And this is how Mike broke it down for me.
[4549.08 --> 4553.82]  I think at the beginning, you kind of looked at it and went, that's a very niche set of the market.
[4554.04 --> 4559.50]  But I think as things have changed, you can look at e-commerce companies or you can look at anybody who's running an application.
[4559.84 --> 4567.80]  We now have stacks that are very nimble, and we end up with things like restarts that are quick or our stats change very, very quickly now.
[4567.80 --> 4575.76]  So our spikes maybe aren't something that, you know, it's not Black Friday and you end up with this gradual spike or this immediate spike that lasts for a long time.
[4575.94 --> 4582.16]  You now have a lot of things happening because you have so many interconnected systems and you have microservices and dependencies everywhere.
[4582.50 --> 4588.54]  Something happening in one obviously affects other things, but if it's something small or happens very quickly, you don't notice that.
[4589.10 --> 4592.20]  And at this point with Mike, I was like, well, what's a better example?
[4592.20 --> 4605.44]  Give me a real-world example that everyone knows about that can really explain how important it is to have one second near real-time monitoring on infrastructure level stuff.
[4605.50 --> 4608.76]  Stuff that really matters, the heartbeat, so to speak, of an infrastructure.
[4609.02 --> 4610.38]  And this is what he had to say. It's pretty interesting.
[4610.88 --> 4618.14]  If you're looking at your EKG and you're looking at your heartbeat, how many doctors would ever look at your heartbeat at a minute interval or a 15-second interval?
[4618.14 --> 4623.54]  You'd be crazy because you'd miss whatever was happening with your heart and that's something that you wouldn't want to screw with.
[4624.08 --> 4628.74]  Wow. What a great real-world example of what that exactly means.
[4628.88 --> 4630.72]  I don't know about you, but I don't want to mess with my heart.
[4631.46 --> 4633.52]  My heart keeps me going. Your heart keeps you going.
[4633.68 --> 4640.02]  And if you value the heart of your business, the heart of your infrastructure, you're going to care about one-second resolution timing.
[4640.16 --> 4641.70]  You're going to care about real-time monitoring.
[4641.70 --> 4646.58]  And BMC's TrueSight Pulse truly is something you should take a look at.
[4646.86 --> 4654.08]  Head to bmc.com slash TrueSight Pulse, all one word, no hyphens, and tell them the Chingslog sent you.
[4657.38 --> 4660.54]  All right, Jose, before the break, we teed up a question for you.
[4660.56 --> 4661.42]  Kind of a big question.
[4661.70 --> 4665.76]  Look forward and think, what does success look like for Elixir?
[4665.76 --> 4671.18]  What could be, beyond your wildest dreams, a success story for Elixir if you're 5, 10 years down the road?
[4671.70 --> 4672.20]  Right.
[4672.40 --> 4683.36]  So, like, before the break, you said that it was kind of surprising, like, that I didn't associate things, like, to increasing the Elixir adoption, right?
[4684.16 --> 4690.62]  And the reason for that is because it's not generating any expectations, right?
[4690.62 --> 4706.08]  Because if I think, imagine, like, I think something is the correct way to do it, and that doesn't lead to better adoption at the end of the day, I should not couple the two, right?
[4706.08 --> 4710.36]  In the sense that, you know, what's going to validate if something is good or fair in the proper direction?
[4711.52 --> 4722.62]  Adoption is always great, but if the adoption falls because of something, you know, it doesn't imply the cause, and I don't want to associate that in terms of the language building.
[4722.62 --> 4725.16]  And the whole idea of just not having expectations.
[4725.38 --> 4739.22]  So your question, basically, like, of what I see as a success, I don't have really an answer because I try really, really hard to not build any expectation, right?
[4739.22 --> 4758.18]  Like, to not try to think about it and just do what I think is right and what I think makes sense, what is going to make easier to write maintainable and scalable software that we're talking about and keep the developers productive and so on.
[4758.18 --> 4773.78]  So, yeah, so I know that this question in particular, I'm not answering it, but it's kind of on purpose because it's something that I try to stay really far from and try not to get into.
[4774.18 --> 4778.24]  But there are a couple of things that I kind of think like, oh, this would be nice, right?
[4778.58 --> 4784.16]  So, I mean, in five years, what would really be nice if I am still working on Elixir, right?
[4784.16 --> 4787.10]  And there is a community and we are continuing to grow.
[4787.28 --> 4789.26]  That's definitely something nice.
[4789.36 --> 4794.12]  I don't try to think of precise numbers, of precise goals, but I obviously want that, right?
[4794.56 --> 4798.28]  And as I said, I want to continue to increase adoption.
[4798.48 --> 4801.66]  I feel like I don't have it as an end goal per se.
[4802.44 --> 4806.86]  Also, I want to have a diverse community.
[4807.22 --> 4811.30]  So I don't want to be focused like only web, right?
[4811.30 --> 4819.02]  Because we have so much with the Erlang virtual machine and the ecosystem that's already there for building concurrent distributed systems.
[4819.76 --> 4827.24]  And so I really want to build more and more around that and go beyond web, right?
[4827.30 --> 4834.74]  So if you're doing things that are more low level or building distributed systems, I want to see more of that happening.
[4834.74 --> 4845.34]  And I've already seen there are like good talks happening at the Elixir conferences about going more toward the distributed system approach and not necessarily web, which is really interesting.
[4845.46 --> 4847.04]  We can learn a bunch of stuff.
[4847.50 --> 4850.70]  One of the things that we mentioned about Phoenix.
[4850.86 --> 4857.64]  So in Phoenix 1.2, we are going to have a present system that allows you to say, hey, someone came up online.
[4857.64 --> 4863.80]  And the work being done, it's really nice because it's going to be completely distributed.
[4864.36 --> 4869.16]  So we don't need a database to persist your presences.
[4869.46 --> 4876.96]  If you have like three nodes and you put a new node up, the nodes are going to talk with each other and it's going to synchronize the data.
[4877.06 --> 4878.60]  So we have the whole distributed system working.
[4878.74 --> 4880.96]  We have the whole present system working.
[4880.96 --> 4894.10]  If the nodes come down, everyone that's connected to that node is going to come down and that information is going to go across to the other nodes as well and update the presence status, which is, you know, very interesting ways of doing stuff.
[4894.10 --> 4906.06]  And Chris and Alexander that are working on that, they are using, you know, like a bunch of research papers that are from this decade, which are interesting things happening.
[4906.06 --> 4913.10]  And I hope it's going to bring more distributed folks to the language, right?
[4913.14 --> 4915.22]  And help build more on that area.
[4916.06 --> 4918.84]  And that's, so that's kind of my vision that would be really nice.
[4918.92 --> 4925.06]  I know also there are a lot of folks working on embedded Elixir and starting to hear more and more.
[4925.06 --> 4938.20]  There is a fantastic project called the NERVS project that's trying to make it really easy to, you know, to build embedded software and deploy to your hardware or whatever you have.
[4938.84 --> 4940.66]  And I think that's something nice, right?
[4940.74 --> 4944.94]  To go and have a diverse community where I can learn more about embedded.
[4945.12 --> 4946.88]  I can learn more about distributed systems.
[4947.34 --> 4954.48]  One of the things I want to explore for future Elixir versions is something more related to streaming data, right?
[4954.48 --> 4965.66]  So if you have data coming in and you need to process it in different ways and send it out somewhere, we want to make that as efficient as possible, which I hope is going to bring more data oriented folks, right?
[4966.36 --> 4967.24]  And so on.
[4967.24 --> 4970.04]  So that's kind of like my view.
[4970.18 --> 4981.02]  It would be really nice to have really a diverse ecosystem and have like all these different kinds of things happening in the community.
[4983.14 --> 4983.88]  Very good.
[4983.88 --> 4987.96]  You mentioned the presence feature, which sounds totally awesome.
[4988.14 --> 4992.98]  I know something similar specifically to Phoenix is coming down the pipelines with regards to presence.
[4993.26 --> 4997.58]  And we have a bunch of Phoenix and Ecto related questions for you, Jose.
[4997.84 --> 5001.58]  And as we said, talked about in the break, we're running short on time here.
[5001.66 --> 5002.92]  So we're definitely going to get you back.
[5003.40 --> 5006.30]  So listeners, stay tuned for a upcoming show with Jose.
[5006.30 --> 5014.74]  And perhaps we can get Chris on as well to talk specifically about web stuff with regard to Elixir because I'm all for diversity in that community.
[5014.88 --> 5017.58]  And that's an awesome goal for you and one that I hope you achieve.
[5017.58 --> 5022.04]  That being said, the web stuff is very exciting to many of us for sure.
[5022.04 --> 5027.00]  But now let's just close with talking about getting started.
[5028.18 --> 5030.84]  You know, if you have people out there, they're probably excited about Elixir.
[5031.34 --> 5034.18]  Maybe they've dipped their toe in the water, but they got a false start.
[5034.18 --> 5046.22]  Specifically, we had some members in our Slack room talking about getting started from the perspective of somebody who hasn't done functional and is really an object-oriented programmer historically.
[5047.22 --> 5053.94]  And they're wondering what your specific advice is coming from that angle, getting started with Elixir and Phoenix and the whole ecosystem.
[5054.62 --> 5057.76]  What are some ways beyond like, go Google, you know, for things?
[5058.00 --> 5061.96]  Like, what are some really solid ways that people can dip their toe in the language?
[5061.96 --> 5064.80]  One option is to go to the website.
[5065.02 --> 5068.10]  We have a really, really good getting started guide.
[5068.64 --> 5074.12]  And I'm saying that because a lot of people, they tell me that, like, I read the getting started guide.
[5074.22 --> 5074.88]  It was fantastic.
[5075.02 --> 5079.94]  It went for the most important things I need to know and to get started.
[5080.12 --> 5083.42]  So that is a getting started point.
[5083.82 --> 5087.44]  And we have already a bunch of resources available.
[5087.44 --> 5099.58]  So there is a programming Elixir book we talked about from Pragmatic Programmers, which is going to go through the language and cover a bit of the aspects of building systems.
[5099.58 --> 5115.88]  But we also have, let's say, more advanced between quotes, books like Erling, oh, sorry, Elixir and OTP in Action or Elixir in Action from Manning, which is an excellent book that's more focused towards the aspect of building systems.
[5115.88 --> 5121.68]  And it's trying to put you more into the mindset of building systems in Elixir.
[5122.44 --> 5124.50]  So those are very good starting points.
[5124.74 --> 5142.96]  And the question about object-oriented, I would say I wouldn't worry because I, like, the majority, for sure the majority of the Elixir ecosystem came exactly from that background, right?
[5142.96 --> 5150.76]  So, you know, you're going, if you're a stumbling, you're going to find resources or you're going to talk to developers.
[5151.16 --> 5153.48]  So we have a Slack room, if that's more of a thing.
[5153.58 --> 5154.82]  I am particularly on IRC.
[5155.08 --> 5156.30]  We have an excellent channel.
[5156.64 --> 5166.84]  So if you're having troubles not understanding some particular mindset, you can, you know, you can go for the resources at a boat, but you can also hop in one of those channels and ask questions like,
[5166.84 --> 5177.16]  Hey, I'm like, I'm having trouble to let go from some of those particular things, or I'm having trouble to express this particular thing that was, that was easy to express in object-oriented language.
[5177.30 --> 5179.68]  So what is the correct way to do this here?
[5179.82 --> 5181.88]  And we are going to have discussions around it.
[5181.92 --> 5186.16]  And hopefully you will be able to get started and have fun.
[5186.16 --> 5191.66]  So we obviously have some closing questions to this deep dive.
[5191.80 --> 5194.72]  I got to say, I'm really excited that we've had you on the show.
[5195.12 --> 5207.42]  I'm more than thrilled to see your path from beginning programmer to where you're at now with Elixir in this community, this budding website and embedded side and so many opportunities for you.
[5207.42 --> 5215.10]  And I'm glad to see that you're authoring a book and going to be at Strange Loop in 2016 to give that talk on the Erlang VM.
[5216.10 --> 5225.94]  And one thing our guests love to talk about when they come on the show is kind of not just where they came from, but who out there may have influenced them along the way.
[5226.06 --> 5229.58]  So this is a chance for you to kind of mention somebody that's been a hero to you.
[5229.62 --> 5232.70]  So who's a programming hero to you and why?
[5232.70 --> 5235.36]  Sorry, I'll have to.
[5235.92 --> 5239.94]  There was a misunderstanding because I won't be on Strange Loop 2016.
[5240.60 --> 5241.60]  Oh, no.
[5241.68 --> 5244.46]  So that's the talk I gave in 2012.
[5245.52 --> 5248.18]  I was telling you about the background.
[5248.50 --> 5251.00]  Maybe I didn't express myself properly at the time.
[5251.32 --> 5258.04]  Well, we got some issues then because I found a page on Strange Loop 2016 Elixir Modern Programming for Erlang VM.
[5258.16 --> 5259.28]  Was that in 2012 then?
[5260.34 --> 5261.24]  That was 2012.
[5261.24 --> 5262.66]  Well, OK, that's my bad then.
[5262.74 --> 5266.28]  So I saw it on the site and I didn't find it anywhere on their YouTube.
[5266.40 --> 5268.72]  I'm like, OK, he hasn't given this talk yet then.
[5269.02 --> 5272.56]  So I thought I heard you say it was in the past, but I wasn't sure.
[5272.62 --> 5273.20]  We'll leave that in.
[5273.24 --> 5274.00]  We won't edit that out.
[5274.14 --> 5275.86]  We'll just let that blip be there.
[5276.50 --> 5280.20]  And we'll obviously let Jose be the correction there for it.
[5280.26 --> 5284.18]  But nonetheless, besides that, who is your programming hero?
[5284.18 --> 5291.12]  So that's a hard question, but I will go with guys too.
[5292.32 --> 5298.74]  Because so I have he did a lot of work on a bunch of different languages, right?
[5298.84 --> 5310.68]  From all from everything you can think of from like scheme to Java and taking part of, you know, things related to JavaScript, Common Lisp, C and so on.
[5310.68 --> 5317.42]  And so he has been, you know, a great influence on the many languages, right?
[5317.50 --> 5320.20]  That the industry uses as a whole.
[5321.16 --> 5323.34]  And he has great talks.
[5323.34 --> 5331.44]  I like to say, like, my favorite talks of all time is a talk from Geistil on building a language.
[5331.84 --> 5343.34]  And usually when I'm talking about Alexei, I have a quote from that talk that, you know, a language needs to be a pattern for building more languages, which is the reason why I always wanted Alexei to be extensible, right?
[5343.34 --> 5348.28]  Because our field today is so, you know, so wide that the language needs to be accessible.
[5348.42 --> 5352.30]  You need to be able to get it and take it to the domain you are working on.
[5353.12 --> 5355.76]  So, yeah, I would definitely go with Geistil.
[5356.02 --> 5356.54]  Geistil.
[5356.62 --> 5356.96]  All right.
[5357.76 --> 5361.46]  And aside from your hero, what is on your open source radar?
[5361.54 --> 5365.32]  Obviously, you're writing this language Elixir and you're doing so much more around it.
[5365.32 --> 5369.14]  But what else out there is on your radar?
[5369.28 --> 5379.92]  What's out there in the open source world that's got you excited that if you had a free weekend that maybe wasn't Elixir focused or maybe it is, might paint back into the future you sort of described a bit ago?
[5380.12 --> 5381.08]  What's on your open source radar?
[5382.42 --> 5385.24]  So there are two things to that.
[5385.40 --> 5388.22]  So one is the NERRS project I talked about.
[5388.22 --> 5396.12]  It's part of the Elixir link community, but they are doing a great job with everything embedded.
[5396.80 --> 5403.00]  And it's something that I will say, oh, I need to play a bit more and maybe help in any way I can if I can help.
[5403.64 --> 5406.54]  So that's definitely something that is in the radar.
[5406.54 --> 5413.16]  But regarding the whole, you know, like future of Elixir, I said like streaming data.
[5413.50 --> 5419.90]  So I have been following what is happening, you know, with Apache Storm and Apache Spark.
[5420.06 --> 5423.52]  It's things that I am like falling on the side, reading about it.
[5423.92 --> 5425.98]  There's also the Microsoft things project.
[5426.26 --> 5428.44]  It's really interesting.
[5428.72 --> 5432.02]  I've read the papers, but I haven't played with it yet.
[5432.14 --> 5433.28]  Something that I plan to do.
[5433.66 --> 5434.38]  What was the Microsoft thing?
[5434.38 --> 5434.56]  Yeah.
[5435.26 --> 5439.68]  Microsoft Orleans about virtual actors.
[5440.04 --> 5443.68]  So they use that, for example, when deploying Hello.
[5444.74 --> 5452.02]  So the whole idea is that, so today in Elixir, you're kind of like, if you are starting a process that gets a computation,
[5452.22 --> 5455.28]  you need to tell exactly, I want to start this process on this particular node.
[5455.90 --> 5456.36]  Right?
[5456.46 --> 5458.94]  So you always need to get to give that information.
[5458.94 --> 5464.74]  And the idea behind Microsoft Orleans, they call it virtual actors.
[5465.24 --> 5467.14]  So you could think there would be like virtual Elixir process.
[5467.92 --> 5474.46]  So, for example, if you have a Hello game, you would have, and if you just joined in and you want to play on multiplayer, for example,
[5475.02 --> 5476.82]  you would send a request to their cluster.
[5476.82 --> 5483.12]  And the cluster would start like a process for you, like similar to the Elixir process, but anywhere in the cluster.
[5483.12 --> 5485.38]  You don't say, I want this thing here.
[5485.50 --> 5486.44]  I want this thing there.
[5486.62 --> 5488.44]  They take care of that for you.
[5488.78 --> 5489.14]  Right?
[5489.14 --> 5497.76]  Which means that if you are not worried about location, for example, if you're having high loads,
[5498.06 --> 5499.88]  what you can do is that you can plug more machines.
[5500.20 --> 5504.50]  And because you don't really care where that particular process is, you can move it around.
[5504.64 --> 5504.74]  Right?
[5504.78 --> 5510.62]  So you can say, okay, I'm going to move this from this machine because this machine is having a spike right now and cannot handle the load.
[5510.62 --> 5520.14]  So it has a bunch of interesting ideas in there regarding virtual actors and process placement in a cluster, which would be nice to explore.
[5520.66 --> 5521.44]  Very cool.
[5522.38 --> 5525.52]  Well, like I said, it's been a blast having you on the show.
[5525.70 --> 5533.40]  I know we've kind of teed up a tease of a potential, I guess, take two on this to get you back on.
[5533.44 --> 5536.26]  And also, Chris, talk deeper about the website of Elixir.
[5536.66 --> 5539.36]  So if you're listening to this, stay tuned to that.
[5539.36 --> 5541.98]  We also have a bunch of great shows in the schedule coming up.
[5542.40 --> 5547.50]  Free Code Camp with Quincy Larson, Tiddly Wiki with Jeremy Ruffston, and a big one for us.
[5547.54 --> 5550.82]  We're excited about the future of WordPress and Calypso with Matt Mollewig.
[5551.20 --> 5552.90]  So those are some upcoming shows for us.
[5553.12 --> 5561.22]  But, Jose, before we close out the show, anything else you want to mention about Elixir, about anything we've talked about today before we close out the show?
[5562.56 --> 5564.50]  I just want to thank you for having me.
[5564.66 --> 5565.94]  It was really fun.
[5565.94 --> 5571.58]  And if you heard the podcast, go give Elixir a try.
[5571.70 --> 5572.64]  We talked about it.
[5573.06 --> 5574.40]  And try to join the community.
[5574.60 --> 5575.72]  There are a bunch of ways.
[5576.22 --> 5584.48]  But if meetups are getting, you know, like with other developers more of a thing, use that to subscribe to the Elixir Raider.
[5584.48 --> 5590.76]  Do that because we have a meetup section that is telling all the meetups that are happening with Elixir around the world.
[5590.84 --> 5592.70]  And then you can find something close to you that you can go.
[5593.16 --> 5595.58]  But there's also a bunch of conferences coming up.
[5595.82 --> 5599.52]  We're going to have Elixir Days in Florida.
[5599.52 --> 5604.48]  We are going to have Elixir Conference in Europe here in Berlin around May.
[5604.96 --> 5607.92]  And the Elixir Days in Florida is March, if I'm not wrong.
[5608.44 --> 5614.16]  And we also have Elixir Conference in the United States about August, September in Florida as well.
[5614.68 --> 5617.40]  So, you know, come and be part of the community.
[5618.24 --> 5620.12]  Yeah, a lot of stuff coming up for you then.
[5620.38 --> 5621.66]  Yeah, that sounds really good.
[5621.72 --> 5624.72]  So we'll make sure we link to a lot of things here.
[5624.88 --> 5630.34]  Definitely the newsletter you mentioned, back to the intro to the site, a lot of links in our show notes.
[5630.44 --> 5631.98]  So this is episode 194.
[5632.24 --> 5635.58]  So if you're listening to this, go to changelog.com slash 194.
[5636.36 --> 5638.20]  Or if you're using a podcast app, check your show notes.
[5638.30 --> 5639.70]  There's all the links in there.
[5639.70 --> 5640.20]  Don't wreck.
[5640.36 --> 5641.90]  Don't pull over and try and write it down.
[5642.36 --> 5644.44]  We'll just use the show notes for that.
[5644.70 --> 5647.24]  But, Jose, it was awesome to have you on the show.
[5647.24 --> 5654.26]  But today I want to give a special thanks to you for taking the time to be in the nighttime because, you know, we're in different time zones.
[5654.36 --> 5657.44]  So you had to really work hard to work the scheduling out with us.
[5657.50 --> 5658.38]  We appreciate that.
[5659.04 --> 5661.16]  And to those listening, thank you so much for listening.
[5661.28 --> 5666.66]  And to the sponsors, TopTile and Node, Rollbar, and also Truesight Pulse, thank you for supporting the show.
[5667.30 --> 5668.92]  But, fellas, that's it for this show.
[5669.02 --> 5670.30]  So let's say goodbye.
[5670.94 --> 5671.26]  Goodbye.
[5671.38 --> 5671.80]  Thanks, Jose.
[5672.48 --> 5672.84]  Bye.
[5672.94 --> 5673.30]  Thank you.
[5677.24 --> 5678.24]  Bye.
[5678.30 --> 5678.76]  Bye.
[5678.76 --> 5679.14]  Bye.
[5679.24 --> 5679.30]  Bye.
[5680.42 --> 5681.10]  Bye.
[5696.88 --> 5699.04]  Bye.
[5699.26 --> 5699.72]  Bye.
[5699.80 --> 5700.14]  Bye.
[5702.42 --> 5704.88]  Bye.

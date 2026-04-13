[0.00 --> 13.68]  Welcome back everyone, this is the Change Log, where a member-supported blog, podcast,
[13.68 --> 18.62]  and weekly email covering what's fresh and what's new in open source.
[18.62 --> 24.50]  Check out the blog at thechangelog.com, our past shows at 5by5.tv slash changelog, and
[24.50 --> 28.70]  subscribe to the Change Log Weekly, that's our weekly email we send out covering everything
[28.70 --> 32.76]  it hits our open source radar, you don't want to miss it, subscribe at thechangelog.com
[32.76 --> 33.46]  slash weekly.
[33.98 --> 38.28]  And you're listening to episode 118, and John Long is joining me to talk about SaaS, the
[38.28 --> 45.26]  SaaS way, the SaaSway.com by the way, open publishing on GitHub, Middleman, Serve, and
[45.26 --> 47.80]  a bunch of cool topics, we had a fun conversation.
[48.76 --> 53.00]  Today's show is sponsored by DigitalOcean, FreshBooks, and TopTile, we'll tell you a bit
[53.00 --> 57.10]  more about FreshBooks later in the show, and also TopTile as well, but DigitalOcean, we're
[57.10 --> 60.24]  hosting on DigitalOcean, we've been working with DigitalOcean for several months now, they're
[60.24 --> 64.68]  a partner of ours, and they're a simple cloud hosting provider that's dedicated to offering
[64.68 --> 67.30]  the most intuitive ways to spin up a cloud server.
[68.00 --> 74.30]  In literally 55 seconds, you can have a full-on server created with root access, and you're
[74.30 --> 75.00]  off to the races.
[75.18 --> 77.30]  It just doesn't get any easier than that, really.
[77.86 --> 83.44]  Pricing plans start affordably at $5 a month for half a gig of RAM, 20 gigs of drive space,
[83.44 --> 88.92]  that's SSD drive space, by the way, one CPU, one terabyte of transfer, and if you only
[88.92 --> 92.26]  need the server for a little bit, for a couple hours, or for a couple days, or for a week,
[92.52 --> 97.60]  they even have it where you can rent by the hour, basically, and it costs just .007 of a
[97.60 --> 100.76]  cent an hour, that's less than a penny an hour, super affordable.
[101.44 --> 105.88]  We've got a special promo code just for our listeners, use the promo code CHANGELOGAPRIL
[105.88 --> 107.78]  to get a $10 credit when you sign up.
[108.08 --> 109.78]  Head to DigitalOcean.com to get started.
[110.18 --> 111.38]  And now, on to the show.
[111.38 --> 116.64]  So, we're joined today by my good friend, John Long.
[116.76 --> 122.74]  John, we, I guess this show is kind of funny because I wanted to have you back on the show.
[122.80 --> 126.84]  This is not your first time on the changelog, so it's kind of like, welcome back too, right?
[127.40 --> 127.70]  Yeah.
[128.50 --> 131.66]  I think the last time we were on here, I was talking about Radiant.
[131.96 --> 132.14]  Yeah.
[132.76 --> 134.62]  So, it was a long time ago.
[134.78 --> 135.72]  It was a long time ago.
[135.72 --> 142.18]  And the funny part is, is that, I gotta say, like, what, three years ago now we started
[142.18 --> 142.94]  the SaaS way?
[143.36 --> 144.58]  The blog, the SaaS way?
[145.06 --> 145.34]  Yeah.
[145.54 --> 146.30]  Was it three years ago?
[147.62 --> 151.28]  It's, it's getting to the point where it's hard for me to remember how long ago it was.
[151.84 --> 152.44]  It's...
[152.44 --> 153.68]  I think it is right around three.
[153.94 --> 154.24]  Yeah.
[154.24 --> 156.82]  It's so crazy to think like three years ago, though.
[156.88 --> 158.36]  It's, I don't even know.
[158.56 --> 160.10]  But, yeah.
[160.36 --> 164.72]  So, I wanted to have you back on the show, one, because you're pretty awesome.
[164.82 --> 168.68]  And two, we've got this kind of, I guess, somewhat of a new announcement.
[168.82 --> 171.60]  It's been about two weeks or three weeks now since we've had this out there.
[171.70 --> 178.38]  But the SaaS way, just to kind of fill everybody in, the SaaSway.com is a blog John and I started
[178.38 --> 181.80]  together maybe, we're saying roughly three years ago.
[181.80 --> 184.80]  We'll figure out the exact mark there, but...
[184.80 --> 185.94]  Looks like it was 2011.
[186.50 --> 186.90]  Was it?
[187.26 --> 187.50]  Yeah.
[187.82 --> 191.06]  So, yeah, it was like around, I guess, yeah, July, August, 2011.
[192.32 --> 192.34]  Yeah.
[192.34 --> 193.20]  Yeah, so we're coming up.
[193.42 --> 194.66]  So, roughly three years.
[194.74 --> 196.36]  Yeah, just, just shy.
[196.62 --> 202.70]  But, so we started this blog because we were super passionate about writing CSS the SaaS way.
[203.50 --> 208.10]  And, and so we wanted to, like, be the SaaS jerk, so to speak.
[208.10 --> 213.00]  We wanted to be that, that person to, like, tell the world about SaaS and compare it to,
[213.46 --> 219.80]  you know, various ways you can do it with CSS, but make your code more readable or use mix-ins
[219.80 --> 221.28]  or use libraries and all this fun stuff.
[221.34 --> 224.60]  So we wanted to share our, our great fun stuff with the SaaS way.
[224.60 --> 231.46]  And, uh, you had a project called SaaS Watch that you started with Brandon Mathis, who's
[231.46 --> 235.58]  also a core contributor to Compass, works at, uh, Mongo HQ.
[235.80 --> 239.56]  And he's pretty well known actually for Octopress, right?
[240.36 --> 240.54]  Yeah.
[241.70 --> 244.60]  Although I'm not sure, I'm not sure if Brandon was involved.
[244.70 --> 250.68]  I know I had asked him, uh, at one point if he would be interested in being a part of it,
[250.68 --> 252.74]  but he's, he's a busy guy.
[253.04 --> 255.92]  Uh, and I didn't get a whole lot of traction on that.
[256.08 --> 261.16]  Um, I think I was doing that for, it wasn't long.
[261.22 --> 264.70]  It was actually just a month or so by the time you contacted me.
[264.70 --> 265.06]  Ah, okay.
[265.60 --> 265.94]  Yeah.
[266.98 --> 271.40]  Well, before, uh, I guess unless we assume somebody went back and listened to, I'm not
[271.40 --> 275.38]  even sure what the episode was that you were on before that we gave you your other intro
[275.38 --> 280.86]  here on the change law, but, uh, for those who may not know who John W. Long is, who, uh,
[280.86 --> 281.54]  who are you, John?
[282.90 --> 288.40]  Uh, so I'm, uh, I, I'm a user interface designer.
[288.40 --> 291.78]  Uh, I work for, uh, user voice.
[292.10 --> 296.68]  Uh, we make, uh, help desk and feedback software.
[297.96 --> 301.50]  Um, yeah, I live in Cary, North Carolina.
[301.50 --> 304.20]  Uh, work in Raleigh, North Carolina.
[304.96 --> 306.50]  Um, yeah.
[306.98 --> 309.88]  Past accomplishments is Radiant CMS and.
[310.60 --> 310.94]  Yeah.
[311.16 --> 319.68]  I was the creator of Radiant CMS and, uh, I also serve, um, yeah, a number of open source
[319.68 --> 322.10]  projects, um, on GitHub.
[322.60 --> 323.04]  Yeah.
[323.04 --> 332.46]  Are you still, uh, involved with, um, with Ruby Lang and the, I guess the site at least?
[333.12 --> 333.50]  You know what?
[333.56 --> 337.20]  That has seemed, it seems like it's, uh, picked up traction.
[337.32 --> 341.92]  They moved away from Radiant at a certain point and, um, I've just been happy to see that
[341.92 --> 346.72]  other people care about that site and are maintaining it, uh, which is great.
[346.88 --> 348.68]  Are you still involved in Radiant then or no?
[348.68 --> 348.76]  Yeah.
[350.02 --> 357.12]  Um, uh, I guess officially I still am, but unofficially I haven't been involved with the project for
[357.12 --> 357.72]  a long time.
[358.00 --> 358.20]  Hmm.
[358.50 --> 358.68]  Okay.
[358.82 --> 359.00]  Yeah.
[360.24 --> 361.36]  How do you feel about that?
[361.42 --> 362.84]  You're pretty happy or just whatever?
[363.64 --> 368.66]  Um, I mean, I still have a lot of things that I would love to see Radiant be able to do.
[369.02 --> 376.50]  Um, but honestly, most of the stuff that I work on nowadays, I'm very content to use a
[376.50 --> 377.60]  static site generator.
[378.46 --> 383.00]  Um, I mean, having the site in a database, unless you're working with like multiple people
[383.00 --> 385.86]  or, uh, it's kind of a drag.
[386.06 --> 386.24]  Yeah.
[386.24 --> 386.58]  It's great.
[386.58 --> 394.28]  It's great to be able to check stuff into Git and, um, you know, and even deploy, uh, through
[394.28 --> 396.44]  Git on like Heroku or something like that.
[396.44 --> 402.36]  Um, so, um, yeah, I mean, I would love to update it.
[402.58 --> 407.20]  Uh, there was a lot of work that went into it when we went, when I first worked on it,
[407.56 --> 408.10]  pushed it out.
[408.16 --> 411.00]  I think there was, I worked on it like eight months, almost solid.
[412.00 --> 417.54]  Um, and I just don't have that kind of time to devote to it anymore.
[417.54 --> 425.82]  Um, at this point, uh, Jim Gay, uh, shout out to him, uh, Saturn Flyer on, on Twitter.
[426.44 --> 433.64]  Uh, has been maintaining Radiant for a number of years and has done a great job, uh, at it.
[433.72 --> 438.30]  So I'm very content to let him lead the, lead the charge with that.
[438.30 --> 446.60]  And Jim, um, actually runs kind of a consult, a web consultancy and is building sites every
[446.60 --> 447.74]  day with Radiant CMS.
[448.28 --> 453.54]  So I think he's the right guy to, um, to work on it.
[453.54 --> 459.60]  I think one of the things that was hard for me was after I created Radiant, um, I ended
[459.60 --> 464.56]  up not do, not building a lot of content oriented websites.
[464.56 --> 468.54]  Instead, I, my career sort of went towards web applications.
[468.54 --> 469.82]  It's kind of funny how that works out, right?
[470.34 --> 471.34]  Applications in general.
[471.34 --> 476.64]  And so, yeah, there's times when I feel like I'm kind of isolated for that problem space.
[476.64 --> 480.88]  Um, you know, I, I don't understand it as well.
[481.02 --> 481.26]  Yeah.
[482.36 --> 485.78]  What's a good tee up for what we've done with the SAS with us.
[485.78 --> 494.00]  The SAS way started out as a, as a Nesta CMS, which is a Ruby, um, file based, I guess is
[494.00 --> 496.58]  the probably easiest way to say it is a static site.
[496.58 --> 501.70]  Uh, I don't think Nesta has, I think it might have that feature, but it's not, it's not
[501.70 --> 503.40]  meant to be a generator.
[503.54 --> 507.48]  It's meant to be basically a flat file based CMS written in Ruby.
[508.04 --> 508.44]  Right.
[508.90 --> 512.10]  Um, and that was a great project.
[512.18 --> 513.76]  It's, it's what helped lift it off the ground.
[513.86 --> 518.82]  You know, we, you and I were able to easily, uh, tee that up pretty quickly.
[518.82 --> 523.92]  We did deploy to Heroku's, you know, super fast cause we took, you know, we took advantage
[523.92 --> 528.28]  of like varnish and caching and other things that Heroku provides and all the other things
[528.28 --> 532.30]  that just a, a flat file system kind of CMS provides.
[532.30 --> 538.36]  But, um, here about three weeks ago, we took this turn to, to finally, I mean, like we said,
[538.40 --> 543.88]  the site's been out there for almost, almost three years and we, our original model was
[543.88 --> 550.48]  kind of to, you know, go out to the SAS world and sort of recruit those that were, uh, for
[550.48 --> 555.04]  lack of better terms, movers and shakers, people that were sharing, you know, their knowledge
[555.04 --> 558.96]  with the SAS community on how to best write CSS the SAS way.
[560.08 --> 565.40]  And, uh, you and I talked, I would say probably like eight months ago about open sourcing the
[565.40 --> 570.36]  SAS way and oddly enough, and I'll come clean, but I felt a little apprehensive about doing it.
[570.38 --> 573.86]  I don't know why, but, uh, I'm really glad you forced us to do it.
[573.88 --> 580.38]  Because I think it's really a much better fit for, um, for the content the way it is.
[580.38 --> 586.30]  So why don't, why don't you share with the listeners why you feel passionate about how the
[586.30 --> 592.30]  SAS way meets up with this get flow, kind of check your content into get kind of mentality,
[592.38 --> 595.30]  this sort of open publishing way of, of doing things.
[595.30 --> 597.12]  Yeah.
[597.22 --> 604.30]  I, um, I mean, I think part of it for me, uh, has just been over the last couple of years
[604.30 --> 609.60]  getting more and more familiar with the way GitHub works with, uh, pull requests and all
[609.60 --> 609.92]  that.
[610.00 --> 615.48]  Um, I mean, we were passionate users of get at user voice and probably about every other
[615.48 --> 616.60]  company these days.
[616.60 --> 624.86]  And that, uh, that workflow of just being able to work on a change, push it into a branch,
[624.86 --> 632.10]  uh, ask for people to review it, comment on it, whatever merge, uh, just seems ideal for,
[632.10 --> 637.44]  uh, you know, building text-based documents.
[637.44 --> 646.84]  I guess you could say, um, I, you know, what, one aspect of it too is where a blog about HTML,
[646.84 --> 652.46]  um, and CSS and, um, you know, SAS.
[652.46 --> 663.28]  And so like having the ability to quickly drop in and write, write that kind of code alongside
[663.28 --> 666.56]  writing code for an article, uh, is pretty awesome.
[667.52 --> 676.72]  Um, so I, I mean, in general, the fact that it is a, uh, uh, static file based content management
[676.72 --> 680.10]  system, uh, it's all checked in on there on GitHub.
[680.42 --> 686.20]  It means it's a lot easier for people to come alongside and submit new articles.
[686.88 --> 692.66]  Um, also, uh, make changes, fix things on the site if it's not displaying correctly.
[693.28 --> 699.62]  Um, and really, I think that the big thing that I love about this is, is that we've reversed
[699.62 --> 705.90]  the, um, trying to go out and recruit people kind of scenario, which we still try and recruit
[705.90 --> 712.72]  people to write stuff on the SAS way to, to it, it being also something where people can
[712.72 --> 716.90]  come to us and say, Hey, I have an article idea, an idea for this article.
[717.32 --> 718.22]  What would you think?
[718.26 --> 722.68]  And then they fork the repository, they write it up and send us a pull request.
[722.68 --> 731.60]  And, um, you know, we, we've had, uh, two articles, I guess, since we, uh, opened it up this
[731.60 --> 731.94]  way.
[731.94 --> 740.10]  And, uh, it, uh, you know, these are from people that we didn't know about and, um, they've
[740.10 --> 745.98]  worked out to be fantastic articles for us filling, you know, some holes, uh, in, in what
[745.98 --> 746.32]  we had.
[746.32 --> 750.52]  And so one of the things that I've struggled with too, is, is that sometimes you really
[750.52 --> 756.72]  need an article on a topic, but one of your go-to people, I guess, is not like, doesn't
[756.72 --> 757.98]  really want to write about that.
[757.98 --> 769.76]  Um, and so really freeing up, uh, just for anybody to be able to contribute to it has
[769.76 --> 772.54]  been, I think a very good thing for the SAS way.
[772.90 --> 772.96]  Yeah.
[773.08 --> 779.86]  I mean, considering that SAS and compass, um, and I guess the SAS world is, is known to be,
[779.86 --> 782.04]  you know, it's their open source technologies.
[782.04 --> 788.16]  Anyways, it would make sense to, and this is why I said, I self-admitted that, uh, that
[788.16 --> 789.74]  I was sort of the bottleneck.
[789.74 --> 793.70]  I mean, it's kind of funny too, that the fact that, you know, I helped lead the changelog
[793.70 --> 797.84]  who, uh, you know, focuses on, uh, what's fresh and new and open source.
[797.84 --> 802.36]  And here I am being a little apprehensive about opening up this publishing flow just because
[802.36 --> 804.30]  I think part of me doesn't want to lose control.
[804.30 --> 808.82]  But then I, I learned something along this path that I realized that wasn't really control
[808.82 --> 810.74]  we were trying to achieve.
[810.74 --> 812.98]  It was, it was really, uh, openness.
[812.98 --> 819.10]  And I think the last probably, you know, a few weeks I've really changed my, uh, idea
[819.10 --> 824.94]  because I've been closely involved in this project being open source and kind of, um, helping
[824.94 --> 827.34]  curate this content and manage it.
[827.34 --> 831.54]  It's, it's, I can see now the light, so to speak.
[831.90 --> 832.42]  Yeah.
[832.54 --> 833.62]  By having it open.
[833.70 --> 838.24]  So like you said, it's, it's really easy for someone to, to forth a repository and, you
[838.24 --> 841.24]  know, don't worry about messing up.
[841.30 --> 842.88]  There is no such thing as messing up.
[842.92 --> 846.04]  And, you know, they, they sent us an idea and worst case scenario, we helped them evolve
[846.04 --> 849.84]  that idea of an article, um, into something even better.
[849.84 --> 854.10]  And that helps lift up the, uh, you know, the SAS community.
[854.10 --> 859.76]  And like you'd mentioned having a certain topic to kind of write upon, we don't always have
[859.76 --> 864.10]  a go-to person, uh, on the team already to, to kind of write one of those.
[864.10 --> 865.98]  And somebody can bring that idea to us.
[866.08 --> 868.22]  And it's, uh, it's a lot easier.
[868.22 --> 873.60]  And we've, I like the way to also how we've kind of dissected the SAS ways content.
[873.76 --> 879.52]  You got a, you got beginner, which makes sense because not everybody is, uh, is, you know,
[879.52 --> 884.94]  a SAS guru, so to speak, you know, no one really has an expertise and not everybody has
[884.94 --> 889.06]  an expertise level and then you got intermediate and then you got advanced and that's fit pretty
[889.06 --> 889.44]  well too.
[889.50 --> 895.16]  Can you speak to maybe how that's played into helping, um, the community kind of, uh, with
[895.16 --> 898.48]  training will, so to speak, get to mastery with, with SAS?
[899.42 --> 909.46]  Well, I mean, I, the best way to kind of answer that in my opinion is, is that I, you know,
[909.46 --> 916.40]  I've, I've been using SAS for a number of years and, um, I know it pretty well backwards
[916.40 --> 922.54]  and forwards, but even, even so, for some reason, I can never remember the syntax for
[922.54 --> 924.16]  like how to write a for loop in SAS.
[925.20 --> 927.34]  And it's the funniest thing.
[927.34 --> 927.64]  Wait, hang on.
[927.82 --> 930.84]  Do you go back to the article then and every, and keep refreshing yourself?
[930.84 --> 935.96]  So the funniest thing is, is that like, I'll just type it into Google, like for loop SAS.
[935.96 --> 942.22]  And like the first thing that comes up as an article on this SAS way, um, on how to write,
[942.30 --> 945.48]  you know, for loops and if statements and things like that.
[945.48 --> 953.96]  And so I really see us, um, and I, I think we've kind of gone back and forth a little bit
[953.96 --> 960.92]  about, you know, are we a news organization or are we, um, you know, are, are we trying to
[960.92 --> 963.12]  stay sort of current in the things that we're writing about?
[963.12 --> 969.44]  Um, I mean, normally like with a blog, it's like this progressive, uh, series of ideas
[969.44 --> 974.38]  that, you know, you're blogging about, but the SAS way has really become much more the
[974.38 --> 983.22]  website about, uh, tutorials and the best tutorials, um, that you can find on SAS, uh, for the most
[983.22 --> 986.42]  part are curated and kept here on the SAS way.
[986.42 --> 993.56]  Um, so I, I definitely see it as like, I feel like the service that we're providing in the SAS
[993.56 --> 1001.44]  community is just that easy onboarding and like understanding how to, um, to use SAS, how to
[1001.44 --> 1006.68]  structure your SAS projects, all of that kind of stuff where we're trying to write about it to help
[1006.68 --> 1015.02]  and assist you. And so for a number of the, just getting started sort of topics, um, I think we're,
[1015.14 --> 1023.54]  we've, we've been a great strength to the SAS community and, and that regard, um, making it so
[1023.54 --> 1028.80]  much easier for people to get, get on board. So that's where kind of, I would see the beginner stuff.
[1028.80 --> 1034.58]  Um, in particular, um, we just had one of the articles that was contributed was on,
[1034.66 --> 1043.24]  you know, choosing great variable names. Um, and in some ways it's a really simple article.
[1044.14 --> 1051.48]  Um, but he's pointing out, uh, that this guy, Frank from South Africa is just pointing out that,
[1051.48 --> 1058.78]  um, you know, naming variables like red and blue and green,
[1058.78 --> 1066.80]  and things like that. And using those throughout your code, uh, isn't a good idea. Um, instead
[1066.80 --> 1072.26]  using variable names like brand color or accent color, or trying to think of the semantic sort of
[1072.26 --> 1081.10]  value that you're capturing there, um, is helpful. And while for somebody who's been writing code for a
[1081.10 --> 1091.26]  long time, that might seem, um, just so obvious that you should, you know, choose good variable names
[1091.26 --> 1096.34]  for people that the thing that we have to remember is, is that a lot of people that are using SAS are
[1096.34 --> 1103.32]  people that have come to it from the design world, not the coding world. And they, they need tips on
[1103.32 --> 1111.52]  like how to code well. And, um, so yeah, I, I'm, I think I've kind of gotten off track here, but
[1111.52 --> 1115.12]  I feel you though. And, you know, what, I think the point you're making there that's really
[1115.12 --> 1119.56]  important is that, um, is that while that particular article you're talking about from,
[1119.56 --> 1125.30]  from Frank is, uh, seems simplistic, it's the obvious sometimes that I think we serve the SAS
[1125.30 --> 1131.64]  community because yeah, sure. It, it makes sense that, you know, the variables should be,
[1131.64 --> 1135.54]  you know, should have semantic names and they should make sense, but not everybody really
[1135.54 --> 1140.10]  understands that. And it's, I think it almost feels like a position that the community blesses.
[1140.10 --> 1144.54]  Like this is a community guideline for lack of better terms. And because it ends up on the SAS way
[1144.54 --> 1150.18]  and makes it through this open publishing model where everyone who watches and stars, the repo kind
[1150.18 --> 1154.84]  of gets these updates. Like there's a new issue, there's a new pull request. There's some dialogue
[1154.84 --> 1159.90]  happening about this particular article. And it gets through this system that even though it's an obvious
[1159.90 --> 1165.60]  idea, choosing great variable names. Sure. That is obvious, but I think the way of Frank and even
[1165.60 --> 1172.90]  the comment you left today pointing back to Gina's, uh, style guide for SAS slang, you know, that's,
[1173.00 --> 1178.82]  that's remarkable. Like, you know, she's got all these different colors identified and they're not like
[1178.82 --> 1185.88]  slightly pink and a little bit more pink. It's like hot bush and bouquet and Venus, you know,
[1185.88 --> 1189.82]  they're not, they got like cool names and you know, I think that makes sense.
[1191.66 --> 1199.56]  Yeah. And then she uses those colors. She assigns them to, uh, like text colors and, um, accent colors
[1199.56 --> 1208.54]  and background colors. Um, yeah. Yeah. I mean, I, I say, I would see us as kind of a jumping off point
[1208.54 --> 1214.30]  to kind of discuss best practices and how, how they're implemented. There's been a number of articles
[1214.30 --> 1221.66]  where the way that I finished it up is just, Hey, go check out these other repositories, right? You
[1221.66 --> 1227.34]  know, go look at what compass does, go look at, at these other projects, Octopress and other things
[1227.34 --> 1235.06]  to see how you structure your SAS projects or, or other things like that. So some of it, um, you know,
[1235.06 --> 1240.70]  I knew, uh, SAS community has been really blessed with some very talented people working on the, uh,
[1240.70 --> 1249.98]  the SAS, uh, laying website. Um, but, uh, a lot of where they're at right now is just kind of
[1249.98 --> 1257.34]  informational. Um, you know, just trying to help people download and get started with SAS kind of
[1257.34 --> 1268.10]  thing. Um, whereas I think we've, the SAS way is more about that conversation and, um, you know,
[1268.10 --> 1274.50]  how do you use SAS in your everyday life kind of thing. Um, so yeah. Well, back someone asked me,
[1274.50 --> 1280.38]  I can't recall who it was, but somebody said, well, well, this, you know, SAS has good documentation
[1280.38 --> 1285.82]  and so does compass. Why are you guys creating this blog? Like, what's the point? And I'm like,
[1285.82 --> 1290.16]  well, not everybody wants to go and read documentation. I mean, documentation is great.
[1290.16 --> 1296.46]  You need it. It works, but to get started, somebody doesn't go always to the docs and say,
[1296.56 --> 1302.18]  okay, let me just get lost in there. You kind of need this guide. And I feel like what we've done
[1302.18 --> 1305.68]  with the SAS way and what we try to do, at least when we invite people to do, and the reason why
[1305.68 --> 1311.74]  we've open sourced it to, to invite everyone to fork it and submit their article and pull request
[1311.74 --> 1318.62]  is that, uh, you know, going to the docs and reading those isn't always an easy way to get started
[1318.62 --> 1324.62]  or an easy way to reach mastery or to know that, you know, there's a better way to do variable
[1324.62 --> 1329.40]  naming. Uh, sometimes you need somebody from the community to kind of guide you through that.
[1329.44 --> 1334.84]  And that's, that's sort of like, you know, the documentations serves that, but it's, it's a
[1334.84 --> 1340.50]  little dry, you know, whereas we kind of bring it to life. We bring it to life. And, um, I think we
[1340.50 --> 1347.58]  kind of show like how you practically use something. So like to give you an example, um, I wrote an article
[1347.58 --> 1354.98]  a couple of months ago about, um, mix-ins for semi-transparent colors. Um, and you know,
[1354.98 --> 1363.16]  how do you provide like browser fallbacks? Not all browsers support RGBA colors. Um, and
[1363.16 --> 1370.50]  since they don't like particularly internet support eight, like how can you use SAS to make your life
[1370.50 --> 1378.14]  easier, um, with calculating two sets of colors for those attributes? And so that's what that article
[1378.14 --> 1385.44]  is about. But what you're introduced to is, well, functions like the RGBA. Um, you're also introduced
[1385.44 --> 1391.58]  to mix-ins, uh, in the course of the article and you're like seeing like how, you know, these are
[1391.58 --> 1396.82]  developed, what the thought processes are, are, are behind that. And you might come across something
[1396.82 --> 1404.56]  like default attributes or something like that, that you didn't know about before. Um, so I think
[1404.56 --> 1412.90]  a lot of what we do is sort of a community awareness kind of thing. Uh, just encouraging people to talk
[1412.90 --> 1419.62]  about and think about SAS and how they're using it, um, in that regard and sort of learn, you're not
[1419.62 --> 1426.24]  going to read documentation from page one to, to the end kind of thing. Right. Um, instead you're going to
[1426.24 --> 1432.38]  pick up and try and use what you have and sometimes you don't realize there are, you know, better ways
[1432.38 --> 1440.40]  to do that. So, um, by giving these practical articles, people are able to, um, you know, jump
[1440.40 --> 1445.46]  in and see how someone else is doing something and, um, learn from that. So.
[1446.60 --> 1450.52]  Let's pause the show for just a minute and give a shout out to our sponsor, TopTile. For those of you
[1450.52 --> 1455.76]  out there who are freelancing, or maybe you'd like to freelance or even kind of try out a freelance,
[1455.76 --> 1459.94]  like project where you're maintaining your full-time position, you have to check out TopTile.
[1460.36 --> 1466.86]  TopTile is a new rapidly growing network of some of the most elite engineers in the world. They're
[1466.86 --> 1472.96]  distributed all across the globe. Their primary focus is connecting their ecosystem of top engineers
[1472.96 --> 1480.50]  and top companies. You work on special projects with companies like Airbnb, IDO, Zendesk, and many
[1480.50 --> 1487.16]  others. You can work remotely on a beach or anywhere in the world. Uh, to get started,
[1487.28 --> 1493.90]  head to TopTile.com slash developer and click join TopTile. That's a nice big old green button.
[1494.00 --> 1502.96]  You cannot miss it. That's T-O-P-T-A-L.com slash developer. Let's talk about the, the process of
[1502.96 --> 1509.48]  taking the SaaS way and making it open source. What, uh, you know, I know that I did the original
[1509.48 --> 1516.64]  design and then the second, uh, the second redo, I guess, is, uh, it's pretty much all you, like you,
[1517.20 --> 1523.22]  um, took the old repo, pulled all the content out, moved us to middleman and a bunch of other fun
[1523.22 --> 1529.08]  stuff. You used SaaS, I'm sure, behind the scenes to, you know, write the styles. Did you use a framework?
[1529.08 --> 1532.90]  You know, what was the process of like redesigning and then going open source?
[1535.32 --> 1543.84]  Yeah. So we, I mean, we had a number of reasons, uh, to redesign. One was that the, um, we really
[1543.84 --> 1552.06]  wanted to update the logo and sort of the feel of the site. Um, SaaS had had the, um, the woman on
[1552.06 --> 1557.24]  the phone, right? Um, the sassy lady with the phone in her hand, the sassy lady with the phone in her
[1557.24 --> 1568.52]  hand. And, um, funny story about that. The, um, with the SaaS website, they redesigned the logo.
[1568.96 --> 1573.78]  Um, and we wanted to update our branding to kind of reflect that. So that, that was part of what
[1573.78 --> 1585.34]  motivated, um, me sort of getting in, rethinking the design. Um, I think, you know, from a higher
[1585.34 --> 1590.74]  level, I was also interested in just kind of simplifying some of the things, um, we wanted
[1590.74 --> 1596.36]  the site to be more responsive. One of the things that I'm learning more and more of is, is that a
[1596.36 --> 1600.40]  lot of times people are reading these things on the go, whether you're, you know, for sure,
[1601.00 --> 1607.14]  whether you're on the bus or, you know, frankly on the toilet at work, you know, you're pulling it up
[1607.14 --> 1611.28]  on your phone and you're looking at it and you're reading your Twitter stream.
[1611.28 --> 1613.96]  Why do they gotta be at work while they're on the toilet? Why, why at work?
[1614.66 --> 1617.20]  I'm trying to think of a productive reason to be on the toilet.
[1617.36 --> 1617.60]  Okay.
[1618.32 --> 1627.24]  Anyway, um, so, so, you know, the mobile side of it was, was part of it. Um, I think the other
[1627.24 --> 1631.30]  thing that I was really kind of interested in too was in just illustrating, particularly
[1631.30 --> 1638.24]  some of the modular CSS stuff I've been writing about on the CSS, the SaaS way for, um, a while.
[1638.24 --> 1643.34]  I wanted to spend some time to kind of make our CSS more modular in that regard. Um,
[1644.44 --> 1653.94]  so a lot of things there, uh, we ended up, um, I had been playing around with middleman and
[1653.94 --> 1659.22]  middleman to me, I, I can't really say enough good things about it. I've created my own thing,
[1659.22 --> 1668.66]  uh, serve, um, which is kind of in the same space. Um, it's really for, um, rapid prototyping
[1668.66 --> 1674.68]  rails applications, but it also generates static sites kind of similar to middleman. Middleman,
[1674.68 --> 1683.96]  um, to me is kind of the, um, Ruby has had a series of static sites generators, uh, Nesta,
[1683.96 --> 1692.66]  um, the oldest one is static matic static matic. Um, there there's, there's really like six or seven
[1692.66 --> 1697.26]  of them that have like played a major sort of role in it. And middleman is kind of the late comer,
[1697.26 --> 1704.16]  but he's sort of learned from everybody in terms of like what people want to do with their static sites.
[1704.16 --> 1712.94]  Uh, Jekyll's another one of them. Um, and middleman has this plugin architecture, uh, and sort of a data
[1712.94 --> 1721.98]  model that, uh, those two things really make it a killer content management system. Um, I actually,
[1722.22 --> 1731.18]  uh, they have plugins for doing the blog portion of it. And I ended up just writing a little Ruby code,
[1731.18 --> 1739.16]  uh, and helpers, uh, to, uh, pull out the information I needed instead of actually using the plugin
[1739.16 --> 1746.20]  that they have. Um, because the structure of our site was significantly different than if we had
[1746.20 --> 1754.06]  chosen to use their, their blog plugin. Um, and it was impressive to me that I was still able to,
[1754.14 --> 1761.74]  you can do things like, uh, go through the list of all of the pages on your site and, you know,
[1761.74 --> 1768.04]  grab their summaries and filter them in different ways. And having the ability to do that, um,
[1768.04 --> 1774.72]  you know, in code to build those category pages and other things like that, that we needed. Um,
[1775.00 --> 1783.10]  and to do it exactly according to our old structure was just amazing. Um, I thought we were going to
[1783.10 --> 1789.20]  have to, you know, do a lot more with redirects or something like that when we upgraded the site.
[1789.42 --> 1795.08]  It's always tough when you move a site from even one similar system, because Nestle wasn't very far off
[1795.08 --> 1799.46]  a middleman, honestly. I mean, they're pretty similar monsters, but obviously a slightly different
[1799.46 --> 1805.04]  structure, but the URLs that we chose originally were meant to be short and sweet, not, you know,
[1806.20 --> 1811.68]  extra category sections and segments in the URL. It's, it was pretty straightforward. So I was really
[1811.68 --> 1817.46]  happy with that too, that we were able to keep the URL structure one, just because it fit. And two,
[1817.54 --> 1819.42]  just to not have to do the redirects like you'd mentioned.
[1819.42 --> 1825.72]  Right. And I think, um, I mean, one of the things that I was really pleased with was, um,
[1826.22 --> 1834.16]  it was almost like I was just deleting code in order to make it work well in middleman. Um,
[1834.82 --> 1843.20]  and what I mean by that is that, um, there were times where we had like, in Nesta had to use like
[1843.20 --> 1850.82]  multiple partials and sort of like these hacks to like go around things. And, um, in middleman,
[1850.90 --> 1855.82]  when the final product was there, there were like less files that were had to be used to like get it.
[1855.94 --> 1859.50]  And, um, yeah, so it's.
[1860.12 --> 1864.06]  Even middleman and Jekyll though, for those listening and thinking like, you know, middleman,
[1864.22 --> 1869.18]  Jekyll, how do you choose and why do we choose middleman? They're very similar. I mean, even they
[1869.18 --> 1874.34]  both have the front matter. They both have similar ecosystems. And I think Jekyll is starting to get
[1874.34 --> 1881.30]  a lot more new life with, uh, with Parker taking over and, um, taking the helm of, you know, leading
[1881.30 --> 1884.94]  that. I mean, it's growing into its own thing as well. And author press has always been there
[1884.94 --> 1888.62]  leading the way as well with it, but middleman, like you had said, it's kind of like in this
[1888.62 --> 1894.36]  middle ground of, and the usability of it's really, really nice as well. And the fact that it's got
[1894.36 --> 1900.18]  that plugin ecosystem and it's got tons of stuff like a blog plugin and all sorts of cool stuff
[1900.18 --> 1908.24]  that you can do with it. Yeah. It's, um, I mean, my, my feeling is, is I would much rather use
[1908.24 --> 1917.96]  middleman and I've used Jekyll before. Um, Jekyll just seems to be, uh, it sort of pushes you into
[1917.96 --> 1924.72]  that blog paradigm kind of thing. It's a little bit like, um, WordPress years ago, uh, how every
[1924.72 --> 1929.06]  WordPress site was like a blog kind of thing. Right. At first it was a blog and then you kind
[1929.06 --> 1934.42]  of morphed into a site. And now it's become more of a content management system WordPress has.
[1934.96 --> 1940.56]  Um, or at least that's my understanding. I haven't used WordPress in years. Um, but I,
[1940.66 --> 1946.40]  and I think Jekyll's on a similar journey, but middleman is a content management system first.
[1946.40 --> 1954.84]  And in my mind, uh, it just makes a lot more of decisions the right way in, in that regard.
[1955.58 --> 1962.36]  Um, so yeah, I'm, I'm a huge fan and I, I mean, serve basically competes with middleman on,
[1962.56 --> 1967.06]  uh, in some people's minds as well. So, you know, I'm a passionate middleman user and I,
[1967.14 --> 1973.32]  I wrote my own thing. So. Yeah. I, I was always, uh, I always wondered about that too. Cause
[1973.32 --> 1980.84]  you know, I was a huge fan of your serve framework, which like you had said, is very similar to
[1980.84 --> 1986.02]  middleman and competes with it. And I think, um, there was even a point too, and I was like,
[1986.06 --> 1990.04]  man, middleman really requires a ton whenever you do, you know, gem install middleman,
[1990.16 --> 1996.22]  a lot comes with it. And I think with serve, you kind of leverage tilt a lot more. And was it tilt or
[1996.22 --> 2000.88]  what was the, the one particular library that you were other Ruby library you were leveraging to kind
[2000.88 --> 2012.64]  of keep things, you know, less dependencies? Do you recall? Um, I mean, I didn't, well, okay. So
[2012.64 --> 2017.58]  rack is probably what you're talking about. Originally serve was not built on rack. Um,
[2017.84 --> 2025.36]  and at a certain point we rewrote it so that it was on top of rack. Um, I, and at a certain point we
[2025.36 --> 2032.66]  rewrote it so that it was on top of tilt as well. Um, so I think middleman and serve are fairly
[2032.66 --> 2040.54]  comparable in that regard now. Um, I still feel like serve, what I love about serve,
[2041.06 --> 2046.72]  particularly using it in unstructured mode, you can just throw a bunch of files in a directory and,
[2046.72 --> 2053.38]  you know, just type the serve command and it knows how to, you know, serve up SAS if you want SAS or
[2053.38 --> 2059.24]  serve up, you know, the other stuff. Um, but when you get to something, so it's almost like the code
[2059.24 --> 2066.04]  pen tool kind of thing. That's, that's sort of where serve sweet spot is. Um, but when you get
[2066.04 --> 2071.48]  to something a little bit bigger and really a site that you want to manage, I think middleman wins
[2071.48 --> 2077.58]  hands down, I'd still probably use serve for prototyping rails apps. One of the, one of the things
[2077.58 --> 2082.74]  that I love about it is that, um, for the most part you use the exact same calls in serve as you
[2082.74 --> 2090.96]  would in rails to do, you know, helper methods and things like that. Um, and middleman somewhat
[2090.96 --> 2096.48]  follows that they make some different decisions on certain things. I think one uses render and the
[2096.48 --> 2103.68]  other uses partial to like call out to, you know, yeah, that, that kind of bugged me when you don't
[2103.68 --> 2111.52]  at least adhere to other, I guess, uh, what do you call it? Like just patterns the way that other,
[2111.52 --> 2116.44]  you know, right. That, that had been set up. So I, I, you know, in that regard, if you're
[2116.44 --> 2123.22]  coming from rails, you know, I think serve still, for example, you know, right. But serve
[2123.22 --> 2130.56]  also has a hard time right now, uh, exporting certain projects. Like, um, there's more work
[2130.56 --> 2136.88]  to be done to make serve. Awesome. Um, and middleman is just much better architected.
[2136.88 --> 2140.84]  So where's serve at nowadays? Like, is it, uh, where's the priority for you on that? Is
[2140.84 --> 2144.02]  it something you're still working on? Um,
[2144.02 --> 2156.40]  it, I, every once in a while I will spend time on serve. Yeah. I, you know, part of it for
[2156.40 --> 2164.56]  me, part of it for me is, is that I've like serve works for me for prototyping rails applications.
[2164.56 --> 2170.06]  It like scratches that itch like really well. And middleman works for me for static sites,
[2170.06 --> 2178.52]  like really well. So where serve could grow is in becoming more like middleman, right?
[2178.92 --> 2181.98]  And that's not, that doesn't make any sense because there's already middleman.
[2182.52 --> 2190.00]  Well, but there's already middleman and, um, it's already solving that problem. So part,
[2190.00 --> 2197.10]  I don't know, I, you know, I've having started, I guess if you count serve two major open source
[2197.10 --> 2204.02]  projects, I'm more than content to let them die at this stage because of the amount of
[2204.02 --> 2207.70]  management that they take. Why would this set your track record, John? You create CMSs
[2207.70 --> 2216.30]  so they die or something like that. I, I don't know. I, I'm just saying that like open source
[2216.30 --> 2222.56]  is a ton of work. Um, it is a ton of work and it's, I'm happy when another tool that's
[2222.56 --> 2225.34]  better comes along and replaces something that I was working on.
[2225.60 --> 2228.76]  What does that, what does that happen then? I know we're kind of hanging out on the serve
[2228.76 --> 2234.20]  topic for a little bit, maybe too long, but, uh, bear with us listeners. But, uh, for serve,
[2234.36 --> 2240.46]  do you have issues coming in often? Do you have people that are like using it for production
[2240.46 --> 2245.18]  and you know, they're, they're bugging you about it? Is that, or is it, is it just kind
[2245.18 --> 2245.48]  of quiet?
[2245.66 --> 2250.82]  I mean, there's, there's, um, probably the biggest thing right now, right now is, uh, people really
[2250.82 --> 2258.10]  want export to work exactly as it does when it's serving the project. And unfortunately,
[2258.92 --> 2267.94]  um, because of the way rack middleware works and all of that, if you have certain things installed,
[2267.94 --> 2275.46]  it's not going to render your site exactly as you wrote it. Now, if you're just doing vanilla
[2275.46 --> 2281.38]  serve, it certainly will. Um, but if you started to do some customization, um, and all that,
[2281.54 --> 2288.52]  the export doesn't know how to read your config.ru to figure out what, what that extra middleware
[2288.52 --> 2295.88]  is doing kind of thing. Yeah. Um, so there's, there's some work that needs to be done basically
[2295.88 --> 2302.26]  to give serve a configuration file to store some of those things in, uh, so that it can
[2302.26 --> 2306.84]  use it when it's exporting, it can use the configuration part of it to figure out how to
[2306.84 --> 2315.64]  rewrite URLs or, or various things like that. Um, yeah. And, and then there's things that
[2315.64 --> 2321.74]  like, I mean, just comparing it to middleman, middleman just does so much better. Um, I mean,
[2321.74 --> 2327.96]  I love being able to like access in code every single page on my site and build navigation or
[2327.96 --> 2333.44]  do whatever I wanted. Whereas with serve, I would have to like write code to navigate the file system.
[2334.38 --> 2342.70]  And there's no concept of like front matter or anything like that. Um, so it's a much,
[2343.12 --> 2345.48]  much different system.
[2345.48 --> 2351.10]  We're going to take a quick pause and give a shout out to our sponsor FreshBooks. Now we use FreshBooks.
[2351.16 --> 2355.42]  We absolutely love FreshBooks. We couldn't do business without them. So I was super excited
[2355.42 --> 2360.28]  to hear that they were supporting five by five and the change log. So, um, we, we just kind of got
[2360.28 --> 2366.60]  through this tax season and I bet if you weren't using FreshBooks, your life was probably a bit of
[2366.60 --> 2372.22]  a mess. And tell me if this sounds right, if this is you, you're hunting for receipts, digging through
[2372.22 --> 2378.40]  invoices, going through every record one by one. And that's, that's the worst, you know,
[2379.10 --> 2385.38]  FreshBooks is the simple cloud accounting solution that makes tax time a breeze. And with FreshBooks,
[2385.46 --> 2390.52]  you can create professional looking invoices, capture and track expenses, uh, get real time
[2390.52 --> 2395.66]  business reports with just a couple of clicks. Uh, I mean, plus you can work from anywhere with
[2395.66 --> 2399.86]  FreshBooks. You got mobile apps, you got one for your phone, you got one for your tablet,
[2399.86 --> 2404.16]  you can do it online, you know, through the webs. I mean, anywhere you are, you've got FreshBooks
[2404.16 --> 2410.10]  available to you. And like I said, we use FreshBooks. Um, we do a lot of invoicing through
[2410.10 --> 2417.78]  sponsorships and partners and stuff like that. So, I mean, we would, I don't know what I would do
[2417.78 --> 2422.16]  if I didn't have FreshBooks. I just say it like that. I really don't. It's, it's the bee's knees
[2422.16 --> 2427.94]  to our business. And the sooner you start using FreshBooks, the sooner you can start focusing on the work
[2427.94 --> 2433.62]  you love. And instead of focusing on your, uh, on your, your paperwork, you can focus on the work.
[2433.92 --> 2438.36]  And for a limited time, you can try FreshBooks for free for 60 days. Uh, to get started,
[2438.48 --> 2444.56]  visit getfreshbooks.com now and enter the changelog in the, how did you hear about us section when
[2444.56 --> 2449.62]  signing up? Huge thanks to FreshBooks for sponsoring a five by five of the changelog. We
[2449.62 --> 2456.22]  absolutely love FreshBooks. See, I was never really a huge fan of,
[2456.22 --> 2463.10]  I guess the front matter all the time. Cause I was, uh, for, for a while there, I had to write
[2463.10 --> 2467.18]  everything in Hamill and I've since kind of like laid that down. I don't, I don't really,
[2467.32 --> 2471.74]  you know, I don't have to write everything in Hamill anymore. I used to be a diehard Hamill fan.
[2471.78 --> 2476.18]  Like I would not write it. And that's probably to my detriment that I wouldn't write it
[2476.18 --> 2482.04]  unless it was an Hamill. Um, but you know, some front matter mixed with Hamill, a Hamill file kind
[2482.04 --> 2487.30]  of, you know, your syntax highlighter kind of gets out of whack or whatever. But, um, yeah, I was,
[2487.70 --> 2491.46]  I liked the, the, the front matter though of middleman. I think, you know, we were able to
[2491.46 --> 2495.78]  like really extend things quite some, quite some bit and kind of going back to the SAS way.
[2496.20 --> 2502.14]  One of the cool things you were doing, um, with this latest version is, is, um, what was the,
[2502.14 --> 2508.44]  there's an article, I think it's in, um, it's still in a pull request for SAS three, three.
[2509.38 --> 2516.48]  Yeah. So we, we wrote one for, we wrote an article for SAS three, three. And what's awesome
[2516.48 --> 2522.80]  about this article from a technical perspective is, is that it has a completely different header
[2522.80 --> 2530.28]  from all the other articles, which is something that I want to experiment, uh, with is, um, writing,
[2530.28 --> 2536.22]  uh, or, or doing a little bit more art direction, I guess you could say with our articles. Um,
[2536.60 --> 2543.96]  and so there's some HTML code that goes along with that CSS, all of that. Um, and we couldn't have
[2543.96 --> 2551.02]  done that easily with something that wasn't a, uh, file-based kind of system. Um, I know there,
[2551.02 --> 2557.86]  there are some plugins for WordPress for shipping custom CSS with each article kind of thing. Um,
[2557.86 --> 2563.02]  you know, and I guess if you're writing a lot in HTML or other things like that, then,
[2563.08 --> 2567.64]  you know, you could use a plugin and do it in WordPress, but again, you end up with stuff in
[2567.64 --> 2574.20]  the database. And if you change something like, I don't know, there's just awkward relationship
[2574.20 --> 2580.36]  on sites like that where, um, you're kind of mixing code design with content and it's,
[2580.36 --> 2586.90]  yeah, not a perfect mix. Well, and what's, what's stored in the database and what's stored on,
[2586.90 --> 2594.62]  you know, actually in code. Um, and if you don't store it in your Git repository, it's stored in
[2594.62 --> 2600.54]  the database, then hopefully your database stores versions of stuff that you work on, but a lot of
[2600.54 --> 2609.02]  times it doesn't. And, uh, so, and then, and because we can work in pull requests, uh, that can
[2609.02 --> 2614.12]  sort of sit on its side with all the code changes that are needed. And then it can be merged in when,
[2614.12 --> 2621.82]  when SAS 3.3 drops, um, you know, we'll pull that article over and, um, you know, it'll,
[2622.04 --> 2628.78]  it'll work perfectly. Um, but until then we don't need all of that extra CSS and other stuff. Um,
[2628.82 --> 2632.62]  and the site will continue to, you know, function. So.
[2632.76 --> 2636.94]  And you were able to pull that, um, additional partial in for that kind of, like you'd mentioned
[2636.94 --> 2641.08]  that art directed kind of editorial style header, the different header, you were able to do that
[2641.08 --> 2649.28]  with just simple YAML or, uh, front matter. Right. Right. Yeah. The front matter concepts, uh,
[2649.98 --> 2656.20]  pretty, pretty powerful. You can add whatever you want to it in middleman and, um, then in your
[2656.20 --> 2661.78]  layout or whatever it is that you're, you know, you can check that front matter and, um, do something
[2661.78 --> 2668.10]  based off of that. Um, there are times too, like one of the differences between Nesta and middleman
[2668.10 --> 2674.14]  was that Nesta had the concept of page title. Is this right? Am I remembering this right? Or was
[2674.14 --> 2680.62]  that some sort of custom attribute that you put on there? I can't recall. I think it did have a...
[2680.62 --> 2687.34]  The way, the way our stuff was set up was that, uh, in Nesta, we had in the front matter, a title.
[2687.52 --> 2696.88]  Yes. Yeah. And middleman by default didn't have that. Uh, sorry. No, the way Nesta works is it
[2696.88 --> 2702.58]  grabs the H1. That's right. Yeah. Yeah. And I didn't like that. It's not in the, in the front
[2702.58 --> 2709.58]  matter. And so I had all these articles that had no titles, right? So, so what I did was I wrote a
[2709.58 --> 2717.80]  helper that basically pre-renders the entire HTML. So it gets rendered twice and grabs the, the H1 and,
[2717.92 --> 2724.22]  you know, pulls that out as the title for it. Um, and it works. It's amazing. It's amazing.
[2724.22 --> 2730.88]  Like, yeah. The fact that you could do that in middleman is pretty awesome to me. Um, that
[2730.88 --> 2734.68]  you, that you have access to like the whole document, you can render it however you want.
[2735.04 --> 2740.54]  Um, it's very customizable. I like the fact that you were able to do a lot of stuff with,
[2740.70 --> 2748.36]  um, with the URLs to like just trimming off things like .html if you had that and, um, you know,
[2748.36 --> 2754.28]  the directories with indexes in them becoming, you know, uh, pretty URLs. And I think we even had an
[2754.28 --> 2760.14]  issue with our comments when we first launched the SAS where we had, we forgot to put the trailing
[2760.14 --> 2765.16]  backslash on there or I think it was on there by default with middleman and we wanted to pull it off
[2765.16 --> 2771.92]  because the, the previous version of the site didn't, didn't handle, um, or didn't have a
[2771.92 --> 2779.88]  trailing backslash, um, on the URL. And that actually caused, um, what is that we use for the
[2779.88 --> 2785.50]  comments? Discus. Yeah. Discus. It caused that to think it was a different, you know, page. So
[2785.50 --> 2790.08]  therefore it had a different, uh, comment stream and we were all, we're all just messed up there, but
[2790.08 --> 2796.68]  got that fixed and it's still not technically fixed, but, uh, you know, yeah, we have the issues
[2796.68 --> 2801.46]  still open. We're, we're getting close. You need to spend some time on that on a weekend or maybe,
[2801.46 --> 2805.36]  maybe one of our listeners. Maybe, yeah, maybe a listener would fix that for us.
[2807.22 --> 2811.70]  You see, you see what's going on here. This is just a giant conspiracy between Adam and me
[2811.70 --> 2816.16]  to get you, the listener to write our code.
[2819.16 --> 2824.26]  Yes. Yes. And our articles. Yes. Absolutely. Let's, you know what, speaking of that, let's give
[2824.26 --> 2829.68]  some shout outs to those who have contributed to the SAS way over the years. You got me and you who
[2829.68 --> 2834.02]  started it. Uh, I don't know if there are any particular, or I'm just going down the contributors
[2834.02 --> 2841.06]  list on the SAS way, which is, uh, Mario Vicaldi, uh, Mason Wendell, Peter Gaston, who wrote a book
[2841.06 --> 2847.08]  on CSS. I think it was, um, something on CSS three, like a couple of years ago. Really, really awesome
[2847.08 --> 2853.80]  book. I liked it. Uh, Roy, not sure how you say your last name. Uh, Hugo, how would you say his last
[2853.80 --> 2863.74]  name? Uh, I do not know. It's French. Uh, so I will need to try then. Uh, Girardelle, Girardelle.
[2863.96 --> 2867.02]  I'm not sure. And then you got Frank S. I don't know what, I don't know why Frank is so elusive
[2867.02 --> 2872.78]  with his last name, but Frank S. Well, that was just the awesome thing. Like here's this guy
[2872.78 --> 2877.72]  posting from South Africa and he doesn't want to tell us his last name and I'm okay with that.
[2877.72 --> 2883.38]  You know, Frank S. Cause he wrote an awesome article for us. He's got some more in the pipe
[2883.38 --> 2891.32]  too, I think. Daniel, uh, Daniel M's, I'ms, probably I'ms, I'm gonna guess. And then over
[2891.32 --> 2895.70]  the years too, we've also had, uh, Chris Epstein come and do some technical editing for us.
[2895.94 --> 2903.26]  Wayne Netherland, um, has done some technical editing for us as well. And I don't think either
[2903.26 --> 2909.70]  of them really ever plan to write anything. Um, I think Chris is just too busy anyways. And so is
[2909.70 --> 2916.98]  Wynn, but they were definitely Sass fans, of course, Wynn and Chris wrote the book Sass and
[2916.98 --> 2923.90]  that was Sass and Compass in Action from, um, uh, who's the Manny. I think that's right.
[2925.32 --> 2929.56]  So, you know, obviously huge fans and, you know, there's been several times when we've had an
[2929.56 --> 2932.80]  article go out that we're like, yeah, we need technical eyes on that one. Make sure that the,
[2932.80 --> 2936.76]  you know, what we were talking about actually does make sense. And, and they come in and kind
[2936.76 --> 2941.44]  of like do some blessing, but see, we always operated on GitHub before, but we just never
[2941.44 --> 2946.68]  had it open. It was in a private repo and it was, you know, this kind of, so for any of you out there
[2946.68 --> 2953.08]  who are rocking out private content based repos similar to the Sass way, you might want to consider
[2953.08 --> 2959.86]  an open publishing, uh, methodology because I got to say, man, I think the, the, you know,
[2959.86 --> 2966.82]  the new design definitely, um, lends to it being a middleman, being so easy to use, uh, lends to it.
[2966.82 --> 2973.38]  But I think the future of the Sass way is definitely bright and being able to fork it. And we even have
[2973.38 --> 2979.64]  a contributing doc to kind of guide you through actually contributing and whatnot. And I think
[2979.64 --> 2984.22]  we've got some plans even to kind of earmark some different topics for people, lack of better terms,
[2984.22 --> 2989.50]  maybe assignments to, so to speak. And if you want to pick it up, you can pick it up, uh, or bring
[2989.50 --> 2994.30]  your own carrot and write about what you want. So that's, uh, pretty excited, man. Pretty excited
[2994.30 --> 3006.56]  about it. Yeah. So, um, so I guess following the normal rhythm of doing a change log show, I know
[3006.56 --> 3012.28]  this time is a little tiny bit different than maybe our past shows. Um, but I still want to treat it the
[3012.28 --> 3017.04]  same in some respects. So, uh, we always ask some cool questions at the end that we're kind of known
[3017.04 --> 3024.74]  for. And, um, the first question I'll ask you, John is, um, is if you weren't writing Sass,
[3025.00 --> 3026.10]  what would you be writing?
[3028.84 --> 3038.44]  I mean, definitely CSS, right? Um, I'm so grateful that there is, is Sass. Uh, I mean,
[3038.44 --> 3045.30]  or maybe less if less was around. I don't know if there wasn't Sass, would we have stylus? Um,
[3045.84 --> 3052.90]  I don't know. I don't know. Maybe. I mean, so I do other things, um, as well. I, I write a lot of
[3052.90 --> 3060.66]  JavaScript. Uh, love JavaScript. Um, it's probably my favorite programming language these days. Uh,
[3060.66 --> 3068.72]  it, I would, it would have definitely been Ruby. I love Ruby's elegance. Um, but I don't get to do a
[3068.72 --> 3074.10]  lot of UI programming in Ruby. And I, I think that's why I love JavaScript. It just lets me get in there
[3074.10 --> 3086.46]  and make stuff awesome. Um, yeah, I'm not a Hamill fan. Sorry. Yeah. I, uh, I've become not a Hamill fan.
[3086.46 --> 3090.74]  Uh, I'd rather just keep it simple. I'm almost, I'm almost a purist at that point. Just
[3090.74 --> 3099.06]  if I can't, I'm, I'd almost just rather write in the case of a Ruby project, like ERB or straight HTML.
[3099.90 --> 3108.20]  Yeah. I like the other ways you can do, but I feel like I've kind of turned away from abstractions
[3108.20 --> 3114.86]  lately. Like I like, you know, for the hardcore, uh, JavaScript, uh, developer who wants to use
[3114.86 --> 3118.98]  CoffeeScript, that totally makes sense. And I think it makes sense to use it when it makes sense
[3118.98 --> 3125.44]  for you and your project and your team. Um, you know, and the same with SAS and CSS, that relationship,
[3125.54 --> 3129.74]  I feel like at each layer, there's some sort of abstraction, but with HTML, I just felt like,
[3129.98 --> 3134.36]  like it was just didn't make any sense anymore for a while. I loved it, loved the short and easy
[3134.36 --> 3138.12]  syntax, but after a while it would somehow bite you in the butt. So I just got sick of it.
[3139.36 --> 3143.94]  And, uh, yeah, I mean, I had a kind of a similar journey with Hamill. Um, I mean, I know,
[3143.94 --> 3148.74]  I remember thinking about it in terms of Rails views and this is technical, but that it seemed
[3148.74 --> 3158.42]  to help make, um, our Rails view code cleaner, um, because it forced you to write stuff on one line
[3158.42 --> 3165.18]  and whenever you just inserted a whole block of Ruby code in Hamill, it looks just awful. Um,
[3165.52 --> 3170.88]  whereas in a regular view, you can kind of get away with it looking okay. Um,
[3170.88 --> 3181.18]  so I, I did like that effect. Um, but at the same time, struggling with indentation and why is it not
[3181.18 --> 3189.68]  rendering? And, um, I don't know. I'm, I, I've sort of backed away from that. I've also backed away
[3189.68 --> 3195.78]  from the indented syntax on, on SAS for similar reasons in that it's just not enough like regular
[3195.78 --> 3203.24]  web development, I think to, um, to merit like making and it doesn't have enough benefits
[3203.24 --> 3206.08]  to merit an entirely new syntax.
[3206.08 --> 3212.06]  Yeah. Um, that's, that's probably an easy way to sum up what I just said. I think that's how I feel
[3212.06 --> 3217.30]  is like you almost put yourself on an Island doing that and it might be a good Island. And, you know,
[3217.30 --> 3221.48]  like you had said, it might clean up your Rails view code in the, in the case of Hamill or something
[3221.48 --> 3226.62]  like that. But what you end up doing is you got the community kind of going one direction and you're
[3226.62 --> 3231.42]  over here and another, and you're hanging out in like white space aware land. And it's just,
[3231.42 --> 3237.90]  you can't copy somebody else's code from a tutorial or you can't like easily riff or pair with somebody
[3237.90 --> 3243.82]  or kind of share ideas. And I think even for like when you're collaborating over code, it's like,
[3243.88 --> 3247.22]  well, you're using one version of the syntax and I'm using another. So we can't,
[3247.22 --> 3250.14]  we can't work together. And that's, that's a problem.
[3250.84 --> 3256.72]  Collaboration is really the thing. I mean, I, I already, I mean, I, I just hate that point in
[3256.72 --> 3263.04]  any project where you're like, well, so what's your favorite tool to do this kind of thing?
[3263.08 --> 3269.26]  You know, it's like, um, you know, I'd rather not have to make those decisions in some ways. Um,
[3270.10 --> 3275.14]  you know, I, I mean, even less or SAS or, or other things like that, you know, I mean,
[3275.14 --> 3283.60]  obviously I'm going to choose SAS. I write a blog about the SAS, but, um, but you know,
[3283.74 --> 3288.40]  the fact is I'm going, there are going to be some, some of those battles on every project and
[3288.40 --> 3290.48]  I just wasn't willing to fight the Hamill battle.
[3291.74 --> 3294.68]  Yes. Yes. That's where I'm at with you. I'm, I'm right there.
[3296.20 --> 3304.22]  Okay. Um, I guess that was a long answer, but, uh, totally cool. Okay. So if, uh, if you had a
[3304.22 --> 3308.84]  weekend, totally free, uh, no one to hang out with nothing planned, nowhere to go, you kind
[3308.84 --> 3313.58]  of just got this weekend all to yourself. Um, what open source projects are on your radar
[3313.58 --> 3314.54]  that you're going to hack with?
[3317.80 --> 3323.96]  Um, it could be something new. It could be something you've been wanting to play with for
[3323.96 --> 3325.22]  a while, but just haven't had the time.
[3325.22 --> 3333.80]  Um, I, I mean, I've been doing a lot of work with backbone lately. Um, I have a friend who's
[3333.80 --> 3341.48]  a big fan of angular. Um, and I would love to probably do an app in angular just to get
[3341.48 --> 3349.26]  a feel for how that works. Angular seems to have a lot of promise of, it's sort of an unstructured,
[3349.26 --> 3354.72]  structured, it has structure, but it's, it's unstructured in a way that like, I feel like
[3354.72 --> 3362.42]  maybe Ember, Ember JS is a little too structured, um, in terms of what it, and too opinionated
[3362.42 --> 3366.64]  in terms of what it, what it does. And then backbone is like the reverse of that. It's like
[3366.64 --> 3375.44]  no structure. And how do you do stuff, uh, in backbone at all? Oh, I got to write my own,
[3375.44 --> 3380.36]  you know, it's like, it's like writing rails sometimes. Like you have to write your own
[3380.36 --> 3385.72]  big chunks of the framework in order to get to work. Um, and angular seems to, I don't know,
[3385.74 --> 3390.32]  a little bit more of a, of the right balance. I like their templating stuff. So I would probably,
[3390.52 --> 3396.32]  if I was doing a new app, I'd probably work with angular. Um, that would be one thing.
[3397.66 --> 3405.42]  Um, uh, I would be interested probably in doing, using, uh, SUSI in SAS.
[3405.44 --> 3412.26]  Um, on a project, get a feel for it. I have heard some great things from Eric about SUSI too.
[3413.28 --> 3417.10]  Um, he's been working on.
[3417.54 --> 3424.42]  SUSI's got to be one of the oldest, um, I guess we used to call them grid frameworks and now
[3424.42 --> 3431.04]  they've become just bootstraps or frameworks or I don't know, we know what you, CSS frameworks.
[3431.70 --> 3435.52]  Like it started out as a grid and it was like the, it was the one that was,
[3435.86 --> 3440.76]  I think I have the story right where it was based on somebody else's ideas, but it was written
[3440.76 --> 3443.02]  specifically with SAS in mind.
[3444.48 --> 3449.92]  Yeah. Well, I think that SUSI has been the enduring grid framework and SAS line.
[3449.92 --> 3456.02]  Yeah. Um, it's been there through all the iterations of web development, like it pre-responsive,
[3456.02 --> 3457.18]  post-responsive.
[3458.24 --> 3459.24]  Right. Yeah.
[3459.56 --> 3467.50]  And I, I think that like the, and I'm a big fan of a very modular approach to writing your,
[3467.58 --> 3474.42]  your CSS. So like for the SAS way, we're using foundations grid framework actually. Um,
[3474.42 --> 3480.80]  so spend a little bit of time and rip that out so that, you know, we could use it. Cause I like,
[3480.80 --> 3486.82]  one of the things about foundation is, is that it has this concept of, for the responsive side of
[3486.82 --> 3491.44]  things, like three different view, you have like your desktop, you have your tablet and then you have
[3491.44 --> 3499.48]  your phone view essentially. And, um, you can put these classes on things to, to size it. And as a
[3499.48 --> 3507.46]  basic default grid framework, it's amazing. But what, where like SUSI, like to me has some advantages
[3507.46 --> 3514.84]  is in allowing you to just kind of go hog wild and crazy. And the way that you implement your,
[3514.84 --> 3521.88]  your framework, like it has no requirements about like class names that you have to use or, um,
[3522.40 --> 3529.38]  it's all mix in base then it's, it's, um, it's all mix in based. Uh, you know, I think he
[3529.38 --> 3535.12]  has some like generators to make it easier for you. Um, but you can use it without using those
[3535.12 --> 3542.44]  grid classes, which some people like, um, about it. I feel like you could use SUSI to kind of create
[3542.44 --> 3548.50]  a custom framework for your website. So I'm very interested in it from, from that way. But again,
[3548.56 --> 3554.38]  I mean, I haven't seriously used it. We're using it on, um, one of our user voice sites right now.
[3554.38 --> 3562.30]  Um, so I've, I've sort of seen an implementation of it. Um, but yeah, I would, I, I, I definitely
[3562.30 --> 3567.80]  think there's more to investigate there. Um, seems like a great framework.
[3568.80 --> 3574.28]  So backbone you're a fan of, if you had a weekend free, you'd be hacking on Angular cause you want
[3574.28 --> 3578.66]  to, you want to play with that and you've heard lots of good stuff about it. And if, uh, your front
[3578.66 --> 3584.72]  end would, would use SUSI. Yeah, I think so. And so let's talk about maybe that just maybe
[3584.72 --> 3590.18]  elongate that for like maybe one more minute, which is, um, you know, how well does the SAS
[3590.18 --> 3595.62]  fit into it? Cause you have stylus in the JavaScript world, right? You got, um, that's kind of par for
[3595.62 --> 3599.26]  the course of you're going to do something there. What happens whenever you want to use something
[3599.26 --> 3610.16]  like SUSI, um, which is it compass agnostic or is it not? Um, it's a compass, a compass extension.
[3610.42 --> 3616.04]  Yeah. Uh, it's built on top of compass. And, and the main reason to do that is that, um,
[3616.58 --> 3624.68]  you can, you can basically package it up as a gem, your extension as a gem, and then compass
[3624.68 --> 3631.20]  can load it from that gem. Um, whereas if, if you use something else, then you're, you
[3631.20 --> 3637.04]  end up in a scenario where you dump your styles, the styles from that thing into a certain directory,
[3637.04 --> 3644.58]  and then you have to figure out the loading yourself. Um, so the compass extensions, it,
[3644.58 --> 3649.06]  it is a true compass extension in that regard. Yeah.
[3649.06 --> 3655.44]  So you kind of got some, some hurdles to, to hop over to hack with angular and use compass
[3655.44 --> 3661.52]  Ruby based gems potentially, or at least be both sides of the fence, right?
[3662.28 --> 3667.50]  Yeah. It seems like a lot of SAS stuff is being distributed over, um, Bauer, like with JavaScript.
[3667.98 --> 3677.16]  Um, so depending on what the backend is, I might end up using, uh, I don't know, that would
[3677.16 --> 3680.42]  be interesting. Well, when you cross that bridge and you get that weekend, you let us know.
[3681.54 --> 3685.04]  That's what I want to know. All right. Last question for you then. Um,
[3687.02 --> 3691.06]  this is a fun one too. So, I mean, feel free to think on this one for, for about a half a second,
[3691.06 --> 3697.94]  but, uh, who would you say is let's, let's open it up for you since you're a designer and developer
[3697.94 --> 3705.18]  who is, you know, like your web hero, you know, who, who is someone that has kind of like either been
[3705.18 --> 3709.74]  guidance to you? Maybe it's somebody who taught you early on, somebody took you into their wing,
[3710.14 --> 3716.02]  could be whatever, could be, you know, a past school teacher that might've inspired you, but
[3716.02 --> 3721.60]  who's someone you would, you would consider a hero, um, to you in terms of web development?
[3721.60 --> 3737.00]  Um, I mean, it's probably, I mean, there's definitely a bunch of people in my life in that way. Um,
[3738.04 --> 3746.20]  different coworkers, bosses, that kind of thing. In terms of a inspirational kind of person,
[3746.20 --> 3754.70]  I would probably have to go with, uh, Sean Inman. Um, and what he's done in sort of,
[3755.62 --> 3761.08]  Sean does design and development, uh, and he's built his own products and that's kind of the
[3761.08 --> 3769.88]  intersection of like all of the things I love. Um, so I, I admire him a whole lot. Uh, I, I would
[3769.88 --> 3775.24]  love to do exactly what he's doing right now, getting into like game development. And I don't know,
[3775.24 --> 3780.56]  it seems like, uh, I'd love going over to his blog and looking at what he's working on. So he,
[3780.56 --> 3789.20]  I mean, he's definitely one. Um, yeah, I mean so many, so many web heroes, Douglas Bowman, uh,
[3789.34 --> 3799.02]  used to be a big fan of his. Uh, I can remember when I was working on Radiant, um, I, uh, the way
[3799.02 --> 3803.46]  that he had built his site, like I tried to make Radiant so that it could do a site like his really
[3803.46 --> 3810.14]  easily. He, he used to curate links on design and books and all of those types of things. So I
[3810.14 --> 3816.96]  wanted Radiant to be able to make it easy to curate those, um, you know, lists of things and,
[3816.96 --> 3827.22]  and it did. Um, so yeah, I don't know. It's, it's really interesting that when I first got into web
[3827.22 --> 3837.10]  development, there were all of these guys that I looked up to, um, and it seems like some of them
[3837.10 --> 3842.62]  have, are not as active anymore in communicating. Nobody blogs anymore, I guess is what it is.
[3842.72 --> 3847.36]  Everybody micro blogs. I mean, that's, it's the Twitter thing, you know, everybody's there.
[3847.36 --> 3855.54]  Yeah. Twitter. You know, it's, it's kind of changed. I mean, um, well, Doug, you know,
[3855.64 --> 3860.02]  you said Douglas Bowman, so he used to blog a lot and he doesn't blog much anymore. And I think Sean
[3860.02 --> 3865.18]  Emmons did as well. And I think that was the rage was, that was the way we kind of originally began,
[3865.18 --> 3871.98]  um, to social network, you know, and then since then actual social networks with following and
[3871.98 --> 3878.46]  actual lists, not blog roles in your sidebar sort of took over that, uh, you know, replaced that older
[3878.46 --> 3885.14]  model and people, they, they, you're right. They do blog a lot less. I think before we kind of had to,
[3885.18 --> 3890.64]  to get our opinions out there, whereas now there's different ways we can share our opinions like on
[3890.64 --> 3896.42]  podcasts and stuff like that. But, uh, Sean Emmons, I think he's been mentioned at least once before,
[3896.42 --> 3901.96]  for sure, as a, as a hero on the show. And I gotta agree, I'm huge on him and fan. Um,
[3901.96 --> 3910.18]  I think I can't even imagine how awesome that guy is to be able to design code, think through
[3910.18 --> 3918.18]  products. And he's a game designer. I mean, like he can, he did that. Um, I forget what this,
[3918.32 --> 3923.24]  what the project was called. I think it was called like retro something, um, on Kickstarter. He and I
[3923.24 --> 3928.96]  think two or three other fellows were doing like really quick iterative game design where like they'd do
[3928.96 --> 3934.54]  a game a week or something like that or a game a month. And it was, I, I backed that and got the
[3934.54 --> 3940.24]  t-shirt to prove it, but, uh, literally got the t-shirt to prove it. Um, and that wasn't just a
[3940.24 --> 3944.78]  joke or something to say, but I think he's an awesome guy, man. Like, I think he is just really
[3944.78 --> 3949.88]  talented and it's those kinds of people that, man, you just wish they shared a bit more.
[3949.88 --> 3955.44]  Yeah. Seriously. Doug, why are you not blogging anymore? I don't mean like, you know,
[3955.48 --> 3961.20]  why don't you blog every day, but like, you know, they've got such insights to like, um, you know,
[3961.24 --> 3966.62]  Doug is a really, really blessed designer. He's had a really great track history of great design,
[3966.70 --> 3972.36]  everything from the version two, I think, which is kind of forever ago of wired and a number of other
[3972.36 --> 3978.16]  like redesigns that he was a part of. And now he's leading design at Twitter and he's, you know,
[3978.16 --> 3982.72]  a part of the team that's responsible for all the new great ways Twitter's rolling out their design
[3982.72 --> 3987.54]  sign. I, I don't mean share like that. I mean, share some of their wisdom, you know?
[3989.10 --> 3996.60]  Yeah. I mean, I think it, it's definitely a season thing, um, for a lot of those guys. I,
[3996.60 --> 4002.86]  I mean, it's, it's, it's hard to be in the public spot spotlight in that regard. I, I've heard that
[4002.86 --> 4016.50]  about Sean that, um, he never really expected to become one of the web gods and, uh, that,
[4016.58 --> 4022.26]  that he's, he's really a, you know, kind of a quiet guy in that regard, humble person. Um,
[4022.58 --> 4028.74]  yeah. And, uh, very talented, but, um, you know, just wasn't expecting to be in the spotlight and
[4028.74 --> 4034.74]  I don't know. I, I, yeah, but the fans, we guys, we want to know.
[4036.18 --> 4041.26]  We'll have to get Sean on the show. Cause I mean, I know that he's, um, I'm not sure how active he,
[4041.26 --> 4047.50]  he is an open source, but, um, we'll have to get into at least release something, uh, open source.
[4047.58 --> 4051.22]  We can get him on the show. It's kind of like part of the course. You have to, you know,
[4051.34 --> 4055.88]  Oh, you have to release something. I mean, you know, it's the change log, you know,
[4055.88 --> 4066.20]  open source moves fast. Keep up. Yeah. So we need a new show where we can, we can just interview,
[4066.20 --> 4073.14]  interview our, our heroes here. Well, you know, to, to speak on that, I mean, I think one of the
[4073.14 --> 4081.00]  things we want to do here, um, is I would like to do, I would like to have more shows, but the,
[4081.00 --> 4087.48]  the problem that comes into play is, is the same reason with open source. You just have only a
[4087.48 --> 4092.40]  limited amount of time. And so I've just tried to like bite off only as much as I can chew. Cause
[4092.40 --> 4098.56]  if I, I want to do everything I do to excellence, you know, I don't want to like half bought anything.
[4098.86 --> 4104.86]  Yeah. I kind of get that. I do wonder about like a special feature though, or something. I don't know.
[4104.86 --> 4110.96]  Yeah. Something to think about. We'll do it though. I mean, cause it's actually, um, an idea I've
[4110.96 --> 4116.86]  wanted to do, which was just, um, take the show that we have here. Cause it's pretty popular.
[4117.24 --> 4121.74]  It's on five by five. You know, everyone who listens to it, loves it. A lot of people write in,
[4122.28 --> 4126.60]  um, and say it's their favorite show. And I appreciate everyone who does that. I mean,
[4126.62 --> 4131.38]  it's certainly the star spirits and keeps the team, you know, motivated and whatnot. But,
[4131.38 --> 4136.66]  um, I'd like to expand a little bit more on the show and do something a little different. I think
[4136.66 --> 4140.76]  the show is great. We have people on, we talk about open source and it's kind of got this rhythm,
[4140.76 --> 4146.40]  but I kind of want to break it up and do, um, not so much more shows, but like different segments,
[4146.72 --> 4152.44]  you know, not always do the same exact show every time. Yeah. I mean, I think there's something along
[4152.44 --> 4158.36]  the lines of like the, you know, you have the news every night, but then there's like, um, the morning
[4158.36 --> 4163.32]  show and, you know, other things like that. Exactly. You know, there's, there's gotta be
[4163.32 --> 4167.76]  room to kind of branch out a little bit. We're gonna, long story short, we're gonna,
[4168.20 --> 4175.44]  we're gonna, um, play with that idea a bit more, but, uh, no promises. We'll see.
[4176.72 --> 4181.62]  It's on our, uh, it's on our to-do list of thinking through that's for sure. But yeah,
[4181.70 --> 4185.74]  you know, John, it's been great having you back on the show. I think that, um, you know,
[4185.74 --> 4191.16]  in all ways that you contribute to open source. I know that I've certainly learned a lot from you've
[4191.16 --> 4196.30]  been a great friend over the years and, um, you know, working with you on the SAS way and all
[4196.30 --> 4201.80]  that it's going to do in the community is just looking forward to where, where we're taking that.
[4201.86 --> 4205.78]  And I think, you know, we'll say it here just because I know we're going to do it soon, but
[4205.78 --> 4211.68]  we've talked about, um, SAS weekly or some sort of weekly newsletter we're going to do. So we're
[4211.68 --> 4216.88]  starting to execute on that as well. And that'll be open as well. Um, the same as,
[4217.02 --> 4221.40]  as everything else is. I'm really excited about the future, man, for us.
[4222.44 --> 4225.24]  Yeah, me too. Very, very excited about it.
[4225.44 --> 4232.04]  And, uh, yeah, the, the SAS way.com go there. Um, github.com slash the SAS way.
[4232.46 --> 4237.04]  We've got a couple repos there. We've got our identity repo there. If you need to use a logo,
[4237.04 --> 4241.66]  uh, by the way, we didn't even get to mention that, but Berman painter, thank you so much for
[4241.66 --> 4249.50]  your hard work on SAS's logo. And then subsequently our, our inheritance of, uh, of your skills to
[4249.50 --> 4254.70]  rock out the SAS way. And then I guess you, John, for your tweaked version of it, right? Your tweaked
[4254.70 --> 4259.82]  version is a little bit different than Berman's, but using his art. So it's good stuff.
[4259.82 --> 4265.90]  Yeah. Berman got it going for us. And, um, then I, I sort of put together the final,
[4265.90 --> 4273.36]  uh, part of it, but it's his brushstrokes that are amazing. But yeah, the SAS way.com,
[4273.48 --> 4279.08]  uh, github.com slash the SAS way. If you want to fork the repo and share your thoughts,
[4279.16 --> 4283.28]  open an issue. If you just want to chime in with us and say hello, I mean, issues don't have to just
[4283.28 --> 4290.04]  be problems. That could be ideas. Say hello. Um, and, and we'd, we'd love to hear your thoughts on
[4290.04 --> 4297.00]  your, uh, what, what gets you excited about SAS and writing CSS the SAS way and just get you excited
[4297.00 --> 4302.26]  about design. So share your thoughts, but I also want to give a shout out to our, uh, our sponsors
[4302.26 --> 4307.54]  of the show, digital ocean and top top for supporting the show. We definitely love you guys.
[4307.54 --> 4314.14]  Digital ocean.com and top towel.com T O P T A L.com. Not, uh, somebody wrote in and said,
[4314.20 --> 4319.64]  I'm not sure what you say when you say top towel, Adam, is it, is it top like towel, like a bath towel?
[4319.86 --> 4328.68]  And I'm like, I can't help it. They got a hard to pronounce business name. Um, it's top towel T O P T A L.com.
[4329.58 --> 4333.18]  But, uh, yeah, John, thank you so much for, for joining us today on the show. And thanks
[4333.18 --> 4338.22]  so much for all that you do, uh, until we hear from you again, let's say goodbye for now.
[4338.64 --> 4340.04]  Okay. Thanks so much.
[4363.18 --> 4381.44]  Thanks.

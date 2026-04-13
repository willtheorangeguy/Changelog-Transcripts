[0.26 --> 3.22]  I'm Nadia Ekbal, and you're listening to The Change Log.
[12.64 --> 16.20]  Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak.
[16.28 --> 21.70]  This is episode 193, and today we're joined by Nadia Ekbal to talk about a huge topic
[21.70 --> 25.16]  to us near and dear to our heart, funding open source.
[25.16 --> 30.92]  We also talked about Nadia's current investigative journalism work, funded by the Ford Foundation.
[31.42 --> 35.70]  We talked about venture-backed open source projects, what it means for an open source
[35.70 --> 40.48]  project to be in good shape, potential solutions to provide better support for open source,
[40.82 --> 46.18]  and we also thought deeply about how much the open source of the world might be worth.
[46.82 --> 51.86]  Our first sponsor of the show is TopTile, and long-time listeners of the show know that
[51.86 --> 57.92]  we love TopTile, head to t-o-p-t-a-l.com and check them out.
[58.02 --> 62.78]  I'd love to give you a personal introduction, whether you're an engineer or designer looking
[62.78 --> 68.18]  for greater opportunities to freelance, travel the world, blog with the TopTile blog, get
[68.18 --> 71.90]  open source grants, or you're a woman looking for more opportunities.
[72.06 --> 77.86]  They have an awesome scholarship program for women, giving back mentorship, giving back
[77.86 --> 84.02]  advice into career paths, really great things happening at TopTile, or maybe you're a CTO
[84.02 --> 87.30]  or a team leader that's building a team and you're looking for some of the best talent
[87.30 --> 87.80]  out there.
[88.20 --> 92.06]  I want to invite you to email me at adam at changelaw.com.
[92.14 --> 96.02]  I'd love to help you connect with the right people at TopTile, take that next step.
[96.30 --> 101.54]  Once again, go to t-o-p-t-a-l.com and tell them what changelaw sent you.
[101.94 --> 103.48]  And now, on to the show.
[107.86 --> 113.70]  All right, everyone, we're here today talking about funding open source with Nadia Ekbal,
[114.00 --> 117.70]  a former founder and also former venture capitalist.
[118.00 --> 119.18]  I'm here, Jared's here.
[119.90 --> 121.78]  And this, Jared, what is this topic?
[121.82 --> 124.40]  This topic is like near and dear, as close as you can get to our heart, right?
[125.06 --> 125.44]  Absolutely.
[125.64 --> 131.08]  It's something that we always seem to bring up on the show because it's so kind of ingrained
[131.08 --> 134.56]  in what we are and what our audience does.
[134.56 --> 139.08]  And so we always touch on it as a side topic in our other conversations, but we have never
[139.08 --> 142.18]  addressed it so pointedly as to dedicate a show to it.
[142.44 --> 142.54]  Yeah.
[142.64 --> 143.56]  So I'm quite excited.
[144.00 --> 146.08]  This is a different kind of show for us, too.
[146.28 --> 148.54]  So Nadia, introduce, I guess, say hello at least.
[148.70 --> 150.00]  We don't want to keep in the wings too long.
[151.16 --> 151.86]  Hi, everyone.
[152.50 --> 154.44]  And Nadia, you're not a developer, though, right?
[154.44 --> 154.88]  Is that right?
[155.64 --> 161.98]  I did build the product for a company that I co-founded, but I would certainly not call myself
[161.98 --> 162.38]  a developer.
[162.38 --> 162.74]  Okay.
[163.16 --> 167.12]  And so the reason I say that is not to say, hey, you are, you're not, but mostly because
[167.12 --> 172.16]  we're such a developer-centric audience, developer-centric show for many, many years.
[172.24 --> 176.20]  Obviously, as we kind of talked to you about before the actual call kicked off, but just
[176.20 --> 180.40]  to sort of say that this is a different kind of show for us where, as Jared mentioned, we've
[180.40 --> 185.80]  been dancing around this funding open source, open source maintainability, sustainability, whatever
[185.80 --> 188.40]  term or phrase you use to describe it.
[188.40 --> 193.48]  And for so long, we love this topic because obviously we love open source, but usually
[193.48 --> 194.62]  we have developers on the show.
[195.64 --> 199.26]  But Jared, maybe you can share how you found this article.
[199.36 --> 202.10]  I remember you sharing that with me in Slack and you're like, hey, is this a good topic
[202.10 --> 202.38]  for us?
[202.40 --> 203.10]  I'm like, absolutely.
[203.10 --> 203.18]  Absolutely.
[203.66 --> 203.78]  Yeah.
[204.18 --> 206.54]  What got you on that Medium post of hers?
[207.22 --> 212.34]  I don't remember where I found it, like specifically probably Twitter, which is where, you know,
[212.46 --> 214.08]  most links get flown.
[214.08 --> 220.96]  And it was something that if you were online last week or the, I guess the second week in
[220.96 --> 226.54]  January 2016, running in our circles, you probably saw it because Nadia made quite a
[226.54 --> 227.84]  splash, I think, with this post.
[227.94 --> 231.68]  It was called, How I Stumbled Upon the Internet's Biggest Blind Spot.
[232.30 --> 236.50]  So if you can't tell, she's an excellent writer because that title is just begging for you to
[236.50 --> 237.20]  click on it, right?
[237.92 --> 240.46]  Everybody wants to know what the blind spot is, you know?
[240.46 --> 240.90]  Yeah.
[241.60 --> 248.66]  So I apparently wanted to know as well and found quite an interesting post of Nadia's
[248.66 --> 251.74]  recent findings, struck home with us.
[251.98 --> 256.14]  And yeah, we just said, well, we got to get her on and talk about this from a perspective
[256.14 --> 257.20]  that we don't normally get.
[257.38 --> 257.54]  Right.
[257.64 --> 259.58]  Like you said, Adam, we're used to developer perspectives.
[260.40 --> 262.76]  Here we have a founder, a former VC.
[263.36 --> 266.68]  And really, I think, Nadia, correct me if I'm wrong, but you're almost acting as a journalist
[266.68 --> 268.20]  in this context.
[268.66 --> 269.00]  Yes, definitely.
[269.00 --> 272.68]  You know, posting what you found.
[274.16 --> 274.82]  Investigate her, too.
[275.36 --> 275.88]  Yeah, absolutely.
[276.94 --> 281.02]  But before we get to that, maybe we can find out where you're coming from.
[282.48 --> 282.80]  Yeah.
[282.92 --> 287.04]  We like to get to know our guests so we know a little bit about you, which is that you're
[287.04 --> 289.54]  not a developer, which is not a very good way to define somebody.
[290.82 --> 291.96]  And again, it's not meant to be negative.
[292.12 --> 293.56]  It's just meant to explain.
[293.74 --> 294.12]  It's accurate.
[294.12 --> 294.34]  Right.
[294.42 --> 294.56]  Yeah.
[295.12 --> 299.80]  So if you could give, you know, kind of your origin story to where you are today, how'd
[299.80 --> 301.46]  you get here and where you're coming from?
[302.00 --> 302.24]  Yeah.
[302.82 --> 305.60]  So I kind of wandered into tech by accident, I would say.
[306.38 --> 313.68]  I went to school out in Boston and I was working more on the impact investing and nonprofit
[313.68 --> 314.12]  side.
[314.12 --> 320.48]  So working with foundations, talking about better ways to, I guess, strategically invest
[320.48 --> 321.10]  their endowments.
[322.04 --> 324.36]  And I moved out to San Francisco on a whim.
[325.12 --> 328.18]  I wish I had a better reason for this, but I just moved out here because the weather was
[328.18 --> 329.46]  really nice and I visited once.
[329.92 --> 330.46]  That's a good reason.
[331.12 --> 331.56]  Where from?
[331.56 --> 332.82]  From Boston.
[333.00 --> 333.24]  Okay.
[333.58 --> 333.64]  Yeah.
[333.64 --> 334.00]  So understandable.
[335.40 --> 338.56]  And I came out here still in the nonprofit sector.
[338.98 --> 344.86]  I was at a strategy consulting firm and found a job out here purely so that I could move
[344.86 --> 345.40]  to San Francisco.
[346.32 --> 350.50]  And the nonprofit that they placed me with was this organization called Great Schools.
[351.46 --> 356.20]  And Great Schools is an education nonprofit, but they also happen to be a website.
[356.20 --> 361.68]  And they provide free school data on every K to 12 school in the country.
[362.12 --> 365.94]  And you can go online and you can look up your school and find all this information about
[365.94 --> 366.16]  it.
[366.42 --> 367.72]  And I thought it was a really cool service.
[367.72 --> 373.22]  And I thought it was cool that it was a nonprofit because you could have made it a
[373.22 --> 374.10]  for-profit, I guess.
[374.46 --> 378.58]  But they saw the value of just saying, hey, here's a bunch of really great data and it'll
[378.58 --> 379.38]  empower parents.
[379.46 --> 381.20]  It'll empower teachers to just have it out there.
[382.28 --> 385.90]  And so while I was there, I was obviously more on the business and strategy side of things.
[386.20 --> 390.90]  But because it was a website, there was a team of engineers, team of designers, et
[390.90 --> 391.28]  cetera, et cetera.
[392.24 --> 397.28]  Got to know that side of the business a little bit better and thought it was really interesting.
[398.08 --> 404.46]  And while I was there, I think, and just being so exposed to tech here, this was in 2010,
[405.36 --> 408.30]  got a little bit more interested in the data side of things at Great Schools.
[409.76 --> 412.74]  Started teaching myself to code because why not?
[413.06 --> 413.24]  Right.
[413.24 --> 413.30]  Right.
[415.10 --> 419.52]  And I think this was like right before all the coding boot camps and everything exploded
[419.52 --> 421.16]  in, let's say, 2013.
[422.18 --> 429.10]  So I went out and bought these little books on how to learn Ruby on Rails and Ruby and
[429.10 --> 429.36]  whatever.
[429.82 --> 430.18]  Mm-hmm.
[430.18 --> 436.04]  Um, and when I left Great Schools, I ended up starting a company with my roommate at the
[436.04 --> 436.30]  time.
[437.24 --> 441.32]  Um, because again, that's what you do when you're in San Francisco and kind of decided
[441.32 --> 444.98]  that tech was maybe a more interesting direction for me to go in.
[445.24 --> 447.42]  Um, because it seemed faster paced.
[447.48 --> 450.66]  It seemed like the way to sort of like implement your ideas in the world.
[450.66 --> 454.18]  Whereas I'd felt more held back, I guess, with the nonprofit sector.
[454.18 --> 459.32]  Um, and we built our, I built our product.
[459.84 --> 464.06]  Um, again, would certainly not call myself a developer, which I think was kind of part
[464.06 --> 464.50]  of the point.
[465.10 --> 469.92]  Um, was, I was somebody who had been coding for, I don't know, maybe like a year and a
[469.92 --> 470.66]  half at this point.
[470.66 --> 475.22]  Uh, but was able to string something together that was usable for us.
[476.02 --> 481.02]  And part of that obviously was because somebody else had gone out and created, you know, all
[481.02 --> 484.18]  the frameworks and libraries that I needed to make myself run.
[484.86 --> 490.16]  Um, and so we went through the traditional startup sausage factory experience.
[490.44 --> 493.36]  Um, we raised money.
[493.58 --> 499.54]  We joined an accelerator, um, had this whole like business that we were growing.
[499.54 --> 507.52]  And I think that being my first experience in startups, I also realized that, uh, there's
[507.52 --> 513.30]  this really great ecosystem for if you have a good idea and you want to get it out there
[513.30 --> 518.14]  and you want to find support, there is a very well-developed industry of venture capital,
[518.32 --> 519.04]  of angel investors.
[519.38 --> 521.70]  There's tons of institutional funding to help you get started.
[522.04 --> 522.98]  There's accelerators.
[523.24 --> 527.76]  I mean, the accelerator we went through 500 startups was like super influential and helpful for us.
[527.76 --> 534.56]  Um, and it kind of got me wondering, well, what about other things that are really valuable,
[534.56 --> 539.14]  but don't have venture backing and don't have that kind of institutional support?
[539.40 --> 540.94]  How do you help those things grow?
[541.02 --> 543.64]  And you know, what sources of funding are out there for them?
[544.32 --> 547.26]  And so this is something that was sort of like percolating in my mind.
[547.62 --> 553.26]  Um, we ended up selling that company to another food brand because it was a food company by the way.
[553.26 --> 559.52]  And yeah, neither, neither I nor my co-founder realized that, uh, we wanted to do this for
[559.52 --> 561.20]  the next five to 10 years.
[562.02 --> 566.80]  Um, but I had sort of gotten stuck on this question again of, well, how do you fund things
[566.80 --> 571.08]  that are really valuable and don't fit into that traditional venture model?
[571.34 --> 574.06]  Like great schools, the education nonprofit that I was at.
[574.06 --> 580.26]  Um, and so I just started exploring after we had kind of wrapped things up with our company
[580.26 --> 584.26]  and started writing about it much like I'm doing now.
[585.16 --> 589.62]  Um, and I wrote this one blog post that was called, what if Facebook were a nonprofit?
[590.54 --> 594.56]  Um, not necessarily because I wanted it to be a nonprofit, but just because I thought it
[594.56 --> 595.38]  was an interesting question.
[595.38 --> 601.12]  And, uh, one of the partners at the venture firm, I ended up joining collaborative fund,
[601.28 --> 603.86]  uh, read that post and thought it was interesting.
[604.32 --> 607.14]  We got to chatting, we got to know each other better.
[607.76 --> 610.88]  And at some point he invited me to join collaborative fund.
[611.80 --> 617.18]  Um, and so I joined not to do venture capital, even though it was a seed stage venture capital
[617.18 --> 622.62]  firm, I had actually joined to do this alternate growth fund that we had talked about, um, creating
[622.62 --> 627.74]  for companies that were profitable and needed extra capital to grow, but didn't necessarily
[627.74 --> 632.34]  want to have your traditional venture exit of like going public or big acquisition or
[632.34 --> 632.56]  whatever.
[633.52 --> 635.58]  Um, and so I thought that was a really interesting project.
[635.58 --> 639.36]  I thought it might be a great way to kind of dig into these questions a little bit more.
[640.36 --> 647.68]  Um, and after I joined, realized that we just didn't have the resources to start a fund that
[647.68 --> 649.90]  was kind of out of the scope of what we were already doing.
[649.90 --> 656.56]  Um, we already had a bunch of money raised for, and had been deploying and whatever for
[656.56 --> 659.18]  seed stage, which are like the earliest stage investments.
[659.30 --> 663.16]  Um, but raising money for like a growth fund is a completely different story.
[663.72 --> 667.32]  Um, and there are four full-time people, including myself.
[667.70 --> 674.22]  Um, I was out here in San Francisco, everyone else was in New York and there's obviously plenty
[674.22 --> 677.08]  to do around seed stage investing in San Francisco.
[677.08 --> 682.18]  And so it just sort of started to make sense that I got more involved on that side of things.
[682.88 --> 690.04]  Um, and so at some point kind of became full-time seed stage investing and it was a really, really
[690.04 --> 690.76]  great experience.
[691.34 --> 698.06]  Um, I learned so much about venture capital, about how startups grow, about how good ideas
[698.06 --> 705.16]  get out there and, um, and, and become successful and how much, uh, venture capital helps contribute
[705.16 --> 705.58]  to that.
[705.94 --> 709.96]  So I think it was a really, really great experience for me overall.
[710.16 --> 711.72]  I'm really glad that I had it.
[712.18 --> 717.12]  Um, but it kind of got to the point where realized that, you know, this wasn't the thing that I,
[717.52 --> 721.14]  it wasn't ultimately answering these questions that had been in my head for so long.
[721.14 --> 729.08]  Um, so I ended up leaving in May of last year and took a little bit of time off to relax.
[730.14 --> 733.94]  Um, and then started diving back into this question, which I had covered in the post,
[733.94 --> 741.06]  um, just about, you know, what are these things exactly in my head that are not venture backable?
[741.06 --> 743.28]  Um, cause it's a very vague thing, right?
[743.30 --> 750.34]  It's like very popular to say, uh, you know, venture is this like evil thing that everyone
[750.34 --> 751.38]  is relying on.
[751.50 --> 751.60]  Yeah.
[751.62 --> 753.70]  We've said on the show, it's like, Ooh, it's bad.
[754.22 --> 754.62]  Right.
[754.70 --> 756.60]  Everyone just likes the shit on venture capital.
[757.28 --> 761.88]  Um, but you know, there's plenty of things that are really great about venture too.
[761.88 --> 767.98]  And I think having been in that scene for a little bit was, um, really helpful to give
[767.98 --> 770.08]  me an appreciation of all the things that it does right.
[770.50 --> 773.80]  And to try to think about, all right, how can you take that framework and make it helpful
[773.80 --> 774.86]  for somebody else?
[775.96 --> 781.18]  Um, and yeah, I mean, I, I, it was kind of that process that I had outlined in the post
[781.18 --> 785.70]  of starting with this very, very broad list of things that are not venture backable in
[785.70 --> 786.32]  tech at all.
[787.12 --> 788.88]  And that was a pretty broad list.
[788.88 --> 796.80]  It was, um, you know, stuff around like data and APIs, um, stuff around like independent
[796.80 --> 802.66]  product makers who were just kind of making games and fun little apps and things, um,
[803.00 --> 804.94]  stuff around like government tech and whatever.
[804.94 --> 811.08]  And so I had this very broad list and started interviewing founders, um, just treating it
[811.08 --> 816.18]  basically like my venture capital job of like going out and sourcing opportunities and talking
[816.18 --> 816.68]  to founders.
[816.90 --> 818.24]  Um, it was the same process.
[818.88 --> 824.02]  And after I started talking to them about specifically, like why things aren't venture
[824.02 --> 827.48]  backable or, or are they interested in these types of things?
[827.64 --> 827.80]  Yeah.
[827.96 --> 832.62]  I wanted to know whether, how they were being funded, how they're literally just paying
[832.62 --> 835.72]  their bills, um, and where that was coming from.
[836.56 --> 841.86]  And I found for some situations, like people were totally fine with the situation.
[841.86 --> 847.96]  They said, you know, like I'm consulting or, you know, I have like one or two apps and make
[847.96 --> 849.70]  a ton of money and let me work on other stuff.
[849.70 --> 854.60]  And so if people were okay with it categorically, then I crossed them off the list.
[855.40 --> 859.72]  Um, but I really wanted to focus on things where people were saying, Oh my God, yes, this
[859.72 --> 860.92]  is a huge issue for me.
[860.92 --> 862.50]  Can we please talk about it now?
[863.32 --> 869.24]  Um, went through that list, narrowed it down, got sort of like a couple of different groupings
[869.24 --> 873.04]  of areas that seemed categorically unfundable.
[873.04 --> 880.70]  Um, and then I started going back to the funding side of things and talking to people I knew
[880.70 --> 886.64]  who are either had a really great perspective on funding companies and projects and organizations,
[887.24 --> 894.54]  um, talking to angels, talking to VCs, um, talking to foundations and just asking them like,
[894.68 --> 896.04]  here are some opportunities I've seen.
[896.40 --> 899.86]  Why would you, or would you not fund stuff like this?
[899.86 --> 903.96]  And that was, that was definitely tough.
[904.52 --> 911.32]  Um, plenty of funders were, and especially I think, um, here in Silicon Valley, like you
[911.32 --> 913.44]  always want to see a return on everything that you're doing.
[913.44 --> 920.10]  And I think that's true even in philanthropy, um, in San Francisco where it's always like,
[920.10 --> 922.18]  what is my return on the thing I'm doing?
[922.18 --> 926.90]  It's, it's never just like pure giving, um, which can be a good and a bad thing.
[926.90 --> 927.28]  I think.
[927.28 --> 931.08]  Like you mean even in these meetings that they would take with you where you're asking
[931.08 --> 933.48]  questions, there's like, there's no upside for them on it.
[933.52 --> 934.70]  So it's kind of like, why do this?
[935.36 --> 935.60]  Yeah.
[935.84 --> 938.90]  I think it was, um, yeah.
[938.94 --> 942.50]  I mean, for things where I was like, this just isn't going to be an investment, this is
[942.50 --> 944.40]  going to be a grant or something.
[944.40 --> 948.12]  Then the response would kind of be like, well, why would I do that?
[948.12 --> 953.90]  Um, which I think is, I mean, having come from the nonprofit sector too, like, I think
[953.90 --> 959.24]  there's absolutely plenty of grant making that gets very bloated and isn't really that
[959.24 --> 959.60]  effective.
[959.60 --> 964.18]  And you absolutely don't want to create a situation where somebody is like always dependent
[964.18 --> 968.02]  on you for money and they haven't diversified, uh, their risk at all.
[968.20 --> 971.34]  That's something that even like foundations and nonprofits talk about all the time.
[971.34 --> 973.32]  Well, there's that radio station out there.
[974.40 --> 974.92]  What's that?
[975.40 --> 978.20]  It's a WII FM.
[978.60 --> 979.26]  What's in it for me?
[980.90 --> 981.60]  It's a joke.
[981.68 --> 981.92]  Sorry.
[982.74 --> 983.62]  That's what people think.
[983.74 --> 987.10]  They think like, what, Hey, if it's, if there's nothing in it for me, why should I, why should
[987.10 --> 987.50]  I care?
[987.68 --> 993.76]  Which seems like your overarching theme across, you know, both of the posts we'll dive deep
[993.76 --> 994.44]  into in this call.
[994.48 --> 998.78]  It just seems like if, if people think what's in it for me and the answer is nothing, they're
[998.78 --> 1000.18]  like, well, I don't care then.
[1000.18 --> 1001.10]  But I do that.
[1001.24 --> 1001.32]  Right.
[1001.84 --> 1002.24]  Yeah.
[1002.40 --> 1006.18]  And I, I mean, I absolutely spent, I would probably say I spent years being really angsty
[1006.18 --> 1006.88]  about that question.
[1007.22 --> 1009.62]  Um, and especially felt it over the summer.
[1010.68 --> 1015.60]  And I think I hit a point where, and this was kind of the, the point where I ended up
[1015.60 --> 1019.98]  focusing in on open source infrastructure was at a point where I was like, okay, you know
[1019.98 --> 1020.22]  what?
[1020.26 --> 1021.74]  Like I can't change human nature.
[1022.52 --> 1024.54]  Um, that is a very big task.
[1024.98 --> 1030.16]  Uh, so let me start with things that people can't argue against where like, you know,
[1030.16 --> 1034.74]  like something is not theoretically, this would be really awesome, or this would make, this
[1034.74 --> 1039.64]  would make a better society if we did this, but it's more like this is already happening.
[1040.12 --> 1041.70]  Um, this is already out there.
[1041.84 --> 1044.06]  You're already using it, whether you know it or not.
[1044.06 --> 1046.70]  And it's not being well-funded or supported.
[1047.12 --> 1051.00]  And the only thing that I really found that was consistently categorically true on my list
[1051.00 --> 1052.14]  was open source infrastructure.
[1053.34 --> 1059.42]  Um, and so that's, I think changed the conversation a lot more because now it's more about, here's
[1059.42 --> 1063.98]  the thing that's a system that we're all relying independent upon that isn't well-supported.
[1064.14 --> 1065.08]  What do we do about it?
[1065.08 --> 1068.14]  Um, and it's still a collective action problem.
[1068.24 --> 1074.98]  It's still a problem of every individual wants to receive support, um, or wants to have this
[1074.98 --> 1081.84]  resource exist, but then is not individually motivated to overcome, uh, their own self-interest.
[1082.84 --> 1088.56]  And I think like, there's still ways to talk about solutions that can work with that and,
[1088.56 --> 1094.96]  um, motivate people to work together, even when it's not always obvious or easy or,
[1095.08 --> 1096.72]  um, or desirable.
[1097.92 --> 1101.38]  So after these conversations with different funders, and like you said, you kind of hit
[1101.38 --> 1106.96]  a wall or you got depressed or distressed about it, um, you changed your question slightly.
[1107.22 --> 1107.66]  Yeah.
[1107.76 --> 1110.86]  So it was originally, what is not venture backable in tech right now?
[1111.24 --> 1116.02]  And then you added an addendum at the end, which was what's not venture backable in tech
[1116.02 --> 1119.02]  right now that tech absolutely cannot do without.
[1120.02 --> 1124.88]  And you had previously kind of come up with categories of types of, not businesses,
[1124.88 --> 1126.74]  but endeavors that aren't backable.
[1127.66 --> 1133.06]  And, um, sometimes it's because they're lifestyle businesses or because they're, you know, small
[1133.06 --> 1138.84]  products that, um, kind of like you said, our agency model or something like that.
[1138.84 --> 1144.88]  But other things you have data, knowledge, infrastructure, media, um, government type things,
[1145.22 --> 1145.82]  public services.
[1145.82 --> 1152.48]  And what was the effect of switching the conversation, the, the question from, you know, what's not
[1152.48 --> 1155.60]  ventureable venture backable, but what they can't live without.
[1155.70 --> 1156.82]  Was that trying to convince them?
[1156.82 --> 1161.10]  Like you said that they're already using this, they already need this and how did that affect
[1161.10 --> 1161.70]  your results?
[1161.70 --> 1162.94]  Yeah, definitely.
[1163.08 --> 1167.52]  I mean, I think that's why I think of this whole thing as a long game, um, where like
[1167.52 --> 1175.42]  systematically we're not, I think, especially for Silicon Valley, like we're just not really
[1175.42 --> 1182.24]  conditioned to think about things that the market can't solve or that, um, aren't somehow
[1182.24 --> 1184.04]  like venture backable businesses.
[1184.04 --> 1186.74]  And so it's, I mean, that's a very hard thing to overcome.
[1186.84 --> 1189.70]  That's a very hard mentality and culture to overcome.
[1190.18 --> 1191.24]  And I get it.
[1191.30 --> 1196.44]  Um, and I think starting with stuff that like, we know we're already using, but it doesn't
[1196.44 --> 1202.04]  fit into that category can help open up a conversation for other things that might be like more theoretically
[1202.04 --> 1202.52]  valuable.
[1202.88 --> 1207.34]  Um, and that also don't fit into your classic like business model.
[1208.16 --> 1212.82]  Um, so for me, it's like, it's not about like throwing away all the other things and saying,
[1212.82 --> 1216.42]  oh, well, these are obviously useless, but it's sort of like, okay, where can I come?
[1216.50 --> 1220.66]  And like, where can we meet each other in the middle and agree that this is something
[1220.66 --> 1225.20]  that is being used and is useful, um, but doesn't have a business model in the classic
[1225.20 --> 1226.56]  Silicon Valley sense.
[1227.72 --> 1232.18]  We got to take our first break, but, uh, I do want to preface that break with the fact
[1232.18 --> 1236.50]  that I think it seems like you're hopeful and maybe the reason why you're hopeful is because
[1236.50 --> 1240.60]  you've done some investigation into this human condition in terms of how you've investigated
[1240.60 --> 1242.38]  this path you've been on.
[1243.00 --> 1246.48]  Uh, so when we come back from the break, I think I want to dive a little deeper into the,
[1246.48 --> 1250.84]  the first topic we'll open up, which is in the post you've been talking about, which we'll
[1250.84 --> 1252.54]  share a link to everyone listening in the show notes.
[1252.60 --> 1257.44]  So you can kind of either pause and read or read along, uh, depends upon how fast you can
[1257.44 --> 1257.66]  read.
[1257.96 --> 1262.14]  And what you said was venture capital showed me the weird and wonderful nature of the human
[1262.14 --> 1262.50]  condition.
[1262.50 --> 1267.44]  And to me, it seems like you're hopeful there's a solution out there and we're wondering, you
[1267.44 --> 1269.84]  know, what you learned from, from that path you got.
[1269.84 --> 1270.60]  So let's take a break.
[1270.70 --> 1272.08]  When we come back, we'll talk about that.
[1273.38 --> 1277.58]  Our friends, Linode are huge fans of the show and many of the developers that work at
[1277.58 --> 1278.02]  Linode.
[1278.42 --> 1279.70]  Listen to the show.
[1280.04 --> 1281.14]  They're huge fans of what we're doing here.
[1281.18 --> 1282.32]  They want to support what we're doing.
[1282.56 --> 1285.62]  And we want to invite you to try out Linode.
[1285.86 --> 1289.54]  One of the most fastest efficient SSD cloud servers on the market.
[1289.76 --> 1293.56]  Use our code change log 20 to get $20 in credit.
[1294.04 --> 1297.58]  Basically two free months plan started just 10 bucks a month.
[1297.58 --> 1303.48]  They have eight data centers spread across the entire world, North America, Europe, Asia
[1303.48 --> 1304.02]  Pacific.
[1304.56 --> 1307.88]  They got hourly billing with a monthly cap on all plans and add on services.
[1308.26 --> 1314.02]  You get full route access from more control, run VMs, run containers, or even your own private
[1314.02 --> 1314.66]  Git server.
[1315.16 --> 1320.82]  You can enjoy native SSD storage, 40 gigabit network, Intel E5 processors.
[1320.82 --> 1325.70]  Again, use the code change log 20 to get a $20 credit with unlimited uses.
[1325.92 --> 1326.60]  Tell your friends.
[1327.00 --> 1328.94]  It doesn't expire until the end of this year.
[1329.10 --> 1330.86]  So use it as many times as you want.
[1331.00 --> 1331.52]  Share it.
[1331.80 --> 1332.64]  Tell everyone you know.
[1333.08 --> 1335.72]  Head to Linode.com slash change log to get started.
[1338.52 --> 1338.94]  All right.
[1338.96 --> 1341.62]  We're back from the break here with Nadia, here with Jared.
[1341.80 --> 1343.48]  And we're talking about funding up in source.
[1343.52 --> 1344.58]  And this is a big topic.
[1345.10 --> 1348.70]  Now you got a couple of blog posts and a Q and a blog post and several to kind of support
[1348.70 --> 1352.82]  some of this journalistic investigation you've been doing.
[1353.02 --> 1354.50]  And we thank you for all that effort.
[1354.66 --> 1360.14]  And we teed up this before the break with this question, I guess, is what you learned
[1360.14 --> 1366.06]  from and maybe what you found to hope in when it came to what the venture capital world you
[1366.06 --> 1369.66]  kind of lived in for a while, that what it showed you about the weird, in your own words,
[1369.78 --> 1371.92]  weird and wonderful nature of the human condition.
[1372.04 --> 1373.18]  So what did you learn?
[1373.18 --> 1382.92]  I would say that most broadly, venture capital taught me to understand how to work with what
[1382.92 --> 1389.64]  is happening right now rather than overly focusing on what might theoretically be great if it
[1389.64 --> 1397.30]  existed somewhere in the future, which is very, very hard for me to just personally to
[1397.30 --> 1399.76]  accept and move up against.
[1399.76 --> 1403.72]  But once you start looking at like, OK, what are the rules right now?
[1403.82 --> 1405.46]  What are the constraints that I have right now?
[1405.54 --> 1410.22]  And then how can I work with those things and talk about those things instead of just
[1410.22 --> 1413.58]  kind of like pushing something that doesn't exist right now?
[1414.42 --> 1415.70]  It just becomes a lot.
[1416.12 --> 1418.26]  Solutions become a lot more obvious because you have constraints.
[1419.50 --> 1424.64]  I think one thing that is interesting, if you just kind of look at the venture capital
[1424.64 --> 1430.84]  and startup ecosystem is that venture is not really just about finding a billion dollar
[1430.84 --> 1433.74]  company the way that a lot of people talk about it.
[1434.10 --> 1439.34]  It's also about creating landscapes and creating new ecosystems and platforms.
[1440.44 --> 1446.36]  And I think that's why venture and I guess I have more consumer focus here just because
[1446.36 --> 1448.18]  our fund was consumer focus.
[1448.82 --> 1450.30]  Might be a little bit different for enterprise.
[1450.30 --> 1455.66]  But within consumer stuff, the companies that are most interesting are those with really
[1455.66 --> 1458.14]  strong communities, really strong networks.
[1458.62 --> 1460.44]  People talk about network effects all the time.
[1461.20 --> 1467.08]  Audience based apps where you have like millions of people using something and nobody really
[1467.08 --> 1467.90]  understands why.
[1468.10 --> 1470.04]  But that's fascinating to an investor.
[1470.26 --> 1472.14]  They're just like, why is everybody doing this?
[1472.18 --> 1473.18]  Why is everybody using it?
[1473.18 --> 1480.28]  That makes it an attractive or interesting opportunity, even if the monetization in the
[1480.28 --> 1481.52]  long run is not always obvious.
[1482.40 --> 1487.44]  And I think that's probably part of why you see a lot of these audience based companies
[1487.44 --> 1490.66]  using advertising or whatever, because they don't really know how to monetize.
[1491.60 --> 1493.44]  The one that comes to mind for me is medium.
[1493.62 --> 1497.30]  Like I hear a lot of people getting upset and that's kind of the medium, so to speak, that
[1497.30 --> 1499.84]  you use to amplify your message here.
[1499.84 --> 1503.22]  But, you know, that's the one that come up recently and I'm like, so what if it's, I
[1503.22 --> 1507.72]  mean, I guess, I guess not so what, but we're talking about why to not post there because
[1507.72 --> 1509.48]  there's no, there's no model.
[1510.12 --> 1510.72]  It's scary.
[1511.56 --> 1511.68]  Yeah.
[1511.80 --> 1512.54]  And I think it's hard.
[1512.60 --> 1517.36]  I mean, there's certainly examples of things where people became overly dependent or relying
[1517.36 --> 1519.60]  on a certain platform even now.
[1519.74 --> 1524.18]  And that platform sucks and then it's really hard to move off of it or it has problems
[1524.18 --> 1524.64]  or whatever.
[1525.20 --> 1529.26]  Or it just has its own best interests in mind and not necessarily the best interests of the
[1529.26 --> 1531.26]  people who are, you know, creating the content.
[1531.48 --> 1531.60]  Right.
[1532.48 --> 1532.82]  Totally.
[1533.42 --> 1533.82]  Yeah.
[1533.94 --> 1538.40]  But then you look at, I think that is part of accepting kind of like what is versus what
[1538.40 --> 1542.82]  should be where like, no matter how much people talk right now about saying like, don't use
[1542.82 --> 1548.32]  medium because medium is like bad for us or whatever, you know, these are some of the
[1548.32 --> 1550.02]  issues we could have somewhere down the line.
[1550.40 --> 1553.18]  Like people just never think that way.
[1553.18 --> 1555.42]  Like in aggregate, that's just not how humans think.
[1555.82 --> 1562.96]  And, um, if medium offers something that is like short-term really great for them, then
[1562.96 --> 1563.68]  they're going to use medium.
[1563.68 --> 1565.16]  And that's why people use medium.
[1565.72 --> 1570.46]  And so there's this difference between like, what is ideological, ideologically like a great
[1570.46 --> 1574.20]  idea versus like, what is the thing that is going to get people actually adopting and
[1574.20 --> 1574.82]  using a product?
[1574.82 --> 1582.32]  Um, so that's a, an interesting, I guess, difference that, um, that I got to understand
[1582.32 --> 1583.06]  better in venture.
[1583.92 --> 1591.88]  Um, but then the, this idea of creating networks and platforms where, I mean, I think I've said
[1591.88 --> 1595.88]  this before, but I think Andreessen Horwitz is like one of the best examples of this where
[1595.88 --> 1597.68]  they made a lot of investments in infrastructure.
[1597.68 --> 1605.20]  Um, so they did GitHub's first, um, venture around, for example, um, where they understand
[1605.20 --> 1610.18]  the idea of like, if you create a platform that everybody is using, then you can build
[1610.18 --> 1610.60]  on it.
[1610.94 --> 1611.34]  Exactly.
[1611.96 --> 1615.38]  Um, and that just creates like so many effects that like people can't even imagine.
[1616.00 --> 1618.58]  Um, and that's like a really powerful thing.
[1618.58 --> 1624.72]  It's like, it's almost less about valuation and, and more about like that creation of power
[1624.72 --> 1625.94]  long tail influence.
[1626.08 --> 1626.88]  Yeah, absolutely.
[1626.88 --> 1631.40]  Um, and I don't know if you guys saw, there was this like Slack fund that was created by
[1631.40 --> 1637.52]  a bunch of venture capitalists recently, um, where a bunch of investors in Slack had come
[1637.52 --> 1642.88]  together and put together, I think I want to say 80 million, but I'm not positive how
[1642.88 --> 1646.56]  much it was, um, to fund apps that are created using Slack.
[1647.62 --> 1652.44]  Um, and it's not because my guess is not because they think that they're going to find the next
[1652.44 --> 1656.16]  billion dollar app on Slack, but by putting money towards that, they're incentivizing people
[1656.16 --> 1656.92]  to build on Slack.
[1657.28 --> 1660.68]  And the more people that build on Slack, the more people are dependent and relying
[1660.68 --> 1661.18]  on Slack.
[1661.38 --> 1663.88]  Therefore they've created this like ecosystem, right?
[1664.62 --> 1665.54]  For better or for worse.
[1665.64 --> 1666.22]  That's what happened.
[1666.22 --> 1671.88]  Um, so, and, and so when I think about that and I apply it to open source, it's, I mean,
[1671.88 --> 1678.04]  open source is kind of one of the most fascinating examples of really strong, tight knit communities,
[1678.18 --> 1681.84]  um, and like self-organized networks of people.
[1681.84 --> 1686.54]  Um, and I think that because people don't understand it very well or haven't taken the
[1686.54 --> 1689.94]  time to understand it, um, open source is really hard to understand.
[1690.26 --> 1691.34]  I've learned this the hard way.
[1691.44 --> 1692.60]  There's just so much happening.
[1693.10 --> 1695.46]  Um, and it's really hard to keep track of everything.
[1695.62 --> 1695.94]  Totally.
[1696.32 --> 1697.70]  Um, that's why we're here.
[1697.78 --> 1698.88]  We try to, we try to keep up.
[1698.92 --> 1699.98]  It's our motto right here.
[1700.82 --> 1701.34]  It's great.
[1701.34 --> 1702.06]  It's really important.
[1702.30 --> 1702.56]  Yeah.
[1703.46 --> 1707.08]  Um, but like, I mean, if you just look at it like that, it's like, are you have like
[1707.08 --> 1713.62]  tons and tons of people using and self-organizing and, um, and making stuff and then other
[1713.62 --> 1716.12]  people build stuff on top of the stuff that they make.
[1716.50 --> 1722.06]  So it's kind of like this like huge decentralized platform that we use to build software on.
[1722.42 --> 1722.82]  Right.
[1722.82 --> 1727.20]  And from that perspective, it's something that any institutional funder who's interested
[1727.20 --> 1732.18]  in supporting landscapes better and creating ecosystems better, they should be supporting
[1732.18 --> 1733.24]  that in some shape or form.
[1733.62 --> 1733.86]  I agree.
[1734.34 --> 1737.74]  And the more we know about it, the more we realize it's like a house of cards and we're
[1737.74 --> 1740.60]  amazed that any of it works at all.
[1741.12 --> 1741.88]  I am too.
[1742.16 --> 1746.04]  On that note, I was going to, I was going to say earlier, Nadia, it seems like you're
[1746.04 --> 1748.86]  writing and your research has sort of painted this picture for us.
[1748.88 --> 1755.14]  And it's like this really awesome chair with really rickety legs and those legs, not so
[1755.14 --> 1759.26]  much that open source is rickety, but that, that it's not stable.
[1759.26 --> 1762.90]  And so that gives the rickety in this, I guess, of this chair and we've got everything
[1762.90 --> 1765.48]  sitting on this chair, this table, if that's the example.
[1765.74 --> 1766.10]  Yeah.
[1766.12 --> 1767.88]  And the legs are not well supported.
[1768.08 --> 1771.14]  That's the picture I see that you've painted through your writing.
[1771.28 --> 1772.12]  Yes, definitely.
[1772.64 --> 1776.40]  But when you mentioned, I was going to say in your post, you know, you titled it that
[1776.40 --> 1778.42]  you stumbled upon the biggest blind spot.
[1778.96 --> 1782.64]  And one of the things that you say there is that when you started to realize that open
[1782.64 --> 1787.38]  source infrastructure, and maybe we do well to define that as opposed to, you know,
[1787.38 --> 1791.50]  open source as a whole, because there's a lot of facets, but open source infrastructure
[1791.50 --> 1793.24]  is so necessary now.
[1793.24 --> 1798.82]  And, and I mean, worldwide, and yet people think it's doing just fine.
[1798.90 --> 1801.10]  Even yourself said you thought to yourself, it's open source.
[1801.24 --> 1802.96]  Isn't open source doing just fine?
[1803.92 --> 1809.86]  And you're, you're, where'd your research go from there to like show you that there are,
[1810.02 --> 1813.42]  you know, that the chair is rickety and it's not a firm foundation.
[1813.42 --> 1813.86]  Yeah.
[1814.36 --> 1819.16]  So I had kind of had a couple of projects on my list, my original list that had just
[1819.16 --> 1819.96]  stumbled upon.
[1821.18 --> 1823.46]  And so I started talking to those people.
[1824.20 --> 1828.78]  Once I kind of made it known to a couple of people that I was really interested in this
[1828.78 --> 1835.78]  topic, then they being the amazing, super close knit network that open source is, people
[1835.78 --> 1841.00]  just started like sending me other projects, pointing me towards their friends who had projects
[1841.00 --> 1841.68]  they knew about.
[1841.68 --> 1848.58]  Um, so I actually like so much of it was based on word of mouth and anecdotal, um, which was
[1848.58 --> 1849.50]  kind of awesome.
[1849.68 --> 1854.50]  How easy it was to just like put yourself out there and have tons of people that were so
[1854.50 --> 1857.56]  nice, so willing to talk and willing to share their perspective.
[1858.56 --> 1862.00]  Um, and I just tried to listen to people as much as possible.
[1862.00 --> 1866.52]  And I'm still trying, I think I'm, I'm trying to be very aware of the fact that like, I'm coming
[1866.52 --> 1873.02]  into this as a, let's call it like researcher with a question, um, or kind of like a call
[1873.02 --> 1873.72]  to action in mind.
[1873.72 --> 1878.80]  But there are people who have like decades of experience or just seen so much stuff.
[1879.12 --> 1881.90]  And it's really cool because I love listening to people all day long.
[1882.04 --> 1885.30]  So, um, just asking them about their experiences.
[1885.30 --> 1891.76]  I never, I try really hard not to assume anything about projects or, um, what people need or whatever,
[1891.76 --> 1894.90]  and just try to like absorb as much information as possible.
[1894.90 --> 1899.78]  Um, and then try to take a step back from that and say, okay, what are the patterns of what
[1899.78 --> 1900.68]  other people are saying?
[1901.20 --> 1908.06]  Um, I think there's very little that I'm saying or proposing that is like entirely my opinion
[1908.06 --> 1913.58]  or my idea or whatever, but I, I'd rather think of myself kind of like as an amalgamation
[1913.58 --> 1917.88]  of like all the other feelings that I've absorbed from other people.
[1918.76 --> 1920.28]  Or any specific feelings?
[1920.36 --> 1924.16]  I know you had a few quotes that you pulled out of what people have been telling you, you
[1924.16 --> 1925.68]  know, the open source trenches.
[1925.96 --> 1928.60]  Like what was the general feeling that you were receiving?
[1929.76 --> 1931.32]  A lot of frustration for sure.
[1932.32 --> 1942.76]  Um, the, the ongoing, the sentiment that I think I've heard very often is I, I, and I
[1942.76 --> 1943.88]  understand why people are frustrated.
[1943.98 --> 1948.50]  It's like, I've created this thing that everybody is using, but I have absolutely no idea how to
[1948.50 --> 1949.06]  sustain it.
[1949.16 --> 1951.48]  And I'm going crazy by myself.
[1952.26 --> 1953.66]  Um, sounds about right.
[1954.16 --> 1954.42]  Yeah.
[1955.36 --> 1960.00]  And it's just so odd because like in the startup world, you're like, I have this thing that
[1960.00 --> 1961.28]  millions of people are using.
[1962.48 --> 1967.62]  And at that point, like VCs will have hunted you down because like that is their job.
[1967.84 --> 1969.28]  Like they will know where you are.
[1969.36 --> 1971.18]  They will find you and try to invest in you.
[1971.18 --> 1975.60]  It's like you, if you're sitting on this thing, that's so valuable, like people are just trying
[1975.60 --> 1976.70]  to throw money at you.
[1977.24 --> 1982.66]  Um, and, and so it just feels so odd to have somebody doing work that is really, really
[1982.66 --> 1984.58]  valuable and appreciated by lots of people.
[1984.94 --> 1987.72]  Um, but they have no support at all whatsoever.
[1987.72 --> 1993.84]  And I think that's the, the biggest thing I've seen lacking is just like, there is no institutional
[1993.84 --> 1994.14]  support.
[1994.22 --> 1996.24]  There's no like quote unquote exit for this.
[1996.24 --> 2000.30]  It's kind of like, here you go, work on this for the rest of your life if you want, or try
[2000.30 --> 2001.64]  to find someone else to give it to.
[2001.64 --> 2006.48]  Um, but it's volunteer time, you know, don't complain.
[2007.18 --> 2008.00]  And I think that's frustrating.
[2008.52 --> 2012.46]  I think it's tough because there's a lots of different projects fall into different categories
[2012.46 --> 2013.78]  of support as well.
[2014.14 --> 2019.80]  Um, you know, you have language support like, uh, Swift, which is open source and Apple of
[2019.80 --> 2021.92]  course is throwing massive money behind that.
[2022.00 --> 2024.14]  Go a good one, you know, from Google.
[2024.48 --> 2025.80]  Um, Mozilla has Rust.
[2025.92 --> 2030.90]  So at the language level, you know, there are all, there are also a lot of, you know, I don't
[2030.90 --> 2034.88]  want to call them toy languages because that's demeaning, but smaller groups of people working
[2034.88 --> 2037.18]  on interesting languages that don't have that kind of support.
[2037.18 --> 2042.70]  Um, but then we also have kind of a rise of venture backed open source products that,
[2042.84 --> 2045.98]  you know, Adam and I have been, Adam, we've had a lot of those lately.
[2045.98 --> 2051.32]  I just put a short list, RethinkDB, ZeroDB, Meteor, Metabase, Docker.
[2052.12 --> 2056.96]  Um, these are open source projects with business models, you know, differing business models.
[2057.20 --> 2060.84]  And so you see support coming to those specific projects.
[2061.60 --> 2067.12]  Um, but then you have really like the grassroots homegrown, you know, the single person project,
[2067.40 --> 2071.54]  Adam Daniel Stenberg of curl is the one I always think of where it's like just a guy
[2071.54 --> 2074.50]  in his basement or in his office and he writes a family.
[2074.92 --> 2075.08]  Yeah.
[2075.16 --> 2075.96]  Talk about infrastructure.
[2075.96 --> 2081.76]  He takes a utility and a, you know, and a library, library, library, library for doing
[2081.76 --> 2084.96]  something, you know, fetching URLs.
[2084.96 --> 2090.00]  And of course it does way more than that now, but, and that's like code that's running in
[2090.00 --> 2092.42]  almost every software system in the world now.
[2093.06 --> 2100.16]  Um, so they have all these different circumstances, but I think your overall finding is that there's
[2100.16 --> 2101.80]  a lot that's falling through the cracks.
[2101.80 --> 2102.70]  Is that fair to say?
[2102.70 --> 2103.72]  Yeah, definitely.
[2104.42 --> 2110.06]  The, the venture backed projects, um, you know, a lot of these are infrastructure specifically.
[2110.06 --> 2110.34]  Yeah.
[2110.80 --> 2112.34]  Like databases is a big one.
[2112.40 --> 2114.42]  Docker, of course, is infrastructure.
[2114.42 --> 2119.92]  I guess from your perspective, what sets those apart as they are venture backable versus
[2119.92 --> 2123.30]  some of the other projects that you found that were people are, you know, don't have
[2123.30 --> 2124.02]  any support at all.
[2124.94 --> 2125.12]  Yeah.
[2125.24 --> 2129.76]  I think I would love to just have like some, a big map of like all the projects.
[2129.76 --> 2132.66]  Cause I, I see it all in my head and sometimes I have a hard time explaining it.
[2133.16 --> 2139.66]  Um, but I think that it's, it's been hard to find the right term to use besides open source
[2139.66 --> 2144.50]  infrastructure because it, that obviously leaves room for a lot of other projects that
[2144.50 --> 2147.44]  count as infrastructure, but aren't exactly the projects I'm talking about.
[2148.12 --> 2153.32]  Um, I think like stuff around like data infrastructure and DevOps seems to be like fairly well supported,
[2153.32 --> 2155.46]  um, at least as a category.
[2155.90 --> 2163.18]  And so, uh, Sam Gerson saying who is currently at Sidewalk Labs, but, um, he used to be at
[2163.18 --> 2168.56]  A16C and at Imgur and, uh, we've talked about this a little bit and he was saying that in
[2168.56 --> 2172.18]  his mind, the stuff that like doesn't have a great business model are things that don't
[2172.18 --> 2174.36]  directly relate to downtime.
[2175.16 --> 2183.22]  Um, so when let's say like a program language is, uh, is like a system of knowledge or a
[2183.22 --> 2183.98]  system of information.
[2184.46 --> 2191.84]  Um, but there's not the fear that like tomorrow, like a language goes down for like five minutes
[2191.84 --> 2192.38]  or something.
[2193.06 --> 2194.48]  Um, it's good.
[2194.48 --> 2199.00]  And, and so I think things where there is that fear are things that companies are willing
[2199.00 --> 2199.56]  to pay for.
[2199.66 --> 2203.44]  They're probably also easier to measure and kind of like meter out.
[2204.30 --> 2207.92]  Um, so that's kind of like a mental separation for me.
[2208.30 --> 2214.22]  Um, for me, like the, like, I absolutely think that if you have a way to monetize something,
[2214.22 --> 2217.96]  then by all means monetize it because that's awesome.
[2218.14 --> 2218.34]  Right.
[2218.34 --> 2220.46]  Like don't make it harder than it has to be.
[2221.02 --> 2227.68]  Um, but there's so many projects, um, where they just don't have a great business model
[2227.68 --> 2233.50]  besides consulting, which is distracting, um, and not always great for a project.
[2233.92 --> 2237.00]  And it's, those are the projects that I want to support.
[2237.92 --> 2242.20]  Another one that you mentioned in your post, which, you know, is probably the biggest one
[2242.20 --> 2242.70]  is Red Hat.
[2243.52 --> 2243.66]  Yeah.
[2243.80 --> 2249.18]  And, um, you know, Red Hat's been a large business for years now.
[2250.00 --> 2251.38]  What, what makes that one different?
[2251.48 --> 2253.26]  How are they, they seem to be an outlier.
[2253.38 --> 2257.90]  You don't hear about too many Red Hats out there, but any insight on why they were successful
[2257.90 --> 2260.42]  or, or how that whole thing works?
[2260.98 --> 2261.84]  They're a funny one.
[2262.12 --> 2268.02]  Um, I haven't met anybody who thinks that another Red Hat will exist, um, or that it's a
[2268.02 --> 2270.86]  great model to be able to emulate these days.
[2270.86 --> 2278.32]  I think as, as I understand it, I think there's some combination of, uh, they have some complex
[2278.32 --> 2281.36]  stuff around licensing that allows them to charge for things.
[2282.36 --> 2291.00]  Um, they came into their space very early on and managed to capture, um, that market and
[2291.00 --> 2292.48]  make people pay for it early on.
[2292.78 --> 2294.78]  What exactly is their model for the listener's sake?
[2294.86 --> 2299.14]  Like just for those who don't, I mean, not know Red Hat's well known, but what exactly is
[2299.14 --> 2300.54]  their model in plain sense?
[2300.54 --> 2305.12]  As far as I understand it, they charge for services and implementation and things like
[2305.12 --> 2305.50]  that.
[2305.74 --> 2311.04]  Um, and support, support, consulting, things like that around, around this open source
[2311.04 --> 2311.82]  operating system.
[2311.82 --> 2312.02]  Yeah.
[2312.24 --> 2313.56]  Around their Linux distribution.
[2313.72 --> 2314.06]  Yeah, exactly.
[2314.18 --> 2314.64]  Their distro.
[2314.90 --> 2315.06]  Gotcha.
[2315.84 --> 2322.46]  So as far as I can tell, it's the case of somebody coming in early and, um, and owning
[2322.46 --> 2322.84]  it.
[2322.92 --> 2323.10]  Right.
[2323.34 --> 2323.92]  Like Craigslist.
[2323.92 --> 2324.20]  Yeah.
[2325.00 --> 2325.28]  Yeah.
[2325.62 --> 2332.24]  They, they also came at a time when, um, a lot of businesses were very interested in
[2332.24 --> 2339.98]  Linux as, you know, and not paying, you know, licensing, um, to Microsoft and whoever else,
[2340.08 --> 2340.94]  son at the time, I'm sure.
[2340.94 --> 2347.44]  Um, and, and the upside of Linux as a platform, but there was just no way they were going to
[2347.44 --> 2352.78]  invest in Linux without some sort of fallback, you know, because nobody ever got fired for,
[2352.78 --> 2356.40]  you know, putting Windows XP on, on their, on their desktops.
[2356.40 --> 2363.70]  But they needed support for it to even make, like, to get the check off, to get Linux into
[2363.70 --> 2364.34]  their enterprise.
[2365.14 --> 2367.70]  And so the timing, I think, was really good.
[2368.48 --> 2373.16]  And Red Hat was kind of, I mean, my history is not great here either, but Red Hat was kind
[2373.16 --> 2377.88]  of one of the only companies out offering that, you know, that fallback of, okay, now
[2377.88 --> 2380.26]  you can, now you can do this because we have your back.
[2380.90 --> 2386.00]  Um, and nowadays there's just like that fear has kind of fallen more by the wayside.
[2387.04 --> 2387.18]  Yeah.
[2388.10 --> 2388.50]  Yeah.
[2388.60 --> 2392.72]  It's, I mean, there are a couple of companies that are organizations where sometimes their
[2392.72 --> 2396.90]  success is kind of legacy and you're not really sure why, like I think of Wikipedia like this.
[2396.90 --> 2399.32]  I mean, Wikipedia is amazing and does exactly its job.
[2399.96 --> 2404.98]  Um, but they've, you know, it's like the first thing that comes up on search now and Craigslist
[2404.98 --> 2406.44]  has captured their own market.
[2406.62 --> 2410.94]  And within VC, there's like a whole category of companies that are supposedly Craigslist killers,
[2411.20 --> 2415.34]  which it spawned its own, like category of startups that are like trying to take down Craigslist
[2415.34 --> 2416.10]  and like camp.
[2416.76 --> 2422.28]  Um, so yeah, it's, I would definitely call Red Hat another type of outlier like that.
[2423.12 --> 2426.66]  Maybe we could talk about, uh, what it means to be in good shape.
[2427.20 --> 2430.70]  Cause, um, I think that's kind of what we're dancing around here.
[2430.70 --> 2435.58]  Some would say that funding doesn't, isn't the solution, uh, to this problem we have
[2435.58 --> 2436.12]  at open source.
[2436.22 --> 2442.28]  And, uh, in, uh, in your post, we've been talking about, uh, you said open source didn't seem
[2442.28 --> 2443.18]  like it had a problem.
[2443.18 --> 2446.56]  It seemed like it was thriving, but after you did some research, you found out that,
[2446.56 --> 2449.38]  and in quotes, our tools were not in great shape.
[2449.38 --> 2450.44]  What did you mean by great shape?
[2450.48 --> 2452.06]  What is, what does great shape mean?
[2452.10 --> 2454.92]  Does it mean, you know, if there's funding, that's good shape.
[2454.92 --> 2458.00]  What does, what does good shape look like for open source infrastructure?
[2458.72 --> 2459.90]  It's a really good question.
[2460.44 --> 2468.22]  Um, I think that ultimately it comes down to enabling more time on projects.
[2468.76 --> 2472.68]  And I think that money is a way to enable more time.
[2473.08 --> 2480.42]  Um, but ultimately anything around solutions or even just talking about the problem comes
[2480.42 --> 2481.54]  down to a lack of time.
[2481.54 --> 2488.22]  So if you intend to be a project that is entirely volunteer run with a strong community of maintainers
[2488.22 --> 2491.88]  and that's super active, like you need people to donate their time to you.
[2491.90 --> 2492.08]  Right.
[2492.08 --> 2498.84]  Um, if you're a single maintainer who is running a project and you're really frustrated because
[2498.84 --> 2504.28]  you don't have better support, um, it might be about enabling that person to work full-time
[2504.28 --> 2504.68]  on it.
[2505.26 --> 2511.52]  Um, people that want more company contributions, uh, that were company.
[2511.54 --> 2516.34]  Companies are using their project, but their employees don't give back maybe because they're
[2516.34 --> 2519.46]  not allowed to, um, or there's just no culture of it.
[2519.46 --> 2521.54]  Like that's about asking for more time.
[2521.54 --> 2524.44]  So that's kind of the, the lens I've thought about through.
[2524.44 --> 2532.32]  And yeah, in terms of like, when I say that tools aren't in great shape, um, for me, it's
[2532.32 --> 2541.28]  about the whole thing being so decentralized and so relying on goodwill that there's no,
[2541.28 --> 2548.70]  there's no like institutional oversight or stewardship or advocacy for it.
[2548.70 --> 2551.82]  Um, that seems really dangerous to me.
[2552.28 --> 2552.76]  Right.
[2552.84 --> 2555.54]  Like if, if it's everybody's job, it's nobody's job kind of thing.
[2555.62 --> 2555.98]  Exactly.
[2556.34 --> 2556.60]  Yeah.
[2557.12 --> 2558.92]  Um, yeah.
[2558.92 --> 2564.44]  And I, I can't think of like another industry that's so, so important that just runs on like
[2564.44 --> 2565.04]  a complete.
[2565.08 --> 2566.60]  Imagine if banking was like that.
[2566.70 --> 2566.88]  Yeah.
[2566.90 --> 2567.44]  It's crazy.
[2567.44 --> 2567.88]  Yeah.
[2568.96 --> 2573.56]  And it's, um, and I think people are wary of changing things because that's how things
[2573.56 --> 2574.34]  have always been.
[2575.00 --> 2579.54]  Um, or because there's something, there is something really magical and pure and thinking
[2579.54 --> 2584.14]  about this is like a purely volunteer driven endeavor.
[2584.72 --> 2590.02]  So you think time is one of the metrics and what else is, is part of that besides time?
[2590.88 --> 2593.18]  I mean, I think time is like the most important part of it.
[2593.84 --> 2596.60]  Um, what would you say to those who say, well, we've got lots of time.
[2596.60 --> 2597.04]  Okay.
[2597.46 --> 2598.68]  How am I still not in good shape?
[2599.60 --> 2604.44]  I mean, to be fair, like, I think there are certainly some projects that are, um, especially
[2604.44 --> 2610.12]  ones that were, you know, like go for example, where they have, um, company sponsorship effectively
[2610.12 --> 2612.86]  or dedicated full-time employees working on a project.
[2613.36 --> 2617.04]  Um, if they had the time to work on it, then like, that's awesome.
[2617.32 --> 2620.98]  There are plenty of projects in it was that are really, really well supported and are doing
[2620.98 --> 2621.42]  great.
[2621.94 --> 2624.92]  Um, I'm more concerned for the ones that didn't get so lucky.
[2624.92 --> 2627.88]  Um, and I think I mentioned this in this post is that like, I kept hearing the word luck
[2627.88 --> 2629.18]  coming up all the time.
[2629.76 --> 2632.08]  Everybody, people who were happy said they were lucky.
[2632.16 --> 2632.82]  People were unhappy.
[2633.04 --> 2638.20]  They said they were like, um, even people who like had projects that were not well support
[2638.20 --> 2640.18]  at all thought they were luckier than other projects.
[2640.26 --> 2643.30]  And I like, it seems like a lottery.
[2643.74 --> 2644.14]  Yeah.
[2644.22 --> 2645.50]  It's literally like a lottery.
[2646.50 --> 2646.82]  Yeah.
[2646.98 --> 2648.82]  And sometimes people submitted a PR for me.
[2648.86 --> 2649.18]  Great.
[2649.18 --> 2649.62]  Yeah.
[2649.94 --> 2650.18]  Right.
[2650.24 --> 2651.00]  Like I woke up this morning.
[2651.08 --> 2651.48]  Thank goodness.
[2651.58 --> 2652.92]  Somebody like contributed something.
[2653.52 --> 2658.34]  Um, or like, I just happened to know somebody who got me a job working somewhere so that
[2658.34 --> 2659.72]  I can do this full time or whatever.
[2660.60 --> 2665.54]  Um, that has been described on the show before we've had, uh, or several people on here say,
[2665.60 --> 2666.86]  well, I've, I was lucky.
[2666.94 --> 2671.64]  I was able to get a job at joint, for example, to keep supporting NPM or node.
[2671.64 --> 2675.38]  Uh, and that word was used on the show before Jared, as you can probably recall.
[2675.74 --> 2677.12]  And then I say, you're living the dream.
[2677.20 --> 2677.32]  Yeah.
[2677.32 --> 2678.00]  You're living the dream.
[2678.14 --> 2679.28]  And they say, yes, I am.
[2679.34 --> 2679.78]  Yes, I am.
[2681.80 --> 2684.42]  So we're all just in this quacky land thinking it's luck and lottery.
[2685.06 --> 2685.42]  Yeah.
[2685.78 --> 2691.42]  It's, um, and I think this is a distinction that I'd wanted to make earlier of like, we
[2691.42 --> 2696.66]  often talk about coding as art or open sources, art or volunteer based or whatever.
[2697.58 --> 2700.50]  Um, which I think is a really beautiful thing at a conceptual level.
[2700.50 --> 2706.92]  And I think that practically speaking right now, it's not so much, at least the infrastructure
[2706.92 --> 2714.28]  piece of it is not art so much as like these, this is like a highway system or roads or any
[2714.28 --> 2721.16]  sort of like basic city infrastructure where the difference with art, I think is that we
[2721.16 --> 2723.02]  can value it on a cultural level.
[2723.26 --> 2727.14]  But like, if somebody stops painting, like the world is not going to literally crash and
[2727.14 --> 2727.40]  burn.
[2727.40 --> 2735.48]  Um, but if like a major highway is broken or blocked or something like that suddenly changes
[2735.48 --> 2736.64]  like the entire economy.
[2736.82 --> 2737.22]  Yeah.
[2737.22 --> 2745.22]  Um, and so when I think about just like how to better support and kind of like steward
[2745.22 --> 2751.98]  this stuff, um, just having some, someone to pay attention to kind of like the big picture
[2751.98 --> 2757.62]  to be able to think like five or 10 steps ahead instead of everything happening on this,
[2757.74 --> 2763.12]  like what happens tomorrow, what happens the next kind of basis, um, could be largely impactful
[2763.12 --> 2764.28]  to the entire system.
[2764.28 --> 2767.48]  Let me submit another metric.
[2767.66 --> 2769.52]  You said time is, is the main one.
[2769.60 --> 2770.94]  I, I would agree with you.
[2771.14 --> 2777.42]  I think another metric that we think about as developers is, um, the trajectory of a project
[2777.42 --> 2779.74]  or, um, control.
[2779.74 --> 2780.64]  Mm-hmm.
[2780.64 --> 2789.32]  And, um, a lot of times those are trade-offs because we see people, um, you know, starting
[2789.32 --> 2792.60]  off on an endeavor that they created on their own.
[2793.10 --> 2798.36]  Um, and it was, you know, they lacked time to work on it, but they had complete control,
[2798.52 --> 2804.08]  complete ownership, complete, you know, decision-making process in the trajectory of that specific piece
[2804.08 --> 2804.58]  of software.
[2805.68 --> 2809.82]  And then as they hit the lottery, as Adam said, or, you know, when luck was a lady for
[2809.82 --> 2814.22]  them, they thought it was, you know, um, corporate interests come in.
[2814.42 --> 2820.82]  And as you become the infrastructure for all of these money generating, you know, businesses,
[2821.34 --> 2825.42]  they start off, if they do start offering you money, which we've seen that, right?
[2825.42 --> 2827.20]  We've seen corporate sponsorship.
[2827.20 --> 2835.78]  Um, and then you have now multiple interests involved and, you know, what claims does that
[2835.78 --> 2840.12]  company rightly have on your output if they're funding your work?
[2840.60 --> 2848.18]  And so it gets to become a, a difficult and perhaps a, uh, kind of a thorny thing to walk
[2848.18 --> 2853.02]  through as we're finding some projects will dwindle once a corporation comes in and gives,
[2853.16 --> 2854.50]  you know, you think the payday is here.
[2854.50 --> 2858.92]  I can work on this full time and now you start to realize that, you know, there's strings
[2858.92 --> 2859.36]  attached.
[2859.74 --> 2862.02]  So lots of, lots of ins, lots of outs.
[2862.32 --> 2863.76]  I think we have a lot more to talk about.
[2864.28 --> 2865.68]  Um, we got to tee up another break.
[2865.78 --> 2869.88]  On the other side, I want to talk more about that specific point, but let's start talking
[2869.88 --> 2877.24]  about some ideas for solutions because, um, you've definitely stumbled on a big problem
[2877.24 --> 2881.78]  and one that we talk about a lot, but honestly, the solutions are a lot harder to come across
[2881.78 --> 2883.74]  than, you know, just recognizing the problem.
[2883.74 --> 2886.72]  So that'll be a fun conversation and we'll continue it after this break.
[2889.16 --> 2893.24]  Our friends at OpBeat are all about application monitoring for developers.
[2893.24 --> 2896.90]  And today we have some good news for our AngularJS listeners out there.
[2897.36 --> 2901.42]  Great performance metrics should not be limited to server side applications.
[2901.42 --> 2908.74]  So we're excited to say that our friends at OpBeat have opened up OpBeat for AngularJS and they're
[2908.74 --> 2910.76]  accepting beta signups right now.
[2910.92 --> 2916.38]  Head to OpBeat.com slash AngularJS to sign up for this beta.
[2916.80 --> 2917.76]  Here's what you can expect.
[2917.76 --> 2921.54]  You'll see the performance of your application in near real time.
[2921.64 --> 2926.20]  You'll be able to visualize the distribution of route render time so you can isolate edge
[2926.20 --> 2926.62]  cases.
[2927.00 --> 2932.92]  You'll also see a breakdown of your Ajax calls, template rendering, digest, and more.
[2933.18 --> 2937.30]  And you'll also be able to see the actual code, the slowing down your requests.
[2937.74 --> 2940.36]  There's also mobile friendly views for when you're on the go.
[2940.36 --> 2946.96]  And all you've got to do is head to OpBeat.com slash AngularJS to sign up for the beta.
[2950.14 --> 2951.92]  All right, we are back not yet.
[2952.00 --> 2958.00]  But before the break, I was mentioning the tradeoff between funding and control.
[2958.64 --> 2967.06]  This was something that you got a lot of because in your Q&A, one of the common responses is,
[2967.20 --> 2969.28]  I'll just quote it, money will ruin open source.
[2969.28 --> 2972.46]  Open source works because there is no money in the system.
[2973.26 --> 2977.32]  People who contribute are motivated by other things like social reputation.
[2977.48 --> 2980.24]  How do you respond to that kind of a thought?
[2981.04 --> 2987.70]  Yeah, I think the analogy that I put in my response to that is one that has been sticking
[2987.70 --> 2994.16]  in my head, which is within the nonprofit sector, you have people who volunteer their
[2994.16 --> 2994.56]  time.
[2994.56 --> 2999.28]  And I'm sure we've all volunteered our time to some sort of social cause at least once
[2999.28 --> 2999.82]  in our lives.
[3000.86 --> 3006.26]  So for example, if you volunteer at a homeless shelter and you spend your afternoon and evening
[3006.26 --> 3010.64]  playing with the kids in the homeless shelter and you have a lot of fun and then you leave
[3010.64 --> 3012.46]  because you have a day job somewhere else.
[3012.46 --> 3015.84]  And that was like your little contribution to the homeless shelter.
[3016.30 --> 3019.20]  But after you leave, someone else has to like run the shelter.
[3019.40 --> 3022.20]  Someone else has to like actually facilitate everything that's happening there.
[3022.88 --> 3026.52]  Somebody has to be responsible for even like organizing those opportunities for you to
[3026.52 --> 3027.12]  volunteer in.
[3027.12 --> 3033.22]  And so I think like right now when people say open source is just fine, open source doesn't
[3033.22 --> 3037.52]  need any money, whatever, like they're really fixated on the, or they're kind of hoping that
[3037.52 --> 3041.68]  like pure volunteerism is going to sustain a larger cause.
[3041.90 --> 3046.22]  And for me, that's the equivalent of saying like, yeah, if people keep coming in and playing
[3046.22 --> 3050.80]  with the kids every day, then they'll be fine.
[3051.36 --> 3057.58]  But you need some sort of like centralized, a little bit of centralization to have somebody
[3057.58 --> 3060.38]  who's actually like managing and administering all of that stuff.
[3061.20 --> 3063.66]  No, I think that's a definitely a good analog.
[3064.40 --> 3066.70]  And I think a lot of us are volunteers.
[3067.06 --> 3071.44]  And so we see life through the lens of an open source volunteer, you know, just kind of,
[3071.52 --> 3074.86]  especially now that it's become so easy to share.
[3074.86 --> 3078.70]  One thing I was thinking earlier, when you mentioned GitHub being backed by Andreessen Horowitz,
[3079.24 --> 3083.62]  interestingly, Git, right, which is the open source software that GitHub's built upon,
[3083.80 --> 3086.18]  not invested in.
[3086.18 --> 3087.26]  Yeah, totally.
[3087.80 --> 3090.80]  But the proprietary tool built on top of Git is.
[3091.20 --> 3091.42]  Right.
[3091.84 --> 3094.54]  So there you have kind of a demonstration of that.
[3094.82 --> 3097.62]  But, you know, we're used to, a lot of us are just kind of throwing stuff on GitHub.
[3098.24 --> 3099.88]  You know, maybe it's useful, maybe it's not.
[3100.00 --> 3102.04]  Maybe I'm going to support it, maybe I'm not.
[3102.04 --> 3105.90]  And so we see everything through that lens.
[3106.50 --> 3112.50]  But then we also have people like you mentioned who are, they're in it for the long haul, you know.
[3113.80 --> 3116.74]  They're working on it tirelessly day in, day out.
[3116.74 --> 3123.90]  And those kind of efforts tend to be the ones that bring value to more businesses, right?
[3124.00 --> 3126.58]  Because they're sustained efforts.
[3127.88 --> 3132.42]  And so supporting those people is probably where you get the most global bang for our bucks.
[3133.08 --> 3133.26]  Yeah.
[3133.26 --> 3149.74]  There's like one, I don't want to go like deep into a rabbit hole in this, but I guess like I do push back a little bit on the assumption that the success model of open source is building a really large and active community of contributors.
[3150.42 --> 3153.06]  I think when that does happen, that's awesome.
[3153.06 --> 3162.14]  There are plenty of really valuable projects that don't have that, that have one or two maintainers or less than five.
[3162.14 --> 3168.08]  Well, something I've been thinking about during this conversation is that not open source, not all open source is the same.
[3168.60 --> 3169.04]  Exactly.
[3169.22 --> 3169.40]  Yeah.
[3169.64 --> 3179.28]  Like you got the Daniel Stenbergs out there that are totally fine, you know, doing curl, being a fun side project that gets him, you know, work.
[3179.28 --> 3181.72]  And that work also gives back into the open source.
[3181.80 --> 3186.00]  And there's other open source projects that are clearly infrastructure, even though his is also termed as infrastructure.
[3186.14 --> 3194.56]  There's not the same kind of type of project that requires lots of people or infrastructure or funding or, you know, all this difference.
[3194.66 --> 3199.34]  I think that's a clear thing too, is that not open source, not all open source is the same.
[3199.74 --> 3200.14]  Yeah.
[3200.54 --> 3200.80]  Yeah.
[3201.08 --> 3201.70]  And I've heard.
[3201.88 --> 3203.20]  Or has the same requirements to be successful.
[3203.20 --> 3210.54]  I've just heard way too many people saying if they come from like the startup side, they'll be like, well, if the project didn't get funded, it wasn't valuable.
[3210.92 --> 3211.02]  Right.
[3211.08 --> 3217.34]  And then from like the pure open source side, people saying, well, if the project is having a hard time finding contributors, it must not be that valuable.
[3217.56 --> 3223.80]  And that's like something I'm really concerned about people assuming because there are more than enough examples of where that's not true.
[3223.80 --> 3235.50]  I like the parallel that Drew drew earlier, which was if a software product, let's say, you know, like a product, like let's say Twitter, for example, or just something like Twitter, something social like that gets a lot of users.
[3236.16 --> 3236.90]  That's a good thing.
[3236.94 --> 3237.82]  And it attracts VCs.
[3237.82 --> 3253.82]  But if an open source project gets a lot of users, so a lot of dependencies, so to speak, in developer speak, and if a lot of people are depending on this project, that doesn't attract VCs or doesn't attract what might come and support it.
[3254.02 --> 3258.50]  It might attract contributors, but it might not attract anything that can financially sustain it.
[3258.50 --> 3266.68]  Yeah. And even then, like it doesn't always attract contributors, which was kind of funny because it might just be they made people's lives way easier and everyone's so happy to use it.
[3266.94 --> 3272.38]  Or it's something that's like really complicated and that people can't just jump in on and use or and contribute to.
[3272.56 --> 3276.02]  You had a term for that in your first post. I'm trying to think about what that was.
[3276.20 --> 3278.36]  Jared, maybe you can help me out there. There was a term for.
[3279.76 --> 3284.26]  Something where people are just coming and using it versus, you know, not supporting it.
[3284.26 --> 3286.30]  There was a term you used where I thought it was kind of interesting.
[3286.30 --> 3289.40]  Hmm. We would call that a leech where I come from.
[3289.60 --> 3289.92]  A leech.
[3291.14 --> 3293.38]  You called it the free rider problem.
[3293.66 --> 3294.38]  That was a free rider.
[3294.76 --> 3295.84]  Yeah, that's right. Yeah.
[3295.88 --> 3302.50]  Which is like a really well established economic concept that exists in a lot of other places and totally applies here.
[3303.38 --> 3309.50]  I've been circulating or testing out my keystone species term.
[3309.94 --> 3314.84]  So I actually studied environmental studies in school, environmental sciences.
[3316.30 --> 3326.24]  And there's this concept of keystone species in conservation biology where you have like a species that is very small in number, but like the entire ecosystem depends upon them.
[3326.24 --> 3332.18]  And so they get overlooked because it's people think like, oh, there aren't that many of this bird out there or whatever.
[3332.54 --> 3335.92]  But actually, if that bird were to disappear, then like all this other stuff collapses.
[3335.92 --> 3346.26]  And so I've been thinking about projects that need more attention, kind of like that, where you have something that like everybody's using and depending on, but there's only like one or two maintainers.
[3346.76 --> 3351.86]  And if there's two, I think actually someone pointed out there's the bus factor, I guess, is like a similar concept.
[3351.94 --> 3351.98]  Oh, yeah.
[3351.98 --> 3352.10]  Yeah.
[3352.52 --> 3352.72]  Yeah.
[3352.72 --> 3352.94]  Yeah.
[3352.98 --> 3356.84]  We're like, how many do you need to like get hit by a bus before the project goes under?
[3357.82 --> 3359.10]  So, yeah, similar concept.
[3359.82 --> 3371.18]  Well, that's the one thing about open source, which I think is beautiful in certain ways, because as a consultant, as a software contractor, which is my quote unquote day job, you know, people ask me, I'm a very small company.
[3371.18 --> 3373.22]  It's myself and perhaps a subcontractor.
[3373.80 --> 3378.04]  And they say, you know, what happens if we hire you to write this software for us?
[3378.48 --> 3381.90]  What happens if you die or the relationship falls apart?
[3382.50 --> 3386.00]  Well, I tend to make it like they'll say it in nicer terms.
[3386.14 --> 3387.16]  And I'll be like, let's just face it.
[3387.16 --> 3389.08]  If I get hit by a bus, are you guys screwed or not?
[3389.40 --> 3390.32]  That's what you want to know, right?
[3390.70 --> 3391.58]  And they're like, yeah.
[3391.58 --> 3402.82]  And, you know, I tell them how I write everything in open source tools and languages and frameworks in very standard, conventional ways so that it's easy to transition that to somebody else.
[3403.50 --> 3409.48]  And one of the beauties of open source in terms of a business investment is exactly that.
[3409.48 --> 3414.82]  I was thinking earlier when you're talking about art versus infrastructure or highway system.
[3415.10 --> 3415.14]  Yeah.
[3415.88 --> 3419.94]  You know, the analog breaks down with software because it's all, you know, ones and zeros.
[3419.94 --> 3428.28]  And if the person just stops working on that infrastructure, there's absolutely nothing stopping somebody else from just keep working on it.
[3428.94 --> 3436.14]  And so maybe that's an excuse to freeload for a while and have a nice fallback.
[3436.30 --> 3436.78]  I don't know.
[3437.34 --> 3445.78]  But it's definitely a benefit of a reason to invest in open source is because it is, as long as the licenses are permitted, it's transferable that way.
[3446.40 --> 3446.48]  Yeah.
[3446.60 --> 3446.78]  So.
[3446.96 --> 3447.30]  Awesome.
[3447.86 --> 3448.54]  Super interesting.
[3448.54 --> 3449.24]  But I like that.
[3449.84 --> 3459.12]  I like that idea of these, these small species or these, you know, very limited animals that people don't think about as being necessary.
[3459.12 --> 3462.96]  But if they're not there, you know, everything falls apart.
[3463.00 --> 3470.68]  And I think there's definitely individuals out there who are bringing immense amounts of value all around the world and nobody knows about it.
[3471.12 --> 3472.22]  Yeah, definitely.
[3472.22 --> 3476.14]  So we all see the problem.
[3476.52 --> 3480.16]  It's an interesting and a very nuanced thing.
[3481.50 --> 3482.64]  What are some solutions?
[3482.64 --> 3492.96]  It seems like in that case, just like knowing or like bringing those, floating those things up to the top, like this needs help to a certain degree as part of a solution.
[3492.96 --> 3495.10]  Although you still have to have people stepping up to help.
[3495.86 --> 3498.46]  We've also seen efforts like foundations.
[3499.94 --> 3502.40]  We've seen corporate sponsorships to a certain degree.
[3502.40 --> 3505.90]  What are some solutions that are currently being tried?
[3506.02 --> 3510.62]  And then maybe we can all, you know, talk about if we have any other ideas that are worth trying.
[3510.62 --> 3530.32]  So I've kind of thought about solutions categorically, depending on like who actually provides the capital, because it's easier for me to think about like, is it actually possible for somebody to create the solution versus it'd be nice in theory if some magical philanthropist came in and threw a billion dollars at us or whatever.
[3530.32 --> 3530.46]  Right.
[3531.12 --> 3537.48]  So I think about like the people who fund open source, it's other developers or like individual contributions from people.
[3538.40 --> 3545.16]  It's software companies in lots of different ways, whether they hire people full time or they sponsor a campaign or whatever.
[3545.16 --> 3557.18]  And then you have VCs are, play a role in the tech ecosystem that where I think there's more potential there than people realize.
[3558.14 --> 3561.76]  And then you have like philanthropic foundations and governments.
[3562.36 --> 3568.28]  So some of the different areas of funders, I guess, that I can think of.
[3568.28 --> 3583.38]  And so I think like starting with like individual donations, I think that crowdfunding and tipping and bounties and things like that are great, like additions to a funding system.
[3584.04 --> 3586.02]  But not like the basis of success, right?
[3586.02 --> 3586.80]  Yeah, right.
[3586.86 --> 3591.58]  It would be like if we only had Kickstarter for startups and no VC and no financials, it would just be like crazy.
[3591.58 --> 3599.58]  So like I kind of I think that's like really great to like build support, get people involved, but I don't see it as a way to like seriously sustain people.
[3600.32 --> 3611.58]  The biggest areas where I find interesting right now are like who is actually directly benefiting from this stuff and therefore might be more incentivized to give back or contribute.
[3612.52 --> 3616.42]  And those two areas are companies and VCs.
[3616.42 --> 3625.52]  And people have been experimenting with solutions and getting companies to fund projects and lots of different ways.
[3625.62 --> 3634.34]  I think part of the problem is that each like individual campaign or individual project that needs help can feel like a very small piece.
[3635.12 --> 3635.20]  Yeah.
[3635.96 --> 3645.28]  And companies right now, like, I mean, depending on who you talk to, especially in a large company, they might be like, yeah, we would love to contribute, but we have no idea what budget this would come out of.
[3645.28 --> 3648.72]  Like we don't have like we don't have a line item for giving to open source or whatever.
[3649.88 --> 3658.98]  And even on the contribution side, it's like, you know, sometimes there are no policies for employees to be able to contribute on work hours or whatever.
[3659.54 --> 3663.72]  So I think there's like tons of stuff that can happen around working with companies.
[3663.72 --> 3684.78]  I think like what I guess like the ecosystem needs, in my opinion, is some sort of central organization or institution that can kind of like be a place for people to go to when they run into that situation of, you know, lots of people are using this and I don't know what to do next.
[3684.78 --> 3685.78]  Right.
[3685.78 --> 3691.28]  So I think there's value in just having like something in people's minds of like, oh, I know where I can get support.
[3691.28 --> 3710.92]  Um, and I think it also makes it easier for companies and for VCs to understand, like, I can put my money into this thing and then like that thing understands the space better than I do and can help figure out like what's actually needed.
[3710.92 --> 3716.92]  Because like, I don't know, a VC is not going to put money into like a very specific project.
[3717.30 --> 3717.36]  Right.
[3717.64 --> 3725.44]  Um, the, and to be clear, like when I talk about VCs being involved, it's not an investment.
[3725.80 --> 3732.08]  Um, but all VCs have management fees and management fees can, they pay for people's salaries.
[3732.48 --> 3737.84]  Um, but they also pay for things like marketing, travel, events, whatever.
[3737.84 --> 3742.86]  Um, so it's not unusual, I think to, well, that's like a very, very tiny portion of a fund.
[3743.58 --> 3755.56]  Um, it's not like out of the question that, uh, VCs might be interested in supporting the entire ecosystem the way that they might support a platform or something else with like large network effects.
[3755.68 --> 3756.12]  Yeah.
[3756.12 --> 3765.96]  The question is, you know, who, who should fund it, whether it's actual dollars or some sort of other, uh, system of, of, of, of value to give back.
[3765.96 --> 3768.58]  But then the other question is how, right?
[3768.66 --> 3773.40]  So finding out who is kind of easy, then how is, is really the, I think the hard part you're trying to answer there.
[3773.82 --> 3773.84]  Yeah.
[3774.30 --> 3774.58]  Yeah.
[3774.86 --> 3781.90]  So there's some, uh, I, I've been kind of just like going through projects that people have sent to me or, um, that I've collected.
[3781.90 --> 3791.00]  I think there are like certain buckets of things that kind of like work together, like Ruby packaging tools is like, you know, an area of stuff.
[3792.00 --> 3805.02]  Um, there are some projects where it's like, there is one or two specific maintainers where like funding them full time is like a very straightforward thing to do.
[3805.02 --> 3812.32]  Um, and there's other ones where obviously like the project is much more decentralized and there is no organization to fund.
[3812.92 --> 3819.66]  Um, and there are also projects that do have their own foundations or organizations like Django does this or NTP does this.
[3820.24 --> 3822.22]  Um, and those foundations need funding.
[3822.36 --> 3832.46]  So yeah, it's a little bit different for each project, but I think there's like, there's probably less than five ways that people can or need to be funded or supported.
[3832.46 --> 3840.94]  Um, I think actually like leveraging what's great about open source, which is that like people can come in and contribute, um, can be a good thing.
[3840.94 --> 3847.40]  And that like, maybe there is no one maintainer to fund, but maybe you fund somebody to work on the project.
[3848.40 --> 3862.44]  Um, and so I did want to mention Ruby together, which I don't know if you guys have seen, but I think is like a really, really great example of a slightly more centralized place to like think long-term around.
[3862.44 --> 3863.08]  Ruby infrastructure.
[3864.22 --> 3877.52]  And they might not be the only people working on Bundler, Ruby gems or whatever, but you're funding people's work on those projects, which is like a slightly different way of thinking about it versus like, how do I donate money to Bundler or whatever?
[3877.66 --> 3877.82]  Right.
[3878.50 --> 3885.52]  Um, and so I like that it's very output oriented, even though it is about taking in money, but the money is about funding time.
[3885.52 --> 3890.88]  And the output of Ruby together is actually like the time to work on these projects.
[3891.54 --> 3906.66]  What do you think the, going back to the VC side, what do you think the likelihood, so you said it's not out of the question, but you know, what, what do you think the likelihood of VCs actually being interested and actually falling through on, on whether it's a grant system or.
[3907.16 --> 3907.40]  Yeah.
[3907.40 --> 3910.52]  Whatever it happens to be for open source infrastructure.
[3910.66 --> 3911.86]  Is that like a super long shot?
[3912.08 --> 3913.08]  Cause it seems like it would be.
[3913.82 --> 3917.02]  I'm optimistic, but it's my job to be optimistic.
[3917.24 --> 3918.16]  I'm a pessimist.
[3918.86 --> 3919.68]  Yes, you are, Jared.
[3921.22 --> 3922.74]  Well, I mean, I'm looking at.
[3922.74 --> 3923.10]  I didn't say that about it, did I?
[3923.10 --> 3923.14]  Yeah.
[3923.68 --> 3924.30]  It's true.
[3924.50 --> 3926.04]  I'll, let's just, I'll, I'll admit it.
[3926.28 --> 3927.72]  But I'm looking at it from the corporate side.
[3927.80 --> 3930.20]  So like we have seen some corporate sponsorship, right?
[3930.22 --> 3931.02]  It's starting to happen.
[3931.28 --> 3934.52]  And then I asked myself, well, why do they do that?
[3934.56 --> 3942.00]  Because there has to be, it's not, you know, there's no free lunches and it's very difficult to appeal to a corporation for altruistic reasons.
[3942.00 --> 3942.36]  Right.
[3942.74 --> 3945.34]  And I think probably for venture capitalists, it's the same way.
[3945.74 --> 3946.36]  They're capitalists.
[3946.44 --> 3948.72]  They're looking for, you know, ROI, like you said.
[3948.74 --> 3949.38]  It's in their name.
[3950.06 --> 3950.36]  Right.
[3950.58 --> 3952.80]  And in the corporation sense, there's a few angles.
[3952.80 --> 3955.98]  First of all, this is tooling that we use.
[3956.16 --> 3960.02]  And so by providing money for it to get better, our product gets better, our service gets better.
[3960.20 --> 3962.72]  So that's, that to me is a pretty straightforward one.
[3962.88 --> 3964.18]  I see the value there as a business.
[3964.88 --> 3973.18]  Secondly, it's very difficult to attract high quality engineers these days because there's more software to be written than there are good people to write it.
[3973.18 --> 3982.56]  And so by supporting open source and being involved in open source, you're attracting engineers who like open source and work on open source.
[3983.14 --> 3989.56]  And so you're kind of, there's a goodwill factor there, I think, for a corporation to support open source either directly or indirectly.
[3989.56 --> 3998.80]  And so they can see some, you know, on the capitalist side for doing that is that it's, it's, it's making their image better.
[3999.34 --> 4002.50]  From a VC, I just have a hard time finding where the hooks are.
[4002.86 --> 4003.22]  Yeah.
[4003.22 --> 4015.78]  I think she kind of hit it on the head and the open source was worth at least 1.4, well, 143 million of Instagram's billion dollar acquisition because they were able to get to exit half as fast or twice as fast.
[4015.96 --> 4016.84]  I guess not half as fast.
[4017.10 --> 4019.52]  Half as long as it would have taken normally without open source.
[4019.66 --> 4023.62]  One tenth of the value, I guess, was, was the, some of the things you were saying there.
[4023.62 --> 4030.80]  And which is kind of the next topic anyways of, of teeing up how much is open source worth, but it's being able to get to exit faster.
[4030.88 --> 4051.28]  And I think that's probably the biggest, if anything, uh, attraction to VCs is like, Hey, if we can fund a company and they can be built on open source that we're helping thrive through, whether it's money, whether it's time, whether it's, you know, developer support or whatever we can come up with and we can get to exit faster or get to return faster, whatever that is.
[4051.28 --> 4053.32]  Then that's, that's going to be lucrative.
[4053.94 --> 4054.38]  Yeah.
[4054.72 --> 4055.14]  Yeah.
[4055.18 --> 4057.36]  I think there are two ways of looking at it.
[4057.40 --> 4060.48]  Like one is that companies are much closer to open source.
[4060.64 --> 4064.26]  Therefore they're, they feel the pain more acutely and they're more likely to fund.
[4064.88 --> 4076.78]  Um, another way of looking at it is that they're too close to open source where they are like the direct beneficiary and no one company might be as motivated to act because they might worry about things like competition.
[4076.78 --> 4084.78]  Um, which I've heard from some projects where companies say, well, if we're funding your project, then aren't we also funding our competitor software and whatever.
[4085.62 --> 4090.40]  Um, VCs have a unique role, I think, in that they're, they're one step above it.
[4090.52 --> 4094.48]  Um, they're a little bit more neutral than any one individual company can be.
[4094.78 --> 4104.82]  They're really interested in the entire landscape and VCs are interested in, they're also interested in being the first to know about anything.
[4104.82 --> 4107.70]  Um, they always want to know something that nobody else knows.
[4107.70 --> 4111.70]  There's this whole like information asymmetry that's in play, which is like super fascinating.
[4112.00 --> 4114.48]  Definitely the weird and wonderful stuff I was referring to.
[4114.86 --> 4114.90]  Yeah.
[4115.24 --> 4122.34]  Um, and it's in their benefit to better understand something that can help them predict the future essentially.
[4122.54 --> 4122.72]  Right.
[4123.10 --> 4129.20]  Um, whether or not VCs actually predict the future, but they want to feel like they can, they know something.
[4129.26 --> 4129.46]  Yeah.
[4129.50 --> 4130.08]  They know something.
[4130.16 --> 4130.62]  No one else is.
[4130.62 --> 4134.34]  Um, and I think like competitive edge.
[4134.62 --> 4135.02]  Totally.
[4135.38 --> 4135.56]  Yeah.
[4136.06 --> 4138.42]  And it benefits like all of their portfolio companies.
[4139.12 --> 4146.96]  Um, but even in thinking about, you know, like what are the next interesting things or the things that might be happening that we don't even realize is going to happen.
[4147.58 --> 4152.90]  Um, you can like think about how like open source has changed so many and shaped so many startup trends.
[4152.90 --> 4162.12]  I mean, just in making startups cheaper themselves, they, that ended up spawning like the growth of all these micro VCs, like very small fund VC firms.
[4162.34 --> 4162.54]  Yeah.
[4162.54 --> 4167.94]  Um, and the rise of angel investors because it was so much cheaper to put money into a startup.
[4168.16 --> 4173.98]  So because of open source, um, therefore like investing itself changed completely.
[4174.82 --> 4182.92]  Um, just the rise of consumer apps like Instagram, which could not have scaled the way they did or reached as many people as they did.
[4182.92 --> 4186.26]  Um, without having open source to back that up.
[4187.26 --> 4193.06]  Um, I mean, just like the explosion of people learning how to code and all the business related stuff that came from that.
[4193.46 --> 4194.48]  I love that.
[4194.48 --> 4197.02]  Uh, parallel you drew there too, with, uh, how.
[4197.76 --> 4200.78]  This entire topic we're talking about, which is essentially becoming.
[4201.20 --> 4203.22]  Open source becoming more and more prolific.
[4203.54 --> 4212.90]  Uh, how that's also spawned, uh, teaching kids to, to code or people getting into code earlier, sooner, or the world becoming a world of coders.
[4212.92 --> 4213.40]  Basically.
[4213.88 --> 4214.16]  Yeah.
[4214.28 --> 4214.88]  I love that.
[4215.70 --> 4216.42]  It's awesome.
[4216.66 --> 4216.86]  Yeah.
[4216.98 --> 4225.90]  It's, and there's so many like really, really tangible effects that if I think people understood the effects of open source better, maybe you can help stay ahead of those things a little bit.
[4226.22 --> 4232.62]  Um, and it's so easy, of course, like look back and say, well, of course, open source, like help change all these things.
[4233.02 --> 4235.74]  Um, and sometimes you don't always know in the moment what's going to happen.
[4235.88 --> 4237.34]  There's so many intangible benefits, you know?
[4237.74 --> 4238.00]  Yeah.
[4238.00 --> 4242.90]  It's, I mean, when I was trying to just like, even like measure the value of it financially, I was just like boggling.
[4242.92 --> 4244.24]  All the ways it could have gone.
[4245.14 --> 4250.34]  So, yeah, I think there's value for VCs to be closer to that, especially now that open source is not a word that.
[4251.42 --> 4257.20]  People still are confused when they hear the word open source or they pretend to know what it is or whatever.
[4258.00 --> 4264.54]  But at least it's not like as unusual of a term as it was even like five years ago among like non-developer people.
[4264.82 --> 4266.88]  They can say like Forrest Gump. It's a household name.
[4268.40 --> 4271.76]  That's what it's become. It's become a household name. Everybody knows open source.
[4271.76 --> 4274.46]  Right. At least in theory, they kind of get what it's about.
[4275.00 --> 4277.88]  Everyone in tech knows there's a whole lot of people that have no idea.
[4279.98 --> 4281.10]  We're in a bubble here.
[4283.20 --> 4289.08]  Let's pause there. Since we're opening up the whole, unless Nadia, you got a point that I want to cut you off.
[4289.20 --> 4292.46]  I do want to kind of swing us into our next point, our next topic.
[4293.34 --> 4294.66]  Is there anything you want to cover real quick?
[4294.74 --> 4295.02]  I'm good.
[4295.36 --> 4300.36]  Okay. So the next topic we're going to talk about after this break is we're going to try our best.
[4300.36 --> 4304.20]  And Nadia, you've done it a day ago on Medium.
[4304.46 --> 4310.90]  You posted a post called Open Source was worth at least $143 million of Instagram's $1 billion acquisition.
[4311.10 --> 4313.66]  So we're going to talk about what Open Source is worth.
[4314.10 --> 4315.18]  You've calculated it.
[4315.24 --> 4316.82]  You've done some math.
[4316.92 --> 4320.00]  So hopefully you can school us as best you might be able to.
[4320.58 --> 4322.04]  Let's do that after the break, though.
[4322.04 --> 4322.72]  So we'll be right back.
[4322.72 --> 4328.62]  Here at the Change Law, we have two emails we'd love for you to subscribe to.
[4328.70 --> 4330.68]  The first is Change Law Weekly.
[4331.18 --> 4333.28]  Now, we've been shipping this email for several years now.
[4333.38 --> 4335.08]  We ship it every single Saturday morning.
[4335.66 --> 4338.32]  It's everything that hits our open source radar.
[4338.46 --> 4344.30]  It's our editorialized take on what happened this week in open source and software development.
[4344.30 --> 4347.92]  Go to changelaw.com slash weekly to subscribe.
[4348.64 --> 4350.94]  And our second email is changelaw nightly.
[4351.04 --> 4359.60]  Every single night we ship this email out covering all the top new and top star repos on GitHub at 10 p.m. Central Time.
[4360.24 --> 4362.78]  It's all the latest stuff on GitHub before it blows up.
[4362.86 --> 4364.28]  It's often our own radar.
[4364.52 --> 4371.56]  We're often creating shows and finding new people, finding new projects, putting things on our own radar based on what we find in there.
[4372.12 --> 4373.62]  So we'd love for you to subscribe to that.
[4373.62 --> 4375.82]  Head to changelaw.com slash nightly.
[4376.06 --> 4377.48]  And now back to the show.
[4381.14 --> 4382.46]  All right, we're back from our break.
[4382.50 --> 4384.62]  And we've kind of been talking about all sorts of stuff.
[4384.64 --> 4387.20]  We've been talking about, you know, sustainability open source.
[4387.28 --> 4397.86]  We talked about, you know, if it is venture backable, if it is worthy enough to fund, give time to it, whatever solution we can kind of piggyback off of.
[4397.94 --> 4400.16]  We kind of talked about who should fund it.
[4400.18 --> 4402.88]  We talked about some ideas on how they can fund it.
[4402.88 --> 4407.96]  And I guess if you're thinking about who and how, you might think about how much is it worth.
[4407.96 --> 4424.76]  So, Nadia, in this really great post a day ago, which is awesome, you calculated how much open source software infrastructure is actually worth to a company and use the now infamous Instagram as its lens, for example, for your example.
[4424.76 --> 4428.42]  And that spawned a blog post titled Open Source's Worth at least one point.
[4428.52 --> 4429.72]  Or sorry, I keep saying one point.
[4429.94 --> 4433.30]  It's $143 million of Instagram's billion-dollar acquisition.
[4433.82 --> 4435.76]  And the term Instagram has become sort of coined.
[4435.90 --> 4436.96]  Everybody knows it now.
[4436.96 --> 4444.78]  And it's being used countless times to describe how many billions a company paid for in terms of an acquisition for a company.
[4445.22 --> 4455.26]  Did you ever track down, by any chance, this is sort of an opening topic to this, but did you ever track down how much money Instagram had given back or invested into open source as part of this research for this article?
[4455.26 --> 4461.84]  Yeah, as far as I know, they are not regular contributors to any open source projects.
[4463.14 --> 4468.00]  They do list the projects, at least some of the projects that they use on their app and on their website.
[4468.22 --> 4470.58]  So no evidence that they've actually funded anything?
[4471.10 --> 4473.42]  To my knowledge, they do not.
[4473.58 --> 4475.28]  So it's not saying no, it's just nothing we've found yet.
[4475.68 --> 4476.66]  Nothing I've found yet.
[4476.66 --> 4483.28]  Yeah, and I do know from some specific projects they've used that those projects have confirmed that they've never given anything to them.
[4483.72 --> 4483.84]  Gotcha.
[4484.54 --> 4486.36]  So how much is it worth then, open source?
[4487.08 --> 4488.24]  Gosh, I wish I knew.
[4489.74 --> 4493.20]  How'd you come to this one specifically, the $143 million?
[4493.52 --> 4494.96]  I took the easy way out on this one.
[4495.48 --> 4502.78]  And I figured I would lowball it because then at least if that lowball is a big number, then we can all agree it's at least worth that much.
[4502.88 --> 4503.12]  Right.
[4503.12 --> 4522.82]  Yeah, this question came up for me because as I was just talking to lots and lots of different people in the space, realizing that everything was sort of anecdotal, lots of stories of people on the ground feeling something, but not a lot of metrics or figures around the value of open source.
[4522.82 --> 4525.86]  There's just not a lot of data out there about it.
[4526.56 --> 4528.76]  And I wanted to start trying to calculate that myself.
[4528.86 --> 4540.64]  I think that's actually very telling that there isn't a lot of data, which suggests that people haven't taken the interest in open source that they should have at this point from kind of like the analyst perspective.
[4540.64 --> 4570.62]  Mm-hmm.
[4570.64 --> 4570.86]  Exactly.
[4571.18 --> 4571.38]  Yeah.
[4571.58 --> 4577.62]  And I mean, because there's just like so many projects too that like how can you even count them all up and inventory them all properly?
[4578.60 --> 4585.60]  And so I tried taking with just focusing on Instagram and I picked Instagram because it's famous for this billion dollar acquisition.
[4585.60 --> 4589.84]  And also because it had this like very short time to exit.
[4589.98 --> 4591.34]  It was only two years.
[4591.78 --> 4594.60]  Most venture-backed companies take seven to 10 years to reach an exit.
[4595.92 --> 4596.94]  So it was very short.
[4597.24 --> 4603.04]  And part of that was because they got like a million users, I think, in the first three months.
[4603.04 --> 4607.76]  And they were able to scale to that demand very, very quickly and keep growing and growing.
[4608.72 --> 4611.06]  So to create something extremely valuable in a short period of time.
[4611.94 --> 4618.66]  And one of the co-founders, Mike Krieger, has written a couple of times about like how valuable open source was to Instagram.
[4619.58 --> 4621.32]  So I tried a couple of different things.
[4621.38 --> 4627.88]  My first thought had been to, because I knew they'd been so transparent about their stack, I was going to just like list out all the projects they used.
[4627.88 --> 4634.18]  And then imagine if you had to pay for each of those things, then like what would that be worth it to them?
[4634.38 --> 4636.72]  But then I realized like way too many projects.
[4638.68 --> 4640.92]  Plus pricing and software is another, you know.
[4641.26 --> 4642.12]  Yeah, right.
[4642.14 --> 4643.26]  It's another hard thing to do.
[4643.72 --> 4644.32]  Taken forever.
[4644.88 --> 4651.80]  I was thinking about just thinking of it as like a time thing of like how long would it take to build all that stuff themselves.
[4651.80 --> 4659.84]  But that's also pretty hard for me to imagine because I don't know every single thing that's needed from say like a DevOps angle or whatever.
[4660.72 --> 4661.66]  So I didn't do that.
[4662.68 --> 4670.24]  And yeah, I got, I really was just like stumped on it, which was frustrating because I was like, how can I not even do this for one company?
[4670.92 --> 4677.44]  But I got lucky because my partner is just like way better at estimating shit than I am.
[4677.44 --> 4695.00]  And I asked him for help because I was desperate and we were thinking about kind of like, all right, what about that time to exit idea of, okay, if we can say that open source cut their time to exit in half, money degrades over time, becomes less valuable over time.
[4695.44 --> 4701.16]  So that billion dollars must be worth more within two years than it would have been in four years.
[4701.16 --> 4708.90]  And so I just calculated the present value of the billion dollars in a two-year time frame versus a four-year time frame.
[4708.98 --> 4711.26]  And the difference between the two was 143 million.
[4712.54 --> 4714.90]  And we went like super conservative on that.
[4715.10 --> 4719.06]  I think open source probably cut down their time to exit by way more than that.
[4719.64 --> 4726.08]  You can even make the argument that like a company like Instagram couldn't even exist if open source hadn't been around.
[4726.08 --> 4728.60]  How many people did they have on their team overall?
[4728.72 --> 4731.88]  I think they had two founders and what was their total team size overall?
[4732.44 --> 4733.08]  I think it was 13.
[4733.56 --> 4737.42]  So it'll probably have to be three times that to build that kind of infrastructure on their own.
[4737.80 --> 4744.28]  And then all the cycles it would take to actually think through the problems that open source provided them.
[4744.90 --> 4751.50]  And from the business angle too, like having to think through monetization stuff if they had been around longer, you'd have to hire people.
[4751.86 --> 4754.06]  Yeah, their Burmy would have been much higher for longer.
[4755.06 --> 4755.24]  Yeah.
[4755.24 --> 4763.12]  Plus they were experiencing like extreme network effects, which if you can't keep up with that, you're not just slowing down your growth.
[4763.26 --> 4766.56]  You're actually destroying the effect.
[4767.20 --> 4767.60]  Exactly.
[4768.88 --> 4769.96]  Yeah, I mean every...
[4769.96 --> 4771.98]  Early on, they had a hard time keeping up.
[4772.18 --> 4774.24]  And when they weren't available, people were...
[4775.06 --> 4775.34]  Moving on.
[4775.80 --> 4777.54]  Moving on or what have you.
[4777.94 --> 4778.14]  Yeah.
[4778.82 --> 4779.06]  Yeah.
[4779.06 --> 4788.00]  I mean, I think like that entire category of companies that we call audience-based apps and venture, I mean, they couldn't even really exist without open source.
[4788.64 --> 4791.60]  So, and those are also the ones that get like kind of crazy valuations.
[4791.60 --> 4796.78]  So, I could not even begin to estimate how much open source is actually worth.
[4797.48 --> 4801.08]  I've had other people quote billions to me.
[4801.08 --> 4804.54]  I haven't done the math out myself.
[4804.54 --> 4818.24]  But I figure that if we can say that open source is worth at least $140 million to one company, then it is absolutely worth like, you know, $50 million to support or whatever it is.
[4818.24 --> 4821.80]  What's the percentage of that number to their billion?
[4822.02 --> 4823.82]  I didn't do the math, but maybe you have.
[4824.38 --> 4828.54]  Because if that's a metric, we can say at least, you know, let's say it's 2%.
[4828.54 --> 4829.70]  I'm just totally just guessing.
[4829.96 --> 4830.66]  Isn't that 14%?
[4830.82 --> 4831.54]  14, yeah.
[4831.78 --> 4831.98]  Yeah.
[4832.06 --> 4832.68]  14%.
[4832.68 --> 4833.72]  I was like way off.
[4834.46 --> 4836.80]  And my basic math try there.
[4837.26 --> 4845.08]  So, if it's 14%, if we said that every company out there that gives back to open source, if they gave a conservative number, 10%.
[4845.08 --> 4850.94]  And I even said here in our notes, Jared, it's so funny it comes out to actually be 10% because I didn't do the math.
[4851.08 --> 4858.16]  But using a quote from you, Nadi, you said a company using open source infrastructure can launch a scale today for one-tenth of the cost.
[4858.16 --> 4874.38]  And so, it seemed logical to me that if that's some sort of medium value we can actually apply to it, then if anyone is out there using open source, any business out there using open source to build their business, they should tithe back 10% to the greater open source ecosystem.
[4874.38 --> 4878.58]  And that could be a good number that would at least be conservative to a degree.
[4878.80 --> 4879.56]  Maybe you work up to there.
[4879.60 --> 4880.66]  Maybe it's 2% at first.
[4880.72 --> 4881.52]  Maybe it's 5%.
[4881.52 --> 4882.34]  And then it's 8%.
[4882.34 --> 4884.58]  And ultimately, the goal is 10% at least.
[4884.86 --> 4888.66]  If you gave back that amount to fund open source, maybe that could help.
[4889.06 --> 4890.10]  Maybe that could be a way.
[4890.94 --> 4891.10]  Yeah.
[4891.24 --> 4892.14]  I mean, I agree.
[4892.22 --> 4897.44]  I think 10% is super conservative, which I think is good because why not start low?
[4897.44 --> 4902.60]  But even if you said, all right, 10% is crazy high, only 1%.
[4902.60 --> 4905.42]  1% of every company is still a ton of money.
[4906.16 --> 4906.26]  Right.
[4906.76 --> 4907.56]  We'll be totally rad.
[4907.70 --> 4909.56]  We're going to start getting into politics here.
[4909.74 --> 4910.08]  Oh, boy.
[4911.50 --> 4915.46]  Because you've got to incentivize businesses to do the quote-unquote right thing.
[4915.94 --> 4916.12]  Right.
[4916.12 --> 4921.86]  And some businesses, 10%, with their specific case, that's nothing.
[4922.32 --> 4924.58]  I mean, it's a lot of money, absolute money.
[4924.72 --> 4926.12]  But to them, relatively small.
[4927.18 --> 4928.24]  Other companies can't.
[4928.36 --> 4930.08]  10%, that's their profit margin, right?
[4930.14 --> 4930.28]  Totally.
[4930.28 --> 4931.94]  So that puts them out of business.
[4932.36 --> 4934.82]  So we're talking about operational or bankruptcy.
[4934.82 --> 4937.16]  Well, that's why you could start low at 1% or 2%.
[4937.16 --> 4937.88]  Right, right, right.
[4938.00 --> 4947.76]  But if you could offset it somehow with some sort of tax break when you give to open source, the government then gives us a percentage of that as a tax break.
[4947.92 --> 4951.12]  Or I guess it would be pre-net anyways.
[4951.38 --> 4952.40]  Yeah, you did get a poll.
[4952.40 --> 4953.30]  Get in over my head.
[4953.94 --> 4954.90]  Just think out loud.
[4954.98 --> 4955.84]  We're solutionizing.
[4956.08 --> 4957.04]  Let's think out loud a little further.
[4957.14 --> 4958.46]  I've got a thought on this note here.
[4958.46 --> 4961.18]  So if we were talking about this how, right?
[4961.26 --> 4962.60]  We got the who.
[4962.82 --> 4964.20]  We got the potentially how much.
[4964.20 --> 4966.62]  And now we got how can someone give back?
[4967.28 --> 4978.34]  And since open source is already in the open, what if we had some sort of open community-ran system that allowed people to apply essentially and say, here's my project.
[4978.34 --> 4986.06]  It's on a known repo host like GitLab, GitHub, whatever is recognizable, Bitbucket.
[4986.92 --> 4988.08]  Here it is.
[4988.42 --> 4989.50]  Here's the contributor metric.
[4989.60 --> 4993.38]  There's some sort of statistical analysis you could do from contributions.
[4993.38 --> 4999.12]  You know, there's all these different tools out there that can show you like open issues and like velocity and all these different things.
[4999.22 --> 5004.56]  What if there was some sort of place we can submit that and say, hey, could we get some money to support it?
[5004.70 --> 5007.64]  And, you know, again, maybe it's just buying time versus money.
[5008.22 --> 5013.60]  Maybe that's somehow, you know, a basic unthought through solution.
[5014.38 --> 5014.48]  Yeah.
[5014.94 --> 5016.78]  That's where my brain is at right now.
[5016.88 --> 5017.16]  Okay.
[5017.16 --> 5018.06]  Tell us more then.
[5018.06 --> 5018.78]  Yeah.
[5018.78 --> 5025.12]  I hear something of that sort come up from a lot of people in this space.
[5025.12 --> 5032.90]  And to me, it speaks to the need to have, again, just like something a little bit more centralized that's at least taking responsibility.
[5033.28 --> 5035.22]  They're not owning the space in any shape or form.
[5036.14 --> 5046.40]  But there's just somebody who's dedicated there to think about like not just code, but kind of like all the things you have to do to support the time to spend on code.
[5046.40 --> 5046.44]  Yeah.
[5048.26 --> 5055.48]  And, yeah, I think like the part that would need to be discussed is a couple of things.
[5055.56 --> 5058.42]  Like one is that obviously like every community is different, right?
[5058.52 --> 5061.68]  Like Ruby's needs are really different from Python's needs or whatever.
[5061.92 --> 5062.04]  Right.
[5062.04 --> 5071.86]  And so it's odd, I guess, to bring them all under one umbrella while also respecting the individual needs and differences of each community.
[5072.30 --> 5074.82]  So that's one thing I've kind of been thinking through.
[5074.96 --> 5085.48]  And the other is how do you make it so that it's not overly risky to centralize like all the decision making into one entity?
[5085.76 --> 5086.24]  Right.
[5086.24 --> 5098.80]  So it's and I love Ruby to see others governance model in this where they have a volunteer board where no amount of money you can give can give you more votes and picking that board.
[5099.50 --> 5101.48]  So I think there's some good precedent for that.
[5102.62 --> 5112.10]  One thing that I was talking about with a friend this weekend was angel list syndicates, which are a way to angel invest more money with startups.
[5112.10 --> 5117.80]  And so basically you have like one angel investor who says, I'm putting 100K into this startup.
[5118.26 --> 5125.34]  And a whole bunch of other people who have committed to that angel syndicate can say, oh, I want to do the same thing.
[5125.34 --> 5127.48]  And I'm going to also put in 50K or whatever.
[5128.36 --> 5141.48]  The idea is that like it's partially about that one angel being able to put in more money than they might have been able to do themselves because they're sort of like crowdsourcing other funding.
[5141.48 --> 5141.76]  Right.
[5141.76 --> 5144.26]  But it's also a little bit about vetting.
[5144.26 --> 5154.56]  And it's also a little bit about like having something that's, I guess, just like sources more ideas from the community or more vetting for the community.
[5154.94 --> 5155.88]  And I thought you said betting.
[5156.02 --> 5156.84]  I was going to actually clarify.
[5157.06 --> 5158.98]  You said betting or vetting because it's almost like I'm just kidding.
[5159.50 --> 5160.00]  With a V.
[5160.00 --> 5169.20]  And so I like the idea of saying, OK, like what if like the institution and a centralized institution can provide a certain amount of capital?
[5169.20 --> 5175.04]  And even that capital should come from a lot of different sources so that, you know, nothing is everything is a little bit de-risked.
[5175.04 --> 5175.26]  Right.
[5175.26 --> 5188.50]  But you could have that and you could also have like a crowdfunding campaign or whatever or just people who are very engaged on this topic and interested that also put in a show of support and small amounts of money.
[5189.02 --> 5202.42]  And it could be a nice way to ensure that like not only is it coming from different funding sources and they're kind of helping each other out, but like individual developers do have a voice in there or anyone else they want to have involved.
[5202.82 --> 5203.36]  Does that make sense?
[5204.26 --> 5204.84]  Makes sense.
[5205.66 --> 5206.34]  Yeah, it makes sense.
[5206.44 --> 5209.46]  I mean, I feel like there's a lot of struggles in there.
[5209.56 --> 5214.40]  I feel like there's a lot of opportunities for corruption or for.
[5214.80 --> 5215.10]  Yeah.
[5215.80 --> 5218.44]  I think just like you open up a whole new.
[5219.98 --> 5220.80]  What is it called?
[5220.92 --> 5221.50]  Sack of worms?
[5221.76 --> 5222.36]  Can of worms.
[5222.48 --> 5223.04]  Can of worms.
[5223.56 --> 5224.34]  Can of worms.
[5226.38 --> 5230.36]  Which, I mean, those are other problems to solve inside there.
[5230.62 --> 5234.56]  But, you know, whenever I think centralized and open source, they're kind of at odds.
[5234.56 --> 5235.12]  Yeah.
[5235.12 --> 5236.40]  In their spirit.
[5237.12 --> 5241.46]  You know, we love distributed version control systems because of the distribution side of it.
[5241.60 --> 5243.60]  We like things like federations, right?
[5244.72 --> 5246.70]  That being said, you know, we all also love GitHub.
[5246.70 --> 5253.40]  So if it's good, if it's good enough, we'll set aside our convictions for the awesomes.
[5253.76 --> 5254.90]  At least for a time.
[5255.32 --> 5256.26]  Yeah, at least for a little bit.
[5256.26 --> 5259.10]  And we'll all think to ourselves, is this really something that we should be doing?
[5259.10 --> 5262.16]  So, yeah.
[5262.24 --> 5267.38]  I mean, I guess that's a bit of a truism to say, you know, where the money is, you know, you'll have more problems.
[5268.08 --> 5275.88]  And so when you centralize an effort around funding, you know, that's going to be gamed all sorts of different things.
[5275.88 --> 5278.58]  That's why I want to be really careful around it because, yeah.
[5279.32 --> 5284.16]  It should be as, like, democratic distributed as is reasonably possible.
[5284.54 --> 5284.70]  Right.
[5285.08 --> 5287.16]  But even in the U.S., you know, we have a representative democracy.
[5287.30 --> 5288.94]  We don't have direct democracy for a reason.
[5289.44 --> 5289.74]  Right.
[5289.74 --> 5290.06]  Yeah.
[5290.46 --> 5290.70]  Yeah.
[5291.32 --> 5298.60]  So are you interested in this, like, in terms of ideation or, like, you know, spawning ideas?
[5298.60 --> 5306.26]  Or is this something that you're actually, like, looking at as a possible endeavor of yours or people that you are in your network moving forward?
[5307.12 --> 5307.92]  I think definitely the latter.
[5309.50 --> 5319.16]  My primary interest in this stage, I guess, is a little bit more journalistic of, can we at least start talking about these issues in a centralized way?
[5319.74 --> 5323.22]  And I think the natural next step of it is, like, what do we do about it?
[5323.48 --> 5323.64]  Yeah.
[5323.64 --> 5330.32]  And when I started writing and talking about this stuff, I was, I first want to make sure that people even care.
[5331.78 --> 5335.68]  Because I was like, well, maybe I'll write about it and no one cares and no one thinks there's a problem.
[5335.88 --> 5336.16]  Wrong.
[5336.36 --> 5336.84]  Right.
[5337.20 --> 5337.90]  Everybody cares.
[5338.46 --> 5339.20]  Everybody cares.
[5339.20 --> 5346.58]  And so if everybody cares and no one who, like, really, really, really cares has the time to think about it, then, like, I'll think about it.
[5347.62 --> 5348.38]  That's why I'm here.
[5348.38 --> 5355.52]  So, yeah, I'm definitely interested in actually making something different and actually proposing a solution.
[5356.38 --> 5358.72]  So expect to hear more about that for sure.
[5359.52 --> 5368.50]  Aside from your history and the perspective which you have, which I think is unique in our space, you say that's why you're here.
[5369.64 --> 5371.08]  You quit your job in May.
[5371.14 --> 5374.26]  You mentioned that some of your writing is funded by the Ford Foundation.
[5374.26 --> 5377.72]  Can you kind of explain, like, I always think of sustainability, like, on your side.
[5377.86 --> 5380.72]  Like, how do you go about doing this and live a life?
[5380.98 --> 5381.26]  So, yeah.
[5382.10 --> 5385.08]  So share with us kind of, like, your thoughts on that side of it.
[5385.90 --> 5386.08]  Yeah.
[5386.08 --> 5395.62]  I joked with a couple people that, like, the headline a year from now is going to be that, like, I tried to figure out how to fund open source and then I ran off funding myself.
[5396.04 --> 5396.52]  Right.
[5397.54 --> 5398.44]  Definitely happened.
[5399.06 --> 5399.48]  That's funny.
[5400.04 --> 5400.30]  I don't.
[5400.46 --> 5401.10]  It is funny.
[5401.54 --> 5402.26]  Sad, but funny.
[5402.26 --> 5409.36]  I'm not, like, overly concerned about money in general, I guess.
[5410.56 --> 5413.40]  As long as I pay my bills, I'm super happy.
[5413.70 --> 5419.08]  So I'm really, really grateful to the Ford Foundation for having even enabled this, the beginning of this journey.
[5419.08 --> 5426.36]  I have no idea where money will come from, but I'm trying not to think too much about it.
[5427.04 --> 5437.34]  I have enough savings right now that I'm not, like, I'm not going to sacrifice something I'm really interested and curious about for just to be able to pay my bills.
[5438.18 --> 5438.20]  So.
[5438.56 --> 5443.44]  So if you don't mind me asking, like, what is the Ford Foundation and, like, what are they?
[5443.56 --> 5446.44]  I mean, obviously they're paying you to write or to do research or something.
[5446.44 --> 5450.52]  Yeah, so they helped fund the initial research for this.
[5451.46 --> 5457.52]  The Ford Foundation is a very large family foundation of Ford Motors fame.
[5458.94 --> 5463.10]  They're, I think, the second largest after the Gates Foundation in the country.
[5463.98 --> 5466.22]  They have a really great internet freedom division.
[5466.22 --> 5477.90]  So that division is thinking about different ways to, that philanthropy can help ensure that the internet is still everything that we intended it to be when it started.
[5477.90 --> 5485.32]  And so a lot of that is about, I don't really want to speak on their behalf, I guess, but.
[5485.50 --> 5485.76]  Sure.
[5486.16 --> 5494.42]  But just about, like, privacy and policy and just making sure that the internet is, like, a democratic place.
[5494.42 --> 5496.92]  And so this kind of falls into that.
[5498.74 --> 5515.66]  And so I've been, they definitely, like, took a chance on this idea when I think a lot of other people thought it was still a little bit crazy or didn't really understand why open source was, you know, worth talking about or had any sort of issues in the first place.
[5515.66 --> 5522.88]  Which I think can happen if you're, like, working so deep in tech that you might not think about, like, what's happening under the hood.
[5523.72 --> 5535.06]  So I think part of them being more around, like, higher level concepts of internet and democracy made them really enthusiastic about this topic.
[5535.64 --> 5537.84]  So I'm, yeah, I'm really grateful to them.
[5538.16 --> 5539.08]  How did you find it?
[5539.14 --> 5544.44]  I mean, I know they have a grants database that you can look through that you know about it, that somebody approached you.
[5544.44 --> 5546.90]  I got, I got very lucky.
[5547.14 --> 5547.88]  I will use that term.
[5548.06 --> 5548.32]  A lottery.
[5548.80 --> 5549.72]  There it is again.
[5550.58 --> 5550.94]  Luck.
[5551.12 --> 5551.88]  Pure luck.
[5552.36 --> 5557.44]  Yeah, we got put in touch by a mutual friend and just had a really good conversation around it.
[5558.34 --> 5565.56]  Well, I think the next topic we should talk about, hopefully we have enough time for this because we are getting close to our time.
[5565.64 --> 5566.94]  I don't know how much time you have, Nadia.
[5567.04 --> 5567.64]  I didn't even ask you.
[5567.72 --> 5567.92]  That's so good.
[5568.28 --> 5568.56]  Okay.
[5568.56 --> 5578.30]  I don't think it would make sense to close this call without talking about what would happen if we leave the sustainability of open source unchecked.
[5578.34 --> 5580.22]  So we talked about the problems.
[5580.34 --> 5586.38]  We talked about, you know, what a, you know, a healthy open source project might look like.
[5586.38 --> 5591.12]  We talked about who might fund it, how they might fund it, why they might fund it, how much it's actually worth.
[5591.86 --> 5595.62]  But then we really haven't talked about what happens if we don't support it.
[5595.76 --> 5597.50]  It doesn't mean fund it with money.
[5597.60 --> 5601.82]  It means time, effort, people, care, whatever you want to say.
[5601.82 --> 5611.02]  So in your, in your original article, how I stumbled upon, um, get back to the title again, cause I don't have that right in my brain, but the internet's biggest blind spot.
[5611.12 --> 5611.64]  There you go.
[5611.72 --> 5612.22]  Thanks, Jared.
[5612.38 --> 5615.34]  Uh, my, my better half there, my other better half.
[5615.78 --> 5617.84]  Um, let me clarify.
[5618.24 --> 5620.84]  She will listen to the show and she'll be like, no, I'm your better half.
[5620.86 --> 5621.98]  And then it's a whole different fight.
[5621.98 --> 5629.32]  Um, but you know, if we leave this unchecked, we've seen this with various bugs in open SSL.
[5629.42 --> 5630.46]  We've seen this elsewhere.
[5630.64 --> 5634.62]  We we've seen this with the, and these are all examples you've given, Nadia, not my example.
[5634.70 --> 5635.72]  So I'm just quoting you back.
[5635.74 --> 5640.30]  But, uh, if we leave it unchecked, what else have you thought about besides what you've shared in this post?
[5641.06 --> 5641.42]  Yeah.
[5641.90 --> 5648.66]  Um, right there, I think there are like effects that can be felt or enumerated within the open source community.
[5648.66 --> 5651.48]  So obviously things like burnout are not great.
[5651.48 --> 5651.88]  Right.
[5652.00 --> 5653.30]  We covered that one here quite a bit.
[5653.32 --> 5653.34]  Yeah.
[5653.62 --> 5655.24]  Security bugs, things like that.
[5655.40 --> 5664.96]  Um, those are probably things that the open source community will feel and maybe like other people might not notice or someone who's like totally non-technical might just like never notice.
[5665.48 --> 5671.96]  Um, on a larger scale, I think about sort of like, well, there are a couple of things.
[5671.96 --> 5677.04]  One, one is around where, like, where is the stewardship of open source going right now?
[5677.88 --> 5680.96]  Um, it seems like, uh,
[5681.48 --> 5692.52]  there is a lot more company interest in supporting open source in some shape or form or, and, or companies that are releasing their own open source projects.
[5692.52 --> 5705.98]  Um, and so it's possible to imagine a world since we're thinking theoretically here, um, and nobody can predict the future, but it's possible to imagine a world where, uh, new open source projects come from companies themselves.
[5705.98 --> 5711.22]  Um, because they're the ones with the resources to support them and to grow them and sustain them.
[5711.22 --> 5717.50]  And we've already seen a bunch of new projects now that are like essentially owned by Google or Facebook or whatever.
[5717.50 --> 5729.70]  Um, which I think like whether, even if people at open source are afraid to talk about money, it's like, well, if that's going to happen, like that wouldn't be really good either.
[5729.70 --> 5730.02]  Right.
[5730.58 --> 5744.46]  Um, where open source is theoretically about openness and volunteerism and whatever, but in practice, like the projects that might get used a lot and have tons of eyeballs might come from companies that are big enough to sustain and support it.
[5744.46 --> 5747.02]  So that's one area that I've thought through.
[5747.62 --> 5755.90]  Um, another is that there are like so many more open source projects being created now, I think than ever before.
[5756.02 --> 5765.80]  Um, so there's a lot of fragmentation happening, um, that can affect the way that the internet itself gets built and is stabilized or not stabilized.
[5765.80 --> 5769.86]  Um, where you have tons and tons of people using like lots of different projects.
[5769.86 --> 5783.22]  Um, and each project might not be that well sustained because it's not really reasonable to expect that you create this like very strong, vibrant community around every single one of these smaller projects or medium-ish projects.
[5783.22 --> 5788.54]  Um, so that can really affect like the actual ecosystem that gets built.
[5788.54 --> 5797.18]  Um, and that it could be a lot more, let's say like ugly and complicated, um, than it needs to be a lot of duplication happening.
[5797.94 --> 5804.28]  Um, that's just like not a very thoughtful way to build a system that we all use and rely upon.
[5804.28 --> 5817.04]  Um, and then from kind of like a, not necessarily like what will go wrong in a doomsday kind of sense, but more of what could be possible if we actually invest in this stuff better.
[5817.04 --> 5833.02]  Um, I mentioned this in that original post, but just the idea that like any platform, whether it's open source or a startup like Slack or Twitter or whatever, but like any platform has these sort of unpredictable effects.
[5833.18 --> 5837.94]  Um, when you, when you hand people tools, they'll use them in ways that you may not even expect them to use.
[5837.94 --> 5848.16]  Um, and so if we can make those tools better and easier for people to use, there are so many things that people could build with them that we can't even imagine.
[5848.16 --> 5857.04]  And this can get like super granular where like maybe somebody who like was otherwise not incentivized to learn how to code can now because it's so much easier.
[5857.52 --> 5859.28]  Um, and stuff like that has already happened.
[5859.94 --> 5866.24]  And, um, and we can't even begin to imagine like all the really cool things that people can build and do with open source.
[5866.24 --> 5873.84]  If we have a system that's well supported and sustained where people are happy, um, and thank you a little bit more thoughtfully.
[5874.72 --> 5894.86]  I think you might've just inadvertently answered our, our question here, Adam, which was going to be what just to ask you to, excuse me, to kind of pontificate a little bit on what, you know, on, so you painted a bleak future there and, uh, you know, it wasn't dystopian perhaps, but it was on its way, you know, we're quite at Fury Road, but, uh, headed there.
[5894.86 --> 5901.30]  Um, if we just leave it unchecked, uh, just to give a shout out to my favorite movie of 2015.
[5901.94 --> 5907.68]  Um, but what on the other side, you know, you kind of mentioned, what if we, what if we do it right?
[5907.74 --> 5916.78]  What if we, we get it supported and, you know, I'll use that word instead of funded because it's there, but there's more, there's more to support than just funding.
[5916.78 --> 5920.38]  Um, but no doubt funding's a part of it for sure.
[5920.98 --> 5932.04]  Um, if we get it supported and the way Adam put it in our notes is what if it, what if it became a societal norm for companies to, to donate support to open source software?
[5932.12 --> 5934.82]  What if it just became like the status quo of what you do?
[5935.48 --> 5937.02]  What are the effects of that?
[5937.06 --> 5943.66]  And, uh, on kind of the utopian side of things, but you kind of pointed out, pointed out to a certain degree.
[5943.66 --> 5953.58]  And I did cover it from, right, like people using those tools that are maybe better built and then making other great things with them, whether they're businesses or whatever.
[5953.96 --> 5965.64]  Um, but as you were saying that too, I was just thinking like, it's also about like, imagine what it'd be like if people in open source were really happy and really like not burnt out and felt really well supported.
[5965.64 --> 5977.66]  And felt like they had a path to like, um, to expressing their creativity and exploring, um, new ideas in a way that, that they're, uh, enabled to.
[5978.00 --> 5980.96]  And like, I wouldn't know what to do with ourselves.
[5981.34 --> 5982.02]  It'd be so crazy.
[5982.08 --> 5982.62]  It'd be so awesome.
[5983.34 --> 5987.70]  And, and, and I think like, it's not just about like maintaining tools that we have right now.
[5987.70 --> 5999.12]  I think that's my focus because it's easier to make a case for supporting things that are already being used, but people have come to me too with like crazy experimental ideas and things that they think would make the world run better.
[5999.12 --> 6003.06]  Um, or organizing things in a way that's like more stable and secure.
[6003.32 --> 6007.58]  And it'd be really cool if they had the support they needed to make those things happen.
[6007.68 --> 6013.36]  Like really big projects, you know, not just kind of like, I need to solve this problem for myself.
[6013.36 --> 6020.76]  So I built this thing over the weekend and I put it up, but like something like really big and crazy if they had support for that, like who knows how much better things could get.
[6021.62 --> 6022.12]  It's funny.
[6022.24 --> 6024.56]  I think it was, it was a year, it was a long time ago, Adam.
[6024.66 --> 6027.70]  I had actually looked it up because we had somebody on the show.
[6027.76 --> 6028.82]  It turned out it was Tim Caswell.
[6028.82 --> 6038.82]  I think I remember where he has so many like, I don't call them crazy ideas, but like he's on the fringe as a developer.
[6039.26 --> 6040.48]  He's like pushing limits.
[6040.62 --> 6041.22]  He's on the fringe.
[6041.22 --> 6046.26]  The stuff that he's making isn't always, you know, viable as a product or as an end.
[6047.18 --> 6050.94]  But okay, maybe it's now getting to the point where we're like talking about code as art to a certain degree.
[6051.44 --> 6057.56]  But like art often pushes us to new limits and it becomes, you know, infrastructure later on as it's discovered.
[6058.06 --> 6059.82]  And I said to him, I don't know if you remember this, Adam.
[6059.86 --> 6066.94]  I was like, I feel like you're the kind of guy that like somebody should just give them a bunch of money and just be like almost like, what's it called?
[6067.00 --> 6069.20]  It's like the patronage model to a certain degree.
[6069.62 --> 6069.94]  Totally.
[6069.94 --> 6073.78]  Where it's like you just genius funding.
[6073.90 --> 6077.98]  I remember some sort of like genius grant or something like that where you give it to somebody who's just really smart.
[6078.08 --> 6081.46]  You know that no matter what they're going to do with this money, they're going to do something that's really profound.
[6082.10 --> 6082.16]  Right.
[6082.34 --> 6088.94]  Like just take care of their needs, you know, as far as, you know, the hierarchy of needs and whatnot and let them just create.
[6088.94 --> 6093.80]  And there's going to be huge value coming out of that creation that's going to benefit everybody.
[6094.22 --> 6095.00]  I feel like there are.
[6095.12 --> 6096.02]  And he's not the only one.
[6096.08 --> 6100.62]  There's, you know, we could list off people where it's like if they're unencumbered, what could they do?
[6101.36 --> 6101.54]  Yeah.
[6102.14 --> 6104.02]  So that'd be exciting to be really awesome to think about.
[6104.02 --> 6106.74]  Well, this was a fun topic.
[6106.84 --> 6107.36]  That's for sure.
[6107.44 --> 6113.00]  I know that, you know, we could probably go on for quite a while and I would absolutely love that.
[6113.06 --> 6114.60]  I'm sure anybody listens like, don't stop.
[6114.70 --> 6115.18]  Don't stop.
[6115.74 --> 6116.56]  I don't want to stop.
[6116.56 --> 6120.34]  But we do have to stop right now.
[6120.42 --> 6120.80]  I'm just kidding.
[6121.40 --> 6122.34]  In the next few minutes.
[6122.76 --> 6125.54]  I mean, Nadia, it was so much fun having you on this call.
[6125.72 --> 6135.56]  I mean, Jared, I don't know about you, man, but I totally loved having her on and just taking a left turn from our normal show, so to speak, and having a discussion about this.
[6135.56 --> 6150.02]  And I think that if I can say something back to the listening audience, you know, Jared and I and the changelog and Nadia, we may not be here so much to give you money and give you support, but we'd love to hear anybody out there who's like hit a brick wall.
[6151.08 --> 6157.58]  One, you know, we can find ways to amplify that message and say, or at least graduated up to Nadia's list, I believe.
[6157.68 --> 6158.60]  What is that list?
[6158.78 --> 6160.56]  It's fundingOSS.com.
[6161.72 --> 6162.76]  Somebody made it for me.
[6162.80 --> 6163.72]  It was really, really nice.
[6163.84 --> 6164.38]  That's sweet.
[6164.38 --> 6164.82]  Yeah.
[6164.82 --> 6167.40]  I mean, so we'd love to hear your story.
[6167.50 --> 6175.48]  Jared and I are always huge fans of the stories of open source, the people behind it, not just the technology and the products that come from it, but the people.
[6175.60 --> 6177.54]  That's what we love most is the people behind it.
[6177.54 --> 6181.52]  So if you're out there and you got a bloody knuckle story, we'd love to hear it.
[6182.10 --> 6186.12]  You can email us at editors at changelog.com.
[6186.18 --> 6187.98]  We also have an open inbox on GitHub.
[6187.98 --> 6193.78]  Go to github.com slash the changelog slash ping, P-I-N-G, like ping the changelog.
[6193.78 --> 6195.52]  And drop an issue in there.
[6195.56 --> 6196.68]  We'd love to kind of hear from it.
[6196.72 --> 6202.28]  And if there's already an issue there that started, maybe people can just kind of pile into that single issue or create your own issue.
[6202.36 --> 6202.60]  I don't know.
[6202.68 --> 6203.54]  But whatever.
[6203.78 --> 6205.18]  Self-organize around that.
[6205.24 --> 6216.86]  But we'd love to hear some more stories, so to speak, of your open source project that's got lots of users that needs support, as Jared's coined here in the show.
[6216.86 --> 6219.90]  So that was really all I had to say there.
[6220.16 --> 6221.02]  But Nadia, anything else?
[6221.24 --> 6222.82]  Can I pile on for a second?
[6223.14 --> 6223.70]  Yeah, do it, please.
[6224.08 --> 6228.90]  Yeah, I just wanted to add that we've just been kind of talking ideas.
[6229.22 --> 6232.98]  And it's very much in the conversation stage.
[6232.98 --> 6238.82]  I think Nadia perhaps will get to a point where she's in the action stage of like, let's take a plan and execute it.
[6239.52 --> 6243.34]  But that plan needs to come together as a community.
[6243.60 --> 6243.78]  Yeah.
[6243.78 --> 6256.04]  Because one of us is not going to have all the answers and Nadia is so fun having you on because you bring a unique perspective that Adam and I don't have and that many of our listeners don't have to the conversation.
[6256.18 --> 6256.84]  I think it's powerful.
[6257.12 --> 6259.24]  So I'll say all that to say this.
[6260.94 --> 6261.74]  Contact us.
[6261.84 --> 6262.72]  Let us know your thoughts.
[6262.72 --> 6270.52]  If you think something I said was really off kilter or wrong or do you have better ideas on how we can go about solving these problems?
[6270.52 --> 6273.70]  Or maybe you think it's not a problem and everything's fine.
[6273.78 --> 6274.78]  We want to hear those opinions.
[6275.22 --> 6277.22]  So hit us up Twitter.
[6277.42 --> 6278.36]  We're at Changelog.
[6278.50 --> 6281.12]  Like Adam said, InPing is a great place to talk to us out in the open.
[6282.46 --> 6284.14]  Yeah, we'd love to hear from everybody.
[6284.80 --> 6284.86]  Yeah.
[6285.20 --> 6286.94]  I just want to echo all that too.
[6286.94 --> 6292.32]  I think the biggest immediate need that I saw was just everyone needs to be talking to each other more.
[6293.06 --> 6296.48]  Because this is something that seems to get talked about a ton in open source.
[6296.48 --> 6302.48]  But honestly, people in big companies might not be aware or startups or venture capitalists or whatever.
[6302.72 --> 6307.10]  So by talking about it out in the open, you're helping everybody else understand what's going on.
[6308.28 --> 6315.22]  And yeah, the conversation is really, really important to make sure that we're doing things as a community and doing it together.
[6315.22 --> 6317.42]  And it isn't just one person dictating stuff.
[6317.58 --> 6318.84]  So please talk more.
[6319.26 --> 6320.28]  Yeah, absolutely.
[6321.56 --> 6322.94]  Awareness is the key.
[6322.94 --> 6326.70]  Well, so if you're listening right now, thank you so much for listening.
[6326.86 --> 6328.42]  This is episode 193.
[6328.56 --> 6332.70]  So you can go to changelog.com slash 193 to find the show notes.
[6332.80 --> 6335.54]  That means that Nadia's Awesome's articles are going to be there.
[6335.66 --> 6339.56]  So if you need to read those prior to listening, you can go there and find those.
[6339.58 --> 6343.74]  Or you can pull up the show notes in your podcast app and do it that way as well.
[6343.86 --> 6348.40]  So you can follow Nadia on Medium, on Twitter.
[6348.40 --> 6354.16]  And you also have a mailing list that I wanted to earmark, which is further in our notes.
[6354.26 --> 6355.38]  That's a tiny letter, by the way.
[6355.38 --> 6356.82]  That's a pretty cool thing.
[6357.12 --> 6361.84]  Mention her email list is what I have in my notes, which is building better software updates.
[6361.98 --> 6364.56]  I guess you're updating people about building better software.
[6364.62 --> 6364.94]  Is that right?
[6365.62 --> 6365.76]  Yeah.
[6365.78 --> 6369.92]  I've just been sending in stuff that I've been doing and also new posts in that list.
[6369.92 --> 6381.48]  And I imagine if you turn around and do something bigger than this, which is maybe your next company, your next founding thing, whatever that might be, whether it's a nonprofit or a for-profit, it'll be mentioned in that email.
[6381.82 --> 6382.18]  Absolutely.
[6382.42 --> 6382.58]  Yeah.
[6382.80 --> 6383.02]  Great.
[6383.20 --> 6383.36]  Great.
[6383.56 --> 6387.68]  We have the link to that tiny letter that you can subscribe to.
[6387.76 --> 6389.28]  I say tiny letter because it's tinyletter.com.
[6389.34 --> 6391.12]  That's the little thing.
[6391.28 --> 6392.54]  I keep calling it little because it's tiny.
[6393.96 --> 6394.76]  I love it.
[6394.82 --> 6395.26]  It's cool.
[6395.64 --> 6396.66]  I love tiny letter.
[6396.74 --> 6397.22]  It's so cool.
[6397.22 --> 6400.62]  But I'm glad you have that so that people can keep in touch.
[6401.06 --> 6401.80]  So follow her on Medium.
[6401.96 --> 6402.50]  Follow her on Twitter.
[6403.12 --> 6404.14]  Subscribe to that email.
[6404.46 --> 6405.74]  Check the show notes for all those links.
[6406.72 --> 6409.16]  And thank you so much, Nadia, for joining us.
[6409.16 --> 6424.18]  And, you know, one, just having the audacity to kind of do what you've done in your career path and then step away back last May and then, you know, get that lead to Ford Foundation and drive this point home.
[6424.18 --> 6431.60]  I mean, it's so cool to see someone like you step out and just do this and raise awareness around such an important topic.
[6431.76 --> 6433.72]  And I can't thank you personally enough.
[6433.94 --> 6437.96]  And however Jared and I and the ChinoDog can support you, you've got it.
[6438.14 --> 6439.18]  Whatever we can do, we'll do it.
[6440.46 --> 6440.70]  Yeah.
[6441.04 --> 6441.80]  Thank you, guys.
[6441.80 --> 6445.36]  And to everyone listening, thank you for listening.
[6445.46 --> 6447.48]  Our members, our sponsors, you all are awesome.
[6448.50 --> 6450.86]  We've got some great shows coming up in the schedule.
[6450.92 --> 6455.28]  I'm going to mention a couple just because Jared did a great job by putting them in the show notes here for us.
[6455.46 --> 6458.50]  So up next, we've got Elixir with Jose Valim.
[6458.92 --> 6460.98]  We've got Free Code Camp with Quincy Larson.
[6460.98 --> 6467.74]  And we've got Tiddly Wiki, which I'd never heard of, by the way, from Jeremy Rustin.
[6468.22 --> 6468.96]  And a big one.
[6469.18 --> 6469.76]  Listen, everybody.
[6469.88 --> 6470.50]  It's a big one.
[6470.62 --> 6477.02]  It's the future of WordPress and Calypso with nobody else but Matthew Mullenweg.
[6477.16 --> 6479.16]  So stay tuned to those upcoming shows.
[6479.34 --> 6485.00]  If you don't know, go to the changelog.com or changelog.com because it used to be the changelog and I'm just crazy like that.
[6485.32 --> 6486.32]  Subscribe to the podcast.
[6486.62 --> 6487.52]  Subscribe to our weekly email.
[6487.64 --> 6488.32]  Subscribe to Nightly.
[6488.32 --> 6491.06]  Just hit subscribe on all the buttons we give you.
[6491.34 --> 6491.78]  All the buttons.
[6491.84 --> 6492.46]  All the buttons.
[6492.90 --> 6495.36]  And with that, that is the show.
[6495.52 --> 6496.56]  So everybody say goodbye.
[6497.22 --> 6497.60]  Bye.
[6497.86 --> 6498.24]  Goodbye.
[6498.54 --> 6499.04]  Thanks, Nadia.
[6518.32 --> 6519.74]  Bye.
[6519.96 --> 6521.82]  Bye.
[6521.92 --> 6523.40]  Bye.
[6523.46 --> 6523.82]  Bye.
[6524.00 --> 6524.76]  Bye.
[6524.82 --> 6525.10]  Bye.
[6525.12 --> 6525.50]  Bye.
[6525.60 --> 6525.70]  Bye.
[6526.10 --> 6526.14]  Bye.
[6526.14 --> 6526.60]  Bye.
[6527.62 --> 6528.00]  Bye.
[6528.16 --> 6528.74]  Bye.
[6528.76 --> 6530.20]  Bye.
[6530.34 --> 6530.50]  Bye.
[6530.50 --> 6531.84]  Bye.
[6531.96 --> 6532.56]  Bye.
[6532.70 --> 6534.18]  Bye.
[6534.24 --> 6534.70]  Bye.
[6536.64 --> 6537.98]  Bye.
[6537.98 --> 6538.16]  Bye.
[6538.34 --> 6539.12]  Bye.
[6539.38 --> 6539.98]  Bye.
[6540.24 --> 6542.38]  Bye.
[6542.44 --> 6543.78]  Bye.
[6544.28 --> 6544.58]  Bye.
[6546.68 --> 6547.44]  Bye.
[6547.44 --> 6547.88]  guitarès resultados Gagaplus.

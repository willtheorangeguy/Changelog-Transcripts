[0.00 --> 11.76]  This is JS Party, your weekly celebration of JavaScript and the web.
[12.02 --> 13.94]  Connect with us on the Fediverse.
[14.20 --> 16.56]  We're JS Party at changelog.social.
[16.92 --> 19.40]  On Twitter, we're at jspartyfm.
[19.52 --> 25.48]  And on YouTube at youtube.com slash changelog, where we host our live shows, post clips and
[25.48 --> 28.76]  highlights from all of our pods, and other cool videos you don't want to miss.
[28.76 --> 33.70]  Special thanks to our partners at Fastly for a ship and JS Party super fast all around
[33.70 --> 34.12]  the world.
[34.42 --> 36.00]  Check them out at fastly.com.
[36.52 --> 37.64]  And to fly.io.
[38.16 --> 41.22]  Host your app servers and database close to your users.
[41.54 --> 42.06]  Smart, right?
[42.46 --> 42.92]  Don't worry.
[43.12 --> 44.30]  No ops are required.
[44.82 --> 46.74]  Learn more at fly.io.
[58.76 --> 65.50]  Oh, hoi, hoi.
[65.72 --> 67.56]  Welcome to another exciting JS Party.
[68.16 --> 69.98]  I'm Nick, and I will be your host for today.
[70.10 --> 72.28]  And I am joined by my pal, K-Ball.
[72.36 --> 73.08]  K-Ball, how's it going?
[73.32 --> 74.18]  It's going great.
[74.34 --> 76.38]  Good to hear you're Mr. Burns, as always.
[78.16 --> 78.60]  Yeah.
[79.42 --> 81.36]  Excited to chat with you once again.
[81.36 --> 85.14]  And we have a special guest today, and that is Thomas Eckert.
[85.22 --> 86.12]  Thomas, how's it going?
[86.58 --> 87.60]  Hey, it's going well.
[87.70 --> 91.14]  I kind of feel like I've been pulled up on stage at a rock concert.
[91.88 --> 96.94]  This shows the value of hanging out in the changelog slack.
[97.26 --> 103.48]  You just loiter around long enough, and on some given Thursday, you might get pulled onto
[103.48 --> 104.22]  JS Party.
[104.22 --> 104.30]  Great.
[104.78 --> 109.98]  And that is exactly what has happened to me, and I'm happy to be here today as we chat,
[110.10 --> 112.46]  have coffee, and just keep it really loose.
[112.82 --> 114.40]  So thank you for having me on.
[114.72 --> 115.74]  Yeah, thanks for joining us.
[115.90 --> 119.72]  We totally didn't even pitch you on that promo for the changelog slack.
[120.06 --> 120.52]  That's right.
[122.44 --> 124.46]  But we are excited to have you on today.
[125.02 --> 129.54]  And so to give some background, I suppose, K-Ball and I were just going to kind of have
[129.54 --> 134.50]  an unscripted coffee chat for this week's episode, and we posted out about, you know,
[134.50 --> 135.16]  what should we talk about?
[135.24 --> 136.00]  What questions should we have?
[136.06 --> 138.30]  And you came with a whole list of questions.
[138.78 --> 142.68]  I just got thinking about it, and some of them are serious.
[142.82 --> 143.78]  Some of them are silly.
[144.28 --> 150.48]  Some of it goes into a lot of the topical things that are going on in JavaScript right
[150.48 --> 150.84]  now.
[151.10 --> 154.26]  And I'd love to pick your brains and get you guys talking.
[154.74 --> 155.76]  And yeah.
[156.14 --> 156.54]  For sure.
[156.78 --> 157.20]  For sure.
[157.20 --> 160.80]  So before we do any of that, why don't you tell us a bit about yourself?
[161.24 --> 161.40]  Yeah.
[161.52 --> 163.18]  Well, my name is Thomas Eckert.
[163.38 --> 167.58]  I am a little bit of an imposter here because mostly I write Go.
[168.16 --> 171.44]  And I work at a company, but I also write a lot of TypeScript.
[171.62 --> 171.80]  Okay.
[172.16 --> 179.08]  I work at a company called HashiCorp, which you may know from Terraform and other fine products.
[179.30 --> 183.26]  I work on Console, which is a service mesh solution.
[183.26 --> 186.98]  So I'm much more focused in the networking side of things.
[187.10 --> 192.20]  But at my old job, I wrote a lot of TypeScript on the weekends and in the evenings.
[192.20 --> 195.40]  I write a lot of JavaScript, a lot of TypeScript.
[195.90 --> 197.40]  And I'm a huge fan of the web.
[197.44 --> 202.64]  And I care about how the web evolves and the tools that we get to make it great.
[202.64 --> 203.04]  Awesome.
[203.70 --> 203.84]  Yeah.
[203.90 --> 205.68]  Well, we are very excited to have you.
[205.80 --> 208.94]  We will probably edit out that part about writing Go, but that's okay.
[209.62 --> 211.64]  Just put that in the Go time podcast.
[212.24 --> 213.54]  I used to write Go also.
[214.32 --> 215.56]  But here I am.
[216.22 --> 216.98]  There you are.
[218.12 --> 220.02]  I have yet to see a good...
[220.02 --> 223.76]  I mean, is there like a WebAssembly Go runtime yet?
[223.92 --> 227.28]  I mean, can you write client-side code in Go and have it...
[227.28 --> 227.70]  You can.
[228.30 --> 228.88]  All right.
[229.02 --> 229.56]  Well...
[229.56 --> 230.48]  You can do it.
[230.62 --> 232.58]  So even as a Go developer, you belong.
[233.00 --> 233.40]  I do.
[233.56 --> 233.88]  I do.
[233.92 --> 234.76]  I appreciate that.
[235.32 --> 236.76]  We're all inclusive here, for sure.
[236.90 --> 237.36]  That's right.
[238.64 --> 239.76]  So how do we want to do this?
[239.80 --> 241.40]  Do we want to jump right into some questions?
[241.64 --> 243.06]  Do we want to...
[243.06 --> 244.92]  Okay, well, should we grill Thomas a little bit beforehand?
[245.36 --> 245.92]  What should we do?
[247.02 --> 247.82]  Well, that's...
[247.82 --> 249.24]  So that's the interesting question, right?
[249.26 --> 251.60]  We're going to run your questions right back on you.
[251.68 --> 252.02]  All right.
[252.02 --> 252.58]  All right.
[252.58 --> 258.04]  I kind of want to know your answer to your second question, which is who would win in
[258.04 --> 262.58]  a fistfight between the Tailwind CSS folks and true CSS people?
[262.96 --> 265.30]  The true CSS, the pure CSS.
[265.80 --> 269.34]  Well, I personally am a fan of Tailwind CSS.
[269.72 --> 271.32]  I've written a lot of Tailwind.
[271.44 --> 273.76]  I've written a lot of CSS, CSS.
[274.18 --> 280.12]  And I think there's a lot of value in both, depending on your environment.
[280.12 --> 283.04]  My personal website, I do everything in Tailwind.
[283.54 --> 287.06]  I've shipped client projects using Tailwind.
[287.62 --> 289.12]  Now, who would win in a fistfight?
[290.78 --> 297.80]  I think, is it all Tailwind CSS people and all CSS people at the same time?
[297.90 --> 299.26]  Because I think there's...
[299.26 --> 300.76]  Pick a random one on each side.
[300.84 --> 301.78]  Yeah, exactly.
[302.40 --> 306.86]  I think Adam Wavin has been working with a personal trainer lately, too.
[306.86 --> 310.44]  So, he might have a little bit of an advantage there.
[310.62 --> 311.08]  I don't know.
[311.16 --> 315.40]  I feel like the people who are into Tailwind, they strike me as the folks who are using the
[315.40 --> 316.60]  machines in the gym, right?
[316.66 --> 318.58]  Like, it keeps you on the straight line.
[318.70 --> 319.96]  It keeps you in the borders.
[320.26 --> 326.16]  And like, the people who are doing like hardcore CSS, they're like the kettlebell experts, right?
[326.22 --> 328.92]  Like, rough and ready, dealing with all the edge cases.
[328.92 --> 335.90]  And in my impression, like, you can build some impressive muscles on gym machines, but you're
[335.90 --> 339.94]  not going to get that like street toughness that you will if you're working out with like
[339.94 --> 340.94]  kettlebells and free weights.
[341.10 --> 347.30]  So, I'm kind of thinking, you know, the originals, the hardcore folks, they're going to win.
[347.36 --> 348.08]  The OGs.
[348.46 --> 349.36]  OG CSS.
[349.82 --> 350.52]  What do you think, Nick?
[350.52 --> 352.22]  I go the other way, I think.
[352.62 --> 357.60]  Because if you're looking for longevity, the people who have the perfect form, which the
[357.60 --> 362.50]  machines will give you the better form, they are going to be at it longer.
[362.64 --> 364.58]  They're not going to hurt themselves.
[364.88 --> 370.58]  They're not going to get into a lot of trouble, as I currently am with my non-Tailwind projects.
[371.24 --> 375.48]  And so, I think like in a long game, they're going to come out ahead.
[375.78 --> 377.06]  Well, we weren't asking about longevity.
[377.18 --> 378.24]  We're asking about a fist fight.
[378.64 --> 379.10]  That's true.
[379.10 --> 379.64]  Yep.
[379.88 --> 380.30]  That's true.
[380.52 --> 382.40]  Well, what are the advantages in a fist fight?
[382.50 --> 383.84]  You get a lot of discipline.
[384.12 --> 386.46]  You know exactly how to fight.
[386.54 --> 391.86]  It's not all about pure strength, but it's about kind of fitting into and accomplishing
[391.86 --> 393.80]  the task, which is winning the fist fight.
[393.86 --> 397.02]  And maybe those Tailwind CSS people, they have that discipline.
[397.14 --> 398.40]  They know exactly what to use.
[398.90 --> 403.52]  None of the CSS they ship is unused by definition.
[404.34 --> 409.48]  So, perhaps they're using all of their energy in the fist fight very,
[409.48 --> 410.74]  very accurately.
[410.74 --> 412.42]  And that's a way you can win.
[412.96 --> 413.52]  All right.
[413.54 --> 416.48]  I think we've punched that one in the face enough times.
[416.92 --> 417.18]  All right.
[417.94 --> 421.88]  What are some of the other spicy questions that you had on there we might discuss?
[422.14 --> 423.60]  Is Agile overrated?
[423.60 --> 426.92]  I feel like that is one I've seen going around a fair amount.
[426.92 --> 427.56]  Yeah.
[427.92 --> 428.98]  What's your take?
[428.98 --> 432.68]  I think Agile has become so many things.
[432.86 --> 435.42]  It's hard to really pin down what it is.
[435.98 --> 441.54]  I think almost every team I've ever worked on will refer to themselves as being Agile,
[441.74 --> 445.32]  but they work in different ways.
[445.46 --> 451.48]  And those ways actually, you know, those processes do actually end up working and we produce great
[451.48 --> 452.10]  output.
[452.10 --> 457.66]  But what even Agile is, I think you'd have to pin it down before you could really say
[457.66 --> 458.56]  if it's overrated.
[458.74 --> 462.90]  Is it really this specific way of working or is it more of a concept?
[463.08 --> 468.24]  And I mean, I've also been on teams that have worked in a more waterfall fashion, especially
[468.24 --> 473.72]  for coordinating between two or more very large projects.
[473.90 --> 477.26]  And that works pretty well sometimes.
[477.26 --> 481.72]  When you need to get everyone on the same page, sometimes having a big document that
[481.72 --> 486.14]  says this is everything I'm going to do over the next three months, it's not a bad idea.
[486.68 --> 486.74]  Yeah.
[486.88 --> 488.94]  I always feel like it's what you said.
[488.98 --> 490.98]  Nobody knows exactly what Agile is.
[491.24 --> 495.66]  And if I had to call it anything, instead of Agile development, I'd call it like Schrodinger's
[495.66 --> 499.66]  development because you think it's Agile until you measure it and see that it's waterfall.
[500.26 --> 504.26]  If you ask the influencers on Twitter what Agile is, they'll say, well, you should never file
[504.26 --> 507.06]  a bug because if you're filing a bug, you're not being Agile enough.
[507.26 --> 507.44]  Yeah.
[507.98 --> 511.22]  Real Agile software doesn't ship bugs.
[511.56 --> 511.92]  Yeah.
[512.54 --> 517.94]  All software ships bugs and you can't solve all your problems at the exact same time.
[518.04 --> 520.92]  So you have to have some system to coordinate.
[521.80 --> 526.84]  And as those systems grow and you need to report upwards, sometimes moving away from Agile
[526.84 --> 527.58]  is the right decision.
[528.00 --> 535.00]  When it comes to non-Agile approaches, you often have to write these documents, right?
[535.00 --> 536.30]  That you're sharing.
[536.92 --> 539.84]  I mean, you have to write a lot of documentation in an Agile environment too.
[539.96 --> 543.20]  But with waterfall, you might have more RFCs.
[543.28 --> 545.98]  You might have these proposals, these high-level docs.
[545.98 --> 555.34]  And what I've experienced is I've not found a perfect tool for writing those docs, getting
[555.34 --> 557.00]  feedback from multiple stakeholders.
[557.58 --> 560.24]  I know some teams use Dropbox Paper.
[560.92 --> 563.08]  I know that we use Google Docs.
[563.40 --> 564.80]  Some teams use Notion.
[565.24 --> 566.94]  What have been your experiences?
[566.94 --> 574.30]  What's the best tool for sharing those non-code-specific ideas and getting feedback?
[575.16 --> 578.58]  Ah, this is an ongoing, ever-long debate.
[580.10 --> 580.78]  Yeah.
[581.36 --> 587.34]  Well, I think if you took an engineer's perspective, they might move more towards pure markdown in
[587.34 --> 588.22]  GitHub, right?
[588.32 --> 588.44]  Yep.
[588.68 --> 590.66]  That, I think, is a wonderful solution.
[590.66 --> 597.76]  But I, like many people, work with fantastic people who do not want to use GitHub, who do
[597.76 --> 604.46]  not want to learn Git, who feel much more comfortable commenting in a shared environment like Google
[604.46 --> 605.76]  Docs, Google Drive.
[606.14 --> 607.98]  What's been your experience around that?
[608.70 --> 608.84]  Yeah.
[608.98 --> 614.20]  This is actually something that we have recently tried to make everyone happy with.
[614.36 --> 618.10]  And the way that we've done that is through markdown in GitHub.
[618.10 --> 623.78]  But there's a plugin, like a GitHub action, that you put some metadata at the top of the
[623.78 --> 630.04]  markdown file, and it will sync that as a Confluence document, which can then be in
[630.04 --> 632.70]  read-only mode there, but you can comment on it there in Confluence.
[633.36 --> 637.14]  And this is also like, not everyone in the company has access to GitHub.
[637.44 --> 641.78]  So it's a way to get that out there, but also keep the developers happy writing their
[641.78 --> 642.94]  comfy markdown like myself.
[642.94 --> 648.44]  And do comments get synced back from Confluence into something in Git or GitHub?
[648.66 --> 650.40]  Or how does that coordination work?
[650.72 --> 652.00]  I don't actually remember.
[652.16 --> 656.84]  I think that something happens with that, but I also haven't tested that.
[657.06 --> 661.60]  Because the last time I was dealing with that combination and had Confluence, a lot of my
[661.60 --> 662.96]  engineers never went into Confluence.
[663.20 --> 665.76]  And so they would miss any comments that happened over there.
[666.14 --> 670.80]  I think that that's the problem with Confluence and Google Docs and probably Dropbox Paper.
[670.80 --> 676.94]  But the fact that they're not tangible, predictable URLs that I can get to, there's some random
[676.94 --> 681.12]  string in there along with it, means that things just feel completely lost to me.
[681.50 --> 683.50]  And their search sucks enough that I never want to go.
[683.96 --> 686.90]  I mean, I'm talking in terms of Confluence, I guess, at this point.
[687.46 --> 689.90]  Their search sucks enough that I never want to even look in there.
[690.64 --> 697.58]  And having that stuff, especially if it's more developer-focused outside of the code, means
[697.58 --> 699.52]  that it doesn't get updated with the code.
[699.72 --> 703.72]  Whereas it has a greater chance if it's in line with the code and you can kind of see
[703.72 --> 709.42]  with the Git versioning when it was last updated and push for it a little bit more there.
[709.90 --> 710.12]  Yeah.
[710.24 --> 712.12]  I'm not sure there is a perfect answer to this.
[712.28 --> 713.34]  Like any engineering problem.
[713.40 --> 715.32]  Like the question of how agile do you get?
[715.40 --> 718.58]  Like there's trade-offs that depend on your environment, who you're working with.
[718.58 --> 725.44]  A combo that I've used that sort of meshed that is we had them in Google Docs, but we
[725.44 --> 726.24]  had a short links tool.
[726.64 --> 733.18]  And so we could create memorable short links and put those in code comments or other places
[733.18 --> 735.44]  where you could make it easier to sync.
[735.94 --> 741.30]  Pros and cons, once again, like doing stuff in Google Docs is more painful for many engineers
[741.30 --> 742.62]  than doing things in Markdown.
[742.62 --> 748.98]  But we had enough weight of people wanting to get in there who weren't necessarily in
[748.98 --> 750.34]  the code that it made a lot of sense.
[750.94 --> 752.16]  Fire question real quick.
[752.66 --> 753.84]  You have to search for something.
[753.98 --> 756.30]  You have to know something that you know is documented somewhere.
[756.84 --> 757.74]  What's the first thing you do?
[758.14 --> 758.44]  Thomas.
[758.98 --> 762.24]  For me, I've actually, we've been really lucky at HashiCorp.
[762.42 --> 765.70]  We've built this tool called HashiDocs.
[765.84 --> 769.82]  It's now publicly being released as Hermes or Hermes.
[769.82 --> 772.28]  I don't know what the right pronunciation is.
[772.62 --> 775.50]  But this is a wrapper around Google Docs.
[775.54 --> 779.42]  And so all of our decisions are made in Google Docs.
[779.50 --> 786.58]  And actually the content of the documents themselves has been, they've been indexed.
[786.60 --> 788.70]  And the search is fantastic.
[789.14 --> 790.66]  Like you can really find the right thing.
[790.76 --> 792.26]  So that's one solution.
[792.40 --> 795.96]  If I know it's in the code, RipGrep is my go-to.
[795.96 --> 802.08]  I go to that repository and I RipGrep for the closest thing that I can and I start reading
[802.08 --> 802.84]  the code.
[803.22 --> 808.00]  So depends on if I'm looking at why did we make this decision?
[808.00 --> 813.52]  I'm going to look at the RFCs, which I think is a really powerful thing about the RFC model.
[813.52 --> 819.36]  I can go back to the very start of the product that I work on and say, okay, why is this thing
[819.36 --> 820.00]  like this?
[820.06 --> 825.12]  Oh, there was a decision that was made because we needed to ship at this date.
[825.22 --> 825.48]  Okay.
[825.52 --> 828.90]  So this is not one of those things that I can never change.
[828.98 --> 829.30]  Right.
[829.30 --> 830.98]  That's where I would start.
[831.22 --> 831.74]  How about yourself?
[832.00 --> 835.60]  That points to something, and I'm going to detour you off in a different direction, but
[835.60 --> 841.92]  that points to something that I've been thinking a lot about, which is documenting in decision
[841.92 --> 846.12]  documents, whether they're RFCs or other forms or durable decision docs or whatever model
[846.12 --> 851.28]  you use, but documenting what are the situations in which this decision might make sense to reopen.
[852.68 --> 858.92]  Because I find that, I mean, maybe this is just engineers, but we love to relitigate decisions.
[859.30 --> 866.26]  And a lot of times those docs are not perfectly annotating all the things that were considered
[866.26 --> 872.38]  or they're opaque enough that people look at them and then they still want to reopen, even
[872.38 --> 876.04]  though oftentimes the reason they want to reopen is rehashing something that was a deliberate
[876.04 --> 876.44]  decision.
[876.44 --> 882.68]  And so one question I have to you all is, how do you think about when does it make sense
[882.68 --> 885.04]  to reopen a document or a decision?
[885.72 --> 888.60]  And how is that annotated or indicated?
[889.30 --> 890.82]  It's not for us.
[892.32 --> 894.56]  Do you see the same problem I mentioned then?
[894.68 --> 895.92]  Oh, yeah, absolutely.
[896.54 --> 902.10]  Well, I think it hits even at a problem that we all encounter when we join a company as
[902.10 --> 911.22]  an engineer is navigating what decisions and, you know, a code base is an artifact of multiple
[911.22 --> 911.74]  decisions.
[911.74 --> 917.40]  What decisions in that code base are fundamental and intentional?
[917.66 --> 920.74]  And what are just externalities of another decision?
[921.06 --> 923.48]  Or, oh, I just got to put this here.
[923.96 --> 932.12]  And you can, once you've learned the culture of your team, ask these questions of, is this
[932.12 --> 934.72]  thing here because it has to be like this?
[935.52 --> 937.66]  Or did you just write this in a day?
[937.90 --> 939.88]  And that's why it looks this way.
[940.10 --> 941.84]  I think that's where you learn.
[941.84 --> 945.08]  Though that approach you'll lose if you have a lot of turnover, right?
[945.16 --> 946.34]  Like that works if you...
[946.34 --> 946.84]  Yeah, exactly.
[947.20 --> 947.44]  Yeah.
[947.52 --> 947.76]  Yeah.
[948.08 --> 948.32]  Yeah.
[948.32 --> 949.64]  Because then you have to learn the team.
[949.78 --> 955.04]  And then I think that's, you know, a big value in these documents is that they outlive
[955.04 --> 957.94]  an individual's tenure at a company.
[958.74 --> 959.72]  So how would we fix that?
[960.36 --> 966.22]  I wonder if my instinct is to put something closer to the code, right?
[966.22 --> 973.64]  I encountered a change just before we got on this podcast where there was a make script
[973.64 --> 975.48]  or an instruction in our make file.
[976.00 --> 983.30]  And there was a readme that was next to this command.
[983.52 --> 991.36]  And it said, we need to pass this empty file because this code gen thing needs something
[991.36 --> 992.40]  as the headers.
[992.40 --> 996.84]  It just needs a file, but we don't have any headers to add to it.
[997.10 --> 999.18]  So we just pass an empty file.
[999.76 --> 1001.44]  Well, I looked at that.
[1001.72 --> 1007.92]  I went to get blame and I saw who made who wrote that and the fact that it was written
[1007.92 --> 1009.18]  about three years ago.
[1009.28 --> 1016.88]  So I went and I looked at what flags actually needed to be passed to that command now and
[1016.88 --> 1019.12]  realized that we don't need to pass an empty file anymore.
[1019.12 --> 1024.62]  So I just deleted that empty file that was just there to solve a problem.
[1025.12 --> 1031.26]  So the closer it gets to the code, I think the better when it comes to making decisions
[1031.26 --> 1032.94]  in situ as an engineer.
[1033.52 --> 1038.72]  But when you're talking about architectural decisions, I think you need something like
[1038.72 --> 1039.84]  these decision documents.
[1039.84 --> 1047.48]  And maybe they need to be written in less formal English and maybe just, hey, we had this discussion.
[1047.48 --> 1055.72]  And if I can go into a topical, topical topic, maybe we need a system that can read all of
[1055.72 --> 1057.00]  these decision documents.
[1057.00 --> 1067.76]  And you can have a chat with a GPT model to say, why do we have these modules broken up?
[1068.20 --> 1075.74]  Well, I've referenced, I've ingested all of the RFCs and I know the answer, right?
[1076.02 --> 1077.44]  Or it can point to an answer.
[1077.44 --> 1082.12]  And the beauty of this is if it doesn't know, it'll tell you just as confidently.
[1082.58 --> 1083.06]  It'll make it up.
[1085.18 --> 1086.58]  It'll just make it up.
[1087.50 --> 1088.72]  That's the problem.
[1088.84 --> 1093.82]  You need at least some kind of source of truth, something that it can point to.
[1094.38 --> 1095.78]  That is the big problem.
[1095.94 --> 1102.04]  And I feel for us, also a lot of this is, quote unquote, not documented by being documented
[1102.04 --> 1103.14]  in Slack history.
[1103.36 --> 1104.78]  And you have to go back and look.
[1104.86 --> 1105.96]  That is a problem.
[1106.46 --> 1106.68]  Yeah.
[1106.68 --> 1107.04]  Yeah.
[1107.24 --> 1109.52]  Oh, Slack is a terrible system of record.
[1109.86 --> 1110.54]  It is.
[1110.66 --> 1111.40]  It really is.
[1111.54 --> 1111.80]  Yes.
[1112.02 --> 1116.46]  But what if you could have some kind of AI attached to your entire Slack instance?
[1117.38 --> 1122.16]  And you could go back and query these things of, do you remember when we made this decision
[1122.16 --> 1127.00]  around, you know, should we use X or Y?
[1127.20 --> 1129.04]  Is that, I think that could be really valuable.
[1129.66 --> 1130.18]  It could be.
[1130.24 --> 1135.62]  And just like simple things like, oh, you know, you have this RFC talking about this specific
[1135.62 --> 1140.08]  topic and that was created or last updated on, you know, March 4th, 2022.
[1140.08 --> 1144.72]  But I see that on September 8th, 2022, you talked about this in Slack and it looks like
[1144.72 --> 1145.90]  you came to some kind of conclusion.
[1146.08 --> 1147.12]  Do you want to update these docs?
[1147.12 --> 1150.54]  Like having that kind of context could be kind of cool.
[1150.84 --> 1151.90]  In looking at this.
[1151.96 --> 1156.36]  So we had Fred shot on a few months ago now, probably to talk about Astro 2.
[1157.06 --> 1159.30]  And we didn't really talk about it on the show much.
[1159.40 --> 1164.84]  But soon after that, he announced Houston, which is like a language model that's trained
[1164.84 --> 1166.72]  on Astro's docs.
[1166.72 --> 1171.14]  And ever since then, like, it's just been in my mind, like, I want, I want that, but
[1171.14 --> 1172.52]  for literally everything at work.
[1172.60 --> 1172.98]  Yeah.
[1172.98 --> 1177.18]  And I actually like kind of started looking for solutions to that, including like going
[1177.18 --> 1182.12]  down the rabbit hole of, um, of the dependencies that he used to, or the Astro team used to
[1182.12 --> 1187.22]  create that, which is like laying chain and this, I think it was some go stuff, unfortunately,
[1187.22 --> 1196.48]  but, uh, but then I did come across this product on, um, on product hunt that it's called ingest
[1196.48 --> 1196.74]  AI.
[1196.74 --> 1199.16]  And it's, it does literally this, it takes confluence.
[1199.16 --> 1201.58]  It takes, uh, Jira, it takes Microsoft teams.
[1201.58 --> 1203.14]  It takes, uh, Slack.
[1203.16 --> 1204.40]  It takes notion.
[1204.40 --> 1208.46]  It takes all of these sources, puts them all together, reads all of that, and then gives
[1208.46 --> 1210.80]  you prompt, a prompt that you can ask anything.
[1211.10 --> 1211.20]  Yeah.
[1211.38 --> 1212.92]  Does it link back to sources?
[1213.36 --> 1214.94]  Oh, that probably I haven't tried it.
[1215.06 --> 1216.04]  I would have to go through.
[1216.04 --> 1218.38]  I think that's where you get something really interesting, right?
[1218.40 --> 1219.84]  You have a conversational interface.
[1219.90 --> 1225.02]  It can give you its best attempt, but not only that, if it can show you how it got there,
[1225.02 --> 1227.20]  you can go and validate that answer.
[1227.66 --> 1232.04]  And suddenly you have something that is not able to just purely bulldoch you.
[1232.46 --> 1232.70]  Yeah.
[1234.14 --> 1237.04]  And I think that that's a promise of a lot of these things right now.
[1237.12 --> 1240.72]  Like a copilot for docs is a perfect example.
[1240.94 --> 1244.18]  It gives you examples and gives you where it's pulling the data from.
[1244.18 --> 1246.34]  Same thing with, with, uh, Houston.
[1246.52 --> 1247.34]  It does that.
[1247.42 --> 1250.58]  And if it doesn't tell you, it tries to tell you that it doesn't know, but they also have
[1250.58 --> 1253.68]  a big banner at the top saying, I might be totally wrong in what I'm telling you.
[1253.74 --> 1254.30]  It might just lie.
[1254.50 --> 1254.74]  Yeah.
[1254.84 --> 1256.82]  It's not that hard to get it to hallucinate too.
[1256.88 --> 1257.88]  I've played around with it sometimes.
[1257.88 --> 1266.20]  Well, you even in passing mentioned this point around, oh, you mentioned this RFC.
[1266.40 --> 1268.52]  Do you want to go back and update it?
[1268.72 --> 1270.46]  Well, that opens up this bigger question.
[1271.08 --> 1275.04]  What is the timeline on which you can go back and update your RFC?
[1275.04 --> 1280.04]  Because for us, we produce an RFC.
[1280.30 --> 1281.10]  It gets reviewed.
[1281.30 --> 1282.26]  It gets accepted.
[1282.66 --> 1287.24]  And then, and usually there's some implementation that goes along with the RFC.
[1287.42 --> 1290.02]  You're not just completely waterfalling.
[1290.16 --> 1293.60]  I'm not going to touch code until this Google doc is accepted.
[1293.60 --> 1299.78]  But you reach a point where the document is accepted.
[1300.96 --> 1305.66]  And as you get further along in your implementation, things change.
[1305.88 --> 1310.90]  Do you go back and change the record of these decisions?
[1311.16 --> 1311.96]  How do you do that?
[1312.00 --> 1317.36]  I think one of the frustrating things in Google docs, I think it exists, but it's not always
[1317.36 --> 1321.40]  easy to find is there's not like a get blame functionality.
[1321.40 --> 1326.42]  I can't see what the RFC looked like at all these different points or see things highlighted
[1326.42 --> 1333.54]  like this edition was made after this was accepted, right?
[1333.98 --> 1336.06]  And I'd love to go back and make notes on it.
[1336.10 --> 1341.30]  And I think there's an appropriate window, like maybe one or two months after the RFC that
[1341.30 --> 1342.94]  you can go back and add things to that.
[1343.30 --> 1349.48]  But I mean, imagine if I were to go back to one of the original RFCs for console that's
[1349.48 --> 1352.08]  a couple years old now and start making changes.
[1352.50 --> 1360.16]  That would feel wrong because I'm disturbing this document that is a record, even though
[1360.16 --> 1362.86]  maybe I'd be making it more accurate.
[1363.70 --> 1365.00]  I have a couple immediate reactions.
[1365.40 --> 1369.92]  One is this is a big advocate in favor of Git-based RFCs.
[1370.14 --> 1370.32]  Yeah.
[1370.32 --> 1378.16]  Because I think the sort of pull request based process and the resulting commit based historical
[1378.16 --> 1385.12]  record is order of magnitudes better than what you end up with in tools like Google Docs
[1385.12 --> 1386.46]  or Confluence or anything like that.
[1386.88 --> 1390.04]  And it lets you have a discussion about why are we updating this?
[1390.34 --> 1392.78]  Should it actually be updated or should this be a new version?
[1392.92 --> 1394.20]  And this is a historical version.
[1394.34 --> 1397.42]  Like how does what's the right approach to it?
[1397.42 --> 1399.44]  So I think that's one piece of this.
[1399.86 --> 1405.00]  The other immediate reaction is that I think your sort of core question of what are the
[1405.00 --> 1410.74]  timelines under which this can be revised is actually something that is important to hash
[1410.74 --> 1416.48]  out broadly within a culture and individually for a particular RFC, right?
[1416.50 --> 1421.66]  Like what are the conditions and timeframes under which revisions to this RFC are acceptable?
[1422.32 --> 1422.58]  Mm-hmm.
[1422.58 --> 1423.18]  No.
[1423.18 --> 1423.48]  No.
[1423.56 --> 1427.60]  And I don't know if I've ever been in an engineering culture that has really laid that
[1427.60 --> 1429.40]  down in a concrete way.
[1429.58 --> 1436.72]  I mean, what is the appropriate window where you can make those adjustments kind of becomes
[1436.72 --> 1439.66]  this, does it feel right?
[1440.14 --> 1446.64]  Like I can tell which ones feel right, but I don't know if everyone would agree on what
[1446.64 --> 1447.54]  that window is.
[1447.54 --> 1448.38]  Mm-hmm.
[1448.38 --> 1455.90]  And I think one thing I've really enjoyed going back to the idea of these Git-based RFCs is
[1455.90 --> 1460.22]  I've participated recently in work in the Kubernetes.
[1460.62 --> 1461.84]  Now I'm bringing up Kubernetes.
[1462.08 --> 1462.66]  Sorry, everyone.
[1463.68 --> 1471.94]  Kubernetes contributor space around the gateway API and a project called Gamma.
[1471.94 --> 1477.80]  And the only thing to bring up there is all of these proposals, these gateway enhancement
[1477.80 --> 1485.30]  protocols or gateway enhancement proposals or gaps are submitted in GitHub and we can track
[1485.30 --> 1485.84]  all that stuff.
[1485.94 --> 1489.68]  It's just fantastic to have that record.
[1490.48 --> 1495.30]  That works well in an environment where everyone involved in the process is a developer.
[1495.90 --> 1496.14]  Yeah.
[1496.56 --> 1498.54]  That's a tough problem to solve.
[1498.68 --> 1499.78]  It's a really tough problem.
[1499.78 --> 1501.92]  I have not seen it solved completely.
[1501.92 --> 1509.12]  This is really though where I do feel like language models have the most potential for
[1509.12 --> 1515.62]  impact is in adding these correlations between these seemingly disparate sources if they get
[1515.62 --> 1516.32]  access to them.
[1516.76 --> 1518.10]  Making those connections and inferences.
[1518.28 --> 1518.44]  Yep.
[1518.98 --> 1526.54]  Though, once again, I think, so there's a question of connecting between disparate pieces, but then
[1526.54 --> 1532.06]  there's also a question that around kind of what Thomas is saying of like, where is the
[1532.06 --> 1535.08]  source of truth and how is that updated?
[1535.54 --> 1538.40]  I don't think a language model should be a source of truth.
[1538.82 --> 1539.16]  No.
[1539.30 --> 1542.12]  I think that's, that sounds like a very dangerous proposition.
[1542.68 --> 1548.78]  It might be one that recognizes sort of the constellation of different things out there
[1548.88 --> 1553.00]  that connect to the source of truth, prompts you when the source of truth should be updated,
[1553.00 --> 1553.84]  things like that.
[1554.26 --> 1558.54]  But, but there is still this core question of what is the source of truth?
[1559.00 --> 1561.04]  When and how can it be updated?
[1561.04 --> 1563.36]  And how does that relate to the historical record?
[1564.06 --> 1565.82]  Not sure that we have an answer for that.
[1566.48 --> 1571.64]  No, but maybe there's somebody listening who can develop that product and it needs to be
[1571.64 --> 1573.94]  usable by engineers.
[1574.14 --> 1576.20]  There needs to be VIM bindings.
[1576.20 --> 1583.88]  There needs to be the ability for multiplayer and comments, complete history, tracking between
[1583.88 --> 1590.84]  multiple documents to show that this RFC affects a decision that was made in this RFC.
[1591.70 --> 1599.00]  And then there also needs to be a machine learning model on top of all that to tell us all of the
[1599.00 --> 1600.50]  reasoning behind all the decisions.
[1600.50 --> 1603.62]  And it needs to be able to not make stuff up.
[1603.94 --> 1605.30]  So that's just, that's the product.
[1605.64 --> 1607.54]  I think all you need is a name and that.
[1607.82 --> 1609.04]  Sounds like a weekend project, right?
[1609.06 --> 1609.94]  That's a weekend project.
[1610.06 --> 1610.58]  Yeah, really.
[1612.22 --> 1618.62]  So speaking of timelines, there's a question in the Slack chat of what is the longest time
[1618.62 --> 1621.52]  over which you've ever chased down a single bug?
[1622.02 --> 1624.36]  What was wrong and how did you finally figure it out?
[1624.92 --> 1625.96]  That's a tough one.
[1627.22 --> 1629.78]  Longest time chasing a single bug.
[1630.50 --> 1635.40]  I mean, I could say that in general, the category of bugs that take me the longest to solve
[1635.40 --> 1645.12]  are usually in some kind of serialization of something that doesn't, that isn't nicely
[1645.12 --> 1645.72]  formatted.
[1646.56 --> 1656.10]  I have had fun experiences working with YAML where I think a lot of the categories of bugs
[1656.10 --> 1657.26]  that I had to solve.
[1657.26 --> 1666.34]  So what I had to do is ingest YAML and then parse that and create a rules engine around
[1666.34 --> 1671.48]  that and say like, if this is set, then this can't be set and had to navigate up and down
[1671.48 --> 1672.18]  that tree.
[1672.18 --> 1681.72]  But part of the YAML in this configuration was executable script.
[1682.18 --> 1691.18]  So I'd have to grab that, execute that script, get the output, trace back and find the...
[1691.18 --> 1696.50]  So at that point, I'm holding in my hands the response from the script.
[1696.66 --> 1703.40]  I'm holding the JSON parsed model of that YAML.
[1703.40 --> 1712.96]  And I'm also holding a reference to that line number where the error occurred.
[1713.26 --> 1717.98]  So being able to report back and say, I mean, when you're running code and you end up with
[1717.98 --> 1726.18]  some sort of error message that's like missing semicolon at da da da da da, like some crazy
[1726.18 --> 1729.16]  line that's or something that's outside of your code.
[1729.16 --> 1735.38]  Even those kinds of problems where you're trying to parse something in and keep track
[1735.38 --> 1740.64]  of all these different parts of the data so that you can report back and say, your error
[1740.64 --> 1744.30]  is with pretty confident it's here.
[1744.64 --> 1748.58]  But there are all kinds of problems around that where you could have multiple keys where
[1748.58 --> 1753.16]  you don't know whether or not what you're being fed is complete.
[1753.16 --> 1762.82]  And the user could get back some crazy bugs just because I would parse a string from the
[1762.82 --> 1767.86]  beginning of this value all the way to the end of the document and having to solve bugs
[1767.86 --> 1768.34]  around that.
[1768.42 --> 1771.22]  It was really hard to track down all of the error cases.
[1771.34 --> 1777.94]  So that's not a single bug, but it was a whole family of bugs as I process that trying to get
[1777.94 --> 1783.24]  YAML and these scripts to give you feedback on whether or not this was a legit input.
[1784.04 --> 1786.38]  Evalling code that lives within YAML.
[1786.64 --> 1789.98]  Just as soon as you said that, I got goosebumps.
[1790.50 --> 1793.36]  That sounds terrifying.
[1794.32 --> 1801.80]  This project at one point, we were given the instruction that users should be able to
[1801.80 --> 1806.90]  add or annotate their configuration with comments.
[1807.40 --> 1814.16]  And so it was suggested that we write our own YAML parser that would also read in comments.
[1814.56 --> 1820.10]  And I did manage to dissuade the idea that we go and write our own YAML parser that also
[1820.10 --> 1820.86]  includes comments.
[1821.90 --> 1823.52]  I was like, that is a bad idea.
[1824.16 --> 1829.54]  I was trying to think of mine and I don't fully remember the specifics of it, but it took
[1829.54 --> 1831.38]  me probably a good solid week.
[1831.46 --> 1838.08]  And it was something as silly as just animations, like not working properly, but it was not
[1838.08 --> 1842.20]  something that you could test locally because it worked every time locally.
[1842.50 --> 1844.12]  It was only out in production.
[1844.78 --> 1852.12]  But this was in the golden age, I think, of JavaScript where we were using, this is a
[1852.12 --> 1852.70]  dojo project.
[1852.70 --> 1857.50]  And so we would have been using AMD or asynchronous module definitions, which are effectively the
[1857.50 --> 1860.12]  same in production and development.
[1860.32 --> 1865.96]  Like there's, you build by just combining them all together, but otherwise like they're
[1865.96 --> 1867.76]  all the same exact thing.
[1868.32 --> 1874.16]  And so this was the first time I learned how to use Charles proxy to like on the production
[1874.16 --> 1880.12]  site proxy in my local copy of the app, but it was just basically the same thing.
[1880.14 --> 1881.36]  So I wasn't having to run a build step.
[1881.36 --> 1885.86]  I just make code changes and then refresh and it was like grabbing from my local machine
[1885.86 --> 1889.62]  instead and was able to reproduce the bug over and over and over again.
[1890.12 --> 1896.56]  And it ended up being something where it was like a race condition between when animations
[1896.56 --> 1900.90]  finish and some script that was being injected at the time.
[1901.02 --> 1905.82]  And because of some network speed, but the way that it was doing it, like you couldn't even
[1905.82 --> 1909.92]  test that with, um, with like the, you know, slow 3g or whatever.
[1910.06 --> 1910.16]  Yeah.
[1910.16 --> 1910.72]  The dev tool.
[1911.22 --> 1913.48]  And so I can't remember exactly why.
[1913.62 --> 1919.10]  So this is a horrible story, but it eventually, you know, came down to like effectively being
[1919.10 --> 1926.12]  some CSS animation code that was by reworking it or coming at it from a different angle.
[1926.12 --> 1931.06]  We were able to effectively make the bug go away, which was good enough for this case.
[1931.06 --> 1935.74]  But it was, it was like a week straight of just like loading this production site, trying
[1935.74 --> 1939.74]  to figure it out, proxying my own code and running through it.
[1940.28 --> 1940.38]  Yeah.
[1940.42 --> 1940.80]  It was a nightmare.
[1940.94 --> 1947.56]  No, I think you're, you're hitting on an entire class of really difficult bugs where the actual
[1947.56 --> 1951.40]  source of the bug is the environment in which the code is running.
[1951.62 --> 1953.90]  And so it's could be mysterious.
[1953.90 --> 1961.16]  And I think we've gotten better in general at replicating the dev and test and production
[1961.16 --> 1962.00]  environments.
[1962.52 --> 1968.08]  Docker has been a huge benefit here, but it's still not perfect.
[1968.08 --> 1975.16]  And those are really hard to debug because there are invisible things that you might never
[1975.16 --> 1977.88]  realize that you were even setting in the first place.
[1978.34 --> 1978.42]  Yeah.
[1978.72 --> 1981.70]  My debugging horror story is exactly one of those.
[1981.70 --> 1985.02]  This took me on the order of a month to debug.
[1985.58 --> 1987.00]  And the situation was this.
[1987.14 --> 1991.02]  So we were hosting our code on Google App Engine.
[1991.72 --> 1998.00]  And at some point in December, this was probably December 2019 or something like that.
[1998.58 --> 2004.12]  The, we started having outages where once traffic would hit to some certain point, the machines
[2004.12 --> 2007.56]  would just start swapping, like freaking out, swapping out of nowhere.
[2008.02 --> 2011.34]  And then like we'd have, you know, cascading outages.
[2012.52 --> 2016.08]  And we could not figure out what was going on.
[2016.08 --> 2020.10]  And we tried like, because it was, it was App Engine, everything was Dockerized.
[2020.28 --> 2022.26]  We had old bundles.
[2022.48 --> 2025.16]  We had old instances and we could actually recreate.
[2025.36 --> 2028.84]  We had an old instance that would not exhibit as far as we could tell the bug.
[2028.92 --> 2033.12]  Now we didn't have a perfect reproduction case because it was tied to some amount of traffic.
[2033.12 --> 2035.72]  So we weren't sure what the situation was.
[2035.84 --> 2038.74]  But we had an old bundle that seemed to not reproduce it.
[2039.24 --> 2045.12]  However, if we took that snapshot of code, rebuilt it, deployed it, it would reproduce the issue.
[2045.12 --> 2053.30]  And so we were able to sort of pinpoint, okay, something changed in the environment around between, you know, X date and Y date.
[2053.38 --> 2054.22]  I don't remember what they were.
[2054.98 --> 2060.62]  And we were like going back and forth with Google support and can't figure things out and all these different things.
[2060.62 --> 2066.08]  I will say a potentially important piece of information, Google App Engine has multiple variants.
[2066.84 --> 2073.16]  We had some applications being deployed on App Engine Standard, which were not showing this.
[2073.32 --> 2076.60]  And some that were deployed on App Engine Flex, which were showing this problem.
[2076.60 --> 2079.04]  So we thought, okay, maybe it's related to that.
[2079.12 --> 2083.28]  But not all of our applications were such that we could move them over to standard.
[2083.42 --> 2088.26]  They were using, you know, different Docker images, which you could do custom on Flex and not on the other.
[2088.60 --> 2090.12]  So we couldn't just switch out of it.
[2090.72 --> 2093.36]  We went on and on and on trying to find different things.
[2093.86 --> 2096.40]  And their support was worthless, absolutely worthless.
[2097.02 --> 2101.38]  But after a month of tracking this down, there were a few different things that came up.
[2101.38 --> 2107.60]  So one is we were able to see that the leading indicator that seemed to go into this is suddenly we would get lots of disk traffic.
[2108.44 --> 2115.42]  And so there would be lots of disk traffic on these instances for reasons we had no idea, including instances that, like, we weren't writing anything to disk.
[2115.48 --> 2116.48]  Like, what is going on?
[2116.80 --> 2122.36]  And this disk traffic would start thrashing the I.O., which would then thrash everything, and it would cascade down.
[2123.32 --> 2131.26]  Eventually, what we were able to do was we were able to get SSH into the boxes and actually get out of our application environment.
[2131.26 --> 2137.48]  And just kind of look around and catch when one of these is going on and find out what was writing all this disk traffic.
[2138.08 --> 2144.66]  And it turns out Google App Engine uses Fluent to handle all or FluentD to handle all of its logging.
[2144.82 --> 2152.00]  Now, if you're not familiar with FluentD, it's basically just like, you know, system software that pulls in logs and pipes it other places, right?
[2152.06 --> 2154.02]  Manages your log, you know, and it's a multiplexer.
[2154.10 --> 2156.86]  So you can pull it from some locations, push out to other locations.
[2156.86 --> 2169.44]  And it has this functionality where if it can't write, it's trying to write a log somewhere and the network fails or times out, it will dump the logs it's trying to write to disk.
[2169.98 --> 2175.84]  And then five minutes later, it'll try to load up all the things that have been, and it's on some sort of fallback mechanism.
[2175.84 --> 2180.82]  But sometime later, it'll try to load up all those things and rewrite them, assuming network failures are transient.
[2180.82 --> 2183.14]  And it doesn't get that, it'll dump them back.
[2183.24 --> 2186.42]  And if it's the same set, it'll dump more and more and more.
[2186.70 --> 2194.40]  And what had happened was Google had changed the location of one of the places that they internally dump logs to.
[2194.90 --> 2200.90]  And they had updated this in App Engine Standard, but they had somehow managed to not update this in App Engine Flex.
[2201.10 --> 2205.44]  So FluentD would just keep trying to write to the old location, say, it's not working.
[2205.56 --> 2206.42]  This must be temporary.
[2206.56 --> 2207.78]  Let me dump a bunch of stuff to disk.
[2207.96 --> 2209.52]  Let me load all that stuff up to disk.
[2209.52 --> 2210.64]  Go, go, go.
[2210.72 --> 2213.78]  And there are timeout mechanisms after which it'll drop the logs.
[2213.92 --> 2223.86]  But at some threshold of traffic, you would start thrashing the disk so much that the machine fell over before you got to the threshold where you would drop those old logs.
[2224.32 --> 2227.76]  And we were able to flag this, point this to them, say, FluentD changed.
[2227.90 --> 2228.92]  Here's where it's trying to send to.
[2228.92 --> 2229.42]  And they could go fix it.
[2229.42 --> 2230.34]  It happened in these times.
[2230.48 --> 2232.10]  And then finally, they said, oh, you're right.
[2232.32 --> 2234.18]  I guess it is our problem after all.
[2234.36 --> 2234.78]  We'll fix it.
[2235.42 --> 2237.78]  I mean, I get it from their end.
[2237.78 --> 2242.48]  And it's hard when you have people who are using your product and saying, oh, something's wrong.
[2242.58 --> 2245.08]  And sometimes it's like, oh, well, you are holding it wrong.
[2245.24 --> 2247.36]  But no, really, when you can point that out.
[2247.42 --> 2256.36]  And I think you have this real perfect storm of a bug there where not only do you have this environmental aspect where you can't see the real cause.
[2256.36 --> 2260.34]  The easiest bugs to fix are ones where you can see all the inputs.
[2260.74 --> 2262.06]  You can see all the outputs.
[2262.26 --> 2266.46]  You can see each step of how they are transformed.
[2267.10 --> 2271.22]  You can go, oh, OK, I can put a breakpoint here, here, here, here.
[2271.32 --> 2271.74]  OK.
[2271.74 --> 2284.68]  But when your bug is dependent on all these conditionals like traffic load, like traffic load itself is such a pain to replicate, especially if you're working on a smaller project.
[2285.38 --> 2288.08]  You know, when you're working at scale, you want to have that kind of testing.
[2288.26 --> 2290.22]  But that really does.
[2291.16 --> 2292.66]  Oh, man.
[2292.66 --> 2301.80]  So, K-Ball, your bug kind of leads into another one of Thomas's questions that I want to ask, which is how much back end should a front end dev know?
[2302.88 --> 2304.62]  Is this for me or is this for K-Ball?
[2305.10 --> 2306.02]  For either of you.
[2307.00 --> 2307.44]  Hmm.
[2308.20 --> 2309.20]  What do you think, K-Ball?
[2309.42 --> 2311.00]  I think it really depends on what you want to do.
[2312.04 --> 2320.40]  So the advantages of knowing back end, even if you're working primarily in the front end, is you get a much better sense of what is and is not possible.
[2320.40 --> 2331.36]  And a much easier time talking with your back end partners about what you need and how you have a good detector.
[2331.74 --> 2334.42]  You can understand what's going to be easy, what's going to be hard.
[2335.24 --> 2346.50]  And if, for example, you're in a small company where people move around a little bit, sometimes some folks are overloaded, like, and you just need a darned API endpoint hooked up, maybe sometimes you go down and you hook it up.
[2347.66 --> 2349.44]  So there's a lot of advantages to that.
[2350.40 --> 2355.88]  That being said, I also think that it's like everything we've been talking about.
[2355.94 --> 2356.86]  It's environment dependent.
[2357.16 --> 2370.50]  If you're in a place where you have large enough teams that you can legitimately purely focus on the front end and there's a clean interface to the back end, maybe everything's going through GraphQL or something else, you don't need that.
[2371.22 --> 2374.00]  So it really depends on your setting and what you want.
[2374.00 --> 2390.30]  What about in terms of like the front end deployment or, I don't know, like serverless, like learning, you know, AWS Amplify or whatever the Google Cloud or Azure equivalents are or Vercel or Netflify.
[2390.30 --> 2396.78]  Like there's a lot of a lot of different pieces that are more like company specific depending on what back end.
[2397.24 --> 2397.32]  Yeah.
[2397.38 --> 2401.66]  I mean, if you're working in an environment where they've got tools and they just work, like why?
[2402.54 --> 2403.76]  It's your setting, right?
[2403.88 --> 2411.18]  If you're working in a small company in a startup and you're blocking for hours on end because you're waiting for the expert on this, like, yeah, learn it.
[2411.22 --> 2412.74]  And then you can get it done.
[2412.74 --> 2418.34]  But if you're working in a big company where they have push button tools and it just works, like you don't need that trash.
[2418.70 --> 2419.66]  Like, just let it go.
[2420.22 --> 2431.28]  No, I think that as you work in the front end, the more that you might know of the back end, it allows you to have that ability to navigate around these blockers.
[2431.28 --> 2440.98]  I mean, I've had times when I'm debugging something that's building on Vercel or on Netlify or working in that way.
[2441.10 --> 2446.58]  And I've had the Jurassic Park moment of, oh, it's a Unix system.
[2446.82 --> 2448.60]  And I just go, oh, yeah, this is Linux.
[2448.88 --> 2453.26]  I can SSH into this and then I can figure out this is why this thing is weird.
[2453.92 --> 2458.22]  And that, I think, will always be valuable.
[2458.22 --> 2463.20]  But then again, I'm a little bit more biased towards the back end because that's where I spend most of my time.
[2463.96 --> 2465.44]  But you don't need to know EBPF.
[2465.68 --> 2466.80]  You don't need to know EBPF.
[2466.96 --> 2467.70]  That's okay.
[2468.18 --> 2469.74]  Good, because I don't know what that stands for.
[2470.92 --> 2471.66]  I don't either.
[2472.82 --> 2474.36]  It's the new hotness.
[2474.36 --> 2477.36]  Early bird performance framework.
[2478.38 --> 2480.72]  Extended Berkeley packet filters.
[2480.92 --> 2488.08]  This allows you to read and respond to any of the Linux syscalls as they occur.
[2488.78 --> 2489.14]  Interesting.
[2489.72 --> 2490.90]  It's the new hotness.
[2491.56 --> 2492.36]  It's not even that new.
[2493.76 --> 2496.12]  As soon as you said Berkeley, I was like, yeah, it's probably not new.
[2496.26 --> 2496.90]  It's Berkeley.
[2500.94 --> 2504.90]  I think it also, another thing to bear in mind here is where you are in your career.
[2505.22 --> 2505.62]  Right?
[2505.62 --> 2513.28]  Like, if you are early in your career, it is way too easy to spread yourself too thin.
[2513.96 --> 2514.36]  Right?
[2514.46 --> 2525.84]  Like, this field is so big and so wide and changes so fast that if you're trying to learn everything at once, you're never going to get anywhere.
[2525.84 --> 2530.50]  So, if you're early in your career, I would pick one place to focus.
[2530.76 --> 2533.22]  And further than that, I wouldn't just focus on frontend.
[2533.30 --> 2535.76]  Frontend itself is so massively wide.
[2535.96 --> 2543.28]  Like, I would focus on, okay, I'm going to learn how to do good web-based frontends using React or using Vue.
[2543.28 --> 2550.20]  Or I'm going to learn how to build good mobile frontends using, I'm not a mobile developer, but one particular framework.
[2550.32 --> 2554.54]  Whether it's, you know, Flutter or it's React Native or what have you.
[2555.18 --> 2562.34]  After you feel like you can deliver just about anything you need in that space, now you can start to diversify.
[2562.46 --> 2566.30]  I mean, you could do it before that, but my sense is you'll be thrashing yourself.
[2566.46 --> 2566.58]  Right?
[2566.60 --> 2570.66]  It's hard to learn the level of depth when you're trying to do everything at once.
[2571.06 --> 2575.16]  And once you do have that level of depth, the other things become easier to learn.
[2575.16 --> 2578.92]  Because as broad as this field is, there are a lot of related concepts.
[2579.14 --> 2580.96]  And you are going to be able to pick things up faster.
[2580.96 --> 2586.18]  So early career, don't even, like, try to do backend as well as frontend.
[2586.28 --> 2589.28]  Like, pick one lane in frontend and specialize there.
[2589.52 --> 2597.00]  And once you are really feeling comfortable there and able to deliver just about anything anyone asks you of it, then start to branch out.
[2597.00 --> 2605.58]  What I think might be the most valuable, like, as you branch out, too, is not to go and buy a book on Linux internals.
[2605.58 --> 2618.32]  But to start off by working your way back through the dev tools, through the networking tools in your browser or whatever your frontend environment makes accessible to you.
[2618.80 --> 2626.10]  See the network and then learn tools that allow you to debug what's going on in the backend.
[2626.46 --> 2629.54]  Or at least see how these things might connect.
[2629.66 --> 2632.08]  And then you can Google your way through to a solution.
[2632.52 --> 2633.44]  Yeah, I think that's great advice.
[2633.44 --> 2635.78]  And it's like a more focused path, too.
[2635.88 --> 2645.26]  If you're looking at how to interface through the parts that you're already touching through the network interface, then you have, like, a starting point rather than, here's Linux.
[2646.00 --> 2646.42]  Okay.
[2647.34 --> 2648.52]  What do you want to know?
[2649.20 --> 2650.64]  Start reading the source code.
[2650.64 --> 2657.68]  No, actually, I've been mentoring someone as they've gotten into tech.
[2658.02 --> 2660.34]  And we're working on a project together.
[2660.58 --> 2665.34]  And I showed him the Chrome dev tools and the networking tools.
[2665.54 --> 2669.18]  And I just encouraged him, go to different websites.
[2669.88 --> 2672.38]  See how does Reddit load its front page?
[2672.50 --> 2675.88]  How does Netflix stream in a video?
[2675.88 --> 2680.74]  You don't need to understand the details of what's happening on that backend.
[2681.34 --> 2685.78]  But what do things look like as they come to you through the network?
[2685.96 --> 2689.02]  And what do these different protocols mean?
[2689.02 --> 2692.74]  Hello, friends.
[2693.18 --> 2696.40]  This is Jared here to tell you about Changelog++.
[2697.10 --> 2704.58]  Over the years, many of our most diehard listeners have asked us for ways they can support our work here at Changelog.
[2704.82 --> 2707.30]  We didn't have an answer for them for a long time.
[2707.66 --> 2714.40]  But finally, we created Changelog++, a membership you can join to directly support our work.
[2714.40 --> 2725.62]  As a thank you, we save you some time with an ad-free feed, sprinkle in bonuses like extended episodes, and give you first access to the new stuff we dream up.
[2726.10 --> 2729.48]  Learn all about it at changelog.com slash plus plus.
[2729.72 --> 2733.04]  You'll also find the link in your chapter data and show notes.
[2733.64 --> 2736.68]  Once again, that's changelog.com slash plus plus.
[2736.90 --> 2737.52]  Check it out.
[2737.90 --> 2738.90]  We'd love to have you with us.
[2744.40 --> 2746.66]  We did get one question.
[2746.78 --> 2750.88]  We asked this question also on Mastodon, and we got one response.
[2751.50 --> 2755.56]  And so what is an underrated library or package?
[2756.10 --> 2767.22]  An underrated library or package is a package that doesn't get enough attention proportional to how valuable it is.
[2770.04 --> 2771.68]  Do you have an example of that?
[2771.68 --> 2771.90]  Oh.
[2774.40 --> 2776.98]  Well played, sir.
[2777.38 --> 2777.70]  Yeah.
[2778.06 --> 2778.50]  Yeah.
[2778.94 --> 2787.12]  I really, working with Svelte and the MDSVX library has been fantastic.
[2787.24 --> 2788.14]  Are you familiar with this?
[2788.34 --> 2801.46]  It's very similar to the MDX that you see in React, where you can write these markdown files that use components from React,
[2801.46 --> 2803.62]  and you can just pull that right in.
[2803.62 --> 2820.90]  But with MDSVX, I don't know how they want us to say it, but that is the equivalent for Svelte, where you can, and Svelte is such a great library, such a great framework for creating personal blogs and websites like that.
[2820.90 --> 2832.06]  And being able to then bring in Svelte components into your markdown is such a superpower because you can write your own, say, code block.
[2832.06 --> 2841.72]  You can build really cool models or use, you can use a 3D asset in Svelte.
[2841.80 --> 2844.80]  You can create that in a component and then just use it in markdown.
[2844.96 --> 2846.00]  It's such a superpower.
[2846.00 --> 2848.68]  I've really enjoyed doing that in the past.
[2849.08 --> 2854.46]  I have a package that is extremely widely used, and yet I would still say underrated, and that's ESLint.
[2855.00 --> 2862.70]  And the way in which I think it's underrated is just about everyone uses it and a set of linters out of the box.
[2863.10 --> 2866.88]  They'll pull down a template from somewhere, or they'll use one of the built-ins.
[2866.88 --> 2870.46]  We, as developers, all develop opinions.
[2871.22 --> 2874.94]  Our teams develop ways of doing things and ways not of doing things.
[2875.22 --> 2880.90]  Writing custom linters and custom configurations in ESLint is something I want to see way more teams doing
[2880.90 --> 2893.04]  because I think the ability to put in those kind of automatic ratchets that check for the types of stylistic things that your team looks for
[2893.04 --> 2901.38]  are extremely valuable and will cut down a lot of people's time where otherwise they'd have to do that in code reviews and other places.
[2901.92 --> 2908.22]  So I think as widely used as ESLint is, it is still extremely underutilized and therefore underrated.
[2908.70 --> 2908.82]  Yeah.
[2908.90 --> 2912.34]  What do you think is keeping it underrated?
[2912.46 --> 2915.56]  Do you think there needs to be more accessibility to writing your own rules?
[2915.68 --> 2917.50]  Is that a culture that needs to be created?
[2917.64 --> 2918.68]  Why is that not happening?
[2918.68 --> 2927.26]  I think probably because some projects bring it in automatically by default.
[2927.40 --> 2931.50]  I just was messing around with Next13 and it brings in its own ESLint rules,
[2931.62 --> 2935.92]  which is great because it helps you with the server components piece of it, right?
[2936.00 --> 2940.60]  It'll warn you if you're trying to use things that you can't use in a server component, for example.
[2941.16 --> 2941.96]  Super cool stuff.
[2942.10 --> 2946.98]  The React rules are great too because they'll tell you you're not using useState properly.
[2946.98 --> 2953.42]  You're not passing the right things to the second argument, the array of values that it has to check.
[2953.86 --> 2962.76]  Where I think it falls down for a lot of people or it just becomes super overwhelming is when you start bringing in Airbnb's rules and just blindly accepting them.
[2963.46 --> 2967.14]  And you're wondering, what's it yelling at me about this type?
[2967.14 --> 2975.08]  And you lose faith in it pretty quickly when it's starting to warn you about all these things that you really don't care about.
[2975.58 --> 2979.64]  I've made that exact mistake before with the Airbnb.
[2980.64 --> 2982.88]  Especially as somebody who's more of a back-end dev.
[2982.92 --> 2986.86]  When I've worked on front-end projects and really one of my first instances is like,
[2986.92 --> 2990.46]  oh, I want to bring in all the tools around to make this the best.
[2990.46 --> 2994.64]  And I was like, no, I know what I'm doing.
[2995.06 --> 2997.34]  No, I don't need that suggestion.
[2997.54 --> 2997.98]  Thank you.
[2998.18 --> 2999.72]  But like, oh, man.
[3000.04 --> 3005.74]  Well, and this comes back to what to me has been a running theme in our conversation, which is it's situation dependent.
[3006.20 --> 3006.40]  Yeah.
[3006.56 --> 3006.72]  Right?
[3007.32 --> 3009.72]  Airbnb's rules were specific to their situation.
[3010.20 --> 3013.02]  And they published them on open source, which is great.
[3013.02 --> 3017.98]  But then we try to pull them down and apply them blindly as if they're going to apply to our situation.
[3018.80 --> 3020.08]  Probably they won't.
[3020.42 --> 3020.50]  No.
[3020.76 --> 3020.88]  Yeah.
[3021.16 --> 3030.52]  I think to your question, we as developers, I think we think about our own personal environments a fair amount.
[3030.62 --> 3038.98]  But I don't think we tend to think about our team environment as just as important for us to be optimizing and thinking about.
[3038.98 --> 3044.34]  Probably because it involves having to have conversations with people and reach agreement on stuff.
[3044.58 --> 3064.22]  But the most effective teams I've been on are constantly having this conversation of how do we as a team want to improve our approach or align our approach or get better synced on our approach rather than just a bunch of individual developers running their own ways.
[3064.38 --> 3064.82]  Yeah.
[3064.90 --> 3067.90]  No, I think you're pointing to the right thing around the messiness of humans.
[3067.90 --> 3073.22]  And I think one other aspect there is that it's constantly changing.
[3073.58 --> 3075.66]  You will add new people to your team.
[3075.78 --> 3076.60]  People will leave.
[3076.70 --> 3077.74]  People will get promoted.
[3078.16 --> 3086.86]  I, at one point, was working at a company and we had a senior engineer with a lot of tenure come into a project.
[3087.48 --> 3089.70]  And we had been working on this JavaScript project.
[3089.90 --> 3095.22]  And I don't know why we had made this decision, but we were using two spaces to indent.
[3095.22 --> 3098.22]  And all the code was using two spaces to indent.
[3098.90 --> 3107.66]  And the first thing this person contributed to the code base was to change the indentation for the entire code base to four spaces.
[3108.20 --> 3108.96]  Didn't ask.
[3109.62 --> 3113.62]  Just opened up a pull request and approved their own pull request.
[3113.74 --> 3114.74]  They probably shouldn't have been able to.
[3114.74 --> 3116.50]  That was probably an oversight.
[3117.22 --> 3120.42]  But that does not feel good.
[3121.20 --> 3129.36]  And needing to have these difficult conversations around how do we best write code is very difficult.
[3129.50 --> 3132.58]  I mean, I can understand some of the hate around Go.
[3132.72 --> 3135.74]  But this is something that Go has gotten really right.
[3135.74 --> 3138.90]  There are no arguments about what Go should look like.
[3139.54 --> 3145.22]  And the nice thing is, regardless of what code base I go into, I know exactly what's going on.
[3145.30 --> 3146.52]  I can read all the code.
[3147.00 --> 3154.90]  Whereas in some of the C++ that I've written in the past, C++ may as well be a different language in every repository you go into.
[3155.08 --> 3157.24]  Because different people pull in different libraries.
[3157.68 --> 3161.58]  And you have to learn that specific flavor in a lot of ways.
[3161.58 --> 3164.88]  It's almost as if, so you mentioned your example.
[3165.10 --> 3166.10]  And you'd made this decision.
[3166.26 --> 3167.16]  You weren't sure why.
[3167.38 --> 3167.58]  Yeah.
[3167.68 --> 3168.84]  And you came in and changed it.
[3169.10 --> 3174.90]  It's almost as if we need some sort of approach or documents for the decisions we make.
[3175.12 --> 3177.44]  And when they need to be reopened or not.
[3177.52 --> 3178.78]  And what the criteria were.
[3178.86 --> 3182.24]  And then we need to ask ChatGPT, why are we using two spaces to indent?
[3183.50 --> 3185.36]  Because you didn't think to use tabs.
[3185.76 --> 3187.44]  Now I'm a big tabs person.
[3187.44 --> 3192.42]  Now, that's when it's been one of my major life shifts in the past few years as I've grown older.
[3192.60 --> 3194.06]  I'm a tabs guy now.
[3194.48 --> 3198.66]  And I think I read that Prettier is going to default to tabs in an upcoming release.
[3198.92 --> 3199.86]  I think it's great.
[3200.42 --> 3200.68]  Yeah.
[3201.16 --> 3202.24]  More accessible, for sure.
[3202.68 --> 3203.56]  I'm all the way on tabs.
[3204.66 --> 3213.06]  It does point back to this problem, though, of we're thinking about the decisions in the product differently than we're thinking about our decisions about our approach to building the product.
[3213.16 --> 3214.34]  And maybe we shouldn't be.
[3214.34 --> 3224.44]  Maybe we should be applying the same level of rigor and iterative thinking and improvement and experimentation to our processes as we are to our products.
[3225.02 --> 3225.14]  Yeah.
[3225.26 --> 3238.04]  And I think that takes a level of ownership and being empowered as an engineer to feel that you can make changes to the code or the repository as a product itself.
[3238.04 --> 3241.62]  I think that's something that's very difficult when you come in on a team.
[3241.88 --> 3247.98]  If you want to be friendly and nice, you don't want to just start saying, we should really be automating this.
[3248.16 --> 3248.98]  We should really be doing this.
[3249.04 --> 3250.12]  Have you thought about dev containers?
[3250.80 --> 3256.72]  But when you are in an environment that you feel empowered to do that, you really can make those changes.
[3256.72 --> 3263.08]  And I think having a sense of experimentation is really valuable there, too.
[3263.86 --> 3265.30]  Also, just knowing how to approach that.
[3266.00 --> 3266.24]  Yeah.
[3266.68 --> 3267.68]  We use spaces.
[3268.04 --> 3269.42]  I would love to use tabs.
[3269.72 --> 3273.04]  I'm not going to open a pull request and merge my own pull request with that.
[3273.26 --> 3275.18]  It's a conversation that has to be had.
[3275.62 --> 3276.60]  And I might lose.
[3276.68 --> 3277.24]  And that's fine.
[3277.24 --> 3291.48]  In Go, in one of the releases recently, they have added a keyword, any, that is equivalent as syntax sugar for interface curly brace, curly brace.
[3291.64 --> 3291.78]  Right?
[3292.24 --> 3299.56]  It's essentially the same as something that when you see interface empty curly braces, what does that mean?
[3299.62 --> 3301.42]  It means it can be any type.
[3301.84 --> 3305.16]  Do we go back in our code base and swap all of them out?
[3305.16 --> 3307.18]  How do you make that as an argument?
[3307.78 --> 3310.06]  Oh, this is what I'm going to go spend some dev time on.
[3310.60 --> 3310.92]  Right?
[3311.20 --> 3312.22]  Do you do it piecemeal?
[3312.46 --> 3313.58]  It's really complicated.
[3313.72 --> 3317.72]  And it's a very sticky, interpersonal thing.
[3318.40 --> 3318.50]  Yeah.
[3318.58 --> 3322.46]  And I think we might have hit our threshold of Go.
[3322.86 --> 3324.44]  So maybe this is where we're going to go.
[3324.44 --> 3324.56]  Oh, OK.
[3324.62 --> 3324.96]  I'm sorry.
[3325.06 --> 3325.74]  No, you can just.
[3325.92 --> 3327.08]  I'm getting kicked off.
[3327.32 --> 3327.44]  What?
[3327.64 --> 3327.82]  Oh.
[3328.74 --> 3330.28]  That hook is coming from the curtain.
[3330.62 --> 3331.02]  Ah!
[3331.02 --> 3335.86]  No, this has been fantastic.
[3336.02 --> 3340.88]  And we are like, this is probably one of the fastest hours we've ever had on this show.
[3341.26 --> 3341.64]  It was just.
[3341.82 --> 3342.48]  This is great.
[3342.64 --> 3343.26]  Flow of.
[3343.52 --> 3343.74]  Yeah.
[3344.28 --> 3348.72]  So with that, any parting thoughts as we play out?
[3349.14 --> 3349.94]  K-Ball, you want to go first?
[3351.36 --> 3352.88]  Everything is context dependent.
[3352.88 --> 3356.32]  And you can't get away from humans.
[3357.14 --> 3361.00]  The problems that you're solving in tech have to do with humans.
[3361.60 --> 3365.12]  You know, when we're talking about decision documents and what's the right approach, it
[3365.12 --> 3367.16]  depends on the people and you need to have conversations.
[3367.16 --> 3373.18]  When we're talking about tabs versus spaces, it depends on the humans and you have to have
[3373.18 --> 3374.12]  conversations with people.
[3374.24 --> 3376.48]  If you're talking about Go versus TypeScript, the answer is TypeScript.
[3378.06 --> 3378.42]  Yes.
[3378.60 --> 3378.88]  Agreed.
[3379.00 --> 3379.24]  Yeah.
[3379.48 --> 3380.86]  No, I mean, I don't disagree.
[3380.86 --> 3382.88]  I love me some TypeScript.
[3383.62 --> 3388.16]  Yeah, I think in a similar vein, when you're thinking about people, you're right that everything
[3388.16 --> 3393.52]  boils down to people making decisions and the interpersonal skills.
[3394.14 --> 3405.28]  I think two pieces, two nuggets of wisdom or whatnot is when you are joining a project,
[3405.28 --> 3415.48]  feel empowered to ask the questions of why and to seek out the answers there and to take
[3415.48 --> 3420.02]  notes around what is a purposefully decided decision?
[3420.12 --> 3421.06]  What's an externality?
[3421.78 --> 3429.22]  And also, as a piece of advice for more senior engineers to whom these decisions seem obvious,
[3429.22 --> 3435.54]  these connections seem obvious, begin to question how obvious they are to other people.
[3436.02 --> 3439.88]  There is, I don't even know if it's real, it might just be apocryphal, but it's a good
[3439.88 --> 3446.38]  story, a concept of knocking and listening, where when you have these two participants in
[3446.38 --> 3454.50]  an experiment, one of them will knock on a table the rhythm to a song and the other person
[3454.50 --> 3456.68]  will try to guess what that song is.
[3457.62 --> 3464.16]  And the person knocking the song characteristically gets upset, frustrated.
[3464.32 --> 3466.72]  Why can you not figure out what I am tapping?
[3467.40 --> 3471.58]  Because they hear the song in their head and they have this context.
[3472.02 --> 3477.44]  And I think as you grow in your understanding of a product, these decisions seem more obvious.
[3477.62 --> 3482.26]  You've been around long enough to know, oh yeah, because, you know, that guy, Bill,
[3482.26 --> 3484.82]  made that decision, that's why we do it this way.
[3484.94 --> 3486.20]  It's obvious.
[3486.32 --> 3487.04]  It feels obvious.
[3487.72 --> 3495.44]  Question that instinct and over-explain and make those decisions transparent because ultimately
[3495.44 --> 3503.52]  we need to foster the right development environment and that environment is the team, not just
[3503.52 --> 3506.58]  your Vim configs and whether or not you use ESLint.
[3508.16 --> 3509.36]  Called out there now.
[3509.74 --> 3510.16]  Yeah.
[3512.26 --> 3513.72]  No, I totally agree.
[3513.72 --> 3519.94]  Like, like an example on ours, on a project I work on is like, you know, we have a lot
[3519.94 --> 3524.84]  of like these weird service things that these weird service files that exist that are like
[3524.84 --> 3527.34]  singletons that don't do a whole lot.
[3527.58 --> 3531.54]  And, you know, new developers come in and they're like, oh, they don't question it.
[3531.54 --> 3532.30]  They just start using it.
[3532.34 --> 3533.66]  They start replicating those everywhere.
[3533.66 --> 3539.12]  And the actual reason why we have those is because when we converted to React, we converted
[3539.12 --> 3543.00]  from Angular and that was the style at the time in Angular.
[3543.26 --> 3544.74]  So they brought it over to React.
[3545.18 --> 3546.06]  We shouldn't really be...
[3546.06 --> 3546.86]  It was the fashion at the time.
[3547.34 --> 3548.90]  Everyone wore an onion on their belt.
[3550.32 --> 3551.30]  Glad you got the reference.
[3551.54 --> 3551.64]  Yeah.
[3551.64 --> 3558.18]  And like, you know, no, very few people actually come in and be like, why are we doing it this
[3558.18 --> 3558.28]  way?
[3558.28 --> 3559.48]  Could we be doing it better?
[3559.62 --> 3560.58]  Should we be doing it better?
[3560.58 --> 3562.14]  I think we should.
[3562.44 --> 3568.50]  Like the real reason why we're at like so many decisions is because somebody did it once
[3568.50 --> 3569.70]  and then we replicated that.
[3569.82 --> 3574.14]  But there was no real thought that went into that initial implementation.
[3574.86 --> 3579.50]  And it's totally fine to come into a project and, you know, question everything.
[3579.58 --> 3584.86]  Don't just go change it like in the case of the tabs versus spaces, but definitely question
[3584.86 --> 3589.10]  it and, you know, make the teams defend their positions on things.
[3589.10 --> 3591.18]  I think that can be really powerful.
[3591.36 --> 3595.66]  I think it takes a team that can be open to that and is accepting.
[3595.92 --> 3600.18]  And I think that psychological safety plays an important role.
[3600.38 --> 3606.64]  And if you want to trace back where psychological safety can lead to better development, faster
[3606.64 --> 3610.00]  velocity, et cetera, that's it there.
[3610.18 --> 3614.20]  Can you ask these questions and say, why are you doing that this way without the answer
[3614.20 --> 3616.72]  being because that's how it's done?
[3616.78 --> 3618.36]  Like, please stop asking questions, right?
[3618.36 --> 3620.52]  And you need to be polite.
[3620.66 --> 3620.98]  You don't want to jump into a...
[3620.98 --> 3621.56]  Your tone matters.
[3621.88 --> 3622.50]  Yeah, your tone matters.
[3622.50 --> 3625.42]  Why the heck are you using tabs instead of spaces?
[3625.74 --> 3625.90]  Yeah.
[3625.96 --> 3627.26]  Or you guys are using JavaScript?
[3627.42 --> 3628.40]  Use TypeScript, you know?
[3628.52 --> 3628.88]  Come on.
[3629.50 --> 3630.92]  Like, okay, well, we have a good reason.
[3631.08 --> 3631.86]  Like there's...
[3631.86 --> 3636.98]  So I think also having a trusted person on that team, having a buddy while you onboard who
[3636.98 --> 3641.74]  you can pull aside and be like, have we talked about TypeScript before?
[3642.42 --> 3644.90]  And they're like, yeah, yeah, we have.
[3645.46 --> 3645.74]  Yeah.
[3647.04 --> 3647.36]  Definitely.
[3648.16 --> 3649.78]  Well, Thomas, thank you so much for coming on.
[3649.96 --> 3651.18]  We literally only got through...
[3651.18 --> 3651.66]  Thank you for having me on.
[3652.04 --> 3652.34]  Yeah.
[3652.36 --> 3652.84]  Thank you.
[3652.98 --> 3654.32]  We only got through half of your questions.
[3654.46 --> 3655.60]  So I guess that means we'll have to have you back.
[3655.60 --> 3656.90]  Some of them were just trolls.
[3657.24 --> 3660.46]  I mean, some of them are just impossible questions.
[3660.46 --> 3660.82]  And this is a problem.
[3660.96 --> 3661.22]  Why?
[3661.46 --> 3661.70]  Yeah.
[3662.08 --> 3662.38]  Yeah.
[3662.38 --> 3663.32]  That's true.
[3664.94 --> 3665.56]  That's true.
[3666.62 --> 3667.02]  Sweet.
[3667.02 --> 3667.66]  Yeah.
[3667.70 --> 3672.34]  Thank you so much for coming on and for being so active in our Slack.
[3672.66 --> 3674.40]  And please continue to do so.
[3674.90 --> 3677.14]  And yeah, we'd love to have you back sometime.
[3677.74 --> 3677.88]  Yeah.
[3677.88 --> 3682.36]  I encourage anyone listening who's not in that Slack to join because there's lots of good
[3682.36 --> 3685.12]  ideas floating around and you might get pulled on stage.
[3685.98 --> 3688.22]  It's just a great place to be and everyone's really nice.
[3688.62 --> 3688.98]  Let me try.
[3689.80 --> 3691.94]  And with that, we will catch you next week.
[3692.64 --> 3693.04]  See ya.
[3693.38 --> 3693.88]  See ya.
[3697.02 --> 3703.12]  Thanks for listening to Nick and K-Ball's Coffee Talk.
[3703.26 --> 3708.86]  On this show, we talk about coffee, New York, daughters, dogs, you know, no big whoop, just
[3708.86 --> 3709.64]  coffee talk.
[3709.92 --> 3714.90]  And shout out to Thomas for bringing some great questions to the discussion and some mighty
[3714.90 --> 3715.72]  fine answers too.
[3716.22 --> 3722.26]  If you want to be like Thomas, join the JS Party channel in ChangeLog's community right
[3722.26 --> 3722.50]  now.
[3722.88 --> 3723.84]  It's totally free.
[3723.84 --> 3727.56]  You can get in on it at changelog.com slash community.
[3728.12 --> 3733.20]  Thanks once again to our partners Fastly and Fly for helping us bring you awesome pods
[3733.20 --> 3734.46]  each and every week.
[3734.72 --> 3738.52]  Check them out at fastly.com and fly.io.
[3738.98 --> 3741.62]  And to our mysterious friend, Breakmaster Cylinder.
[3742.32 --> 3747.08]  JS Party's beats are banging because BMC bumps out banging beats for us.
[3747.56 --> 3749.68]  All we do is take those beats and...
[3749.68 --> 3750.40]  Paste it in there.
[3750.76 --> 3751.38]  What could go wrong?
[3751.84 --> 3757.18]  Next up on the pod, Nick, K-Ball, and Amelia would like to add you to their professional
[3757.18 --> 3758.30]  network on LinkedIn.
[3758.90 --> 3759.36]  Confused?
[3759.84 --> 3763.94]  It'll all make sense when we drop that episode into your podcast feed next week.
[3763.94 --> 3764.94]  Bye.
[3764.94 --> 3765.94]  Bye.
[3765.94 --> 3766.94]  Bye.
[3766.94 --> 3767.94]  Bye.
[3767.94 --> 3768.00]  Bye.
[3768.00 --> 3768.06]  Bye.
[3768.06 --> 3768.12]  Bye.
[3768.12 --> 3768.16]  Bye.
[3768.16 --> 3768.22]  Bye.
[3768.22 --> 3768.28]  Bye.
[3768.28 --> 3768.30]  Bye.
[3768.30 --> 3768.34]  Bye.
[3768.34 --> 3768.44]  Bye.
[3768.44 --> 3768.46]  Bye.
[3768.46 --> 3768.50]  Bye.
[3768.50 --> 3768.56]  Bye.
[3768.56 --> 3768.74]  Bye.
[3768.74 --> 3768.80]  Bye.
[3768.80 --> 3768.84]  Bye.
[3768.84 --> 3768.90]  Bye.
[3768.90 --> 3769.34]  Bye.
[3769.34 --> 3769.40]  Bye.
[3769.40 --> 3769.46]  Bye.
[3769.46 --> 3769.96]  Bye.
[3769.96 --> 3770.00]  Bye.
[3770.00 --> 3770.06]  Bye.
[3770.06 --> 3771.90]  Bye.
[3771.90 --> 3773.90]  Bye.
[3773.90 --> 3773.94]  Bye.
[3773.94 --> 3773.98]  Bye.
[3773.98 --> 3774.00]  Bye.
[3774.00 --> 3774.04]  Bye.
[3774.04 --> 3775.94]  Bye.
[3775.94 --> 3775.98]  Bye.
[3775.98 --> 3776.00]  Bye.
[3776.00 --> 3776.02]  Bye.
[3776.02 --> 3776.04]  Bye.

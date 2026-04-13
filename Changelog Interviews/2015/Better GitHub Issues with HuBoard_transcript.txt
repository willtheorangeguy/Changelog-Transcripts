[0.00 --> 10.90]  Welcome back, everybody.
[11.06 --> 13.84]  This is the Change Log, and I'm your host, Adam Stachowiak.
[13.96 --> 20.48]  This is episode 137, and today, Jared and I talk to Ryan Rau, the maker of Hubboard.
[21.02 --> 24.26]  Hubboard is a compound board for GitHub issues.
[24.26 --> 34.94]  Fun conversation today with Ryan about open source, licensing, taking contributions, building his business on top of somebody else's business, GitHub issues, their API.
[35.38 --> 36.54]  A lot of fun conversation.
[37.30 --> 43.26]  We have some awesome sponsors to mention for this show today, CodeShip, TopTile, and DigitalOcean.
[43.62 --> 52.10]  We'll tell you a bit more about TopTile and DigitalOcean later in the show, but our friends at CodeShip, big shout out to them because they just launched a brand new design.
[52.10 --> 53.34]  It looks beautiful, by the way.
[54.20 --> 57.44]  CodeShip is a hosted continuous deployment service that just works.
[57.94 --> 65.70]  You can easily set up continuous integration for your application in just a few steps and automatically deploy your code when all your tests pass.
[66.22 --> 70.88]  CodeShip has great support for lots of languages, test frameworks, as well as notification services.
[70.88 --> 81.22]  They easily integrate with GitHub or Bitbucket and can deploy your code to cloud services like Heroku, AWS, Nojitsu, Google App Engine, or even your own servers.
[81.76 --> 85.62]  Setup takes just three minutes, so you can get started today with their free plan.
[85.76 --> 92.90]  And make sure you use the code, TheChangelogPodcast, to get a 20% discount for three months on any plan you choose.
[93.00 --> 94.88]  Again, that code is TheChangelogPodcast.
[96.70 --> 97.64]  Make sure you use that code.
[97.64 --> 102.88]  Head to CodeShip.com slash TheChangelog, tell them you sent you, and now on to the show.
[106.18 --> 107.06]  What's up, everybody?
[107.20 --> 107.92]  We are back.
[108.06 --> 109.70]  This is Jared with TheChangelog.
[109.80 --> 111.18]  Got Adam Stack in the house.
[111.30 --> 111.86]  Adam, what's up?
[112.32 --> 113.06]  Adam Stack.
[113.18 --> 113.98]  Yes, that's me.
[114.14 --> 114.48]  Woo-hoo!
[115.20 --> 119.70]  And we are joined today by Ryan Rau with Hubord.com.
[120.26 --> 122.78]  Ryan's a guy we met down at Keep Ruby Weird in the fall.
[122.78 --> 128.04]  I enjoyed talking to him, and we're interested in what he was up to with this open source product.
[128.28 --> 129.04]  Ryan, how you doing?
[130.14 --> 130.70]  I'm doing well.
[130.80 --> 131.62]  Thanks for having me, guys.
[131.70 --> 132.98]  Austin, Texas, man.
[133.74 --> 134.68]  ATX in the house.
[134.88 --> 135.12]  ATX.
[135.16 --> 136.48]  But you're not from ATX.
[137.18 --> 137.56]  Oh, no.
[138.48 --> 139.10]  I was-
[139.10 --> 139.58]  Cornfields.
[140.06 --> 140.34]  Yeah.
[140.74 --> 143.68]  I'm originally from Northeast Iowa.
[143.76 --> 144.08]  Northeast.
[145.16 --> 147.00]  Teeny, tiny town called Cresco.
[147.00 --> 147.28]  Okay.
[147.50 --> 147.66]  Yeah.
[148.92 --> 152.74]  My hometown butts up to the Iowegians.
[154.00 --> 154.36]  Iowegians.
[154.38 --> 155.28]  But that's on the west side.
[155.32 --> 156.18]  On the west side of Iowa.
[156.30 --> 157.22]  I've never heard that before.
[157.50 --> 157.90]  Iowegians.
[158.10 --> 160.22]  You're from the great state of Nebraska?
[160.54 --> 160.84]  That's right.
[161.56 --> 161.96]  Omaha.
[162.98 --> 166.36]  But I've drove through there a few times.
[166.82 --> 170.00]  It's pretty fun to go 95 plus on I-70.
[170.00 --> 174.22]  Yeah, not much to see, but you can definitely drive fast because there aren't too many folks
[174.22 --> 174.70]  around either.
[175.78 --> 176.06]  Right.
[176.06 --> 178.72]  So, Ryan, tell us about Hubboard.
[180.48 --> 181.78]  So, what is Hubboard?
[181.92 --> 183.02]  What does it do?
[184.32 --> 189.20]  You know, I get asked this all the time and I keep trying to refine it.
[190.32 --> 194.56]  When I first launched it, it was GitHub issues made awesome.
[195.62 --> 201.10]  But I've been trying to better describe it as it's really like a project management solution
[201.10 --> 204.86]  for teams and or GitHub organizations.
[204.86 --> 211.90]  The reason I say that is because we don't really just deal with GitHub issues anymore.
[212.40 --> 217.96]  We've added some features around linking repos together so you can have this holistic view
[217.96 --> 222.42]  of your entire project.
[222.42 --> 231.20]  So, you can link repos together and you can also manage milestones across multiple repos,
[231.68 --> 236.92]  which was kind of a challenge to implement as well.
[236.92 --> 239.14]  So, it's kind of broadened in scope over time.
[239.14 --> 243.78]  But when you first kicked it off, it was you were using GitHub issues.
[244.26 --> 250.62]  You thought they were lacking this project management visual Kanban thing.
[251.38 --> 252.76]  And you decided to build it.
[252.84 --> 254.46]  Were you just scratching your own inch back in the day?
[254.46 --> 263.34]  I guess it was really born out of a need or maybe even like a hatred of other tools that
[263.34 --> 264.32]  I've used in the past.
[265.32 --> 266.38]  You want to name any names?
[267.58 --> 273.44]  I don't think the great hatred tool needs to be mentioned.
[273.70 --> 275.36]  More like the vaults more.
[275.50 --> 275.80]  Yes.
[275.92 --> 277.10]  The tool that will not be named.
[277.10 --> 280.32]  Everybody's used the tool that will not be named.
[280.92 --> 285.76]  And although I'll just come out and say it's usually JIRA, right?
[286.24 --> 290.64]  And I think it's a fantastic tool for businesses.
[291.04 --> 296.30]  It's so configurable almost to a fault, right?
[296.78 --> 297.02]  Yes.
[297.58 --> 306.22]  You can put so many rules dictating the flow of your issues with that tool that sometimes
[306.22 --> 307.50]  it gets cumbersome to use.
[308.04 --> 315.34]  What really made Hubbard come about was a little over three years ago, I came to Austin to work
[315.34 --> 316.22]  for a company.
[317.18 --> 324.28]  And we were building a really complex, as far as business rules and requirements, enterprise
[324.28 --> 329.88]  application for large enterprise HR needs.
[329.88 --> 337.72]  And so there was a lot of rules around who could see what data and things of that nature.
[338.20 --> 345.90]  We really had this fine-grained requirement to lock down security down to the field level
[345.90 --> 353.28]  of like Sally Sue can't see the salary of X person if they're not in this certain role.
[353.28 --> 360.50]  And so to fit that bill, we actually ended up building a web framework and we decided to
[360.50 --> 367.50]  open source it to try to like kind of get a groundswell or like a force multiplier of productivity.
[367.50 --> 374.80]  And so we, of course, hosted that on GitHub and that framework was called Fubu MVC.
[375.24 --> 382.32]  So sort of as open source developers on GitHub, you know, we were in GitHub, love GitHub.
[383.10 --> 386.76]  We ended up choosing it for the business side of things as well.
[387.66 --> 393.84]  And so when you're, rather than using multiple tools, we kind of settled upon GitHub issues
[393.84 --> 395.94]  for the product side of things, right?
[396.78 --> 403.54]  And what we kind of found was, you know, the simplicity of it is fantastic for an open source project,
[403.54 --> 409.36]  but it has some shortcomings as far as like communicating to a business
[409.36 --> 415.62]  and prioritizing a business's needs, you know, versus an open source like project.
[416.54 --> 420.38]  GitHub issues is fantastic, but it doesn't really have any prioritization
[420.38 --> 428.76]  or any sense of where things are, whether they're in progress or, you know, in review.
[429.28 --> 432.46]  I don't know if you guys have ever personally tried to use GitHub.
[433.38 --> 433.86]  Yes.
[434.02 --> 436.24]  Like issues to manage a project.
[436.42 --> 445.90]  We've gone off and on using that between, we use Trello now, but we mainly don't use GitHub issues
[445.90 --> 451.36]  because we use Trello and we have business sides of the house that need to sort of play a part
[451.36 --> 455.44]  in moving cards around and seeing the state of things and commenting and coordinating and stuff.
[455.60 --> 461.76]  So Trello is fit for us, but we did try GitHub issues way back in the day, and it was label hell.
[461.94 --> 463.96]  It was, you know, the same thing you're talking about.
[464.00 --> 467.14]  You couldn't really tell where something was at in the process.
[467.14 --> 473.34]  So, and that's what we liked about Trello, which was this sort of Kanban approach to how you can do things.
[473.34 --> 476.54]  Right, and Trello's fantastic too, right?
[476.70 --> 484.40]  Like it's extremely simple, and for non-technical stakeholders, it's a lot easier to say,
[484.56 --> 492.20]  oh, hey, here's this tool, and it really only is around like issue management or like project planning
[492.20 --> 498.04]  rather than trying to get a non-stakeholder to be like, oh, hey, you have, okay,
[498.14 --> 501.16]  so we use this thing called GitHub, and you have to explain what GitHub is.
[501.16 --> 504.74]  And then you have to like, they have to go create an account in it.
[505.10 --> 507.86]  And they're like, well, why do I need this account just to manage issues?
[508.42 --> 509.44]  Yeah, very confusing.
[510.44 --> 511.30]  So there's definitely some short...
[511.30 --> 515.20]  We have that with documentation too, because we have wikis and some documentation in our repos,
[515.30 --> 519.14]  and it's just like, unless you're a developer on the development team, you don't see that stuff,
[519.24 --> 522.02]  and it's, or they do, they just forget they have a GitHub account,
[522.12 --> 523.28]  and they don't know how to log in.
[523.38 --> 526.06]  It's just like, it's totally foreign to them.
[526.06 --> 533.32]  Right. And so, you know, back to being at this company, we ran into all these problems, right?
[533.34 --> 536.18]  Because we didn't want to like use different tools.
[536.32 --> 541.10]  And at this point, we have, you know, hundreds of open issues, you know, a lot of them like
[541.10 --> 542.90]  two to three years old in GitHub.
[543.52 --> 547.76]  And, you know, we started like making duplicates of old issues.
[547.76 --> 552.24]  So it just became like a bit of a nightmare to manage.
[552.56 --> 558.92]  And so we started playing around with the API and trying to find solutions as to like,
[559.42 --> 563.10]  how maybe we could better organize them, right?
[563.20 --> 567.54]  And so we came up with this tool called, at the time, I think we called it Hookshot.
[568.30 --> 573.22]  And so what we did is we subscribed to the issue webhook, right?
[573.22 --> 579.20]  And so anytime an issue was closed, if it didn't have this reviewed label,
[579.54 --> 588.44]  we would basically reopen it and add a needs review label to it and assign it to our QA engineer.
[589.38 --> 592.00]  And so for a while, that really worked.
[592.18 --> 597.06]  So, you know, we would basically create an issue in GitHub,
[597.32 --> 600.16]  and then we would use the linking part.
[600.16 --> 606.00]  It's a feature in GitHub where if you reference an issue number in a commit message,
[606.50 --> 612.12]  it will actually link that SHA and that commit in the discussion history of a GitHub issue.
[612.64 --> 614.08]  With a timestamp and stuff.
[614.62 --> 615.70]  With a timestamp.
[616.02 --> 618.54]  And you could like click on it and go,
[618.54 --> 625.92]  and you can like actually make inline comments on like a certain line of the commit.
[625.92 --> 631.30]  And those actually come through into the GitHub issue discussion.
[631.68 --> 639.82]  And they actually have some really fantastic features around like really integrating it in with your code, right?
[640.48 --> 647.46]  And so that really helped like our testing and QA engineers see like they could go to the,
[648.00 --> 651.68]  so they would get tagged with needs review, right?
[651.68 --> 654.48]  And they would get it assigned to them and they'd look at it and be like,
[654.60 --> 659.46]  and they would be able to easily reference back into the code, like what actually changed.
[659.90 --> 662.66]  And so we like really fell in love with that functionality.
[662.92 --> 666.82]  And when we hit some of these shortcomings of GitHub,
[667.12 --> 670.32]  as far as like communicating the business, what we were doing, right?
[670.58 --> 672.48]  Because we're programming, right?
[672.52 --> 674.58]  We're like, we're busting out features.
[674.78 --> 675.84]  We're being productive.
[675.84 --> 679.92]  But, you know, some of the stakeholders didn't really see that.
[680.06 --> 684.86]  They didn't really understand how to extract that value out of GitHub, right?
[684.96 --> 687.08]  Because they just, they didn't really see it.
[687.22 --> 689.26]  Like you can't see the progress.
[690.08 --> 693.00]  And so we didn't want to lose that code linking,
[693.50 --> 698.84]  but we saw this need for like visibility to the business.
[698.84 --> 703.58]  So we started looking at tools like Trello, like Pivotal Tracker, like Jira.
[704.56 --> 706.76]  And I came up with a crazy idea.
[706.88 --> 711.32]  I was like, well, what if we, you know, what if we had this conventional label, right?
[711.76 --> 713.16]  Almost like a Kanban board.
[713.26 --> 717.78]  Like we could just name a label like with a certain pattern.
[717.78 --> 722.20]  And then I could use the API to pull all those labels and then turn those into columns.
[722.20 --> 726.90]  And if you drug one issue from another one, I just remove that label and add the other one, right?
[726.90 --> 732.74]  And so, you know, I just spent a weekend or two hacking on it.
[733.08 --> 738.12]  And that was what birthed the first version of what eventually became Whoboard.
[738.98 --> 741.88]  And at that time I called it Inch Pebbles.
[742.18 --> 742.84]  Inch Pebbles?
[743.94 --> 744.50]  Yes.
[744.62 --> 746.20]  It was a playoff of milestones.
[746.54 --> 746.84]  Okay.
[747.02 --> 747.74]  Ah, Inch Pebbles.
[747.74 --> 749.72]  Like milestone, Inch Pebble.
[749.86 --> 750.40]  Got it.
[750.78 --> 751.20]  Got it.
[751.32 --> 751.98]  So clever.
[752.86 --> 754.08]  Yeah, very clever, right?
[754.08 --> 756.88]  And so Inch Pebbles was born.
[757.14 --> 760.46]  It was hosted on a free dino on Heroku, right?
[760.98 --> 762.10]  I'm a .NET developer.
[762.34 --> 763.40]  I don't know any Ruby.
[763.66 --> 767.76]  So I write it in Ruby because, you know, Heroku was like free.
[768.38 --> 770.16]  And I kind of wanted to learn Ruby.
[770.80 --> 773.18]  So it was just kind of like this side project.
[773.18 --> 774.26]  This is 2011, right?
[774.92 --> 776.00]  Yeah, it's 2011.
[776.86 --> 778.54]  So it's just like the side project.
[778.54 --> 779.82]  It's running on a free dino.
[779.82 --> 784.84]  It really only like had, you couldn't create issues or anything.
[785.04 --> 789.62]  It was effectively like you could navigate to this page that had the same URL structure
[789.62 --> 790.06]  as GitHub.
[790.24 --> 794.68]  And you would see this Kanban board just magically appear as long as you had these
[794.68 --> 797.14]  specially named labels.
[797.14 --> 802.92]  And we could drag them, like basically say, hey, here, business.
[803.68 --> 809.86]  Here's this Kanban board that can just show you this like read view of what we're doing.
[810.10 --> 815.14]  So it sounds like you could still use issues as normal with a dev team.
[815.70 --> 821.00]  But hand them, Hue board, the business team, Hue board, and just especially names and labels.
[821.12 --> 823.38]  Is that what you're talking about at this point?
[823.38 --> 823.42]  Right.
[824.48 --> 827.88]  Where you still had issues and it's still worth the way issues works, but you can use this
[827.88 --> 828.34]  in tandem.
[829.14 --> 829.54]  Right.
[829.60 --> 833.90]  It was really, it's really just a different view on top of GitHub issues.
[834.18 --> 836.00]  Like there's no separate data model.
[836.36 --> 840.80]  Like it would pull the issues from the API and create cards from each issue.
[841.16 --> 843.50]  And it would look at the labels on the issue.
[843.66 --> 847.86]  And if it had one of these conventional labels on it, it would then be in that column.
[847.96 --> 849.84]  It would just be represented in that column, right?
[849.84 --> 856.48]  And it just had a really simple like if like a like jQuery draggable, like, oh, if you drag
[856.48 --> 861.50]  it over here, then it just made an API call that removed X label and added the other one.
[861.50 --> 861.74]  Right.
[861.82 --> 863.14]  That represented the new column.
[864.90 --> 869.00]  And so it just was born out of pure need and pure simplicity.
[869.36 --> 869.64]  Right.
[870.36 --> 874.08]  I started showing people that I knew I'd be like, oh, yeah, I made this cool thing.
[874.16 --> 874.78]  Check this out.
[874.82 --> 875.98]  And like I would just show it to people.
[875.98 --> 878.30]  And they're like, yeah, that's that's cool.
[878.44 --> 881.12]  Like we would we would kind of be interested in using that.
[881.62 --> 887.58]  So I was convinced to like show the world, like reveal it, like let let people use it.
[887.88 --> 892.26]  So I go shopping for the domain name inch pebbles and it's taken.
[892.96 --> 893.00]  What?
[893.24 --> 896.30]  It's like, yeah, it's like parked by this blog.
[896.62 --> 897.00]  Man.
[897.04 --> 901.56]  So I just didn't want to I didn't want to go through the hassle of trying to get that name
[901.56 --> 904.42]  from whoever, you know, randomly had it.
[904.42 --> 905.74]  Somebody else thought of inch pebbles.
[906.76 --> 907.84]  That's what I'm impressed.
[908.16 --> 908.40]  I guess.
[908.60 --> 909.02]  I don't know.
[909.22 --> 916.46]  And the tagline of this this blog is like dealings dealing with life's milestones or something.
[916.86 --> 920.16]  I mean, like it even had the same word exact play.
[920.52 --> 921.68]  It's so great.
[921.68 --> 928.36]  So then we started, you know, brainstorming on names and it was like, you know, things
[928.36 --> 934.20]  were thrown around like octo cards, octo board, you know, kind of playing off the octo cat
[934.20 --> 934.64]  thing.
[934.64 --> 939.18]  But then that didn't really have anything to do with like a board or I don't know.
[939.42 --> 943.10]  So somebody just threw out like what have what about hub board, right?
[943.16 --> 946.34]  Like the play on the play on words from hubot.
[946.56 --> 946.62]  Yeah.
[946.62 --> 954.32]  And so it had some like it kind of had like a backwards tie in back to GitHub.
[954.32 --> 961.12]  But it really kind of gave us the, you know, gave me the freedom to sort of be unique in
[961.12 --> 962.56]  a way or claim that I wasn't.
[962.56 --> 967.56]  So like if you ever wanted to like use it or like build an adapter for a different issue
[968.12 --> 973.16]  tracker, maybe, you know, the word would or the name would still be relevant.
[973.44 --> 973.64]  Yeah.
[974.44 --> 976.26]  So, yeah, Hubboard was born.
[976.26 --> 979.60]  Jared and I were saying we thought it was hub board.
[980.66 --> 981.46]  Hub board.
[982.08 --> 982.42]  I don't know.
[982.60 --> 983.00]  Too many.
[983.28 --> 983.56]  I don't know.
[984.42 --> 985.68]  There's not two B's.
[986.10 --> 986.40]  I don't know.
[986.56 --> 988.40]  You know, it was just I was lost.
[989.16 --> 991.14]  You know, as you guys, you probably know this, right?
[991.14 --> 994.30]  And as developers, you know, we spend most of our time reading words on the Internet.
[994.80 --> 995.04]  Yeah.
[995.14 --> 997.46]  And we don't ever have to say those words out loud to anybody.
[997.70 --> 1002.16]  And so we all come up with our own like just rendering of what that actually sounds like.
[1002.16 --> 1006.74]  And then we get together with other developers and we finally use that word and they give
[1006.74 --> 1009.24]  us this stare like, man, what are you talking about?
[1009.72 --> 1013.82]  And you just realize that like my my version of that word is just like completely does not
[1013.82 --> 1014.58]  line up with reality.
[1014.88 --> 1017.50]  It's like OzCon or OSCon.
[1017.60 --> 1017.78]  Yeah.
[1018.52 --> 1019.44]  Or Imgur.
[1019.44 --> 1019.48]  Imgur.
[1020.12 --> 1021.30]  I don't even know what that is.
[1021.64 --> 1021.84]  See?
[1022.72 --> 1023.08]  Yeah.
[1023.22 --> 1024.64]  You never go on Imgur.
[1025.20 --> 1025.96]  Yeah, exactly.
[1026.16 --> 1026.74]  M-I-G-U-R.
[1026.74 --> 1027.28]  Oh, no, I know Imgur.
[1027.38 --> 1027.58]  Yeah.
[1028.18 --> 1028.36]  Yeah.
[1028.44 --> 1029.36]  Exactly like that.
[1029.96 --> 1030.08]  Yeah.
[1030.18 --> 1030.90]  No, it's Imgur.
[1031.12 --> 1031.82]  Definitely Imgur.
[1032.04 --> 1032.40]  Imgur.
[1034.52 --> 1039.58]  So you mentioned, you know, switching out, you know, the possibility because the name
[1039.58 --> 1044.04]  is a little bit distinct that you could have a separate back end, which makes me think
[1044.04 --> 1049.28]  of one concern that I had, you know, hearing about it is like, you know, because you're
[1049.28 --> 1053.06]  building a business, you've built a business around Hubord and you've, we'll talk about,
[1053.18 --> 1056.44]  you know, kind of some of the challenges and things that happen around this business around
[1056.44 --> 1057.34]  open source product.
[1057.34 --> 1065.08]  But were you scared to, obviously not scared enough, but did it bother you or that you're
[1065.08 --> 1067.52]  building a product on top of somebody else's product?
[1069.38 --> 1074.58]  At first, you know, I really didn't, I guess I didn't have, when I set out to build it,
[1074.62 --> 1079.12]  I didn't particularly have the intention of turning it into a business, right?
[1079.12 --> 1086.06]  So my concerns around not having the stickiness of the tool, I like to call it stickiness,
[1086.18 --> 1086.36]  right?
[1086.82 --> 1088.76]  Like, I don't own the data model.
[1089.32 --> 1093.90]  It literally all, all that controls Hubord is still in GitHub, right?
[1094.68 --> 1100.78]  Hubord is not the single source of truth at all for what represents the state of the board.
[1101.10 --> 1105.30]  So there's really not much stickiness in the tool.
[1105.30 --> 1114.92]  Like, it's really easy to use it, try it out, even use it for a while, and then maybe
[1114.92 --> 1116.86]  you outgrow it and you can go to something else.
[1116.92 --> 1119.80]  There's nothing keeping you using the tool, right?
[1119.94 --> 1123.68]  That's a blessing and a curse, though, because you also have, it's really easy to try it out,
[1123.90 --> 1124.04]  too.
[1124.24 --> 1124.48]  Right.
[1124.62 --> 1125.34]  So there's your blessing.
[1125.46 --> 1127.52]  The curse is it's also really easy to just ditch it.
[1128.18 --> 1128.96]  Just to ditch it.
[1128.96 --> 1134.30]  So being that I didn't set out with the intention of turning it into a business, I didn't really
[1134.30 --> 1135.96]  care that it wasn't sticky, right?
[1136.30 --> 1142.78]  And also, it was kind of a thought experiment or even just like a challenge, kind of like
[1142.78 --> 1150.04]  a, like it was, it was fun to try to see how far you could stretch using an API and not
[1150.04 --> 1152.42]  have a database whatsoever, right?
[1153.08 --> 1154.46]  Like Hubord existed.
[1154.46 --> 1161.54]  And I kept adding features like linking repos together, custom ordering of like keeping
[1161.54 --> 1166.26]  the order of where cards were, flipping the board on its side on like milestones where the
[1166.26 --> 1171.90]  columns were milestones, being able to order milestones as in like a custom order instead
[1171.90 --> 1172.66]  of the due date.
[1173.94 --> 1177.68]  All these things I was able to do for free.
[1177.88 --> 1179.54]  Like I didn't have a database.
[1179.54 --> 1181.72]  Like it cost me nothing to host it.
[1181.94 --> 1187.92]  It, it pretty much lived on a free Heroku dino for like over two years.
[1188.06 --> 1193.42]  I think, I think at its peak when, when I wasn't charging any money, it was somewhere
[1193.42 --> 1197.16]  around like, and again, like I didn't have intention to make it a business.
[1197.36 --> 1201.32]  So I didn't even really have any metrics on like how many users there were.
[1201.32 --> 1201.74]  Right.
[1201.74 --> 1208.62]  The only metric I had to go by was like GitHub has this thing when you create an application,
[1208.94 --> 1215.70]  they'll show you how many keys your, your OAuth application has authorized.
[1216.62 --> 1219.76]  And so at the time it was like somewhere around 6,000 or something.
[1220.02 --> 1220.20]  Right.
[1220.78 --> 1224.74]  I don't know how, you know, I've never spent a dollar on marketing or anything, but somehow
[1224.74 --> 1229.84]  like it just groundswelled into like, like all this interest in people using it and it didn't
[1229.84 --> 1230.88]  cost me anything to host.
[1231.02 --> 1236.68]  So I was like, okay, la-di-da, you know, like I just kept trying to, trying to stretch it,
[1236.76 --> 1239.98]  trying to stretch it, see how far I could take it without having a database.
[1241.16 --> 1247.08]  And then when the, when the time came to where like, it kind of got so big that, that other
[1247.08 --> 1251.92]  companies saw it as like an opportunity to make money, I had a decision to make.
[1251.92 --> 1252.14]  Right.
[1252.18 --> 1254.20]  It was like, let, let my experiment die.
[1254.20 --> 1260.02]  Like let the thing I build, built die to people who were like turning it into a business or
[1260.02 --> 1261.38]  turn it into a business myself.
[1261.54 --> 1261.94]  Right.
[1262.60 --> 1262.86]  All right.
[1262.86 --> 1264.04]  Let's pause the show for a minute.
[1264.12 --> 1265.12]  Give a shout out to a sponsor.
[1265.22 --> 1266.36]  I want to talk to you about TopTile.
[1266.44 --> 1270.44]  We've been working with them for the last year and it's just been a great time working
[1270.44 --> 1270.94]  with them.
[1271.06 --> 1275.74]  We thought it would make some sense to circle back and talk to some of our listeners who've
[1275.74 --> 1281.46]  applied with TopTile and have been accepted because only about two to 3% of the engineers
[1281.46 --> 1285.16]  who apply, make it past their strict elite engineer process.
[1285.60 --> 1290.64]  And that person is Daniel Lausanne, a long time fan and listener of the change log.
[1291.06 --> 1294.46]  He is now living the dream as an elite engineer at TopTile.
[1294.68 --> 1300.46]  And I say living the dream because he's now able to have 100% control of the types of projects
[1300.46 --> 1303.98]  and technologies he's working on, as well as the rate he wants to charge.
[1304.42 --> 1308.10]  Daniel earns 100% of his income as a TopTile engineer.
[1308.10 --> 1313.56]  And he wanted me to pass on his seal of approval, so to speak, of the TopTile experience.
[1313.66 --> 1318.02]  And for those of you out there who are freelancing or would like to test out freelancing or even
[1318.02 --> 1322.12]  try out a no-risk freelance-like project while you maintain your full-time position,
[1322.42 --> 1323.66]  you've got to check out TopTile.
[1323.84 --> 1327.76]  If you think you have what it takes, head to TopTile.com to get started.
[1328.12 --> 1329.38]  Tell them the change log sent you.
[1329.78 --> 1330.70]  And now back to the show.
[1330.70 --> 1338.98]  And you had some real competition come in and offer a very similar product.
[1339.14 --> 1340.36]  Is that fair to say?
[1341.16 --> 1346.96]  There's a couple of competitors that come into the space, and some of them are really, really similar
[1346.96 --> 1349.72]  as far as almost clones.
[1350.24 --> 1350.92]  Like fork your repo?
[1350.92 --> 1355.34]  I don't think anyone's forked the repo, per se.
[1356.02 --> 1362.40]  But they definitely were largely inspired by Hubboard, right?
[1362.94 --> 1363.84]  And that's not bad.
[1363.96 --> 1365.56]  Like competition is good, right?
[1365.80 --> 1368.94]  It convinced me that it was a viable thing.
[1369.22 --> 1376.32]  It inspired me to take it seriously and take it to the next level and build in things like
[1376.32 --> 1378.54]  SSL support and stuff like that.
[1378.54 --> 1384.00]  But at the same time, if I could do it all over again, it sure would be nice to have
[1384.00 --> 1387.92]  some inkling of stickiness to the tool, right?
[1388.50 --> 1391.10]  But at the same time, it's okay.
[1392.10 --> 1397.30]  It still gets a lot of interest, and a lot of people use it and like it.
[1398.58 --> 1404.30]  I guess it's a challenge to keep the tool compelling and good enough that people stick around,
[1404.44 --> 1406.08]  even though there's really no reason to.
[1407.88 --> 1408.24]  Yeah.
[1408.54 --> 1410.26]  Yeah, I think that's a testimonial for the tool.
[1410.38 --> 1416.20]  It's awesome you got there with no marketing, too, to have that many OAuth keys and use.
[1417.38 --> 1423.86]  I'm looking at our notes, and I've got a note here that April 19, 2012, was when you said
[1423.86 --> 1428.78]  somehow on Twitter, somehow Hubboard grows to 400 users.
[1429.02 --> 1430.60]  Is that the 6,000?
[1430.68 --> 1432.80]  Is that post that or before that?
[1434.20 --> 1434.44]  Before?
[1434.44 --> 1436.22]  You know, I don't remember.
[1436.22 --> 1437.94]  I was preparing for the show.
[1438.04 --> 1444.70]  I was trying to go back in my Twitter history and figure out how big it was at certain points,
[1444.78 --> 1444.96]  right?
[1445.00 --> 1447.30]  And that was just a random tweet that I came across, right?
[1447.30 --> 1451.08]  So Hubboard.com really kind of launched.
[1451.08 --> 1454.08]  I wouldn't say it actually launched, right?
[1454.08 --> 1460.54]  Like, I told people about it on my personal blog in January of 2012.
[1460.54 --> 1465.24]  And by April, four months later, there was already 400 people, like, using it.
[1465.94 --> 1473.34]  By the time, like, I got to the 6,000 mark was when I really took it to, like, actually
[1473.34 --> 1480.04]  formed a business out of it and launched it out of Free for Everyone, you know, over a
[1480.04 --> 1483.36]  year later, somewhere in, like, October of 2013.
[1483.36 --> 1486.50]  So when I actually, like...
[1486.50 --> 1487.84]  So when Hubboarding came into play.
[1488.56 --> 1488.80]  Right.
[1489.02 --> 1495.68]  So when I formed, like, an LLC to actually charge money to people, it was over a year,
[1495.80 --> 1496.54]  you know, later.
[1497.06 --> 1497.16]  Yeah.
[1497.28 --> 1503.30]  And it had still, it had grown up to, like, that many, like, user keys that had been authorized.
[1503.76 --> 1504.14]  That's not...
[1504.14 --> 1509.90]  That's probably not, like, a fair metric as to how many people were actually using it, right?
[1509.90 --> 1513.48]  Like, because some people would maybe, like, check it out, and then, you know, you tick
[1513.48 --> 1513.94]  the number.
[1515.06 --> 1518.24]  But it was pretty, it was still pretty impressive for me.
[1518.50 --> 1522.72]  Like, you know, you just keep getting into those, like, 10-based milestones.
[1523.20 --> 1524.26]  Like, woo, 1,000.
[1524.50 --> 1525.30]  Woo, 400.
[1525.54 --> 1528.54]  You know, like, every 100, I would kind of be pumped up.
[1529.84 --> 1533.42]  So you had all these, you had all these free users, and there was all this interest and
[1533.42 --> 1534.80]  buzz despite no marketing.
[1534.80 --> 1540.28]  Then competitors come in, and they start to offer your product or a very similar product
[1540.28 --> 1542.02]  to yours for pay.
[1542.44 --> 1545.36]  And so you decide at this point, I'm not going to resign.
[1545.54 --> 1547.30]  I'm going to man up and turn it into a company.
[1548.02 --> 1550.40]  And you relaunch as a business, paid accounts.
[1551.02 --> 1553.44]  Did the people just, you know, fork over their money immediately?
[1553.86 --> 1558.44]  Or was there still a moment in there where after you had turned it into a company and
[1558.44 --> 1562.30]  decided you're going to start accepting money where, you know, you had all the free users,
[1562.30 --> 1567.04]  but nobody was interested in paying, or did they just sign up right away?
[1568.48 --> 1570.40]  Yeah, so that was an interesting thing.
[1571.06 --> 1573.18]  You know, it was foreign territory to me.
[1573.74 --> 1581.42]  When you take a thing from free to for pay, you know, out of the blue, a lot of people go
[1581.42 --> 1585.08]  the route of grandfathering in, you know, the people that are already using it.
[1585.08 --> 1591.36]  And I didn't do that maybe out of laziness or maybe out of like urgency to put it out
[1591.36 --> 1591.58]  there.
[1591.98 --> 1598.26]  So when I launched it, I launched it with anyone who signed up within the first year
[1598.26 --> 1599.78]  got a six month trial.
[1600.54 --> 1606.74]  I basically kind of I saw that as a way like, hey, I'm sorry, like, I kind of got I got to
[1606.74 --> 1608.36]  turn this into like something real.
[1608.36 --> 1610.68]  I understand you're using it for free.
[1611.54 --> 1615.98]  If you sign up, like I'm not charging anyone, you know, if you sign up before November 1,
[1616.20 --> 1621.94]  you get 180 days free trial, right, which is like, a really long time.
[1623.26 --> 1629.10]  And there was maybe 1000, like after you do some analytics and like, and slicing and dicing
[1629.10 --> 1633.50]  of who's using it, there's maybe like 1000 potential like paying customers at that point.
[1633.50 --> 1639.76]  And I, I was just kind of okay with the fact that I wasn't going to convert all of them.
[1639.76 --> 1640.30]  Right.
[1641.06 --> 1646.00]  And that's in fact, what happened, like, it ended up being that I didn't, I didn't convert
[1646.00 --> 1650.48]  everyone, I lost a large majority of those people, sort of sort of like starting from
[1650.48 --> 1650.86]  scratch.
[1651.72 --> 1657.98]  And but like, I guess any SaaS business, it's kind of like that.
[1657.98 --> 1664.64]  It's, it's a slow linear growth until you hit that thing that makes you like, do that
[1664.64 --> 1667.58]  exponential bell curve, and then like, everybody uses it.
[1670.14 --> 1673.24]  And, you know, it's been over a little over a year now.
[1673.82 --> 1680.38]  And we've hit, you know, being fully bootstrapped with zero outside funding, you know, we've been
[1680.38 --> 1687.02]  able to, I have hired my first full time employee, which is absolutely nuts about a year later.
[1687.02 --> 1694.34]  All, you know, just kind of bootstrapping it, staying profitable, staying soluble the entire
[1694.34 --> 1694.80]  time.
[1694.94 --> 1695.86]  Well, congrats.
[1696.06 --> 1697.20]  Congrats on that for sure.
[1697.82 --> 1698.08]  Yeah.
[1698.64 --> 1702.34]  You know, for those who don't know, this, this is completely open source.
[1702.70 --> 1708.42]  So if you wanted to check out Hubord, you could just go to github.com slash rowerion slash
[1708.42 --> 1713.64]  Hubord, which is always admirable and interesting when we see people building open source products
[1713.64 --> 1716.12]  and then also turning those into businesses that are successful.
[1716.12 --> 1722.68]  I think the stigma is that, you know, that won't work because people will just, will just
[1722.68 --> 1724.64]  clone it or run it themselves.
[1724.80 --> 1727.86]  I mean, your audience is developers in a large part.
[1728.30 --> 1731.98]  I guess we can talk about your growing customer base and how it's turning more enterprise next.
[1732.18 --> 1735.64]  But first I want to ask you about the open sourcing of it.
[1735.96 --> 1738.12]  I'm sure it was probably open source from the beginning.
[1738.40 --> 1739.56]  Is that fair to say?
[1739.96 --> 1742.96]  It's been open source from day one or did you open source it at a certain point?
[1742.96 --> 1746.40]  It was like just open source from day one, right?
[1746.52 --> 1750.82]  Like I just, I just, I just threw it out there.
[1751.06 --> 1756.28]  Like, Hey, here's this, here's this random cool thing that I built, you know, for fun.
[1756.92 --> 1758.96]  I open sourced it from day one.
[1758.96 --> 1764.72]  Um, I made it MIT just out of like, I guess, randomness.
[1764.86 --> 1765.92]  Like, Oh, I'll just pick that one.
[1765.98 --> 1766.72]  That one sounds good.
[1767.60 --> 1768.46]  And, uh,
[1768.46 --> 1769.96]  Contributor license agreement too.
[1770.08 --> 1771.36]  How does that differ from the MIT?
[1771.36 --> 1774.82]  So I actually added that later.
[1775.18 --> 1778.74]  I added that after I turned it into a business.
[1779.12 --> 1786.04]  Um, and that was more because when it turned into a business, I did, you know, it's just
[1786.04 --> 1786.82]  out of ignorance.
[1786.82 --> 1790.94]  I had no idea like, well, what if somebody does fork it?
[1791.00 --> 1791.72]  It is MIT.
[1791.96 --> 1799.66]  So someone could, someone could host it and, uh, make zero changes and charge money for it.
[1799.66 --> 1804.42]  That is, that is completely within legal realm and you can do it and that's fine.
[1805.00 --> 1807.32]  Uh, MIT does not stop you from doing that.
[1807.50 --> 1817.10]  So when I launched it, I was contemplating, uh, changing the license to a GPL, which would
[1817.10 --> 1822.94]  kind of prevent people from doing that in a way hosting it and then gaining money from
[1822.94 --> 1823.12]  it.
[1823.12 --> 1824.78]  But then I actually never did that.
[1824.90 --> 1829.10]  I just left it like at the end of the day, like no one.
[1829.66 --> 1830.08]  Did it.
[1830.32 --> 1833.94]  No one forked it and just tried to make money on it.
[1833.94 --> 1839.24]  And I'm not the only, like Hubbard is not the only company out there that has, that has
[1839.24 --> 1846.82]  figured out kind of a way to charge money or, or, or at least sort of make a living off
[1846.82 --> 1848.32]  of their open source contributions.
[1848.32 --> 1850.66]  I mean, Docker's doing it.
[1850.86 --> 1852.12]  Vagrant's doing it.
[1852.88 --> 1855.50]  You know, discourse is doing it.
[1855.86 --> 1857.20]  Mike Perman.
[1857.54 --> 1858.86]  I'm probably going to butcher his name.
[1858.90 --> 1859.22]  Yeah.
[1859.28 --> 1863.90]  We had Mike on last summer talking about his business around sidekick.
[1863.90 --> 1863.94]  Yeah.
[1864.06 --> 1868.92]  He's, he's been able to do a really similar thing to Hubbard as Hubbard.
[1869.02 --> 1869.20]  Right.
[1869.28 --> 1875.12]  And like productize, he kind of has this open source version and then this pro version.
[1875.58 --> 1876.06]  Right.
[1876.06 --> 1879.62]  And that's kind of the same thing as, as Hubbard.
[1879.74 --> 1879.92]  Right.
[1879.92 --> 1882.92]  Like you can certainly host Hubbard yourself.
[1882.92 --> 1883.28]  Right.
[1883.38 --> 1889.78]  But I think that we're within the realm of reasonable pricing that even if you do it on Heroku, all
[1889.78 --> 1898.68]  of the components that run a production instance equal or are less than just paying for hubbard.com.
[1899.54 --> 1899.56]  Right.
[1899.56 --> 1909.70]  Which also makes it keep getting developed and hiring employees and supporting the software, upgrading the software, current version of Rails, you name it.
[1909.82 --> 1909.94]  Right.
[1910.40 --> 1910.66]  Right.
[1910.66 --> 1918.60]  One of the things is when, when we launched, when I launched it in October, you know, it was, you couldn't even create issues.
[1918.90 --> 1921.86]  You had to go to GitHub to create issues.
[1922.16 --> 1923.24]  It was literally like.
[1923.76 --> 1925.08]  It was like organizing.
[1925.66 --> 1926.18]  Right.
[1926.44 --> 1927.82]  Read only or not read only.
[1927.82 --> 1934.82]  No, it wasn't read only, but it was like, it was like, maybe I have this perfectionism in me.
[1934.86 --> 1935.04]  Right.
[1935.14 --> 1941.58]  That I was like, well, I don't want to provide a UX that's not as good as GitHub.
[1941.78 --> 1942.04]  Right.
[1942.08 --> 1948.10]  And I saw like creating issues as like, well, you know, there's a lot of ways to create issues.
[1948.96 --> 1951.20]  And that's a lot of effort for me to do that.
[1951.20 --> 1959.28]  You know, for the most part, I didn't see it as like that big a deal that you had to go to issues, go over to GitHub to create your issues.
[1959.44 --> 1959.56]  Right.
[1960.48 --> 1965.88]  But feature parity became like my highest priority when I started charging money for it.
[1965.88 --> 1966.10]  Right.
[1966.58 --> 1972.88]  Like when you're not charging money for something, you kind of have this leeway to be like, yeah, I don't, I don't have that.
[1973.24 --> 1973.60]  Right.
[1973.60 --> 1973.78]  Yeah.
[1973.96 --> 1974.18]  Right.
[1974.24 --> 1978.02]  But when people are paying money for it, they don't really take that as an excuse.
[1978.44 --> 1978.58]  Right.
[1979.66 --> 1984.38]  So charging money for it, like funded, improving of the tools.
[1984.38 --> 1987.54]  And that actually goes back into the open source version.
[1987.96 --> 1992.58]  So, you know, I wouldn't have done those things if I wasn't charging money for it.
[1992.58 --> 1992.74]  Right.
[1992.74 --> 1998.52]  Like it probably still would, I'd probably still be like, nah, you just go to GitHub for that.
[1998.60 --> 1998.78]  Right.
[1998.80 --> 2000.00]  Or use a command line tool.
[2000.48 --> 2005.10]  So coming up to feature parity was a big thing that was funded by getting money.
[2005.60 --> 2009.36]  And increasing the performance is something that is funded by that.
[2009.44 --> 2011.02]  And enterprise support as well.
[2011.02 --> 2015.70]  So, you know, things get better if you pay for them.
[2015.84 --> 2015.96]  Right.
[2016.08 --> 2018.50]  Like everything can't be free, I guess.
[2018.50 --> 2027.06]  So there's this, this old story about Apple and Dropbox when, back when Steve Jobs wanted
[2027.06 --> 2032.40]  to acquire Dropbox and his kind of took the strategy of making them feel like they needed
[2032.40 --> 2035.98]  to be acquired because he told them all you are is a feature.
[2036.54 --> 2038.16]  You know, you're not a business, you're a feature.
[2039.50 --> 2043.78]  And that, you know, that was not a winning strategy for him at the time.
[2043.80 --> 2048.06]  And we all seen what has happened with Dropbox grown to be a massive company since then.
[2048.50 --> 2053.28]  I think perhaps a naysayer, a few board would say, are you just, are you not just a feature
[2053.28 --> 2057.82]  of something that GitHub could add and then you'd be out of business?
[2058.22 --> 2059.26]  Have you thought about that?
[2060.80 --> 2063.40]  You know, it's, it's looms in the back of my mind.
[2063.48 --> 2063.84]  Right.
[2064.06 --> 2071.64]  Like, but then I just, I wonder, you know, part of me thinks like whether or not that's
[2071.64 --> 2072.98]  really what their focus is.
[2072.98 --> 2073.24]  Right.
[2073.38 --> 2080.82]  Like their focus right now is how do we make collaborating and sharing code more important?
[2081.04 --> 2086.94]  Like there, you see it in their entire tool chain is that GitHub is about sharing your
[2086.94 --> 2087.28]  code.
[2087.38 --> 2087.80]  Right.
[2088.48 --> 2090.66]  Like you can even see it in their permissions models.
[2090.82 --> 2091.12]  Right.
[2091.14 --> 2095.56]  Like when you give somebody OAuth access to your repo, you get everything.
[2095.72 --> 2098.92]  There's no way to just say, oh, give me issues only.
[2098.92 --> 2099.36]  Right.
[2099.72 --> 2102.94]  Like I think it flies in the face of their entire business model.
[2103.10 --> 2103.22]  Right.
[2103.30 --> 2107.30]  Like we, like they exist to share code.
[2107.42 --> 2114.16]  So why would they cripple their own tool and not give you access to code?
[2114.64 --> 2115.78]  If that makes sense.
[2116.10 --> 2116.36]  Yeah.
[2116.50 --> 2117.58]  You know, so.
[2117.74 --> 2120.76]  Well, I would think of it as a, as a feature ad on top of issues.
[2120.88 --> 2123.54]  Like here's a different, like you said, Hubbard was a view.
[2123.62 --> 2124.88]  It's a different view into issues.
[2124.88 --> 2125.84]  Obviously it's grown.
[2126.42 --> 2129.14]  So that was kind of the, the initial feature, the initial conceit.
[2129.74 --> 2131.62]  And they've also done some redesign to issues too.
[2131.68 --> 2136.46]  Like it's what's gotten, you know, full width and there's been enhancements over the years
[2136.46 --> 2137.14]  of issues too.
[2137.22 --> 2140.54]  So they've definitely been paying attention to the usefulness of issues.
[2140.82 --> 2145.60]  And according, you know, and according to their blog posts, they spent nine months on
[2145.60 --> 2149.32]  their, their redo, their latest redo of, of issues.
[2149.32 --> 2155.72]  And, you know, nine months of work and it, it didn't really significantly change.
[2157.64 --> 2164.82]  They still, I think to the core, they don't think you need anything more than what is there.
[2164.92 --> 2167.10]  And in some aspects, I agree.
[2167.80 --> 2175.08]  The original vision and my vision for, for Hubbard is not to particularly change the way
[2175.08 --> 2176.06]  you should use GitHub.
[2176.06 --> 2179.12]  It's kind of to enhance the way that you use GitHub, right?
[2179.20 --> 2182.80]  Like I believe wholeheartedly in GitHub flow.
[2183.06 --> 2186.64]  My own, my own personal development flow is right.
[2186.72 --> 2189.78]  Like I have master and master is always deployable.
[2190.42 --> 2193.14]  And when I want to work on something, I cut a branch.
[2193.90 --> 2200.94]  And then I, while I'm in that branch, depending on what I'm working on, every commit is tied to
[2200.94 --> 2202.12]  an issue number, right?
[2202.12 --> 2206.66]  So that I had like this full traceability into whatever it, it is or was.
[2207.26 --> 2212.86]  And then at the end of that, that turns into a pull request that feature branch turns into
[2212.86 --> 2217.84]  a pull request and somebody other than me looks at it and merges it in.
[2218.00 --> 2218.44]  Right.
[2218.48 --> 2223.22]  And that's how the, like my entire team, the two of us, that's how we work.
[2223.22 --> 2223.44]  Right.
[2223.44 --> 2227.46]  Like we don't require like a daily standup meeting or anything like that.
[2227.46 --> 2232.46]  Like we collaborate through like the tool itself, the tool itself, like GitHub itself.
[2232.56 --> 2239.38]  And, and really Hooboard is an effort to like enhance that or make that easier or like visualize
[2239.38 --> 2242.36]  that workflow, not like change it.
[2242.56 --> 2243.06]  You know what I mean?
[2243.84 --> 2245.54]  Like, let's ask a different question then.
[2245.62 --> 2248.36]  What if, um, let's say there's a GitHub or listen to this.
[2248.44 --> 2252.04]  Let's say it's Chris Wallenstroth for what, for whatever reason he's listening to the
[2252.04 --> 2252.58]  change log.
[2252.66 --> 2253.46]  Hi, Chris, by the way.
[2253.96 --> 2255.46]  Um, and he's like, you know what?
[2255.46 --> 2256.94]  I like what you did here, Ryan.
[2257.02 --> 2259.46]  And he, he, he wants to acquire you.
[2259.52 --> 2260.56]  Is that an option for you?
[2261.40 --> 2263.00]  I guess, I don't, I don't know.
[2263.10 --> 2267.04]  I would, I would take an unsolicited offer, uh, any day.
[2267.10 --> 2268.84]  I don't, I don't know necessarily.
[2269.60 --> 2270.78]  Do you want to become a GitHub?
[2271.10 --> 2272.00]  It depends.
[2273.80 --> 2274.82]  Derek's chuckling over there.
[2275.26 --> 2277.96]  Everything for sale at the right price.
[2277.96 --> 2283.06]  You're giving me a hard time, but like, is that an out strategy that I've, I've thought
[2283.06 --> 2283.96]  of, of course, right?
[2284.28 --> 2286.84]  Um, maybe it depends.
[2287.18 --> 2288.40]  Like anything, it depends.
[2288.62 --> 2288.68]  Yeah.
[2288.74 --> 2292.62]  It comes back to that question too, that Jerry was asking earlier, which is, well, I think
[2292.62 --> 2296.32]  even you mentioned it, Ryan, which is that, you know, you could write an adapter for a
[2296.32 --> 2301.78]  different application other than GitHub issues and still take Hubboard and do something with
[2301.78 --> 2302.06]  it.
[2302.16 --> 2302.76]  That's useful.
[2302.76 --> 2308.18]  I think what we're trying to get at here is how much anxiety looms over you, over the
[2308.18 --> 2312.62]  fact that you're building a business on top of a business and that even the data model,
[2312.70 --> 2313.72]  you don't have control over.
[2313.90 --> 2319.06]  And any other day, you're not the, you're not the, um, you know, the canonical data source
[2319.06 --> 2319.36]  even.
[2320.72 --> 2320.82]  Yeah.
[2321.02 --> 2326.36]  And, uh, I do, I wouldn't say it keeps me up at night, but yeah, I think about it.
[2326.70 --> 2327.98]  I definitely think about it.
[2327.98 --> 2333.76]  Um, not being the single source of truth as far as like the viability of a business,
[2333.76 --> 2337.82]  I'm not like, personally, I'm not concerned, right?
[2338.08 --> 2340.54]  I have a skill it's called, you know, I'm a developer.
[2340.54 --> 2341.24]  I have a skill.
[2341.40 --> 2342.30]  I built this thing.
[2342.30 --> 2347.96]  Like, even if it fails at the end of the day, I'm not going to be unemployable, but yeah,
[2347.96 --> 2353.58]  once you turn into a business and you have employees, your concerns change, right?
[2353.58 --> 2358.70]  Like, I'm more concerned about the wellbeing of the person that I convinced to come work
[2358.70 --> 2360.80]  for me than I am for my own wellbeing.
[2361.40 --> 2363.30]  So yeah, that really concerns me.
[2364.24 --> 2364.42]  Yeah.
[2364.46 --> 2371.60]  At the same time, I just don't, I don't think GitHub is in, is secretly working on a Kanban
[2371.60 --> 2373.00]  view for, for issues.
[2373.36 --> 2373.62]  Probably not.
[2373.72 --> 2373.84]  Yeah.
[2374.18 --> 2375.10]  I don't think so.
[2375.16 --> 2376.22]  I would think that they're-
[2376.22 --> 2376.42]  I'm not worried about it.
[2376.44 --> 2378.02]  I just wondered if you were worried about it.
[2378.10 --> 2378.34]  Right.
[2378.34 --> 2385.52]  I would think that they're ethical enough to let me know, or, or at least maybe business
[2385.52 --> 2392.56]  savvy enough to be like, to at least exhaust acquisition avenues before, before, before
[2392.56 --> 2393.86]  committing their own development time.
[2393.86 --> 2394.06]  Right.
[2394.66 --> 2394.92]  Yeah.
[2395.78 --> 2397.12]  Let's pause the show for a minute.
[2397.64 --> 2399.60]  Give a shout out to a sponsor, DigitalOcean.
[2399.98 --> 2402.30]  Simple cloud hosting built for developers.
[2402.30 --> 2408.58]  In 55 seconds, you'll have a cloud server with full root access, and it just doesn't get
[2408.58 --> 2410.12]  any easier than that.
[2410.68 --> 2416.30]  Pricing plan started only five bucks a month for half a RAM, 20 gigs of SSD drive space,
[2416.52 --> 2419.36]  one CPU, and one terabyte of transfer.
[2419.58 --> 2422.38]  That's a lot for five bucks a month.
[2422.98 --> 2428.68]  DigitalOcean also has data centers all across the world, New York, San Francisco, Amsterdam,
[2429.18 --> 2431.86]  Singapore, and their newest region, London.
[2431.86 --> 2437.32]  You can easily migrate your data between those regions, making your data always closest to
[2437.32 --> 2437.92]  your users.
[2438.36 --> 2441.92]  Use the promo code CHANGELOGNovember in lowercase.
[2442.08 --> 2443.66]  It's important that you use lowercase.
[2444.32 --> 2448.22]  CHANGELOGNovember to get a $10 hosting credit when you sign up.
[2448.58 --> 2452.04]  Head to digitalocean.com right now to get started, and back to the show.
[2452.04 --> 2459.22]  You said that GitHub acquisition would be a decent exit strategy for you, but the fact
[2459.22 --> 2462.80]  of the matter is that you don't need an exit strategy at the moment.
[2462.94 --> 2467.64]  You have a growing business, a very small, probably, overhead.
[2467.64 --> 2471.60]  You have some increasingly large customers.
[2472.82 --> 2476.96]  Perhaps a surprise to you is how many enterprise customers you have on your homepage.
[2477.18 --> 2482.16]  I see Microsoft, Mozilla, Adobe amongst your customer list.
[2482.90 --> 2487.16]  Tell us about the enterprise and your success there and challenges.
[2487.16 --> 2491.64]  So on the enterprise site, those are actually SaaS users.
[2491.64 --> 2492.04]  Oh, are they?
[2492.30 --> 2492.62]  They're not?
[2492.82 --> 2493.10]  Yeah.
[2493.62 --> 2500.44]  Most, the dirty little secret is that when you get into enterprise, I really am contractually
[2500.44 --> 2504.06]  restricted from telling you who actually bought it.
[2505.74 --> 2506.90]  If that makes sense.
[2506.90 --> 2508.86]  So by enterprise, you're speaking of a different product.
[2509.00 --> 2512.60]  This is an on-premise product as opposed to just like a large enterprise company that's
[2512.60 --> 2513.54]  using your SaaS product.
[2513.54 --> 2513.94]  Yeah.
[2514.84 --> 2521.46]  Over the lifespan of Hubbard, there's been a lot of interest in providing GitHub enterprise
[2521.46 --> 2523.00]  support, right?
[2523.24 --> 2530.64]  So a lot of people may not be aware of it, but GitHub offers an on-premise version of GitHub.
[2530.96 --> 2531.26]  Right.
[2531.42 --> 2531.62]  Right?
[2532.04 --> 2538.82]  You can go to them and they will give you a virtual machine that has GitHub installed on
[2538.82 --> 2539.02]  it.
[2539.02 --> 2548.98]  And you can basically, as simple as importing it into your vSphere or your Essex environment,
[2549.40 --> 2555.28]  you spin up this VM, you upload like this package, they call it the GitHub package, the GHP,
[2556.04 --> 2557.14]  and a license file.
[2557.52 --> 2559.50]  And you hit a big green button.
[2560.12 --> 2563.02]  And, you know, like an hour later, the thing's fully provisioned.
[2563.02 --> 2569.26]  And it is literally like GitHub inside your network behind your firewall, which is a really
[2569.26 --> 2572.38]  incredible way to like deliver software.
[2573.60 --> 2575.76]  It's really fascinating.
[2575.76 --> 2585.56]  And there was like tons of interest for people that were like, hey, we want to use Hubbard for our internal
[2585.56 --> 2587.80]  GitHub enterprise instance.
[2588.46 --> 2592.80]  And it seemed plausible, you know?
[2593.46 --> 2593.76]  Like...
[2594.40 --> 2595.14]  You weren't sure?
[2595.14 --> 2601.86]  Well, you know, it was like, well, they claim that their API is fully compatible.
[2602.10 --> 2603.44]  Like it should work the same.
[2603.64 --> 2607.70]  So, you know, it should be as easy as, you know, we'll just point it at GitHub enterprise
[2607.70 --> 2608.62]  and it should work.
[2608.72 --> 2608.84]  Right?
[2609.70 --> 2616.14]  It turns out that big companies are not particularly interested in...
[2616.14 --> 2623.58]  They weren't or aren't like interested in taking the open source version of Hubbard and sort of
[2623.58 --> 2626.14]  hosting it themselves and pointing at their GitHub enterprise.
[2626.32 --> 2626.44]  Right?
[2627.10 --> 2632.76]  Like there's some challenges around configuring it correctly and updating it.
[2632.92 --> 2635.00]  And like you're going to have to pay a full-time engineer.
[2635.00 --> 2635.52]  Right?
[2635.78 --> 2638.24]  Or somebody to maintain the thing.
[2638.92 --> 2640.78]  To know how to like...
[2640.78 --> 2644.24]  If I made changes to the database, right?
[2644.68 --> 2645.86]  Like it uses CouchDB.
[2646.14 --> 2651.18]  That's not like a widely used or commonly known thing.
[2651.28 --> 2654.06]  Like how do you migrate documents in CouchDB?
[2654.36 --> 2662.04]  That's kind of a thing that isn't going to be easy for me to like put in a wiki.
[2662.56 --> 2668.64]  And I'm not particularly going to want to sit down with somebody who isn't paying me money
[2668.64 --> 2670.38]  and walk them through how to do it.
[2670.42 --> 2670.62]  Right?
[2671.26 --> 2673.42]  I'm likely going to be like, no, that's okay.
[2673.48 --> 2674.54]  I'm not interested.
[2674.54 --> 2679.34]  That being said, you know, there's a ton of interest in enterprise support.
[2680.50 --> 2685.82]  And, you know, maybe me being a perfectionist, I really wanted to give the same experience
[2685.82 --> 2688.96]  as GitHub enterprise itself.
[2689.18 --> 2689.50]  Right?
[2689.50 --> 2699.62]  So we set out to build a virtual appliance that, you know, kind of like reverse engineered GitHub enterprise itself
[2699.62 --> 2702.32]  and tried to build the exact same experience.
[2703.32 --> 2704.94]  Did you collaborate with them at all on that?
[2705.30 --> 2708.58]  Did you like work with the GitHub enterprise team by any chance?
[2708.58 --> 2711.90]  So no and yes.
[2712.50 --> 2717.22]  At the time it was like for a long time it was this growing interest in it.
[2717.54 --> 2724.04]  And I was like, well, does anybody want to like loan me their GitHub enterprise environment so I can test this thing?
[2724.58 --> 2725.84]  You know, at the time I didn't have any money.
[2725.84 --> 2733.28]  I'm not going to go pay $5,000 for a license to GitHub enterprise just to test something that I don't even know anyone would pay for.
[2733.48 --> 2733.60]  Right?
[2734.72 --> 2739.72]  And so I asked GitHub for, you know, a license to GitHub enterprise.
[2740.86 --> 2744.10]  And they were like, oh, yeah, here's a 90 day free trial.
[2744.10 --> 2748.64]  And then, you know, like 90 days later I still didn't have a product, you know.
[2749.52 --> 2759.18]  And so, you know, I think part of that effort kind of got them in gear to start their developer program.
[2760.40 --> 2767.12]  And so now like you just enroll in their developer program and you do get a license to GitHub enterprise now.
[2767.76 --> 2770.84]  Which is really nice for integrators like myself.
[2770.84 --> 2780.64]  But as far as like building the virtual appliance itself, like there wasn't a whole lot of back and forth with GitHub.
[2781.84 --> 2795.44]  I did ask them, you know, we asked them some questions around like, you know, how are you exporting, you know, how are you creating this OVA that like cleanly installs into VMware and stuff?
[2795.62 --> 2797.68]  And they actually like were really helpful.
[2797.68 --> 2814.12]  And someone from their team like provided us with like this code that like I think that was like our one hanging point was like we couldn't get it to cleanly and import into VMware without it complaining about like its manifest file being corrupted.
[2814.84 --> 2817.18]  And so, yeah, they definitely helped with that.
[2817.58 --> 2817.78]  Yeah.
[2818.02 --> 2818.26]  Yeah.
[2818.26 --> 2818.82]  They helped.
[2819.30 --> 2819.90]  I'm going to.
[2819.98 --> 2820.14]  Yeah.
[2820.40 --> 2820.94]  They helped.
[2821.30 --> 2821.74]  They helped.
[2821.74 --> 2823.82]  That was a really long explanation to.
[2824.02 --> 2824.28]  Yes.
[2824.68 --> 2831.14]  It's just interesting because, I mean, that's that's one of their obvious directions in their business.
[2831.66 --> 2833.52]  And you just wonder how flexible they are to.
[2834.32 --> 2843.12]  And even them helping you with that enterprise integration might give you some, you know, signs of bright spots, whether or not they're going to.
[2843.68 --> 2845.56]  You know, consume you at some point.
[2846.98 --> 2847.70]  What I mean?
[2847.80 --> 2848.18]  Well said.
[2848.28 --> 2848.46]  Yeah.
[2849.32 --> 2849.74]  Consume.
[2849.74 --> 2855.52]  Consume you, take you over, eat you, whatever, you know, stomp on you or acquire you, whatever you want to say.
[2856.10 --> 2859.70]  That sounds like you had some technical challenges around creating this virtual appliance.
[2860.66 --> 2871.08]  Any interesting stories or neat solutions that came out of that technology wise or maybe even the toolkits that you're using to build these this virtual appliance?
[2871.08 --> 2880.56]  You know, the interesting thing is there isn't there isn't a lot of tools out there for this.
[2881.28 --> 2882.14]  No stack overflow?
[2882.98 --> 2883.90]  Not really.
[2884.32 --> 2892.02]  You know, there's no there's no guide or screencast on like or blog about like how to how to create a virtual appliance.
[2892.02 --> 2908.22]  Like, how do you create this virtual, you know, how do you create this VM that gets deployed on someone else's network that, you know, if you sell this thing to a Fortune 500 company, you're going to see big boy networks, I like to call.
[2908.48 --> 2908.64]  Right.
[2908.64 --> 2911.24]  Like, these things are like lockdown.
[2912.00 --> 2922.60]  You need you need like if you want to reach out to the Internet or outside of their firewall, you need credentials to get out of their, you know, their proxy servers.
[2922.60 --> 2931.54]  So things that you take for granted, like gem install or bundle install, try to do that without the Internet.
[2933.04 --> 2936.24]  You know, things like apt get install without the Internet.
[2936.96 --> 2940.08]  Handling things like self-signed SSL certificates.
[2940.88 --> 2942.52]  Man, I can't do anything without the Internet.
[2942.74 --> 2944.84]  I try to get on a on an airplane thing.
[2944.92 --> 2946.48]  I'm going to get a whole bunch of coding done.
[2946.54 --> 2947.26]  It's going to be awesome.
[2948.02 --> 2951.22]  And I've and then I realized I didn't prepare some sort of docs I need.
[2951.22 --> 2952.98]  And I'm just like, screw it.
[2953.00 --> 2954.16]  I'm going to watch a movie or something.
[2955.32 --> 2955.44]  Right.
[2956.14 --> 2960.46]  And then and then supporting something that you can't touch or.
[2960.74 --> 2960.92]  Yeah.
[2960.92 --> 2961.38]  How do you do that?
[2961.50 --> 2961.64]  See.
[2964.46 --> 2964.90]  Poorly.
[2970.14 --> 2971.52]  It's a lot of back and forth.
[2971.70 --> 2972.96]  Sometimes it's screen sharing.
[2972.96 --> 2973.30]  Yeah.
[2974.86 --> 2978.96]  You know, one of one of the biggest challenges usually is around SSL.
[2978.96 --> 2981.96]  SSL people will configure customers.
[2982.78 --> 2983.02]  Sorry.
[2983.14 --> 2993.94]  We'll configure GitHub Enterprise with a self-signed SSL certificate or they'll use like a certificate chain that isn't installed by default in Linux.
[2995.24 --> 2998.72]  And so getting those onto the machine is probably the biggest hurdle.
[2998.72 --> 3019.74]  And then, you know, you run into challenges of like, you know, you have to you have to configure the network to speak to internal name servers to, you know, because like, how do you resolve GitHub dot company dot com when it isn't in, you know, a public name server?
[3019.92 --> 3021.08]  It's in an internal name server.
[3021.08 --> 3021.32]  Right.
[3021.38 --> 3031.64]  Like, so you're given this string of this host name, but you have to talk to an internal you have to talk to like an internal DNS server to get the IP of the machine.
[3032.48 --> 3032.90]  Yeah.
[3033.86 --> 3034.98]  It was challenging.
[3035.14 --> 3035.38]  Right.
[3035.38 --> 3063.78]  And coming from a guy who started his career as a dot net developer and then did this out of a whim, wasn't even a Ruby developer, you know, and having to debug some of these things like open SSL peer verification, you know, and like, you know, going from a front end heavy developer, like to a full fledged DevOps engineer is something I never expected my career to take a path to.
[3063.78 --> 3065.62]  So is it worth it?
[3067.86 --> 3069.82]  It's it's worth it.
[3071.00 --> 3082.08]  So I've had I've had a couple people who they're they're also building kind of GitHub focused products that like extend GitHub.
[3082.56 --> 3087.46]  I've had them approach me and say, you know, ask me questions like, how did you start this?
[3087.54 --> 3089.72]  What's your relationship with like with GitHub?
[3089.72 --> 3093.18]  And I've also reached out to other ones like Travis CI.
[3093.72 --> 3101.62]  I've had conversations with Matthias, I think his name is, you know, and asked him questions about like how how they do stuff.
[3102.56 --> 3109.38]  And, you know, it comes up like, do you do you regret like doing enterprise support?
[3109.38 --> 3113.28]  And, you know, at the end of the day, no, of course not.
[3113.38 --> 3116.12]  Like, like, it's very lucrative.
[3116.38 --> 3121.66]  But you're talking about in some instances, it's a 10 month sales cycle.
[3121.84 --> 3130.40]  So unless you can unless you have that SaaS backing to like sustain you through that 10 month sales cycle, you're it's not going to be fun.
[3130.40 --> 3130.80]  Right.
[3130.80 --> 3132.94]  It's a it's a lot of work.
[3133.02 --> 3137.92]  There's a lot of red tape you have to go through to sell to to large enterprises.
[3138.26 --> 3140.70]  But it's a learning experience.
[3140.76 --> 3149.68]  I'll tell you, if you guys ever really want to know, like the contract negotiations and, you know, stuff like that.
[3150.10 --> 3152.46]  And the but it can be.
[3153.26 --> 3154.00]  It can be.
[3154.00 --> 3162.90]  Well, since we're talking about pains in the buts, maybe it's a good segue to to something that's probably a deeper topic, which we may not have the full amount of time we should actually give this.
[3163.12 --> 3170.60]  So I don't know if it's something we could talk about in, you know, the the sub 10 minutes we have for this show left or not.
[3170.68 --> 3174.48]  But can you talk briefly about the technical stack that you built upon?
[3174.56 --> 3178.00]  You know, I know you started in 2011 from a Java background.
[3179.46 --> 3179.72]  Dot net.
[3179.84 --> 3180.52]  Used Ruby.
[3180.80 --> 3181.72]  Or sorry, was it dot net?
[3182.60 --> 3183.18]  It was dot net.
[3183.18 --> 3187.18]  OK, I remember talking earlier to you about somebody through on a Java project.
[3187.98 --> 3189.14]  I thought Java for a second.
[3189.80 --> 3194.76]  You know, so, you know, doing Ruby mainly to use Heroku for free or one dyno.
[3195.24 --> 3198.62]  Can you talk about your tech stack and just what you're using to any degree?
[3200.06 --> 3200.72]  Yeah, sure.
[3201.08 --> 3205.88]  The Hubort API itself or is effectively a Sinatra app.
[3206.40 --> 3212.58]  I've rewrote it probably four times and they're like improving it and stuff.
[3213.18 --> 3219.38]  And I settled on and, you know, I'll give a little shout out to forget his name.
[3219.46 --> 3221.14]  Andrew Macaray.
[3222.94 --> 3223.72]  That's what I call him.
[3224.60 --> 3226.14]  He he wrote like a tool called Monocle.
[3226.84 --> 3231.90]  And I think he has a new like app called he's a big Sinatra guy.
[3231.90 --> 3239.48]  He wrote a tool called Trevi, which is like a little like some patterns he uses to build Sinatra apps.
[3239.98 --> 3242.60]  So I eventually refactored to that.
[3242.86 --> 3244.26]  And and it's good.
[3245.06 --> 3250.26]  I think eventually we will rewrite majority of it in Rails.
[3250.26 --> 3253.92]  I like to say that there's a lot of paper cuts with Sinatra.
[3254.24 --> 3260.28]  And once you get to a certain size, it's just a lot easier just to just go with Rails.
[3260.46 --> 3263.04]  Like Rails is pretty fantastic in that regard.
[3263.86 --> 3265.04]  The front end.
[3265.50 --> 3268.82]  I rewrote an Ember JS and love it.
[3269.00 --> 3269.56]  It's great.
[3269.56 --> 3272.70]  I highly recommend Ember.
[3273.06 --> 3273.44]  It is.
[3273.92 --> 3275.08]  It's such a.
[3275.68 --> 3276.44]  When did you rewrite?
[3277.32 --> 3278.64]  Oh, last year.
[3279.08 --> 3284.00]  January ish of last year is when we when I released the full Ember rewrite.
[3284.92 --> 3286.38]  Previously, it was Backbone.
[3286.96 --> 3290.46]  And, you know, three years ago, Backbone wasn't even one.
[3290.56 --> 3295.20]  Oh, I think I started the project with Backbone zero point three point three.
[3295.20 --> 3299.76]  So it was definitely bleeding edge from the start.
[3299.90 --> 3301.60]  And even with Ember, it was still pre one.
[3302.62 --> 3305.02]  You know, we store some things in CouchDB.
[3305.58 --> 3308.10]  We, of course, use Redis as part of our stack.
[3308.74 --> 3309.22]  Memcached.
[3309.72 --> 3313.72]  We do some real time communication stuff with WebSockets.
[3314.46 --> 3316.26]  And that was kind of a journey.
[3317.20 --> 3318.76]  I started out with Socket.io.
[3319.38 --> 3322.62]  That that worked great for like two and a half years.
[3322.62 --> 3328.04]  I literally it was like 40 lines of JavaScript that I never touched for a year and a half.
[3328.98 --> 3334.80]  And then I had some problems with that and moved to a hand rolled like Sinatra streaming server.
[3335.32 --> 3337.02]  And then I had some problems with that.
[3337.12 --> 3339.62]  And then eventually settled on Faye.
[3340.38 --> 3341.58]  I've used Faye in the past.
[3341.72 --> 3342.18]  Nice tool.
[3342.36 --> 3343.88]  It's it's not perfect.
[3344.68 --> 3349.62]  I really wish that I could use something like Pusher or PubNub.
[3350.62 --> 3351.06]  But.
[3351.78 --> 3352.30]  Why can't you?
[3353.62 --> 3354.30]  Enterprise.
[3355.26 --> 3357.12]  To be to be short and sweet.
[3357.24 --> 3357.58]  Enterprise.
[3359.12 --> 3368.18]  I have to be really cautious in particular about the technology choices that we make is because everything still needs to run.
[3369.06 --> 3371.40]  On a VM for enterprise.
[3371.76 --> 3371.94]  Right.
[3372.12 --> 3372.88]  So like I don't.
[3373.38 --> 3377.42]  Some of these really fantastic services are kind of out of reach.
[3378.06 --> 3379.88]  Unless they're easily hosted.
[3379.88 --> 3380.76]  You know.
[3381.56 --> 3381.80]  Yeah.
[3382.28 --> 3384.62]  We're doing some things around right now.
[3384.76 --> 3387.06]  We're doing some things around improving a performance.
[3387.56 --> 3387.74]  Making.
[3387.98 --> 3388.72]  Speeding things up.
[3389.40 --> 3392.20]  And building some business insights.
[3392.48 --> 3393.16]  And some analytics.
[3393.82 --> 3394.94]  Into like.
[3395.32 --> 3395.48]  You know.
[3395.56 --> 3396.66]  Lead times of cards.
[3397.16 --> 3398.22]  Things of that nature.
[3398.22 --> 3400.22]  We've settled on.
[3400.22 --> 3400.24]  We've settled on.
[3400.46 --> 3401.62]  The elk stack.
[3401.96 --> 3402.60]  Log stash.
[3403.70 --> 3404.78]  Elastic search.
[3405.72 --> 3406.06]  Cabana.
[3406.46 --> 3407.50]  Puppet of course is.
[3407.90 --> 3408.92]  The magic that.
[3409.14 --> 3409.92]  That get up.
[3410.02 --> 3412.04]  Or who board enterprise is built upon.
[3413.02 --> 3413.36]  And then.
[3413.50 --> 3413.64]  You know.
[3413.70 --> 3414.54]  Shout out to Heroku.
[3414.72 --> 3415.54]  They've been fantastic.
[3415.76 --> 3417.38]  We're still on them to this day.
[3418.18 --> 3418.62]  I think.
[3418.80 --> 3419.92]  I think who board.
[3420.42 --> 3421.24]  Chugs along.
[3421.78 --> 3423.04]  I think we have 6,000.
[3423.04 --> 3423.34]  You know.
[3423.40 --> 3425.46]  Average monthly active users.
[3425.76 --> 3425.90]  You know.
[3426.02 --> 3427.10]  Really pounding it.
[3427.54 --> 3430.04]  And we're on two extra large dynos.
[3430.42 --> 3430.90]  Nice.
[3431.12 --> 3432.26]  Or not extra large.
[3432.36 --> 3433.66]  But the 2x dynos.
[3434.08 --> 3434.36]  Mm-hmm.
[3434.84 --> 3435.18]  So.
[3435.38 --> 3435.56]  You know.
[3435.66 --> 3435.78]  That's.
[3436.22 --> 3437.14]  It's pretty great.
[3437.46 --> 3439.14]  We have some things on AWS.
[3439.14 --> 3439.82]  Of course.
[3440.62 --> 3442.16]  I guess that's pretty much.
[3442.16 --> 3442.90]  The whole rundown.
[3443.18 --> 3444.08]  Of our stack.
[3445.54 --> 3446.12]  Awesome man.
[3446.18 --> 3446.66]  Well unfortunately.
[3446.78 --> 3447.52]  We're running out of time.
[3447.58 --> 3447.80]  Otherwise.
[3448.00 --> 3448.36]  We would.
[3448.68 --> 3449.52]  Question you on.
[3449.72 --> 3450.58]  Individual choices.
[3450.74 --> 3451.18]  Why Ember?
[3451.28 --> 3451.74]  Why Couch?
[3451.74 --> 3452.88]  We love those kind of questions.
[3453.12 --> 3453.26]  But.
[3453.62 --> 3454.64]  I have more questions.
[3454.78 --> 3455.30]  We just can't.
[3455.32 --> 3456.18]  We just can't answer them.
[3456.36 --> 3456.40]  We can't do it.
[3456.42 --> 3457.12]  We can't ask them.
[3457.56 --> 3458.96]  Can we maybe ask this one question.
[3459.10 --> 3459.60]  Before we ask.
[3459.82 --> 3460.04]  What you got.
[3460.16 --> 3460.40]  The final question.
[3460.44 --> 3460.80]  What you got.
[3461.08 --> 3461.40]  Is.
[3461.74 --> 3462.76]  I don't know if you've.
[3463.14 --> 3464.46]  And maybe this is a short one too.
[3464.54 --> 3465.04]  Which is.
[3465.56 --> 3466.78]  The fact that you're open source.
[3467.08 --> 3467.76]  And accepting.
[3468.60 --> 3469.00]  Contributions.
[3469.00 --> 3469.66]  And pull requests.
[3469.74 --> 3470.40]  I know we talked about.
[3470.52 --> 3471.36]  About the license there.
[3471.40 --> 3472.04]  But then we just kind of.
[3472.12 --> 3472.88]  Close the loop on.
[3473.22 --> 3474.36]  How you deal with.
[3475.32 --> 3476.38]  Forks and pull requests.
[3476.38 --> 3477.90]  Back to the open source version.
[3477.98 --> 3479.00]  And how that plays into.
[3479.38 --> 3480.26]  Just this fact.
[3480.34 --> 3481.28]  Because it brought that up.
[3481.30 --> 3481.70]  In my mind.
[3481.76 --> 3482.32]  Whenever you mentioned.
[3482.44 --> 3482.80]  Enterprise.
[3482.90 --> 3483.24]  And how.
[3483.80 --> 3484.80]  Every time you make a choice.
[3484.86 --> 3485.64]  On what to use.
[3485.76 --> 3486.84]  And code to add.
[3486.92 --> 3487.56]  Is based on.
[3487.66 --> 3488.12]  Whether or not.
[3488.32 --> 3489.50]  Enterprise can support it.
[3490.42 --> 3490.94]  You know.
[3490.94 --> 3492.16]  We don't get a whole lot.
[3492.36 --> 3493.34]  Of pull requests.
[3494.26 --> 3494.32]  And.
[3494.88 --> 3495.74]  Bad on me.
[3496.08 --> 3496.42]  There's.
[3496.78 --> 3497.62]  One in particular.
[3497.80 --> 3498.72]  That's been open for a while.
[3498.72 --> 3499.22]  Which is.
[3500.18 --> 3501.06]  Add milestone.
[3501.86 --> 3502.44]  You know.
[3502.54 --> 3504.14]  It's been open for a couple months.
[3504.14 --> 3504.46]  And.
[3505.14 --> 3506.04]  Unfortunately for him.
[3506.04 --> 3506.50]  It was like.
[3506.72 --> 3508.02]  In the middle of a big rewrite.
[3508.16 --> 3508.64]  That I made.
[3508.86 --> 3509.56]  And so.
[3509.56 --> 3510.32]  Some of his stuff.
[3510.32 --> 3510.74]  Didn't.
[3510.74 --> 3511.98]  Merge in cleanly.
[3512.60 --> 3513.10]  Accepting.
[3513.18 --> 3514.60]  Contributions is hard.
[3514.72 --> 3515.30]  It's kind of.
[3515.86 --> 3516.44]  It's difficult.
[3516.56 --> 3516.94]  Ethically.
[3516.94 --> 3517.70]  And it's difficult.
[3517.70 --> 3518.16]  Like.
[3519.68 --> 3520.16]  Legally.
[3520.38 --> 3520.60]  Too.
[3520.98 --> 3522.22]  I don't really know.
[3522.44 --> 3523.02]  The specifics.
[3523.02 --> 3523.52]  But.
[3523.52 --> 3524.78]  I guess.
[3524.78 --> 3526.30]  To try to cover all my bases.
[3526.30 --> 3527.60]  I do ask people.
[3527.60 --> 3528.20]  To sign.
[3528.62 --> 3528.96]  A.
[3528.96 --> 3530.54]  Contributor license agreement.
[3531.08 --> 3531.82]  Which basically.
[3531.82 --> 3532.44]  Just says.
[3532.62 --> 3532.78]  You know.
[3532.90 --> 3533.86]  Kind of do whatever.
[3534.52 --> 3535.60]  We want to do.
[3535.76 --> 3536.36]  With your code.
[3536.94 --> 3537.46]  That being said.
[3537.58 --> 3537.74]  Anything.
[3537.96 --> 3538.06]  That's.
[3538.06 --> 3539.08]  Within the MIT license though.
[3539.14 --> 3539.32]  Right.
[3539.34 --> 3540.54]  Within the MIT license.
[3540.94 --> 3541.14]  You know.
[3541.42 --> 3542.18]  Just ethically.
[3542.38 --> 3542.48]  And.
[3542.48 --> 3542.70]  And.
[3542.70 --> 3543.22]  And for me.
[3543.36 --> 3543.44]  Like.
[3543.54 --> 3543.58]  If.
[3543.64 --> 3544.48]  If somebody contributes.
[3544.52 --> 3545.26]  Something significant.
[3545.68 --> 3545.88]  To.
[3546.64 --> 3547.52]  The open source version.
[3548.38 --> 3548.82]  I.
[3548.82 --> 3549.80]  I will do my best.
[3549.90 --> 3551.24]  To continue to support it.
[3551.38 --> 3551.62]  For.
[3551.88 --> 3552.16]  Forever.
[3552.50 --> 3552.66]  Like.
[3552.82 --> 3553.02]  I'm.
[3553.08 --> 3553.98]  I'm not going to take.
[3554.74 --> 3555.82]  Large contributions.
[3556.08 --> 3556.42]  Lightly.
[3556.64 --> 3556.84]  Right.
[3556.94 --> 3557.16]  Like.
[3558.44 --> 3559.28]  If someone.
[3559.96 --> 3560.70]  Contributes something.
[3560.82 --> 3561.02]  That's.
[3561.14 --> 3561.80]  That's significant.
[3562.10 --> 3562.72]  I'm going to make sure.
[3562.84 --> 3563.18]  That I can.
[3563.66 --> 3564.20]  Support it.
[3564.60 --> 3564.96]  Because.
[3565.12 --> 3566.14]  You can't really trust.
[3566.32 --> 3567.08]  Somebody else.
[3567.22 --> 3567.32]  To.
[3567.32 --> 3568.54]  To be there forever.
[3568.86 --> 3569.00]  Right.
[3569.86 --> 3570.34]  So.
[3570.56 --> 3571.44]  If I do.
[3572.22 --> 3572.56]  Uh.
[3572.82 --> 3573.54]  I will.
[3573.70 --> 3574.06]  Make sure.
[3574.16 --> 3574.40]  That it.
[3574.52 --> 3574.98]  That it's.
[3575.10 --> 3576.10]  Going to be supported.
[3576.32 --> 3576.60]  Forever.
[3577.30 --> 3578.16]  Other than that.
[3578.22 --> 3578.36]  Like.
[3578.50 --> 3579.28]  There's people.
[3579.28 --> 3580.28]  That have forked it.
[3580.80 --> 3581.34]  Crush path.
[3581.42 --> 3582.06]  Is a big one.
[3583.10 --> 3583.46]  I think.
[3583.58 --> 3583.64]  They're.
[3583.72 --> 3584.52]  They're a San Francisco.
[3584.52 --> 3585.04]  Startup.
[3585.20 --> 3585.54]  I know.
[3585.54 --> 3586.68]  That they run a fork.
[3586.76 --> 3587.48]  And they've added.
[3587.48 --> 3588.32]  Tons of features.
[3588.32 --> 3589.62]  That are important to them.
[3590.68 --> 3591.04]  Um.
[3591.66 --> 3592.30]  And then.
[3592.52 --> 3593.18]  For a spell.
[3593.40 --> 3593.72]  Uh.
[3593.72 --> 3594.04]  Shopify.
[3594.04 --> 3594.66]  Had a.
[3594.76 --> 3595.40]  Had a fork.
[3595.52 --> 3596.38]  That they were working on.
[3596.38 --> 3597.40]  But that kind of disappeared.
[3597.52 --> 3598.38]  I'm not sure if they.
[3599.16 --> 3599.92]  Privatized that.
[3600.12 --> 3600.28]  Or.
[3601.00 --> 3602.16]  Or what went on there.
[3602.24 --> 3603.28]  If they decided to.
[3603.50 --> 3604.10]  Do something else.
[3604.20 --> 3604.80]  And deleted it.
[3604.94 --> 3605.14]  But.
[3605.54 --> 3605.72]  You know.
[3605.76 --> 3606.10]  There are.
[3606.26 --> 3607.50]  There are people that exist.
[3607.64 --> 3607.82]  That.
[3607.92 --> 3608.74]  That have forked it.
[3608.84 --> 3609.62]  And added features.
[3609.62 --> 3610.68]  That they care about.
[3611.10 --> 3611.96]  But they necessarily.
[3612.06 --> 3613.32]  Haven't contributed back.
[3613.74 --> 3614.38]  If that makes sense.
[3615.02 --> 3615.16]  Sure.
[3615.16 --> 3615.80]  All right.
[3615.86 --> 3616.06]  Ryan.
[3616.14 --> 3616.26]  Well.
[3616.34 --> 3617.78]  It's time for those closing questions.
[3618.16 --> 3619.02]  As a change log listener.
[3619.18 --> 3620.50]  You probably saw this one coming.
[3620.68 --> 3621.38]  Our old favorite.
[3622.04 --> 3623.40]  Who is your programming hero?
[3624.58 --> 3626.90]  This kind of changes on a frequent basis.
[3627.44 --> 3627.74]  Uh.
[3628.46 --> 3630.50]  I always look up to a good friend of mine.
[3630.74 --> 3631.40]  Charles Lowell.
[3631.48 --> 3631.96]  Cowboy D.
[3632.04 --> 3632.46]  On Twitter.
[3633.26 --> 3633.76]  But lately.
[3633.88 --> 3634.08]  My.
[3634.18 --> 3635.04]  My programming hero.
[3635.14 --> 3635.80]  Has really been.
[3636.32 --> 3637.08]  My girlfriend.
[3637.66 --> 3638.74]  Who is a.
[3638.74 --> 3639.30]  A budding.
[3639.70 --> 3640.10]  Female.
[3640.38 --> 3640.74]  Learning.
[3640.88 --> 3641.24]  Developer.
[3641.24 --> 3641.64]  developer.
[3642.10 --> 3643.38]  About six months ago.
[3643.62 --> 3643.80]  She.
[3644.48 --> 3645.98]  Left her cushy support job.
[3646.20 --> 3646.94]  And leap.
[3647.26 --> 3648.06]  Did a leap of faith.
[3648.18 --> 3649.46]  And she's learning to be a developer.
[3649.86 --> 3650.02]  So.
[3650.20 --> 3650.40]  Nice.
[3650.60 --> 3650.76]  You know.
[3650.80 --> 3650.92]  That.
[3651.10 --> 3651.70]  That really.
[3652.26 --> 3653.40]  It's fun to see her.
[3653.88 --> 3654.78]  Learn and grow.
[3655.24 --> 3655.56]  And.
[3656.08 --> 3656.66]  To do it at.
[3656.78 --> 3657.38]  At kind of a.
[3657.38 --> 3657.82]  A later.
[3658.30 --> 3658.64]  Age.
[3659.36 --> 3659.76]  As well.
[3660.10 --> 3660.32]  You know.
[3660.32 --> 3661.62]  When you already have an established career.
[3662.82 --> 3663.40]  And the risk.
[3663.50 --> 3663.64]  You know.
[3664.14 --> 3664.36]  Yeah.
[3664.36 --> 3664.68]  It's.
[3664.76 --> 3665.40]  It's a big deal.
[3665.66 --> 3665.92]  So.
[3667.48 --> 3668.24]  I'm kind of.
[3668.38 --> 3668.70]  In awe.
[3668.98 --> 3669.10]  And.
[3669.36 --> 3670.28]  A bit of a hero to me.
[3670.50 --> 3670.64]  So.
[3671.24 --> 3672.10]  Gotta give a shout out there.
[3672.22 --> 3672.74]  Awesome man.
[3673.08 --> 3674.12]  Make sure she listens to this.
[3674.14 --> 3675.34]  So you get them brownie points too.
[3675.40 --> 3676.58]  Don't miss out on them brownie points.
[3677.88 --> 3678.42]  Next up.
[3678.48 --> 3679.14]  And a new question.
[3679.68 --> 3680.60]  Trying to share the.
[3680.60 --> 3681.60]  The podcast love.
[3681.64 --> 3682.14]  A little bit.
[3682.38 --> 3682.64]  And.
[3682.96 --> 3683.88]  Give some shout outs.
[3683.96 --> 3684.76]  To different podcasts.
[3684.88 --> 3685.68]  Out around the ecosystem.
[3685.92 --> 3686.06]  So.
[3687.32 --> 3688.34]  You're a podcast listener.
[3688.44 --> 3688.64]  Please.
[3688.76 --> 3689.18]  If you would.
[3689.24 --> 3689.60]  Share us.
[3689.74 --> 3690.14]  Share with us.
[3690.14 --> 3691.56]  A couple of your favorite podcasts.
[3693.26 --> 3693.62]  I'm.
[3693.62 --> 3694.30]  I'm a big fan.
[3694.30 --> 3695.14]  Of the JRE.
[3695.82 --> 3697.06]  The Joe Rogan experience.
[3698.32 --> 3698.92]  If you guys.
[3699.02 --> 3699.72]  Haven't heard of it.
[3699.72 --> 3701.22]  Joe Rogan.
[3701.54 --> 3701.74]  Yes.
[3701.84 --> 3702.78]  The one and only.
[3702.78 --> 3703.92]  Fear factor host.
[3704.12 --> 3705.46]  From way back in the day.
[3706.18 --> 3707.92]  He has one of the most popular.
[3708.90 --> 3709.62]  Podcasts.
[3710.20 --> 3710.92]  In the world.
[3711.28 --> 3711.52]  And.
[3712.10 --> 3712.42]  You know.
[3712.58 --> 3713.18]  Strap in.
[3713.32 --> 3714.54]  It's three hours a piece.
[3714.76 --> 3714.88]  But.
[3715.96 --> 3716.66]  I don't know.
[3716.78 --> 3717.04]  I.
[3717.18 --> 3717.58]  I enjoy.
[3717.74 --> 3719.16]  I think we should do the changelon for three hours.
[3719.16 --> 3719.76]  I don't know what.
[3719.76 --> 3721.36]  That's a long experience right there.
[3721.56 --> 3722.44]  It's a long experience.
[3723.90 --> 3724.58]  What else?
[3724.58 --> 3725.14]  Any other.
[3725.30 --> 3726.52]  Any other shows you got on your.
[3727.14 --> 3728.80]  I listen to you guys of course.
[3729.04 --> 3730.58]  I'll listen to the front side podcast.
[3732.18 --> 3734.34]  Like front end development or design or what's that?
[3734.76 --> 3735.42]  The front side.
[3735.58 --> 3735.70]  It's.
[3735.76 --> 3736.80]  It's Charles's little.
[3736.94 --> 3737.48]  Just personal.
[3738.04 --> 3738.28]  Thing.
[3738.38 --> 3738.56]  Cool.
[3738.56 --> 3742.86]  I listen to Ruby Rogues and JavaScript Jabber.
[3743.80 --> 3744.24]  Sometimes.
[3744.64 --> 3745.54]  I still.
[3746.18 --> 3747.56]  Tune in to Herding Code.
[3747.72 --> 3748.30]  Which is like a.
[3748.30 --> 3748.90]  A dot net.
[3749.26 --> 3749.92]  Focused one.
[3750.64 --> 3752.50]  I'll listen to the Ruby five by five.
[3753.26 --> 3754.50]  You mean Ruby five.
[3754.58 --> 3755.16]  Ruby five.
[3755.32 --> 3755.98]  The Ruby five.
[3756.12 --> 3756.54]  I by five.
[3756.72 --> 3758.56]  You mix Ruby five by five.
[3758.68 --> 3759.14]  And I was like.
[3759.22 --> 3759.42]  Yeah.
[3759.88 --> 3760.86]  Is that a new one?
[3761.04 --> 3761.60]  Could be a new one.
[3761.70 --> 3761.86]  No.
[3762.90 --> 3763.66]  Ruby five.
[3764.52 --> 3764.98]  Then you got.
[3765.20 --> 3766.82]  You also have a Ruby.
[3767.60 --> 3768.54]  Ruby on Rails podcast.
[3768.56 --> 3769.60]  On five by five.
[3769.76 --> 3769.86]  So.
[3770.14 --> 3770.40]  That's right.
[3770.72 --> 3772.02]  You can probably add that one to your list too.
[3772.16 --> 3772.68]  Like that show.
[3774.34 --> 3774.88]  You know.
[3775.00 --> 3776.16]  We obviously love podcasts.
[3776.28 --> 3777.70]  We appreciate you listening to our show.
[3777.76 --> 3778.68]  That's totally cool.
[3779.64 --> 3780.90]  And I guess to wrap up the show.
[3781.06 --> 3781.08]  We.
[3781.24 --> 3781.58]  You know.
[3781.80 --> 3782.72]  It's been great talking to you.
[3782.76 --> 3783.48]  I know we saw you.
[3784.00 --> 3784.66]  Back at.
[3784.94 --> 3785.72]  Keeper be weird.
[3785.82 --> 3786.28]  In Austin.
[3786.80 --> 3787.28]  What was that?
[3787.84 --> 3788.20]  October.
[3788.32 --> 3788.58]  Jared.
[3788.68 --> 3789.16]  We were there.
[3789.54 --> 3789.90]  October.
[3790.20 --> 3790.28]  Yeah.
[3790.38 --> 3790.70]  October.
[3790.98 --> 3791.34]  September.
[3791.60 --> 3791.96]  October.
[3792.68 --> 3793.72]  That was good times.
[3793.82 --> 3794.48]  That was good times.
[3794.94 --> 3796.64]  We do have some pending video.
[3796.64 --> 3797.40]  We shot there.
[3797.40 --> 3799.10]  And you'll get to see Ryan's.
[3799.36 --> 3800.82]  Awesome face on the video.
[3801.48 --> 3802.44]  Sharing once again.
[3802.52 --> 3803.66]  His other programming heroes.
[3803.76 --> 3803.98]  Not.
[3804.36 --> 3805.64]  You didn't mention your girlfriend in that one.
[3805.72 --> 3806.16]  But maybe.
[3806.28 --> 3807.04]  Maybe she wasn't your hero.
[3807.12 --> 3807.72]  Keeping it fresh.
[3808.38 --> 3809.04]  Keeping it fresh.
[3809.86 --> 3810.08]  Yeah.
[3810.14 --> 3811.76]  Ryan has been great having you on the show.
[3811.86 --> 3812.22]  I know.
[3812.22 --> 3815.28]  We're definitely excited about where you're going with this.
[3815.50 --> 3816.10]  And you know.
[3816.36 --> 3817.34]  It's fun to see.
[3817.76 --> 3819.02]  We've seen this time and time again.
[3819.12 --> 3819.92]  You mentioned Mike Parham.
[3820.08 --> 3820.94]  And others.
[3821.42 --> 3822.40]  Tim Caswell.
[3823.14 --> 3825.26]  The list goes on of people that have been on the show.
[3825.42 --> 3825.84]  That you know.
[3825.84 --> 3827.14]  Have done something in open source.
[3827.34 --> 3829.74]  And found a way to make it free and open source.
[3829.84 --> 3831.44]  But still make a business out of it.
[3831.84 --> 3832.68]  And support it.
[3832.72 --> 3833.24]  And we think that's.
[3833.24 --> 3834.20]  That's always a great one.
[3834.54 --> 3836.42]  And we want to highlight that one.
[3836.50 --> 3837.74]  That when we get a chance to do so.
[3838.32 --> 3838.72]  Yeah.
[3838.72 --> 3841.20]  I really appreciate you guys letting me on.
[3841.44 --> 3842.44]  One thing I want to say too.
[3842.54 --> 3843.90]  As I close with this.
[3844.66 --> 3845.90]  It's a two part thing.
[3846.42 --> 3846.62]  One.
[3846.68 --> 3848.12]  To promote our issues.
[3848.50 --> 3848.80]  Or sorry.
[3848.90 --> 3850.52]  Our ping issues on GitHub.
[3850.78 --> 3851.18]  And two.
[3851.28 --> 3852.26]  Just to kind of.
[3852.26 --> 3854.72]  Maybe get a shout out from listeners of the show.
[3854.80 --> 3856.24]  That use Hubboard.
[3856.36 --> 3858.08]  If you are a user of Hubboard.
[3858.52 --> 3859.54]  Or if you love this show.
[3859.54 --> 3861.82]  Go on to our GitHub issues.
[3862.66 --> 3864.14]  It's github.com of course.
[3864.38 --> 3865.98]  Slash the changelog slash ping.
[3866.68 --> 3867.68]  And submit a new issue.
[3868.38 --> 3869.56]  If there isn't one yet.
[3869.60 --> 3870.62]  And if there already is one.
[3870.68 --> 3871.76]  Just go and throw a comment on there.
[3871.94 --> 3873.28]  And give a shout out back to Ryan.
[3873.36 --> 3875.50]  About just using Hubboard.
[3875.66 --> 3876.86]  And what you thought of this show.
[3876.92 --> 3877.26]  Or whatever.
[3877.34 --> 3878.18]  That'd be super cool.
[3878.26 --> 3880.32]  To just kind of see who listens to this show.
[3880.38 --> 3881.44]  And see who's using Hubboard.
[3881.86 --> 3883.36]  And try to connect the dots a bit.
[3883.50 --> 3886.90]  But we do have some pretty awesome sponsors.
[3886.90 --> 3888.90]  That helped make this show possible.
[3889.52 --> 3890.30]  We got CodeShip.
[3890.44 --> 3891.48]  Definitely love CodeShip.
[3891.56 --> 3893.42]  Who doesn't want to have tested code in production?
[3893.58 --> 3893.64]  Right?
[3893.66 --> 3895.02]  That's the name of the game.
[3895.16 --> 3895.30]  Right?
[3896.14 --> 3896.54]  Rackspace.
[3896.80 --> 3897.62]  And TopTowel.
[3898.08 --> 3899.92]  Keeping us on the airwaves.
[3900.02 --> 3900.30]  Yes.
[3900.42 --> 3900.82]  Rackspace.
[3901.18 --> 3901.56]  CodeShip.
[3901.66 --> 3902.32]  And TopTowel.
[3902.74 --> 3903.60]  Friends of the show.
[3903.92 --> 3904.88]  They support us.
[3904.92 --> 3905.56]  They love us.
[3905.70 --> 3908.76]  And we hope that you love them too.
[3908.92 --> 3911.22]  But that's it for this week of the change.
[3911.28 --> 3912.22]  We'll be back next week.
[3912.22 --> 3913.14]  But for now, let's say goodbye.
[3913.14 --> 3913.20]  Goodbye.
[3914.40 --> 3915.44]  Goodbye.
[3915.44 --> 3945.42]  Outro Music

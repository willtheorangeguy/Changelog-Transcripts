[0.00 --> 13.48]  Welcome back everyone, this is The Change Log and I'm your host Adam Stikowiak.
[13.58 --> 18.54]  This is episode 144 and today we're talking to Ilya Grigorik.
[19.14 --> 22.76]  Ilya is a so-professed internet plumber as you'll hear on the show today.
[23.30 --> 27.14]  He works at Google and he basically makes the internet faster and much more of course
[27.14 --> 29.56]  for those who are fans of Ilya's work.
[30.34 --> 34.66]  Ilya has a side project called GitHub Archive which we took some interest in because we
[34.66 --> 38.30]  wanted to start shipping a daily email, nightly as a matter of fact.
[38.66 --> 41.72]  I'm going to break some news real quick because we're going to tell you later in this episode
[41.72 --> 44.22]  but I have to tell you now because I want you to sign up this email.
[44.72 --> 49.06]  Stop the show, go to thechangelog.com slash nightly and sign up right now.
[49.66 --> 52.92]  It's an email we're shipping now called changelog nightly as you can tell from the URL.
[52.92 --> 59.52]  And this email unearths the hottest repos on GitHub every single night and drops them
[59.52 --> 60.14]  in your inbox.
[60.38 --> 61.70]  It's going to be awesome.
[61.92 --> 62.54]  You're going to love it.
[62.98 --> 67.66]  We have some awesome sponsors for today's show, CodeShip, TopTile, and CodeSchool.
[68.00 --> 72.14]  We'll tell you a bit more about CodeSchool and TopTile later in the show but our friends
[72.14 --> 77.54]  at CodeShip, they have released a brand new feature called Parallel CI.
[77.90 --> 82.16]  If you want to get faster tests from your builds, you've got to run your builds in parallel.
[82.16 --> 86.58]  They recently shipped Parallel CI and now you can split up your test commands into up to
[86.58 --> 89.26]  10 pipelines, 10 test pipelines.
[89.48 --> 93.90]  This enables you to run your test suite in parallel and drastically reduce the time it
[93.90 --> 95.54]  takes to run your builds.
[95.90 --> 97.62]  They integrate with GitHub and Bitbucket.
[97.98 --> 102.48]  You can deploy your code to cloud services like Heroku or AWS and much more.
[102.90 --> 106.40]  And you can get started today by trying out their free plan which includes 100 builds a
[106.40 --> 108.52]  month and 5 private projects.
[108.52 --> 115.94]  Or you can also use our offer code, the ChangeLawPodcast, to get a 20% discount on any plan you choose
[115.94 --> 116.66]  for three months.
[117.02 --> 119.70]  Head to CodeShip.com slash the ChangeLaw to get started.
[119.98 --> 121.44]  And now, on to the show.
[121.44 --> 125.16]  All right, everybody, we're back.
[125.24 --> 126.88]  We've got Ilya Grigork joining us today.
[127.00 --> 129.38]  Ilya, you've been on the show before.
[129.60 --> 131.64]  Episode 55, if we go back in time.
[132.60 --> 135.36]  Back when Gwyn was around and that was an awesome show.
[135.42 --> 138.82]  You were talking about Goliath and Event Machine and other fun stuff.
[138.92 --> 140.10]  So welcome back to the show, man.
[140.20 --> 140.62]  How are you?
[141.34 --> 142.02]  I'm doing great.
[142.12 --> 143.40]  Thanks for the invitation.
[143.80 --> 145.02]  And yeah, it's been a while.
[145.02 --> 146.92]  I think that episode was back in 2011.
[148.72 --> 153.10]  It's like we were laughing before the show how forever ago that was, basically.
[153.68 --> 155.32]  And that's just crazy.
[155.64 --> 157.56]  Yeah, Speedy was a brand new thing back then.
[157.68 --> 160.40]  And now it's been completely replaced, right?
[160.40 --> 160.42]  That's right, actually.
[160.42 --> 165.14]  As of today or yesterday, the new HTTP2 stuff is now official.
[165.14 --> 170.46]  So we went from this kind of experimental thing that a couple of engineers at Google started
[170.46 --> 174.58]  to something that's out in the wild and ready to be deployed.
[174.84 --> 175.48]  It's pretty amazing.
[176.54 --> 179.46]  And as you can hear, we also have Jared Santo on the call as well.
[179.52 --> 180.34]  So Jared, say what's up.
[180.72 --> 181.12]  What's up?
[181.32 --> 181.88]  What's up?
[182.82 --> 187.18]  So Ilya, this is sort of a two-part show, right?
[187.22 --> 190.22]  We got sort of an announcement from us, which we'll talk about later.
[190.22 --> 195.08]  But then we have this awesome project that you started, GitHub Archive, and that kind
[195.08 --> 197.92]  of tees off of Google's BigQuery project.
[198.50 --> 202.06]  You've been on the show before, but since it's been a while, back then you were a founder
[202.06 --> 205.12]  and CTO of PostRank, which has since been acquired by Google.
[205.68 --> 209.14]  And you now work at Google, and it's been all that time since then.
[209.34 --> 213.76]  How do you introduce yourself now whenever you're on a stage or saying hello to people?
[213.76 --> 217.84]  So nowadays, within Google, I basically work as an internet plumber.
[217.84 --> 222.74]  And my job is more or less to figure out how to make the internet faster.
[223.38 --> 231.08]  That's related to spec work for things like Google Chrome, so open standards, also things
[231.08 --> 232.90]  like HTTP2 and all the rest.
[233.22 --> 236.78]  So trying to figure out how to make Chrome faster, how to make Google products faster,
[237.06 --> 243.06]  because we know that speed helps user retention and just leads to happier users, and also just
[243.06 --> 244.32]  make internet faster as a whole.
[245.18 --> 246.44]  So it's been a pretty fun gig.
[247.84 --> 250.72]  I like the name, or the title at least, internet plumber.
[251.16 --> 256.62]  It's a good description of kind of the dirty work that you actually have to do to make
[256.62 --> 257.08]  it all work.
[257.28 --> 257.76]  Yep, yep.
[257.92 --> 258.80]  Someone's got to do it, right?
[259.40 --> 261.72]  And how big is your team that you work with there at Google?
[262.20 --> 263.02]  That's a good question.
[263.20 --> 268.66]  It's actually a big distributed effort, as you can imagine, because every product within
[268.66 --> 270.72]  Google is focused on speed.
[270.72 --> 276.20]  So I work, kind of collaborate with a lot of different teams within Google, and then even
[276.20 --> 277.40]  outside of Google as well.
[277.46 --> 282.88]  So we work with mobile carriers, because mobile is becoming so important, and everything's migrating
[282.88 --> 283.24]  there.
[283.80 --> 287.78]  Other vendors, Microsoft, Mozilla, Apple, and all the rest.
[287.78 --> 294.04]  So it's hard to say what the team is, because we don't have just a strictly unified team,
[294.14 --> 295.40]  but it's hundreds of people.
[296.96 --> 299.56]  So do you work in an office, or are you remote?
[299.62 --> 303.78]  I work in an office, but I do find myself kind of jumping between offices, depending on
[303.78 --> 305.04]  where I have a lot of meetings.
[305.04 --> 308.84]  But my day-to-day is mostly in Mountain View, California.
[310.60 --> 310.70]  Gotcha.
[311.88 --> 312.40]  Well, cool.
[312.64 --> 316.96]  Didn't you live not in San Francisco before you were acquired?
[316.98 --> 317.24]  That's right.
[317.30 --> 319.58]  Yeah, we were actually in Waterloo, Canada.
[321.00 --> 321.48]  All right.
[321.50 --> 322.94]  Then we moved to sunny California.
[324.48 --> 324.68]  All right.
[324.74 --> 325.46]  Must be better, right?
[325.50 --> 329.26]  So you're not dealing with the whole winter apocalypse, or what is it called over there?
[329.28 --> 329.80]  Yeah, the snowpocalypse.
[330.88 --> 332.16]  Snowpocalypse, yes.
[332.46 --> 333.86]  I feel bad for the people on the East Coast.
[333.86 --> 338.22]  Because here in sunny Texas, it's just around 55 degrees today or something.
[338.34 --> 338.46]  Yep.
[338.58 --> 339.12]  Can't complain.
[340.72 --> 344.44]  Well, I got sun, but I also have like nine degree sun.
[344.82 --> 345.62]  So it's not exactly...
[345.62 --> 346.76]  I guess I can complain.
[348.26 --> 350.80]  Not as much as them on the East Coast, but I can still complain.
[351.28 --> 355.04]  So maybe just to paint a little bit of the history for people, too, to kind of let them
[355.04 --> 356.38]  know which Ilya we're talking to.
[356.40 --> 357.56]  I don't think there's that many out there.
[358.80 --> 362.08]  VimGolf, GitHub Archive, you were a Ruby Hero in 2008.
[362.08 --> 364.24]  You started PostRank.
[364.34 --> 369.08]  Can you kind of give a primer of what PostRank was prior to the acquisition in Google and
[369.08 --> 372.16]  sort of what sort of made you this internet plumber you are today?
[372.60 --> 372.70]  Yeah.
[372.80 --> 376.76]  The PostRank work was actually, I'm going to say, mostly unrelated to the work that I'm
[376.76 --> 377.32]  doing before.
[377.32 --> 386.54]  But the idea behind PostRank was to help measure the impact of just social advertising on the
[386.54 --> 386.74]  web.
[387.24 --> 391.54]  And by advertising, like I share a link to an open source project and we want to be able
[391.54 --> 394.40]  to figure out what did that yield?
[394.70 --> 398.12]  Was that a good share in the sense that did a lot of people click on it?
[398.74 --> 400.02]  Whom should you approach?
[400.24 --> 404.86]  Or where should you advertise to kind of make the most of your advertising budget?
[404.86 --> 410.38]  So we built a collection of tools for marketers, advertisers, and the rest to kind of help
[410.38 --> 414.60]  them facilitate that whole end-to-end cycle of, you want to invest money into social and
[414.60 --> 416.34]  what is the return on investment?
[416.94 --> 421.24]  And then I guess that was interesting to Google, who at the time was really kind of expanding
[421.24 --> 422.38]  their social strategy.
[423.14 --> 428.84]  So we ended up there and I spent about a year building and rebuilding some of the products
[428.84 --> 429.88]  that we build within PostRank.
[429.88 --> 436.20]  And then jumped to kind of this web performance work, which has always been my passion in the
[436.20 --> 436.54]  background.
[436.90 --> 441.12]  The last episode that we did with you guys with Goliath was actually centered around that.
[441.22 --> 445.34]  We wrote our own HTTP server because we found that the performance of some of the existing
[445.34 --> 446.98]  servers just wasn't up to par.
[447.78 --> 451.92]  So I've always kind of played that plumber role, perhaps in the background as an engineer.
[452.22 --> 457.42]  And then when I got the opportunity to actually focus on it full-time, I decided to jump on it.
[457.42 --> 463.82]  But as Adam mentioned, you are a Ruby hero and many people probably remember you from
[463.82 --> 469.54]  igvita.com, your blog that you wrote on very commonly back then.
[470.04 --> 473.56]  Curious if you're still slinging any Ruby inside Google or if you've switched tool sets.
[473.66 --> 476.90]  I am, but perhaps not kind of day-to-day production projects.
[477.30 --> 481.80]  So I still have open source projects, certainly a lot of kind of my day-to-day work for, you
[481.80 --> 484.00]  know, I need a script for this, I need to automate something like that.
[484.06 --> 484.74]  I still use Ruby.
[484.74 --> 486.92]  It's my default language to date.
[487.70 --> 492.54]  Probably the most recent project that I worked on was actually the HTTP2 Ruby gem.
[493.16 --> 497.40]  So it's a pure Ruby implementation of the full HTTP protocol, HTTP2 protocol.
[497.92 --> 501.10]  So that was fun, just kind of roll up my sleeves and work on that.
[501.32 --> 505.86]  And I should also mention that I got some great contributions from a number of people on
[505.86 --> 508.22]  GitHub, from the Tokyo community in particular.
[508.56 --> 510.60]  So they've been helping out quite a bit.
[510.60 --> 511.94]  So it was really good.
[512.06 --> 518.12]  And I actually went to Tokyo last year to talk at HTTP2 events.
[518.22 --> 521.98]  So I met a lot of the Rubyists there that were also doing HTTP2.
[522.12 --> 523.10]  So that was really good.
[523.92 --> 524.20]  Awesome, man.
[524.26 --> 529.08]  Well, we're here today to talk about a specific project of yours, one that had caught our radar
[529.08 --> 533.78]  and that I was quite fond of for some time, which is your GitHub Archive project,
[534.00 --> 535.00]  GitHubarchive.org.
[535.00 --> 538.54]  Tell us about that and what it is and kind of where you got the idea for it.
[538.62 --> 538.72]  Sure.
[538.90 --> 540.36]  So this is a fun one.
[540.46 --> 544.48]  And I think as most every open source project, it starts with a personal itch.
[545.32 --> 549.12]  And my personal itch was, I love open source.
[549.30 --> 550.66]  I love following open source.
[550.86 --> 555.10]  And I'd like to keep on top of what are the interesting projects that are coming up, being
[555.10 --> 558.16]  released, what are the new issues, so on and so forth.
[558.48 --> 562.92]  So back in the early days of GitHub, I would just follow a lot of people, right?
[562.92 --> 566.88]  Once you follow kind of the right people in any particular community, you just observe
[566.88 --> 569.62]  like what they star or what they comment on and all the rest.
[570.44 --> 572.38]  And that worked well for a while.
[573.30 --> 577.78]  But with time, as more and more projects and more and more people joined GitHub, I found
[577.78 --> 582.72]  that, and I was subscribing to like a thousand plus projects and people, that my stream was
[582.72 --> 584.04]  actually just being overwhelmed.
[584.66 --> 590.64]  Like I went from being able to check my stream on GitHub.com for like what are the new events
[590.64 --> 594.76]  once every couple of days to, I had to check it once a day because they had a limit, I
[594.76 --> 596.00]  think it was like 500 events.
[596.52 --> 597.82]  And it would just kind of scroll off the bottom.
[598.06 --> 599.12]  So I couldn't catch up.
[599.44 --> 601.68]  And then finally, it was like every half a day, I would have to check it.
[601.86 --> 603.38]  And clearly that wasn't scaling.
[604.12 --> 605.74]  So that was a problem.
[605.82 --> 608.82]  And I figured like, hey, I should figure out how to solve this problem.
[609.02 --> 612.52]  I specifically wanted to just solve that problem for myself.
[612.52 --> 618.08]  So I started looking around and realized that GitHub actually provides this API where they
[618.08 --> 619.28]  show you the latest activity.
[619.60 --> 624.60]  So this is like somebody opened a pull request, somebody closed an issue, just basically anything
[624.60 --> 625.14]  and everything.
[625.64 --> 628.76]  And if you pull that API, you can actually get the live stream.
[630.08 --> 634.48]  So based on that, I said, okay, well, fine, I'll just write a crawler that will just basically
[634.48 --> 636.62]  sit there in the loop and just log all of that data.
[636.72 --> 640.94]  And then once I have the data, I can mash it off and answer my question that I actually
[640.94 --> 641.36]  need to do.
[641.56 --> 644.06]  So, you know, nothing like a good yak shave.
[646.26 --> 650.08]  So that was basically the inception of GitHub Archive.
[650.38 --> 655.44]  I just wrote a little Ruby crawler that sits there and just collects this data, logs it
[655.44 --> 661.12]  into archives, hourly archives, which I store all on cloud storage.
[661.24 --> 663.96]  At the time it was S3, then I moved it to Google Cloud Storage.
[664.68 --> 670.42]  And I think I started that back in March of 2012 or 2013.
[670.42 --> 671.44]  One of those years.
[672.44 --> 673.58]  I think it was 2013.
[674.48 --> 677.28]  And ever since, it's just been logging those hourly archives.
[677.90 --> 684.80]  And then based on that data, I tried to figure out like, okay, now you have those JSON payloads.
[685.64 --> 687.24]  What can you do with it?
[687.44 --> 687.60]  Right?
[687.68 --> 692.32]  Because now you actually have a ton of data, which is in itself kind of a problem.
[692.68 --> 695.20]  And processing all of that may take some time.
[695.20 --> 701.88]  And Google at the time just announced BigQuery, which was a project that was actually an internal
[701.88 --> 705.18]  project called Dremel within Google, which is incredibly popular.
[705.18 --> 709.22]  And the idea there is you can write kind of SQL-like.
[709.80 --> 713.04]  You have a SQL-like syntax that you can write.
[713.48 --> 717.82]  And under the hood, it's actually implemented as a MapReduce job.
[718.74 --> 723.66]  So you write SQL, it gets translated to MapReduce, and you can run it across massive data sets.
[723.66 --> 730.16]  And it returns really fast, which was a plus, of course, because you want to have that sort of kind of interactive
[730.16 --> 731.50]  querying capabilities.
[732.72 --> 735.22]  And that just became available as BigQuery.
[735.52 --> 737.82]  So I figured like, hey, this seems like a perfect fit.
[737.82 --> 746.00]  So if I just push all of this data into BigQuery, I get the ability to kind of query the data really easily and in a fast way.
[746.66 --> 753.26]  And two, that data actually becomes, I can make it as a public data set, such that other people can come and write
[753.26 --> 755.72]  queries against it without having to do the import.
[756.78 --> 760.00]  And the import part turns out to be kind of significant.
[760.14 --> 764.84]  I think we'll talk about it later, because at the time, there were some restrictions on how I could store the data.
[764.84 --> 773.74]  But the gist of it is, write a crawler, log all the data, import the data into BigQuery.
[774.44 --> 778.08]  And then with BigQuery, you have this data set that's easy to queryable.
[778.24 --> 784.46]  And then finally, after doing all the yak shaving, I wrote a simple Ruby script that just queried BigQuery once a day
[784.46 --> 787.80]  and sent me two things.
[788.16 --> 793.32]  The top 10 repos that were open source within the last 24 hours,
[793.32 --> 795.76]  and top 10 by number of stars received.
[796.46 --> 798.36]  So just which of the repos that received the most intention.
[799.06 --> 802.94]  And then which repos that are not new, but received the most stars.
[804.52 --> 808.08]  And that became a newsletter that I also opened out to other people.
[808.38 --> 810.38]  And approximately 1,000 people have signed up for it.
[810.78 --> 815.46]  And a funny thing, I actually, last year, I got a report from MailChimp,
[815.58 --> 818.26]  which is the service that I was using to do the delivery.
[818.26 --> 820.20]  And I was just looking at it before the show.
[821.20 --> 826.80]  And it said that the average open rate for those emails, for those campaigns, was about 40%,
[826.80 --> 829.04]  which is massive, right?
[829.28 --> 831.16]  Compared to the rest of the industry.
[831.40 --> 835.22]  So it was not only were people signing up, they were actually opening the emails.
[835.68 --> 839.18]  And the click-through rate for the links sent in there was about 15%,
[839.18 --> 844.40]  which is about 10 times higher than your industry average.
[844.40 --> 846.34]  So it worked.
[848.50 --> 850.02]  It worked. I like that.
[850.38 --> 855.40]  While it worked on me, I was a subscriber, which is kind of how I came across the whole thing.
[855.48 --> 859.20]  I can't remember who keyed me on to the newsletter immediately, or originally.
[860.22 --> 862.74]  But I had been getting it for months.
[863.24 --> 867.36]  And you were scratching your own itch, but you scratched an itch that Adam and I have
[867.36 --> 871.70]  around these parts, trying to keep up with open source, is to find the new repos.
[871.70 --> 879.08]  And yeah, every night, I think coming in, something about daily emails, where it's like,
[879.94 --> 882.52]  eventually you kind of get sick of them, because you're like, yeah, here it is again.
[882.62 --> 884.40]  Every single day, old faithful.
[885.42 --> 889.88]  But more often than not, there's good stuff, there's gems sitting in there.
[890.06 --> 891.60]  So it was very valuable.
[891.72 --> 892.34]  It definitely worked.
[892.34 --> 897.62]  It's interesting that it kind of came, you know, I assume because you're at Google,
[897.72 --> 902.36]  and BigQuery is a Google product, that it was kind of worked the other way around,
[902.52 --> 905.44]  where it was like, here they have BigQuery, and maybe they asked some of their employees
[905.44 --> 908.60]  to use this thing, to have some good use cases.
[908.76 --> 912.62]  But it's kind of interesting that it was kind of organic, the way that you ended up using BigQuery.
[912.62 --> 917.76]  Yeah, it was actually pretty lucky timing, because at the time, I wasn't even aware that the product
[917.76 --> 919.56]  was going to be released.
[919.66 --> 922.34]  I was just kind of struggling to figure out a way how to do this.
[922.88 --> 927.62]  So either I had to write just my own processing logic to go through all the archives,
[927.82 --> 930.98]  but then they announced BigQuery, and it was like, oh, yeah, I heard of this thing called Dremel,
[931.08 --> 933.06]  and Google was very popular, so let me just give it a try.
[933.22 --> 936.50]  And it turns out that was actually probably one of the best decisions I've made,
[936.50 --> 943.58]  just because aside from having the ability to do these fast queries,
[943.86 --> 947.94]  it opened it up to anybody and everybody to just run arbitrary queries.
[948.24 --> 951.58]  And one of the benefits of BigQuery is that actually gives you a free quota.
[952.08 --> 957.56]  So you do need to have a Google account, but once you sign in, it's a webpage
[957.56 --> 961.62]  where you just type in your SQL query, and you can ask it any question you want.
[961.62 --> 968.30]  So if you are curious about what is the top start repo for, I don't know,
[968.56 --> 972.90]  for a particular user, you can just write a query and get an answer to that.
[972.98 --> 977.46]  Or if you're interested in what are the top repos that have the most issues open
[977.46 --> 981.46]  that are Ruby repos, you can ask that too, and you get immediate answers.
[981.84 --> 983.98]  And that turned out to be very popular with a lot of people,
[984.10 --> 987.68]  because it just kind of feels very easy to approach and start asking these questions.
[987.68 --> 992.68]  So we've seen a lot of kind of really interesting projects built up around it,
[993.28 --> 996.98]  even though originally it was just meant to solve this kind of very narrow problem that I had.
[997.86 --> 1002.96]  Do you have any further instances for us of people using the GitHub Archive BigQuery
[1002.96 --> 1004.22]  and making cool stuff with it?
[1004.22 --> 1005.40]  Oh yeah, oh man, there's so many.
[1006.20 --> 1011.64]  So we actually worked with, when I started this, I also pinged GitHub crew
[1011.64 --> 1014.98]  to make sure that this is all good, and I'm logging this data,
[1015.08 --> 1016.62]  and they don't have any kind of issues with it.
[1016.62 --> 1020.70]  And to their credit, not only did they say it was all great,
[1020.84 --> 1023.78]  but they also helped me to get the word out there.
[1024.12 --> 1027.22]  So actually, Brian, who's on their marketing team,
[1027.76 --> 1032.22]  has organized the big data challenge, the GitHub data challenge,
[1032.90 --> 1037.08]  for the last three years, where they have a prize or a set of prizes at the end.
[1037.16 --> 1040.18]  And basically the idea is, like, here's the data, use GitHub Archive,
[1040.44 --> 1043.80]  or any of the data if you want, and just build an interesting visualization
[1043.80 --> 1047.96]  or something that kind of extracts some interesting insights out of the data.
[1047.96 --> 1052.48]  So if you guys go to githubarchive.org and you scroll down to the bottom,
[1052.60 --> 1055.40]  there's actually a collection of links to various projects
[1055.40 --> 1059.62]  and also the blog posts from GitHub where they show the winners.
[1060.24 --> 1063.22]  And some of my favorites, I'll just, I guess, pick out a few.
[1064.32 --> 1068.04]  There was one project that was the open source report card,
[1068.04 --> 1070.64]  and the idea there was you type in a username,
[1071.10 --> 1073.60]  and the report card would be for a particular user.
[1073.72 --> 1075.90]  So it would aggregate all of the repos that you worked on
[1075.90 --> 1078.24]  and kind of figure out which languages you contribute to,
[1078.32 --> 1081.40]  what type of commits, like do you typically open issues,
[1081.56 --> 1084.82]  you do fix issues, do you write codes, do you kind of discuss more,
[1085.52 --> 1089.92]  and give you kind of a nice description of the type of work that you do on GitHub.
[1090.08 --> 1090.92]  So that was kind of cool.
[1092.28 --> 1096.12]  Another project was just showing the geographic distribution.
[1096.12 --> 1099.40]  So you pick a project or even a language, and you can say,
[1099.68 --> 1101.48]  like, where are my contributors coming from?
[1101.56 --> 1105.10]  Are they from U.S., Europe, New Zealand?
[1105.58 --> 1109.40]  Just show me a map, which is kind of like a simple, intuitive thing to ask,
[1109.48 --> 1112.32]  but it's something that GitHub doesn't provide by itself.
[1113.14 --> 1116.18]  But here you just had this kind of third-party tool fill in that gap.
[1117.70 --> 1120.44]  Another one that's kind of, and all these projects approach
[1120.44 --> 1123.18]  the data from a different angle.
[1123.18 --> 1125.68]  So the one was on users, one was on projects,
[1126.12 --> 1129.18]  GitHub is an interesting one, so github.com.
[1129.90 --> 1132.78]  It actually provides a really cool visualization
[1132.78 --> 1135.64]  for comparing programming languages.
[1136.54 --> 1139.36]  So you can see, for example, that if you select Ruby,
[1140.10 --> 1145.16]  you can see where it is ranked in terms of number of pull requests
[1145.16 --> 1149.58]  or issues or other things on GitHub.
[1149.58 --> 1153.24]  So not surprisingly, today, JavaScript is at the top
[1153.24 --> 1154.94]  in terms of the number of just commits.
[1156.64 --> 1159.08]  Yeah, you know, this one actually made the rounds, I think.
[1159.18 --> 1161.48]  It was either last week or even maybe just Monday.
[1161.96 --> 1164.06]  This githut, that's G-I-T-H-U-T.
[1165.32 --> 1168.20]  Somebody had posted to some, whether it was Hacker News or something,
[1168.36 --> 1171.16]  about the top languages of the year,
[1171.76 --> 1173.68]  JavaScript being so massive.
[1173.68 --> 1176.76]  And that came across my radar, and I saw it.
[1176.82 --> 1177.62]  I'm like, oh, that's pretty cool.
[1177.70 --> 1179.40]  I didn't even think that that was using the same data.
[1180.20 --> 1181.84]  So yeah, that's been a fun one.
[1181.94 --> 1183.44]  And I've seen it pop up a few times,
[1183.52 --> 1186.36]  because I think it was actually done as a last year's entry.
[1187.42 --> 1189.30]  So yeah, that one's really cool.
[1190.10 --> 1192.06]  Yeah, I guess every year it becomes interesting again, right?
[1192.10 --> 1193.68]  Because you can see what happens since last year.
[1193.84 --> 1194.04]  Right.
[1194.28 --> 1196.20]  Yeah, and the great thing about this stuff is
[1196.20 --> 1198.28]  they're just leveraging BigQuery under the hood.
[1198.44 --> 1200.24]  So every once in a while, they rerun the queries.
[1200.24 --> 1202.08]  So the data is always up to date.
[1202.86 --> 1204.58]  They don't have to worry about collecting the data
[1204.58 --> 1206.22]  or doing any of the other stuff.
[1207.22 --> 1209.48]  And now a word from our sponsor.
[1210.88 --> 1214.52]  TopTal is the best place to work as a freelance software developer.
[1214.84 --> 1217.78]  If you're freelancing right now as a software developer
[1217.78 --> 1220.06]  and you're looking for a way to work with top clients
[1220.06 --> 1222.78]  on projects that are interesting, challenging,
[1223.04 --> 1224.98]  and using the technologies you want to use,
[1225.52 --> 1228.02]  TopTal might just be the place for you.
[1228.02 --> 1230.66]  Working as a freelance software developer with TopTal,
[1230.98 --> 1233.90]  your days of searching for high-quality, long-term work
[1233.90 --> 1236.14]  and getting paid with your worth will be over.
[1236.60 --> 1238.36]  Let's face it, you're an awesome developer
[1238.36 --> 1240.38]  and you deserve to be compensated like one.
[1241.08 --> 1243.36]  Joining TopTal means that you'll have the opportunity
[1243.36 --> 1245.64]  to travel the world as an elite freelancer.
[1246.02 --> 1248.86]  On top of that, TopTal can help provide the software,
[1249.28 --> 1251.46]  hardware, and support you need to work effectively
[1251.46 --> 1252.64]  no matter where you are.
[1252.64 --> 1255.20]  Head to TopTal.com slash developers.
[1255.48 --> 1259.46]  That's T-O-P-T-A-L.com slash developers
[1259.46 --> 1261.98]  to learn more and tell them the changelog sent you.
[1263.72 --> 1267.46]  So essentially, GitHub Archive is a snapshot
[1267.46 --> 1271.68]  or the big data snapshot of all of GitHub public activity.
[1271.96 --> 1272.26]  That's right.
[1272.40 --> 1274.98]  So you actually have two ways of interacting with that data
[1274.98 --> 1275.44]  if you want.
[1275.56 --> 1278.70]  One is you can go and download the raw archives,
[1279.00 --> 1279.76]  the hourly archives,
[1279.76 --> 1281.96]  and that just gives you exactly the data
[1281.96 --> 1283.48]  as I saw it coming from GitHub.
[1284.20 --> 1286.50]  And you can apply anything you want to it.
[1286.92 --> 1288.90]  So if you want to, I don't know,
[1288.94 --> 1290.20]  boot up your own Hadoop cluster
[1290.20 --> 1292.18]  or write your own Ruby script to process it,
[1292.80 --> 1293.38]  go for it.
[1293.64 --> 1294.80]  And the other option is,
[1294.94 --> 1296.44]  the more convenient option,
[1296.54 --> 1299.44]  is to use the BigQuery interface
[1299.44 --> 1301.32]  where you can just write the SQL stuff.
[1301.64 --> 1302.96]  So whichever one fits you best.
[1302.96 --> 1307.34]  So if you want to make a GitHub or something like this,
[1307.40 --> 1310.10]  you can use the GitHub Archive data set
[1310.10 --> 1312.12]  to sort of slice and dice big data coming from GitHub.
[1312.12 --> 1312.40]  That's right.
[1312.66 --> 1312.78]  Yep.
[1313.34 --> 1313.58]  Gotcha.
[1315.12 --> 1317.58]  It's pretty neat how these artifacts
[1317.58 --> 1319.80]  can have such insights after the fact.
[1320.18 --> 1322.36]  And just the foresight of collecting the information,
[1322.46 --> 1324.50]  I guess this is kind of the whole conceit of big data, right?
[1325.02 --> 1327.02]  It's like one person with the foresight of,
[1327.16 --> 1329.22]  let's collect this data and make it publicly available.
[1329.22 --> 1330.64]  Well, down the road,
[1330.70 --> 1332.02]  it opens up all these opportunities
[1332.02 --> 1333.42]  and visualizations and insights
[1333.42 --> 1334.80]  into the open source community
[1334.80 --> 1336.78]  that otherwise wouldn't have been available.
[1337.16 --> 1337.70]  Yeah, absolutely.
[1337.92 --> 1339.70]  And I guess one thing that I've learned
[1339.70 --> 1340.92]  through this process,
[1341.10 --> 1342.90]  and I've seen it happen before as well,
[1343.04 --> 1347.56]  is it's very important to make the analysis
[1347.56 --> 1351.38]  of the data very cheap and easy.
[1352.50 --> 1354.18]  And that, because that enables
[1354.18 --> 1356.04]  a very different type of collaboration
[1356.04 --> 1357.54]  and just iteration, right?
[1357.54 --> 1359.42]  Because if it takes you, let's say,
[1359.60 --> 1360.90]  half a day to answer a question,
[1361.22 --> 1363.16]  you're very limited in the types of questions
[1363.16 --> 1364.22]  you can ask of the data.
[1364.92 --> 1367.16]  Whereas if you get a very quick response,
[1367.28 --> 1369.28]  you can actually start iterating on your questions.
[1369.68 --> 1373.00]  So it's very often that I'll start
[1373.00 --> 1375.22]  with a particular question and then be like,
[1375.32 --> 1377.18]  oh, well, I didn't expect that.
[1377.30 --> 1378.60]  That looks like an outlier.
[1378.72 --> 1379.90]  Let me drill in a little bit further.
[1380.20 --> 1381.52]  So having the tools,
[1381.66 --> 1383.72]  and this is where the BigQuery stuff really helped.
[1384.26 --> 1385.66]  And by the way, there's other projects
[1385.66 --> 1386.82]  that can do this sort of thing.
[1386.82 --> 1388.24]  There are open source projects.
[1388.50 --> 1390.00]  I think Amazon has some of the kind
[1390.00 --> 1390.96]  of similar capabilities.
[1391.22 --> 1392.74]  The fact that it's BigQuery or not
[1392.74 --> 1393.92]  is not the important part.
[1394.02 --> 1395.80]  It's just the fact that it allows you
[1395.80 --> 1397.60]  to quickly and easily ask questions
[1397.60 --> 1398.74]  and get fast answers.
[1399.40 --> 1401.60]  And just having that has been incredibly valuable.
[1401.96 --> 1402.24]  Because it allows...
[1402.24 --> 1403.84]  When you say fast, how fast is fast?
[1404.58 --> 1407.10]  Well, you're processing on the order of,
[1407.36 --> 1408.84]  let's see, I think the current data set
[1408.84 --> 1411.06]  is on the order of a couple hundred gigs.
[1411.28 --> 1412.64]  And you can process all of that
[1412.64 --> 1414.58]  in a span of one to ten seconds.
[1416.02 --> 1419.40]  So if you write a very complicated query,
[1419.98 --> 1421.66]  then it'll take up to ten seconds.
[1422.66 --> 1424.00]  In comparison to, say,
[1424.10 --> 1427.06]  doing that on your desktop would be a day?
[1427.32 --> 1427.92]  Well, yeah.
[1428.32 --> 1429.20]  Depends on your desktop.
[1430.68 --> 1431.34]  Yeah, on your desktop.
[1431.34 --> 1432.68]  Oh, yeah, run-of-the-mill MacBook Pro.
[1433.64 --> 1435.10]  It would take like an hour
[1435.10 --> 1436.96]  just to read the data off disk, right?
[1437.24 --> 1440.00]  Whereas if you have a nice distributed system,
[1440.20 --> 1442.04]  you would just read it from many different disks.
[1442.28 --> 1443.88]  And that goes a heck of a lot faster.
[1444.58 --> 1445.42]  I'm just trying to paint a picture
[1445.42 --> 1446.38]  for those out there who are like,
[1446.48 --> 1447.12]  what is this BigQuery?
[1447.42 --> 1449.20]  And what does he mean by fast?
[1449.78 --> 1452.84]  Because an hour or two hours is way slow.
[1453.10 --> 1453.30]  Sure.
[1453.40 --> 1454.32]  Ten seconds is way fast.
[1454.32 --> 1455.08]  So, yeah.
[1455.30 --> 1456.28]  So that's a great question.
[1456.40 --> 1457.90]  So I guess for context,
[1457.90 --> 1462.32]  so BigQuery is the public version of a product
[1462.32 --> 1464.06]  that we use internally at Google called Dremel.
[1464.38 --> 1468.46]  And Dremel is used to analyze terabyte-sized data sets,
[1468.64 --> 1470.40]  so in multi-terabyte data.
[1471.12 --> 1472.62]  And, you know,
[1472.66 --> 1475.40]  you're leveraging the large computer infrastructure
[1475.40 --> 1476.28]  that Google has,
[1476.56 --> 1477.20]  and, you know,
[1477.26 --> 1478.78]  a terabyte of data can be processed
[1478.78 --> 1480.74]  in the same order of magnitude,
[1481.00 --> 1483.56]  kind of seconds, at most minutes,
[1484.12 --> 1487.10]  which would take otherwise literally days or weeks
[1487.10 --> 1488.24]  on your single computer.
[1489.44 --> 1490.46]  I think this is cool.
[1490.72 --> 1492.70]  I think this GitHub Archive kind of shows
[1492.70 --> 1496.08]  really that internet plumber attitude
[1496.08 --> 1497.36]  that you have towards things.
[1497.40 --> 1498.12]  Because what you've done
[1498.12 --> 1499.32]  is some of the dirty work, right?
[1499.96 --> 1502.28]  And you started off with this itch to scratch.
[1502.88 --> 1503.08]  And, you know,
[1503.08 --> 1503.86]  I have these all the time,
[1503.88 --> 1505.24]  and I'm sure developers out there,
[1505.30 --> 1506.36]  we always have like this little,
[1506.36 --> 1507.68]  ooh, if I could just do this,
[1507.74 --> 1508.34]  it'd be nice.
[1508.92 --> 1510.28]  And then you follow the thread a little bit,
[1510.36 --> 1510.92]  and you realize,
[1511.22 --> 1512.60]  this is like two, three,
[1512.72 --> 1513.38]  maybe a week,
[1513.44 --> 1513.58]  you know,
[1513.60 --> 1514.10]  three days,
[1514.16 --> 1516.26]  maybe a week worth of work,
[1516.26 --> 1517.52]  or whatever threshold
[1517.52 --> 1518.06]  that's just like,
[1518.14 --> 1518.36]  eh,
[1518.62 --> 1519.52]  and you just kind of shelve it.
[1520.16 --> 1521.26]  If you would have done that,
[1521.68 --> 1521.82]  you know,
[1521.84 --> 1522.74]  all these other projects
[1522.74 --> 1524.16]  probably wouldn't have existed
[1524.16 --> 1525.98]  because you've lowered the bar for them
[1525.98 --> 1528.08]  to get to what the interesting part, right?
[1528.08 --> 1529.34]  I want to visualize the data.
[1529.62 --> 1530.68]  You just wanted the email
[1530.68 --> 1533.52]  of the repos every night.
[1533.52 --> 1535.14]  But all this extra work
[1535.14 --> 1536.00]  actually turned into something
[1536.00 --> 1537.18]  that, you know,
[1537.24 --> 1538.36]  we all can use
[1538.36 --> 1540.60]  and has made the ecosystem
[1540.60 --> 1542.16]  kind of more fruitful because of it.
[1542.16 --> 1543.52]  Yeah,
[1543.66 --> 1545.46]  I think that sounds about right.
[1545.74 --> 1545.86]  It's,
[1546.66 --> 1546.88]  you know,
[1546.90 --> 1548.10]  that sort of approach
[1548.10 --> 1549.30]  does take a bit more
[1549.30 --> 1549.78]  at the beginning
[1549.78 --> 1553.08]  because you're required
[1553.08 --> 1553.82]  to do more work.
[1554.38 --> 1554.48]  Like,
[1554.64 --> 1555.20]  how to make sure
[1555.20 --> 1556.00]  that this is accessible,
[1556.18 --> 1556.70]  this is usable,
[1556.84 --> 1557.98]  usable by other people
[1557.98 --> 1558.54]  and all the rest.
[1558.68 --> 1559.36]  But in the long run,
[1559.42 --> 1560.04]  I definitely think
[1560.04 --> 1561.16]  it's kind of a better approach
[1561.16 --> 1562.64]  because exactly as you said,
[1562.68 --> 1564.08]  it allows other people
[1564.08 --> 1565.10]  to leverage that data.
[1565.84 --> 1566.88]  And it also allows me
[1566.88 --> 1567.82]  to play with the data more
[1567.82 --> 1569.12]  because instead of just having
[1569.12 --> 1570.94]  that report card
[1570.94 --> 1572.04]  for what are the interesting
[1572.04 --> 1572.94]  new projects yesterday,
[1573.10 --> 1574.32]  I can ask it tons
[1574.32 --> 1574.98]  of other questions.
[1576.44 --> 1576.60]  Yeah,
[1576.70 --> 1577.44]  so it also means
[1577.44 --> 1578.26]  that you got to kind of,
[1578.38 --> 1578.98]  you got something
[1578.98 --> 1580.56]  you need to maintain as well,
[1580.66 --> 1581.28]  which is kind of
[1581.28 --> 1582.14]  the other side of that coin.
[1583.80 --> 1584.82]  So GitHub Archive
[1584.82 --> 1585.04]  is,
[1585.14 --> 1585.28]  you know,
[1585.28 --> 1586.00]  not a new project.
[1586.10 --> 1586.76]  It's been out there.
[1587.32 --> 1588.52]  And GitHub itself
[1588.52 --> 1589.44]  has changed.
[1589.60 --> 1590.26]  I think the API
[1590.26 --> 1591.74]  has changed over time.
[1592.34 --> 1593.34]  Did that present
[1593.34 --> 1594.30]  any difficulties for you?
[1594.56 --> 1595.30]  API changes
[1595.30 --> 1595.92]  on the GitHub side?
[1596.88 --> 1597.78]  It did in some ways.
[1597.78 --> 1599.34]  So the trouble here
[1599.34 --> 1600.06]  was that,
[1600.84 --> 1601.70]  and this is more of a
[1601.70 --> 1603.62]  kind of BigQuery-specific gotcha,
[1604.18 --> 1606.00]  when BigQuery was first introduced,
[1606.68 --> 1607.22]  you could,
[1607.88 --> 1609.30]  in terms of the data schema
[1609.30 --> 1610.30]  that you could store
[1610.30 --> 1612.46]  within BigQuery,
[1612.92 --> 1614.48]  you had to define that up front.
[1614.70 --> 1615.46]  So you would say,
[1616.16 --> 1616.36]  you know,
[1616.40 --> 1617.42]  these are the columns
[1617.42 --> 1618.92]  for all of my records.
[1619.94 --> 1621.14]  And you couldn't
[1621.14 --> 1622.06]  change that afterwards.
[1622.24 --> 1622.84]  You could create
[1622.84 --> 1623.52]  a new data set
[1623.52 --> 1624.54]  that had a different schema.
[1625.28 --> 1625.78]  But later,
[1625.78 --> 1626.66]  later,
[1626.78 --> 1627.48]  that actually started
[1627.48 --> 1628.18]  causing problems
[1628.18 --> 1628.52]  because,
[1628.74 --> 1629.16]  as you said,
[1629.30 --> 1629.90]  GitHub would,
[1630.32 --> 1630.90]  as they would,
[1631.02 --> 1631.24]  you know,
[1631.34 --> 1632.24]  enhance their product,
[1632.38 --> 1633.04]  add new fields,
[1633.14 --> 1634.66]  maybe deprecate an old field.
[1635.28 --> 1636.78]  And I had a little bit
[1636.78 --> 1637.42]  of pain there
[1637.42 --> 1637.78]  where,
[1638.20 --> 1639.06]  even though I was logging
[1639.06 --> 1639.96]  all of the raw data,
[1640.06 --> 1640.22]  you know,
[1640.24 --> 1641.74]  I always had the raw data stored,
[1642.06 --> 1642.96]  I would have to kind of
[1642.96 --> 1643.60]  massage it
[1643.60 --> 1644.80]  into the schema
[1644.80 --> 1646.26]  that I froze early on,
[1646.70 --> 1647.22]  such that
[1647.22 --> 1647.98]  you could run
[1647.98 --> 1648.90]  a query against
[1648.90 --> 1649.80]  the entire data set.
[1650.52 --> 1650.86]  So,
[1651.06 --> 1651.82]  that did cause
[1651.82 --> 1652.60]  a little bit of friction.
[1652.60 --> 1653.72]  But then,
[1654.36 --> 1655.30]  last year,
[1656.62 --> 1657.86]  BigQuery actually allowed you
[1657.86 --> 1658.88]  to start importing
[1658.88 --> 1659.48]  just like
[1659.48 --> 1661.02]  JSON payloads,
[1661.12 --> 1662.18]  so unstructured data.
[1663.20 --> 1664.68]  And this actually
[1664.68 --> 1665.90]  gave me an opportunity
[1665.90 --> 1667.00]  to go back
[1667.00 --> 1667.84]  and kind of revisit
[1667.84 --> 1669.22]  my original implementation.
[1670.00 --> 1671.02]  And I switched it
[1671.02 --> 1672.36]  after kind of
[1672.36 --> 1673.84]  a bunch of back and forth
[1673.84 --> 1674.80]  on what's the best way
[1674.80 --> 1675.24]  to do it.
[1675.98 --> 1677.02]  Earlier this year,
[1677.24 --> 1678.12]  or actually exactly
[1678.12 --> 1679.04]  on January 1st,
[1679.04 --> 1680.10]  I switched to a new model
[1680.10 --> 1681.36]  where instead of having
[1681.36 --> 1682.36]  every column be fixed,
[1682.60 --> 1683.48]  I'm actually
[1683.48 --> 1686.20]  fixing a subset
[1686.20 --> 1686.96]  of the columns,
[1687.10 --> 1688.08]  which I know are stable.
[1688.78 --> 1689.48]  And if you look at
[1689.48 --> 1690.52]  the API documentation
[1690.52 --> 1692.16]  for the events API
[1692.16 --> 1692.58]  in GitHub,
[1693.00 --> 1693.80]  they'll tell you that
[1693.80 --> 1694.94]  like these five columns
[1694.94 --> 1695.98]  are fixed,
[1696.20 --> 1697.16]  they will always be there.
[1697.58 --> 1698.06]  But then,
[1698.22 --> 1699.00]  take for example,
[1699.22 --> 1700.28]  a pull request
[1700.28 --> 1701.34]  versus issue request.
[1702.50 --> 1703.20]  Both of those
[1703.20 --> 1704.06]  always have an actor,
[1704.34 --> 1705.00]  so somebody who's
[1705.00 --> 1705.70]  doing the action.
[1706.42 --> 1707.12]  And both of those
[1707.12 --> 1708.14]  have like a timestamp
[1708.14 --> 1708.80]  and something else.
[1709.02 --> 1709.90]  And that's always there.
[1710.36 --> 1711.02]  So that's,
[1711.24 --> 1712.02]  like I mapped that
[1712.02 --> 1714.16]  into distinct columns.
[1714.46 --> 1715.06]  But then the actual
[1715.06 --> 1716.24]  payload of the request
[1716.24 --> 1717.12]  or the activity
[1717.12 --> 1717.82]  is different
[1717.82 --> 1718.48]  for each activity.
[1718.62 --> 1719.48]  And that I just store
[1719.48 --> 1720.72]  as kind of a JSON blob.
[1721.14 --> 1721.90]  So it just requires
[1721.90 --> 1722.98]  a little bit more work
[1722.98 --> 1724.12]  on people that are
[1724.12 --> 1725.36]  writing the queries now
[1725.36 --> 1726.76]  to kind of reach
[1726.76 --> 1727.84]  into the JSON data
[1727.84 --> 1728.70]  and pull out the fields
[1728.70 --> 1729.16]  that they want.
[1729.54 --> 1730.02]  But now,
[1730.12 --> 1730.80]  I don't have this problem
[1730.80 --> 1731.90]  at all because GitHub
[1731.90 --> 1732.56]  could just change
[1732.56 --> 1733.34]  anything they want
[1733.34 --> 1735.56]  and I just throw that data
[1735.56 --> 1736.08]  into BigQuery
[1736.08 --> 1737.90]  and there's no updates
[1737.90 --> 1738.40]  on the send.
[1740.02 --> 1740.60]  Yeah, I think I ran
[1740.60 --> 1741.00]  into that
[1741.00 --> 1741.60]  as I was trying
[1741.60 --> 1743.34]  to do some of the queries
[1743.34 --> 1745.02]  to get the email going.
[1745.20 --> 1746.62]  And I'd just like to say
[1746.62 --> 1747.14]  that, man,
[1747.24 --> 1748.76]  you are fast on the trigger
[1748.76 --> 1749.34]  helping out
[1749.34 --> 1750.20]  on the issues.
[1750.64 --> 1751.22]  I appreciate
[1751.22 --> 1753.02]  how quickly
[1753.02 --> 1753.76]  you got back to me
[1753.76 --> 1755.84]  on GitHub
[1755.84 --> 1756.92]  helping me out
[1756.92 --> 1757.88]  with getting the queries
[1757.88 --> 1758.28]  all going.
[1759.56 --> 1760.56]  January 1st.
[1760.66 --> 1761.60]  So that's right about
[1761.60 --> 1762.76]  probably the same time
[1762.76 --> 1763.56]  you turned the email off,
[1763.62 --> 1764.20]  is it not?
[1764.20 --> 1764.56]  Yes.
[1765.28 --> 1765.80]  So actually,
[1765.92 --> 1766.06]  yeah,
[1766.10 --> 1766.96]  on January 1st
[1766.96 --> 1767.84]  after that update
[1767.84 --> 1768.26]  went out,
[1768.60 --> 1770.04]  I guess I didn't
[1770.04 --> 1771.16]  explicitly turn it off
[1771.16 --> 1772.20]  as much as I didn't
[1772.20 --> 1773.64]  update the query
[1773.64 --> 1776.62]  in my daily run
[1776.62 --> 1777.38]  and then I realized
[1777.38 --> 1777.94]  that, whoops,
[1778.50 --> 1779.26]  the data schema
[1779.26 --> 1779.68]  has changed.
[1779.74 --> 1780.04]  Or rather,
[1780.14 --> 1781.16]  I stopped logging data
[1781.16 --> 1782.04]  into the same table.
[1782.50 --> 1783.40]  I have created
[1783.40 --> 1784.02]  a new table
[1784.02 --> 1784.74]  and now I'm actually
[1784.74 --> 1785.90]  creating daily tables.
[1786.42 --> 1787.10]  One of the things
[1787.10 --> 1787.76]  we found was
[1787.76 --> 1788.48]  because I've been
[1788.48 --> 1789.06]  logging data
[1789.06 --> 1790.08]  into the same table
[1790.08 --> 1790.88]  for now over
[1790.88 --> 1791.92]  three years
[1791.92 --> 1792.94]  and we've actually
[1792.94 --> 1794.02]  backported some data
[1794.02 --> 1794.96]  with GitHub's help.
[1795.10 --> 1795.70]  So there's about
[1795.70 --> 1796.48]  three and a half years
[1796.48 --> 1797.04]  of data there.
[1797.78 --> 1798.46]  We do,
[1798.62 --> 1799.34]  or you do have
[1799.34 --> 1799.98]  a free quota,
[1800.28 --> 1801.08]  but it's very easy
[1801.08 --> 1802.16]  to exceed that free quota
[1802.16 --> 1802.86]  if you're not careful.
[1803.82 --> 1805.52]  So that was the reason
[1805.52 --> 1806.24]  why we went into
[1806.24 --> 1806.82]  this new model
[1806.82 --> 1807.98]  where each day
[1807.98 --> 1808.76]  and each month
[1808.76 --> 1809.60]  is a separate table
[1809.60 --> 1811.58]  such that people
[1811.58 --> 1812.74]  can experiment a bit more
[1812.74 --> 1813.96]  without exceeding
[1813.96 --> 1814.56]  their free quota.
[1814.56 --> 1818.96]  So what was the thought
[1818.96 --> 1819.40]  behind,
[1819.62 --> 1819.90]  I mean,
[1820.12 --> 1820.66]  obviously because
[1820.66 --> 1821.36]  it just stopped working,
[1822.32 --> 1822.82]  you didn't turn
[1822.82 --> 1823.66]  the email back on.
[1823.76 --> 1824.64]  There were a few cries
[1824.64 --> 1826.24]  for help.
[1826.76 --> 1827.80]  Myself being one of them,
[1827.86 --> 1828.28]  I think there's
[1828.28 --> 1828.90]  three or four other
[1828.90 --> 1830.58]  people on your
[1830.58 --> 1831.30]  GitHub account
[1831.30 --> 1832.18]  asking what's up
[1832.18 --> 1832.74]  with the email.
[1833.56 --> 1834.26]  What was your decision
[1834.26 --> 1835.52]  to not rewrite that?
[1835.52 --> 1836.00]  So,
[1837.28 --> 1838.30]  as I said,
[1838.72 --> 1840.12]  the first two days,
[1840.22 --> 1840.40]  or I guess
[1840.40 --> 1841.26]  three days before
[1841.26 --> 1842.36]  I realized that
[1842.36 --> 1843.72]  the email stopped coming in,
[1843.84 --> 1844.58]  because as you said,
[1844.68 --> 1846.92]  there's something
[1846.92 --> 1847.68]  about daily emails
[1847.68 --> 1848.36]  where after a while
[1848.36 --> 1849.80]  you start to tune them out.
[1850.82 --> 1851.36]  It took me about
[1851.36 --> 1852.08]  three days to register,
[1852.26 --> 1852.70]  like, oh right,
[1853.02 --> 1853.86]  this is why
[1853.86 --> 1854.58]  I'm not seeing it.
[1854.94 --> 1855.56]  And then a couple
[1855.56 --> 1856.36]  of GitHub issues
[1856.36 --> 1856.82]  popped up.
[1856.92 --> 1857.90]  And the thought process
[1857.90 --> 1858.34]  there was,
[1858.40 --> 1858.54]  I guess,
[1858.60 --> 1858.92]  twofold.
[1859.04 --> 1859.56]  One was,
[1860.12 --> 1861.24]  since I've actually
[1861.24 --> 1863.32]  started the GitHub
[1863.32 --> 1864.44]  Archive newsletter,
[1864.44 --> 1866.14]  GitHub came up
[1866.14 --> 1866.88]  with their own
[1866.88 --> 1867.48]  kind of trending
[1867.48 --> 1869.20]  repositories email
[1869.20 --> 1870.42]  that you can sign up to.
[1871.14 --> 1871.94]  And I've subscribed
[1871.94 --> 1872.42]  to that,
[1872.66 --> 1874.10]  and to be honest,
[1874.16 --> 1875.00]  I actually don't find
[1875.00 --> 1875.76]  it as valuable
[1875.76 --> 1877.00]  as the one I implemented,
[1877.18 --> 1878.04]  but of course I'm biased,
[1878.20 --> 1880.32]  because...
[1880.32 --> 1881.48]  Hey,
[1881.56 --> 1882.08]  we are with you.
[1882.72 --> 1883.50]  Otherwise I wouldn't
[1883.50 --> 1884.56]  ask you to turn it back on
[1884.56 --> 1886.24]  if I was satisfied.
[1886.32 --> 1886.92]  What they're doing
[1886.92 --> 1887.12]  is,
[1887.28 --> 1887.94]  it's basically
[1887.94 --> 1888.70]  the same thing,
[1888.82 --> 1889.62]  but they just provide
[1889.62 --> 1891.14]  fewer repos in there.
[1891.52 --> 1892.18]  I think it's like
[1892.18 --> 1892.94]  the top ten.
[1893.32 --> 1893.84]  And they also
[1893.84 --> 1894.54]  don't separate
[1894.54 --> 1896.04]  what are the new repos
[1896.04 --> 1897.12]  versus the old repos
[1897.12 --> 1898.12]  that got the most activity.
[1899.08 --> 1899.68]  So I just,
[1900.12 --> 1901.86]  I read both effectively,
[1902.18 --> 1903.10]  but I find that there,
[1903.32 --> 1904.64]  I find different things
[1904.64 --> 1905.72]  in both repos
[1905.72 --> 1906.56]  or in both emails.
[1907.28 --> 1908.24]  But at the same time,
[1908.28 --> 1908.80]  it was there,
[1909.06 --> 1909.32]  right?
[1909.46 --> 1909.90]  So I was,
[1910.70 --> 1911.58]  once I realized
[1911.58 --> 1912.48]  that the email
[1912.48 --> 1913.48]  stopped going out,
[1913.90 --> 1915.44]  I actually wondered
[1915.44 --> 1916.58]  if anybody would
[1916.58 --> 1918.18]  cry about it,
[1918.40 --> 1918.56]  right?
[1918.64 --> 1919.42]  If anybody would
[1919.42 --> 1919.92]  contact me,
[1919.96 --> 1920.68]  so I gave it
[1920.68 --> 1921.54]  another couple of days.
[1921.84 --> 1922.34]  And sure enough,
[1922.40 --> 1922.90]  as you said,
[1922.90 --> 1923.46]  there was a couple
[1923.46 --> 1923.94]  of issues
[1923.94 --> 1925.02]  that were being opened
[1925.02 --> 1926.36]  on the repo.
[1926.56 --> 1927.34]  And then at the same time,
[1927.38 --> 1927.92]  I guess you guys
[1927.92 --> 1928.60]  reached out to me
[1928.60 --> 1929.96]  about the work
[1929.96 --> 1930.74]  that you guys are doing.
[1931.00 --> 1931.88]  And at that point,
[1931.92 --> 1932.68]  it kind of became clear
[1932.68 --> 1933.32]  that perhaps
[1933.32 --> 1935.38]  I should find somebody else
[1935.38 --> 1936.32]  to run that project
[1936.32 --> 1937.08]  and focus on
[1937.08 --> 1938.04]  the infrastructure part,
[1938.18 --> 1938.52]  which is,
[1938.98 --> 1939.96]  kind of to your point earlier,
[1940.06 --> 1941.06]  just enable other people
[1941.06 --> 1942.40]  to build cool things
[1942.40 --> 1942.76]  on top.
[1942.76 --> 1945.20]  Well, that's a good
[1945.20 --> 1946.26]  segue then,
[1946.32 --> 1946.64]  isn't it?
[1947.94 --> 1948.30]  Yeah,
[1948.32 --> 1949.66]  we obviously have
[1949.66 --> 1952.76]  a hand in the bag,
[1952.84 --> 1953.40]  so to speak,
[1953.60 --> 1954.40]  in terms of
[1954.40 --> 1955.14]  shooting out emails
[1955.14 --> 1955.96]  and stuff like that.
[1956.32 --> 1958.44]  And to our best ability,
[1958.50 --> 1959.36]  we try to keep up.
[1959.74 --> 1960.90]  And as Jared mentioned,
[1960.98 --> 1962.08]  we used GitHub R-Cod before
[1962.08 --> 1962.88]  and we were like,
[1962.98 --> 1963.62]  well, that's a bummer.
[1963.68 --> 1964.38]  It's not going on anymore.
[1964.58 --> 1966.70]  So it made sense
[1966.70 --> 1967.14]  to reach out
[1967.14 --> 1967.78]  and see if that was
[1967.78 --> 1968.68]  something we could take over.
[1968.68 --> 1970.56]  And we've since
[1970.56 --> 1973.04]  had some conversation about it.
[1973.14 --> 1974.48]  We're launching a new email
[1974.48 --> 1976.26]  called Change Log Nightly
[1976.26 --> 1978.22]  that will essentially become
[1978.22 --> 1979.38]  what GitHub Archive was,
[1980.02 --> 1981.46]  the daily emails at least.
[1982.12 --> 1983.20]  And working with Ilya,
[1983.28 --> 1985.72]  we've transferred the email list.
[1985.78 --> 1986.88]  So we're going to work
[1986.88 --> 1988.52]  with Ilya on making sure
[1988.52 --> 1989.24]  this continues.
[1989.54 --> 1991.32]  So if you're listening to this
[1991.32 --> 1992.32]  and you're on that email list
[1992.32 --> 1993.34]  and you get an email from us
[1993.34 --> 1994.02]  here in the near future,
[1994.20 --> 1995.46]  it's the same email list
[1995.46 --> 1996.78]  and we'll sort of put out
[1996.78 --> 1997.24]  an announcement
[1997.24 --> 1998.60]  in addition with this
[1998.60 --> 1999.60]  podcast to sort of
[1999.60 --> 2001.08]  clear the way
[2001.08 --> 2002.04]  in terms of, you know,
[2002.72 --> 2003.94]  not spamming and stuff like that.
[2003.98 --> 2004.32]  Like it's,
[2004.46 --> 2005.26]  this is a collaboration.
[2005.90 --> 2006.00]  So.
[2006.80 --> 2006.90]  Yeah.
[2006.92 --> 2007.86]  And I'm really excited.
[2008.00 --> 2008.78]  You guys showed me
[2008.78 --> 2010.86]  the preview of the email.
[2011.02 --> 2011.58]  It looks great.
[2011.86 --> 2013.30]  It looks much better designed
[2013.30 --> 2014.52]  than what I managed
[2014.52 --> 2015.06]  to pull off
[2015.06 --> 2016.58]  and in my version.
[2016.76 --> 2017.70]  So that's awesome.
[2018.42 --> 2020.18]  So if you're listening
[2020.18 --> 2021.00]  to this right now,
[2021.20 --> 2022.16]  we're in the,
[2022.30 --> 2023.44]  we're recording this
[2023.44 --> 2024.04]  in the past,
[2024.06 --> 2024.62]  but you're going to listen
[2024.62 --> 2025.72]  to this in the future.
[2025.72 --> 2027.26]  So when you're actually
[2027.26 --> 2028.08]  listening to this,
[2028.08 --> 2029.04]  so if you're hearing
[2029.04 --> 2029.74]  my voice right now,
[2029.80 --> 2030.52]  you can actually go
[2030.52 --> 2031.46]  to the changelaw.com
[2031.46 --> 2032.14]  slash nightly.
[2032.90 --> 2033.86]  That may move
[2033.86 --> 2035.68]  to nightly.the changelaw.com
[2035.68 --> 2036.84]  in the near future,
[2036.98 --> 2037.78]  but for now,
[2037.80 --> 2038.38]  it's going to be there.
[2038.46 --> 2039.58]  You can subscribe now.
[2040.54 --> 2041.10]  Hopefully, Jared,
[2041.14 --> 2042.20]  you can give me a nod
[2042.20 --> 2042.82]  or something like that
[2042.82 --> 2043.50]  to say for sure
[2043.50 --> 2043.76]  we're going to be
[2043.76 --> 2044.28]  shooting emails.
[2044.42 --> 2044.84]  Right now,
[2044.88 --> 2045.72]  we're doing it internally.
[2046.46 --> 2047.42]  As Ilya just mentioned,
[2047.52 --> 2051.14]  we had shared the design
[2051.14 --> 2051.72]  with him now.
[2051.72 --> 2052.34]  And Ilya,
[2052.50 --> 2052.72]  you know,
[2052.80 --> 2054.16]  on the work,
[2054.50 --> 2055.42]  like I love how
[2055.42 --> 2056.32]  there's a sort of layers
[2056.32 --> 2056.86]  to this onion.
[2057.12 --> 2057.98]  Like your itch
[2057.98 --> 2059.04]  from way back when
[2059.04 --> 2060.12]  all this work
[2060.12 --> 2060.62]  with BigQuery,
[2060.80 --> 2061.26]  all this work
[2061.26 --> 2062.02]  with like storing
[2062.02 --> 2062.54]  this data,
[2062.74 --> 2063.08]  and then,
[2063.28 --> 2063.94]  you know,
[2063.98 --> 2064.66]  and then now
[2064.66 --> 2066.32]  we've come behind you,
[2066.36 --> 2067.00]  which would you say
[2067.00 --> 2067.62]  that you're a designer,
[2067.74 --> 2067.84]  Ilya?
[2068.00 --> 2068.42]  Or would you say
[2068.42 --> 2069.06]  you're not a designer?
[2069.32 --> 2070.02]  Sometimes I pretend
[2070.02 --> 2070.70]  to be a designer.
[2070.94 --> 2071.82]  I can't say I'm a good one.
[2072.70 --> 2073.68]  Play one on TV.
[2074.00 --> 2074.22]  Yeah.
[2074.48 --> 2074.94]  So I mean,
[2075.00 --> 2075.90]  I would consider myself
[2075.90 --> 2076.42]  a designer.
[2076.42 --> 2078.24]  And when we,
[2078.42 --> 2078.90]  you know,
[2078.94 --> 2080.32]  we came across this project
[2080.32 --> 2081.42]  and taking over
[2081.42 --> 2082.48]  the email part of it,
[2083.06 --> 2083.88]  I was like,
[2083.92 --> 2084.42]  there's a way,
[2084.50 --> 2085.30]  I like the data,
[2085.52 --> 2086.00]  but there's a way
[2086.00 --> 2086.50]  we can visualize
[2086.50 --> 2087.32]  it a little differently.
[2088.16 --> 2088.52]  And,
[2088.58 --> 2089.22]  you know,
[2089.26 --> 2090.52]  we're sharing
[2090.52 --> 2091.60]  the stars a lot clearer,
[2091.82 --> 2093.48]  the up stars
[2093.48 --> 2094.14]  for that day
[2094.14 --> 2094.84]  a lot more clearer.
[2094.92 --> 2095.84]  So when you see this email,
[2095.92 --> 2096.34]  you're going to love
[2096.34 --> 2096.94]  how it looks.
[2098.62 --> 2099.78]  We even went
[2099.78 --> 2100.74]  as far as
[2100.74 --> 2101.66]  making it have
[2101.66 --> 2102.20]  a night theme
[2102.20 --> 2102.76]  because we figured
[2102.76 --> 2104.04]  if you're going to be,
[2104.12 --> 2104.80]  you know,
[2104.82 --> 2105.56]  on your phone
[2105.56 --> 2106.54]  or on your MacBook
[2106.54 --> 2107.40]  at night
[2107.40 --> 2108.64]  if you're in the
[2108.64 --> 2109.16]  East Coast
[2109.16 --> 2110.28]  Central time zones
[2110.28 --> 2111.94]  or in the U.S. time zones,
[2112.10 --> 2113.68]  it's probably going to be at night.
[2113.78 --> 2114.02]  Otherwise,
[2114.16 --> 2114.58]  it's daytime
[2114.58 --> 2115.42]  or something like that
[2115.42 --> 2116.00]  for you.
[2116.12 --> 2116.90]  But we figured
[2116.90 --> 2117.42]  let's ship it
[2117.42 --> 2118.16]  with a night theme.
[2118.34 --> 2119.88]  So we made it dark.
[2120.38 --> 2121.54]  We may actually offer
[2121.54 --> 2122.50]  a day and night theme
[2122.50 --> 2122.92]  in the future,
[2122.92 --> 2123.76]  but at least for now
[2123.76 --> 2124.16]  it's going to ship
[2124.16 --> 2124.72]  with a night theme
[2124.72 --> 2126.02]  to make your eyes
[2126.02 --> 2126.60]  a little bit,
[2126.86 --> 2127.16]  you know,
[2127.36 --> 2127.84]  a little easier
[2127.84 --> 2128.58]  on the eyes at night.
[2129.58 --> 2130.84]  And as Adam said,
[2130.92 --> 2132.32]  we've been shipping this
[2132.32 --> 2133.04]  just to ourselves
[2133.04 --> 2134.24]  over the last couple of days.
[2134.24 --> 2136.14]  And I texted him,
[2136.28 --> 2137.00]  was it last night?
[2137.04 --> 2137.28]  I'm like,
[2137.32 --> 2137.98]  I'm so happy.
[2139.30 --> 2140.04]  It's weird.
[2140.30 --> 2141.26]  I'm a total nerd
[2141.26 --> 2142.42]  that this makes me so happy
[2142.42 --> 2143.50]  to have this back
[2143.50 --> 2144.88]  every night.
[2145.02 --> 2145.84]  So we're excited
[2145.84 --> 2146.58]  to get it out there
[2146.58 --> 2148.04]  and get it in your mailboxes
[2148.04 --> 2148.42]  as well.
[2148.80 --> 2148.92]  Yeah,
[2148.96 --> 2149.56]  so go to
[2149.56 --> 2150.60]  the changelog.com
[2150.60 --> 2151.38]  slash nightly,
[2151.58 --> 2152.20]  sign up.
[2152.82 --> 2153.00]  And Ilya,
[2153.06 --> 2153.76]  I think we've grown a list
[2153.76 --> 2154.18]  a little bit
[2154.18 --> 2155.64]  since you handed it to us.
[2155.70 --> 2156.38]  It went from
[2156.38 --> 2158.42]  like just around 900
[2158.42 --> 2159.52]  to like I think
[2159.52 --> 2160.66]  just a little over 1,000 now.
[2160.90 --> 2161.40]  Oh, that's awesome.
[2161.68 --> 2162.58]  We've actually grown the list
[2162.58 --> 2163.20]  a tiny little bit.
[2163.20 --> 2163.80]  So hopefully
[2163.80 --> 2165.08]  between this
[2165.08 --> 2166.62]  and our changelog weekly email
[2166.62 --> 2167.68]  which won't change,
[2168.10 --> 2169.14]  we'll still share repos in there.
[2169.20 --> 2169.84]  That's more of our
[2169.84 --> 2170.72]  edits realized,
[2172.00 --> 2172.16]  you know,
[2172.22 --> 2173.26]  highly curated email
[2173.26 --> 2174.58]  whereas this one's automated.
[2174.76 --> 2175.40]  So they sort of
[2175.40 --> 2176.50]  sister and brother
[2176.50 --> 2177.56]  in that regard
[2177.56 --> 2178.84]  where you got nightly
[2178.84 --> 2179.66]  which is sort of this
[2179.66 --> 2181.60]  constant daily update,
[2181.72 --> 2182.32]  nightly update.
[2182.50 --> 2183.66]  And then our changelog weekly
[2183.66 --> 2185.56]  which goes out on Saturdays
[2185.56 --> 2187.34]  which is links,
[2187.62 --> 2188.16]  videos,
[2188.46 --> 2189.10]  top repos
[2189.10 --> 2189.46]  that are hitting
[2189.46 --> 2190.56]  our radar.
[2191.16 --> 2192.12]  We're still sharing that email.
[2192.12 --> 2194.06]  Yeah, that's awesome.
[2194.26 --> 2195.22]  So for the
[2195.22 --> 2196.40]  GitHub mailing list
[2196.40 --> 2197.64]  or the original mailing list,
[2197.76 --> 2197.88]  you know,
[2197.90 --> 2198.60]  I've never actually
[2198.60 --> 2199.92]  even actively promoted it.
[2200.04 --> 2200.88]  It was just one of those things
[2200.88 --> 2202.22]  where I had the email
[2202.22 --> 2203.20]  and I think one time
[2203.20 --> 2203.76]  I forwarded it
[2203.76 --> 2204.48]  to one of my friends
[2204.48 --> 2205.26]  because I was like,
[2205.30 --> 2205.60]  oh look,
[2205.78 --> 2206.86]  your repo
[2206.86 --> 2208.00]  has made the list.
[2208.60 --> 2209.66]  And then he asked me
[2209.66 --> 2210.40]  for like
[2210.40 --> 2211.34]  where can I sign up?
[2212.22 --> 2212.38]  So
[2212.38 --> 2214.02]  after that
[2214.02 --> 2215.52]  I just dropped a link
[2215.52 --> 2215.80]  on the
[2215.80 --> 2217.56]  GitHubarchive.org website
[2217.56 --> 2219.20]  and I never actively
[2219.20 --> 2219.82]  promoted it
[2219.82 --> 2220.56]  and yet somehow
[2220.56 --> 2221.74]  it gathered a thousand people.
[2221.96 --> 2222.12]  So
[2222.12 --> 2223.70]  I'm curious to see
[2223.70 --> 2224.48]  where you guys take it
[2224.48 --> 2225.50]  because I agree,
[2225.58 --> 2227.00]  I find them incredibly valuable
[2227.00 --> 2227.56]  and
[2227.56 --> 2228.44]  I actually think
[2228.44 --> 2229.22]  there's a lot of room
[2229.22 --> 2230.40]  for kind of experimenting
[2230.40 --> 2231.38]  in the space as well.
[2232.38 --> 2233.10]  One of the things
[2233.10 --> 2233.50]  that I've wanted
[2233.50 --> 2234.16]  for a long time
[2234.16 --> 2235.34]  and just never got around to it
[2235.34 --> 2235.78]  was
[2235.78 --> 2237.50]  creating more
[2237.50 --> 2238.14]  thematic
[2238.14 --> 2239.30]  lists as well.
[2239.52 --> 2239.68]  So
[2239.68 --> 2240.42]  right now
[2240.42 --> 2241.20]  it's just like
[2241.20 --> 2242.40]  everything across GitHub,
[2242.66 --> 2242.84]  right?
[2242.84 --> 2243.84]  but if I'm
[2243.84 --> 2244.94]  particularly interested
[2244.94 --> 2245.64]  in let's say
[2245.64 --> 2246.72]  Ruby or Node
[2246.72 --> 2247.58]  or something else
[2247.58 --> 2248.70]  you can imagine
[2248.70 --> 2249.82]  just copying it to that
[2249.82 --> 2251.40]  which would be quite cool.
[2252.84 --> 2254.20]  I would say
[2254.20 --> 2254.54]  and Jared
[2254.54 --> 2255.56]  you can back me up on this
[2255.56 --> 2256.02]  but I would say
[2256.02 --> 2257.30]  that this is definitely
[2257.30 --> 2258.92]  a start for us.
[2260.12 --> 2261.20]  I think that
[2261.20 --> 2262.10]  as we can get
[2262.10 --> 2263.26]  more and more
[2263.26 --> 2264.24]  interesting data
[2264.24 --> 2264.88]  out of
[2264.88 --> 2265.94]  what you've been storing
[2265.94 --> 2266.74]  in BigQuery
[2266.74 --> 2268.10]  and GitHubarchive
[2268.10 --> 2268.80]  I think that
[2268.80 --> 2270.70]  I'd love to keep exploring.
[2270.82 --> 2271.60]  I think this is just
[2271.60 --> 2272.46]  the tip of the iceberg
[2272.46 --> 2273.02]  for us
[2273.02 --> 2273.58]  because I've already
[2273.58 --> 2274.24]  had tons of fun
[2274.24 --> 2274.72]  just doing what
[2274.72 --> 2275.54]  we've done so far
[2275.54 --> 2277.08]  and I think we'll just
[2277.08 --> 2277.40]  keep
[2277.40 --> 2278.38]  from a listener
[2278.38 --> 2278.78]  perspective
[2278.78 --> 2280.04]  if you're listening
[2280.04 --> 2280.46]  to this
[2280.46 --> 2280.78]  and you love
[2280.78 --> 2281.36]  the changelog
[2281.36 --> 2282.40]  and you're a member
[2282.40 --> 2283.34]  or you're not
[2283.34 --> 2284.98]  we aim to
[2284.98 --> 2286.50]  serve the open source
[2286.50 --> 2286.92]  community
[2286.92 --> 2287.90]  as best we can
[2287.90 --> 2288.32]  and sometimes
[2288.32 --> 2289.14]  that might be
[2289.14 --> 2290.14]  shipping really awesome
[2290.14 --> 2290.46]  emails
[2290.46 --> 2291.16]  sometimes that's
[2291.16 --> 2291.58]  doing a really
[2291.58 --> 2292.42]  awesome podcast
[2292.42 --> 2294.86]  sometimes that's
[2294.86 --> 2295.58]  sharing things
[2295.58 --> 2295.96]  on Twitter
[2295.96 --> 2296.50]  or blog
[2296.50 --> 2296.96]  or wherever
[2296.96 --> 2298.50]  or going to a conference
[2298.50 --> 2299.80]  so this is one of the ways
[2299.80 --> 2300.50]  we definitely plan
[2300.50 --> 2301.56]  to press hard.
[2302.46 --> 2303.80]  Yeah and we do plan
[2303.80 --> 2304.68]  to also open source
[2304.68 --> 2305.10]  the repo
[2305.10 --> 2305.92]  that runs Nightly
[2305.92 --> 2308.12]  so you can contribute
[2308.12 --> 2308.78]  as well
[2308.78 --> 2310.16]  if you're a reader
[2310.16 --> 2310.74]  of the email
[2310.74 --> 2311.30]  and you want to see
[2311.30 --> 2311.92]  a new data point
[2311.92 --> 2312.38]  in there
[2312.38 --> 2313.94]  or you'd love to have
[2313.94 --> 2314.56]  these language
[2314.56 --> 2315.44]  specific emails
[2315.44 --> 2316.12]  which has definitely
[2316.12 --> 2316.58]  been something
[2316.58 --> 2317.20]  we've discussed
[2317.20 --> 2317.60]  internally
[2317.60 --> 2318.42]  but it's a little bit
[2318.42 --> 2320.02]  more heavy lifting
[2320.02 --> 2321.22]  it's going to be
[2321.22 --> 2321.70]  open source
[2321.70 --> 2322.50]  you can hop on there
[2322.50 --> 2323.12]  open an issue
[2323.12 --> 2323.76]  or fork it
[2323.76 --> 2324.38]  and do all that
[2324.38 --> 2325.08]  good stuff too.
[2325.88 --> 2326.22]  That's awesome.
[2326.34 --> 2326.96]  That good stuff.
[2327.98 --> 2328.60]  So Elliot
[2328.60 --> 2329.08]  what do you think
[2329.08 --> 2329.70]  about Nightly then?
[2329.80 --> 2330.42]  What are your
[2330.42 --> 2331.22]  initial thoughts
[2331.22 --> 2331.74]  and just us
[2331.74 --> 2332.34]  taking it over
[2332.34 --> 2333.26]  and not having
[2333.26 --> 2333.86]  to worry about
[2333.86 --> 2334.42]  the burden
[2334.42 --> 2335.62]  of the email anymore?
[2335.74 --> 2336.16]  I'm happy.
[2336.68 --> 2337.66]  I'm super happy.
[2338.06 --> 2338.64]  So first of all
[2338.64 --> 2339.62]  I get my emails back
[2339.62 --> 2340.22]  which is great
[2340.22 --> 2340.92]  because I've been
[2340.92 --> 2341.58]  for the last
[2341.58 --> 2341.88]  I guess
[2341.88 --> 2342.86]  month and a half
[2342.86 --> 2343.40]  I've been relying
[2343.40 --> 2344.22]  on the GitHub version
[2344.22 --> 2345.04]  and as I said
[2345.04 --> 2346.06]  those are great
[2346.06 --> 2346.82]  but I don't find
[2346.82 --> 2347.96]  that they're
[2347.96 --> 2349.08]  as interesting
[2349.08 --> 2350.06]  in many ways.
[2350.20 --> 2350.72]  I don't discover
[2350.72 --> 2351.64]  as many interesting things.
[2352.58 --> 2353.32]  That and just
[2353.32 --> 2354.10]  having you guys
[2354.10 --> 2354.58]  work on it
[2354.58 --> 2355.24]  I think you'll
[2355.24 --> 2355.76]  do a much better
[2355.76 --> 2356.64]  long term job
[2356.64 --> 2357.52]  of it.
[2357.70 --> 2358.46]  I appreciate that.
[2358.58 --> 2359.44]  And you know
[2359.44 --> 2361.20]  these itches
[2361.20 --> 2362.12]  you keep scratching too
[2362.12 --> 2363.32]  I would say
[2363.32 --> 2365.20]  let's figure out
[2365.20 --> 2366.16]  a way to keep
[2366.16 --> 2366.68]  working together.
[2366.98 --> 2367.78]  I know Jared
[2367.78 --> 2368.44]  and I will take over
[2368.44 --> 2369.10]  and start doing
[2369.10 --> 2369.52]  some things
[2369.52 --> 2371.36]  but if you've got
[2371.36 --> 2372.32]  a particular email
[2372.32 --> 2373.62]  that you want
[2373.62 --> 2374.34]  to see go out
[2374.34 --> 2375.68]  or data set
[2375.68 --> 2376.20]  pulled from
[2376.20 --> 2377.22]  this then
[2377.22 --> 2378.66]  let's work on it.
[2379.06 --> 2379.34]  Let's figure out
[2379.34 --> 2379.98]  a way to make it happen.
[2380.26 --> 2380.66]  Yeah for sure.
[2381.34 --> 2382.10]  I'm really happy
[2382.10 --> 2382.80]  to hear that you guys
[2382.80 --> 2383.32]  are going to make
[2383.32 --> 2384.52]  the actual code
[2384.52 --> 2385.40]  for that open source.
[2385.86 --> 2386.20]  And I guess
[2386.20 --> 2386.76]  I should mention
[2386.76 --> 2388.32]  all the GitHub Archive
[2388.32 --> 2389.44]  source
[2389.44 --> 2390.34]  for the website
[2390.34 --> 2391.28]  for the crawler
[2391.28 --> 2392.46]  and even for the
[2392.46 --> 2393.12]  old reports
[2393.12 --> 2394.52]  if you still want them
[2394.52 --> 2395.34]  is online.
[2395.54 --> 2396.10]  So if you just go
[2396.10 --> 2396.52]  under
[2396.52 --> 2397.84]  igregorix
[2397.84 --> 2399.46]  slash githubarchive.org
[2399.46 --> 2400.36]  that's the repo
[2400.36 --> 2401.00]  and
[2401.00 --> 2402.74]  if you find bugs
[2402.74 --> 2403.42]  improvements
[2403.42 --> 2404.38]  all the stuff
[2404.38 --> 2404.76]  is welcome.
[2405.68 --> 2407.64]  Awesome.
[2407.74 --> 2408.28]  Well we do have
[2408.28 --> 2408.94]  a note in here
[2408.94 --> 2409.66]  to talk a little bit
[2409.66 --> 2410.40]  about the future
[2410.40 --> 2411.54]  of GitHub Archive.
[2412.14 --> 2412.88]  If you have
[2412.88 --> 2413.72]  future plans
[2413.72 --> 2414.16]  or a roadmap
[2414.16 --> 2415.06]  or if you consider
[2415.06 --> 2415.98]  it kind of a finished
[2415.98 --> 2417.02]  thing as a piece
[2417.02 --> 2417.46]  of plumbing
[2417.46 --> 2418.60]  what are your
[2418.60 --> 2419.20]  thoughts on that?
[2419.90 --> 2420.30]  So I think
[2420.30 --> 2421.02]  it's mostly
[2421.02 --> 2422.78]  a finished thing
[2422.78 --> 2424.06]  in the sense
[2424.06 --> 2425.80]  that the crawler
[2425.80 --> 2426.42]  is running
[2426.42 --> 2427.12]  it's stable
[2427.12 --> 2428.30]  I think I've
[2428.30 --> 2429.16]  figured out
[2429.16 --> 2429.94]  all the bugs there
[2429.94 --> 2430.74]  and I'm really happy
[2430.74 --> 2431.04]  with it
[2431.04 --> 2431.80]  like it's been
[2431.80 --> 2432.50]  running for years.
[2432.50 --> 2433.88]  So that part
[2433.88 --> 2434.30]  is good.
[2434.72 --> 2435.36]  What I would
[2435.36 --> 2436.00]  like to do
[2436.00 --> 2436.72]  is maybe
[2436.72 --> 2437.62]  go back
[2437.62 --> 2438.18]  and revisit
[2438.18 --> 2438.78]  how I've
[2438.78 --> 2439.14]  imported
[2439.14 --> 2439.60]  some of the
[2439.60 --> 2440.04]  data into
[2440.04 --> 2440.32]  BigQuery
[2440.32 --> 2441.98]  because as I
[2441.98 --> 2442.32]  mentioned
[2442.32 --> 2443.08]  the schema
[2443.08 --> 2443.72]  was changing
[2443.72 --> 2444.98]  and I had
[2444.98 --> 2445.82]  a frozen schema
[2445.82 --> 2446.56]  so some of the
[2446.56 --> 2447.16]  fields may not
[2447.16 --> 2447.54]  be there
[2447.54 --> 2448.08]  that perhaps
[2448.08 --> 2448.40]  should have
[2448.40 --> 2448.52]  been.
[2449.88 --> 2450.18]  So that's
[2450.18 --> 2450.58]  just kind of
[2450.58 --> 2452.18]  one of those
[2452.18 --> 2452.72]  things where
[2452.72 --> 2453.48]  I would like
[2453.48 --> 2454.20]  to get to it
[2454.20 --> 2454.98]  where I'd like
[2454.98 --> 2455.58]  to go back
[2455.58 --> 2456.96]  and re-import
[2456.96 --> 2457.96]  the old data
[2457.96 --> 2458.70]  in the same way
[2458.70 --> 2459.28]  that I'm importing
[2459.28 --> 2459.82]  the new data
[2459.82 --> 2460.06]  now
[2460.06 --> 2461.00]  just to make
[2461.00 --> 2461.54]  it all nice
[2461.54 --> 2462.06]  and consistent
[2462.06 --> 2464.42]  and if somebody
[2464.42 --> 2465.46]  is interested
[2465.46 --> 2466.04]  in taking that
[2466.04 --> 2466.40]  on that would
[2466.40 --> 2466.86]  be even better
[2466.86 --> 2467.44]  to be honest
[2467.44 --> 2468.28]  but that's
[2468.28 --> 2469.06]  probably the
[2469.06 --> 2469.60]  main thing
[2469.60 --> 2470.04]  otherwise
[2470.04 --> 2470.96]  it's running
[2470.96 --> 2471.36]  it's humming
[2471.36 --> 2471.74]  along
[2471.74 --> 2473.68]  I should plug
[2473.68 --> 2474.12]  actually
[2474.12 --> 2475.30]  the BigQuery
[2475.30 --> 2475.78]  team
[2475.78 --> 2476.18]  they've given
[2476.18 --> 2476.54]  me a lot
[2476.54 --> 2477.08]  of support
[2477.08 --> 2479.52]  and they've
[2479.52 --> 2480.12]  paid the bills
[2480.12 --> 2480.66]  for hosting
[2480.66 --> 2481.22]  all that data
[2481.22 --> 2482.94]  so kudos
[2482.94 --> 2483.32]  to them
[2483.32 --> 2483.78]  so there's
[2483.78 --> 2485.40]  that
[2485.40 --> 2486.94]  there's no
[2486.94 --> 2487.54]  kind of concerns
[2487.54 --> 2488.12]  over how much
[2488.12 --> 2488.72]  data we're storing
[2488.72 --> 2489.48]  so that's been
[2489.48 --> 2489.90]  really good.
[2491.06 --> 2491.62]  That's nice
[2491.62 --> 2492.18]  right there
[2492.18 --> 2492.76]  I was going to
[2492.76 --> 2493.46]  add I guess
[2493.46 --> 2494.04]  on the tail end
[2494.04 --> 2494.22]  of that
[2494.22 --> 2494.80]  is this
[2494.80 --> 2495.94]  one of the
[2495.94 --> 2496.84]  main ways
[2496.84 --> 2497.36]  is there any
[2497.36 --> 2498.70]  other large
[2498.70 --> 2499.20]  data sets
[2499.20 --> 2499.56]  of GitHub
[2499.56 --> 2500.94]  data out
[2500.94 --> 2501.22]  there
[2501.22 --> 2501.84]  other than
[2501.84 --> 2502.18]  this one?
[2503.18 --> 2503.48]  You know what
[2503.48 --> 2504.24]  I'm not sure
[2504.24 --> 2504.92]  I don't think so
[2504.92 --> 2505.54]  not that I've
[2505.54 --> 2506.04]  come across
[2506.04 --> 2506.76]  I've seen
[2506.76 --> 2507.76]  I keep coming
[2507.76 --> 2508.54]  across projects
[2508.54 --> 2509.64]  that I'm surprised
[2509.64 --> 2510.08]  to find out
[2510.08 --> 2510.50]  are using
[2510.50 --> 2511.36]  GitHub Archive
[2511.36 --> 2511.80]  data under
[2511.80 --> 2512.14]  the hood
[2512.14 --> 2512.72]  because either
[2512.72 --> 2513.10]  they grab
[2513.10 --> 2513.68]  the archives
[2513.68 --> 2514.56]  or they're
[2514.56 --> 2515.10]  using BigQuery
[2515.10 --> 2516.26]  but I've not
[2516.26 --> 2516.92]  seen other
[2516.92 --> 2517.44]  people
[2517.44 --> 2519.08]  kind of log it
[2519.08 --> 2519.56]  and store it
[2519.56 --> 2520.26]  and process it
[2520.26 --> 2520.72]  on their own.
[2522.00 --> 2522.36]  And in terms of
[2522.36 --> 2522.80]  the future
[2522.80 --> 2523.60]  you mentioned
[2523.60 --> 2524.22]  your collaboration
[2524.22 --> 2524.66]  with GitHub
[2524.66 --> 2525.92]  and improving
[2525.92 --> 2526.66]  things and things
[2526.66 --> 2527.02]  like that
[2527.02 --> 2529.84]  are they mutually
[2529.84 --> 2531.24]  involved in this
[2531.24 --> 2531.70]  to a degree?
[2531.90 --> 2532.44]  Is there any sort
[2532.44 --> 2533.36]  of interest in
[2533.36 --> 2534.32]  this for them
[2534.32 --> 2534.74]  in the future?
[2534.74 --> 2535.46]  Yeah I think so
[2535.46 --> 2536.36]  actually just
[2536.36 --> 2537.24]  last week
[2537.24 --> 2537.74]  I was exchanging
[2537.74 --> 2538.16]  emails
[2538.16 --> 2539.38]  with somebody
[2539.38 --> 2539.74]  at GitHub
[2539.74 --> 2540.84]  where they're
[2540.84 --> 2541.66]  interested in
[2541.66 --> 2542.38]  engaging the
[2542.38 --> 2543.18]  academic community
[2543.18 --> 2544.10]  and actually
[2544.10 --> 2544.80]  coming back
[2544.80 --> 2545.34]  to the
[2545.34 --> 2545.64]  kind of
[2545.64 --> 2546.10]  interesting
[2546.10 --> 2547.72]  use cases
[2547.72 --> 2548.20]  of this
[2548.20 --> 2548.46]  data
[2548.46 --> 2549.84]  I've been
[2549.84 --> 2550.18]  approached
[2550.18 --> 2550.60]  by a number
[2550.60 --> 2551.12]  of researchers
[2551.12 --> 2551.88]  in various
[2551.88 --> 2552.74]  universities
[2552.74 --> 2553.58]  that are using
[2553.58 --> 2554.28]  GitHub Archive
[2554.28 --> 2554.94]  data for
[2554.94 --> 2555.76]  analyzing things
[2555.76 --> 2556.14]  like what
[2556.14 --> 2556.68]  makes a great
[2556.68 --> 2557.08]  open source
[2557.08 --> 2557.52]  community
[2557.52 --> 2558.48]  or what
[2558.48 --> 2558.88]  patterns
[2558.88 --> 2559.10]  do they
[2559.10 --> 2559.36]  exhibit
[2559.36 --> 2559.80]  what makes
[2559.80 --> 2560.26]  a resilient
[2560.26 --> 2560.76]  open source
[2560.76 --> 2561.28]  community
[2561.28 --> 2562.12]  so on and so
[2562.12 --> 2562.26]  forth
[2562.26 --> 2563.12]  the social
[2563.12 --> 2563.60]  dynamics
[2563.60 --> 2564.50]  of open
[2564.50 --> 2564.76]  source
[2564.76 --> 2565.88]  so there's
[2565.88 --> 2566.26]  been a couple
[2566.26 --> 2566.76]  of papers
[2566.76 --> 2567.48]  published on
[2567.48 --> 2567.80]  this stuff
[2567.80 --> 2568.32]  using GitHub
[2568.32 --> 2568.94]  Archive data
[2568.94 --> 2569.70]  and I think
[2569.70 --> 2570.14]  GitHub in
[2570.14 --> 2570.70]  particular is
[2570.70 --> 2571.48]  interested in
[2571.48 --> 2572.44]  getting more
[2572.44 --> 2572.74]  of that
[2572.74 --> 2573.00]  kind of
[2573.00 --> 2573.42]  collaboration
[2573.42 --> 2573.78]  with the
[2573.78 --> 2574.08]  academic
[2574.08 --> 2574.50]  community
[2574.50 --> 2575.46]  so we're
[2575.46 --> 2576.02]  chatting now
[2576.02 --> 2576.84]  about potentially
[2576.84 --> 2577.32]  exposing
[2577.32 --> 2578.38]  additional
[2578.38 --> 2579.02]  data sets
[2579.02 --> 2579.78]  via BigQuery
[2579.78 --> 2581.24]  because clearly
[2581.24 --> 2581.82]  the researchers
[2581.82 --> 2582.30]  are already
[2582.30 --> 2583.18]  using that
[2583.18 --> 2583.58]  interface
[2583.58 --> 2585.10]  so in the
[2585.10 --> 2585.66]  future you may
[2585.66 --> 2586.14]  see some
[2586.14 --> 2586.66]  additional
[2586.66 --> 2587.28]  augmented
[2587.28 --> 2589.00]  data become
[2589.00 --> 2589.52]  available
[2589.52 --> 2591.72]  through GitHub
[2591.72 --> 2592.12]  Archive
[2592.12 --> 2593.52]  but we're
[2593.52 --> 2593.94]  still kind of
[2593.94 --> 2594.38]  working through
[2594.38 --> 2594.80]  the details
[2594.80 --> 2595.30]  of what that
[2595.30 --> 2595.78]  is and how
[2595.78 --> 2596.02]  that would
[2596.02 --> 2596.48]  work and all
[2596.48 --> 2596.74]  the rest
[2596.74 --> 2599.16]  and now a
[2599.16 --> 2599.68]  word from our
[2599.68 --> 2600.14]  sponsor
[2600.14 --> 2602.32]  it is time to
[2602.32 --> 2602.86]  put the program
[2602.86 --> 2603.44]  books away
[2603.44 --> 2604.12]  put them away
[2604.12 --> 2604.76]  put them down
[2604.76 --> 2605.78]  and learn by
[2605.78 --> 2606.16]  doing with
[2606.16 --> 2606.70]  CodeSchool
[2606.70 --> 2608.18]  CodeSchool offers
[2608.18 --> 2608.98]  a variety of
[2608.98 --> 2609.68]  courses to help
[2609.68 --> 2610.50]  you expand your
[2610.50 --> 2611.46]  skills and learn
[2611.46 --> 2612.22]  new technologies
[2612.22 --> 2612.96]  such as
[2612.96 --> 2613.68]  JavaScript
[2613.68 --> 2614.70]  Ruby
[2614.70 --> 2615.78]  iOS
[2615.78 --> 2616.20]  Git
[2616.20 --> 2616.76]  HTML
[2616.76 --> 2617.28]  CSS
[2617.28 --> 2618.14]  and many
[2618.14 --> 2618.52]  more
[2618.52 --> 2619.40]  CodeSchool
[2619.40 --> 2619.92]  knows that
[2619.92 --> 2620.40]  learning the
[2620.40 --> 2620.98]  code can be a
[2620.98 --> 2621.70]  daunting task
[2621.70 --> 2622.70]  so they combine
[2622.70 --> 2623.42]  experienced
[2623.42 --> 2624.26]  instructors with
[2624.26 --> 2625.04]  proven learning
[2625.04 --> 2626.18]  techniques to
[2626.18 --> 2626.62]  make learning
[2626.62 --> 2627.70]  to code educational
[2627.70 --> 2628.66]  as well as
[2628.66 --> 2629.70]  memorable giving
[2629.70 --> 2630.30]  you the confidence
[2630.30 --> 2631.02]  you need to
[2631.02 --> 2631.80]  continue past the
[2631.80 --> 2632.12]  hurdles
[2632.12 --> 2633.34]  they're always
[2633.34 --> 2634.04]  launching new
[2634.04 --> 2635.28]  courses on new
[2635.28 --> 2636.18]  technologies and
[2636.18 --> 2636.82]  offering deep
[2636.82 --> 2638.16]  dives on tried
[2638.16 --> 2638.90]  and true languages
[2638.90 --> 2639.82]  so if you don't
[2639.82 --> 2640.54]  see them you need
[2640.54 --> 2641.76]  suggest a course
[2641.76 --> 2642.64]  and they'll build
[2642.64 --> 2643.22]  it if there's
[2643.22 --> 2643.84]  enough demand
[2643.84 --> 2645.42]  CodeSchool also
[2645.42 --> 2646.34]  knows that languages
[2646.34 --> 2646.96]  are a moving
[2646.96 --> 2647.30]  target
[2647.30 --> 2648.28]  they're always
[2648.28 --> 2649.20]  updating content
[2649.20 --> 2649.74]  to give you the
[2649.74 --> 2650.46]  latest and
[2650.46 --> 2651.12]  greatest learning
[2651.12 --> 2651.68]  resources
[2651.68 --> 2653.10]  you can even
[2653.10 --> 2654.04]  try before you
[2654.04 --> 2655.30]  buy roughly one
[2655.30 --> 2656.34]  out of every five
[2656.34 --> 2657.66]  courses on CodeSchool
[2657.66 --> 2658.98]  is free this
[2658.98 --> 2660.16]  includes introductory
[2660.16 --> 2661.26]  classes for Git
[2661.26 --> 2662.92]  Ruby and jQuery
[2662.92 --> 2663.68]  which allow free
[2663.68 --> 2664.36]  members to play
[2664.36 --> 2666.16]  full courses with
[2666.16 --> 2666.92]  coding challenges
[2666.92 --> 2668.22]  included you can
[2668.22 --> 2669.64]  also pay as you
[2669.64 --> 2671.38]  go one monthly fee
[2671.38 --> 2672.16]  gives you full
[2672.16 --> 2673.68]  access to every
[2673.68 --> 2674.62]  CodeSchool course
[2674.62 --> 2675.66]  and if you ever
[2675.66 --> 2676.42]  need a breather
[2676.42 --> 2677.34]  take a break
[2677.34 --> 2678.30]  you can suspend
[2678.30 --> 2679.08]  your account at
[2679.08 --> 2679.68]  any time
[2679.68 --> 2680.52]  don't worry
[2680.52 --> 2681.28]  your account
[2681.28 --> 2682.58]  history points
[2682.58 --> 2683.34]  and badges
[2683.34 --> 2684.38]  will all be there
[2684.38 --> 2685.10]  when you're ready
[2685.10 --> 2685.70]  to pick things up
[2685.70 --> 2686.00]  again
[2686.00 --> 2687.12]  get started on
[2687.12 --> 2687.62]  sharpening your
[2687.62 --> 2688.26]  skills today
[2688.26 --> 2689.74]  at CodeSchool.com
[2689.74 --> 2690.58]  once again
[2690.58 --> 2692.32]  that's CodeSchool.com
[2692.32 --> 2695.86]  so while we're
[2695.86 --> 2696.50]  talking about I
[2696.50 --> 2697.26]  guess the future
[2697.26 --> 2699.70]  of GitHub Archive
[2699.70 --> 2700.76]  what are some of
[2700.76 --> 2701.66]  the ways that the
[2701.66 --> 2702.36]  community can step
[2702.36 --> 2702.64]  in
[2702.64 --> 2703.80]  we always ask a
[2703.80 --> 2704.38]  question like
[2704.38 --> 2705.24]  you know
[2705.24 --> 2705.96]  what's a call to
[2705.96 --> 2706.58]  arms for GitHub
[2706.58 --> 2707.12]  Archive
[2707.12 --> 2708.30]  that doesn't
[2708.30 --> 2709.26]  require you to
[2709.26 --> 2709.90]  do every single
[2709.90 --> 2710.14]  thing
[2710.14 --> 2710.54]  work in the
[2710.54 --> 2710.76]  community
[2710.76 --> 2711.30]  step in
[2711.30 --> 2712.08]  to help out
[2712.08 --> 2712.72]  on this project
[2712.72 --> 2713.76]  so I'd say
[2713.76 --> 2714.34]  two things
[2714.34 --> 2715.26]  one is
[2715.26 --> 2716.08]  just go and
[2716.08 --> 2716.44]  play with the
[2716.44 --> 2716.62]  data
[2716.62 --> 2717.20]  I think that's
[2717.20 --> 2717.72]  the best place
[2717.72 --> 2718.08]  to start
[2718.08 --> 2719.72]  because if you
[2719.72 --> 2720.38]  get hooked on
[2720.38 --> 2720.72]  that data
[2720.72 --> 2721.10]  and I think
[2721.10 --> 2721.72]  it's pretty easy
[2721.72 --> 2722.82]  to get hooked
[2722.82 --> 2723.26]  because there's
[2723.26 --> 2723.84]  so much of it
[2723.84 --> 2724.24]  and you can
[2724.24 --> 2724.98]  analyze all kinds
[2724.98 --> 2725.28]  of stuff
[2725.28 --> 2726.12]  then it just
[2726.12 --> 2726.60]  becomes much
[2726.60 --> 2727.04]  more interesting
[2727.04 --> 2727.60]  in the long run
[2727.60 --> 2729.02]  like you start
[2729.02 --> 2730.20]  thinking of new
[2730.20 --> 2730.88]  things you could
[2730.88 --> 2731.76]  figure out
[2731.76 --> 2732.32]  based on this
[2732.32 --> 2732.56]  data
[2732.56 --> 2733.38]  so that's one
[2733.38 --> 2734.88]  just start
[2734.88 --> 2735.34]  playing with the
[2735.34 --> 2735.56]  data
[2735.56 --> 2736.28]  you can either
[2736.28 --> 2736.94]  grab the
[2736.94 --> 2737.80]  raw archives
[2737.80 --> 2738.22]  the JSON
[2738.22 --> 2738.82]  stuff and just
[2738.82 --> 2739.16]  do something
[2739.16 --> 2739.56]  with it
[2739.56 --> 2740.26]  or you can
[2740.26 --> 2740.58]  try the
[2740.58 --> 2740.82]  BigQuery
[2740.82 --> 2741.78]  approach
[2741.78 --> 2742.38]  and the
[2742.38 --> 2742.78]  second one
[2742.78 --> 2743.56]  is if you
[2743.56 --> 2743.98]  are interested
[2743.98 --> 2744.34]  in helping
[2744.34 --> 2745.34]  out the
[2745.34 --> 2745.98]  project that I
[2745.98 --> 2746.24]  mentioned
[2746.24 --> 2747.06]  where it's
[2747.06 --> 2747.48]  just about
[2747.48 --> 2748.10]  re-importing
[2748.10 --> 2748.40]  the old
[2748.40 --> 2748.66]  data
[2748.66 --> 2750.12]  that can be
[2750.12 --> 2750.50]  interesting
[2750.50 --> 2751.42]  and if that's
[2751.42 --> 2751.90]  something that
[2751.90 --> 2752.48]  you want to
[2752.48 --> 2752.88]  help with
[2752.88 --> 2753.42]  that'd be
[2753.42 --> 2753.96]  cool
[2753.96 --> 2755.06]  so is that
[2755.06 --> 2755.80]  still an
[2755.80 --> 2756.22]  in-progress
[2756.22 --> 2756.78]  project then
[2756.78 --> 2757.64]  the re-import
[2757.64 --> 2758.42]  you're talking
[2758.42 --> 2758.62]  about the
[2758.62 --> 2759.08]  tables right
[2759.08 --> 2759.44]  breaking up
[2759.44 --> 2760.12]  one big table
[2760.12 --> 2760.50]  into many
[2760.50 --> 2761.40]  smaller tables
[2761.40 --> 2761.62]  right
[2761.62 --> 2762.76]  yeah
[2762.76 --> 2763.40]  so is that
[2763.40 --> 2763.80]  still going
[2763.80 --> 2764.14]  on then
[2764.14 --> 2765.06]  well it's
[2765.06 --> 2765.34]  one of the
[2765.34 --> 2766.00]  things that
[2766.00 --> 2766.56]  you know
[2766.56 --> 2766.98]  on my
[2766.98 --> 2767.44]  to-do
[2767.44 --> 2768.36]  project list
[2768.36 --> 2769.04]  of a hundred
[2769.04 --> 2769.56]  things that I
[2769.56 --> 2769.74]  need to
[2769.74 --> 2770.14]  yak shave
[2770.14 --> 2771.92]  it's there
[2771.92 --> 2773.00]  it's just a
[2773.00 --> 2773.42]  question of
[2773.42 --> 2774.08]  when will I
[2774.08 --> 2774.92]  get to it
[2774.92 --> 2776.16]  so is there
[2776.16 --> 2776.70]  currently an
[2776.70 --> 2777.22]  issue open
[2777.22 --> 2777.80]  with some
[2777.80 --> 2779.04]  like guide
[2779.04 --> 2779.68]  marks or
[2779.68 --> 2780.58]  guidelines for
[2780.58 --> 2780.92]  someone to
[2780.92 --> 2781.30]  step in and
[2781.30 --> 2781.64]  help out
[2781.64 --> 2781.74]  there
[2781.74 --> 2782.24]  that's a
[2782.24 --> 2782.60]  good point
[2782.60 --> 2783.36]  there isn't
[2783.36 --> 2783.94]  and I
[2783.94 --> 2785.30]  will do
[2785.30 --> 2785.58]  that
[2785.58 --> 2786.74]  yeah
[2786.74 --> 2787.08]  I think
[2787.08 --> 2787.42]  that would
[2787.42 --> 2787.80]  be helpful
[2787.80 --> 2788.42]  especially
[2788.42 --> 2789.06]  you know
[2789.06 --> 2789.34]  I like
[2789.34 --> 2790.54]  when project
[2790.54 --> 2790.88]  owners
[2790.88 --> 2791.44]  you know
[2791.44 --> 2791.66]  if they
[2791.66 --> 2792.18]  haven't asked
[2792.18 --> 2792.66]  like that
[2792.66 --> 2792.90]  you know
[2792.90 --> 2793.12]  if they
[2793.12 --> 2793.66]  can put
[2793.66 --> 2794.06]  something out
[2794.06 --> 2794.16]  there
[2794.16 --> 2794.60]  because you're
[2794.60 --> 2795.00]  going to get
[2795.00 --> 2795.34]  a question
[2795.34 --> 2795.62]  anyway
[2795.62 --> 2795.96]  someone will
[2795.96 --> 2796.20]  start the
[2796.20 --> 2796.60]  issue for you
[2796.60 --> 2796.92]  if you don't
[2796.92 --> 2798.36]  so might as
[2798.36 --> 2798.80]  as well give
[2798.80 --> 2799.42]  someone some
[2799.42 --> 2800.52]  guide rails
[2800.52 --> 2801.06]  to follow
[2801.06 --> 2802.40]  and that way
[2802.40 --> 2803.06]  people can step
[2803.06 --> 2803.60]  in so if
[2803.60 --> 2804.48]  you're wanting
[2804.48 --> 2804.96]  to hack on
[2804.96 --> 2805.46]  big query
[2805.46 --> 2806.20]  or play with
[2806.20 --> 2807.06]  you know
[2807.06 --> 2808.48]  breaking up
[2808.48 --> 2808.86]  these tables
[2808.86 --> 2809.28]  into smaller
[2809.28 --> 2809.62]  tables
[2809.62 --> 2810.46]  then you know
[2810.46 --> 2810.96]  Ilya will give
[2810.96 --> 2811.92]  you some help
[2811.92 --> 2812.64]  on making that
[2812.64 --> 2812.88]  happen
[2812.88 --> 2813.38]  yeah I'll do
[2813.38 --> 2814.30]  that I'll definitely
[2814.30 --> 2815.22]  put something
[2815.22 --> 2815.66]  together
[2815.66 --> 2817.08]  well
[2817.08 --> 2818.20]  so many
[2818.20 --> 2818.60]  yaks
[2818.60 --> 2819.00]  so little
[2819.00 --> 2819.28]  time
[2819.28 --> 2819.84]  yes
[2819.84 --> 2820.56]  pretty much
[2820.56 --> 2821.06]  yes
[2821.06 --> 2822.42]  is there a
[2822.42 --> 2823.04]  t-shirt for that
[2823.04 --> 2823.76]  because I like that
[2823.76 --> 2824.54]  there should be
[2824.54 --> 2825.84]  yeah that'd be a
[2825.84 --> 2826.42]  nice yak shave
[2826.42 --> 2827.22]  go make a t-shirt
[2827.22 --> 2828.30]  about yak shave
[2828.30 --> 2828.56]  okay
[2828.56 --> 2829.86]  another question
[2829.86 --> 2830.50]  that we like to
[2830.50 --> 2831.06]  ask at the end
[2831.06 --> 2831.34]  and I know
[2831.34 --> 2831.70]  you've been
[2831.70 --> 2832.58]  lacking your
[2832.58 --> 2833.10]  email lately
[2833.10 --> 2834.26]  but you're a
[2834.26 --> 2834.76]  guy who
[2834.76 --> 2835.64]  has his thumb
[2835.64 --> 2836.42]  on the pulse
[2836.42 --> 2837.06]  of open source
[2837.06 --> 2838.18]  I think your
[2838.18 --> 2838.70]  twitter account
[2838.70 --> 2839.82]  is a good one
[2839.82 --> 2840.34]  that I follow
[2840.34 --> 2841.52]  just constantly
[2841.52 --> 2842.82]  kind of surfacing
[2842.82 --> 2843.72]  cool new projects
[2843.72 --> 2844.86]  so what are
[2844.86 --> 2845.52]  some projects
[2845.52 --> 2846.24]  name one or a
[2846.24 --> 2846.76]  couple that are
[2846.76 --> 2847.36]  on your radar
[2847.36 --> 2847.88]  that are exciting
[2847.88 --> 2848.40]  to you
[2848.40 --> 2849.80]  these days
[2849.80 --> 2851.44]  these days
[2851.44 --> 2851.94]  well
[2851.94 --> 2853.66]  so I guess
[2853.66 --> 2854.82]  the main
[2854.82 --> 2855.20]  open source
[2855.20 --> 2855.84]  project that I
[2855.84 --> 2856.68]  spend probably
[2856.68 --> 2857.26]  most of my
[2857.26 --> 2857.96]  time on nowadays
[2857.96 --> 2858.60]  is chromium
[2858.60 --> 2859.56]  so that's
[2859.56 --> 2860.12]  definitely something
[2860.12 --> 2861.10]  that's very
[2861.10 --> 2861.50]  interesting
[2861.50 --> 2862.24]  exciting to me
[2862.24 --> 2862.62]  and I keep
[2862.62 --> 2863.14]  learning new
[2863.14 --> 2863.84]  things about it
[2863.84 --> 2864.70]  and if you're
[2864.70 --> 2865.12]  not familiar
[2865.12 --> 2866.00]  chromium is the
[2866.00 --> 2866.74]  open source
[2866.74 --> 2868.22]  version of
[2868.22 --> 2869.14]  the chrome
[2869.14 --> 2869.58]  project
[2869.58 --> 2869.88]  the chrome
[2869.88 --> 2870.18]  browser
[2870.18 --> 2870.68]  so there's a
[2870.68 --> 2871.20]  chromium browser
[2871.20 --> 2871.54]  which you can
[2871.54 --> 2872.04]  build on your
[2872.04 --> 2872.24]  own
[2872.24 --> 2872.92]  and then
[2872.92 --> 2873.26]  chrome
[2873.26 --> 2873.54]  is kind
[2873.54 --> 2873.74]  of the
[2873.74 --> 2874.20]  repackaged
[2874.20 --> 2874.52]  version
[2874.52 --> 2874.86]  that just
[2874.86 --> 2875.54]  adds the
[2875.54 --> 2875.82]  kind of
[2875.82 --> 2876.12]  the google
[2876.12 --> 2876.58]  branding
[2876.58 --> 2876.98]  on top
[2876.98 --> 2877.22]  of it
[2877.22 --> 2877.70]  and a few
[2877.70 --> 2877.98]  additional
[2877.98 --> 2878.34]  things
[2878.34 --> 2880.08]  so I
[2880.08 --> 2880.48]  spend most
[2880.48 --> 2880.68]  of my
[2880.68 --> 2881.02]  days
[2881.02 --> 2881.90]  working on
[2881.90 --> 2882.14]  that
[2882.14 --> 2882.66]  trying to
[2882.66 --> 2883.02]  figure out
[2883.02 --> 2883.28]  what are
[2883.28 --> 2883.60]  the things
[2883.60 --> 2883.86]  that we
[2883.86 --> 2884.14]  need in
[2884.14 --> 2884.32]  there
[2884.32 --> 2884.72]  to make
[2884.72 --> 2885.20]  it faster
[2885.20 --> 2885.76]  or what
[2885.76 --> 2886.02]  are the
[2886.02 --> 2886.44]  performance
[2886.44 --> 2886.98]  regressions
[2886.98 --> 2887.30]  bugs
[2887.30 --> 2887.90]  and so on
[2887.90 --> 2888.30]  so forth
[2888.30 --> 2888.84]  so that's
[2888.84 --> 2889.32]  that's
[2889.32 --> 2889.50]  definitely
[2889.50 --> 2890.10]  been occupying
[2890.10 --> 2890.36]  a lot
[2890.36 --> 2890.56]  of my
[2890.56 --> 2890.82]  time
[2890.82 --> 2891.92]  and then
[2891.92 --> 2892.90]  others
[2892.90 --> 2893.50]  are
[2893.50 --> 2894.22]  actually
[2894.22 --> 2896.20]  HTTP2
[2896.20 --> 2896.66]  related
[2896.66 --> 2897.28]  so as we
[2897.28 --> 2897.64]  mentioned at the
[2897.64 --> 2898.06]  beginning of the
[2898.06 --> 2898.30]  show
[2898.30 --> 2899.42]  HTTP2 is now
[2899.42 --> 2900.00]  officially a
[2900.00 --> 2900.24]  thing
[2900.24 --> 2900.90]  as of
[2900.90 --> 2901.22]  I guess
[2901.22 --> 2901.60]  yesterday
[2901.60 --> 2903.04]  and now
[2903.04 --> 2903.52]  the big
[2903.52 --> 2904.26]  push is
[2904.26 --> 2904.56]  now that
[2904.56 --> 2904.92]  the spec
[2904.92 --> 2905.48]  is final
[2905.48 --> 2906.18]  and it's
[2906.18 --> 2906.52]  stable
[2906.52 --> 2907.32]  is to
[2907.32 --> 2907.98]  actually have
[2907.98 --> 2908.38]  servers
[2908.38 --> 2908.82]  supported
[2908.82 --> 2909.86]  if you
[2909.86 --> 2910.28]  think about
[2910.28 --> 2910.58]  let's say
[2910.58 --> 2910.98]  the Ruby
[2910.98 --> 2911.48]  ecosystem
[2911.48 --> 2912.58]  there's
[2912.58 --> 2913.20]  actually not
[2913.20 --> 2914.16]  any server
[2914.16 --> 2914.48]  that I'm
[2914.48 --> 2914.90]  aware of
[2914.90 --> 2915.44]  that is
[2915.44 --> 2916.10]  HTTP2
[2916.10 --> 2916.54]  compatible
[2916.54 --> 2916.94]  at this
[2916.94 --> 2917.14]  point
[2917.14 --> 2919.22]  so that's
[2919.22 --> 2919.98]  that's
[2919.98 --> 2920.58]  something that
[2920.58 --> 2921.10]  I'm
[2921.10 --> 2922.00]  thinking about
[2922.00 --> 2922.60]  actively right
[2922.60 --> 2922.84]  now
[2922.84 --> 2923.26]  there's
[2923.26 --> 2923.62]  if you
[2923.62 --> 2923.88]  go to
[2923.88 --> 2924.06]  the
[2924.06 --> 2924.84]  HTTP2
[2924.84 --> 2925.28]  wiki
[2925.28 --> 2926.16]  if you
[2926.16 --> 2926.52]  just search
[2926.52 --> 2926.74]  for
[2926.74 --> 2927.54]  HTTP2
[2927.54 --> 2928.20]  on Google
[2928.20 --> 2929.06]  or use
[2929.06 --> 2929.50]  your other
[2929.50 --> 2929.84]  favorite
[2929.84 --> 2930.14]  search
[2930.14 --> 2930.42]  engine
[2930.42 --> 2931.34]  you'll
[2931.34 --> 2931.90]  you'll
[2931.90 --> 2932.64]  arrive at
[2932.64 --> 2933.30]  just kind
[2933.30 --> 2933.52]  of a
[2933.52 --> 2934.08]  status page
[2934.08 --> 2934.68]  for HTTP2
[2934.68 --> 2934.98]  if you
[2934.98 --> 2935.26]  click on
[2935.26 --> 2935.94]  implementations
[2935.94 --> 2936.34]  there's a
[2936.34 --> 2936.66]  list of
[2936.66 --> 2936.98]  servers
[2936.98 --> 2937.34]  that are
[2937.34 --> 2937.58]  already
[2937.58 --> 2938.04]  implemented
[2938.04 --> 2940.06]  and a
[2940.06 --> 2940.38]  lot of
[2940.38 --> 2940.78]  those
[2940.78 --> 2942.30]  could use
[2942.30 --> 2942.76]  some help
[2942.76 --> 2943.26]  in terms
[2943.26 --> 2943.82]  of like
[2943.82 --> 2945.06]  contributions
[2945.06 --> 2945.78]  testing
[2945.78 --> 2946.20]  them
[2946.20 --> 2947.16]  compatibility
[2947.16 --> 2947.90]  with other
[2947.90 --> 2948.24]  browsers
[2948.24 --> 2949.00]  and all
[2949.00 --> 2949.30]  the rest
[2949.30 --> 2949.88]  so if
[2949.88 --> 2950.00]  you're
[2950.00 --> 2950.22]  interested
[2950.22 --> 2950.50]  in that
[2950.50 --> 2950.68]  sort
[2950.68 --> 2950.78]  of
[2950.78 --> 2950.98]  thing
[2950.98 --> 2951.34]  that's
[2951.34 --> 2951.58]  definitely
[2951.58 --> 2952.04]  something
[2952.04 --> 2952.48]  that I
[2952.48 --> 2953.42]  would
[2953.42 --> 2953.72]  encourage
[2953.72 --> 2954.02]  others
[2954.02 --> 2954.24]  to
[2954.24 --> 2954.48]  play
[2954.48 --> 2954.72]  with
[2954.72 --> 2956.52]  excellent
[2956.52 --> 2956.90]  I think
[2956.90 --> 2957.02]  I'll
[2957.02 --> 2957.36]  just give
[2957.36 --> 2957.58]  you a
[2957.58 --> 2957.96]  plug as
[2957.96 --> 2958.14]  well
[2958.14 --> 2958.46]  because you
[2958.46 --> 2958.78]  won't take
[2958.78 --> 2959.24]  it yourself
[2959.24 --> 2960.56]  you also
[2960.56 --> 2961.74]  have a
[2961.74 --> 2962.22]  book out
[2962.22 --> 2962.88]  high performance
[2962.88 --> 2963.36]  browser
[2963.36 --> 2963.94]  networking
[2963.94 --> 2964.64]  it's an
[2964.64 --> 2964.98]  O'Reilly
[2964.98 --> 2965.40]  book
[2965.40 --> 2966.66]  looks like
[2966.66 --> 2966.84]  you can
[2966.84 --> 2967.08]  read the
[2967.08 --> 2967.40]  entire
[2967.40 --> 2967.68]  thing
[2967.68 --> 2967.96]  online
[2967.96 --> 2968.54]  for free
[2968.54 --> 2969.96]  or buy
[2969.96 --> 2970.34]  it for a
[2970.34 --> 2970.82]  few bucks
[2970.82 --> 2972.06]  definitely
[2972.06 --> 2972.58]  if you guys
[2972.58 --> 2973.04]  are interested
[2973.04 --> 2973.46]  in these
[2973.46 --> 2973.78]  types of
[2973.78 --> 2974.20]  things
[2974.20 --> 2975.40]  HTTP2
[2975.40 --> 2975.96]  XHR
[2975.96 --> 2976.52]  improvements
[2976.52 --> 2977.18]  server
[2977.18 --> 2977.38]  set
[2977.38 --> 2977.66]  events
[2977.66 --> 2977.94]  that kind
[2977.94 --> 2978.30]  of stuff
[2978.30 --> 2978.84]  I
[2978.84 --> 2979.14]  haven't read
[2979.14 --> 2991.06]  I haven't
[2991.06 --> 2991.26]  read the
[2991.26 --> 2991.38]  book
[2991.38 --> 2992.44]  I do
[2992.44 --> 2992.74]  have a
[2992.74 --> 2993.04]  section
[2993.04 --> 2993.38]  in the
[2993.38 --> 2993.52]  book
[2993.52 --> 2993.76]  so
[2993.76 --> 2994.84]  as you
[2994.84 --> 2995.06]  mentioned
[2995.06 --> 2995.36]  the book
[2995.36 --> 2995.86]  is online
[2995.86 --> 2996.28]  for free
[2996.28 --> 2996.56]  so if
[2996.56 --> 2996.76]  you just
[2996.76 --> 2997.14]  go to
[2997.14 --> 2999.52]  hpbn.co
[2999.52 --> 3001.00]  you'll
[3001.00 --> 3001.64]  arrive at a
[3001.64 --> 3002.00]  page where
[3002.00 --> 3002.30]  you can
[3002.30 --> 3002.90]  flip through
[3002.90 --> 3003.00]  it
[3003.00 --> 3003.38]  and there's
[3003.38 --> 3003.50]  an
[3003.50 --> 3003.92]  HTTP2
[3003.92 --> 3004.18]  chapter
[3004.18 --> 3004.50]  in there
[3004.50 --> 3004.88]  but I
[3004.88 --> 3005.24]  wrote that
[3005.24 --> 3005.56]  chapter
[3005.56 --> 3006.32]  about a
[3006.32 --> 3006.82]  year ago
[3006.82 --> 3007.78]  and since
[3007.78 --> 3008.30]  then there's
[3008.30 --> 3009.00]  been some
[3009.00 --> 3009.66]  protocol
[3009.66 --> 3010.06]  changes
[3010.06 --> 3011.44]  that I
[3011.44 --> 3011.68]  need to
[3011.68 --> 3012.18]  go back
[3012.18 --> 3012.88]  and update
[3012.88 --> 3014.28]  but that's
[3014.28 --> 3015.42]  true of
[3015.42 --> 3015.98]  any tech
[3015.98 --> 3016.34]  book in
[3016.34 --> 3016.62]  general
[3016.62 --> 3017.28]  the moment
[3017.28 --> 3017.56]  you hit
[3017.56 --> 3017.88]  publish
[3017.88 --> 3018.36]  it's already
[3018.36 --> 3018.86]  out of date
[3018.86 --> 3019.18]  so
[3019.18 --> 3021.86]  we'll definitely
[3021.86 --> 3022.50]  link that up
[3022.50 --> 3022.84]  in the show
[3022.84 --> 3023.22]  notes for
[3023.22 --> 3023.58]  people who
[3023.58 --> 3024.00]  are interested
[3024.00 --> 3024.72]  remember you
[3024.72 --> 3025.14]  mentioned
[3025.14 --> 3026.44]  HTTP2
[3026.44 --> 3027.04]  as well
[3027.04 --> 3027.50]  that's
[3027.50 --> 3028.10]  fresh
[3028.10 --> 3028.62]  off the
[3028.62 --> 3028.86]  press
[3028.86 --> 3029.32]  as of
[3029.32 --> 3029.72]  basically
[3029.72 --> 3030.34]  last night
[3030.34 --> 3030.68]  so
[3030.68 --> 3032.90]  don't expect
[3032.90 --> 3033.20]  you to go
[3033.20 --> 3034.98]  update the
[3034.98 --> 3035.70]  book today
[3035.70 --> 3035.98]  or anything
[3035.98 --> 3036.62]  I'm actually
[3036.62 --> 3037.24]  hoping to
[3037.24 --> 3038.08]  get it done
[3038.08 --> 3038.60]  sooner rather
[3038.60 --> 3038.98]  than later
[3038.98 --> 3039.52]  because I
[3039.52 --> 3040.06]  think there's
[3040.06 --> 3040.44]  a lot of
[3040.44 --> 3040.90]  interest right
[3040.90 --> 3041.42]  now in the
[3041.42 --> 3041.78]  community
[3041.78 --> 3042.78]  what is this
[3042.78 --> 3043.38]  thing how do I
[3043.38 --> 3043.96]  make it work
[3043.96 --> 3044.90]  what does it
[3044.90 --> 3045.76]  mean for the
[3045.76 --> 3046.90]  servers what does
[3046.90 --> 3047.42]  it mean for my
[3047.42 --> 3048.60]  website so this
[3048.60 --> 3049.26]  would be a good
[3049.26 --> 3049.98]  time to actually
[3049.98 --> 3050.50]  have that out
[3050.50 --> 3051.32]  so I'm hoping
[3051.32 --> 3052.42]  that within the
[3052.42 --> 3053.76]  next fingers
[3053.76 --> 3054.74]  crossed couple
[3054.74 --> 3055.32]  of weeks unless
[3055.32 --> 3056.00]  I find other
[3056.00 --> 3056.62]  yaks to shave
[3056.62 --> 3057.96]  I'll have that
[3057.96 --> 3058.20]  up
[3058.20 --> 3059.62]  we'll have to
[3059.62 --> 3060.04]  have you come
[3060.04 --> 3060.66]  back and talk
[3060.66 --> 3061.66]  HTTP2 because
[3061.66 --> 3062.62]  I have a lot of
[3062.62 --> 3063.28]  questions about it
[3063.28 --> 3064.10]  and I'm sure you've
[3064.10 --> 3064.50]  got a lot of
[3064.50 --> 3065.14]  answers so I think
[3065.14 --> 3065.58]  that'd be a good
[3065.58 --> 3065.84]  time
[3065.84 --> 3066.20]  yeah I'd be
[3066.20 --> 3066.62]  happy to
[3066.62 --> 3067.98]  let's do it
[3067.98 --> 3068.40]  let's get on
[3068.40 --> 3068.86]  the books
[3068.86 --> 3069.70]  four weeks
[3069.70 --> 3070.94]  from now
[3070.94 --> 3071.26]  damn
[3071.26 --> 3071.86]  done
[3071.86 --> 3075.34]  well it was
[3075.34 --> 3076.24]  definitely fun
[3076.24 --> 3077.10]  having you on
[3077.10 --> 3077.80]  the call today
[3077.80 --> 3079.62]  we'll definitely
[3079.62 --> 3080.28]  enjoy working with
[3080.28 --> 3082.24]  you on keeping
[3082.24 --> 3083.08]  the emails
[3083.08 --> 3084.16]  current looking
[3084.16 --> 3084.90]  awesome on
[3084.90 --> 3085.46]  mobile and
[3085.46 --> 3086.46]  desktop frequent
[3086.46 --> 3088.24]  and exploring new
[3088.24 --> 3089.46]  frontiers with
[3089.46 --> 3090.36]  that as well so
[3090.36 --> 3091.30]  definitely excited
[3091.30 --> 3092.04]  about the future
[3092.04 --> 3092.70]  of working with
[3092.70 --> 3093.02]  you on that
[3093.02 --> 3093.56]  part there
[3093.56 --> 3095.04]  you mentioned
[3095.04 --> 3096.74]  githubarchive.org
[3096.74 --> 3097.66]  will have an
[3097.66 --> 3098.14]  update
[3098.14 --> 3099.10]  mentioning
[3099.10 --> 3100.26]  changelog nightly
[3100.26 --> 3101.08]  if you're going
[3101.08 --> 3101.50]  to subscribe
[3101.50 --> 3102.14]  go to
[3102.14 --> 3103.48]  the changelog.com
[3103.48 --> 3104.62]  slash nightly
[3104.62 --> 3105.28]  you can subscribe
[3105.28 --> 3105.78]  there
[3105.78 --> 3106.72]  when you're
[3106.72 --> 3107.16]  listening to this
[3107.16 --> 3107.60]  we should be
[3107.60 --> 3108.16]  shipping emails
[3108.16 --> 3109.24]  so expect
[3109.24 --> 3110.40]  an email
[3110.40 --> 3110.98]  like the next
[3110.98 --> 3111.26]  night
[3111.26 --> 3111.58]  I think we're
[3111.58 --> 3112.04]  shipping what
[3112.04 --> 3112.66]  Jared at
[3112.66 --> 3113.18]  10 o'clock
[3113.18 --> 3114.88]  on central time
[3114.88 --> 3115.76]  or eastern time
[3115.76 --> 3116.44]  central
[3116.44 --> 3118.06]  so 10pm central
[3118.06 --> 3118.46]  because Jared
[3118.46 --> 3118.90]  and I live in
[3118.90 --> 3119.30]  central and
[3119.30 --> 3119.66]  that's like the
[3119.66 --> 3119.92]  center of the
[3119.92 --> 3120.44]  world to us
[3120.44 --> 3121.30]  because it's
[3121.30 --> 3121.94]  central right
[3121.94 --> 3122.62]  that's right
[3122.62 --> 3123.16]  they call the
[3123.16 --> 3124.20]  central time
[3124.20 --> 3124.72]  zone for a
[3124.72 --> 3124.94]  reason
[3124.94 --> 3125.34]  it's the
[3125.34 --> 3125.54]  center
[3125.54 --> 3126.34]  humor
[3126.34 --> 3126.98]  arrogance
[3126.98 --> 3127.32]  there
[3127.32 --> 3127.68]  that's what
[3127.68 --> 3128.04]  that is
[3128.04 --> 3129.02]  humorous
[3129.02 --> 3129.38]  arrogance
[3129.38 --> 3131.22]  that we're
[3131.22 --> 3131.58]  going to ship
[3131.58 --> 3132.22]  at our time
[3132.22 --> 3132.56]  at 10
[3132.56 --> 3133.00]  so if you're
[3133.00 --> 3133.42]  on the other
[3133.42 --> 3133.72]  side of the
[3133.72 --> 3133.90]  world
[3133.90 --> 3135.08]  we can't
[3135.08 --> 3135.48]  help that
[3135.48 --> 3135.78]  so it'll be
[3135.78 --> 3136.44]  like 10
[3136.44 --> 3136.88]  in the afternoon
[3136.88 --> 3137.24]  for you or
[3137.24 --> 3137.52]  something like
[3137.52 --> 3137.74]  that
[3137.74 --> 3139.72]  that'll be the
[3139.72 --> 3140.20]  changelog
[3140.20 --> 3141.02]  afternoonly
[3141.02 --> 3142.60]  doesn't have
[3142.60 --> 3143.00]  the same ring
[3143.00 --> 3143.32]  to it
[3143.32 --> 3145.70]  and if you're
[3145.70 --> 3146.42]  a fan of the
[3146.42 --> 3147.06]  show you know
[3147.06 --> 3148.06]  back in episode
[3148.06 --> 3149.14]  141
[3149.14 --> 3150.58]  we had a pretty
[3150.58 --> 3151.42]  decent announcement
[3151.42 --> 3152.46]  that I came on
[3152.46 --> 3153.90]  as a full-time
[3153.90 --> 3155.48]  employee of
[3155.48 --> 3155.92]  this here
[3155.92 --> 3156.66]  fledgling company
[3156.66 --> 3157.02]  we're building
[3157.02 --> 3157.32]  called the
[3157.32 --> 3157.82]  changelog
[3157.82 --> 3159.50]  I once worked
[3159.50 --> 3160.36]  for a non-profit
[3160.36 --> 3161.86]  full-time there
[3161.86 --> 3162.68]  and stepped away
[3162.68 --> 3163.88]  to pursue the
[3163.88 --> 3164.52]  dreams of
[3164.52 --> 3165.88]  keeping up
[3165.88 --> 3167.28]  with open source
[3167.28 --> 3167.84]  and serving the
[3167.84 --> 3168.36]  open source community
[3168.36 --> 3170.12]  so this is now
[3170.12 --> 3171.36]  my full-time gig
[3171.36 --> 3172.88]  and as part of that
[3172.88 --> 3174.14]  we ask our
[3174.14 --> 3174.76]  listeners to
[3174.76 --> 3175.40]  become members
[3175.40 --> 3176.06]  supporting members
[3176.06 --> 3176.28]  of the
[3176.28 --> 3176.68]  changelog
[3176.68 --> 3177.54]  you can go to
[3177.54 --> 3178.62]  the changelog.com
[3178.62 --> 3179.60]  membership to
[3179.60 --> 3180.12]  learn more
[3180.12 --> 3181.10]  but right now
[3181.10 --> 3182.12]  I'm gonna rattle
[3182.12 --> 3182.96]  off a list
[3182.96 --> 3183.48]  of I don't know
[3183.48 --> 3183.86]  how many
[3183.86 --> 3184.82]  but quite a few
[3184.82 --> 3185.84]  members that have
[3185.84 --> 3186.46]  stepped up in
[3186.46 --> 3186.88]  support of the
[3186.88 --> 3187.42]  changelog
[3187.42 --> 3189.08]  Gabriel Solis
[3189.08 --> 3190.28]  forgive me if I
[3190.28 --> 3191.06]  mispronounce a few
[3191.06 --> 3191.48]  names here
[3191.48 --> 3192.22]  because some of
[3192.22 --> 3193.56]  them do have
[3193.56 --> 3193.98]  nine letters
[3193.98 --> 3194.60]  like my last
[3194.60 --> 3195.72]  name or like
[3195.72 --> 3196.26]  Gregorick
[3196.26 --> 3197.72]  Jonathan
[3197.72 --> 3199.58]  Lewaniski
[3199.58 --> 3200.78]  sorry if I
[3200.78 --> 3201.24]  messed that one
[3201.24 --> 3201.50]  up
[3201.50 --> 3202.74]  Darcy Clark
[3202.74 --> 3203.90]  Mike Oliveri
[3203.90 --> 3204.70]  Todd Ward
[3204.70 --> 3206.46]  Colin Coghill
[3206.46 --> 3208.20]  G.D.
[3208.34 --> 3208.80]  Jensen
[3208.80 --> 3209.92]  Magnus
[3209.92 --> 3210.50]  Enger
[3210.50 --> 3210.90]  that's an
[3210.90 --> 3211.40]  awesome name
[3211.40 --> 3212.60]  Benoit
[3212.60 --> 3213.26]  Tijanat
[3213.26 --> 3213.76]  I believe
[3213.76 --> 3214.76]  that definitely
[3214.76 --> 3215.36]  messed that one
[3215.36 --> 3215.72]  up that's
[3215.72 --> 3216.16]  French though
[3216.16 --> 3216.88]  so you can
[3216.88 --> 3217.92]  I get a buy
[3217.92 --> 3218.34]  on French
[3218.34 --> 3218.76]  names
[3218.76 --> 3219.78]  Charles Hicks
[3219.78 --> 3220.82]  this one I
[3220.82 --> 3221.10]  can't even
[3221.10 --> 3221.54]  pronounce
[3221.54 --> 3223.68]  Penna Goddess
[3223.68 --> 3224.46]  I'm not even
[3224.46 --> 3224.90]  sure of that one
[3224.90 --> 3225.62]  sorry about that
[3225.62 --> 3226.56]  David
[3226.56 --> 3227.30]  can't see your
[3227.30 --> 3228.00]  last time either
[3228.00 --> 3229.26]  Steven
[3229.26 --> 3230.38]  Howes
[3230.38 --> 3230.80]  Brett
[3230.80 --> 3231.38]  Weaver
[3231.38 --> 3231.80]  and
[3231.80 --> 3232.26]  Jan
[3232.26 --> 3232.96]  Novak
[3232.96 --> 3233.84]  all these
[3233.84 --> 3234.30]  awesome people
[3234.30 --> 3234.62]  have stepped
[3234.62 --> 3235.20]  up to
[3235.20 --> 3236.18]  make sure the
[3236.18 --> 3236.64]  changelog stays
[3236.64 --> 3237.34]  around and
[3237.34 --> 3238.00]  support us and
[3238.00 --> 3238.64]  going full time
[3238.64 --> 3240.18]  so if you want to
[3240.18 --> 3240.62]  do it too
[3240.62 --> 3241.40]  the changelog.com
[3241.40 --> 3241.96]  membership
[3241.96 --> 3242.68]  you got some
[3242.68 --> 3243.28]  awesome benefits
[3243.28 --> 3243.70]  there I won't
[3243.70 --> 3243.98]  tell you what
[3243.98 --> 3244.72]  there are now but
[3244.72 --> 3245.56]  lots of cool
[3245.56 --> 3246.12]  stuff on that
[3246.12 --> 3246.74]  page there check
[3246.74 --> 3247.18]  it out
[3247.18 --> 3249.04]  Ilya thanks again
[3249.04 --> 3249.70]  so much for
[3249.70 --> 3250.18]  coming on the
[3250.18 --> 3250.78]  show working with
[3250.78 --> 3251.34]  us on changelog
[3251.34 --> 3251.96]  nightly definitely
[3251.96 --> 3252.46]  excited about
[3252.46 --> 3253.02]  shipping that in
[3253.02 --> 3254.38]  the future we've
[3254.38 --> 3254.86]  got some awesome
[3254.86 --> 3255.42]  sponsors I think
[3255.42 --> 3255.96]  to mention as
[3255.96 --> 3256.58]  well let's see
[3256.58 --> 3257.46]  who those are
[3257.46 --> 3259.16]  code ship top
[3259.16 --> 3260.62]  towel and code
[3260.62 --> 3262.38]  school awesome
[3262.38 --> 3263.36]  people so with
[3263.36 --> 3263.78]  that let's say
[3263.78 --> 3264.34]  goodbye everybody
[3264.34 --> 3265.46]  goodbye
[3265.46 --> 3265.82]  bye
[3277.18 --> 3279.18]  bye

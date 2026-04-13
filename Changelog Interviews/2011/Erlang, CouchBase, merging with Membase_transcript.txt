[0.00 --> 6.00]  Yo Chris
[6.00 --> 7.62]  What up Claire?
[8.00 --> 10.72]  I gots a database problem that I gots to share
[10.72 --> 13.68]  I hate my SQL, it's giving me tears
[13.68 --> 16.56]  This alter table statement is gonna take years
[16.56 --> 19.26]  No need to trip on a funky query
[19.26 --> 21.80]  Use my producing JavaScript with CouchDB
[21.80 --> 24.78]  This schema lesson replicates using JSON
[24.78 --> 27.98]  Non-relational databases turn me on
[27.98 --> 29.54]  From now on I'll use CouchDB
[29.54 --> 30.68]  Updates
[30.68 --> 32.40]  I'm my sister's in CouchDB
[32.40 --> 50.28]  Welcome to the Changelog episode 0.5.4
[50.28 --> 51.50]  I'm Adam Stachowiak
[51.50 --> 52.90]  And I'm Wynne Netherland
[52.90 --> 55.30]  This is the Changelog, we cover what's fresh and new
[55.30 --> 56.46]  In the world of open source
[56.46 --> 58.58]  If you found us on iTunes, we're also on the web
[58.58 --> 59.92]  At thechangelog.com
[59.92 --> 61.02]  We're also up on GitHub
[61.02 --> 62.76]  Head to github.com slash explore
[62.76 --> 65.22]  You'll find some training reposts, some feature reposts from the blog
[65.22 --> 66.58]  As well as our audio podcast
[66.58 --> 68.92]  And if you're on Twitter, follow Changelog Show
[68.92 --> 70.30]  And me, Adam Stach
[70.30 --> 71.42]  And I'm Penguin
[71.42 --> 73.30]  P-E-N-G-W-I-N-N
[73.30 --> 75.22]  This episode is sponsored by GitHub Jobs
[75.22 --> 78.02]  Head to the changelog.com slash jobs to get started
[78.02 --> 80.26]  If you'd like us to feature your job on this show
[80.26 --> 82.82]  Select advertise on the changelog when posting your job
[82.82 --> 84.14]  And we will take care of the rest
[84.14 --> 87.10]  The irony of a real radio station
[87.10 --> 88.68]  Advertising on the fake radio
[88.68 --> 90.42]  Southern California Public Radio
[90.42 --> 92.84]  KPCC 89.3
[92.84 --> 93.72]  On your FM dial
[93.72 --> 95.72]  Looking for a Django Python developer
[95.72 --> 98.26]  That would report into the senior UX designer
[98.26 --> 100.70]  And implement HTML, CSS
[100.70 --> 103.38]  The Python Django templates
[103.38 --> 105.20]  Experience with Full Stack MVC
[105.20 --> 106.32]  MySQL Plus
[106.32 --> 108.94]  If you're in the Pasadena, California area
[108.94 --> 110.48]  Be sure and check out
[110.48 --> 113.00]  LG.gd slash 9s
[113.00 --> 114.96]  Fun episode this week
[114.96 --> 116.32]  Took a break from our
[116.32 --> 119.04]  Regularly scheduled design programs
[119.04 --> 120.88]  Save your emails, guys
[120.88 --> 121.30]  We know
[121.30 --> 124.12]  Two back-to-back design episodes
[124.12 --> 126.56]  Set off the switchboards
[126.56 --> 128.42]  But we're back to the no-sequel
[128.42 --> 130.40]  Talk to Chris Anderson
[130.40 --> 131.54]  Over at Couchbase
[131.54 --> 134.00]  About the Membase CouchDB merger
[134.00 --> 136.32]  And the full line of products that they have
[136.32 --> 137.18]  Let me ask you a question
[137.18 --> 138.78]  Did he have a brand new theme song, Ben?
[138.78 --> 140.62]  You know, he sent it to me
[140.62 --> 141.86]  We will put that in the show notes
[141.86 --> 143.68]  Actually, if you can cut it into the intro
[143.68 --> 144.58]  That would be awesome
[144.58 --> 145.32]  We'll try
[145.32 --> 147.04]  We'll do our best
[147.04 --> 148.84]  If you guys haven't caught the
[148.84 --> 150.38]  The ad hoc
[150.38 --> 152.18]  Theme show
[152.18 --> 153.06]  Or theme song
[153.06 --> 154.78]  That we recorded the first time
[154.78 --> 156.02]  I guess the no-sequel Smackdown
[156.02 --> 157.30]  At South by last year
[157.30 --> 158.82]  Chris was
[158.82 --> 160.38]  Was awesome in that little dilly
[160.38 --> 161.34]  It's
[161.34 --> 162.22]  We had the video too
[162.22 --> 163.08]  And he was bouncing around
[163.08 --> 163.38]  So
[163.38 --> 164.92]  I don't think anybody got to see that though
[164.92 --> 166.92]  Fun times with
[166.92 --> 167.74]  Chris Abound
[167.74 --> 168.44]  We talked about
[168.44 --> 169.94]  What it's like to work with Damien Katz
[169.94 --> 171.44]  On the Apache Project
[171.44 --> 172.54]  And also his buddy
[172.54 --> 173.06]  Jan Lennert
[173.06 --> 174.14]  Who if you don't know Jan
[174.14 --> 174.86]  Then you're missing out
[174.86 --> 175.84]  Yeah, absolutely
[175.84 --> 177.24]  Fun episode
[177.24 --> 177.90]  Should we get to it?
[178.04 --> 178.70]  Let's do it
[178.70 --> 188.66]  We're chatting today
[188.66 --> 189.50]  With Chris Anderson
[189.50 --> 190.44]  From Couchbase
[190.44 --> 190.90]  So Chris
[190.90 --> 192.24]  Why don't you introduce yourself
[192.24 --> 193.52]  And your role over at Couchbase
[193.52 --> 194.86]  Sure
[194.86 --> 195.28]  Yeah
[195.28 --> 196.58]  I've been a long time
[196.58 --> 197.42]  Committer to the
[197.42 --> 198.58]  Apache CouchDB project
[198.58 --> 199.92]  And founded
[199.92 --> 201.40]  CouchDB company
[201.40 --> 202.98]  With Damien Katz
[202.98 --> 203.66]  And Jan Lennert
[203.66 --> 204.92]  Back in 2009
[204.92 --> 206.34]  And we
[206.34 --> 207.32]  You know
[207.32 --> 208.96]  Were a merry band
[208.96 --> 209.90]  Of engineers
[209.90 --> 210.54]  You know
[210.54 --> 211.34]  Doing everything we could
[211.34 --> 213.00]  To make CouchDB awesome
[213.00 --> 214.74]  And then
[214.74 --> 215.24]  You know
[215.24 --> 215.90]  In the
[215.90 --> 217.62]  Last few months
[217.62 --> 218.18]  We were
[218.18 --> 218.86]  You know
[218.86 --> 219.98]  Kind of faced with
[219.98 --> 220.82]  The choice between
[220.82 --> 221.68]  Doing a
[221.68 --> 223.72]  Another round of VC
[223.72 --> 224.50]  Or
[224.50 --> 226.14]  Merging with these guys
[226.14 --> 227.02]  Over at Membase
[227.02 --> 228.08]  And as we started
[228.08 --> 228.72]  To look closer
[228.72 --> 229.52]  And closer at them
[229.52 --> 231.22]  It got to be
[231.22 --> 231.88]  You know
[231.88 --> 232.56]  Obvious
[232.56 --> 233.22]  That
[233.22 --> 234.90]  It was just the right choice
[234.90 --> 236.04]  So now we're Couchbase
[236.04 --> 236.90]  And we're bigger
[236.90 --> 237.44]  And stronger
[237.44 --> 238.50]  And
[238.50 --> 239.58]  You know
[239.58 --> 240.52]  Me and Damien and Jan
[240.52 --> 241.42]  Get to focus on our
[241.42 --> 243.22]  On the things we're good at
[243.22 --> 243.54]  So
[243.54 --> 244.14]  Yeah
[244.14 --> 245.66]  It's been a wild ride
[245.66 --> 246.58]  And I guess
[246.58 --> 247.38]  We're just getting started
[247.38 --> 247.66]  So
[247.66 --> 248.62]  Well we'll get into
[248.62 --> 249.94]  Couchbase in just a moment
[249.94 --> 250.28]  So
[250.28 --> 251.04]  For the
[251.04 --> 252.14]  Five or so people out there
[252.14 --> 253.16]  That aren't familiar
[253.16 --> 253.84]  With CouchDB
[253.84 --> 254.62]  Why don't you give an
[254.62 --> 255.34]  Overview of the
[255.34 --> 256.72]  Apache CouchDB project
[256.72 --> 257.52]  Sure
[257.52 --> 258.64]  So Apache CouchDB
[258.64 --> 260.10]  Is a database
[260.10 --> 261.52]  That's accessed
[261.52 --> 262.60]  Via web protocols
[262.60 --> 263.54]  So you just store
[263.54 --> 264.34]  JSON in it
[264.34 --> 264.80]  And
[264.80 --> 265.86]  You know
[265.86 --> 266.76]  Get JSON back
[266.76 --> 267.78]  Both in the form
[267.78 --> 268.42]  Of what you stored
[268.42 --> 269.56]  And you can also build
[269.56 --> 270.74]  Dynamic queries
[270.74 --> 271.54]  So
[271.54 --> 272.16]  You know
[272.16 --> 273.36]  I want all the blog posts
[273.36 --> 273.90]  In the last
[273.90 --> 274.74]  You know
[274.74 --> 275.18]  Two days
[275.18 --> 276.08]  That sort of thing
[276.08 --> 276.88]  Is easy to pull out
[276.88 --> 279.16]  It's got some
[279.16 --> 279.64]  Other
[279.64 --> 281.08]  Fun features
[281.08 --> 281.58]  The
[281.58 --> 282.62]  The killer one
[282.62 --> 283.16]  That really
[283.16 --> 284.32]  We're not seeing
[284.32 --> 284.74]  Anywhere else
[284.74 --> 285.28]  In the marketplace
[285.28 --> 286.48]  Is the ability
[286.48 --> 286.94]  To keep
[286.94 --> 287.70]  Two copies
[287.70 --> 288.50]  Two or more copies
[288.50 --> 288.88]  Of it all
[288.88 --> 289.54]  Synchronized
[289.54 --> 290.24]  So
[290.24 --> 290.86]  The idea
[290.86 --> 291.26]  You know
[291.26 --> 291.66]  Kind of like
[291.66 --> 292.32]  Dropbox
[292.32 --> 292.72]  But
[292.72 --> 293.68]  You know
[293.68 --> 294.52]  For your
[294.52 --> 295.30]  API
[295.30 --> 296.04]  Not for
[296.04 --> 296.88]  Your files
[296.88 --> 298.26]  So
[298.26 --> 298.86]  You know
[298.86 --> 299.60]  You've got two copies
[299.60 --> 299.98]  Of it
[299.98 --> 300.78]  And
[300.78 --> 301.62]  You know
[301.62 --> 302.18]  There's work going on
[302.18 --> 302.78]  On both ends
[302.78 --> 303.26]  And you can
[303.26 --> 304.08]  Synchronize them
[304.08 --> 305.20]  More or less
[305.20 --> 305.86]  Effortlessly
[305.86 --> 307.04]  So
[307.04 --> 307.48]  You know
[307.48 --> 307.90]  I can talk
[307.90 --> 308.72]  Technically more
[308.72 --> 309.34]  About the
[309.34 --> 311.44]  You know
[311.44 --> 312.48]  How that
[312.48 --> 313.62]  Synchronization works
[313.62 --> 314.34]  But
[314.34 --> 315.64]  For most developers
[315.64 --> 316.78]  It just works
[316.78 --> 318.12]  So in reference
[318.12 --> 318.70]  To Couch
[318.70 --> 319.52]  Base
[319.52 --> 320.02]  The new
[320.02 --> 320.94]  I guess
[320.94 --> 321.60]  Merger of
[321.60 --> 322.02]  Membase
[322.02 --> 322.82]  And CouchDB
[322.82 --> 323.68]  How did that
[323.68 --> 324.16]  Come about
[324.16 --> 325.04]  And what's
[325.04 --> 326.08]  I guess
[326.08 --> 326.72]  The offering
[326.72 --> 327.86]  From Couchbase
[327.86 --> 328.08]  Now
[328.08 --> 329.08]  Sure
[329.08 --> 329.82]  Yes
[329.82 --> 330.20]  I mentioned
[330.20 --> 330.60]  Earlier
[330.60 --> 331.04]  That
[331.04 --> 331.98]  You know
[331.98 --> 332.56]  As part of
[332.56 --> 333.80]  Our wild ride
[333.80 --> 334.74]  As founders
[334.74 --> 336.32]  So
[336.32 --> 337.34]  You know
[337.34 --> 338.46]  What happened
[338.46 --> 339.42]  Was Damien and I
[339.42 --> 340.18]  Had a chance
[340.18 --> 340.92]  Meeting with
[340.92 --> 341.36]  James
[341.36 --> 342.08]  Who is
[342.08 --> 342.98]  Our
[342.98 --> 343.90]  You know
[343.90 --> 344.48]  Lead product
[344.48 --> 345.22]  Architect guy
[345.22 --> 346.04]  Now
[346.04 --> 347.12]  And
[347.12 --> 348.18]  We just started
[348.18 --> 348.56]  Talking
[348.56 --> 349.38]  And what they'd
[349.38 --> 349.98]  Been doing
[349.98 --> 350.70]  For the last
[350.70 --> 351.08]  Year
[351.08 --> 351.70]  You know
[351.70 --> 352.30]  It was kind of
[352.30 --> 353.12]  At the other
[353.12 --> 353.96]  End of the spectrum
[353.96 --> 354.56]  From what we'd been
[354.56 --> 355.48]  Doing as far as
[355.48 --> 355.70]  You know
[355.70 --> 356.06]  Where they're
[356.06 --> 356.78]  Putting their focus
[356.78 --> 357.94]  And vice versa
[357.94 --> 358.58]  And then
[358.58 --> 359.20]  Comparing notes
[359.20 --> 359.74]  Even more
[359.74 --> 360.36]  Our plans
[360.36 --> 361.74]  For 2011
[361.74 --> 362.80]  Were to do
[362.80 --> 363.10]  What they'd
[363.10 --> 363.72]  Already done
[363.72 --> 365.10]  And vice versa
[365.10 --> 365.72]  They wanted to
[365.72 --> 366.62]  Build into
[366.62 --> 367.24]  Their product
[367.24 --> 367.66]  Membase
[367.66 --> 368.14]  A lot of the
[368.14 --> 368.68]  Features that
[368.68 --> 369.30]  CouchDB already
[369.30 --> 369.68]  Has
[369.68 --> 371.12]  So
[371.12 --> 371.64]  You know
[371.64 --> 371.84]  We started
[371.84 --> 372.30]  Talking more
[372.30 --> 372.62]  And more
[372.62 --> 373.36]  And we realized
[373.36 --> 373.72]  That
[373.72 --> 374.88]  At the end
[374.88 --> 375.34]  Of the day
[375.34 --> 376.62]  Doing this
[376.62 --> 377.02]  Merger
[377.02 --> 378.10]  Would accelerate
[378.10 --> 379.12]  Both companies
[379.12 --> 379.78]  Roadmaps
[379.78 --> 379.98]  And
[379.98 --> 381.06]  There's one
[381.06 --> 381.56]  Thing that you
[381.56 --> 382.08]  Can't buy
[382.08 --> 382.48]  And that's
[382.48 --> 382.78]  Time
[382.78 --> 383.08]  So
[383.08 --> 384.16]  I really feel
[384.16 --> 384.52]  Like
[384.52 --> 386.30]  If it continues
[386.30 --> 386.86]  To go well
[386.86 --> 387.32]  On the technical
[387.32 --> 387.64]  Front
[387.64 --> 388.48]  Integrating stuff
[388.48 --> 389.70]  That we have
[389.70 --> 390.56]  Jumped forward
[390.56 --> 391.00]  A year
[391.00 --> 391.44]  Or maybe
[391.44 --> 391.92]  Even two
[391.92 --> 392.48]  In terms of
[392.48 --> 392.92]  Our roadmap
[392.92 --> 393.70]  And capabilities
[393.70 --> 394.54]  And you know
[394.54 --> 395.34]  Viability as a
[395.34 --> 395.62]  Company
[395.62 --> 395.96]  So
[395.96 --> 397.38]  You know
[397.38 --> 398.10]  On top of that
[398.10 --> 398.76]  It's a huge relief
[398.76 --> 399.12]  For me
[399.12 --> 399.62]  Because I went
[399.62 --> 400.46]  From being
[400.46 --> 401.20]  The CFO
[401.20 --> 401.86]  To being
[401.86 --> 402.42]  The president
[402.42 --> 402.98]  And having
[402.98 --> 403.60]  To manage
[403.60 --> 403.86]  You know
[403.86 --> 404.14]  All these
[404.14 --> 404.72]  Teams and stuff
[404.72 --> 405.04]  Which is
[405.04 --> 406.00]  Great fun
[406.00 --> 406.90]  But I'd much
[406.90 --> 407.60]  Rather focus
[407.60 --> 408.80]  On you know
[408.80 --> 409.48]  Where the rubber
[409.48 --> 410.04]  Meets the road
[410.04 --> 410.54]  As far as
[410.54 --> 411.24]  What developers
[411.24 --> 411.78]  Are using
[411.78 --> 413.00]  So
[413.00 --> 413.94]  How many CFOs
[413.94 --> 414.42]  Do you know
[414.42 --> 415.00]  That actually
[415.00 --> 415.44]  Have a GitHub
[415.44 --> 415.80]  Account
[415.80 --> 418.16]  Well there's
[418.16 --> 418.72]  A few of them
[418.72 --> 419.26]  But you know
[419.26 --> 420.00]  That's what you
[420.00 --> 420.40]  Do when
[420.40 --> 420.64]  You're
[420.64 --> 421.22]  When there's
[421.22 --> 421.78]  Three of you
[421.78 --> 422.40]  You gotta
[422.40 --> 422.92]  Somebody's gotta
[422.92 --> 423.54]  Be the CFO
[423.54 --> 425.00]  And I drew
[425.00 --> 425.68]  The short straw
[425.68 --> 426.06]  I guess
[426.06 --> 426.30]  So
[426.30 --> 427.52]  You know
[427.52 --> 428.04]  The first link
[428.04 --> 428.48]  On the couch
[428.48 --> 429.62]  Base website
[429.62 --> 430.12]  Is why
[430.12 --> 430.64]  NoSQL
[430.64 --> 431.68]  So it's
[431.68 --> 432.82]  Now 2011
[432.82 --> 434.54]  Not only
[434.54 --> 434.76]  Were you
[434.76 --> 435.12]  Having to
[435.12 --> 435.60]  Answer this
[435.60 --> 435.92]  Question
[435.92 --> 437.00]  You're
[437.00 --> 438.32]  Featuring it
[438.32 --> 438.74]  Prominently
[438.74 --> 439.06]  On your
[439.06 --> 439.88]  Home page
[439.88 --> 440.22]  Are you
[440.22 --> 440.66]  Finding that
[440.66 --> 440.98]  You have to
[440.98 --> 441.58]  Sell NoSQL
[441.58 --> 442.14]  Just as much
[442.14 --> 442.38]  As you have
[442.38 --> 442.62]  To sell
[442.62 --> 443.08]  Your products
[443.08 --> 444.46]  Yeah
[444.46 --> 444.90]  So
[444.90 --> 446.44]  It really
[446.44 --> 446.90]  Depends on
[446.90 --> 447.34]  The audience
[447.34 --> 447.88]  That you're
[447.88 --> 448.42]  Talking to
[448.42 --> 448.78]  The core
[448.78 --> 449.42]  Audience of
[449.42 --> 449.90]  This show
[449.90 --> 450.32]  Probably
[450.32 --> 450.70]  Already
[450.70 --> 451.54]  Knows what
[451.54 --> 452.14]  NoSQL
[452.14 --> 452.70]  Is for
[452.70 --> 453.42]  And they're
[453.42 --> 453.60]  Probably
[453.60 --> 454.14]  Even over
[454.14 --> 454.64]  That hump
[454.64 --> 455.00]  Where
[455.00 --> 456.26]  It seems
[456.26 --> 456.84]  Like a threat
[456.84 --> 457.68]  To their
[457.68 --> 459.22]  Tried and
[459.22 --> 459.70]  True relational
[459.70 --> 460.30]  Databases
[460.30 --> 461.34]  I think
[461.34 --> 461.78]  Most of
[461.78 --> 462.08]  The cutting
[462.08 --> 462.26]  Edge
[462.26 --> 462.58]  Developer
[462.58 --> 463.08]  Community
[463.08 --> 464.00]  Sees
[464.00 --> 464.88]  That there's
[464.88 --> 465.40]  Problems
[465.40 --> 466.52]  That are
[466.52 --> 466.86]  Just a
[466.86 --> 467.34]  Better fit
[467.34 --> 468.00]  For schema
[468.00 --> 468.58]  Less storage
[468.58 --> 468.80]  Where you
[468.80 --> 469.08]  Don't have
[469.08 --> 469.40]  To deal
[469.40 --> 470.12]  With migration
[470.12 --> 471.12]  You know
[471.12 --> 471.60]  Migrating your
[471.60 --> 472.00]  Schema all
[472.00 --> 472.34]  The time
[472.34 --> 473.74]  And then
[473.74 --> 474.08]  Of course
[474.08 --> 474.68]  Once you
[474.68 --> 475.08]  Go over
[475.08 --> 475.54]  That hump
[475.54 --> 475.94]  Then there's
[475.94 --> 476.24]  All kinds
[476.24 --> 476.46]  Of other
[476.46 --> 476.88]  Benefits
[476.88 --> 477.42]  Like the
[477.42 --> 478.16]  Synchronization
[478.16 --> 478.44]  That we
[478.44 --> 478.84]  Offer
[478.84 --> 479.94]  Or the
[479.94 --> 480.40]  Ability to
[480.40 --> 481.28]  Do scale
[481.28 --> 481.50]  Out
[481.50 --> 482.26]  Because of
[482.26 --> 482.64]  Key value
[482.64 --> 482.86]  Based
[482.86 --> 483.44]  Architectures
[483.44 --> 483.94]  Instead of
[483.94 --> 485.00]  The relational
[485.00 --> 485.32]  Model
[485.32 --> 486.98]  So at the
[486.98 --> 487.20]  Cutting
[487.20 --> 487.48]  Edge
[487.48 --> 488.08]  I feel like
[488.08 --> 488.66]  That story
[488.66 --> 489.22]  Is told
[489.22 --> 489.60]  But
[489.60 --> 491.80]  The percentage
[491.80 --> 492.42]  Of developers
[492.42 --> 493.46]  Who even
[493.46 --> 494.44]  Know what
[494.44 --> 495.02]  GitHub is
[495.02 --> 495.76]  Is vanishingly
[495.76 --> 496.34]  Small compared
[496.34 --> 496.78]  To the
[496.78 --> 497.68]  Large mass
[497.68 --> 497.96]  Of people
[497.96 --> 498.82]  Out there
[498.82 --> 500.20]  And so
[500.20 --> 500.94]  Yeah
[500.94 --> 501.34]  To
[501.34 --> 503.02]  They're
[503.02 --> 503.16]  Going to
[503.16 --> 503.42]  Come to
[503.42 --> 503.54]  Us
[503.54 --> 504.00]  Not because
[504.00 --> 504.34]  They heard
[504.34 --> 504.80]  About couch
[504.80 --> 505.20]  But because
[505.20 --> 505.54]  They heard
[505.54 --> 505.98]  Oh there's
[505.98 --> 506.28]  Something
[506.28 --> 506.80]  Different
[506.80 --> 507.58]  And you
[507.58 --> 507.76]  Know
[507.76 --> 509.60]  That little
[509.60 --> 510.42]  Blurb may be
[510.42 --> 510.84]  The first
[510.84 --> 511.80]  Explanation they
[511.80 --> 512.18]  Get of no
[512.18 --> 512.80]  SQL at all
[512.80 --> 514.06]  So what
[514.06 --> 514.08]  So what
[514.08 --> 514.86]  Does the
[514.86 --> 515.30]  Product line
[515.30 --> 516.00]  Look like
[516.00 --> 516.58]  For couch
[516.58 --> 516.80]  Base
[516.80 --> 517.86]  So what
[517.86 --> 518.44]  Names
[518.44 --> 519.14]  Survivor
[519.14 --> 519.40]  Is it
[519.40 --> 519.84]  Just a
[519.84 --> 520.50]  New name
[520.50 --> 520.98]  Totally
[520.98 --> 521.50]  With couch
[521.50 --> 521.76]  Base
[521.76 --> 522.78]  Sure
[522.78 --> 523.54]  That's a
[523.54 --> 523.68]  Great
[523.68 --> 524.12]  Question
[524.12 --> 525.62]  The answer
[525.62 --> 526.20]  Is kind
[526.20 --> 526.74]  Of it's
[526.74 --> 527.28]  Easier to
[527.28 --> 527.76]  Talk about
[527.76 --> 528.58]  It from
[528.58 --> 528.94]  The technical
[528.94 --> 529.36]  Side
[529.36 --> 530.72]  Because what
[530.72 --> 531.30]  We're doing
[531.30 --> 532.00]  For integration
[532.00 --> 532.80]  Is fairly
[532.80 --> 533.44]  Obvious
[533.44 --> 533.74]  I mean
[533.74 --> 534.34]  That's a
[534.34 --> 534.70]  Big part
[534.70 --> 534.98]  Of why
[534.98 --> 535.40]  The merger
[535.40 --> 535.70]  Looked
[535.70 --> 536.12]  Viable
[536.12 --> 536.42]  After
[536.42 --> 536.98]  It looked
[536.98 --> 537.42]  Exciting
[537.42 --> 537.70]  Then of
[537.70 --> 537.94]  Course we
[537.94 --> 538.14]  Had to
[538.14 --> 538.34]  Go
[538.34 --> 539.94]  Look at
[539.94 --> 540.12]  It with
[540.12 --> 540.50]  A skeptical
[540.50 --> 540.84]  Eye
[540.84 --> 541.16]  And see
[541.16 --> 541.78]  Is it
[541.78 --> 541.88]  Going to
[541.88 --> 542.08]  Be too
[542.08 --> 542.22]  Hard
[542.22 --> 542.48]  To pull
[542.48 --> 542.78]  Off
[542.78 --> 544.18]  But it's
[544.18 --> 544.44]  Really
[544.44 --> 545.18]  Technically
[545.18 --> 545.84]  Kind of
[545.84 --> 546.14]  Obvious
[546.14 --> 546.48]  What we've
[546.48 --> 546.72]  Got to
[546.72 --> 546.92]  Do
[546.92 --> 548.64]  So before
[548.64 --> 549.16]  You understand
[549.16 --> 549.58]  What our
[549.58 --> 549.88]  Combined
[549.88 --> 550.34]  Product is
[550.34 --> 550.56]  Going to
[550.56 --> 550.84]  Look like
[550.84 --> 551.02]  You've
[551.02 --> 551.28]  Got to
[551.28 --> 551.80]  Understand
[551.80 --> 552.44]  Membase
[552.44 --> 553.40]  Which
[553.40 --> 554.86]  The elevator
[554.86 --> 555.24]  Pitch
[555.24 --> 555.60]  Is
[555.60 --> 555.80]  It's
[555.80 --> 556.14]  Basically
[556.14 --> 556.80]  A big
[556.80 --> 557.64]  Memcache
[557.64 --> 558.34]  D cluster
[558.34 --> 559.86]  That doesn't
[559.86 --> 560.80]  Forget everything
[560.80 --> 561.08]  When the
[561.08 --> 561.54]  Power goes
[561.54 --> 561.80]  Out
[561.80 --> 563.70]  So it
[563.70 --> 564.16]  Handles
[564.16 --> 564.52]  The
[564.52 --> 566.70]  Resizing
[566.70 --> 567.22]  The cluster
[567.22 --> 567.62]  And it
[567.62 --> 568.06]  Handles
[568.06 --> 568.40]  If you
[568.40 --> 568.72]  Want it
[568.72 --> 569.00]  To
[569.00 --> 570.28]  Proxying
[570.28 --> 571.12]  Each request
[571.12 --> 571.38]  To the
[571.38 --> 571.78]  Particular
[571.78 --> 572.14]  Cluster
[572.14 --> 572.40]  Member
[572.40 --> 572.78]  Or if
[572.78 --> 573.12]  You use
[573.12 --> 573.36]  Smart
[573.36 --> 573.74]  Clients
[573.74 --> 574.02]  Then you
[574.02 --> 574.20]  Can
[574.20 --> 575.04]  Have
[575.04 --> 575.62]  Slightly
[575.62 --> 575.92]  Better
[575.92 --> 576.72]  Efficiency
[576.72 --> 578.52]  But overall
[578.52 --> 579.04]  It'll do
[579.04 --> 579.26]  All the
[579.26 --> 579.78]  Rebalancing
[579.78 --> 580.42]  And make
[580.42 --> 580.74]  Sure
[580.74 --> 581.04]  That
[581.04 --> 582.16]  As your
[582.16 --> 582.66]  Data set
[582.66 --> 583.02]  Grows
[583.02 --> 583.36]  You can
[583.36 --> 583.82]  Maintain
[583.82 --> 584.12]  Sub
[584.12 --> 584.64]  Millisecond
[584.64 --> 584.90]  Query
[584.90 --> 585.40]  Latencies
[585.40 --> 586.76]  Via
[586.76 --> 587.44]  The
[587.44 --> 587.70]  Mem
[587.70 --> 588.14]  Capable
[588.14 --> 589.10]  API
[589.10 --> 589.92]  So
[589.92 --> 591.48]  That's
[591.48 --> 592.14]  Membase
[592.14 --> 592.80]  And
[592.80 --> 594.14]  Currently
[594.14 --> 594.82]  Today
[594.82 --> 595.48]  The
[595.48 --> 595.98]  Backend
[595.98 --> 596.44]  Storage
[596.44 --> 597.08]  Is
[597.08 --> 597.44]  Handled
[597.44 --> 597.90]  By
[597.90 --> 598.74]  Sqlite
[598.74 --> 599.90]  So
[599.90 --> 601.18]  But
[601.18 --> 601.34]  They're
[601.34 --> 601.50]  Not
[601.50 --> 601.86]  Using
[601.86 --> 602.24]  The
[602.24 --> 602.60]  Relational
[602.60 --> 602.92]  Features
[602.92 --> 603.04]  Of
[603.04 --> 603.46]  Sqlite
[603.46 --> 603.64]  They're
[603.64 --> 604.04]  Basically
[604.04 --> 604.40]  Using
[604.40 --> 604.60]  It
[604.60 --> 604.82]  Instead
[604.82 --> 604.96]  Of
[604.96 --> 605.14]  Raw
[605.14 --> 605.58]  Files
[605.58 --> 606.94]  So
[606.94 --> 607.06]  The
[607.06 --> 607.28]  First
[607.28 --> 607.60]  Step
[607.60 --> 608.02]  Pretty
[608.02 --> 608.48]  Obvious
[608.48 --> 608.80]  To
[608.80 --> 609.04]  Do
[609.04 --> 609.20]  Is
[609.20 --> 610.16]  Pull
[610.16 --> 610.56]  Out
[610.56 --> 611.46]  Sqlite
[611.46 --> 611.64]  And
[611.64 --> 612.02]  Replace
[612.02 --> 612.20]  It
[612.20 --> 612.42]  With
[612.42 --> 612.96]  CouchDB
[612.96 --> 613.46]  Storage
[613.46 --> 613.86]  Engine
[613.86 --> 615.30]  And
[615.30 --> 615.56]  So
[615.56 --> 616.16]  That's
[616.16 --> 616.64]  Easier
[616.64 --> 617.14]  And
[617.14 --> 618.20]  So
[618.20 --> 619.10]  That's
[619.10 --> 620.56]  Easier
[620.56 --> 621.10]  Everything
[621.10 --> 621.30]  But
[621.30 --> 621.40]  The
[621.40 --> 621.68]  Critical
[621.68 --> 621.94]  Write
[621.94 --> 622.30]  Path
[622.30 --> 622.96]  Is
[622.96 --> 623.16]  Written
[623.16 --> 623.30]  In
[623.30 --> 623.64]  Erlang
[623.64 --> 624.04]  Already
[624.04 --> 625.26]  And
[625.26 --> 625.46]  Then
[625.46 --> 625.74]  There's
[625.74 --> 625.88]  The
[625.88 --> 626.04]  C
[626.04 --> 626.44]  Based
[626.44 --> 627.38]  Memcache
[627.38 --> 627.64]  D
[627.64 --> 628.38]  And
[628.38 --> 628.90]  Sqlite
[628.90 --> 629.40]  Portions
[629.40 --> 629.72]  But
[629.72 --> 630.58]  This
[630.58 --> 630.72]  Is
[630.72 --> 630.86]  Just
[630.86 --> 631.02]  Going
[631.02 --> 631.10]  To
[631.10 --> 631.38]  Be
[631.38 --> 632.16]  Placing
[632.16 --> 632.30]  A
[632.30 --> 632.54]  Bigger
[632.54 --> 632.78]  Bet
[632.78 --> 633.06]  On
[633.06 --> 633.48]  Erlang
[633.48 --> 634.18]  And
[634.18 --> 634.30]  It
[634.30 --> 634.52]  Also
[634.52 --> 634.82]  Makes
[634.82 --> 634.98]  It
[634.98 --> 635.32]  Really
[635.32 --> 636.02]  Smooth
[636.02 --> 636.26]  To
[636.26 --> 636.62]  Integrate
[636.62 --> 637.00]  Couch
[637.00 --> 638.48]  So
[638.48 --> 638.76]  First
[638.76 --> 638.98]  Step
[638.98 --> 639.10]  Is
[639.10 --> 639.36]  Just
[639.36 --> 639.92]  Getting
[639.92 --> 640.16]  Couch
[640.16 --> 640.28]  In
[640.28 --> 640.36]  There
[640.36 --> 640.48]  As
[640.48 --> 640.56]  A
[640.56 --> 640.84]  Storage
[640.84 --> 641.18]  Engine
[641.18 --> 641.84]  And
[641.84 --> 642.02]  We're
[642.02 --> 642.12]  Going
[642.12 --> 642.22]  To
[642.22 --> 642.58]  Release
[642.58 --> 642.96]  That
[642.96 --> 643.60]  Product
[643.60 --> 644.94]  As
[644.94 --> 645.40]  Essentially
[645.40 --> 645.78]  Something
[645.78 --> 646.12]  That
[646.12 --> 646.82]  Provides
[646.82 --> 647.10]  A lot
[647.10 --> 647.20]  Of
[647.20 --> 647.44]  Value
[647.44 --> 647.62]  To
[647.62 --> 648.04]  Existing
[648.04 --> 648.42]  Membase
[648.42 --> 648.72]  Users
[648.72 --> 649.04]  Because
[649.04 --> 649.18]  You
[649.18 --> 649.36]  Get
[649.36 --> 650.28]  For
[650.28 --> 650.36]  The
[650.36 --> 650.50]  One
[650.50 --> 650.76]  Thing
[650.76 --> 651.16]  Slightly
[651.16 --> 651.58]  Better
[651.58 --> 652.28]  IO
[652.28 --> 652.56]  Through
[652.56 --> 652.88]  To
[652.88 --> 653.26]  Disk
[653.26 --> 653.90]  Couch
[653.90 --> 654.04]  Is
[654.04 --> 654.16]  Just
[654.16 --> 654.32]  More
[654.32 --> 654.84]  Optimized
[654.84 --> 655.02]  For
[655.02 --> 655.16]  The
[655.16 --> 655.38]  Kinds
[655.38 --> 655.46]  Of
[655.46 --> 655.76]  Access
[655.76 --> 656.18]  Patterns
[656.18 --> 656.44]  That
[656.44 --> 657.02]  Membase
[657.02 --> 657.16]  Was
[657.16 --> 657.38]  Already
[657.38 --> 657.66]  Doing
[657.66 --> 659.14]  And
[659.14 --> 659.32]  So
[659.32 --> 659.68]  That's
[659.68 --> 660.02]  Just
[660.02 --> 660.20]  Kind
[660.20 --> 660.30]  Of
[660.30 --> 660.48]  Like
[660.48 --> 660.70]  A
[660.70 --> 661.28]  Really
[661.28 --> 661.68]  Basic
[661.68 --> 661.98]  Win
[661.98 --> 662.22]  But
[662.22 --> 662.40]  Maybe
[662.40 --> 662.58]  Not
[662.58 --> 662.78]  Worth
[662.78 --> 662.90]  All
[662.90 --> 663.00]  The
[663.00 --> 663.28]  Technical
[663.28 --> 663.66]  Risk
[663.66 --> 664.08]  Of
[664.08 --> 664.26]  Trying
[664.26 --> 664.36]  To
[664.36 --> 664.44]  Do
[664.44 --> 664.58]  This
[664.58 --> 664.92]  Integration
[664.92 --> 665.12]  On
[665.12 --> 665.26]  Its
[665.26 --> 665.48]  Own
[665.48 --> 666.22]  The
[666.22 --> 666.36]  Other
[666.36 --> 666.58]  Thing
[666.58 --> 666.70]  You
[666.70 --> 666.96]  Get
[666.96 --> 667.48]  More
[667.48 --> 667.58]  Or
[667.58 --> 667.74]  Less
[667.74 --> 667.90]  For
[667.90 --> 668.18]  Free
[668.18 --> 669.14]  Is
[669.14 --> 669.34]  The
[669.34 --> 669.74]  Ability
[669.74 --> 669.94]  To
[669.94 --> 670.32]  Query
[670.32 --> 670.68]  Now
[670.68 --> 671.90]  Your
[671.90 --> 672.74]  Membase
[672.74 --> 674.22]  Cluster
[674.22 --> 675.48]  With
[675.48 --> 676.32]  Couch
[676.32 --> 676.48]  DB
[676.48 --> 676.78]  Style
[676.78 --> 677.00]  Map
[677.00 --> 677.36]  Reduce
[677.36 --> 678.56]  So
[678.56 --> 678.90]  That's
[683.90 --> 684.02]  You
[684.02 --> 684.14]  Can
[684.14 --> 684.26]  Get
[684.26 --> 684.36]  It
[684.36 --> 684.52]  Out
[684.52 --> 684.68]  By
[684.68 --> 684.80]  The
[684.80 --> 684.96]  Same
[684.96 --> 685.12]  Key
[685.12 --> 685.22]  You
[685.22 --> 685.38]  Put
[685.38 --> 685.48]  It
[685.48 --> 685.62]  In
[685.62 --> 685.78]  But
[685.78 --> 685.92]  As
[685.92 --> 686.04]  Soon
[686.04 --> 686.18]  As
[686.18 --> 686.26]  You
[686.26 --> 686.42]  Want
[686.42 --> 686.52]  To
[686.52 --> 686.66]  Get
[686.66 --> 686.84]  More
[686.84 --> 687.26]  Complex
[687.26 --> 687.48]  Than
[687.48 --> 687.72]  That
[687.72 --> 688.28]  Then
[688.28 --> 688.60]  You're
[688.60 --> 689.96]  You're
[689.96 --> 690.10]  Either
[690.10 --> 690.34]  Having
[690.34 --> 690.48]  To
[690.48 --> 690.62]  Do
[690.62 --> 690.74]  A
[690.74 --> 690.92]  Bunch
[690.92 --> 691.12]  Of
[691.12 --> 692.14]  Pointer
[692.14 --> 692.64]  Following
[692.64 --> 692.92]  In
[692.92 --> 693.04]  Your
[693.04 --> 693.56]  Application
[693.56 --> 693.90]  Or
[693.90 --> 694.04]  You're
[694.04 --> 694.24]  Having
[694.24 --> 694.38]  To
[694.38 --> 694.64]  Write
[694.64 --> 694.80]  Some
[694.80 --> 695.12]  Custom
[695.12 --> 695.42]  Layer
[695.42 --> 696.16]  That
[696.16 --> 696.54]  Interacts
[696.54 --> 696.68]  With
[696.68 --> 697.02]  Memcached
[697.02 --> 697.46]  So
[697.46 --> 697.96]  This
[697.96 --> 698.06]  Will
[698.06 --> 698.18]  Give
[698.18 --> 698.58]  People
[698.58 --> 699.14]  A
[699.14 --> 700.20]  Straightforward
[700.20 --> 700.64]  Ability
[700.64 --> 700.88]  To
[700.88 --> 701.10]  Get
[701.10 --> 701.28]  Real
[701.28 --> 701.64]  Time
[701.64 --> 704.00]  Queries
[704.00 --> 704.32]  On
[704.32 --> 704.60]  Top
[704.60 --> 705.00]  Of
[705.00 --> 705.36]  Their
[705.36 --> 705.84]  Memcached
[705.84 --> 706.38]  Clusters
[706.38 --> 706.86]  Or
[706.86 --> 707.44]  Membase
[707.44 --> 707.88]  Clusters
[707.88 --> 708.82]  And
[708.82 --> 709.64]  That
[709.64 --> 710.06]  Alone
[710.06 --> 710.32]  Is
[710.32 --> 710.54]  Enough
[710.54 --> 710.70]  To
[710.70 --> 710.90]  Be
[710.90 --> 711.38]  Pretty
[711.38 --> 711.88]  Exciting
[711.88 --> 712.04]  But
[712.04 --> 712.36]  That's
[712.36 --> 712.78]  Really
[712.78 --> 712.98]  Just
[712.98 --> 713.12]  The
[713.12 --> 713.34]  First
[713.34 --> 713.62]  Step
[713.62 --> 714.68]  You
[714.68 --> 714.78]  Know
[714.78 --> 714.90]  Once
[714.90 --> 714.98]  You
[714.98 --> 715.06]  Go
[715.06 --> 715.20]  Down
[715.20 --> 715.30]  The
[715.30 --> 715.58]  Path
[715.58 --> 715.72]  Of
[715.72 --> 715.98]  Choosing
[715.98 --> 716.10]  A
[716.10 --> 716.20]  No
[716.20 --> 716.42]  Sequel
[716.42 --> 716.86]  Option
[716.86 --> 717.32]  And
[717.32 --> 717.48]  There's
[717.48 --> 717.68]  A
[717.68 --> 717.92]  Whole
[717.92 --> 718.14]  Lot
[718.14 --> 718.26]  Of
[718.26 --> 718.56]  Options
[718.56 --> 718.76]  Out
[718.76 --> 718.86]  There
[718.86 --> 719.04]  We've
[719.04 --> 719.22]  Covered
[719.22 --> 719.36]  A
[719.36 --> 719.52]  Lot
[719.52 --> 719.60]  Of
[719.60 --> 719.72]  Them
[719.72 --> 720.40]  On
[720.40 --> 720.54]  The
[720.54 --> 720.78]  Show
[720.78 --> 720.90]  I
[720.90 --> 721.04]  Think
[721.04 --> 721.18]  We're
[721.18 --> 721.48]  Couch
[721.48 --> 721.60]  In
[721.60 --> 721.68]  The
[721.68 --> 721.98]  Past
[721.98 --> 722.18]  Has
[722.18 --> 722.56]  Shined
[722.56 --> 723.40]  Been
[723.40 --> 723.58]  In
[723.58 --> 723.80]  The
[723.80 --> 724.74]  Replication
[724.74 --> 725.02]  Area
[725.02 --> 725.18]  But
[725.18 --> 725.28]  You
[725.28 --> 725.40]  Got
[725.40 --> 725.72]  Another
[725.72 --> 727.62]  Ace
[727.62 --> 727.74]  In
[727.74 --> 727.86]  The
[727.86 --> 728.08]  Hole
[728.08 --> 728.28]  As
[728.28 --> 728.36]  It
[728.36 --> 728.56]  Were
[728.56 --> 729.14]  Coming
[729.14 --> 729.46]  Up
[729.46 --> 729.76]  Talk
[729.76 --> 729.92]  About
[729.92 --> 730.06]  Your
[730.06 --> 730.38]  Mobile
[730.38 --> 731.52]  Yeah
[731.52 --> 732.22]  Mobile
[732.22 --> 735.14]  Is
[735.14 --> 736.48]  Been
[736.48 --> 736.62]  A
[736.62 --> 737.06]  Focus
[737.06 --> 737.68]  Of
[737.68 --> 738.16]  Couch
[738.16 --> 738.32]  One
[738.32 --> 738.52]  Before
[738.52 --> 738.68]  The
[738.68 --> 739.04]  Merger
[739.04 --> 739.54]  And
[739.54 --> 741.28]  Even
[741.28 --> 741.40]  Though
[741.40 --> 741.56]  We've
[741.56 --> 741.68]  Got
[741.68 --> 741.90]  More
[741.90 --> 742.16]  Going
[742.16 --> 742.34]  On
[742.34 --> 742.60]  After
[742.60 --> 742.78]  The
[742.78 --> 743.08]  Merger
[743.08 --> 743.24]  I
[743.24 --> 743.40]  Think
[743.40 --> 743.58]  That
[743.58 --> 743.74]  We're
[743.74 --> 743.92]  Getting
[743.92 --> 744.18]  More
[744.18 --> 744.70]  Momentum
[744.70 --> 744.84]  On
[744.84 --> 745.14]  Mobile
[745.14 --> 745.74]  If
[745.74 --> 745.98]  Only
[745.98 --> 746.50]  Because
[746.50 --> 746.82]  I'm
[746.82 --> 747.04]  Not
[747.04 --> 747.44]  Dealing
[747.44 --> 747.76]  With
[747.76 --> 748.64]  HR
[748.64 --> 748.80]  And
[748.80 --> 749.26]  Fundraising
[749.26 --> 749.70]  I'm
[749.70 --> 749.90]  Working
[749.90 --> 750.08]  On
[750.08 --> 750.30]  Mobile
[750.30 --> 752.36]  And
[752.36 --> 753.04]  For
[753.04 --> 753.14]  The
[753.14 --> 753.30]  Most
[753.30 --> 753.48]  Part
[753.48 --> 753.74]  That's
[753.74 --> 754.00]  Been
[754.00 --> 754.66]  Coordinating
[754.66 --> 754.96]  A Lot
[754.96 --> 755.02]  Of
[755.02 --> 755.14]  The
[755.14 --> 755.34]  Code
[755.34 --> 755.50]  That
[755.50 --> 755.58]  We
[755.58 --> 755.88]  Had
[755.88 --> 757.42]  Around
[757.42 --> 758.16]  And
[758.16 --> 758.86]  Starting
[758.86 --> 759.18]  Some
[759.18 --> 759.54]  QA
[759.54 --> 759.66]  And
[759.66 --> 759.78]  Some
[759.78 --> 760.06]  Release
[760.06 --> 760.40]  Process
[760.40 --> 760.70]  On
[760.70 --> 760.80]  It
[760.80 --> 760.90]  And
[760.90 --> 761.38]  Documenting
[761.38 --> 761.52]  It
[761.52 --> 761.66]  And
[761.66 --> 761.86]  Getting
[761.86 --> 761.98]  It
[761.98 --> 762.08]  Out
[762.08 --> 762.16]  To
[762.16 --> 762.26]  The
[762.26 --> 762.62]  Community
[762.62 --> 763.84]  So
[763.84 --> 764.22]  I'm
[764.22 --> 764.36]  Really
[764.36 --> 764.62]  Lucky
[764.62 --> 764.82]  To
[764.82 --> 765.02]  Our
[765.02 --> 765.52]  Engineers
[765.52 --> 765.90]  For
[765.90 --> 766.40]  Having
[766.40 --> 766.72]  Already
[766.72 --> 767.46]  Kicked
[767.46 --> 767.56]  A
[767.56 --> 767.70]  Bunch
[767.70 --> 767.78]  Of
[767.78 --> 768.00]  Ass
[768.00 --> 768.26]  On
[768.26 --> 769.34]  Getting
[769.34 --> 769.56]  Stuff
[769.56 --> 769.72]  To
[769.72 --> 769.98]  Run
[769.98 --> 770.22]  On
[770.22 --> 770.56]  iOS
[770.56 --> 771.70]  It's
[771.70 --> 772.12]  Not
[772.12 --> 773.66]  It's
[773.66 --> 774.26]  Not
[774.26 --> 774.76]  Real
[774.76 --> 775.16]  Simple
[775.16 --> 775.34]  We
[775.34 --> 775.48]  Had
[775.48 --> 775.60]  To
[775.60 --> 775.76]  Do
[775.76 --> 775.98]  A
[775.98 --> 776.22]  Lot
[776.22 --> 776.42]  Of
[776.42 --> 777.40]  Low
[777.40 --> 777.62]  Level
[777.62 --> 777.96]  Stuff
[777.96 --> 778.14]  To
[778.14 --> 778.36]  The
[778.36 --> 778.84]  Erlang
[778.84 --> 779.34]  VM
[779.34 --> 780.46]  To
[780.46 --> 781.00]  CouchDB
[781.00 --> 781.68]  Itself
[781.68 --> 782.34]  And
[782.34 --> 783.38]  You know
[783.38 --> 783.50]  But
[783.50 --> 783.60]  The
[783.60 --> 783.92]  Upshot
[783.92 --> 784.22]  Is
[784.22 --> 784.50]  Now
[784.50 --> 784.70]  We've
[784.70 --> 784.98]  Got
[784.98 --> 785.36]  A
[785.36 --> 785.90]  CouchDB
[785.90 --> 786.50]  Instance
[786.50 --> 786.68]  That
[786.68 --> 787.10]  Runs
[787.10 --> 787.34]  On
[787.34 --> 787.44]  Your
[787.44 --> 787.92]  Device
[787.92 --> 789.46]  We
[789.46 --> 789.58]  Were
[789.58 --> 789.98]  Surprised
[789.98 --> 790.16]  To
[790.16 --> 790.42]  Find
[790.42 --> 790.74]  That
[790.74 --> 790.98]  It
[790.98 --> 791.98]  Has
[791.98 --> 792.20]  Almost
[792.20 --> 792.40]  No
[792.40 --> 792.72]  Impact
[792.72 --> 792.88]  On
[792.88 --> 793.14]  Battery
[793.14 --> 793.46]  Life
[793.46 --> 793.66]  So
[793.66 --> 793.86]  That
[793.86 --> 794.02]  Was
[794.02 --> 794.54]  Real
[794.54 --> 794.88]  Lucky
[794.88 --> 796.32]  It's
[796.32 --> 796.62]  Not
[796.62 --> 796.96]  Surprising
[796.96 --> 797.16]  When
[797.16 --> 797.24]  You
[797.24 --> 797.58]  Understand
[797.58 --> 798.02]  Erlang
[798.02 --> 798.32]  And
[798.32 --> 798.90]  You
[798.90 --> 799.00]  Know
[799.00 --> 799.24]  How
[799.24 --> 799.80]  Erlang
[799.80 --> 799.96]  Is
[799.96 --> 800.16]  Good
[800.16 --> 800.32]  At
[800.32 --> 800.56]  Being
[800.56 --> 800.88]  Idle
[800.88 --> 802.14]  But
[802.14 --> 802.48]  Still
[802.48 --> 802.88]  We
[802.88 --> 803.04]  Were
[803.04 --> 803.54]  Expecting
[803.54 --> 803.62]  To
[803.62 --> 803.72]  Have
[803.72 --> 803.82]  To
[803.82 --> 804.10]  Invest
[804.10 --> 804.22]  A
[804.22 --> 804.30]  Lot
[804.30 --> 804.54]  There
[804.54 --> 805.22]  Instead
[805.22 --> 805.74]  We've
[805.74 --> 805.88]  Still
[805.88 --> 806.06]  Got
[806.06 --> 806.18]  To
[806.18 --> 806.70]  Tackle
[806.70 --> 806.96]  The
[806.96 --> 807.42]  Overall
[807.42 --> 807.82]  Download
[807.82 --> 808.22]  Size
[808.22 --> 808.48]  So
[808.48 --> 808.62]  Right
[808.62 --> 808.76]  Now
[808.76 --> 808.88]  It
[808.88 --> 809.06]  Adds
[809.06 --> 809.22]  About
[809.22 --> 809.62]  15
[809.62 --> 810.08]  Megabytes
[810.08 --> 810.32]  To
[810.32 --> 810.52]  Your
[810.52 --> 811.06]  Application
[811.06 --> 812.06]  Which
[812.06 --> 812.18]  We
[812.18 --> 812.36]  See
[812.36 --> 812.58]  Being
[812.58 --> 813.00]  Fine
[813.00 --> 813.32]  For
[813.32 --> 813.90]  Enterprise
[813.90 --> 814.58]  Applications
[814.58 --> 814.78]  And
[814.78 --> 815.08]  More
[815.08 --> 815.54]  Serious
[815.54 --> 815.86]  Stuff
[815.86 --> 816.12]  But
[816.12 --> 816.60]  If
[816.60 --> 816.82]  Somebody
[816.82 --> 817.06]  Just
[817.06 --> 817.26]  Wants
[817.26 --> 817.36]  A
[817.36 --> 817.48]  Little
[817.48 --> 817.60]  Bit
[817.60 --> 817.66]  Of
[817.66 --> 818.28]  Synchronization
[818.28 --> 818.70]  That
[818.70 --> 818.98]  Is
[818.98 --> 819.28]  Big
[819.28 --> 819.42]  Enough
[819.42 --> 819.54]  To
[819.54 --> 819.66]  Make
[819.66 --> 819.76]  Them
[819.76 --> 819.94]  Think
[819.94 --> 820.24]  Twice
[820.24 --> 820.56]  So
[820.56 --> 821.16]  Our
[821.16 --> 821.48]  First
[821.48 --> 821.86]  Goal
[821.86 --> 822.12]  Is
[822.12 --> 822.24]  To
[822.24 --> 822.54]  Shrink
[822.54 --> 822.86]  That
[822.86 --> 823.54]  So
[823.54 --> 823.62]  I
[823.62 --> 823.74]  Guess
[823.74 --> 823.88]  On
[823.88 --> 824.32]  iOS
[824.32 --> 824.70]  Which
[824.70 --> 825.30]  Every
[825.30 --> 825.56]  App
[825.56 --> 825.68]  Is
[825.68 --> 825.72]  It
[825.72 --> 825.86]  It's
[825.86 --> 825.88]  It's
[825.88 --> 825.90]  It's
[825.90 --> 826.98]  It's
[826.98 --> 827.30]  Pretty
[827.30 --> 827.48]  Much
[827.48 --> 827.88]  Additive
[827.88 --> 828.12]  To
[828.12 --> 828.38]  Every
[828.38 --> 828.60]  App
[828.60 --> 828.80]  You
[828.80 --> 829.46]  Can't
[829.46 --> 830.16]  Install
[830.16 --> 830.40]  The
[830.40 --> 830.74]  Couch
[830.74 --> 830.92]  Base
[830.92 --> 831.34]  Framework
[831.34 --> 831.74]  Once
[831.74 --> 831.90]  And
[831.90 --> 832.64]  Share
[832.64 --> 832.84]  That
[832.84 --> 833.06]  Right
[833.06 --> 833.90]  Right
[833.90 --> 834.16]  Yeah
[834.16 --> 834.56]  That's
[834.56 --> 835.22]  Down
[835.22 --> 835.40]  To
[835.40 --> 835.64]  The
[835.64 --> 835.88]  Apple
[835.88 --> 836.46]  Restrictions
[836.46 --> 836.78]  Which
[836.78 --> 836.98]  I
[836.98 --> 837.18]  Think
[837.18 --> 837.42]  Make
[837.42 --> 837.70]  Perfect
[837.70 --> 838.04]  Sense
[838.04 --> 838.18]  I
[838.18 --> 838.42]  They
[838.42 --> 838.76]  They're
[838.76 --> 839.22]  Sandboxing
[839.22 --> 839.48]  These
[839.48 --> 839.74]  Apps
[839.74 --> 839.90]  They
[839.90 --> 840.06]  Don't
[840.06 --> 840.32]  Want
[840.32 --> 840.90]  Some
[840.90 --> 841.46]  They
[841.46 --> 841.58]  Don't
[841.58 --> 841.70]  Want
[841.70 --> 842.04]  DLL
[842.04 --> 842.30]  Hell
[842.30 --> 842.46]  They
[842.46 --> 842.58]  Don't
[842.58 --> 842.72]  Want
[842.72 --> 842.90]  Your
[842.90 --> 843.90]  Underlying
[843.90 --> 844.38]  Libraries
[844.38 --> 844.86]  Swapping
[844.86 --> 845.24]  Versions
[845.24 --> 845.42]  Out
[845.42 --> 845.56]  From
[845.56 --> 845.90]  Underneath
[845.90 --> 846.12]  Your
[846.12 --> 846.60]  Application
[846.60 --> 846.96]  So
[846.96 --> 848.32]  Yeah
[848.32 --> 848.62]  We
[848.62 --> 848.82]  Just
[848.82 --> 849.04]  You
[849.04 --> 849.44]  It's
[849.44 --> 849.56]  Our
[849.56 --> 849.74]  Job
[849.74 --> 849.86]  To
[849.86 --> 849.98]  Get
[849.98 --> 850.12]  That
[850.12 --> 850.30]  Thing
[850.30 --> 850.56]  Small
[850.56 --> 850.80]  Enough
[850.80 --> 851.24]  To
[851.24 --> 851.82]  Not
[851.82 --> 852.10]  Have
[852.10 --> 852.34]  That
[852.34 --> 852.56]  Negative
[852.56 --> 852.92]  Impact
[852.92 --> 853.06]  And
[853.06 --> 853.16]  I
[853.16 --> 853.32]  Think
[853.32 --> 853.66]  Five
[853.66 --> 854.08]  Megabytes
[854.08 --> 854.36]  Is
[854.36 --> 855.00]  The
[855.00 --> 855.30]  Threshold
[855.30 --> 855.50]  Where
[855.50 --> 855.62]  We
[855.62 --> 855.74]  Can
[855.74 --> 855.94]  Start
[855.94 --> 856.06]  To
[856.06 --> 856.26]  Feel
[856.26 --> 856.78]  So
[856.78 --> 857.00]  Why
[857.00 --> 858.04]  Why
[858.04 --> 858.56]  iOS
[858.56 --> 859.00]  First
[859.00 --> 859.22]  Was
[859.22 --> 859.34]  It
[859.34 --> 859.86]  An
[859.86 --> 860.12]  Install
[860.12 --> 860.46]  Based
[860.46 --> 861.24]  Decision
[861.24 --> 861.46]  Or
[861.46 --> 861.98]  Lower
[861.98 --> 862.46]  Buried
[862.46 --> 862.56]  Of
[862.56 --> 862.82]  Entry
[862.82 --> 863.00]  As
[863.00 --> 863.14]  Far
[863.14 --> 863.24]  As
[863.24 --> 863.56]  A
[863.56 --> 863.80]  Technical
[863.80 --> 864.14]  Problem
[864.14 --> 864.96]  Well
[864.96 --> 865.70]  We've
[865.70 --> 865.92]  Been
[865.92 --> 866.18]  Running
[866.18 --> 866.40]  On
[866.40 --> 866.94]  Android
[866.94 --> 867.46]  For
[867.46 --> 867.80]  I
[867.80 --> 867.88]  Don't
[867.88 --> 868.00]  Know
[868.00 --> 868.22]  About
[868.22 --> 868.46]  Nine
[868.46 --> 868.78]  Months
[868.78 --> 869.04]  Now
[869.04 --> 870.56]  And
[870.56 --> 871.04]  The
[871.04 --> 871.50]  You
[871.50 --> 871.56]  Know
[871.56 --> 871.66]  The
[871.66 --> 871.96]  Response
[871.96 --> 872.08]  Has
[872.08 --> 872.18]  Been
[872.18 --> 872.36]  Really
[872.36 --> 872.68]  Strong
[872.68 --> 872.86]  We've
[872.86 --> 872.98]  Got
[872.98 --> 873.08]  A
[873.08 --> 873.26]  Couple
[873.26 --> 873.40]  Of
[873.40 --> 873.64]  Case
[873.64 --> 873.90]  Studies
[873.90 --> 874.20]  In
[874.20 --> 874.28]  The
[874.28 --> 874.64]  Pipeline
[874.64 --> 874.76]  Of
[874.76 --> 874.96]  People
[874.96 --> 875.26]  Who
[875.26 --> 875.74]  Are
[875.74 --> 875.94]  Using
[875.94 --> 876.28]  Android
[876.28 --> 876.46]  On
[876.46 --> 876.56]  The
[876.56 --> 876.98]  Device
[876.98 --> 877.54]  And
[877.54 --> 881.00]  It's
[881.00 --> 882.66]  But
[882.66 --> 882.76]  It
[882.76 --> 882.90]  Was
[882.90 --> 883.22]  Actually
[883.22 --> 883.44]  Kind
[883.44 --> 883.52]  Of
[883.52 --> 883.86]  Scary
[883.86 --> 884.18]  Because
[884.18 --> 884.48]  Android
[884.48 --> 884.96]  Affords
[884.96 --> 885.06]  You
[885.06 --> 885.20]  So
[885.20 --> 885.34]  Much
[885.34 --> 885.64]  Freedom
[885.64 --> 886.72]  That
[886.72 --> 887.18]  Question
[887.18 --> 887.32]  You
[887.32 --> 887.40]  Were
[887.40 --> 887.68]  Asking
[887.68 --> 887.98]  About
[887.98 --> 888.28]  Is
[888.28 --> 888.40]  It
[888.40 --> 888.66]  In
[888.66 --> 889.00]  Each
[889.00 --> 889.32]  App
[889.32 --> 889.48]  Or
[889.48 --> 889.66]  Is
[889.66 --> 889.78]  It
[889.78 --> 890.06]  Once
[890.06 --> 890.30]  On
[890.30 --> 890.40]  The
[890.40 --> 890.78]  Device
[890.78 --> 891.24]  On
[891.24 --> 891.56]  Android
[891.56 --> 891.76]  You
[891.76 --> 891.90]  Can
[891.90 --> 892.10]  Have
[892.10 --> 892.36]  Couch
[892.36 --> 892.52]  DB
[892.52 --> 892.68]  Be
[892.68 --> 892.78]  A
[892.78 --> 893.18]  Library
[893.18 --> 893.94]  And
[893.94 --> 894.18]  So
[894.18 --> 894.64]  There's
[894.64 --> 894.72]  This
[894.72 --> 894.84]  Whole
[894.84 --> 895.02]  Line
[895.02 --> 895.12]  Of
[895.12 --> 895.42]  Development
[895.42 --> 895.70]  Going
[895.70 --> 896.18]  Down
[896.18 --> 896.40]  About
[896.40 --> 896.62]  How
[896.62 --> 896.84]  To
[896.84 --> 897.38]  Manage
[897.38 --> 897.74]  A
[897.74 --> 898.34]  Centralized
[898.34 --> 898.88]  Database
[898.88 --> 899.12]  That
[899.12 --> 899.58]  Multiple
[899.58 --> 900.06]  Applications
[900.06 --> 900.20]  Are
[900.20 --> 900.44]  Talking
[900.44 --> 900.64]  To
[900.64 --> 901.26]  It's
[901.26 --> 901.44]  Really
[901.44 --> 901.94]  Powerful
[901.94 --> 902.12]  And
[902.12 --> 902.44]  Interesting
[902.44 --> 902.82]  And
[902.82 --> 903.22]  Like
[903.22 --> 903.60]  Threatened
[903.60 --> 903.92]  To
[903.92 --> 905.22]  Pull
[905.22 --> 905.34]  Us
[915.20 --> 915.40]  When
[915.40 --> 915.50]  You're
[915.50 --> 915.60]  A
[915.60 --> 915.94]  Startup
[915.94 --> 916.46]  Find
[916.46 --> 916.78]  The
[916.78 --> 918.06]  Run
[918.06 --> 918.22]  Up
[918.22 --> 918.38]  The
[918.38 --> 918.70]  Steepest
[918.70 --> 918.86]  Hill
[918.86 --> 919.00]  You
[919.00 --> 919.14]  Can
[919.14 --> 919.50]  Find
[919.50 --> 919.84]  Just
[919.84 --> 920.08]  Do
[920.08 --> 920.92]  The
[920.92 --> 921.30]  Hardest
[921.30 --> 921.54]  Thing
[921.54 --> 921.70]  That
[921.70 --> 921.80]  You
[921.80 --> 921.94]  Can
[921.94 --> 922.14]  See
[922.14 --> 922.44]  Because
[922.44 --> 922.74]  Probably
[922.74 --> 922.96]  Most
[922.96 --> 923.16]  People
[923.16 --> 923.36]  Aren't
[923.36 --> 923.64]  Looking
[923.64 --> 924.24]  With
[924.24 --> 924.36]  The
[924.36 --> 924.54]  Same
[924.54 --> 924.76]  Amount
[924.76 --> 924.84]  Of
[924.84 --> 925.14]  Detail
[925.14 --> 925.38]  As
[925.38 --> 925.78]  What
[925.78 --> 925.92]  You're
[925.92 --> 926.18]  Looking
[926.18 --> 926.34]  At
[926.34 --> 926.46]  So
[926.46 --> 926.56]  If
[926.56 --> 926.64]  You
[926.64 --> 926.74]  See
[926.74 --> 926.92]  Something
[926.92 --> 927.22]  Really
[927.22 --> 927.78]  Challenging
[927.78 --> 928.46]  And
[928.46 --> 928.58]  You
[928.58 --> 928.84]  Can
[928.84 --> 929.68]  Nail
[929.68 --> 929.84]  It
[929.84 --> 930.16]  First
[930.16 --> 930.38]  Then
[930.38 --> 930.50]  That
[930.50 --> 930.68]  Gives
[930.68 --> 930.78]  You
[930.78 --> 930.88]  A
[930.88 --> 931.20]  Strong
[931.20 --> 931.64]  Position
[931.64 --> 932.30]  So
[932.30 --> 932.46]  We
[932.46 --> 932.80]  Think
[932.80 --> 933.20]  That
[933.20 --> 934.20]  A
[934.20 --> 934.46]  Win
[934.46 --> 934.58]  On
[934.58 --> 935.00]  iOS
[935.00 --> 935.22]  Is
[935.22 --> 935.34]  Going
[935.34 --> 935.38]  To
[935.38 --> 935.48]  Be
[935.48 --> 935.74]  Easier
[935.74 --> 935.90]  To
[935.90 --> 936.34]  Translate
[936.34 --> 936.48]  To
[936.48 --> 936.66]  Other
[936.66 --> 937.24]  Platforms
[937.24 --> 937.34]  And
[937.34 --> 937.54]  Vice
[937.54 --> 938.00]  Versa
[938.00 --> 939.08]  So
[939.08 --> 939.28]  One
[939.28 --> 939.40]  Of
[939.40 --> 939.54]  The
[939.54 --> 940.02]  Attractive
[940.02 --> 940.28]  Features
[940.28 --> 940.46]  Of
[940.46 --> 940.70]  Couch
[940.70 --> 940.80]  In
[940.80 --> 940.92]  The
[940.92 --> 941.26]  Past
[941.26 --> 941.48]  Has
[941.48 --> 941.88]  Been
[941.88 --> 942.06]  These
[942.06 --> 942.40]  Couch
[942.40 --> 942.68]  Apps
[942.68 --> 942.88]  Right
[942.88 --> 942.98]  And
[942.98 --> 943.16]  It's
[943.16 --> 943.56]  More
[943.56 --> 944.08]  Of
[944.08 --> 944.18]  A
[944.18 --> 944.48]  Move
[944.48 --> 945.06]  Back
[945.06 --> 945.22]  To
[945.22 --> 945.54]  Client
[945.54 --> 945.86]  Server
[945.86 --> 946.06]  Where
[946.06 --> 946.18]  You've
[946.18 --> 946.34]  Got
[946.34 --> 946.62]  Your
[946.62 --> 947.22]  Views
[947.22 --> 947.64]  And
[947.64 --> 948.88]  Presentation
[948.88 --> 949.14]  Logic
[949.14 --> 949.40]  Actually
[949.40 --> 949.70]  Running
[949.70 --> 950.50]  In
[950.50 --> 950.60]  Your
[950.60 --> 951.04]  Database
[951.04 --> 951.20]  So
[951.20 --> 951.30]  To
[951.30 --> 951.54]  Speak
[951.54 --> 951.74]  Is
[951.74 --> 951.92]  That
[951.92 --> 952.20]  The
[952.20 --> 952.56]  Same
[952.56 --> 953.12]  Pattern
[953.12 --> 953.28]  That
[953.28 --> 953.34]  You
[953.34 --> 953.58]  Follow
[953.58 --> 953.78]  With
[953.78 --> 953.86]  A
[953.86 --> 954.04]  Mobile
[954.04 --> 954.48]  Application
[954.48 --> 956.38]  Sort
[956.38 --> 956.62]  Of
[956.62 --> 957.66]  In
[957.66 --> 957.96]  The
[957.96 --> 958.16]  Sense
[958.16 --> 958.36]  That
[958.36 --> 958.66]  Couch
[958.66 --> 958.90]  Apps
[958.90 --> 959.38]  Are
[959.38 --> 960.02]  The
[960.02 --> 960.34]  Least
[960.34 --> 960.76]  Amount
[960.76 --> 961.26]  Of
[961.26 --> 962.48]  Stuff
[962.48 --> 962.72]  You've
[962.72 --> 962.90]  Got
[962.90 --> 963.04]  To
[963.04 --> 963.26]  Do
[963.26 --> 963.74]  Aside
[963.74 --> 964.24]  From
[964.24 --> 964.48]  The
[964.48 --> 964.68]  Thing
[964.68 --> 964.84]  That
[964.84 --> 965.04]  Runs
[965.04 --> 965.10]  In
[965.10 --> 965.18]  Your
[965.18 --> 965.44]  Browser
[965.44 --> 965.60]  That
[965.60 --> 965.72]  You're
[965.72 --> 965.90]  Already
[965.90 --> 966.10]  Good
[966.10 --> 966.28]  At
[966.28 --> 966.40]  I
[966.40 --> 966.42]  I
[966.42 --> 966.50]  I
[966.50 --> 966.68]  I
[966.68 --> 966.72]  I
[966.72 --> 967.62]  I
[967.62 --> 967.68]  I
[967.68 --> 968.08]  I
[968.08 --> 968.14]  I
[968.14 --> 968.38]  I
[968.38 --> 969.08]  I
[969.08 --> 970.20]  I
[970.20 --> 970.38]  I
[970.38 --> 971.20]  I
[971.20 --> 971.70]  I
[971.70 --> 972.20]  I
[972.20 --> 972.38]  I
[972.38 --> 972.80]  I
[972.80 --> 973.70]  I
[973.70 --> 974.14]  I
[974.14 --> 974.20]  I
[974.20 --> 974.26]  I
[974.26 --> 976.20]  I
[976.20 --> 976.38]  I
[976.38 --> 978.20]  I
[978.20 --> 978.38]  I
[978.38 --> 978.70]  I
[978.70 --> 978.80]  I
[978.80 --> 979.70]  I
[979.70 --> 980.20]  I
[980.20 --> 980.26]  I
[980.26 --> 980.38]  I
[980.38 --> 980.70]  I
[980.70 --> 980.74]  I
[980.74 --> 980.80]  I
[980.80 --> 981.80]  I
[981.80 --> 982.20]  I
[982.20 --> 982.80]  I
[982.80 --> 983.80]  I
[983.80 --> 984.28]  I
[984.28 --> 999.90]  I
[999.90 --> 1000.70]  I
[1000.70 --> 1002.52]  I
[1002.52 --> 1004.92]  I
[1005.12 --> 1006.12]  I
[1006.12 --> 1006.22]  I
[1006.22 --> 1006.34]  I
[1006.34 --> 1006.46]  I
[1006.46 --> 1006.74]  I
[1006.74 --> 1007.56]  I
[1007.56 --> 1007.64]  I
[1007.64 --> 1007.66]  I
[1007.66 --> 1008.50]  I
[1008.50 --> 1008.94]  I
[1008.96 --> 1009.12]  I
[1009.12 --> 1010.22]  I
[1010.22 --> 1013.96]  I
[1014.28 --> 1019.60]  Ideally, existing apps that already use Core Data, you just plug our library in and get the synchronization for free.
[1020.48 --> 1022.98]  That's the goal, and hopefully we can get there.
[1023.28 --> 1026.70]  But even if there's roadblocks, we've still got something I think is pretty valuable.
[1027.70 --> 1035.72]  So on your product page, you've got one of these nice manager-friendly diagrams that just has the word CouchSync between CouchBase and the mobile app.
[1035.78 --> 1037.50]  Is that replication, or how is that working?
[1038.08 --> 1038.94]  Yeah, that's replication.
[1039.60 --> 1043.34]  And so plain old replication is just so easy to do in Couch.
[1043.34 --> 1055.36]  You post some JSON via HTTP at the server and tell it the remote server that you want it synchronized with, and it does the rest of the work and does it as bandwidth efficient as possible.
[1056.26 --> 1063.56]  And you can even tell it to continuously keep up to date, which that even turns out to be a good fit for mobile networks.
[1063.94 --> 1071.92]  That long pole or continuous changes feed connection is actually – I thought it was going to run counter to the way cell networks work,
[1071.92 --> 1075.72]  but they're already optimized for these kind of long-running, mostly quiet connections.
[1077.06 --> 1078.52]  So that was nice.
[1079.08 --> 1090.96]  So basic replication is a really good fit for mobile, but there are some patterns that we want to embody in CouchSync to make things easier.
[1091.08 --> 1094.76]  So for instance, on the membase side, one of the big users is Zynga.
[1094.76 --> 1098.86]  So you can imagine all the data in FarmVille, and right now it's in a big cluster.
[1099.44 --> 1106.94]  But if you want to take FarmVille and make it offline capable, then you'd need to have the ability to get the data for a single given user
[1106.94 --> 1116.62]  and put it in its own little database, essentially so that the user can then replicate that back and forth for their backup slash offline.
[1116.62 --> 1123.52]  So tools to make that stuff super easy, that's what's out on the horizon for us.
[1125.10 --> 1127.28]  Let's talk about CouchApps for a moment.
[1127.50 --> 1128.42]  Did you coin this term?
[1129.70 --> 1130.62]  I guess so.
[1130.72 --> 1131.74]  I mean, it's kind of obvious.
[1132.46 --> 1135.00]  Pretty much every Couch term in the universe is taken at this point.
[1135.00 --> 1146.62]  But yeah, the CouchApps script that's like sort of a developer toolkit that you can find linked from CouchApp.org, implemented in Python.
[1147.24 --> 1154.30]  Now, I originally wrote something in Ruby that did essentially the same thing and just didn't have time to do the maintenance burden.
[1154.38 --> 1159.28]  So I handed it off to Benoit and Jan, both CouchTB committers.
[1159.28 --> 1166.90]  And they worked on it some in Ruby and then decided to port it to Python because that's where Benoit is.
[1167.34 --> 1168.38]  That's where he feels most comfortable.
[1168.52 --> 1173.64]  So now we've got this Python thing with all these practically enterprise-y features.
[1173.86 --> 1176.20]  You can write eggs to plug into it.
[1176.42 --> 1179.80]  I don't use any of that stuff, but it's good that it's there when you need it.
[1180.78 --> 1184.82]  So that's a developer tool chain, but it's different from the idea.
[1184.82 --> 1194.46]  The idea of a CouchApp is just an app that is served out of CouchDB and to whatever the native client you have around is.
[1194.52 --> 1197.66]  The most popular native client in the world right now, of course, is the HTML browser.
[1198.92 --> 1205.30]  But on iOS, if it's just Objective-C and CouchDB, I'll call that a CouchApp.
[1205.30 --> 1218.48]  So, yeah, I think that the real fundamental idea is that if you are allowing your users to take a database offline onto their device,
[1218.94 --> 1223.98]  you've kind of got to understand the security model of the fact that they've got a copy of all the data.
[1224.50 --> 1230.46]  And so the place where you apply your security policy is going to be on that inbound replication stream.
[1230.46 --> 1239.32]  It's not going to be by writing some middleware Rails app or something that sits there and validates everything as it's going through.
[1240.42 --> 1247.22]  You know, one of the things that I noticed when I got into development was that no matter how good you were on the front end,
[1247.28 --> 1255.92]  unless you were an uber front-end ninja, to use the term, you pretty much had to deal with a server implementation of some sort.
[1255.92 --> 1264.10]  And we were all kind of in tribes based on whichever server platform you chose because you really couldn't afford to pick up more than one
[1264.10 --> 1267.58]  because it was such an overhead of knowing more than one platform.
[1267.82 --> 1279.76]  But as apps like CouchDB and Node.js have taken off, it seems like we've kind of this JavaScript layer that all of us were familiar with
[1279.76 --> 1284.92]  as we started to do more with it, we're starting to kind of bleed or blur those lines in between our tribes.
[1284.92 --> 1286.04]  Have you noticed anything like that?
[1286.98 --> 1287.44]  Well, absolutely.
[1287.66 --> 1292.28]  I mean, especially, you know, talking about the cutting-edge developers who have the choice to use the tools they want.
[1293.46 --> 1298.06]  You know, JavaScript seems to be really taking off, and I think that's the reason is, you know,
[1298.06 --> 1304.74]  why I switch all those contexts when JavaScript has, you know, most of the runtime benefits that the other languages can give you.
[1304.90 --> 1310.66]  But on the other hand, you do have a bunch of developers, you know, in the enterprise world who don't get to pick what they use.
[1310.76 --> 1312.14]  However, that's even changing.
[1312.14 --> 1317.04]  I mean, JavaScript in the browser has been common there for a long time, so maybe we can leapfrog.
[1318.10 --> 1324.54]  People can move, you know, straight from their, you know, vb.net backends to Couch apps.
[1324.88 --> 1335.54]  And we've heard stories of, you know, large internal, you know, customer management systems and stuff being moved over to Couch and getting, you know, much better.
[1335.54 --> 1344.50]  Basically, less code means less to maintain, and also a lot of these guys have been seeing better performance just because, you know,
[1344.56 --> 1347.98]  you don't have a Java stack trace, you know, 50 frames deep or whatever.
[1348.54 --> 1353.70]  You know, one of the things that intrigues me about Couch is not only does it collapse a lot of the middle layers,
[1353.82 --> 1360.02]  which seem to be superfluous for a lot of the smaller end apps, but also it's built-in versioning for everything,
[1360.02 --> 1361.88]  not just your data, but you're also, you're GUI.
[1363.18 --> 1368.64]  Yeah, yeah, I mean, it's got, so it's important to distinguish CouchDB's, you know,
[1368.70 --> 1372.46]  the built-in versioning, as it were, is multi-version concurrency control.
[1372.70 --> 1376.80]  So what that means is if, you know, we're both working on the same, against the same cloud server,
[1377.14 --> 1380.66]  and you load the document, and I load the document, and then you make a change and save it,
[1380.66 --> 1384.94]  when I try to save it, Couch is going to reject my save as being out of date,
[1385.32 --> 1387.82]  and that's just to prevent race conditions.
[1388.48 --> 1394.26]  But it also means that readers can always proceed against a view query or against, you know,
[1394.30 --> 1397.44]  scanning the documents in a database without being blocked by writers.
[1397.88 --> 1400.44]  Everyone has, you know, their own independent snapshot of the database.
[1400.90 --> 1405.50]  So that's all, you know, goes really deep into the technical design of Couch when you start to look at it.
[1405.50 --> 1413.66]  But the thing to be clear on is that, by default, those old versions do not get replicated around.
[1413.80 --> 1416.54]  So when you synchronize, it just sends, you know, the current version.
[1417.48 --> 1420.98]  When you compact, which, you know, if you're not your own DBA,
[1421.10 --> 1424.98]  your DBA may compact when you least expect it to clean up wasted space.
[1425.00 --> 1427.06]  That'll also clean up the outdated versions.
[1427.94 --> 1429.72]  That's not to say you can't do versioning in Couch.
[1429.72 --> 1434.14]  There's lots of applications that either do like a, you know, entity for, you know,
[1434.14 --> 1440.16]  have an entity document and then log additional documents that refer, you know, refer to that entity.
[1441.76 --> 1446.76]  So you can do patterns like that, or you can do patterns like actually keeping the full history
[1446.76 --> 1451.24]  as binary attachments on the old history.
[1451.34 --> 1452.76]  So there's a lot of patterns there to do.
[1452.90 --> 1457.50]  And it's, if you Google, you know, CouchDB simple document versioning,
[1457.50 --> 1458.98]  I wrote a blog post about this a few months.
[1458.98 --> 1462.90]  It'll come up and it'll kind of go through the pros and cons of all the patterns.
[1464.14 --> 1469.02]  In an effort to keep it real, what sort of applications are not suited for CouchDB?
[1470.30 --> 1471.60]  Yeah, that's a good question.
[1471.80 --> 1477.70]  I think that, you know, a worst case scenario for what, you know,
[1477.72 --> 1484.48]  how much storage and resources you're using up compared to, you know, the alternative.
[1485.16 --> 1489.40]  Like a real-time message queue where you don't care about archiving it.
[1489.40 --> 1492.42]  So, you know, some kind of something where you've got something that's, you know,
[1492.44 --> 1493.74]  fairly reliable but in memory.
[1495.04 --> 1500.08]  And, you know, that's, so if you were going to do that workload in CouchDB,
[1500.22 --> 1504.44]  you'd have all the message history, you know, for that application stored on disk.
[1504.94 --> 1510.40]  On the other hand, most real-time messaging applications do have some sort of need to archive
[1510.40 --> 1511.24]  and query the messages.
[1511.42 --> 1513.56]  I mean, maybe not most, but a fair proportion of them.
[1513.56 --> 1515.90]  So I've seen Couch used for spam filters.
[1516.14 --> 1518.78]  I've seen Couch, you know, used for chat rooms.
[1519.04 --> 1522.36]  And it makes a good fit for that sort of stuff.
[1523.54 --> 1525.76]  The, you know, other ephemeral data.
[1526.32 --> 1530.76]  So if you were just doing like a dig style upvote counter on a post,
[1531.32 --> 1534.32]  maybe, you know, maybe something else would be a better fit.
[1534.36 --> 1536.24]  Although we're addressing that.
[1536.24 --> 1541.40]  I think there is some truth to be said that right now the different NoSQLs have all been
[1541.40 --> 1545.26]  kind of finding their niche and getting entrenched there.
[1545.56 --> 1550.14]  But really, everyone's going after some form of 80% solution.
[1550.30 --> 1555.02]  So people are going to be adding each other's feature sets to the extent that it makes sense technically.
[1556.92 --> 1560.46]  What was involved with getting the Erlang runtime on iOS?
[1561.10 --> 1562.26]  Do you guys have to talk about that?
[1562.26 --> 1562.36]  Sure.
[1563.46 --> 1568.62]  Our engineer, Aaron Miller, is, you know, gets most of the credit for that.
[1568.80 --> 1571.14]  So he went through the Erlang VM.
[1571.42 --> 1572.76]  You know, Erlang is implemented in C.
[1573.68 --> 1578.30]  And it uses dynamic linking for, you know, kind of a whole lot of it.
[1578.48 --> 1583.02]  You know, it's basically built out of its own plug-in system at some level.
[1583.52 --> 1587.22]  And so he went through and turned all that dynamic linking into static linking,
[1587.22 --> 1592.26]  which was just like, you know, touching a bunch of code and having to know what to do.
[1592.36 --> 1595.68]  And then there was a bunch of other, you know, strange little gotchas that you wouldn't expect.
[1597.18 --> 1607.80]  But, you know, for instance, Erlang uses a, you know, uses the syscall fork to create a sub process to handle DNS lookups.
[1607.80 --> 1610.58]  And that's just not going to fly on iOS.
[1610.76 --> 1611.42]  You can't do fork.
[1611.58 --> 1614.14]  So we had to do, you know, little subtle changes like that.
[1614.20 --> 1618.26]  We also had to get SpiderMonkey running on the device.
[1618.40 --> 1623.20]  So we have JavaScript running in a background thread because the built-in JavaScript on iOS,
[1623.90 --> 1629.66]  at least to my knowledge, always blocks the main UI thread when it's running.
[1629.78 --> 1632.56]  So you can't have the UI locked up just because a MapReduce is generating.
[1632.56 --> 1640.44]  So we included that SpiderMonkey in there, which I think also had to have some technical changes.
[1640.74 --> 1644.96]  But, you know, mostly it was just a matter of getting the build cleaned up
[1644.96 --> 1651.00]  and then going through and conforming to, you know, sort of Apple's view of the world.
[1651.90 --> 1657.46]  Was SpiderMonkey a holdover from a previous design decision or any consideration for V8?
[1657.46 --> 1662.38]  Yeah, so we've done the SpiderMonkey V8 shootout and SpiderMonkey wins.
[1662.92 --> 1667.44]  And the reason why is because V8 is optimized for, you know, process launch time.
[1667.54 --> 1669.66]  You open a new tab, it needs to be responsive right away.
[1670.46 --> 1675.84]  SpiderMonkey has the JIT compiler, which, you know, as it's running,
[1675.96 --> 1678.52]  especially with these map functions where you define the function once
[1678.52 --> 1682.26]  and then run 100,000 documents through it, the JIT will get it up to, you know,
[1682.28 --> 1684.14]  faster than C in some places.
[1684.14 --> 1689.10]  So coupled with that, SpiderMonkey seems to use a little less memory than V8.
[1690.44 --> 1693.50]  And, you know, the startup time being not that important to us,
[1694.20 --> 1699.02]  we find that SpiderMonkey is better for at least on a big server install of Couch,
[1699.10 --> 1700.04]  you're going to get better throughput.
[1701.50 --> 1706.16]  You know, that being said, on iOS, if we could somehow use the built-in Nitro or whatever,
[1706.36 --> 1709.06]  I mean, the, you know, number one constraint there is I wouldn't, you know,
[1709.08 --> 1711.50]  I'd rather not have to download all of SpiderMonkey to the device,
[1711.78 --> 1712.94]  even if it's a little slower.
[1712.94 --> 1715.36]  So we're working on figuring out solutions there.
[1717.00 --> 1720.08]  So CouchDB is part of the Apache Foundation lineup.
[1720.40 --> 1723.54]  What is the licensing rundown on everything CouchBase these days?
[1724.60 --> 1731.44]  So CouchBase right now has Mimbase, which is, I think, Apache licensed.
[1732.58 --> 1739.38]  And then, you know, CouchBase, which is our build of CouchDB that includes GeoCouch
[1739.38 --> 1742.36]  and some other little features and QA and stuff.
[1743.36 --> 1745.34]  And that's Apache licensed as well.
[1746.06 --> 1751.26]  As far as what the license is going to be on, you know, stuff way down in the future,
[1751.56 --> 1752.98]  we're still figuring that out.
[1752.98 --> 1763.24]  But, you know, the main consideration for me right now is I want to make sure that we're contributing to the Apache CouchDB community,
[1763.84 --> 1769.30]  you know, not just code, but that Apache CouchDB is where, you know, the work,
[1769.66 --> 1773.16]  the Erlang work, you know, that's appropriate where that ends up.
[1773.16 --> 1777.92]  But, you know, we could have easily come out the gate and said, okay, we're just going to, like, you know,
[1777.96 --> 1780.40]  fork CouchDB and try and build up a community around that fork.
[1780.50 --> 1784.04]  But I would much rather, you know, stay in the Apache CouchDB community.
[1785.18 --> 1791.52]  So on your comparison page, you compare yourself to CouchBase versus Cassandra and MongoDB.
[1791.78 --> 1794.22]  So we've had Reoc on the show twice.
[1794.40 --> 1798.58]  Any other NoSQL options out there that you could draw a distinction to?
[1798.58 --> 1808.72]  You know, I think that it's real important that people understand that CouchDB's MapReduce is really different from all the others,
[1809.82 --> 1810.84]  and especially Hadoop.
[1811.34 --> 1816.64]  So Hadoop is, as far as I'm concerned, the big winner right now for, you know,
[1816.66 --> 1820.76]  especially in the enterprise people, you know, doing something other than just using Oracle.
[1822.60 --> 1826.74]  And so, you know, CouchDB MapReduce is incremental.
[1826.74 --> 1833.08]  And what that means is that if you, you know, have 10 million documents in a database and you define a view,
[1833.24 --> 1835.28]  then it takes some time to build that view the first time.
[1835.88 --> 1838.86]  But queries against that index are almost instantaneous.
[1839.60 --> 1845.74]  And then on top of that, CouchDB automatically keeps the index up to date as efficiently as possible
[1845.74 --> 1849.22]  just by recomputing based on changes.
[1849.22 --> 1856.90]  Whereas Hadoop-style MapReduce, which is what you'll find in the other products for the most part,
[1857.20 --> 1859.58]  is it's a batch process.
[1859.92 --> 1866.10]  So you'll put a few gigabytes into HDFS and then define your query and run it on it
[1866.10 --> 1873.48]  and take the results of that query and maybe put them back into a database for, you know, real-time viewing.
[1873.48 --> 1877.76]  So if you change, you know, 20% of those inputs,
[1877.88 --> 1882.46]  then it's usually better in the Hadoop context to just rebuild the whole thing, which is fine.
[1882.56 --> 1884.30]  I mean, Hadoop obviously seems very popular,
[1884.90 --> 1890.40]  but it's different from the kinds of MapReduce that would be useful to a company like Zynga
[1890.40 --> 1895.32]  wanting to support FarmVille and having real-time results available, you know, as they stream in.
[1896.18 --> 1898.68]  So in the mobile context, you mentioned long-running connections.
[1898.68 --> 1902.70]  What's available with CouchDB on the desktop or the server?
[1904.06 --> 1904.26]  Sure.
[1904.52 --> 1912.36]  So we have a CouchBase desktop for OSX that is a rev of CouchDBX,
[1912.42 --> 1914.20]  a project that Jan had been working on for a long time.
[1914.90 --> 1920.34]  It's finally, you know, cleaned out some of the annoyances and stuff
[1920.34 --> 1925.36]  and really stripped it down to just being an icon in your menu bar that, you know,
[1925.36 --> 1928.66]  has a CouchBase server running there, and you can pop it open on port 5984,
[1928.66 --> 1932.26]  and, you know, create documents and play around in futon.
[1933.08 --> 1936.02]  So that was, I think that's important for supporting developers.
[1936.56 --> 1944.68]  On the server, that, you know, we also have a CouchBase server build for, you know, Linux and Windows.
[1945.56 --> 1950.16]  And we see actually, you know, starting to get some interest from the Windows side of the world.
[1950.16 --> 1955.56]  But in the long run, you know, everyone's asking us, what about scale up?
[1955.62 --> 1956.46]  What about scale out?
[1956.62 --> 1960.36]  Because currently Apache CouchDB is designed for a single node.
[1960.52 --> 1964.38]  The API is designed to scale up, but the actual implementation doesn't contain that.
[1965.54 --> 1967.26]  So that's what we're going for.
[1967.46 --> 1971.48]  I mean, you know, that's the point of this merger is that when we've got our combined product,
[1971.72 --> 1974.66]  it's going to be the big, fast CouchDB that everyone always wished for.
[1974.66 --> 1977.92]  So what becomes of Couch.io?
[1979.22 --> 1983.04]  That's just an old domain name that I've still got laying around.
[1984.56 --> 1991.46]  So, yeah, so we've got, you know, the history of the company was we founded it as the, you know,
[1991.60 --> 1996.48]  the business entity being Relax Incorporated, which is kind of like GitHub's Logical Awesome.
[1996.48 --> 2003.78]  And then, yeah, we had this Couch.io domain name, which was cute, but it had usability issues.
[2004.12 --> 2007.86]  And that's, you know, just became obvious the more people that we talked to about it.
[2008.46 --> 2010.72]  So that's why we switched to Couch1.
[2011.26 --> 2017.86]  And, you know, finally with the merger, we were, you know, Couchbase, kind of obvious coming out of Couch1 and Mimbase.
[2017.86 --> 2024.04]  And my cabbie in Austin last weekend, you know, could understand what I was saying right away.
[2024.12 --> 2028.16]  I said Couchbase, and, you know, he wasn't like, couch what, which happens when you say CouchDB.
[2028.74 --> 2030.94]  So I was pretty happy about that.
[2031.52 --> 2035.72]  So we're not allowed to entertain the idea of changing the company's name ever again.
[2038.00 --> 2039.50]  So what about Couch in the Cloud?
[2040.62 --> 2045.48]  Oh, so the Couch hosting that we have is expanding.
[2045.48 --> 2052.14]  We've got, well, we've just recently been going through some upgrade pains, you know, as everything does.
[2052.24 --> 2055.06]  But we've moved everyone's data on to EBS.
[2055.24 --> 2060.90]  So we're getting faster latency and, you know, better throughput on those boxes.
[2062.26 --> 2068.36]  Jason is, Jason Smith is our guy in Thailand who handles most of the hosting.
[2068.76 --> 2073.44]  And he's also working on, you know, rolling out the paid options for hosting.
[2073.44 --> 2083.76]  And so it's really going to be, you know, catering to professional users who are, you know, either storing mission critical data in there or want to use it as a, you know, development point in the cloud.
[2085.10 --> 2087.74]  So there's other services out there, Cloudant being one.
[2087.98 --> 2095.26]  Are you guys supporters of that as far as paid commercial support or do you see them as a competitor long term?
[2095.26 --> 2100.12]  Well, long term, what we see is the more CouchDB companies, the better.
[2101.18 --> 2103.10]  And so, you know, we love it that Cloudant's there.
[2103.40 --> 2104.48]  There's another company.
[2105.10 --> 2108.94]  I think they're still stealth, but they're actually working on a Couch app marketplace.
[2110.70 --> 2115.92]  So there's a fair amount of action going on in the CouchDB ecosystem.
[2116.34 --> 2118.28]  And, you know, we think the more diversity, the better.
[2118.28 --> 2126.56]  So Cloudant has Big Couch, which is sort of the, you know, it's a CouchDB that scales out.
[2126.96 --> 2130.76]  And it's all written in Erlang and is fairly performant and high throughput.
[2131.28 --> 2134.40]  And we think that's great to have out there, have people using it.
[2135.36 --> 2138.48]  It's a little, or at least their, you know, their business model.
[2139.12 --> 2139.74]  Excuse me.
[2140.18 --> 2145.64]  Cloudant's business model is a little more focused on, you know, kind of these real-time search workloads.
[2145.64 --> 2155.88]  So they've got a lot of customers who are consuming, you know, Twitter Firehose or, you know, other feeds like that and doing semantic analysis and stuff on top of their, on top of that data.
[2156.54 --> 2160.38]  We're a lot more interested in the, you know, real-time.
[2160.76 --> 2164.60]  Somebody clicked to buy a cabbage and now they have a cabbage.
[2165.06 --> 2166.04]  Those kind of queries.
[2167.70 --> 2175.48]  So, you know, we think that there's room easily for Cloudant and CouchBase and hopefully a whole slew of other companies to come along.
[2176.24 --> 2187.70]  So for the developer that's not doing just front-end, back-end, direct JavaScript to Couch type application architecture, where are you seeing the growth and adoption?
[2187.88 --> 2190.64]  In Python, Ruby, what sorts of communities are embracing Couch?
[2190.64 --> 2204.78]  So we're going right now to focus on PHP first because, you know, the runtime already makes a lot of sense with, you know, Couch's ability to crash and recover quickly.
[2204.92 --> 2207.60]  The PHP runtime, every single request is isolated.
[2207.60 --> 2214.16]  So if you have, you know, if what you need to do is turn some JSON into some HTML, you can do worse than to turn to PHP.
[2214.84 --> 2223.16]  But on the other hand, they need, there's some work that needs to be done there to make the clients really, you know, really smart and strong.
[2223.16 --> 2232.46]  So we're plowing energy into the PHP drivers, also into Ruby and Python and Java and .NET.
[2232.46 --> 2240.40]  So it's actually Jan who's heading up the effort to put our SDKs together for the various platforms and picking which ones to do first.
[2240.64 --> 2245.78]  And maybe we're picking to start with PHP because Jan's an old-time PHP guy.
[2246.42 --> 2250.00]  Don't tell anyone, but he's got a php.net email address.
[2250.00 --> 2250.44]  Nice.
[2250.96 --> 2251.40]  Nice.
[2252.52 --> 2254.00]  So let's switch gears for a moment.
[2254.78 --> 2259.78]  When you're not hacking on Couch or Couch apps, what's really got you excited in the world of open source?
[2261.22 --> 2261.66]  Oh, gosh.
[2262.06 --> 2263.08]  That's a good question.
[2263.30 --> 2265.22]  I've been so heads down.
[2265.78 --> 2271.62]  First of all, you know, I'm on the merger and now finally getting back to write code.
[2271.62 --> 2287.16]  But, you know, I think that the mobile stuff, iOS, Erlang, I mean, I'm sorry, iOS and Android are really kind of, they're still going to surprise us.
[2287.62 --> 2290.68]  People are making fun of that color funding.
[2290.90 --> 2297.26]  You know, they raised like $40-something million, which is maybe more money than seems reasonable.
[2297.50 --> 2299.08]  But their app seems kind of cool.
[2299.24 --> 2299.64]  I don't know.
[2299.64 --> 2313.62]  Maybe, I don't know about the financial side of it, but I think that this kind of finding people who are near you in real-time stuff is, you know, hasn't even started to change the world yet compared to how it's going to.
[2314.10 --> 2314.98]  I'll tell you what I'd like to see.
[2315.42 --> 2315.96]  Oh, yeah, yeah.
[2315.96 --> 2329.16]  I'd like to see the new Couch-based mobile be a module for Titanium AppCelerator so that you've got, or AppCelerator Titanium Mobile so that you've got a CouchDB option on both iOS and Android one day.
[2329.64 --> 2335.30]  Yeah, so we know of at least a few apps out there that are using Titanium and CouchDB together.
[2335.76 --> 2342.90]  I'm not sure if the code is open source or, you know, clean enough to turn it into a module, but people are doing it, so it seems like it's a good fit.
[2342.90 --> 2357.46]  Yeah, and I'm doing what I can, meeting with, you know, all these various HTML5 kind of UI and widget component companies and, you know, jQuery Mobile and delving into all that.
[2357.46 --> 2371.40]  If people are out there and are kind of interested in the intersection between frontend and mobile, there's a seven-part series by this guy Todd Anderson on jQuery Mobile and CouchDB.
[2371.82 --> 2377.92]  And if you go through that seven-part series, you'll come out the other end of it probably better at that stuff than I am right now.
[2377.92 --> 2389.50]  I mean, it's just got everything you need to know, you know, so a week from now you can be an expert iOS CouchDB developer or, you know, HTML5 Mobile CouchDB developer.
[2389.66 --> 2390.76]  Todd Anderson, no relation?
[2391.70 --> 2392.52]  Nope, no relation.
[2393.38 --> 2395.14]  But, well, not that we know of yet.
[2395.14 --> 2397.82]  So, one last question.
[2398.58 --> 2399.78]  Who's your programming hero?
[2401.46 --> 2406.56]  Oh, you know, that's kind of easy because I get to hang out with him on a fair basis.
[2406.84 --> 2409.66]  At the risk of being a fanboy, Damian's pretty awesome.
[2409.84 --> 2417.06]  I mean, as far as knowing what not to do, he's always coming to me saying, like, Chris, are you sure you want to write that code?
[2417.34 --> 2419.58]  You know, if you write that code, someone's going to have to maintain it.
[2419.58 --> 2428.24]  And that's like having somebody be that conscious to not always add features is, you know, is really cool.
[2428.42 --> 2433.20]  And then being able to see how stuff at the low level affects stuff at the high level.
[2434.18 --> 2439.78]  One story that, you know, he tells about Erlang that is, you know, really true.
[2440.28 --> 2447.54]  I saw some performance benchmarks of some, what was it, an image converter that someone had written Erlang, which seems unlikely to be fast, but it was.
[2447.54 --> 2454.14]  So, each Erlang process, which is, you know, an Erlang process is kind of similar to a Java object.
[2454.32 --> 2457.18]  You can create 100,000 of them in a second.
[2457.88 --> 2463.00]  And you can, you know, and they're all running concurrently scheduled by the scheduler.
[2463.38 --> 2467.96]  So, each one of those has its own isolated stack and its own isolated heap.
[2468.46 --> 2473.16]  And that means that when one gets swapped onto a core, the whole thing gets swapped onto the core.
[2473.16 --> 2481.04]  And, you know, maybe it doesn't all fit right there on the L1 cache, but over the, you know, over the cache hierarchy, the active memory is all just localized.
[2481.82 --> 2489.14]  As opposed to threaded concurrent code, which has to jump, you know, randomly across memory access all the time, potentially.
[2490.02 --> 2492.74]  So, you've got these, you know, little processes that get swapped in.
[2492.88 --> 2496.18]  They burn through their workload and then they get swapped out for another one.
[2496.18 --> 2501.10]  And then on top of that, since they're isolated, they can be garbage collected independently.
[2502.26 --> 2505.96]  And that means, you know, you don't have any stop the world pauses when the garbage collector is running.
[2506.12 --> 2508.08]  And if a process is done, you can just throw it out.
[2508.14 --> 2509.36]  You don't even have to crawl its heap.
[2509.36 --> 2516.72]  So, those things combined together, you know, this is the sort of stuff that Damien explains to me and then I get all excited about.
[2517.52 --> 2526.10]  But I've seen Erlang apps where, you know, you dial up the benchmark on it after it's, you know, after it's sort of prototyped.
[2526.44 --> 2528.20]  And you look at it and you go, this isn't going to work.
[2528.30 --> 2531.66]  This is just, you know, we're like two orders of magnitude outside of spec here.
[2532.76 --> 2536.36]  But that's only with, you know, 50% load applied.
[2536.36 --> 2541.46]  So, then you do, you know, a couple of optimizations and you're getting better but it still doesn't look great.
[2541.70 --> 2551.72]  And then you go crank the load up all the way, you know, actually get more than one box that's not the server box to apply load with instead of just, you know, A, B running on one box or something.
[2552.32 --> 2560.40]  Really saturate it and the process scheduler can do these optimizations it can't do when it's less busy.
[2560.40 --> 2567.70]  And so, you end up getting kind of this better than linear ringing out, you know, the last bits of performance from the box.
[2567.90 --> 2572.02]  And just any kind of language that can do that is, I don't know, awesome.
[2572.44 --> 2575.64]  And it's even more fun when Damien comes along and tells you why that happened.
[2576.30 --> 2581.68]  You know, one of the things that struck me about Damien when I first discovered Couch TV was just the story behind the project.
[2581.68 --> 2590.72]  And how he basically punted on his corporate career that was just not satisfying him to follow an open source project, which he didn't even know what it was at the time.
[2592.06 --> 2592.26]  Yeah.
[2593.24 --> 2598.68]  I mean, that's, if people want to see that story, the best resources.
[2599.02 --> 2607.14]  He did, or InfoQ has the video posted from the talk he did at Ruby Fringe back in, I think, 2009.
[2607.78 --> 2608.62]  Maybe it was 2008.
[2608.74 --> 2610.88]  But, yeah, back at the Ruby Fringe conference in Toronto.
[2612.54 --> 2614.84]  Yeah, he got a standing ovation for that talk.
[2614.98 --> 2616.38]  And I think he tears up in the middle.
[2616.48 --> 2617.20]  So, it's worth watching.
[2617.72 --> 2618.92]  Definitely put that in the show notes.
[2619.02 --> 2621.02]  One last question for you as a bonus.
[2621.60 --> 2625.18]  So, I had the opportunity to be on the NoSQL Smackdown with your buddy Jan.
[2625.26 --> 2627.60]  I think you made an appearance in that one as well.
[2628.30 --> 2630.82]  What's it like working with Jan?
[2630.82 --> 2634.84]  Is he half as passionate in his day-to-day job as he was on that panel?
[2635.62 --> 2636.64]  Oh, yeah, he definitely is.
[2636.64 --> 2641.96]  He's the guy who, you know, there will be a meeting and, you know, someone will say something.
[2642.38 --> 2644.54]  And I'll be like, I don't know about that.
[2644.60 --> 2648.94]  But it doesn't, you know, not enough to, like, actually speak up because I've got whatever else on my mind.
[2649.08 --> 2653.82]  And I'll just jump right in and, you know, get to the bottom of whatever the issue is.
[2654.68 --> 2659.14]  And so, you know, it takes you a minute to get used to that.
[2659.14 --> 2660.78]  But then you start to thank him for it.
[2660.78 --> 2672.82]  And that's, you know, it's important to have people who are really looking out for, you know, especially looking out for end users and developers and, you know, making sure that it takes the least amount of clicks to get to the download and all that.
[2674.30 --> 2681.52]  Well, Chris, certainly appreciate the time and taking the time out of a busy schedule after the merger here to tell us about the new lineup and where you're headed.
[2681.52 --> 2683.18]  Yeah, thanks, Wyn.
[2683.92 --> 2684.88]  Glad to be here.
[2685.20 --> 2695.06]  And anybody who's, you know, getting started with Couch and gets stuck or whatever, you know, has questions, the community really loves helping new people.
[2695.38 --> 2703.18]  So even if you just, you know, tweet about your, oh, I wrote this MapReduce, you know, at CouchDB, you'll probably get some helpful replies.
[2704.02 --> 2704.70]  Cool. Thanks again.
[2704.70 --> 2734.68]  Thank you.

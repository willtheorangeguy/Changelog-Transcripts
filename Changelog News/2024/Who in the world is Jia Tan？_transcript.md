[0.00 --> 14.00]  What up nerds? I'm Jared, and this is Changelog News for the week of Monday, April 1st, 2024.
[14.74 --> 20.72]  Yes, it's April Fool's Day, the worst day of the year to be an internet denizen. But don't worry,
[20.96 --> 27.42]  Changelog News is 100% prank-free, AI-free, and gluten-free too. The big story right now is the
[27.42 --> 35.92]  recently uncovered backdoor in LibLZMA, aka XZ, a relatively obscure compression library that
[35.92 --> 41.62]  happens to be a dependency of OpenSSH. This incident is noteworthy for so many reasons.
[41.94 --> 46.88]  The exploit itself, how it was deployed, how it was found, what it says about our industry,
[47.12 --> 51.58]  and how the community reacted. Today's episode is entirely dedicated to this story,
[51.58 --> 55.64]  looking at it from all those angles. So let's get straight into the news.
[55.64 --> 62.46]  The Discovery. Let's start our story the same way most folks did on Friday when Microsoft
[62.46 --> 69.62]  researcher Andres Frund posted an email to Debian's OSS security list containing this bombshell.
[69.96 --> 76.30]  Quote, after observing a few odd symptoms around LibLZMA, part of the XZ package,
[76.30 --> 81.88]  on Debian SID installations over the last weeks, logins with SSH taking a lot of CPU,
[81.88 --> 89.56]  Valgrind errors, etc. I figured out the answer. The upstream XZ repository and the XZ tarballs
[89.56 --> 94.14]  have been backdoored. At first, I thought this was a compromise of Debian's package,
[94.46 --> 100.22]  but it turns out to be upstream. End quote. Andres goes on to explain his findings in detail.
[100.62 --> 105.92]  The mind-blowing thing is that he decided to shave this particular yak because he was doing some
[105.92 --> 112.32]  microbenchmarking and needed the system to be super low load, which made him realize that SSHD was
[112.32 --> 117.76]  using a lot of CPU. Go read all the work he put in to find the backdoor and then consider how
[117.76 --> 123.12]  specific his situation had to be in order to even notice it. Thankfully, he found the backdoor
[123.12 --> 128.80]  relatively early in its rollout. Quote, due to the working of the injected code, it is likely the
[128.80 --> 138.06]  backdoor can only work on glibc-based systems. Luckily, XZ 5.6.0 and 5.6.1 have not yet widely
[138.06 --> 142.48]  been integrated by Linux distros, and where they have, mostly in pre-release versions.
[142.88 --> 149.42]  The code. The exploit itself is super interesting as well. I'm not ashamed to say most of it's over
[149.42 --> 155.38]  my head, but recurring changelog guest Filippo Valsorda does a great job explaining the nitty-gritty
[155.38 --> 160.66]  details. Follow the link if you're interested in all of the particulars, but this statement sums it
[160.66 --> 166.50]  up well. Quote, this might be the best executed supply chain attack we've seen described in the
[166.50 --> 172.90]  open, and it's a nightmare scenario. Malicious, competent, authorized upstream in a widely used
[172.90 --> 177.70]  library. Looks like this got caught by chance. Wonder how long it would have taken otherwise.
[177.70 --> 185.90]  End quote. So, the attacker is competent, malicious, and has authorized write access to a widely used
[185.90 --> 192.90]  library. How did that happen? The maintainer. The linked page is maintained by Lassie Collin,
[193.22 --> 198.90]  the solo maintainer of XZ. Can you guess where all this is headed? Lassie says, quote,
[198.90 --> 207.16]  XZutils 5.6.0 and 5.6.1 release tarballs contain a backdoor. These tarballs were created and signed by
[207.16 --> 215.10]  Gia Tan. Tarballs created by Gia Tan were signed by him. Any tarballs signed by me were created by me.
[215.38 --> 223.74]  GitHub accounts of both me and Gia Tan are suspended. End quote. Gia Tan? Who's that? The plot thickens.
[223.74 --> 232.96]  It's now time for sponsored news. AI-powered autofix debugs and fixes your code in minutes.
[233.60 --> 239.24]  Ben Pevin, writing for Sentry, says, quote, Sentry knows a lot about the inner workings of an
[239.24 --> 244.48]  application's code base. So we got to thinking, how can we use this rich data set to make debugging
[244.48 --> 251.20]  with Sentry even faster? Many generative AI tools, like GitHub Copilot, improve developer productivity
[251.20 --> 256.68]  in their dev environment, though few have the contextual data Sentry has to help fix errors
[256.68 --> 262.72]  in production. Our new AI-enabled autofix feature understands what your users are doing when an
[262.72 --> 268.60]  error occurs, analyzes the error, generates a fix, and even opens a pull request for your review.
[268.94 --> 275.00]  It's like having a junior developer ready to help on demand. End quote. Pretty cool stuff. Give it a try.
[275.00 --> 281.44]  Oh, and don't forget to use code CHANGELOG when you sign up for Sentry to get $100 off their team plan.
[281.66 --> 284.42]  Thanks again to Sentry for sponsoring Changelog News.
[284.80 --> 295.48]  The attacker. Evan Bowes looked up the public history of GitHub user GiaT75, Gia Tan, which goes all the way back to 2021.
[295.88 --> 302.42]  Tan starts slowly, then ramps up as he gains trust alongside a few other accounts that appear to be sock puppets.
[302.42 --> 308.90]  Evan tried to use the other public information to identify who Gia Tan really is, but a potential LinkedIn match
[308.90 --> 310.88]  seems unlikely. Quote,
[311.10 --> 315.72]  I have received a few emails alerting me to a LinkedIn of somebody named Gia Tan 2.
[315.98 --> 321.24]  Their bio boasts of large-scale vulnerability management. They claim to live in California. Is this our man?
[321.52 --> 328.54]  The commits on Gia T75's GitHub are set to plus 800, which would not indicate presence in California.
[329.04 --> 331.50]  UTC minus 800 would be California.
[331.50 --> 336.92]  Most of the commits were made between UTC 12 to 17, which is awfully early for California.
[337.36 --> 342.52]  In my opinion, there is no sufficient evidence that the LinkedIn being discussed is our man.
[342.76 --> 343.08]  End quote.
[343.52 --> 347.96]  Analysis of the name has also been performed, but when you include the middle name,
[348.22 --> 352.72]  CHANG, that was found in one Git log, it seems unlikely that it's a real name.
[352.92 --> 353.68]  Evan says, quote,
[353.68 --> 353.70]  Quote,
[353.78 --> 358.38]  It's most likely our actor simply mashed plausible-sounding Chinese names together.
[358.60 --> 358.96]  End quote.
[359.42 --> 363.34]  As of the time of this recording, it's unknown who Gia Tan really is.
[363.70 --> 364.82]  The Pattern
[364.82 --> 370.64]  Rob Menching lays out the process of the attack and focuses in on step zero.
[370.98 --> 371.28]  Quote,
[371.28 --> 371.38]  Quote,
[371.38 --> 375.44]  Original maintainer burns out and only the attacker offers to help.
[375.78 --> 379.42]  So attacker inherits trust built up by the original maintainer.
[379.56 --> 379.96]  End quote.
[380.48 --> 386.80]  Somebody found an email thread that captured the individual messages sent when step zero was taking place.
[386.92 --> 391.68]  And Rob goes through and picks out salient messages to paint a picture for us.
[392.02 --> 392.34]  Quote,
[392.34 --> 396.50]  First, we start with a reasonable request asked reasonably.
[396.92 --> 400.00]  The question forces the maintainer to address his, quote, failings.
[400.30 --> 406.42]  I use, quote, failings in quotes here because, A, the maintainer doesn't actually owe anything here,
[406.62 --> 410.46]  so he hasn't actually failed, and, B, I know exactly how this feels.
[410.68 --> 413.68]  It feels terrible to let down your, quote, community.
[413.92 --> 415.22]  The question asked was,
[415.44 --> 417.50]  Is XZ for Java still maintained?
[417.80 --> 421.52]  I asked a question here a week ago and have not heard back.
[421.52 --> 425.64]  The maintainer acknowledges he's, quote, behind and is struggling to keep up.
[425.90 --> 427.40]  This is a cry in pain.
[427.74 --> 428.94]  This is a cry for help.
[429.20 --> 431.70]  Help will not be coming in this thread.
[432.02 --> 432.38]  End quote.
[433.00 --> 436.16]  The question quoted doesn't originate from Giatan.
[436.44 --> 441.82]  Instead, its author eventually points to Giatan as a good person to, quote,
[441.92 --> 443.38]  have a bigger role in the future.
[444.00 --> 447.28]  How many of us find ourselves in positions similar to Lassie?
[447.46 --> 451.36]  I've spoken with so many maintainers who would love to pass their project on to
[451.36 --> 454.58]  someone capable and interested, but is darn near impossible.
[454.94 --> 456.26]  Rob closes with this.
[456.68 --> 459.14]  It takes skill and knowledge to write software.
[459.58 --> 462.02]  And while many skills and some knowledge will transfer,
[462.38 --> 467.44]  working on a new software project inevitably requires developing new skills and more knowledge.
[467.86 --> 471.90]  Software developers are not fungible cogs that you can swap in and out at will.
[471.90 --> 477.78]  The email thread ends with the complaining consumers offering no help while continuing to make demands.
[478.18 --> 479.80]  Only the attacker is left.
[479.80 --> 481.14]  The debate.
[481.34 --> 486.32]  In the wake of this event, many voices have called out the unhealthy relationship between
[486.32 --> 489.86]  unpaid maintainers and companies that benefit from their work.
[490.20 --> 491.00]  And don't get me wrong.
[491.28 --> 493.84]  Yes, that absolutely is a problem.
[494.08 --> 499.30]  But Substack writer LeCamtuff wrote up a different take that I haven't heard previously
[499.30 --> 501.88]  that I absolutely believe plays a part.
[502.12 --> 502.86]  They say, quote,
[502.86 --> 509.14]  The real issue with a lot of small foundational OSS libraries is just that there isn't enough to do.
[509.48 --> 511.58]  They were written decades ago by a single person.
[511.86 --> 515.42]  And beyond bug fixes, they are not really supposed to change that much.
[515.72 --> 519.96]  You don't do major facelifts of Zlib or Giflib every year.
[520.22 --> 525.40]  Even if you wave some cash around, it's hard to build a sustainable community around watching paint dry.
[525.40 --> 528.88]  After a while, the maintainer just isn't all that into it anymore.
[529.10 --> 533.92]  They are eager to pass the baton to anyone with a pulse and some modicum of skill.
[534.24 --> 534.60]  End quote.
[534.94 --> 542.66]  Unfortunately, sometimes that person with a pulse and some modicum of skill is a highly competent, malicious actor.
[543.26 --> 543.62]  Quote,
[543.62 --> 568.20]  That's the news for now.
[568.20 --> 571.84]  But scan this episode's companion newsletter, link in the show notes,
[572.06 --> 579.38]  for more commentary on the XZbackdoor O and 13 other interesting links that are completely unrelated.
[579.80 --> 580.64]  Have a great week.
[580.82 --> 582.76]  Leave us a five-star review if you dig it.
[582.88 --> 584.34]  And I'll talk to you again real soon.

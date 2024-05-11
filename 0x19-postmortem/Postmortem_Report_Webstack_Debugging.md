Postmortem Report

Incident Report: The Great Website Meltdown of September 11th, 2018

Summary:
On the infamous night of September 11th, 2018, our server experienced a meltdown of epic proportions, resulting in a 504 error for anyone daring to visit our beloved website. It was as if the digital universe decided to play a cruel joke on us, plunging our site into darkness.

Timeline:

00:00 PST: The chaos ensued as users encountered the dreaded 504 error, sending panic rippling through cyberspace.
00:05 PST: Like fearless cyber-sleuths, our engineers swiftly verified that Apache and MySQL were still clinging to life.
00:10 PST: Despite their valiant efforts, our intrepid team discovered that while the server and database were alive and kicking, the website itself was playing hard to get.
00:12 PST: In a desperate bid to coax the website back to life, a daring Apache server restart was performed, offering a glimmer of hope.
00:18 PST: Armed with nothing but their wits and a cup of coffee, our engineers delved into the murky depths of error logs, hoping to uncover the source of the chaos.
00:25 PST: Lo and behold, the error logs revealed a diabolical plot: premature shutdowns of the Apache server, with PHP error logs missing, as if they vanished into thin air.
00:30 PST: After navigating through the treacherous labyrinth of configuration files, our heroes discovered the culprit: error logging had been disabled, leaving them in the dark.
00:32 PST: With error logging resurrected from its digital grave, the true villain was unmasked—a mistyped file name lurking in the shadows of wp-settings.php.
00:36 PST: Armed with the power of correct spelling, our valiant engineers vanquished the typo and restarted the Apache server, restoring peace to the digital realm.
00:40 PST: Order was restored, and the website emerged from the darkness, ready to greet visitors once more.
Root Cause and Resolution:
The nefarious villain behind the outage was none other than a mistyped file name, lurking in the shadows of wp-settings.php like a silent assassin. With error logging disabled, our heroes faced an uphill battle, but through perseverance and sheer determination, they emerged victorious. By correcting the typo and enabling error logging, the website was resurrected from its digital slumber, ready to face whatever challenges the digital frontier had in store.

Corrective and Preventive Measures:

Enable Error Logging: Like a vigilant sentinel, ensure that error logging is always enabled to catch mischievous typos and lurking gremlins before they wreak havoc.
Local Testing: Before unleashing our creations upon the world, let us first subject them to the rigors of local testing, sparing us from the embarrassment of public failures.


django-tsuchi
=============

Copyright
---------

Copyright (c) 2012 John Weaver

See LICENSE file.


These are the problems that this app solves
-------------------------------------------

Activities, both by other users (such as actions resulting in new items in
followed activity streams) and by asynchronous background tasks should have
the ability to send notifications to users without having their browser poll
for new items or task statuses. While for some notifications email is
appropriate, having on-site real time notifications encourages users to
stay on the site. Some users don't like email notifications, or prefer
digests of activity.


What I intend for this app to provide
-------------------------------------

* A simple API for sending notifications targeted to a user, without
  needing an open request instance.

* Support for translating notification strings for the user.

* Users can enable email notifications either as instant emails, or a daily or
  weekly digest.

* Uses Pusher to send notifications to users, and provides Javascript to
  receive notifications and render them.

* Provides Javascript to enable HTML5 notifications if available, otherwise
  falls back to HTML inserted into the DOM.

* Developers can inject the notification Javascript into their templates
  with a template tag. The channel and use of HTML5 notifications can be
  overridden with parameters to this tag.

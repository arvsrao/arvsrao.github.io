# arvsrao.github.io


### Develop Locally

Run the following command to generate the site, including drafts ( `-D`), and serve it locally.

```bash
bundle exec jekyl serve -D
```

### Replace the Favicon (the short icon)

The *favicon* is a tiny picture that appears to the left of the website title in the browser tab. If you want to replace it do the following:

1. Search on [flaticon](https://www.flaticon.com/icons) for a replacement. 

2. Download a 512 x 512 `png` format version of the desired icon.

3. Find a favicon generator online, and generate favicon images from the `png` image. 

4. unzip the favicon folder and rename it with a descriptive name. 

5. move the renamed favicon folder to `/public/favicon/`. For example `/public/favicon/tetris`.

6. Finally, edit the icon links in `_includes/head.html`.

   ```HTML
   <!-- Icons -->
       <link rel="android-chrome-512x512" type="image/png" sizes="512x512" href="/public/favicon/tetris/android-chrome-512x512.png">
       <link rel="android-chrome-192x192" type="image/png" sizes="192x192" href="/public/favicon/tetris/android-chrome-192x192.png">
       <link rel="apple-touch-icon" type="image/png" sizes="180x180" href="/public/favicon/tetris/apple-touch-icon.png">
       <link rel="shortcut icon" type="image/x-icon" href="/public/favicon/tetris/favicon.ico">
   ```



[1]: https://www.moncefbelyamani.com/how-to-install-xcode-homebrew-git-rvm-ruby-on-mac/?utm_source=stackoverflow

import os
import sys
import datetime
import asyncio
import requests
import threading
from bs4 import BeautifulSoup
from hunter_style import *

def conectar(site):
  global verifica
  sessions = requests.Session()
  verifica = sessions.get(site,timeout=60)
async def sites_urls(name=False,armaz=False):
  Found = False
  tamanho = []
  accepts = []
  perfis = {}
  Base_Sites = {'TikTok': 'https://www.tiktok.com/@{}'.format(name),
      'X/Twitter': 'https://x.com/{}/'.format(name),
      'Vk': 'https://vk.com/{}'.format(name),
      'Vsco': 'https://vsco.co/{}/gallery'.format(name),
      'Telegram': 'https://t.me/{}'.format(name),
      'PicPay': 'https://app.picpay.com/user/{}'.format(name),
      'Intigriti': 'https://app.intigriti.com/profile/{}'.format(name),
      'Intigriti-2': 'https://api.intigriti.com/user/public/profile/{}'.format(name),
      'ItemFlix': 'https://www.itemfix.com/c/{}'.format(name),
      'Linktree': 'https://linktr.ee/{}'.format(name),
      'Listed': 'https://listed.to/@{}'.format(name),
      'Fórum-MMORPG': 'https://forums.mmorpg.com/profile/{}'.format(name),
      'Minecraft': 'https://api.mojang.com/users/profiles/minecraft/{}'.format(name),
      'MonkeyType': 'https://monkeytype.com/profile/{}'.format(name),
      'MonkeyType-API': 'https://api.monkeytype.com/users/{}/profile'.format(name),
      'Motorrad': 'https://motherless.com/m/{}'.format(name),
      'Needrom': 'https://www.needrom.com/author/{}/'.format(name),
      'Nitendo': 'https://www.nintendolife.com/users/{}'.format(name),
      'PasteBin': 'https://pastebin.com/u/{}'.format(name),
      'Patreon': 'https://www.patreon.com/{}'.format(name),
      'PinkBike': 'https://www.pinkbike.com/u/{}/'.format(name),
      'PokemonShow': 'https://pokemonshowdown.com/users/{}'.format(name),
      'Poligon': 'https://www.polygon.com/users/{}'.format(name),
      'ProductHunt': 'https://www.producthunt.com/@{}'.format(name),
      'Redbubble': 'https://www.redbubble.com/people/{}'.format(name),
      'Replit': 'https://replit.com/@{}'.format(name),
      'Roblox': 'https://www.roblox.com/user.aspx?username={}'.format(name),
      'Shitpostbot': 'https://www.shitpostbot.com/user/{}'.format(name),
      'Slack.com': 'https://{}.slack.com'.format(name),
      'Speedrun': 'https://speedrun.com/user/{}'.format(name),
      'Sports':  'https://www.sportlerfrage.net/nutzer/{}'.format(name),
      'Fórum Sublime': 'https://forum.sublimetext.com/u/{}'.format(name),
      'TnaFlix': 'https://www.tnaflix.com/profile/{}'.format(name),
      'VirusTotal_1': 'https://www.virustotal.com/gui/user/{}'.format(name),
      'VirusTotal_2': 'https://www.virustotal.com/ui/users/{}/avatar'.format(name),
      'Wikipédia': 'https://en.wikipedia.org/wiki/Special:CentralAuth/{}?uselang=qqx'.format(name),
      'Windy': 'https://community.windy.com/user/{}'.format(name),
      'Wix': 'https://{}.wix.com'.format(name),
      'Wordpress': 'https://{}.wordpress.com/'.format(name),
      'Xbox': 'https://xboxgamertag.com/search/{}'.format(name),
      'You Know': 'https://www.younow.com/{}/'.format(name),
      'Chaos': 'https://chaos.social/@{}'.format(name),
      'Privacy': 'https://privacy.com/{}'.format(name),
      'OnlyFans': 'https://onlyfans.com/Profile/{}'.format(name),
      'CameraPrive': 'https://cameraprive.com/br/{}'.format(name),
      'Xvideos': 'https://www.xvideos.com/profiles/{}'.format(name),
      'Xnxx': 'https://www.xnxx.com/profile/{}'.format(name),
      'Pornhub-stars': 'https://www.pornhub.com/pornstar/{}'.format(name),
      'Pornhub-users': 'https://www.pornhub.com/users/{}'.format(name),
      'Pornhub-models': 'https://www.pornhub.com/model/{}'.format(name),
      'Pornhub-espanhol': 'https://es.pornhub.com/model/{}'.format(name),
      'D3': 'https://d3.ru/user/{}/posts'.format(name),
      'Hunting': 'https://www.hunting.ru/forum/members/?username={}'.format(name),
      'Jeux': 'https://www.jeuxvideo.com/profil/{}'.format(name),
      'Open.net': 'https://www.opennet.ru/~{}'.format(name),
      'Prog': 'https://prog.hu/azonosito/info/{}'.format(name),
      'Social.de': 'https://social.tchncs.de/@{}'.format(name),
      'Toster': 'https://www.toster.ru/user/{}/answers'.format(name),
      'Uid.me': 'http://uid.me/{}'.format(name),
      'Znanylekarz': 'https://www.znanylekarz.pl/{}'.format(name),
      'Chess': 'https://www.chess.com/member/{}'.format(name),
      'PornoRoulette': 'https://cams.pornoroulette.com/{}'.format(name),
      'Chatujme': 'https://profil.chatujme.cz/{}'.format(name),
      'Instagram': 'https://www.instagram.com/{}'.format(name),
      'Codeberg.org': 'https://codeberg.org/{}'.format(name),
      'Codechefe': 'https://www.codecademy.com/profiles/{}'.format(name),
      'Clubhouse': 'https://www.clubhouse.com/@{}'.format(name),
      'Clozemaster': 'https://www.clozemaster.com/players/{}'.format(name),
      'CloudFlare': 'https://community.cloudflare.com/u/{}'.format(name),
      'Clapperapp': 'https://clapperapp.com/{}'.format(name),
      'Codersrank': 'https://profile.codersrank.io/user/{}/'.format(name),
      'Coinvote': 'https://coinvote.cc/profile/{}'.format(name),
      'Contently': 'https://{}.contently.com/'.format(name),
      'Cracked': 'https://www.cracked.com/members/{}/'.format(name),
      'Crevado': 'https://{}.crevado.com'.format(name),
      'Cults3d': 'https://cults3d.com/en/users/{}/creations'.format(name),
      'CyberDefender': 'https://cyberdefenders.org/p/{}'.format(name),
      'Dev': 'https://dev.to/{}'.format(name),
      'DailyMotion': 'https://www.dailymotion.com/{}'.format(name),
      'Dealabs': 'https://www.dealabs.com/profile/{}'.format(name),
      'Discogs': 'https://www.discogs.com/user/{}'.format(name),
      'Discord': 'https://discord.com/users/{}'.format(name),
      'HubDocker': 'https://hub.docker.com/u/{}/'.format(name),
      'HubDocker-alias': 'https://hub.docker.com/v2/users/{}/'.format(name),
      'Envato-Fórum': 'https://forums.envato.com/u/{}'.format(name),
      'Fanpop': 'https://www.fanpop.com/fans/{}'.format(name),
      'Fliver': 'https://www.fiverr.com/{}'.format(name),
      'FlightRadar': 'https://my.flightradar24.com/{}'.format(name),
      'Rusfootball': 'https://www.rusfootball.info/user/{}/'.format(name),
      'Forumphilia': 'https://www.forumophilia.com/profile.php?mode=viewprofile&u={}'.format(name),
      'Fosstodon': 'https://fosstodon.org/@{}'.format(name),
      'Freesound': 'https://freesound.org/people/{}/'.format(name),
      'Gaionline': 'https://www.gaiaonline.com/profiles/{}'.format(name),
      'Gamespot': 'https://www.gamespot.com/profile/{}/'.format(name),
      'GeekForGeeks': 'https://auth.geeksforgeeks.org/user/{}'.format(name),
      'Genius-Artists': 'https://genius.com/artists/{}'.format(name),
      'Genius-users': 'https://genius.com/{}'.format(name),
      'GiantBomb': 'https://www.giantbomb.com/profile/{}/'.format(name),
      'Gitea': 'https://gitea.com/{}'.format(name),
      'Gitee': 'https://gitee.com/{}'.format(name),
      'Google-Play': 'https://play.google.com/store/apps/developer?id={}'.format(name),
      'HackDay': 'https://hackaday.io/{}'.format(name),
      'HackerOne': 'https://hackerone.com/{}'.format(name),
      'Harvard': 'https://scholar.harvard.edu/{}'.format(name),
      'Holopin': 'https://holopin.io/@{}'.format(name),
      'HubPage': 'https://hubpages.com/@{}'.format(name),
      'Galeria': 'https://irc-galleria.net/users/search?username={}'.format(name),
      'Imgur': 'https://imgur.com/user/{}'.format(name),
      'Imgur2': 'https://api.imgur.com/account/v1/accounts/{}?client_id=546c25a59c58ad7'.format(name),
      'Reddit': 'https://www.reddit.com/user/{}'.format(name),
      'Medium': 'https://medium.com/@{}'.format(name),
      'Facebook': 'https://www.facebook.com/{}'.format(name),
      'GitHub': 'https://github.com/{}'.format(name),
      'Snapchat': 'https://www.snapchat.com/add/{}'.format(name),
      'WeChat': 'https://weixin.qq.com/u/{}'.format(name),
      'LinkedIn': 'https://www.linkedin.com/in/{}'.format(name),
      'Skype': 'https://join.skype.com/invite/{}'.format(name),
      'Spotify': 'https://open.spotify.com/user/{}'.format(name),
      'Pinterest': 'https://www.pinterest.com/{}/'.format(name),
      'YouTube': 'https://www.youtube.com/{}'.format(name),
      'Twitch': 'https://www.twitch.tv/{}'.format(name),
      'FreeCodeCamp': 'https://www.freecodecamp.org/{}'.format(name),
      'TryHackMe': 'https://tryhackme.com/p/{}'.format(name),
      'Freelancer': 'https://www.freelancer.com/u/{}'.format(name),
      'FreelancerBR': 'https://www.freelancer.com.br/u/{}'.format(name),
      'GitLab': 'https://gitlab.com/{}'.format(name),
      'Archive.org': 'https://archive.org/details/@{}'.format(name),
      'Pr0gramm': 'https://pr0gramm.com/user/{}'.format(name),
      'Fandom': 'https://www.fandom.com/wiki/User:{}'.format(name),
      'Interpals': 'https://www.interpals.net/{}'.format(name),
      'PSNProfiles': 'https://psnprofiles.com/{}'.format(name),
      'About.me': 'https://about.me/{}'.format(name),
      'PyPI': 'https://pypi.org/user/{}'.format(name),
      'Tumblr': 'https://{}.tumblr.com/'.format(name),
      '9GAG': 'https://9gag.com/u/{}'.format(name),
      'Flickr': 'https://www.flickr.com/people/{}'.format(name),
      'YouPic': 'https://youpic.com/photographer/{}'.format(name),
      'MyAnimeList': 'https://myanimelist.net/profile/{}'.format(name),
      'Wattpad': 'https://www.wattpad.com/user/{}'.format(name),
      'MySpace': 'https://myspace.com/{}'.format(name),
      'Passes': 'https://passes.com/{}'.format(name),
      'Disqus': 'https://disqus.com/by/{}'.format(name),
      'Threads': 'https://threads.net/{}'.format(name),
      'XHamster': 'https://xhamster.com/users/{}'.format(name),
      'Sharesome': 'https://sharesome.com/{}'.format(name),
      'YouPorn': 'https://youporn.com/users/{}'.format(name),
      'Chaturbate': 'https://chaturbate.com/{}'.format(name),
      'BongaCams': 'https://pt.bongacams.com/profile/{}'.format(name),
      'Tinder': 'https://tinder.com/@{}'.format(name),
      'LiveJasmin': 'https://livejasmin.com/{}'.format(name),
      '7 Cups': 'https://www.7cups.com/{}'.format(name),
      'Apclips': 'https://apclips.com/{}'.format(name),
      'AdmireMe': 'https://admireme.vip/{}'.format(name),
      'Airbit': 'https://airbit.com/{}'.format(name),
      'AllMyLinks': 'https://allmylinks.com/{}'.format(name),
      'AllThingsWorn': 'https://www.allthingsworn.com/{}'.format(name),
      'AniWorld': 'https://aniworld.to/{}'.format(name),
      'AniList': 'https://anilist.co/{}'.format(name),
      'ArtStation': 'https://www.artstation.com/{}'.format(name),
      'Blipfoto': 'https://www.blipfoto.com/{}'.format(name),
      'Blogger': 'https://www.blogger.com/{}'.format(name),
      'RedTube': 'https://www.redtube.com.br/{}'.format(name),
      'RoyalCams': 'https://pt.royalcams.com/{}'.format(name),
      'Shpock': 'https://www.shpock.com/{}'.format(name),
      'Scribd': 'https://pt.scribd.com/{}'.format(name),
      'Scratch': 'https://scratch.mit.edu/{}'.format(name),
      'ImgSrc': 'https://imgsrc.ru/{}'.format(name),
      'MercadoLivre': 'https://www.mercadolivre.com.br/{}'.format(name),
      'Note': 'https://note.com/{}'.format(name),
      'PicsArt': 'https://picsart.com/{}'.format(name),
      'Cont.ws': 'https://cont.ws/@{}'.format(name),
      'Estante Virtual': 'https://www.estantevirtual.com.br/busca?editora={}'.format(name),
      'Kwai': 'https://www.kwai.com/@{}'.format(name),
      'Disqus': 'https://disqus.com/by/{}/?'.format(name),
      'Hack This Site': 'https://www.hackthissite.org/user/view/{}'.format(name),
      'Duolingo': 'https://www.duolingo.com/profile/{}'.format(name),
      'Hentai City': 'https://www.hentaicity.com/profile/{}'.format(name),
      'Strip Chat': 'https://stripchat.com/user/{}'.format(name),
      'Ifunnny': 'https://br.ifunny.co/user/{}'.format(name),
      'Itch': 'https://itch.io/profile/{}'.format(name),
      'Etsy': 'https://www.etsy.com/pt/people/{}?ref=l_review'.format(name),
      'Ludopedia': 'https://ludopedia.com.br/usuario/{}'.format(name),
      'Viva o Linux': 'https://www.vivaolinux.com.br/~{}'.format(name),
      'Cursos Alura': 'https://cursos.alura.com.br/user/{}'.format(name),
      'Guj': 'https://www.guj.com.br/u/{}/summary'.format(name),
      'Mk Auth': 'https://mk-auth.com.br/members/{}'.format(name),
      'Forum Elipse': 'https://forum.elipse.com.br/u/{}/summary'.format(name),
      'Home Assistent': 'https://homeassistantbrasil.com.br/u/{}/summary'.format(name),
      'Endian Eth0': 'https://endian.eth0.com.br/forums/profile/{}'.format(name),
      'Vakinha': 'https://www.vakinha.com.br/usuario/{}'.format(name),
      'Mastodon': 'https://mastodon.social/@{}'.format(name),
      'Anime Planet': 'https://www.anime-planet.com/users/{}'.format(name),
      'Bsky': 'https://bsky.app/profile/{}.bsky.social'.format(name),
      'Live Journal': 'https://{}.livejournal.com/'.format(name),
      'Deviantart': 'https://www.deviantart.com/{}/gallery'.format(name),
      'Last': 'https://www.last.fm/pt/user/{}'.format(name),
      'Veoh': 'https://www.veoh.com/users/{}'.format(name),
      'Behance': 'https://www.behance.net/{}'.format(name),
      'Tripadvisor': 'https://www.tripadvisor.com.br/Profile/{}'.format(name),
      'Polyvore': 'https://polyvore.ch/author/{}/'.format(name),
      'Kongregate': 'https://www.kongregate.com/accounts/{}'.format(name),
      'Beebom': 'https://beebom.com/author/{}/'.format(name),
      'Wikihow': 'https://www.wikihow.com/Author/{}'.format(name),
      'Laptopmag': 'https://www.laptopmag.com/uk/author/{}'.format(name),
      'Flip Board': 'https://flipboard.com/@{}'.format(name),
      'Hackr': 'https://hackr.io/blog/author/{}'.format(name),
      'Clean': 'https://clean.email/authors/{}'.format(name),
      'Gravatar': 'https://gravatar.com/{}'.format(name),
      'Dio': 'https://www.dio.me/users/{}'.format(name),
      'Sex HD': 'https://www.sexhd.pics/mobile/{}'.format(name),
      'Blog Bang': 'https://blog.bang.com/author/{}'.format(name),
      'Bang': 'https://www.bang.com/videos?term={}'.format(name),
      'Eplay': 'https://www.eplay.com/{}'.format(name),
      'Eporner': 'https://www.eporner.com/profile/{}'.format(name),
      'Eyeem': 'https://www.eyeem.com/u/{}'.format(name),
      'Dribbble': 'https://dribbble.com/{}'.format(name),
      'Members Fotki': 'https://members.fotki.com/{}/about'.format(name),
      'eyeem': 'https://br.eyeem.com/bee/{}'.format(name),
      'Sound Cloud': 'https://soundcloud.com/{}'.format(name),
      'Weibo': 'https://www.weibo.com/{}'.format(name),
      'Kiwi Box': 'https://www.kiwibox.com/author/{}'.format(name),
      'Forums Opera': 'https://forums.opera.com/user/{}'.format(name),
      'Revista Forum': 'https://revistaforum.com.br/autor/{}.html'.format(name),
      'Viex Americanas': 'https://www.viex-americas.com/{}'.format(name),
      'Community Kobotoolbox': 'https://community.kobotoolbox.org/u/{}/summary'.format(name),
      'Forum Asana': 'https://forum.asana.com/u/{}/summary'.format(name),
      'UFBA Academia': 'https://ufba.academia.edu/{}'.format(name),
      'Community': 'https://community.auth0.com/u/{}/summary'.format(name),
      'Marautomation': 'https://www.marautomation.com/blog/author/{}'.format(name),
      'Social Bund': 'https://social.bund.de/@{}'.format(name),
      'CurseForge': 'https://www.curseforge.com/members/{}/projects'.format(name),
      'Hatrick Sport': 'https://www.hatricksport.net/author/{}'.format(name),
      'Pikabu': 'https://pikabu.ru/@{}'.format(name),
      'Amino': 'https://aminoapps.com/u/{}'.format(name),
      'Bikemap': 'https://www.bikemap.net/en/u/{}/routes/created/'.format(name),
      'HackTheBox': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'Vero': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'BabyRU': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'Strava': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'NitroType': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'Linchess': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'LibraryThings': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'Kick': 'https://forum.hackthebox.eu/profile/{}'.format(name),
      'HudsonRock': 'https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-username?username={}'.format(name),
      'Houzz': 'https://houzz.com/user/{}'.format(name),
      'HackenProof': 'https://hackenproof.com/hackers/{}'.format(name),
      'Fiverr': 'https://www.fiverr.com/{}'.format(name),
      '1337x.io': 'https://www.1337x.to/user/{}/'.format(name),
      '2Dimensions': 'https://2Dimensions.com/a/{}'.format(name),
      '3Dnews Fórum': 'http://forum.3dnews.ru/member.php?username={}'.format(name),
      '7Cups': 'https://www.7cups.com/@{}'.format(name),
      '8Tracks': 'https://8tracks.com/{}'.format(name),
      'Airlinepilot.life': 'https://airlinepilot.life/u/{}'.format(name),
      'Airliners.net': 'https://www.airliners.net/user/{}/profile/photos'.format(name),
      'Discussions.apple': 'https://discussions.apple.com/profile/{}'.format(name),
      'Developer.apple': 'https://developer.apple.com/forums/profile/{}'.format(name),
      'Asciinema.org': 'https://asciinema.org/~{}'.format(name),
      'Ask.fedoraproject': 'https://ask.fedoraproject.org/u/{}'.format(name),
      'Audiojungle':'https://audiojungle.net/user/{}'.format(name),
      'Autofrage': 'https://www.autofrage.net/nutzer/{}'.format(name),
      'Aviso.cz': 'https://www.avizo.cz/{}/'.format(name),
      'Blip.fm': 'https://blip.fm/{}'.format(name),
      'BandCamp': 'https://www.bandcamp.com/{}',
      'Bazar.cz': 'https://www.bazar.cz/{}/'.format(name),
      'Bezuzyteczna.pl': 'https://bezuzyteczna.pl/uzytkownicy/{}'.format(name),
      'Biggerpockets': 'https://www.biggerpockets.com/users/{}'.format(name),
      'Forum.Dangerous': 'https://forum.dangerousthings.com/u/{}'.format(name),
      'Bitbucket': 'https://bitbucket.org/{}/'.format(name),
      'Blogspot': 'https://{}.blogspot.com'.format(name),
      'Bodyspace': 'https://bodyspace.bodybuilding.com/{}'.format(name),
      'BookCrossing': 'https://www.bookcrossing.com/mybookshelf/{}/'.format(name),
      'Community-Brave': 'https://community.brave.com/u/{}/'.format(name),
      'Bugcrowd': 'https://bugcrowd.com/{}'.format(name),
      'Buy-me A Coffe': 'https://buymeacoff.ee/{}'.format(name),
      'Buzzfeed': 'https://buzzfeed.com/{}'.format(name),
      'Cgtrader':'https://www.cgtrader.com/{}'.format(name),
      'Cnet': 'https://www.cnet.com/profiles/{}/'.format(name),
      'CssBatle': 'https://cssbattle.dev/player/{}'.format(name),
      'Ctan.org': 'https://ctan.org/author/{}'.format(name),
      'CarbonMade': 'https://{}.carbonmade.com'.format(name),
      'Carrer': 'https://career.habr.com/{}'.format(name),
      'Championat': 'https://www.championat.com/user/{}'.format(name),
      'StripChat': 'https://pt.stripchat.com/{}/profile'.format(name)}
  os.system("cls")
  start = datetime.datetime.now()
  Baner()
  print("""
      \033[1;31m#################################################\033[m
          Buscando pelo usuário --> \033[1;32m{}\033[m
      \033[1;31m#################################################\033[m\n""".format(name))
  print("\033[1;33mProcurando por contas com esse usuário...\033[m")
  for site,links in Base_Sites.items():
    tamanho.append(links)
  for url,sites in Base_Sites.items():
      try:
        verificar = threading.Thread(target=conectar(site=sites))
        verificar.start()
        verificar.join()
      except KeyboardInterrupt:
        raise SystemExit
      except:
        pass
      else:
        if verifica.status_code == 200:
          try:
            resultado = BeautifulSoup(verifica.content,"html.parser")
            if url == "Instagram":
              if resultado.find("meta",{"property":"og:title"}):
                print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
                perfis[url] = sites
                Found = True
                accepts.append(sites)
            elif url == "Telegram":
              if f"Telegram:Contact@{name}DownloadIfyouhaveTelegram,youcancontact@{name}rightaway.SendMessage" in resultado.get_text().replace(" ","").replace("\n",""):
                pass
              else:
                print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
                perfis[url] = sites
                Found = True
                accepts.append(sites)
            elif url == "Reddit":
              if "nobodyonRedditgoesbythatname" in resultado.get_text().replace(" ","").replace("\n",""):
                pass
              else:
                print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
                perfis[url] = sites
                Found = True
                accepts.append(sites)
            elif url == "Bang":
              if "0results" in resultado.get_text().replace(" ","").replace("\n",""):
                pass
              else:
                print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
                perfis[url] = sites
                Found = True
                accepts.append(sites)
            elif url == "Wordpress":
              if f"Doyouwanttoregister{name}.wordpress.com" in resultado.get_text().replace(" ","").replace("\n",""):
                pass
              else:
                print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
                perfis[url] = sites
            elif name in resultado.get_text():
              print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1;32m {}:\033[m\033[1m {}\033[m".format(url,sites))
              perfis[url] = sites
              Found = True
              accepts.append(sites)
          except KeyboardInterrupt:
            raise SystemExit
  if armaz:
    for nome_site,url_site in perfis.items():
      with open("Perfis.txt","a") as save:
        save.write("{} tem conta no: {} link -> {}\n".format(name,nome_site,url_site))
      save.close()
    with open("Perfis.txt","a") as save2:
      save2.write("-----------------------------------\n\n")
    save2.close()
  fim = datetime.datetime.now() - start
  fim = datetime.datetime.now() - start

  print("\n\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[1;32m Urls escaneadas:\033[m [ {} ]".format(len(tamanho)))
  print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[1;32m Perfis encontrados:\033[m [ {} ]".format(len(accepts)))
  if Found:
    print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1m Tempo que levei para encontrar:\033[m\033[1;32m {}\033[m\n".format(fim))
  else:
    print("\033[1m[\033[m\033[1;32m+\033[m\033[1m]\033[m\033[1m Scan total: {} | Infelizmente não encontrei nada correspondente para o usuário {}:\033[m\n".format(fim,name))

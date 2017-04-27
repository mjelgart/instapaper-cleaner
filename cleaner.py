from instapaper import Instapaper as ipaper
import configparser



config = configparser.ConfigParser()
cleanercfg = config.read('instapaper-cleaner.cfg')


i = ipaper(cleanercfg['Instapaper OAuth]']['ID'], cleanercfg['Instapaper OAuth]']['Secret'])
i.login(cleanercfg['Instapaper Login']['email'], cleanercfg['Instapaper Login']['password'])




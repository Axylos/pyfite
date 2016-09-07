from errbot import BotPlugin, botcmd
from fitedb import db_api

class Errfite(BotPlugin):
  @botcmd
  def ping(self, message, args):
      return 'ping'

  @botcmd
  def get_pending_lists(self, message, args):
      return db_api.get_pending_lists()

import os
import pathlib

__all__ = ('BASE_DIR',)
# __all__ = ('BASE_DIR', 'DB_CONFIG')

BASE_DIR = pathlib.Path(__file__).parent.parent.absolute()

# DB_CONFIG = {
#     'connections': {
#         'default': {
#             'engine': 'tortoise.backend.asyncpg',
#             'credentials': {
#                 'host': os.getenv('PG_HOST'),
#                 'port': int(os.getenv('PG_PORT')),
#                 'user': 'a_net',
#                 'password': 'yulia123',
#                 'database': 'anet'
#             }
#         },
#     },
#     'apps': {
#         'user': {
#             'models': ['anet.api.user.models'],
#             'default_connection': 'default',
#         }
#     },
#     'use_tz': True,
#     'timezone': 'UTC'
# }


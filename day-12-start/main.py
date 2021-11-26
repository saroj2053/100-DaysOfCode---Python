# Namespaces Local vs Global Scope

# Local Scope
def coc_enemies():
    enemy = 5
    return enemy


num_of_enemies = coc_enemies()
print(num_of_enemies)

# Global SCope
player_health = 100


def apply_bandage(health_status=2):
    bandage_heath_gain = 90
    health_status += bandage_heath_gain
    print(health_status)

apply_bandage()
print(player_health)


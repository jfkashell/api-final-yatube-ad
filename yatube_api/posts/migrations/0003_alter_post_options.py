from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_group_alter_comment_id_alter_post_id_post_group_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-pub_date',)},
        ),
    ]

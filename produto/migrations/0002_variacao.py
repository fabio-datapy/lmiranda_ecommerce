# Generated by Django 4.2.15 on 2024-09-24 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Variacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(blank=True, max_length=50, null=True)),
                ("preco", models.FloatField()),
                ("preco_promocional", models.FloatField(default=0)),
                ("estoque", models.PositiveIntegerField(default=1)),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produto.produto",
                    ),
                ),
            ],
            options={
                "verbose_name": "Variação",
                "verbose_name_plural": "Variações",
            },
        ),
    ]

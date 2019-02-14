# Generated by Django 2.1.4 on 2019-01-25 13:16

from django.db import migrations, models
import django.db.models.deletion

from django.db import migrations, models

import webdjango.models.TranslationModel


def init_migrations(apps, schema_editor):
    from libs.core.cms.api.models.Page import Page
    from libs.core.cms.api.models.Block import Block
    from libs.core.cms.api.configs import CMSCoreConfig
    from webdjango.models.Core import CoreConfig, Website
    from webdjango.configs import CONFIG_HOME_PAGE, DEFAULT_FOOTER, DEFAULT_HEADER

    website = Website.objects.create(
        domain="http://localhost:4200/", code='default')

    header = Block.objects.create(
        title="Header", slug="header", content="<nav>Header</nav>")
    footer = Block.objects.create(
        title="Footer", slug="footer", content="<footer>Footer</footer>")

    page = Page.objects.create(
        title="Home", slug="Home", content="<h1>Hello World!</h1>", header=header, footer=footer)

    CoreConfig.write(CMSCoreConfig.GROUP_SLUG, {
        CONFIG_HOME_PAGE: page.pk, DEFAULT_FOOTER: footer.pk, DEFAULT_HEADER: header.pk}, website=website)


def insert_system_blocks(apps, schema_editor):

    from libs.core.cms.api.configs import CMSCoreConfig
    from libs.core.cms.api.models.Block import Block
    from libs.core.cms.api.models.Block import BlockClasses
    from webdjango.models.Core import CoreConfig, Website
    from webdjango.configs import DEFAULT_SIDEBAR, FOOTER_WIDGET_HOLDER_1, FOOTER_WIDGET_HOLDER_2, \
        FOOTER_WIDGET_HOLDER_3, FOOTER_WIDGET_HOLDER_4, FOOTER_WIDGET_HOLDER_5, LAYOUT_FULL_CONTENT, \
        LAYOUT_RIGHT_SIDEBAR, LAYOUT_LEFT_SIDEBAR, DEFAULT_SITE_TITLE, DEFAULT_TITLE_SEPARATOR, \
        DEFAULT_TITLE_PLACEHOLDER

    # Default Widgets holders:
    default_sidebar = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Default Sidebar",
        slug=DEFAULT_SIDEBAR,
        is_system=True,
        content=""""""
    )
    footer_wh_1 = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Footer Widgets 1",
        slug=FOOTER_WIDGET_HOLDER_1,
        is_system=True,
        content=""""""
    )
    footer_wh_2 = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Footer Widgets 2",
        slug=FOOTER_WIDGET_HOLDER_2,
        is_system=True,
        content=""""""
    )
    footer_wh_3 = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Footer Widgets 3",
        slug=FOOTER_WIDGET_HOLDER_3,
        is_system=True,
        content=""""""
    )
    footer_wh_4 = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Footer Widgets 4",
        slug=FOOTER_WIDGET_HOLDER_4,
        is_system=True,
        content=""""""
    )
    footer_wh_5 = Block.objects.create(
        block_class=BlockClasses.WIDGET_HOLDER,
        title="Footer Widgets 4",
        slug=FOOTER_WIDGET_HOLDER_5,
        is_system=True,
        content=""""""
    )

    # Default Layouts
    layout_full_content = Block.objects.create(
        block_class=BlockClasses.LAYOUT,
        title="Full Content",
        slug=LAYOUT_FULL_CONTENT,
        is_system=True,
        settings={'type': 'boxed'},
        content="""
                  <div class="row">
                    <div class="col p-0">
                      {{ content }}
                    </div>
                  </div>
                """
    ),
    layout_right_sidebar = Block.objects.create(
        block_class=BlockClasses.LAYOUT,
        title="Right Sidebar",
        slug=LAYOUT_RIGHT_SIDEBAR,
        is_system=True,
        settings={'type': 'boxed'},
        content="""
                  <div class="row">
                    <div class="col-12 col-md-8">
                      {{ content }}
                    </div>
                    <div class="col-12 col-md-4">
                        {{ default_sidebar }}
                    </div>
                  </div>
                """
    ),
    layout_left_sidebar = Block.objects.create(
        block_class=BlockClasses.LAYOUT,
        title="Left Sidebar",
        slug=LAYOUT_LEFT_SIDEBAR,
        is_system=True,
        settings={'type': 'boxed'},
        content="""
                  <div class="row">
                    <div class="col-12 col-md-4">
                        {{ default_sidebar }}
                    </div>
                    <div class="col-12 col-md-8">
                      {{ content }}
                    </div>
                  </div>
                """
    )

    header = Block.objects.filter(slug="header").update(
        block_class=BlockClasses.HEADER, is_system=True)
    footer = Block.objects.filter(slug="footer").update(
        block_class=BlockClasses.FOOTER, is_system=True)

    website = Website.objects.filter(code__exact='default').first()

    core_config = CoreConfig.read(CMSCoreConfig.GROUP_SLUG)
    core_config[DEFAULT_SITE_TITLE] = 'WDA'
    core_config[DEFAULT_TITLE_SEPARATOR] = '-'
    core_config[DEFAULT_TITLE_PLACEHOLDER] = '${title} ${title_separator} ${site_title}'

    CoreConfig.write(CMSCoreConfig.GROUP_SLUG, core_config, website=website)


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0008_page_layout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='categories',
            field=models.ManyToManyField(
                related_name='pages', to='cms.PageCategory'),
        ),
        migrations.AlterField(
            model_name='page',
            name='footer',
            field=models.ForeignKey(blank=True, default=None, null=True,
                                    on_delete=django.db.models.deletion.PROTECT, related_name='footers', to='cms.Block'),
        ),
        migrations.AlterField(
            model_name='page',
            name='header',
            field=models.ForeignKey(blank=True, default=None, null=True,
                                    on_delete=django.db.models.deletion.PROTECT, related_name='headers', to='cms.Block'),
        ),
        migrations.AlterField(
            model_name='page',
            name='tags',
            field=models.ManyToManyField(
                related_name='pages', to='cms.PageTag'),
        ),
        migrations.RunPython(init_migrations),
        migrations.RunPython(insert_system_blocks)
    ]

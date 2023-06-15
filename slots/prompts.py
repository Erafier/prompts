from pylon.core.tools import web, log  # pylint: disable=E0611,E0401

from tools import auth, theme  # pylint: disable=E0401


class Slot:  # pylint: disable=E1101,R0903

    @web.slot('prompts_content')
    @auth.decorators.check_slot(["models.prompts"],
                                access_denied_reply=theme.access_denied_part)
    def content(self, context, slot, payload):
        log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'content.html',
            )

    @web.slot('prompts_scripts')
    @auth.decorators.check_slot(["models.prompts"])
    def scripts(self, context, slot, payload):
        # log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'scripts.html',
            )

    @web.slot('prompts_styles')
    @auth.decorators.check_slot(["models.prompts"])
    def styles(self, context, slot, payload):
        # log.info('slot: [%s], payload: %s', slot, payload)
        with context.app.app_context():
            return self.descriptor.render_template(
                'styles.html',
            )

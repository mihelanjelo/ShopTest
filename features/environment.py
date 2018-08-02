# encoding=utf8
import logging
import uuid
import utils.basic_actions as ba
logger = logging.getLogger('logger')
list_of_failed_scenarios = []
list_of_passed_scenarios = []


def before_all(context):
    try:
        context.browser = context.config.userdata["browser"]
    except KeyError:
        raise AssertionError('Не выбран браузер!')
    context.browser_exe_path = context.config.userdata.get("executable_path")


def before_feature(context, feature):
    hdlr = logging.FileHandler('./reports/{feature}_{browser}.log'.format(feature=feature.name.replace(" ", "_"),
                                                                          browser=context.browser))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.INFO)

    context.execute_steps("""
    Given Open browser
    """)

    # print("\nВыполняются сценарии функции: {feature} {browser}".format(feature=feature.name,
    #                                                                    browser=browser))


def before_scenario(context, scenario):
    logger.info('Выполняется сценарий: {name} {browser}'.format(name=scenario.name, browser=context.browser))


def after_scenario(context, scenario):
    global browser
    if scenario.status == 'failed':
        logger.info('Сценарий "{name}" {browser} завершен с ошибкой\n\n'.format(name=scenario.name,
                                                                                browser=context.browser))
        list_of_failed_scenarios.append("{name}".format(name=scenario.name))
    else:
        logger.info('Сценарий "{name}" {browser} завершен успешно\n\n'.format(name=scenario.name,
                                                                              browser=context.browser))
        list_of_passed_scenarios.append("{name}".format(name=scenario.name))


def after_feature(context, feature):
    global browser
    logger.info("\nУспешно пройденные сценарии: {}".format(list_of_passed_scenarios) +
                "\nНеуспешно пройденные сценарии: {}".format(list_of_failed_scenarios) + "\n\n")

    if len(list_of_failed_scenarios) == 0 and len(list_of_passed_scenarios) > 0:
        # print("[УСПЕШНО] Завершены сценарии функции: {feature} {browser} ({success}/{all})".
        #       format(feature=feature.name, success=len(list_of_passed_scenarios),
        #              all=len(list_of_passed_scenarios), browser=browser))
        for completed_scenario in list_of_passed_scenarios:
            pass
            # print("   [+] {passed}".format(passed=completed_scenario))

    else:
        # print("[НЕУСПЕШНО] Завершены сценарии функции: {feature} {browser} ({success}/{all})".
        #       format(feature=feature.name, success=len(list_of_passed_scenarios), all=len(list_of_passed_scenarios)
        #                                                                               + len(
        #     list_of_failed_scenarios), browser=browser))
        for completed_scenario in list_of_passed_scenarios:
            print("   [+] {passed}".format(passed=completed_scenario))

        for completed_scenario in list_of_failed_scenarios:
            print("   [-] {failed}".format(failed=completed_scenario))
    # try:
    #     context.helper.quit()
    # except AttributeError:
    #     raise Exception(u'Браузер завис или отсутствует!!')


def before_step(context, step):
    logger.info('Выполняется шаг: {}'.format(step.name))


def after_step(context, step):
    if step.status == 'failed':
        event_id = uuid.uuid4()
        trace = step.error_message
        if not trace:
            trace = ''
        logger.error('(event_id={id})Обнаружен дефект при выполнении шага: "{step}"'
                     .format(step=step.name, id=event_id) + '\n' + trace)

        context.helper.driver.save_screenshot('./screenshots/{event_id}.png'.
                                              format(event_id=event_id))

        logger.info(ba.last_wanted_element_info)

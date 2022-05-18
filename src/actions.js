// Code borrowed from facond as example
// https://github.com/yourlabs/facond/blob/npm/src/facond/actions.js

/**
 * Apply a reversible action on the DOM if conditions apply, unapply otherwise.
 */
class Action {
    /**
     * @param conditions List of :js:cls:`Condition` objects
     */
    constructor(conditions) {
        this.conditions = conditions || []
    }

    /**
     * Call :js:meth:`apply()` if conditions validate, :js:meth:`unapply` otherwise.
     *
     * @param form :js:class:`Form` object to execute on.
     */
    execute(form) {
        let method = 'apply'

        for (var i=0; i<this.conditions.length; i++) {
            if (!this.conditions[i].validate(form)) {
                method = 'unapply'
                break
            }
        }

        log(this, '.', method, '(', this.field, ')')
        this[method](form)
    }
